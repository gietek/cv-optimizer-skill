# ATS & AI Resume Screening Optimization Guide

Modern recruitment pipelines evaluate CVs across two automated layers before a human recruiter spends 6–10 seconds scanning the page:

1. **Deterministic & Rule-Based ATS Parsers** (Workday, Greenhouse, Lever, Taleo, iCIMS, BambooHR, SmartRecruiters, eRecruiter):
   - Parse layout into structured JSON fields (`contact`, `work_experience[]`, `education[]`, `skills[]`, `certifications[]`).
   - Compute exact and stemmed keyword matches, role tenure (months per skill/title), and recency weighting.
2. **LLM & Semantic AI Screeners** (Eightfold AI, HireVue, Paradox, LinkedIn Recruiter AI, custom GPT/Gemini screening agents):
   - Evaluate **evidence of impact** (quantified outcomes vs. generic duties).
   - Check **contextual skill validation** (whether a skill listed in the "Skills" section actually appears in a concrete project or work experience bullet).
   - Analyze **career trajectory & progression** (promotions, increasing scope, continuity, recency of relevant experience).

---

## 1. Structural & Parsing Rules (Zero Data Loss)

To ensure 100% extraction accuracy across all ATS parsers:

- **Single-Column Linear Layout**: Never use multi-column tables, text boxes, floating sidebars, or canvas graphics. Many older parsers read across columns left-to-right, scrambling job titles with unrelated skill lists.
- **Standard Section Headings**: Use universally recognized headings in the target language (see [`cv-templates-and-clauses.md`](./cv-templates-and-clauses.md)). Creative headers like *"My Journey"* or *"Where I've Been"* fail section classification.
- **Company & Role Hierarchy**:
  Place the **Job Title**, **Company Name**, **Location**, and **Date Range** in a predictable, consistent pattern:
  ```markdown
  ### Senior Backend Engineer | Acme Corp
  *Warsaw, Poland (Hybrid) | 03/2023 – Present*
  ```
- **Standardized Date Formats**:
  Always use `MM/YYYY – MM/YYYY` (e.g., `04/2021 – 11/2024`) or `YYYY-MM – YYYY-MM`, with `Present` / `Obecnie` for current roles. Never mix formats (e.g., `"Spring 2021"`, `"2021 - 23"`) as ATS tenure calculators miscalculate total years of experience when months are omitted.
- **No Visual Skill Bars or Star Ratings**:
  Graphics like `Python ★★★★☆` or `85%` are stripped by text extractors or parsed as gibberish. Instead, group skills by domain or specify years/context of usage.
- **Contact Information in the Main Body & Page Number in the Footer**:
  Never place contact details inside the Word/Google Docs document `Header` or `Footer` region—several legacy ATS parsers ignore header/footer XML nodes completely. Keep Name, Title, Email, Phone, Location (City, Country), LinkedIn, and Portfolio/GitHub at the very top of the main document body. Use the document `Footer` **exclusively for the page number** (paginated layout).

---

## 2. Rewriting Experience Bullets: The XYZ / CAR Framework

AI screeners score experience bullets on **Action + Context/Method + Quantified Result**.

### Google's XYZ Formula
> **"Accomplished [X] as measured by [Y], by doing [Z]."**

### CAR (Challenge – Action – Result) Formula
> **"[Action Verb] [System/Project/Scope] using [Tools/Methods] to solve [Challenge], resulting in [Quantifiable Metric/Business Outcome]."**

### Weak vs. AI-Optimized Examples

| Language | Weak (Duty-Based — Low AI Score) | Strong (XYZ / Impact-Based — High AI Score) |
| :--- | :--- | :--- |
| **English** | Responsible for backend microservices and database optimization in Python. | **Reduced API p95 latency by 42% (from 480ms to 275ms)** for a high-traffic checkout service handling **15k RPS** by redesigning PostgreSQL indexing and introducing Redis caching in Python/FastAPI. |
| **Polish** | Odpowiedzialny za zarządzanie zespołem sprzedaży i obsługę klientów B2B. | **Zwiększyłem roczną sprzedaż B2B o 34% (+1,8 mln PLN YoY)** poprzez wdrożenie nowego procesu kwalifikacji leadów w HubSpot oraz przebudowę onboardingu dla **12-osobowego zespołu handlowego**. |
| **English** | Helped migrate legacy infrastructure to AWS and wrote CI/CD pipelines. | **Cut cloud infrastructure costs by $4,200/month (-28%)** and accelerated deployment frequency from bi-weekly to **15+ daily releases** by migrating 18 legacy services to **AWS ECS (Terraform)** with automated GitHub Actions CI/CD pipelines. |
| **Polish** | Tworzenie raportów finansowych i automatyzacja procesów w Excelu. | **Skróciłem czas zamknięcia miesiąca o 3 dni robocze (z 8 do 5 dni)** dzięki automatyzacji konsolidacji raportów dla **5 spółek zależnych** przy użyciu **Power BI, SQL oraz Power Query**. |

### What If the Candidate Doesn't Remember Exact Percentages?
Never fabricate numbers. Instead, guide the user during the interview to uncover **proxy metrics & verifiable scope**:
1. **Scale / Volume**: How many users, clients, tickets, servers, SKUs, employees, countries, or transactions did the work touch?
2. **Frequency / Cadence**: Daily, weekly, monthly volume? How many releases, campaigns, or audits per quarter?
3. **Time Saved**: Did an automation reduce a 4-hour manual task to 15 minutes?
4. **Team & Stakeholder Scope**: Size of the team led or collaborated with; C-level or external client visibility.
5. **Reliability / Quality**: SLA targets met (`99.95%`), zero critical incidents during migration, audit pass rate.

---

## 3. Keyword & Semantic Alignment for AI Screeners

1. **Contextual Validation (The "Two-Touch Rule")**:
   Modern LLM screeners penalize "keyword stuffing" where a skill appears only in the `Skills` section without any mention in `Work Experience` or `Projects`.
   - Every core skill for the target role should appear **both** in the categorized `Skills` section **and** naturally inside at least one `Work Experience` bullet showing *how* it was applied.
2. **Canonical Name + Acronym Pairing**:
   Include both full terms and standard abbreviations where appropriate so both exact-match ATS filters and semantic vector searches hit:
   - e.g., `Key Performance Indicators (KPIs)`, `Search Engine Optimization (SEO)`, `Enterprise Resource Planning (ERP - SAP S/4HANA)`, `Large Language Models (LLMs)`.
3. **Title Alignment (Without Misrepresentation)**:
   If a user had an internal, non-standard company title (e.g., *"Ninja Member of Technical Staff III"* or *"Specjalista ds. Różnych"*), pair the official title with the industry-standard equivalent in parentheses:
   - `Member of Technical Staff III (Senior Full-Stack Developer)`
   - `Kierownik Projektów Technicznych (Technical Project Manager)`
4. **Recency Weighting**:
   ATS algorithms weight the **most recent 3–5 years** (and the top 1/3 of the first page) most heavily. Allocate the most detailed bullet points (4–6 bullets) to the current and immediately preceding roles, while condensing roles older than 8–10 years to 1–3 high-level bullets.

---

## 4. Strong Action Verbs Bank

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
