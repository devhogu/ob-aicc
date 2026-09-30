# Document assessment report: Document Control

| Field | Entry |
| --- | --- |
| Document | Document Control, version 0.1, `charter/document-control.md` |
| Document Class | A |
| Assessment | 2026-09-30 |
| Assessor | Delivery Lead (first Assessment prepared for the AICC Lead) |
| Author | AICC Lead |
| Status in header | draft |
| Readiness Level | R2 |
| Lines | 121 |

## 1. Scores

| Criterion | Score (0 to 3) | Failed items |
| --- | --- | --- |
| D-1 Intent fit | 3 | D-1.4 |
| D-2 Structure fit | 3 | D-2.2, D-2.6 |
| D-3 Completeness | 3 | none |
| D-4 Vocabulary and style | 2 | D-4.3 |
| D-5 Internal consistency | 3 | none |
| D-6 Cross-document consistency | 1 | D-6.1, D-6.3 |
| D-7 Traceability | 3 | none |
| D-8 Operability | 2 | D-8.3, D-8.4 |
| D-9 Proportionality | 3 | none |
| D-10 Currency and governance | 3 | none |

## 2. Findings

| Finding | Category | Severity | Failed items | Evidence | Recommendation | Owner | Wave |
| --- | --- | --- | --- | --- | --- | --- | --- |
| F-001 | non-conformance | Minor | D-2.2 | The header title differs from the title in the register and from the title-case rule. The Statement of Intent has three titles: "Statement of Intent" (register), "Statement of Intent on the Adoption of Artificial Intelligence" (heading), and "AI adoption statement of intent" (header). The Operating Model and the Vocabulary and Style have an "AICC" prefix in the header only. The other headers use sentence case. | Set one canonical title for each document, in title case, and use it in the header, the heading, the Charter README, and the Document Control. | AICC Lead | 1 |
| F-006 | duplication | Minor | D-6.3 | The Role codes are listed in Roles 7.1 and Decision Rights 2.2. The Template list is in Artifact Standards 5.1 and the Templates index. The rules of status, header, and promotion are in Charter README 3 to 5 and in the Document Control. The engagement of a Domain is in Operating Model 13 and Portfolio Management 5. | Keep each in one place and refer to it from the other: codes in Roles, the Template list in the Templates index, status and promotion in the Document Control, and the engagement sequence in the Operating Model. | AICC Lead | 1 |
| F-011 | misalignment | Blocker | D-6.1 | The owner of the Templates differs. The Roles and the Decision Rights make the Lead Architect accountable for setting standards and templates. Decision Management and the Document Control give the decision on Templates to the AICC Lead. | Decide: the AICC Lead approves all Templates, and the Lead Architect decides technical standards and technical patterns only. Correct the Roles and the Decision Rights. | AICC Lead | 2 |
| F-015 | non-conformance | Minor | D-2.6 | Figures are numbered 1 to 7 across five documents, and the rule for numbering is not stated. Numbers will collide when a document changes. | State in the Vocabulary and Style 3.13 that figures are numbered within the document, and renumber. | AICC Lead | 1 |
| F-016 | non-conformance | Major | D-4.3 | Capitalized terms are used but not defined: Chair, written procedure, Quarterly Report, Domain engagement record, Use Case card, and Change history. "Secretary" is defined and is not used in its capitalized form. | Define the terms that are used, and use "Secretary" as defined or remove it. | AICC Lead | 1 |
| F-018 | gap | Minor | D-1.4 | The header has no Document Class field, so the class cannot be checked mechanically. The next review date is "none" in every document. | Add a class field to the header and to the header rule in the Charter README, and set the next review date at approval. | AICC Lead | 1 |
| F-019 | gap | Minor | D-8.4 | Periods, hours, and intervals (two, five, and ten working days, one hour, every two weeks, each six months) are stated in six documents and have not been tested against staffing or against the Control Functions. | Gather the parameters in one table, and have the Control Functions and the AI Steering Committee confirm them. | AICC Lead | 3 |
| F-033 | gap | Major | D-8.3 | No procedure has been run: there is no Decision Record, no minutes, no backlog entry, and no register entry. The Templates have not been used. | Run each core procedure once, with the Template, and correct the documents from the experience. | AICC Lead | 5 |

## 3. Recommendations

1. (Wave 1: conformance) Set one canonical title for each document, in title case, and use it in the header, the heading, the Charter README, and the Document Control. Closes F-001.
2. (Wave 1: conformance) Keep each in one place and refer to it from the other: codes in Roles, the Template list in the Templates index, status and promotion in the Document Control, and the engagement sequence in the Operating Model. Closes F-006.
3. (Wave 1: conformance) State in the Vocabulary and Style 3.13 that figures are numbered within the document, and renumber. Closes F-015.
4. (Wave 1: conformance) Define the terms that are used, and use "Secretary" as defined or remove it. Closes F-016.
5. (Wave 1: conformance) Add a class field to the header and to the header rule in the Charter README, and set the next review date at approval. Closes F-018.
6. (Wave 2: close ghosts, gaps, and contradictions) Decide: the AICC Lead approves all Templates, and the Lead Architect decides technical standards and technical patterns only. Correct the Roles and the Decision Rights. Closes F-011.
7. (Wave 3: write the stub documents and confirm the parameters) Gather the parameters in one table, and have the Control Functions and the AI Steering Committee confirm them. Closes F-019.
8. (Wave 5: operate and publish) Run each core procedure once, with the Template, and correct the documents from the experience. Closes F-033.

## 4. Result

The document is at Readiness Level R2. It is not accepted for consultation. The Blocker findings are F-011.
