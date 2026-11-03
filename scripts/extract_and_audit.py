#!/usr/bin/env python3
"""
Zero-dependency CV Text Extractor & ATS/AI Heuristic Pre-Auditor.

Usage:
    python3 scripts/extract_and_audit.py <cv_file_1> [<cv_file_2> ...]

Supports:
- .docx (native OpenXML parsing via standard library zipfile + xml.etree)
- .md, .txt, .html (standard library)
- .pdf (via pypdf/pdfplumber/pdftotext if available; advises agent to also use read_file)
"""

import html
import json
import os
import re
import shutil
import subprocess
import sys
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path
from typing import Dict, List, Tuple

WEAK_PATTERNS_EN = [
    r"\bresponsible for\b",
    r"\bduties included\b",
    r"\bhelped with\b",
    r"\bworked on\b",
    r"\bassisted in\b",
    r"\bparticipated in\b",
    r"\btasked with\b",
]

WEAK_PATTERNS_PL = [
    r"\bodpowiedzialn[ya] za\b",
    r"\bdo moich obowiązków\b",
    r"\bzajmował[ea]m się\b",
    r"\bwsparcie przy\b",
    r"\bbranie udziału w\b",
    r"\buczestniczenie w\b",
    r"\bpomoc w\b",
]

METRIC_REGEX = re.compile(
    r"(\b\d+(?:[.,]\d+)?\+?\s*(?:%|percent\b|proc\.|x\b|k\b|m\b|mln\b|tys\.|usd\b|eur\b|pln\b|gbp\b|\$|€|zł|hrs?\b|hours?\b|godz\.|days?\b|dni\b|wks?\b|weeks?\b|months?\b|mies\.|users?\b|klientów\b|osób\b|projects?\b|projektów\b|ms\b|s\b|min\b|rps\b|sla\b|stores?\b|apis?\b|services?\b|engineers?\b|markets?\b)|"
    r"(?:\$|€|PLN|USD|EUR|GBP)\s*\d+(?:[.,]\d+)?)",
    re.IGNORECASE,
)

YEAR_REGEX = re.compile(r"\b(19[89]\d|20[0-3]\d)\b")
EMAIL_REGEX = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
PHONE_REGEX = re.compile(r"(?:\+?\d{1,3}[\s-]?)?(?:\(?\d{2,3}\)?[\s-]?)?\d{3}[\s-]?\d{2,3}[\s-]?\d{2,4}")
LINKEDIN_REGEX = re.compile(r"linkedin\.com/in/[a-zA-Z0-9_-]+", re.IGNORECASE)
GITHUB_REGEX = re.compile(r"github\.com/[a-zA-Z0-9_-]+", re.IGNORECASE)


def extract_docx(path: Path) -> Tuple[str, Dict[str, bool]]:
    """Extract text from a .docx file and detect structural risks (tables, headers)."""
    paragraphs: List[str] = []
    diagnostics = {"has_tables": False, "has_header_footer_text": False}

    with zipfile.ZipFile(path, "r") as zf:
        namelist = zf.namelist()
        for name in namelist:
            if name.startswith("word/header") or name.startswith("word/footer"):
                xml_bytes = zf.read(name)
                root = ET.fromstring(xml_bytes)
                header_text = "".join(root.itertext()).strip()
                # Ignore simple page number fields in footers (e.g. "PAGE 1")
                if header_text and not re.fullmatch(
                    r"(?:PAGE|NUMPAGES|Strona|Page|\d+|\s|/|-|z|of)+",
                    header_text,
                    flags=re.IGNORECASE,
                ):
                    diagnostics["has_header_footer_text"] = True
                    paragraphs.append(f"[HEADER/FOOTER]: {header_text}")

        if "word/document.xml" in namelist:
            xml_bytes = zf.read("word/document.xml")
            root = ET.fromstring(xml_bytes)
            ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
            if root.findall(".//w:tbl", ns):
                diagnostics["has_tables"] = True

            for p in root.findall(".//w:p", ns):
                texts = [t.text for t in p.findall(".//w:t", ns) if t.text]
                line = "".join(texts).strip()
                if line:
                    paragraphs.append(line)

    return "\n".join(paragraphs), diagnostics


def extract_pdf(path: Path) -> str:
    """Attempt PDF text extraction via installed Python libraries or pdftotext."""
    try:
        import pypdf  # type: ignore

        reader = pypdf.PdfReader(str(path))
        return "\n".join(page.extract_text() or "" for page in reader.pages)
    except Exception:
        pass

    if shutil.which("pdftotext"):
        try:
            res = subprocess.run(
                ["pdftotext", "-layout", str(path), "-"],
                capture_output=True,
                text=True,
                check=True,
            )
            return res.stdout
        except Exception:
            pass

    return (
        "[INFO: Native PDF text extraction tool not found in Python/CLI. "
        "Please read this PDF directly using the agent's `read_file` tool.]"
    )


def extract_text(path: Path) -> Tuple[str, Dict[str, bool]]:
    suffix = path.suffix.lower()
    diagnostics = {"has_tables": False, "has_header_footer_text": False}

    if suffix == ".docx":
        return extract_docx(path)
    elif suffix == ".pdf":
        return extract_pdf(path), diagnostics
    elif suffix in {".html", ".htm"}:
        raw = path.read_text(encoding="utf-8", errors="replace")
        if "<table" in raw.lower():
            diagnostics["has_tables"] = True
        cleaned = re.sub(r"<[^>]+>", " ", raw)
        return html.unescape(cleaned), diagnostics
    else:
        return path.read_text(encoding="utf-8", errors="replace"), diagnostics


def audit_cv_text(text: str, diagnostics: Dict[str, bool]) -> Dict[str, object]:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    words = re.findall(r"\S+", text)

    # Identify experience bullet-like lines (excluding short Skill/Language key:value lines)
    explicit_bullets = [
        line
        for line in lines
        if line.startswith(("-", "*", "•", "–", "▪", "·"))
        and not re.match(r"^[-*•–▪·]\s+\*\*[^*]+:\*\*", line)
        and len(line.split()) >= 6
    ]
    bullet_lines = (
        explicit_bullets
        if explicit_bullets
        else [line for line in lines if len(line.split()) >= 10]
    )
    quantified_lines = [line for line in bullet_lines if METRIC_REGEX.search(line)]

    weak_hits: List[str] = []
    for pat in WEAK_PATTERNS_EN + WEAK_PATTERNS_PL:
        matches = re.findall(pat, text, flags=re.IGNORECASE)
        if matches:
            weak_hits.extend(m.lower() for m in matches)

    years = sorted({int(y) for y in YEAR_REGEX.findall(text)})
    emails = sorted(set(EMAIL_REGEX.findall(text)))
    linkedin = sorted(set(LINKEDIN_REGEX.findall(text)))
    github = sorted(set(GITHUB_REGEX.findall(text)))

    quant_ratio = (
        round((len(quantified_lines) / len(bullet_lines)) * 100, 1)
        if bullet_lines
        else 0.0
    )

    return {
        "word_count": len(words),
        "line_count": len(lines),
        "candidate_bullet_count": len(bullet_lines),
        "quantified_bullet_count": len(quantified_lines),
        "quantification_rate_pct": quant_ratio,
        "weak_passive_phrases_found": sorted(set(weak_hits)),
        "weak_phrase_occurrences": len(weak_hits),
        "years_detected": years,
        "earliest_year": min(years) if years else None,
        "latest_year": max(years) if years else None,
        "contact_detected": {
            "emails": emails,
            "has_phone": bool(PHONE_REGEX.search(text)),
            "linkedin": linkedin,
            "github": github,
        },
        "structural_risks": diagnostics,
    }


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/extract_and_audit.py <cv_file_1> [<cv_file_2> ...]")
        return 1

    all_years: List[int] = []

    for arg in sys.argv[1:]:
        path = Path(arg).expanduser().resolve()
        print("=" * 80)
        print(f"FILE: {path.name} ({path})")
        print("=" * 80)

        if not path.exists():
            print(f"[ERROR] File does not exist: {path}\n")
            continue

        try:
            text, diagnostics = extract_text(path)
            audit = audit_cv_text(text, diagnostics)
            all_years.extend(audit["years_detected"])  # type: ignore

            print("--- ATS & AI PRE-AUDIT SUMMARY ---")
            print(json.dumps(audit, indent=2, ensure_ascii=False))
            print("\n--- EXTRACTED TEXT ---")
            print(text)
            print("\n")
        except Exception as exc:
            print(f"[ERROR] Failed to process {path}: {exc}\n")

    if len(sys.argv) > 2 and all_years:
        print("=" * 80)
        print(
            f"MULTI-CV TIMELINE SPAN: {min(all_years)} – {max(all_years)} "
            f"(Check for gaps between {max(all_years)} and current year!)"
        )
        print("=" * 80)

    return 0


if __name__ == "__main__":
    sys.exit(main())
