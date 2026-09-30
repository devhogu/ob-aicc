# Document assessment report: Governance Forums

| Field | Entry |
| --- | --- |
| Document | Governance Forums, version 0.1, `charter/governance-forums.md` |
| Document Class | A |
| Assessment | 2026-09-30 |
| Assessor | Delivery Lead (first Assessment prepared for the AICC Lead) |
| Author | AICC Lead |
| Status in header | draft |
| Readiness Level | R2 |
| Lines | 206 |

## 1. Scores

| Criterion | Score (0 to 3) | Failed items |
| --- | --- | --- |
| D-1 Intent fit | 3 | D-1.4 |
| D-2 Structure fit | 3 | D-2.2, D-2.6 |
| D-3 Completeness | 3 | none |
| D-4 Vocabulary and style | 2 | D-4.3 |
| D-5 Internal consistency | 3 | none |
| D-6 Cross-document consistency | 3 | D-6.3, D-6.5 |
| D-7 Traceability | 2 | D-7.4 |
| D-8 Operability | 2 | D-8.1, D-8.3, D-8.4 |
| D-9 Proportionality | 2 | D-9.1 |
| D-10 Currency and governance | 3 | none |

## 2. Findings

| Finding | Category | Severity | Failed items | Evidence | Recommendation | Owner | Wave |
| --- | --- | --- | --- | --- | --- | --- | --- |
| F-001 | non-conformance | Minor | D-2.2 | The header title differs from the title in the register and from the title-case rule. The Statement of Intent has three titles: "Statement of Intent" (register), "Statement of Intent on the Adoption of Artificial Intelligence" (heading), and "AI adoption statement of intent" (header). The Operating Model and the Vocabulary and Style have an "AICC" prefix in the header only. The other headers use sentence case. | Set one canonical title for each document, in title case, and use it in the header, the heading, the Charter README, and the Document Control. | AICC Lead | 1 |
| F-002 | misalignment | Minor | D-6.5 | The Templates, and the file names, are called "Steering Committee agenda" and "Steering Committee minutes", while the Forum and the Vocabulary use "AI Steering Committee". | Rename the Templates and files to "AI Steering Committee agenda" and "AI Steering Committee minutes" and update the lists that name them. | AICC Lead | 1 |
| F-005 | duplication | Minor | D-6.3 | "Domain" is defined in three documents (Statement of Intent 1.1, Operating Model 7.4, Vocabulary) and "Entity" and "Participating Entity" in two, each in different words. The membership of the AI Steering Committee is described in four places (Statement of Intent 7.5, Operating Model 5.2, Roles 2.2, Governance Forums 4.3). | Keep one definition in the Vocabulary and Style. The Statement of Intent may repeat its definitions verbatim because it is read alone. Define the membership of the AI Steering Committee in the Governance Forums and refer to it elsewhere. | AICC Lead | 1 |
| F-012 | overengineering | Major | D-9.1 | Eight Forums, eight Registers, 23 Templates, and nine AICC Services are active on paper, while no Role has a Holder. The counts are at or near the limits of the complexity budget. No document states the Maturity Level from which each construct is active. | Write an activation schedule in the Evolution Plan: for each Forum, Register, Template, and AICC Service, the Maturity Level from which it is active. Start with a core set. Mark the rest dormant. | AICC Lead | 4 |
| F-015 | non-conformance | Minor | D-2.6 | Figures are numbered 1 to 7 across five documents, and the rule for numbering is not stated. Numbers will collide when a document changes. | State in the Vocabulary and Style 3.13 that figures are numbered within the document, and renumber. | AICC Lead | 1 |
| F-016 | non-conformance | Major | D-4.3 | Capitalized terms are used but not defined: Chair, written procedure, Quarterly Report, Domain engagement record, Use Case card, and Change history. "Secretary" is defined and is not used in its capitalized form. | Define the terms that are used, and use "Secretary" as defined or remove it. | AICC Lead | 1 |
| F-017 | gap | Major | D-8.1 | The Register of Appointments holds no Holder for any Role. No Forum has a named chair or secretary. | Complete the Register, beginning with the Executive Sponsor and the AICC Lead, and record the Roles that the AICC Lead holds. | AICC Lead | 5 |
| F-018 | gap | Minor | D-1.4 | The header has no Document Class field, so the class cannot be checked mechanically. The next review date is "none" in every document. | Add a class field to the header and to the header rule in the Charter README, and set the next review date at approval. | AICC Lead | 1 |
| F-019 | gap | Minor | D-8.4 | Periods, hours, and intervals (two, five, and ten working days, one hour, every two weeks, each six months) are stated in six documents and have not been tested against staffing or against the Control Functions. | Gather the parameters in one table, and have the Control Functions and the AI Steering Committee confirm them. | AICC Lead | 3 |
| F-029 | gap | Major | D-7.4 | Secretaries are named only for the AI Steering Committee. The other Forums have a chair and no secretary, and the deputy of a chair is not stated. The Roles do not state the duties of a secretary. | Assign the secretary of each Forum in the Governance Forums and state the secretary duties in the Roles. | AICC Lead | 2 |
| F-033 | gap | Major | D-8.3 | No procedure has been run: there is no Decision Record, no minutes, no backlog entry, and no register entry. The Templates have not been used. | Run each core procedure once, with the Template, and correct the documents from the experience. | AICC Lead | 5 |

## 3. Recommendations

1. (Wave 1: conformance) Set one canonical title for each document, in title case, and use it in the header, the heading, the Charter README, and the Document Control. Closes F-001.
2. (Wave 1: conformance) Rename the Templates and files to "AI Steering Committee agenda" and "AI Steering Committee minutes" and update the lists that name them. Closes F-002.
3. (Wave 1: conformance) Keep one definition in the Vocabulary and Style. The Statement of Intent may repeat its definitions verbatim because it is read alone. Define the membership of the AI Steering Committee in the Governance Forums and refer to it elsewhere. Closes F-005.
4. (Wave 1: conformance) State in the Vocabulary and Style 3.13 that figures are numbered within the document, and renumber. Closes F-015.
5. (Wave 1: conformance) Define the terms that are used, and use "Secretary" as defined or remove it. Closes F-016.
6. (Wave 1: conformance) Add a class field to the header and to the header rule in the Charter README, and set the next review date at approval. Closes F-018.
7. (Wave 2: close ghosts, gaps, and contradictions) Assign the secretary of each Forum in the Governance Forums and state the secretary duties in the Roles. Closes F-029.
8. (Wave 3: write the stub documents and confirm the parameters) Gather the parameters in one table, and have the Control Functions and the AI Steering Committee confirm them. Closes F-019.
9. (Wave 4: proportionality) Write an activation schedule in the Evolution Plan: for each Forum, Register, Template, and AICC Service, the Maturity Level from which it is active. Start with a core set. Mark the rest dormant. Closes F-012.
10. (Wave 5: operate and publish) Complete the Register, beginning with the Executive Sponsor and the AICC Lead, and record the Roles that the AICC Lead holds. Closes F-017.
11. (Wave 5: operate and publish) Run each core procedure once, with the Template, and correct the documents from the experience. Closes F-033.

## 4. Result

The document is at Readiness Level R2. It is not accepted for consultation.
