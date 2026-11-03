# CV Structure Templates, Section Headers & GDPR/RODO Clauses

Use this reference in **Phase 4 (Drafting & Optimization)** to ensure the generated Markdown and Google Docs CV uses standard, ATS-recognized section headings and clean hierarchy.

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

## 2. Canonical Markdown Template (Input for `export_cv_docx.py` & Google Docs)

When saving the optimized CV in Markdown (`CV_<Name>_<LANG>.md`), follow this exact heading hierarchy so both the Google Docs plugin (`gdocs`) and `scripts/export_cv_docx.py` render it into a crisp, executive document:

```markdown
# FULL NAME
**Target Role Title / Headline**
City, Country | Phone | email@example.com | linkedin.com/in/username | github.com/username

## Professional Summary
Results-driven [Target Role] with [X]+ years of experience in [Core Domains]. Proven track record of [Top Achievement 1 with metric] and [Top Achievement 2 with metric]. Expert in [Key Skill 1], [Key Skill 2], and [Key Skill 3].

## Work Experience

### Job Title | Company Name
*Location (Remote / Hybrid / On-site) | MM/YYYY – Present*
- **[Action Verb] [Outcome + Metric]** by implementing [Method/Technology] across [Scope].
- **[Action Verb] [Outcome + Metric]**, reducing [Problem] from [X] to [Y] through [Action].
- **[Action Verb] [Scope/Team]** to deliver [Project/Product] on schedule and within [Budget/SLA].

### Previous Job Title | Previous Company Name
*Location | MM/YYYY – MM/YYYY*
- **[Action Verb] [Outcome + Metric]** using [Tools/Skills] for [Client/System scale].
- **[Action Verb] [Outcome + Metric]** by redesigning [Process/Architecture].

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
