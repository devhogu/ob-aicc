# Document assessment report: Data Classification Policy

| Field | Entry |
| --- | --- |
| Document | Data Classification Policy, version 0.0, `charter/policies/data-classification.md` |
| Document Class | B |
| Assessment | 2026-09-30 |
| Assessor | Delivery Lead (first Assessment prepared for the AICC Lead) |
| Author | AICC Lead |
| Status in header | stub |
| Readiness Level | R1 |
| Lines | 17 |

## 1. Scores

| Criterion | Score (0 to 3) | Failed items |
| --- | --- | --- |
| D-1 Intent fit | 2 | D-1.1, D-1.4 |
| D-2 Structure fit | 2 | D-2.2, D-2.3, D-2.4 |
| D-3 Completeness | 0 | D-3.1, D-3.2, D-3.3, D-3.4, D-3.5 |
| D-4 Vocabulary and style | 3 | none |
| D-5 Internal consistency | 3 | none |
| D-6 Cross-document consistency | 3 | none |
| D-7 Traceability | 2 | D-7.1 |
| D-8 Operability | 0 | all items (stub) |
| D-9 Proportionality | 3 | none |
| D-10 Currency and governance | 3 | none |

## 2. Findings

| Finding | Category | Severity | Failed items | Evidence | Recommendation | Owner | Wave |
| --- | --- | --- | --- | --- | --- | --- | --- |
| F-001 | non-conformance | Minor | D-2.2 | The header title differs from the title in the register and from the title-case rule. The Statement of Intent has three titles: "Statement of Intent" (register), "Statement of Intent on the Adoption of Artificial Intelligence" (heading), and "AI adoption statement of intent" (header). The Operating Model and the Vocabulary and Style have an "AICC" prefix in the header only. The other headers use sentence case. | Set one canonical title for each document, in title case, and use it in the header, the heading, the Charter README, and the Document Control. | AICC Lead | 1 |
| F-010 | gap | Blocker | D-3.1 | Eight documents that the Operating Model lists are stubs: the AICC Charter, Funding Model, Metrics, Evolution Plan, Enablement Plan, AI Use Policy, Data Classification Policy, and Third-Party AI Policy. Milestones MS-003 and MS-006 of the Portfolio Roadmap depend on them. | Write them in the order in section 8 of the corpus report, each to a stated minimum content. | AICC Lead | 3 |
| F-018 | gap | Minor | D-1.4 | The header has no Document Class field, so the class cannot be checked mechanically. The next review date is "none" in every document. | Add a class field to the header and to the header rule in the Charter README, and set the next review date at approval. | AICC Lead | 1 |
| F-032 | gap | Major | D-7.1 | The three policies must align with existing policies of the Bank (information classification, third-party risk management, and incident management), which have not been reviewed. The risk is duplication or conflict. | Obtain the existing policies and record how each policy builds on them before drafting. | AICC Lead | 3 |

The document is a stub. The items D-1.1, D-2.3, D-2.4, and D-3.1 to D-3.5 fail by rule.

## 3. Recommendations

1. (Wave 1: conformance) Set one canonical title for each document, in title case, and use it in the header, the heading, the Charter README, and the Document Control. Closes F-001.
2. (Wave 1: conformance) Add a class field to the header and to the header rule in the Charter README, and set the next review date at approval. Closes F-018.
3. (Wave 3: write the stub documents and confirm the parameters) Write them in the order in section 8 of the corpus report, each to a stated minimum content. Closes F-010.
4. (Wave 3: write the stub documents and confirm the parameters) Obtain the existing policies and record how each policy builds on them before drafting. Closes F-032.

Minimum content: the classes of data of the Bank, taken from its existing scheme and not invented; the models and services that each class may reach; where each may run; and the separation of data between Entities (F-032).

## 4. Result

The document is a stub at Readiness Level R1. It is not accepted for consultation.
