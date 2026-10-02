# Document assessment report: Risk Tier Policy

| Field | Entry |
| --- | --- |
| Document | Risk Tier Policy, version 0.1, `charter/policies/risk-tiers.md` |
| Document Class | B |
| Assessment | 2026-09-30 |
| Assessor | Delivery Lead (first Assessment prepared for the AICC Lead) |
| Author | AICC Lead |
| Status in header | draft |
| Readiness Level | R2 |
| Lines | 73 |

## 1. Scores

| Criterion | Score (0 to 3) | Failed items |
| --- | --- | --- |
| D-1 Intent fit | 3 | D-1.4 |
| D-2 Structure fit | 3 | D-2.2 |
| D-3 Completeness | 3 | none |
| D-4 Vocabulary and style | 3 | none |
| D-5 Internal consistency | 3 | none |
| D-6 Cross-document consistency | 1 | D-6.1 |
| D-7 Traceability | 3 | none |
| D-8 Operability | 3 | D-8.4 |
| D-9 Proportionality | 3 | none |
| D-10 Currency and governance | 3 | none |

## 2. Findings

| Finding | Category | Severity | Failed items | Evidence | Recommendation | Owner | Wave |
| --- | --- | --- | --- | --- | --- | --- | --- |
| F-001 | non-conformance | Minor | D-2.2 | The header title differs from the title in the register and from the title-case rule. The Statement of Intent has three titles: "Statement of Intent" (register), "Statement of Intent on the Adoption of Artificial Intelligence" (heading), and "AI adoption statement of intent" (header). The Operating Model and the Vocabulary and Style have an "AICC" prefix in the header only. The other headers use sentence case. | Set one canonical title for each document, in title case, and use it in the header, the heading, the Charter README, and the Document Control. | AICC Lead | 1 |
| F-009 | misalignment | Blocker | D-6.1 | The Risk Tier Policy 4.1 requires a decision of the AI Steering Committee before a Risk Tier 4 Use Case is released. No Decision Category, forum agenda, or row of the Decision Rights provides that decision. | Add the decision to the Portfolio Decision Category, to the AI Steering Committee inputs, and to the Decision Rights. | AICC Lead | 2 |
| F-018 | gap | Minor | D-1.4 | The header has no Document Class field, so the class cannot be checked mechanically. The next review date is "none" in every document. | Add a class field to the header and to the header rule in the Charter README, and set the next review date at approval. | AICC Lead | 1 |
| F-019 | gap | Minor | D-8.4 | Periods, hours, and intervals (two, five, and ten working days, one hour, every two weeks, each six months) are stated in six documents and have not been tested against staffing or against the Control Functions. | Gather the parameters in one table, and have the Control Functions and the AI Steering Committee confirm them. | AICC Lead | 3 |

## 3. Recommendations

1. (Wave 1: conformance) Set one canonical title for each document, in title case, and use it in the header, the heading, the Charter README, and the Document Control. Closes F-001.
2. (Wave 1: conformance) Add a class field to the header and to the header rule in the Charter README, and set the next review date at approval. Closes F-018.
3. (Wave 2: close ghosts, gaps, and contradictions) Add the decision to the Portfolio Decision Category, to the AI Steering Committee inputs, and to the Decision Rights. Closes F-009.
4. (Wave 3: write the stub documents and confirm the parameters) Gather the parameters in one table, and have the Control Functions and the AI Steering Committee confirm them. Closes F-019.

## 4. Result

The document is at Readiness Level R2. It is not accepted for consultation. The Blocker findings are F-009.
