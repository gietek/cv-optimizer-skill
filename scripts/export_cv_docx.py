#!/usr/bin/env python3
"""
Zero-Dependency Markdown-to-DOCX Exporter for ATS & Google Docs CVs.

Converts a canonical Markdown CV file into a clean, single-column,
ATS-friendly .docx file that opens natively in Google Docs and Microsoft Word
with preserved Heading 1/2/3 hierarchy, section dividers, bullet lists, and
inline bold/italic formatting.

Usage:
    python3 scripts/export_cv_docx.py <input_cv.md> <output_cv.docx>
"""

import re
import sys
import zipfile
from pathlib import Path
from typing import List, Tuple
from xml.sax.saxutils import escape

W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
R_NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"

CONTENT_TYPES_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
  <Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
  <Override PartName="/word/numbering.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.numbering+xml"/>
  <Override PartName="/word/footer1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml"/>
</Types>
"""

ROOT_RELS_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>
"""

DOC_RELS_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/numbering" Target="numbering.xml"/>
  <Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/footer" Target="footer1.xml"/>
</Relationships>
"""

FOOTER_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:ftr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:p>
    <w:pPr>
      <w:jc w:val="right"/>
      <w:spacing w:before="0" w:after="0" w:line="240" w:lineRule="auto"/>
    </w:pPr>
    <w:r>
      <w:rPr>
        <w:sz w:val="18"/>
        <w:szCs w:val="18"/>
        <w:color w:val="64748B"/>
      </w:rPr>
      <w:fldChar w:fldCharType="begin"/>
    </w:r>
    <w:r>
      <w:rPr>
        <w:sz w:val="18"/>
        <w:szCs w:val="18"/>
        <w:color w:val="64748B"/>
      </w:rPr>
      <w:instrText xml:space="preserve"> PAGE </w:instrText>
    </w:r>
    <w:r>
      <w:rPr>
        <w:sz w:val="18"/>
        <w:szCs w:val="18"/>
        <w:color w:val="64748B"/>
      </w:rPr>
      <w:fldChar w:fldCharType="separate"/>
    </w:r>
    <w:r>
      <w:rPr>
        <w:sz w:val="18"/>
        <w:szCs w:val="18"/>
        <w:color w:val="64748B"/>
      </w:rPr>
      <w:t>1</w:t>
    </w:r>
    <w:r>
      <w:rPr>
        <w:sz w:val="18"/>
        <w:szCs w:val="18"/>
        <w:color w:val="64748B"/>
      </w:rPr>
      <w:fldChar w:fldCharType="end"/>
    </w:r>
  </w:p>
</w:ftr>
"""

NUMBERING_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:numbering xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:abstractNum w:abstractNumId="0">
    <w:multiLevelType w:val="hybridMultilevel"/>
    <w:lvl w:ilvl="0">
      <w:start w:val="1"/>
      <w:numFmt w:val="bullet"/>
      <w:lvlText w:val="&#x2022;"/>
      <w:lvlJc w:val="left"/>
      <w:pPr>
        <w:ind w:left="360" w:hanging="180"/>
      </w:pPr>
      <w:rPr>
        <w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:cs="Arial"/>
      </w:rPr>
    </w:lvl>
  </w:abstractNum>
  <w:num w:numId="1">
    <w:abstractNumId w:val="0"/>
  </w:num>
</w:numbering>
"""

STYLES_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:docDefaults>
    <w:rPrDefault>
      <w:rPr>
        <w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:eastAsia="Arial" w:cs="Arial"/>
        <w:sz w:val="21"/>
        <w:szCs w:val="21"/>
        <w:color w:val="1F2937"/>
      </w:rPr>
    </w:rPrDefault>
    <w:pPrDefault>
      <w:pPr>
        <w:spacing w:after="80" w:line="260" w:lineRule="auto"/>
      </w:pPr>
    </w:pPrDefault>
  </w:docDefaults>

  <w:style w:type="paragraph" w:default="1" w:styleId="Normal">
    <w:name w:val="Normal"/>
    <w:qFormat/>
  </w:style>

  <w:style w:type="paragraph" w:styleId="Title">
    <w:name w:val="Title"/>
    <w:basedOn w:val="Normal"/>
    <w:qFormat/>
    <w:pPr>
      <w:spacing w:before="0" w:after="40" w:line="240" w:lineRule="auto"/>
    </w:pPr>
    <w:rPr>
      <w:b/>
      <w:sz w:val="40"/>
      <w:szCs w:val="40"/>
      <w:color w:val="0F172A"/>
    </w:rPr>
  </w:style>

  <w:style w:type="paragraph" w:styleId="Subtitle">
    <w:name w:val="Subtitle"/>
    <w:basedOn w:val="Normal"/>
    <w:qFormat/>
    <w:pPr>
      <w:spacing w:before="0" w:after="60" w:line="240" w:lineRule="auto"/>
    </w:pPr>
    <w:rPr>
      <w:sz w:val="21"/>
      <w:szCs w:val="21"/>
      <w:color w:val="334155"/>
    </w:rPr>
  </w:style>

  <w:style w:type="paragraph" w:styleId="Heading1">
    <w:name w:val="heading 1"/>
    <w:basedOn w:val="Normal"/>
    <w:next w:val="Normal"/>
    <w:qFormat/>
    <w:pPr>
      <w:keepNext/>
      <w:spacing w:before="220" w:after="80" w:line="240" w:lineRule="auto"/>
      <w:pBdr>
        <w:bottom w:val="single" w:sz="6" w:space="3" w:color="CBD5E1"/>
      </w:pBdr>
      <w:outlineLvl w:val="0"/>
    </w:pPr>
    <w:rPr>
      <w:b/>
      <w:caps/>
      <w:sz w:val="23"/>
      <w:szCs w:val="23"/>
      <w:color w:val="0F172A"/>
    </w:rPr>
  </w:style>

  <w:style w:type="paragraph" w:styleId="Heading2">
    <w:name w:val="heading 2"/>
    <w:basedOn w:val="Normal"/>
    <w:next w:val="Normal"/>
    <w:qFormat/>
    <w:pPr>
      <w:keepNext/>
      <w:spacing w:before="140" w:after="20" w:line="240" w:lineRule="auto"/>
      <w:outlineLvl w:val="1"/>
    </w:pPr>
    <w:rPr>
      <w:b/>
      <w:sz w:val="22"/>
      <w:szCs w:val="22"/>
      <w:color w:val="1E293B"/>
    </w:rPr>
  </w:style>

  <w:style w:type="paragraph" w:styleId="MetaLine">
    <w:name w:val="MetaLine"/>
    <w:basedOn w:val="Normal"/>
    <w:pPr>
      <w:keepNext/>
      <w:spacing w:before="0" w:after="60" w:line="240" w:lineRule="auto"/>
    </w:pPr>
    <w:rPr>
      <w:i/>
      <w:sz w:val="19"/>
      <w:szCs w:val="19"/>
      <w:color w:val="475569"/>
    </w:rPr>
  </w:style>

  <w:style w:type="paragraph" w:styleId="ListBullet">
    <w:name w:val="List Bullet"/>
    <w:basedOn w:val="Normal"/>
    <w:pPr>
      <w:numPr>
        <w:ilvl w:val="0"/>
        <w:numId w:val="1"/>
      </w:numPr>
      <w:spacing w:before="0" w:after="50" w:line="250" w:lineRule="auto"/>
    </w:pPr>
  </w:style>

  <w:style w:type="paragraph" w:styleId="FooterClause">
    <w:name w:val="FooterClause"/>
    <w:basedOn w:val="Normal"/>
    <w:pPr>
      <w:spacing w:before="180" w:after="0" w:line="210" w:lineRule="auto"/>
      <w:pBdr>
        <w:top w:val="single" w:sz="4" w:space="6" w:color="E2E8F0"/>
      </w:pBdr>
    </w:pPr>
    <w:rPr>
      <w:i/>
      <w:sz w:val="16"/>
      <w:szCs w:val="16"/>
      <w:color w:val="64748B"/>
    </w:rPr>
  </w:style>
</w:styles>
"""


def parse_inline_runs(text: str) -> List[Tuple[str, bool, bool]]:
    """
    Parse inline Markdown (**bold**, *italic*, `code`) into (text, is_bold, is_italic) tuples.
    """
    tokens: List[Tuple[str, bool, bool]] = []
    pattern = re.compile(r"(\*\*\*.*?\*\*\*|\*\*.*?\*\*|\*[^*]+?\*|`[^`]+?`)")
    pos = 0
    for match in pattern.finditer(text):
        if match.start() > pos:
            tokens.append((text[pos : match.start()], False, False))
        raw = match.group(0)
        if raw.startswith("***") and raw.endswith("***"):
            tokens.append((raw[3:-3], True, True))
        elif raw.startswith("**") and raw.endswith("**"):
            tokens.append((raw[2:-2], True, False))
        elif raw.startswith("*") and raw.endswith("*"):
            tokens.append((raw[1:-1], False, True))
        elif raw.startswith("`") and raw.endswith("`"):
            tokens.append((raw[1:-1], False, False))
        pos = match.end()

    if pos < len(text):
        tokens.append((text[pos:], False, False))

    return tokens


def build_paragraph_xml(
    text: str,
    style: str = "Normal",
    force_italic: bool = False,
) -> str:
    runs_xml: List[str] = []
    for chunk, is_bold, is_italic in parse_inline_runs(text):
        if not chunk:
            continue
        rpr_parts: List[str] = []
        if is_bold:
            rpr_parts.append("<w:b/><w:bCs/>")
        if is_italic or force_italic:
            rpr_parts.append("<w:i/><w:iCs/>")
        rpr = f"<w:rPr>{''.join(rpr_parts)}</w:rPr>" if rpr_parts else ""
        escaped = escape(chunk)
        runs_xml.append(
            f'<w:r>{rpr}<w:t xml:space="preserve">{escaped}</w:t></w:r>'
        )

    return (
        f"<w:p>"
        f'<w:pPr><w:pStyle w:val="{style}"/></w:pPr>'
        f"{''.join(runs_xml)}"
        f"</w:p>"
    )


def markdown_to_document_xml(md_text: str) -> str:
    paragraphs: List[str] = []
    in_header_zone = False
    in_footer_clause = False

    for raw_line in md_text.splitlines():
        line = raw_line.strip()
        if not line:
            continue

        # Horizontal rule marks transition to GDPR/footer clause if near bottom
        if re.match(r"^[-*_]{3,}$", line):
            in_footer_clause = True
            in_header_zone = False
            continue

        # Heading 1 (# Full Name)
        if line.startswith("# "):
            title_text = line[2:].strip()
            paragraphs.append(build_paragraph_xml(title_text, style="Title"))
            in_header_zone = True
            in_footer_clause = False
            continue

        # Section Heading (## Work Experience, ## Education, etc.)
        if line.startswith("## "):
            sec_text = line[3:].strip()
            paragraphs.append(build_paragraph_xml(sec_text, style="Heading1"))
            in_header_zone = False
            in_footer_clause = False
            continue

        # Role / Degree Subheading (### Job Title | Company)
        if line.startswith("### ") or line.startswith("#### "):
            sub_text = re.sub(r"^#{3,4}\s+", "", line).strip()
            paragraphs.append(build_paragraph_xml(sub_text, style="Heading2"))
            in_header_zone = False
            continue

        # Bullet list item (-, *, •)
        if re.match(r"^[-*•]\s+", line):
            bullet_text = re.sub(r"^[-*•]\s+", "", line).strip()
            paragraphs.append(build_paragraph_xml(bullet_text, style="ListBullet"))
            in_header_zone = False
            continue

        # Footer GDPR/RODO clause after `---`
        if in_footer_clause:
            clean_clause = line.strip("*_ ")
            paragraphs.append(
                build_paragraph_xml(
                    clean_clause, style="FooterClause", force_italic=True
                )
            )
            continue

        # Contact / Headline lines right under `# Full Name`
        if in_header_zone:
            paragraphs.append(build_paragraph_xml(line, style="Subtitle"))
            continue

        # Date / Location italic metadata line under `### Role`
        if (
            line.startswith("*")
            and line.endswith("*")
            and not line.startswith("**")
        ):
            meta_text = line.strip("*").strip()
            paragraphs.append(
                build_paragraph_xml(meta_text, style="MetaLine", force_italic=True)
            )
            continue

        # Standard paragraph
        paragraphs.append(build_paragraph_xml(line, style="Normal"))

    # A4 page geometry with 0.65 inch (936 twips) margins and default page-number footer
    sect_pr = (
        "<w:sectPr>"
        '<w:footerReference w:type="default" r:id="rId3"/>'
        '<w:pgSz w:w="11906" w:h="16838"/>'
        '<w:pgMar w:top="936" w:right="936" w:bottom="936" w:left="936" '
        'w:header="450" w:footer="450" w:gutter="0"/>'
        "</w:sectPr>"
    )

    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        f'<w:document xmlns:w="{W_NS}" xmlns:r="{R_NS}">'
        f"<w:body>{''.join(paragraphs)}{sect_pr}</w:body>"
        "</w:document>"
    )


def export_docx(md_path: Path, docx_path: Path) -> None:
    md_text = md_path.read_text(encoding="utf-8")
    document_xml = markdown_to_document_xml(md_text)

    docx_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(docx_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("[Content_Types].xml", CONTENT_TYPES_XML.strip())
        zf.writestr("_rels/.rels", ROOT_RELS_XML.strip())
        zf.writestr("word/_rels/document.xml.rels", DOC_RELS_XML.strip())
        zf.writestr("word/styles.xml", STYLES_XML.strip())
        zf.writestr("word/numbering.xml", NUMBERING_XML.strip())
        zf.writestr("word/footer1.xml", FOOTER_XML.strip())
        zf.writestr("word/document.xml", document_xml)


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: python3 scripts/export_cv_docx.py <input_cv.md> <output_cv.docx>")
        return 1

    md_path = Path(sys.argv[1]).expanduser().resolve()
    docx_path = Path(sys.argv[2]).expanduser().resolve()

    if not md_path.exists():
        print(f"[ERROR] Input Markdown file not found: {md_path}")
        return 1

    export_docx(md_path, docx_path)
    size_kb = round(docx_path.stat().st_size / 1024, 1)
    print(f"[OK] Generated ATS & Google-Docs ready DOCX: {docx_path} ({size_kb} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
