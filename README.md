# CV Optimizer (`cv-optimizer`) — AI & ATS Resume Builder Skill

> **English** | [Polski poniżej 🇵🇱](#-cv-optimizer--skill-do-tworzenia-cv-pod-ai-i-ats-pl)

A reusable Agent Skill (compatible with **Google Antigravity**, **Claude Code**, **Gemini CLI**, and the open `SKILL.md` standard) that transforms one or more outdated CVs/resumes from previous years into a high-impact, **AI- and ATS-optimized CV**, conducts a structured gap-filling interview, and generates a ready-to-edit **Google Docs** document in your chosen language.

---

## ✨ Key Features (EN)

1. **Multi-CV Ingestion & Reconciliation**: Accepts one or more legacy CVs (`.pdf`, `.docx`, `.md`, `.txt`, `.html`, or images) across different years, roles, or languages and merges them into a unified **Master Career Timeline**.
2. **AI & ATS Screening Audit**: Evaluates your existing CV(s) against modern rule-based ATS parsers (Workday, Greenhouse, Lever, Taleo) and LLM-based AI screeners:
   - Flags passive, duty-based phrasing (*"Responsible for..."*) and replaces it with quantified achievement statements using **Google's XYZ** and **CAR** frameworks.
   - Checks contextual skill validation (*Two-Touch Rule*), date standardization (`MM/YYYY`), and single-column parsing safety.
3. **Structured Gap-Filling Interview**: Asks focused follow-up questions in digestible rounds to fill missing employment periods, extract measurable metrics (`%`, `$`, scale, time saved), complete education/certification details, and resolve conflicts between older CV versions.
4. **Target Language Selection**: Explicitly asks in which language (e.g., English, Polish, German, or multiple versions) the final CV should be written, while conversing naturally in your preferred language.
5. **Hybrid Google Docs Output**:
   - **Primary**: Creates a native Google Docs document via the official Antigravity **Google Docs (`gdocs`)** plugin when connected.
   - **Universal Fallback**: Includes a zero-dependency Python exporter ([`scripts/export_cv_docx.py`](./scripts/export_cv_docx.py)) that generates a clean, single-column `.docx` with semantic `Heading 1/2` styles, bullet lists, and section borders—opening natively in **Google Docs** with 100% preserved layout.

---

## 📦 Repository Structure

```text
cv-optimizer/
├── SKILL.md                                 # Core Agent Skill definition & 5-phase workflow
├── plugin.json                              # Optional Antigravity plugin manifest
├── README.md                                # Bilingual documentation (EN + PL)
├── LICENSE                                  # MIT License
├── scripts/
│   ├── extract_and_audit.py                 # Zero-dependency CV text extractor & heuristic ATS pre-auditor
│   └── export_cv_docx.py                    # Zero-dependency Markdown -> Google-Docs-ready .docx exporter
├── references/
│   ├── ats-ai-optimization-guide.md         # Rules for ATS parsers, LLM screeners & XYZ/CAR bullet writing
│   ├── interview-question-bank.md           # Structured gap-filling questions (EN & PL)
│   └── cv-templates-and-clauses.md          # Canonical section headers (EN/PL/DE/ES) & GDPR/RODO clauses
└── examples/
    └── sample-optimized-cv.md               # Example of an AI/ATS-optimized CV in canonical Markdown
```

---

## 🚀 Installation

### Option 1: Install Globally in Google Antigravity
Clone this repository directly into your global Antigravity skills directory:

```bash
git clone https://github.com/<your-username>/cv-optimizer.git ~/.gemini/config/skills/cv-optimizer
```

### Option 2: Install in a Project Workspace
Clone into `.agents/skills/` inside any project workspace:

```bash
mkdir -p .agents/skills
git clone https://github.com/<your-username>/cv-optimizer.git .agents/skills/cv-optimizer
```

### Option 3: `npx skills` CLI (Agent Skills Ecosystem)
```bash
npx skills add <your-username>/cv-optimizer
```

---

## 💡 Usage

Drop your old CV file(s) into your workspace (or pass their paths) and prompt the agent:

```text
/cv-optimizer Here are my old CVs from 2021 and 2024 (cv_2021.pdf, cv_2024.docx). Audit them and help me create a new 2026 CV in Google Docs.
```

---
---

# 🇵🇱 CV Optimizer — Skill do tworzenia CV pod AI i ATS (PL)

Reużywalny skill dla agentów AI (zgodny z **Google Antigravity**, **Claude Code**, **Gemini CLI** oraz standardem `SKILL.md`), który przyjmuje jedną lub więcej starych wersji CV z poprzednich lat, analizuje je pod kątem automatycznych systemów selekcji (**ATS oraz skanerów AI/LLM**), przeprowadza ustrukturyzowany wywiad uzupełniający braki i generuje gotowy dokument **Google Docs** w wybranym przez Ciebie języku.

---

## ✨ Główne możliwości

1. **Analiza i łączenie wielu starych wersji CV**: Przyjmuje jedną lub więcej starszych wersji CV (`.pdf`, `.docx`, `.md`, `.txt`, `.html` lub skany/obrazy) z różnych lat i łączy je w spójną historię kariery, odzyskując pominięte projekty oraz wyłapując rozbieżności w datach czy stanowiskach.
2. **Audyt pod kątem AI oraz systemów ATS**:
   - Wykrywa bierne opisy obowiązków (*„Odpowiedzialny za..."*, *„Zajmowałem się..."*) i zamienia je na punkty oparte o mierzalne osiągnięcia wg formuły **XYZ Google** (*Osiągnąłem [X] mierzone przez [Y], wykonując [Z]*) oraz **CAR**.
   - Weryfikuje nasycenie słowami kluczowymi w kontekście doświadczenia (*Two-Touch Rule*), spójność dat (`MM/YYYY`) oraz bezpieczeństwo parsowania układu jednoszpaltowego.
3. **Seria pytań uzupełniających (Gap-Filling Interview)**: Zadaje uporządkowane pytania w 2–3 krótkich rundach, aby uzupełnić:
   - Aktualne doświadczenie od czasu powstania ostatniego CV,
   - Konkretne metryki i skalę projektów (procenty, budżety, zaoszczędzony czas, wielkość zespołów, użyte technologie),
   - Braki w wykształceniu, certyfikatach, językach obcych (skala CEFR B1–C2) oraz klauzuli RODO/GDPR.
4. **Wybór języka docelowego CV**: Zawsze pyta, w jakim języku (np. polskim, angielskim, niemieckim lub w kilku wersjach językowych) ma zostać wygenerowane docelowe CV.
5. **Tworzenie dokumentu Google Docs (tryb hybrydowy)**:
   - **Metoda natywna**: Tworzy dokument bezpośrednio w chmurze Google Docs przez oficjalny plugin **Google Docs (`gdocs`)** w Antigravity.
   - **Metoda uniwersalna (Fallback / Google Drive)**: Zawiera bezinwazyjny skrypt w czystym Pythonie ([`scripts/export_cv_docx.py`](./scripts/export_cv_docx.py)) niewymagający żadnych zewnętrznych bibliotek (`pip`), który generuje czysty, jednoszpaltowy plik `.docx` ze stylami nagłówków `Heading 1/2` i wypunktowaniami, gotowy do otwarcia bezpośrednio jako **Google Docs**.

---

## 🛠️ Instalacja (PL)

### 1. Instalacja globalna w Google Antigravity
Sklonuj repozytorium do katalogu globalnych skilli Antigravity:

```bash
git clone https://github.com/<twoj-login>/cv-optimizer.git ~/.gemini/config/skills/cv-optimizer
```

### 2. Instalacja lokalna w projekcie / workspace
```bash
mkdir -p .agents/skills
git clone https://github.com/<twoj-login>/cv-optimizer.git .agents/skills/cv-optimizer
```

---

## 🚀 Jak używać?

Umieść swoje stare pliki CV w folderze roboczym (lub podaj do nich ścieżki) i napisz do agenta:

```text
/cv-optimizer Przeanalizuj moje stare CV z poprzednich lat, dopytaj o brakujące informacje i przygotuj nową wersję CV w Google Docs.
```

Możesz też uruchomić narzędzia pomocnicze z terminala:

```bash
# 1. Ekstrakcja tekstu i wstępny audyt heurystyczny starych CV:
python3 scripts/extract_and_audit.py stare_cv_2022.pdf stare_cv_2024.docx

# 2. Konwersja zoptymalizowanego CV z Markdown do pliku .docx dla Google Docs:
python3 scripts/export_cv_docx.py examples/sample-optimized-cv.md CV_Jan_Kowalski_EN.docx
```

---

## 📄 Licencja / License

Released under the [MIT License](./LICENSE).
