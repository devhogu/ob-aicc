# Document assessment report: Statement of Intent

| Field | Entry |
| --- | --- |
| Document | Statement of Intent, version 0.5, `charter/statement-of-intent.md` |
| Document Class | A |
| Assessment | 2026-09-30 |
| Assessor | Delivery Lead (first Assessment prepared for the AICC Lead) |
| Author | AICC Lead |
| Status in header | draft |
| Readiness Level | R3 |
| Lines | 312 |

## 1. Scores

| Criterion | Score (0 to 3) | Failed items |
| --- | --- | --- |
| D-1 Intent fit | 3 | D-1.3, D-1.4 |
| D-2 Structure fit | 3 | D-2.2, D-2.5 |
| D-3 Completeness | 3 | none |
| D-4 Vocabulary and style | 3 | D-4.2 |
| D-5 Internal consistency | 3 | none |
| D-6 Cross-document consistency | 2 | D-6.2, D-6.3 |
| D-7 Traceability | 3 | none |
| D-8 Operability | 3 | none |
| D-9 Proportionality | 3 | none |
| D-10 Currency and governance | 2 | D-10.4 |

## 2. Findings

| Finding | Category | Severity | Failed items | Evidence | Recommendation | Owner | Wave |
| --- | --- | --- | --- | --- | --- | --- | --- |
| F-001 | non-conformance | Minor | D-2.2 | The header title differs from the title in the register and from the title-case rule. The Statement of Intent has three titles: "Statement of Intent" (register), "Statement of Intent on the Adoption of Artificial Intelligence" (heading), and "AI adoption statement of intent" (header). The Operating Model and the Vocabulary and Style have an "AICC" prefix in the header only. The other headers use sentence case. | Set one canonical title for each document, in title case, and use it in the header, the heading, the Charter README, and the Document Control. | AICC Lead | 1 |
| F-003 | non-conformance | Minor | D-4.2 | Defined terms and document titles appear in lower case: "delivery backlog" (Operating Model 12.1), "AI incident policy" (Operating Model 8.1), "data classification rules" (Statement of Intent, Roles), and "AI use policy" (Statement of Intent 11.3). | Use the defined term, or the document title, with capitals. | AICC Lead | 1 |
| F-004 | drift | Major | D-10.4 | The published portal (html/aicc) shows the v0.1 Statement of Intent, imported at wiki revision add2031: six principles, no Maturity Roadmap, no governance section. The charter version is v0.5. The import records a source path, wiki/statement-of-intent.md, that no longer exists. | After approval, regenerate the portal page from the charter folder. Until then, mark the published page as superseded. Add a drift check to the Assessment. | AICC Lead | 5 |
| F-005 | duplication | Minor | D-6.3 | "Domain" is defined in three documents (Statement of Intent 1.1, Operating Model 7.4, Vocabulary) and "Entity" and "Participating Entity" in two, each in different words. The membership of the AI Steering Committee is described in four places (Statement of Intent 7.5, Operating Model 5.2, Roles 2.2, Governance Forums 4.3). | Keep one definition in the Vocabulary and Style. The Statement of Intent may repeat its definitions verbatim because it is read alone. Define the membership of the AI Steering Committee in the Governance Forums and refer to it elsewhere. | AICC Lead | 1 |
| F-007 | ghost | Major | D-6.2 | The AI Risk Appetite Statement is required (Statement of Intent 7.7, the Strategic Decision Category, the Executive Sponsor Role, and a row of the Decision Rights) but exists only as a phrase in the stub of the AICC Charter. The Vocabulary defines it as a statement, not as a section. | Decide whether it is a section of the AICC Charter or a document of its own, and write it. State the decision in the Document Control. | AICC Lead | 2 |
| F-013 | incoherence | Minor | D-2.5, D-1.3 | The Statement is written for the Board, regulators, and investors, but at 312 lines it carries operating detail: capability and enablers (section 10), the platform capability by level (11.2), and the measures by level (11.3). | Move sections 11.2 and 11.3 to an annex or to the Metrics, and reduce section 10 to commitments. | AICC Lead | 4 |
| F-018 | gap | Minor | D-1.4 | The header has no Document Class field, so the class cannot be checked mechanically. The next review date is "none" in every document. | Add a class field to the header and to the header rule in the Charter README, and set the next review date at approval. | AICC Lead | 1 |
| F-030 | gap | Minor | none | No Russian version of any document exists, although the portal is Russian-first. | Produce the Russian versions after approval. State the source version in each. | AICC Lead | 5 |

## 3. Recommendations

1. (Wave 1: conformance) Set one canonical title for each document, in title case, and use it in the header, the heading, the Charter README, and the Document Control. Closes F-001.
2. (Wave 1: conformance) Use the defined term, or the document title, with capitals. Closes F-003.
3. (Wave 1: conformance) Keep one definition in the Vocabulary and Style. The Statement of Intent may repeat its definitions verbatim because it is read alone. Define the membership of the AI Steering Committee in the Governance Forums and refer to it elsewhere. Closes F-005.
4. (Wave 1: conformance) Add a class field to the header and to the header rule in the Charter README, and set the next review date at approval. Closes F-018.
5. (Wave 2: close ghosts, gaps, and contradictions) Decide whether it is a section of the AICC Charter or a document of its own, and write it. State the decision in the Document Control. Closes F-007.
6. (Wave 4: proportionality) Move sections 11.2 and 11.3 to an annex or to the Metrics, and reduce section 10 to commitments. Closes F-013.
7. (Wave 5: operate and publish) After approval, regenerate the portal page from the charter folder. Until then, mark the published page as superseded. Add a drift check to the Assessment. Closes F-004.
8. (Wave 5: operate and publish) Produce the Russian versions after approval. State the source version in each. Closes F-030.

## 4. Result

The document is at Readiness Level R3. It is accepted for consultation. It is accepted for approval when the open findings above Minor are closed.
