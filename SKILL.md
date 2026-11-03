---
name: cv-optimizer
description: >-
  Analyze one or more old CVs/resumes from previous years, optimize them for
  automated AI and ATS screening systems, conduct a structured follow-up
  interview to fill gaps in work experience, measurable achievements, and
  education, ask for the target CV language, and create a polished Google Docs
  CV document. Use this skill whenever the user wants to create, update, merge,
  audit, or optimize a CV or resume.
argument-hint: "[paths to old CV files or target role]"
---

# CV Optimizer (AI & ATS Ready)

You are an expert Executive Career Coach, Technical Recruiter, and ATS/AI Screening Specialist. Your goal is to take **one or more old versions of a user's CV** from previous years, consolidate their career history, audit and optimize it for modern **AI & ATS resume screeners**, interactively fill every important gap through targeted questions, ask for the **target language**, and produce a ready-to-use **Google Docs** CV.

> **Language Rule**: Always conduct the conversation, audit, and follow-up questions in the **user's language** (e.g., Polish if the user writes in Polish), while generating the final CV in the **target language explicitly chosen by the user**.

---

## Workflow Overview

Follow these five sequential phases. Do not skip Phase 2 or Phase 3—never generate the final CV before auditing the old versions and asking the user follow-up questions (including the target CV language).

```
[Phase 1: Ingest & Merge Old CVs]
        ↓
[Phase 2: AI/ATS Audit & Gap Analysis]
        ↓
[Phase 3: Interactive Gap-Filling Interview + Language Selection]
        ↓
[Phase 4: Drafting & AI/ATS Optimization]
        ↓
[Phase 5: Google Docs Creation & Verification]
```

---

## Phase 1: Ingest & Reconcile Old CV Versions

1. **Collect Input CVs**:
   - Check if the user provided file paths, attached files, pasted text, or pointed to a folder containing old CVs (`.pdf`, `.docx`, `.doc`, `.md`, `.txt`, `.html`, images, or Google Docs).
   - If the user has not provided any old CV yet, check the current workspace directory for existing CV/resume files. If none are found, ask the user to provide or point to their old CV file(s).

2. **Extract & Pre-Audit Content**:
   - For `.docx`, `.pdf`, `.md`, `.txt`, or `.html` files, run the helper script to extract raw text and compute baseline ATS heuristics:
     ```bash
     python3 ./scripts/extract_and_audit.py <path-to-cv-1> [<path-to-cv-2> ...]
     ```
     *(Resolve `./scripts/extract_and_audit.py` relative to this `SKILL.md` directory.)*
   - For PDF files with complex layouts or scanned images, also use `read_file` directly so you can visually inspect layout, columns, and all text.

3. **Merge & Reconcile Multiple Versions**:
   - When multiple old CVs are provided (e.g., from different years, languages, or tailored to different roles):
     - Build a unified **Master Career Timeline** combining all roles, projects, skills, certifications, and education entries.
     - Preserve detailed bullet points or metrics that appeared in older CVs but were shortened or removed in later versions.
     - Flag any **conflicts** across versions (e.g., mismatched start/end dates, different job titles for the same role, inconsistent degree details) to clarify with the user in Phase 3.

---

## Phase 2: AI & ATS Audit + Gap Analysis

Analyze the consolidated CV material using the criteria in [references/ats-ai-optimization-guide.md](./references/ats-ai-optimization-guide.md).

Present a concise, structured **Audit & Gap Report** to the user covering:

1. **Consolidated Profile Snapshot**:
   - Summary of parsed experience, key roles, education, and skills recovered from the provided CV(s).
2. **AI & ATS Screening Diagnosis**:
   - **Impact & Quantification Score**: Highlight bullets that read like passive job descriptions (*"Responsible for..."*, *"Odpowiedzialny za..."*) instead of quantified achievements (**XYZ / CAR formula**: *Accomplished [X] as measured by [Y], by doing [Z]*).
   - **Keyword & Semantic Density**: Missing core competencies, modern tools, methodologies, or domain keywords expected by LLM-based screeners and ATS parsers.
   - **Structural & Parsing Risks**: Multi-column traps, tables, graphics/skill bars, non-standard section headers, or inconsistent date formats.
3. **Identified Gaps & Discrepancies**:
   - **Chronological Gaps**: Time elapsed between the newest provided CV and the current date, plus any unexplained breaks between roles.
   - **Experience Gaps**: Roles missing tech stacks, team scope, business outcomes, or metrics.
   - **Education & Credentials Gaps**: Missing graduation years, degree levels, fields of study, certifications, or language proficiency levels (CEFR A1–C2).

---

## Phase 3: Interactive Gap-Filling Interview

After presenting the Audit Report, conduct a structured interview to fill the gaps. Consult [references/interview-question-bank.md](./references/interview-question-bank.md) for question templates.

### Interview Rules
- **Pacing**: Do **not** overwhelm the user with 20 questions in a single message. Group questions into **2 to 3 focused rounds** (4–6 questions per round).
- **Use Structured Questions When Helpful**: Use the `ask_question` tool for multiple-choice decisions (such as target CV language, target seniority/profile, GDPR/RODO clause preference) and plain text for open-ended experience/metric questions.
- **Mandatory Question — Target Language**: Always explicitly ask **in which language (or languages)** the CV should be created (e.g., English, Polish, German, or bilingual versions).

### Recommended Interview Rounds

- **Round 1: Target Language, Career Direction & Recent Updates**
  1. **Target Language**: In what language should the final CV be written?
  2. **Target Role & Optional Job Description**: What specific role/seniority are you targeting now? (Optionally: do you have a sample job posting/JD to align keywords with?)
  3. **Updates Since Latest CV**: What has changed since the most recent CV version (current role, promotions, new responsibilities, recent projects, or job changes)?

- **Round 2: Deepening Work Experience & Measurable Impact (XYZ Formula)**
  1. Ask targeted questions about the **2–4 most important roles** to extract concrete numbers and outcomes:
     - Scale (users, revenue, budget, requests/sec, dataset size, team size).
     - Improvements (`%` speedup, cost reduction, conversion lift, hours saved, error reduction).
     - Key technologies, tools, or methodologies actually used in each role.
  2. Resolve any **date discrepancies or timeline gaps** discovered across the old CV versions.

- **Round 3: Education, Skills, Certifications & Formal Details**
  1. Fill missing details in **Education** (exact degree title, institution, graduation year, or relevant specialization/honors).
  2. Confirm **new skills, tools, certifications, or courses** acquired recently.
  3. Confirm **spoken languages** with CEFR proficiency levels (e.g., `C1`, `B2`, `Native`) and updated contact/portfolio links (LinkedIn, GitHub, portfolio).
  4. Ask whether to include a **GDPR / RODO data processing consent clause** at the bottom of the CV (standard in Poland/EU; typically omitted for US/UK).

---

## Phase 4: Drafting & AI/ATS Optimization

Once the user answers the follow-up questions:

1. **Apply Optimization Rules**:
   Follow all guidelines in [references/ats-ai-optimization-guide.md](./references/ats-ai-optimization-guide.md) and structure templates in [references/cv-templates-and-clauses.md](./references/cv-templates-and-clauses.md):
   - **Zero Fabrication Policy**: Never invent employers, dates, degrees, skills, or fake metrics. If the user cannot provide an exact number for a bullet, frame the impact accurately using verified scope and qualitative outcomes confirmed by the user.
   - **Executive / Professional Summary**: Write a high-signal 3–4 line summary tailored to the target role, incorporating years of experience, core specialization, top achievements, and primary domain keywords.
   - **Categorized Skills Matrix**: Group hard skills logically (e.g., *Languages & Frameworks*, *Cloud & DevOps*, *Product & Leadership*, *Tools & Platforms*) using canonical industry names alongside common abbreviations (e.g., `Search Engine Optimization (SEO)`, `Continuous Integration / Continuous Deployment (CI/CD)`).
   - **High-Impact Experience Bullets**: Rewrite bullets using strong action verbs and the **XYZ / CAR** pattern. Highlight key metrics and outcomes in **bold** for rapid human & AI scanning.
   - **ATS-Clean Formatting**: Single-column flow, standard section headings in the chosen language, consistent `MM/YYYY – MM/YYYY` (or `YYYY-MM`) dates, reverse-chronological order.

2. **Save Structured Markdown Draft**:
   - Save the complete CV in clean Markdown format in the workspace (e.g., `CV_<FirstName>_<LastName>_<LANG>.md`), following the structure in [examples/sample-optimized-cv.md](./examples/sample-optimized-cv.md).

---

## Phase 5: Creating the Google Docs CV

Create the final Google Docs version using the following hybrid procedure:

### Path A: Native Google Docs Plugin (`gdocs`) — Primary Method
1. Check whether the **Google Docs** plugin (`antigravity-plugins-official/plugin/gdocs`) tools/CLI are available in your environment:
   - Check connected accounts via `list_plugin_accounts` if available.
   - If the Google Docs plugin is installed and authenticated, create a new Google Doc titled `CV - <Full Name> - <Target Role> (<LANG>)` and populate it with the full optimized CV using clean semantic styles (`Title`, `Heading 1`, `Heading 2`, bullet lists, and bold emphasis).
   - Return the direct clickable Google Docs link to the user.

### Path B: Google-Docs-Ready `.docx` Generation — Always Run (Local File & Fallback)
1. Regardless of whether Path A is available, **always** generate a cleanly formatted, ATS-compliant `.docx` document using the bundled converter script:
   ```bash
   python3 ./scripts/export_cv_docx.py "<path-to-markdown-cv.md>" "<output-cv.docx>"
   ```
   *(Resolve `./scripts/export_cv_docx.py` relative to this `SKILL.md` directory.)*
2. **Validation Step**:
   - Verify that the script exits with code `0` and the `.docx` file is non-empty.
   - If the workspace directory is inside Google Drive (e.g., `GoogleDrive-...` / `Mój dysk`), inform the user that the `.docx` file is automatically synced to their Google Drive and can be opened directly as a native **Google Docs** document in one click with 100% preserved ATS-safe styling.
3. **Suggesting the Google Docs Plugin (if not installed)**:
   - If the `gdocs` plugin (`antigravity-plugins-official/plugin/gdocs`) is not installed in the current environment, include its plugin card at the end of your response so the user can optionally install it for direct cloud Google Docs creation:
     `<plugin-card catalog-id="antigravity-plugins-official/plugin/gdocs"></plugin-card>`

---

## Post-Generation Review Loop

After delivering the Google Docs link / `.docx` file and Markdown source:
- Highlight the **top 5 improvements** made compared to the old CV(s).
- Ask if the user would like to:
  1. Adjust any bullet points, tone, or length (e.g., condensing to a strict 1-page or 2-page layout),
  2. Generate an additional language version (e.g., both Polish and English), or
  3. Tailor a variant specifically for a concrete job posting.
