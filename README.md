# CV Optimizer (`cv-optimizer`) — AI & ATS Resume Builder Skill

> **English** | [Polski poniżej 🇵🇱](#-cv-optimizer--skill-do-tworzenia-cv-pod-ai-i-ats-pl)

A reusable Agent Skill (compatible with **Google Antigravity**, **Claude Code**, **Gemini CLI**, and the open `SKILL.md` standard) that transforms one or more outdated CVs/resumes from previous years into a high-impact, **AI- and ATS-optimized CV**, conducts a structured gap-filling interview focused on **measurable results** and **ecosystem technologies**, and generates a ready-to-edit **Google Docs** document in your chosen language.

---

## ✨ Key Features (EN)

1. **Multi-CV Ingestion & Reconciliation**: Accepts one or more legacy CVs (`.pdf`, `.docx`, `.md`, `.txt`, `.html`, or images) across different years, roles, or languages and merges them into a unified **Master Career Timeline**.
2. **AI & ATS Screening Audit**: Evaluates your existing CV(s) against modern rule-based ATS parsers (Workday, Greenhouse, Lever, Taleo) and LLM-based AI screeners:
   - Flags passive, duty-based phrasing (*"Responsible for..."*) and replaces it with **measurable achievement statements** using **Google's XYZ** and **CAR** frameworks.
   - **Warns against slang and colloquialisms** (e.g., *"fixing random bugs"*, *"ninja"*, *"klepanie kodu"*, *"dowożenie ficzerów"*) and translates them into formal industry terminology.
   - Checks contextual skill validation (*Two-Touch Rule*), date standardization (`MM/YYYY`), and single-column parsing safety.
3. **Proactive Adjacent Technology Discovery**: Detects technologies listed in a given role and proactively asks whether to add matching ecosystem tools:
   - *Example*: Candidate lists `React` → asks whether they used `React Router` (or `Next.js`, `TanStack Query`).
   - *Example*: Candidate lists `React` and `Redux` → asks whether they used `Redux Toolkit (RTK)` and `RTK Query`.
4. **Structured Gap-Filling Interview (Focused on Measurable Results)**: Asks focused follow-up questions in digestible rounds to extract quantifiable metrics (`%`, `$`, scale, time saved), fill missing employment periods, complete education/certification details, and resolve conflicts between older CV versions.
5. **GitHub / GitLab & Link Hygiene**:
   - Checks if a **GitHub** or **GitLab** profile is present; if missing, asks the user whether to add it and requests the link.
   - Ensures every link in the CV (LinkedIn, GitHub, GitLab, portfolio) starts with **`https://`**.
   - Ensures generated filenames contain **only basic English ASCII characters** (no Polish diacritics or special characters in filenames).
6. **Target Language Selection & Google Docs Output**: Explicitly asks in which language the final CV should be written and creates the document in **Google Docs** via the `gdocs` plugin (alongside an ASCII-named Markdown source file).

---

## 📦 Repository Structure

```text
cv-optimizer/
├── SKILL.md                                 # Core Agent Skill definition & 5-phase workflow
├── plugin.json                              # Optional Antigravity plugin manifest
├── README.md                                # Bilingual documentation (EN + PL)
├── LICENSE                                  # MIT License
├── scripts/
│   └── extract_and_audit.py                 # Zero-dependency CV text extractor & heuristic ATS pre-auditor
├── references/
│   ├── ats-ai-optimization-guide.md         # Rules for ATS parsers, LLM screeners, slang & XYZ/CAR bullets
│   ├── interview-question-bank.md           # Gap-filling questions & Ecosystem Technology Inference Map
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

Reużywalny skill dla agentów AI (zgodny z **Google Antigravity**, **Claude Code**, **Gemini CLI** oraz standardem `SKILL.md`), który przyjmuje jedną lub więcej starych wersji CV z poprzednich lat, analizuje je pod kątem automatycznych systemów selekcji (**ATS oraz skanerów AI/LLM**), przeprowadza ustrukturyzowany wywiad skupiony na **mierzalnych wynikach** i **powiązanych technologiach**, a następnie generuje gotowy dokument **Google Docs** w wybranym przez Ciebie języku.

---

## ✨ Główne możliwości

1. **Analiza i łączenie wielu starych wersji CV**: Przyjmuje jedną lub więcej starszych wersji CV (`.pdf`, `.docx`, `.md`, `.txt`, `.html` lub skany/obrazy) z różnych lat i łączy je w spójną historię kariery, odzyskując pominięte projekty oraz wyłapując rozbieżności w datach czy stanowiskach.
2. **Skupienie na mierzalnych wynikach (XYZ / CAR)**:
   - Zarówno podczas zadawania pytań uzupełniających, jak i przy redagowaniu CV skupia się na twardych, mierzalnych efektach pracy (procenty, kwoty, zaoszczędzony czas, skala ruchu, liczba użytkowników, SLA, wielkość zespołów).
3. **Ostrzeganie przed używaniem slangu**:
   - Wykrywa zwroty potoczne i żargon (np. *„ogarnianie tematów"*, *„dowożenie ficzerów"*, *„klepanie kodu"*, *„gaszenie pożarów"*, *„robienie calli"*) i ostrzega przed ich stosowaniem, zamieniając je na profesjonalne słownictwo rozpoznawane przez systemy ATS i rekruterów.
4. **Wykrywanie pasujących technologii z ekosystemu**:
   - Na podstawie technologii podanych przy danym stanowisku proaktywnie dopytuje użytkownika o powiązane biblioteki i narzędzia, o których kandydaci często zapominają:
     - *Przykład 1*: Podano `React` → dopytuje o `React Router` (oraz np. `Next.js`, `TanStack Query`).
     - *Przykład 2*: Podano `React` oraz `Redux` → dopytuje o `Redux Toolkit (RTK)` oraz `RTK Query`.
5. **Weryfikacja GitHub / GitLab, linków `https://` oraz nazw plików ASCII**:
   - Jeśli w CV brakuje linku do **GitHuba** lub **GitLaba**, pyta czy go dodać i prosi o link.
   - Pilnuje, aby wszystkie linki (np. do LinkedIna, GitHuba, portfolio) zawierały pełny prefiks **`https://`**.
   - Generując nazwy plików używa wyłącznie podstawowych znaków alfabetu angielskiego ASCII (bez polskich znaków diakrytycznych, np. `CV_Artur_Wrobel_PL.md`).
6. **Wybór języka docelowego i zapis do Google Docs**:
   - Zawsze pyta, w jakim języku ma powstać CV, a następnie tworzy sformatowany dokument w **Google Docs** za pomocą pluginu `gdocs`.

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

Możesz też uruchomić skrypt wstępnego audytu z terminala:

```bash
python3 scripts/extract_and_audit.py stare_cv_2022.pdf stare_cv_2024.docx
```

---

## 📄 Licencja / License

Released under the [MIT License](./LICENSE).
