# Document assessment report: Decision Rights

| Field | Entry |
| --- | --- |
| Document | Decision Rights, version 0.4, `charter/decision-rights.md` |
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
| D-2 Structure fit | 3 | D-2.2 |
| D-3 Completeness | 3 | none |
| D-4 Vocabulary and style | 3 | none |
| D-5 Internal consistency | 3 | none |
| D-6 Cross-document consistency | 1 | D-6.1, D-6.2, D-6.3 |
| D-7 Traceability | 3 | none |
| D-8 Operability | 2 | D-8.3 |
| D-9 Proportionality | 3 | none |
| D-10 Currency and governance | 3 | none |

## 2. Findings

| Finding | Category | Severity | Failed items | Evidence | Recommendation | Owner | Wave |
| --- | --- | --- | --- | --- | --- | --- | --- |
| F-001 | non-conformance | Minor | D-2.2 | The header title differs from the title in the register and from the title-case rule. The Statement of Intent has three titles: "Statement of Intent" (register), "Statement of Intent on the Adoption of Artificial Intelligence" (heading), and "AI adoption statement of intent" (header). The Operating Model and the Vocabulary and Style have an "AICC" prefix in the header only. The other headers use sentence case. | Set one canonical title for each document, in title case, and use it in the header, the heading, the Charter README, and the Document Control. | AICC Lead | 1 |
| F-006 | duplication | Minor | D-6.3 | The Role codes are listed in Roles 7.1 and Decision Rights 2.2. The Template list is in Artifact Standards 5.1 and the Templates index. The rules of status, header, and promotion are in Charter README 3 to 5 and in the Document Control. The engagement of a Domain is in Operating Model 13 and Portfolio Management 5. | Keep each in one place and refer to it from the other: codes in Roles, the Template list in the Templates index, status and promotion in the Document Control, and the engagement sequence in the Operating Model. | AICC Lead | 1 |
| F-007 | ghost | Major | D-6.2 | The AI Risk Appetite Statement is required (Statement of Intent 7.7, the Strategic Decision Category, the Executive Sponsor Role, and a row of the Decision Rights) but exists only as a phrase in the stub of the AICC Charter. The Vocabulary defines it as a statement, not as a section. | Decide whether it is a section of the AICC Charter or a document of its own, and write it. State the decision in the Document Control. | AICC Lead | 2 |
| F-009 | misalignment | Blocker | D-6.1 | The Risk Tier Policy 4.1 requires a decision of the AI Steering Committee before a Risk Tier 4 Use Case is released. No Decision Category, forum agenda, or row of the Decision Rights provides that decision. | Add the decision to the Portfolio Decision Category, to the AI Steering Committee inputs, and to the Decision Rights. | AICC Lead | 2 |
| F-011 | misalignment | Blocker | D-6.1 | The owner of the Templates differs. The Roles and the Decision Rights make the Lead Architect accountable for setting standards and templates. Decision Management and the Document Control give the decision on Templates to the AICC Lead. | Decide: the AICC Lead approves all Templates, and the Lead Architect decides technical standards and technical patterns only. Correct the Roles and the Decision Rights. | AICC Lead | 2 |
| F-018 | gap | Minor | D-1.4 | The header has no Document Class field, so the class cannot be checked mechanically. The next review date is "none" in every document. | Add a class field to the header and to the header rule in the Charter README, and set the next review date at approval. | AICC Lead | 1 |
| F-033 | gap | Major | D-8.3 | No procedure has been run: there is no Decision Record, no minutes, no backlog entry, and no register entry. The Templates have not been used. | Run each core procedure once, with the Template, and correct the documents from the experience. | AICC Lead | 5 |

## 3. Recommendations

1. (Wave 1: conformance) Set one canonical title for each document, in title case, and use it in the header, the heading, the Charter README, and the Document Control. Closes F-001.
2. (Wave 1: conformance) Keep each in one place and refer to it from the other: codes in Roles, the Template list in the Templates index, status and promotion in the Document Control, and the engagement sequence in the Operating Model. Closes F-006.
3. (Wave 1: conformance) Add a class field to the header and to the header rule in the Charter README, and set the next review date at approval. Closes F-018.
4. (Wave 2: close ghosts, gaps, and contradictions) Decide whether it is a section of the AICC Charter or a document of its own, and write it. State the decision in the Document Control. Closes F-007.
5. (Wave 2: close ghosts, gaps, and contradictions) Add the decision to the Portfolio Decision Category, to the AI Steering Committee inputs, and to the Decision Rights. Closes F-009.
6. (Wave 2: close ghosts, gaps, and contradictions) Decide: the AICC Lead approves all Templates, and the Lead Architect decides technical standards and technical patterns only. Correct the Roles and the Decision Rights. Closes F-011.
7. (Wave 5: operate and publish) Run each core procedure once, with the Template, and correct the documents from the experience. Closes F-033.

## 4. Result

The document is at Readiness Level R2. It is not accepted for consultation. The Blocker findings are F-009, F-011.
