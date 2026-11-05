# CV Structure Templates, Section Headers & GDPR/RODO Clauses

Use this reference in **Phase 4 (Drafting & Optimization)** to ensure the generated Markdown and Google Docs CV uses standard, ATS-recognized section headings, `https://` links, and clean hierarchy.

---

## 1. Standard ATS Section Headings by Language

Always use these canonical section titles so ATS parsers classify every section with 100% confidence:

| Section Concept | English (EN) | Polish (PL) | German (DE) | Spanish (ES) |
| :--- | :--- | :--- | :--- | :--- |
| **Summary** | Professional Summary | Podsumowanie zawodowe | Profil / Zusammenfassung | Resumen Profesional |
| **Experience** | Work Experience | Doświadczenie zawodowe | Berufserfahrung | Experiencia Laboral |
| **Skills** | Skills & Competencies | Umiejętności | Kenntnisse & Fähigkeiten | Habilidades |
| **Education** | Education | Wykształcenie | Ausbildung / Studium | Educación |
| **Certifications** | Certifications & Courses | Certyfikaty i szkolenia | Zertifikate & Weiterbildung | Certificaciones |
| **Projects** | Key Projects | Wybrane projekty | Ausgewählte Projekte | Proyectos Destacados |
| **Languages** | Languages | Języki obce | Sprachen | Idiomas |
| **GDPR / Consent** | Data Protection Clause | Klauzula RODO | Datenschutzerklärung | Cláusula de Privacidad |

---

## 2. Canonical Markdown Template (Input for Google Docs)

When saving the optimized CV in Markdown (`CV_<FirstName>_<LastName>_<LANG>.md`), ensure:
- The **document length** stays within **at most 3 pages**.
- The **filename** contains **only basic English ASCII characters** (`A-Z`, `a-z`, `0-9`, `_`, `-`, `.`), with all diacritics transliterated (`ą→a`, `ł→l`, `ó→o`, `ż→z`, etc.).
- Every link in the document includes **`https://`**.
- The **Professional Summary** is **3–4 sentences**, caps experience at **`20+` years** (`ponad 20 lat` in Polish if >20), and does **not** repeat specific technologies or specific achievements/items already written under individual job positions.
- **Avoid redundant repetitions** such as `"2-krotnie (2x)"` or `"50 procent (50%)"`.
- **Roles from 12+ years ago** are condensed to 1–2 brief bullets.

```markdown
# FULL NAME
**Target Role Title / Headline**
City, Country | Phone | email@example.com | https://linkedin.com/in/username | https://github.com/username

## Professional Summary
Results-driven [Target Role] with [X or max 20+] years of experience designing, scaling, and governing mission-critical systems across [Core Domains / Industries]. Specializes in transforming legacy architectures into resilient, high-availability platforms while optimizing operational efficiency at scale. Adept at leading cross-functional engineering teams, mentoring technical talent, and aligning product delivery with strategic business objectives.

## Work Experience

### Job Title | Company Name
*Location (Remote / Hybrid / On-site) | MM/YYYY – Present*
- **[Action Verb] [Measurable Outcome + Metric]** by implementing [Method/Technology] across [Scope].
- **[Action Verb] [Measurable Outcome + Metric]**, reducing [Problem] from [X] to [Y] through [Action].
- **[Action Verb] [Scope/Team]** to deliver [Project/Product] on schedule and within [Budget/SLA].

### Previous Job Title | Previous Company Name
*Location | MM/YYYY – MM/YYYY*
- **[Action Verb] [Measurable Outcome + Metric]** using [Tools/Skills] for [Client/System scale].
- **[Action Verb] [Measurable Outcome + Metric]** by redesigning [Process/Architecture].

### Early Career Job Title (12+ Years Ago — Condensed) | Legacy Company Name
*Location | MM/YYYY – MM/YYYY*
- **[Brief 1-line summary of scope and key measurable outcome without verbose detail].**

## Skills & Competencies
- **Core Technical Skills:** Skill A, Skill B, Skill C, Skill D
- **Tools & Platforms:** Tool 1, Tool 2, Tool 3, Tool 4
- **Methodologies & Domain:** Agile/Scrum, CI/CD, System Architecture, Stakeholder Management

## Education

### Degree Title in Field of Study | University Name
*Location | YYYY – YYYY*
- Optional: Specialization, honors, GPA (if high and recent), or relevant thesis topic.

## Certifications & Courses
- **Certification Name** – Issuing Organization (YYYY)
- **Certification Name** – Issuing Organization (YYYY)

## Languages
- **Language 1:** Native / C2
- **Language 2:** Fluent / Full Professional Proficiency (C1)

---
*Optional GDPR / RODO consent clause at the very bottom*
```

---

## 3. Standard GDPR / RODO Consent Clauses

Include at the bottom of the CV **only if requested or confirmed by the user** (standard in Poland; optional elsewhere in the EU; omit for US/UK/CA/AU).

### Polish (Klauzula RODO – uniwersalna: obecna i przyszłe rekrutacje)
> *Wyrażam zgodę na przetwarzanie moich danych osobowych dla potrzeb niezbędnych do realizacji obecnego oraz przyszłych procesów rekrutacji (zgodnie z Rozporządzeniem Parlamentu Europejskiego i Rady (UE) 2016/679 z dnia 27 kwietnia 2016 r. – RODO oraz ustawą z dnia 10 maja 2018 r. o ochronie danych osobowych).*

### English (GDPR Consent Clause – Current & Future Recruitments)
> *I hereby give consent for my personal data included in my application to be processed for the purposes of the current and future recruitment processes in accordance with Regulation (EU) 2016/679 of the European Parliament and of the Council of 27 April 2016 (GDPR).*

### German (DSGVO-Einwilligung)
> *Ich stimme der Verarbeitung meiner personenbezogenen Daten zum Zwecke des aktuellen sowie zukünftiger Bewerbungsverfahren gemäß der Datenschutz-Grundverordnung (DSGVO) zu.*

---

## 4. Google Docs Page Layout & Pagination Batch Recipe (A4 + 1.25 cm Margins)

When creating the Google Docs document in **Phase 5**, always create it as a paginated document (`--pageless=false`) and apply the following `raw` batch operations via `gdocs mutate batch DOC_ID -f layout.json`:

- **A4 Page Size**: `595.28 × 841.89 PT` (`210 × 297 mm`)
- **Margins**: `1.25 cm = 35.43 PT` on all four sides (`marginTop`, `marginBottom`, `marginLeft`, `marginRight`)
- **Paragraph Pagination**: `keepWithNext: true`, `keepLinesTogether: true`, `avoidWidowAndOrphan: true`

```json
[
  {
    "op": "raw",
    "raw_request": {
      "updateDocumentStyle": {
        "documentStyle": {
          "pageSize": {
            "width": {"magnitude": 595.28, "unit": "PT"},
            "height": {"magnitude": 841.89, "unit": "PT"}
          },
          "marginTop": {"magnitude": 35.43, "unit": "PT"},
          "marginBottom": {"magnitude": 35.43, "unit": "PT"},
          "marginLeft": {"magnitude": 35.43, "unit": "PT"},
          "marginRight": {"magnitude": 35.43, "unit": "PT"}
        },
        "fields": "pageSize,marginTop,marginBottom,marginLeft,marginRight"
      }
    }
  },
  {
    "op": "raw",
    "raw_request": {
      "updateParagraphStyle": {
        "range": {
          "startIndex": 1,
          "endIndex": END_INDEX_OF_DOCUMENT
        },
        "paragraphStyle": {
          "keepWithNext": true,
          "keepLinesTogether": true,
          "avoidWidowAndOrphan": true
        },
        "fields": "keepWithNext,keepLinesTogether,avoidWidowAndOrphan"
      }
    }
  }
]
```
*(Replace `END_INDEX_OF_DOCUMENT` with the document's final body character index obtained from `gdocs readonly structure DOC_ID --json` or `gdocs readonly dump-body DOC_ID`.)*
