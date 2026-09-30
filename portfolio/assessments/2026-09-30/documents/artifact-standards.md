# Document assessment report: Artifact Standards

| Field | Entry |
| --- | --- |
| Document | Artifact Standards, version 0.1, `charter/artifact-standards.md` |
| Document Class | C |
| Assessment | 2026-09-30 |
| Assessor | Delivery Lead (first Assessment prepared for the AICC Lead) |
| Author | AICC Lead |
| Status in header | draft |
| Readiness Level | R2 |
| Lines | 135 |

## 1. Scores

| Criterion | Score (0 to 3) | Failed items |
| --- | --- | --- |
| D-1 Intent fit | 3 | D-1.4 |
| D-2 Structure fit | 3 | D-2.2, D-2.6 |
| D-3 Completeness | 2 | D-3.3 |
| D-4 Vocabulary and style | 3 | none |
| D-5 Internal consistency | 3 | none |
| D-6 Cross-document consistency | 3 | D-6.3, D-6.5 |
| D-7 Traceability | 3 | none |
| D-8 Operability | 2 | D-8.3 |
| D-9 Proportionality | 2 | D-9.1 |
| D-10 Currency and governance | 3 | none |

## 2. Findings

| Finding | Category | Severity | Failed items | Evidence | Recommendation | Owner | Wave |
| --- | --- | --- | --- | --- | --- | --- | --- |
| F-001 | non-conformance | Minor | D-2.2 | The header title differs from the title in the register and from the title-case rule. The Statement of Intent has three titles: "Statement of Intent" (register), "Statement of Intent on the Adoption of Artificial Intelligence" (heading), and "AI adoption statement of intent" (header). The Operating Model and the Vocabulary and Style have an "AICC" prefix in the header only. The other headers use sentence case. | Set one canonical title for each document, in title case, and use it in the header, the heading, the Charter README, and the Document Control. | AICC Lead | 1 |
| F-002 | misalignment | Minor | D-6.5 | The Templates, and the file names, are called "Steering Committee agenda" and "Steering Committee minutes", while the Forum and the Vocabulary use "AI Steering Committee". | Rename the Templates and files to "AI Steering Committee agenda" and "AI Steering Committee minutes" and update the lists that name them. | AICC Lead | 1 |
| F-006 | duplication | Minor | D-6.3 | The Role codes are listed in Roles 7.1 and Decision Rights 2.2. The Template list is in Artifact Standards 5.1 and the Templates index. The rules of status, header, and promotion are in Charter README 3 to 5 and in the Document Control. The engagement of a Domain is in Operating Model 13 and Portfolio Management 5. | Keep each in one place and refer to it from the other: codes in Roles, the Template list in the Templates index, status and promotion in the Document Control, and the engagement sequence in the Operating Model. | AICC Lead | 1 |
| F-012 | overengineering | Major | D-9.1 | Eight Forums, eight Registers, 23 Templates, and nine AICC Services are active on paper, while no Role has a Holder. The counts are at or near the limits of the complexity budget. No document states the Maturity Level from which each construct is active. | Write an activation schedule in the Evolution Plan: for each Forum, Register, Template, and AICC Service, the Maturity Level from which it is active. Start with a core set. Mark the rest dormant. | AICC Lead | 4 |
| F-015 | non-conformance | Minor | D-2.6 | Figures are numbered 1 to 7 across five documents, and the rule for numbering is not stated. Numbers will collide when a document changes. | State in the Vocabulary and Style 3.13 that figures are numbered within the document, and renumber. | AICC Lead | 1 |
| F-018 | gap | Minor | D-1.4 | The header has no Document Class field, so the class cannot be checked mechanically. The next review date is "none" in every document. | Add a class field to the header and to the header rule in the Charter README, and set the next review date at approval. | AICC Lead | 1 |
| F-022 | gap | Major | D-3.3 | No rule states the classification of the Records and the documents, or where the repository may be hosted. The content is internal to the Bank and the repository is hosted at an external code-hosting service. | State the classification and the hosting rule, and confirm the visibility of the repository with information security. | AICC Lead | 2 |
| F-033 | gap | Major | D-8.3 | No procedure has been run: there is no Decision Record, no minutes, no backlog entry, and no register entry. The Templates have not been used. | Run each core procedure once, with the Template, and correct the documents from the experience. | AICC Lead | 5 |

## 3. Recommendations

1. (Wave 1: conformance) Set one canonical title for each document, in title case, and use it in the header, the heading, the Charter README, and the Document Control. Closes F-001.
2. (Wave 1: conformance) Rename the Templates and files to "AI Steering Committee agenda" and "AI Steering Committee minutes" and update the lists that name them. Closes F-002.
3. (Wave 1: conformance) Keep each in one place and refer to it from the other: codes in Roles, the Template list in the Templates index, status and promotion in the Document Control, and the engagement sequence in the Operating Model. Closes F-006.
4. (Wave 1: conformance) State in the Vocabulary and Style 3.13 that figures are numbered within the document, and renumber. Closes F-015.
5. (Wave 1: conformance) Add a class field to the header and to the header rule in the Charter README, and set the next review date at approval. Closes F-018.
6. (Wave 2: close ghosts, gaps, and contradictions) State the classification and the hosting rule, and confirm the visibility of the repository with information security. Closes F-022.
7. (Wave 4: proportionality) Write an activation schedule in the Evolution Plan: for each Forum, Register, Template, and AICC Service, the Maturity Level from which it is active. Start with a core set. Mark the rest dormant. Closes F-012.
8. (Wave 5: operate and publish) Run each core procedure once, with the Template, and correct the documents from the experience. Closes F-033.

## 4. Result

The document is at Readiness Level R2. It is not accepted for consultation.
