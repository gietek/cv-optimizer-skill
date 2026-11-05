# ATS & AI Resume Screening Optimization Guide

Modern recruitment pipelines evaluate CVs across two automated layers before a human recruiter spends 6–10 seconds scanning the page:

1. **Deterministic & Rule-Based ATS Parsers** (Workday, Greenhouse, Lever, Taleo, iCIMS, BambooHR, SmartRecruiters, eRecruiter):
   - Parse layout into structured JSON fields (`contact`, `work_experience[]`, `education[]`, `skills[]`, `certifications[]`).
   - Compute exact and stemmed keyword matches, role tenure (months per skill/title), and recency weighting.
2. **LLM & Semantic AI Screeners** (Eightfold AI, HireVue, Paradox, LinkedIn Recruiter AI, custom GPT/Gemini screening agents):
   - Evaluate **evidence of measurable impact** (quantified outcomes vs. generic duties).
   - Check **contextual skill validation** (whether a skill listed in the "Skills" section actually appears in a concrete project or work experience bullet).
   - Penalize **colloquialisms and slang**, favoring formal, standardized industry terminology.
   - Analyze **career trajectory & progression** (promotions, increasing scope, continuity, recency of relevant experience).

---

## 1. Structural, Link & Filename Hygiene

To ensure 100% extraction accuracy across all ATS parsers and clean cross-platform file handling:

- **ASCII-Only Filenames (Zero Non-English Characters)**:
  Whenever saving or naming a CV file, use **exclusively basic English ASCII characters** (`A-Z`, `a-z`, `0-9`, `_`, `-`, `.`). Never include Polish diacritics or other non-ASCII characters in filenames, as legacy ATS uploaders and zip/mail gateways often corrupt UTF-8 filenames.
  - **Transliteration Map**: `ą→a`, `ć→c`, `ę→e`, `ł→l`, `ń→n`, `ó→o`, `ś→s`, `ź→z`, `ż→z` (and uppercase equivalents: `Ł→L`, `Ó→O`, `Ś→S`, `Ż→Z`, etc.).
  - *Good*: `CV_Artur_Wrobel_EN.md`, `CV_Lukasz_zolc_PL.md`
  - *Bad*: `CV_Artur_Wróbel_EN.md`, `CV_Łukasz_Żółć_PL.md`
- **All Links Must Include `https://`**:
  Every URL in the CV (LinkedIn, GitHub, GitLab, personal portfolio, project links) **must** begin with `https://` (e.g., `https://linkedin.com/in/username`, `https://github.com/username`, `https://gitlab.com/username`). Many ATS parsers and PDF/Google Docs exporters fail to turn bare domains (`linkedin.com/in/...`) into clickable hyperlinks without an explicit `https://` scheme.
- **GitHub / GitLab Presence**:
  For technical, engineering, data, and IT roles, AI screeners and technical recruiters actively look for a `https://github.com/...` or `https://gitlab.com/...` profile link. Always check if it is present and ask the user whether to add it if missing.
- **Single-Column Linear Layout**:
  Never use multi-column tables, text boxes, floating sidebars, or canvas graphics. Many older parsers read across columns left-to-right, scrambling job titles with unrelated skill lists.
- **Standard Section Headings**:
  Use universally recognized headings in the target language (see [`cv-templates-and-clauses.md`](./cv-templates-and-clauses.md)).
- **Standardized Date Formats**:
  Always use `MM/YYYY – MM/YYYY` (e.g., `04/2021 – 11/2024`) or `YYYY-MM – YYYY-MM`, with `Present` / `Obecnie` for current roles.
- **Contact Information in the Main Body**:
  Keep Name, Title, Email, Phone, Location (City, Country), LinkedIn (`https://...`), and GitHub/GitLab (`https://...`) at the very top of the main document body.

---

## 2. Focus on Measurable Results: The XYZ / CAR Framework

AI screeners score experience bullets primarily on **Measurable Results** (**Action + Context/Method + Quantified Result**). Both during the user interview and when generating the CV, focus relentlessly on measurable outcomes.

### Google's XYZ Formula
> **"Accomplished [X] as measured by [Y], by doing [Z]."**

### CAR (Challenge – Action – Result) Formula
> **"[Action Verb] [System/Project/Scope] using [Tools/Methods] to solve [Challenge], resulting in [Quantifiable Metric/Business Outcome]."**

### Weak vs. AI-Optimized Examples

| Language | Weak (Duty-Based — Low AI Score) | Strong (XYZ / Measurable Result — High AI Score) |
| :--- | :--- | :--- |
| **English** | Responsible for backend microservices and database optimization in Python. | **Reduced API p95 latency by 42% (from 480ms to 275ms)** for a high-traffic checkout service handling **15k RPS** by redesigning PostgreSQL indexing and introducing Redis caching in Python/FastAPI. |
| **Polish** | Odpowiedzialny za zarządzanie zespołem sprzedaży i obsługę klientów B2B. | **Zwiększyłem roczną sprzedaż B2B o 34% (+1,8 mln PLN YoY)** poprzez wdrożenie nowego procesu kwalifikacji leadów w HubSpot oraz przebudowę onboardingu dla **12-osobowego zespołu handlowego**. |
| **English** | Helped migrate legacy infrastructure to AWS and wrote CI/CD pipelines. | **Cut cloud infrastructure costs by $4,200/month (-28%)** and accelerated deployment frequency from bi-weekly to **15+ daily releases** by migrating 18 legacy services to **AWS ECS (Terraform)** with automated GitHub Actions CI/CD pipelines. |
| **Polish** | Tworzenie raportów finansowych i automatyzacja procesów w Excelu. | **Skróciłem czas zamknięcia miesiąca o 3 dni robocze (z 8 do 5 dni)** dzięki automatyzacji konsolidacji raportów dla **5 spółek zależnych** przy użyciu **Power BI, SQL oraz Power Query**. |

### How to Extract Measurable Results When Exact `%` Isn't Known
Never fabricate numbers. Guide the user during the interview to uncover verifiable metrics:
1. **Scale / Volume**: Number of users, clients, tickets, servers, SKUs, employees, markets, or daily transactions.
2. **Frequency / Cadence**: Releases per week, campaigns per quarter, reports automated per month.
3. **Time Saved**: Reduction of a manual process from `4 hours` to `15 minutes`.
4. **Reliability & Quality**: SLA achieved (`99.95%`), bug reduction, test coverage increase (`from 35% to 85%`).

---

## 3. Warning Against Slang & Colloquialisms

Candidates frequently use workplace slang, developer jargon, or casual shorthand in old CVs or during interviews. **Always warn the user against using slang** because:
1. **ATS Keyword Misses**: ATS systems search for canonical terms (*"Incident Management"*, *"Code Review"*, *"Feature Delivery"*), never slang (*"gaszenie pożarów"*, *"klepanie kodu"*, *"dowożenie ficzerów"*).
2. **Recruiter & AI Penalties**: LLM screeners evaluate tone and professionalism; colloquial phrasing signals lower seniority.

### Common Slang vs. Professional ATS Replacements

| Colloquial / Slang (Warn & Remove!) | Professional ATS-Ready Equivalent |
| :--- | :--- |
| *"Ogarnianie tematów / ogarnianie projektów"* | *Koordynacja projektów end-to-end / Zarządzanie realizacją inicjatyw* |
| *"Dowożenie ficzerów / dowiezienie projektu na czas"* | *Terminowe wdrażanie nowych funkcjonalności (End-to-End Feature Delivery)* |
| *"Klepanie kodu / pisanie kodu"* | *Projektowanie i implementacja oprogramowania (Software Engineering)* |
| *"Gaszenie pożarów na produkcji"* | *Rozwiązywanie krytycznych incydentów produkcyjnych (Incident Management & Root Cause Analysis)* |
| *"Robienie calli z klientem / dzwonienie"* | *Prowadzenie spotkań warsztatowych i zbieranie wymagań biznesowych (Stakeholder Management)* |
| *"Grzebanie w bazie / poprawianie zamulających zapytań"* | *Optymalizacja wydajności zapytań SQL oraz indeksowania bazy danych* |
| *"Stawianie serwerów / odpalanie dokerów"* | *Konfiguracja i utrzymanie infrastruktury kontenerowej (Docker / Kubernetes / IaC)* |
| *"Ninja / Rockstar / Guru developer"* | *Senior Software Engineer / Subject Matter Expert (SME)* |
| *"Fixing random bugs & tech debt stuff"* | *Resolving production defects and systematically reducing technical debt* |

---

## 4. Keyword Alignment & Adjacent Technology Inference

1. **Proactive Ecosystem Skill Inference**:
   Candidates often list only top-level technologies (e.g., `React`, `Redux`, `Python`, `AWS`) while omitting core companion libraries they actually used. Because ATS filters often match specific library names, **always detect adjacent technologies for a given role and ask the user whether to include them**:
   - Listed `React` → ask about `React Router`, `Next.js`, `TanStack Query`.
   - Listed `React` + `Redux` → ask about `Redux Toolkit (RTK)` and `RTK Query`.
   - Listed `Python` → ask about `FastAPI` / `Django`, `SQLAlchemy`, `Pydantic`, `pytest`.
2. **Contextual Validation (The "Two-Touch Rule")**:
   Every core skill for the target role should appear **both** in the categorized `Skills` section **and** naturally inside at least one `Work Experience` bullet showing *how* it was applied to achieve a measurable result.
3. **Canonical Name + Acronym Pairing**:
   Include both full terms and standard abbreviations where appropriate:
   - e.g., `Redux Toolkit (RTK)`, `Key Performance Indicators (KPIs)`, `Continuous Integration / Continuous Deployment (CI/CD)`.

---

## 5. Length Control, Summary Rules, Anti-Ageism, Anti-Redundancy & Page Layout

1. **Maximum Document Length (Up to 3 Pages)**:
   - Keep the complete CV concise so that the generated Google Docs document **does not exceed 3 pages** (typically 600–1,200 words depending on career length).
   - Trim low-value fluff, generic filler phrases, and overly verbose project descriptions.
2. **Concise Professional Summary (3–4 Sentences, Zero Duplication of Tech or Role Achievements)**:
   - Limit the `Professional Summary` / `Podsumowanie zawodowe` strictly to **3–4 sentences**.
   - **Do NOT list specific technologies, frameworks, or tools in the summary** if they are already included later in the document (`Work Experience` or `Skills`).
   - **Do NOT repeat specific items, metrics, or achievements from individual job positions** (for example, do not write *"increased automated test coverage"* or repeat a single role's specific percentage metric in the summary if it already appears in a role bullet below).
   - Instead, write the summary as a **high-level executive synthesis** covering: total years of experience (subject to the `20+` cap below), core domain specialization, leadership/architectural scope, and overarching business value delivered across the career.
3. **Anti-Ageism Cap on Years of Experience (`20+` Maximum)**:
   - To prevent automated or human ageism filters from flagging senior candidates, **cap the stated number of years of experience in the Professional Summary at `20+`**:
     - If the candidate has `<= 20` years of experience (e.g., `10` years), state the exact number (`10 years of experience` / `10 lat doświadczenia`).
     - If the candidate has `> 20` years of experience (e.g., `25` years), always write **`20+`** (`20+ years of experience` in English, or `ponad 20 lat doświadczenia` / `20+ lat doświadczenia` in Polish).
4. **Avoid Redundant Repetitions & Pleonasms**:
   - Never repeat the same number, multiplier, or concept in two notations side-by-side:
     - *Bad*: `"zwiększyłem przepustowość 2-krotnie (2x)"`, `"dwukrotnie (2x)"`, `"o 50 procent (50%)"`, `"zespół pięcioosobowy (5 osób)"`.
     - *Good*: `"zwiększyłem przepustowość 2-krotnie"` lub `"zwiększyłem przepustowość o 100%"` (pick one clean form, never both).
5. **Condense Roles from 12+ Years Ago**:
   - Recruiters and AI screeners weight recent experience heavily while treating roles from **12 or more years ago** primarily as career foundation context.
   - **Recent roles (< 12 years ago)**: Describe with full detail (3–6 measurable XYZ bullets per role).
   - **Older roles (12+ years ago)**: Significantly reduce detail—limit each old role to **1–2 short summary bullets** (or a single concise sentence capturing scope and key achievement) instead of full technical breakdowns.
6. **Google Docs Page Layout (A4, 1.25 cm Margins & Paragraph Pagination)**:
   - Always configure the Google Docs CV as a **paginated (`PAGES`) A4 document** (`595.28 × 841.89 PT`) with **1.25 cm (`35.43 PT`) margins** (`top`, `bottom`, `left`, `right`).
   - Set paragraph pagination properties **`keepWithNext: true`**, **`keepLinesTogether: true`**, and **`avoidWidowAndOrphan: true`** so headings never detach from their content at the bottom of a page and paragraphs are never split across page breaks.

---

## 6. Strong Action Verbs Bank

Avoid passive openers (*"Responsible for"*, *"Duties included"*, *"Helped with"*, *"Worked on"*, *"Odpowiedzialny za"*, *"Zajmowałem się"*).

### English Action Verbs
- **Leadership & Strategy**: Spearheaded, Orchestrated, Directed, Mentored, Scaled, Pioneered, Championed, Aligned, Restructured
- **Engineering & Technical**: Architected, Engineered, Automated, Refactored, Migrated, Deployed, Optimized, Integrated, Hardened
- **Revenue & Growth**: Accelerated, Generated, Expanded, Captured, Converted, Negotiated, Outperformed, Monetized
- **Operations & Efficiency**: Streamlined, Consolidated, Standardized, Eliminated, Reduced, Overhauled, Expedited

### Polish Action Verbs (Czasowniki dokonane w 1. os. l. poj. lub rzeczowniki odsłowne)
> *Tip for Polish CVs*: Choose either **1st person past tense perfective verbs** (*Wdrożyłem/am, Zoptymalizowałem/am, Zwiększyłem/am*) or **gerunds/verbal nouns** (*Wdrożenie, Optymalizacja, Zwiększenie*) and keep the form **100% consistent** across the entire document.
- **Liderowanie i strategia**: Zbudowałem/am (Zbudowanie), Pokierowałem/am (Kierowanie), Przeszkoliłem/am (Przeszkolenie), Wyznaczyłem/am, Zreorganizowałem/am
- **Technologia i inżynieria**: Zaprojektowałem/am (Zaprojektowanie), Wdrożyłem/am (Wdrożenie), Zautomatyzowałem/am (Automatyzacja), Zmigrowałem/am (Migracja), Zoptymalizowałem/am (Optymalizacja), Zintegrowałem/am
- **Sprzedaż i wzrost**: Zwiększyłem/am (Zwiększenie), Pozyskałem/am (Pozyskanie), Wynegocjowałem/am (Wynegocjowanie), Rozwinąłem/am (Rozwinięcie), Przekroczyłem/am
- **Operacje i efektywność**: Usprawniłem/am (Usprawnienie), Skróciłem/am (Skrócenie), Obniżyłem/am (Obniżenie), Wyeliminowałem/am (Wyeliminowanie), Ustandaryzowałem/am
