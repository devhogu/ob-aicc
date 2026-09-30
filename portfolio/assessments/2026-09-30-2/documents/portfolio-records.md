# Document assessment report: Records of the Portfolio

## 1. Header

| Field | Entry |
| --- | --- |
| Document | Records of the Portfolio, portfolio/ (excluding assessments) (Records (PRI, RMP, PBL, SPF, REG-xx, PRG-main, ...)) |
| Assessment | 2026-09-30, second Assessment (folder 2026-09-30-2) |
| Assessor | Independent assessor, not the author; the Delivery Lead Role has no Holder |
| Author | AICC Lead (owner of every document, Document Catalog 1.2) |
| Readiness Level | R2 |
| Previous Readiness Level | not assessed at a level |

## 2. Scores

Scores follow Corpus Assessment 7.1 from the failed items; severities are those of 6.2.

| Criterion | Score (0 to 3) | Failed items | Evidence |
| --- | --- | --- | --- |
| D-1 Intent fit | 3 | none | none |
| D-2 Structure fit | 3 | none | none |
| D-3 Completeness | 2 | D-3.5 | D-3.5 (Major): The Roadmap defines quarter 0 by an approval that has not occurred and enters no date; no Milestone can be due (F-070). |
| D-4 Vocabulary and style | 2 | D-4.1 | D-4.1 (Major): "approved" for documents and "Document Control" (roadmap.md MS-001, MS-003; assessments README "Not ready for approval") (F-043). |
| D-5 Internal consistency | 3 | none | none |
| D-6 Cross-document consistency | 1 | D-6.1 | D-6.1 (Blocker): The Records differ from the documents that define them: the identifiers are not in Artifact Standards 3.1; the AI Incident Register has no reporter; the AI Registry has no link; the Risk and Issue Register has no Finding column; PRI-3 is named "Adoption within business functions" against "Adoption within Domains" (F-054, F-063). |
| D-7 Traceability | 2 | D-7.2 | D-7.2 (Major): No location exists for the Domain engagement record, AI Incident Report, and Exception Request (F-054). |
| D-8 Operability | 1 | D-8.1, D-8.2, D-8.3 | D-8.1 (Major): The owners named in every Record header (Executive Sponsor, Portfolio Manager, Delivery Lead, AICC Lead, Platform Owner) have no Holder.; D-8.2 (Major): Twelve Records and five meeting folders presuppose keepers that are not recorded.; D-8.3 (Major): Every Record is empty; none has been used (F-031, F-033). |
| D-9 Proportionality | 3 | D-9.3 | D-9.3 (Minor): Every Record and five meeting folders are "Active" before any Use Case, Decision, or meeting exists. |
| D-10 Currency and governance | 2 | D-10.1, D-10.3 | D-10.1 (Minor): Every Record header holds "[date]" for the date of last change.; D-10.3 (Major): "Document Control" and "approved" remain in roadmap.md (F-043). |

## 3. Strengths

- Seeded for the whole flow: Strategic Priorities, both backlogs, Roadmaps, Service Portfolio, six Registers, Delivery Program, folders for minutes, reports, initiatives, and assessments.
- Every Record has a header with identifier, status, owner, date, and tracker reference (Artifact Standards 4.1).
- The seven Strategic Priorities agree in number and order with the Statement of Intent.

## 4. Findings

| Finding | Category | Severity | Evidence | Recommendation | Owner | Wave |
| --- | --- | --- | --- | --- | --- | --- |
| F-012 (continues) | overengineering | Major | Eight Forums, seven Registers, 23 Templates, and nine AICC Services are active on paper. No document states the Maturity Level from which each is active, so the Level 1 limits (five Forums, four Registers, ten Templates) cannot be met or tested. No Role has a Holder. The Evolution Plan, which is to hold the activation schedule, is a stub. Milestone MS-005 of the Portfolio Roadmap implies three Forums at Level 1 and no other document confirms it. | State in the Governance Forums, the Registers, the Document Catalog (Templates), and the Service Catalog the Maturity Level from which each construct is active, and mark the rest dormant. Start with the AI Steering Committee, Replenishment, and Delivery Review; the Decision, Risk and Issue, and AI Registry Registers; and ten Templates. | AICC Lead | 4 |
| F-017 (continues) | gap | Major | The Register of Appointments holds no Holder for any Role, including the Executive Sponsor and the AICC Lead. No Forum has a named chair or secretary. MS-002 is not evidenced. | Appoint the Executive Sponsor and the AICC Lead first, enter them with a date, then the other mandatory Roles, and record the Roles that the AICC Lead holds. | AICC Lead | 5 |
| F-031 (continues) | gap | Major | The Records are seeded and empty: no Investment Envelope, no Limit on Work in Progress, no date, no Decision Record, no Initiative, no Use Case. Every Record header holds "[date]" for the date of last change. | Enter the values as decisions are taken, beginning with the Strategic Priorities and the first Milestones. | AICC Lead | 5 |
| F-033 (continues) | gap | Major | No procedure has been run. There is no Decision Record, no minutes, no backlog entry, and no register entry. Of 23 Templates only the two assessment Templates have been used, and the first Assessment report did not follow the Corpus Assessment Report Template (its findings table has no Owner and Date columns and its sections are renamed). | Run each core procedure once with its Template (a Decision Record, an AI Steering Committee meeting, an Intake, a Risk Tier assessment) and correct the documents from the experience. | AICC Lead | 5 |
| F-043 (new) | legacy | Major | portfolio/roadmap.md: MS-001 lists "Document Control" as a document to be approved (the document no longer exists; the Document Catalog replaced it), uses "approved" for documents, and defines quarter 0 as "the approval of the Statement of Intent and the AICC Charter". MS-003 uses "Policies approved". portfolio/assessments/README.md says "Not ready for approval". | Replace "approved" by "activated", remove Document Control, name the documents of MS-001 by the Catalog, and define quarter 0 by the Decision Record of activation. | AICC Lead | 1 |
| F-044 (new) | legacy | Major | Superseded words remain. "approved" for documents: Corpus Assessment 1.3, D-10.4, C-8.1, 12.1; Artifact Standards 2.1 and Figure 7 ("approved documents of the charter folder"). The Corpus Assessment Report Template keeps a "Class" column and the level "R4 Approved" (the standard says R4 Active); the Document Assessment Template offers "accepted for consultation", a result the standard does not know. The AI Use Policy intent uses "AI tools", an excluded term. | Replace "approved" by "active" or "activated", and align both assessment Templates to sections 5 and 9 of the Corpus Assessment. | AICC Lead | 1 |
| F-054 (new) | gap | Major | Artifact Standards gives no location or identifier for the Domain Engagement Record, the AI Incident Report, and the Exception Request (the Use Case folder README lists the Records of a Use Case, but Figure 7 of the Artifact Standards does not). The seeded Records use identifiers that Artifact Standards 3.1 does not define: PRI, RMP, PBL, SPF, REG-DEC, REG-AI, REG-RSK, REG-INC, REG-EXC, REG-BEN, PRG-main, DBL-main, PRM-main, ROS-main. No status values are defined for a Record header (4.1) and all Records hold "Active". | Extend the Artifact Standards folder structure and identifier table to every Template and Record, and define the Record status values. | AICC Lead | 2 |
| F-062 (new) | gap | Major | Corpus Assessment 10.4 and Registers 3.3 require each open Finding to be tracked as an issue in the Risk and Issue Register with its identifier. The Register is empty; no finding of the first Assessment was entered. The Record has no column for the Finding identifier, and Registers 3.3 places the rule inside the field list. | Enter the open Findings of this report in the Register, add a Finding column, and move the rule in 3.3 to section 4. | AICC Lead | 2 |
| F-070 (new) | gap | Major | The Portfolio Roadmap has no dates. Quarter 0 depends on an approval that has not occurred, so no Milestone is due and none can be evidenced: MS-001 and MS-002 at quarter 0 have no evidence, and C-9.4 cannot be assessed. No Maturity Level is reached for any of the seven Strategic Priorities. | Fix the calendar: set quarter 0 by the Decision Record of activation, enter dates for MS-001 to MS-010, and review them at the next Assessment. | AICC Lead | 5 |
| F-052 (new) | misalignment | Minor | Smaller differences between documents. Governance Forums 5.4.3 requires a Decision Record for every design approval; Decision Management 2.1 and 3.1 require one only where more than one Domain is affected. Portfolio Management 3.3 has the Portfolio Manager keep the Delivery Backlog; Decision Rights 4.3 makes the Portfolio Manager only consulted. Decision Management 10.1 gives the identifier as "DR-year-number" and Artifact Standards as "DR-yyyy-nnn". portfolio/README.md makes the Portfolio Manager the owner of the Decision Records; Decision Management 4.6 has the secretary or Proposer write them. Decision Rights 2.3 lets each Control Function decide for itself; Risk Tier Policy 3.3 lets only model risk lower a Risk Tier. | Align the pairs in one change, with the Decision Rights as the source. | AICC Lead | 1 |
| F-063 (new) | misalignment | Minor | The Records differ from the documents that define them. portfolio/registers/ai-incident-register.md has no reporter (Registers 3.4); ai-registry.md has no link to the Use Case Record (3.2); the Risk and Issue Register has no Finding identifier (3.3). portfolio/priorities.md and roadmap.md name PRI-3 "Adoption within business functions"; Statement of Intent 9.4 names it "Adoption within Domains". Records show "Status: Active" and "[date]" although they hold no data. | Add the missing columns, use the Strategic Priority names of the Statement of Intent, and define what "Active" means for an empty Record. | AICC Lead | 1 |
| F-068 (new) | gap | Minor | The Community of Practice and the Stand-up have no Template and no Record location, and Replenishment, Delivery Review, Design Review, and Control Review use the general Meeting Agenda and Minutes (no Template for Design Review or Control Review outputs). portfolio/meetings holds folders for five Forums; the Delivery Review notes go to programs/main/reviews. | State in the Governance Forums which Forums keep minutes and where, and state that the Stand-up and the Community of Practice keep none. | AICC Lead | 1 |

## 5. Recommendations

1. (Wave 1, P2) Replace "approved" by "activated", remove Document Control, name the documents of MS-001 by the Catalog, and define quarter 0 by the Decision Record of activation. Closes F-043; raises D-4.1, D-10.3.
2. (Wave 1, P2) Replace "approved" by "active" or "activated", and align both assessment Templates to sections 5 and 9 of the Corpus Assessment. Closes F-044; raises D-4.1, D-6.1, D-10.3.
3. (Wave 1, P3) Align the pairs in one change, with the Decision Rights as the source. Closes F-052; raises D-6.1.
4. (Wave 1, P3) Add the missing columns, use the Strategic Priority names of the Statement of Intent, and define what "Active" means for an empty Record. Closes F-063; raises D-6.1.
5. (Wave 1, P3) State in the Governance Forums which Forums keep minutes and where, and state that the Stand-up and the Community of Practice keep none. Closes F-068; raises corpus criteria.
6. (Wave 2, P2) Extend the Artifact Standards folder structure and identifier table to every Template and Record, and define the Record status values. Closes F-054; raises D-3.5, D-6.1, D-7.2.
7. (Wave 2, P2) Enter the open Findings of this report in the Register, add a Finding column, and move the rule in 3.3 to section 4. Closes F-062; raises corpus criteria.
8. (Wave 4, P2) State in the Governance Forums, the Registers, the Document Catalog (Templates), and the Service Catalog the Maturity Level from which each construct is active, and mark the rest dormant. Start with the AI Steering Committee, Replenishment, and Delivery Review; the Decision, Risk and Issue, and AI Registry Registers; and ten Templates. Closes F-012; raises D-9.3.
9. (Wave 5, P2) Appoint the Executive Sponsor and the AICC Lead first, enter them with a date, then the other mandatory Roles, and record the Roles that the AICC Lead holds. Closes F-017; raises D-8.1, D-8.2.
10. (Wave 5, P2) Enter the values as decisions are taken, beginning with the Strategic Priorities and the first Milestones. Closes F-031; raises D-8.3, D-10.1.
11. (Wave 5, P2) Run each core procedure once with its Template (a Decision Record, an AI Steering Committee meeting, an Intake, a Risk Tier assessment) and correct the documents from the experience. Closes F-033; raises D-8.3.
12. (Wave 5, P2) Fix the calendar: set quarter 0 by the Decision Record of activation, enter dates for MS-001 to MS-010, and review them at the next Assessment. Closes F-070; raises D-3.5.

## 6. Result

Returned. The document is at Readiness Level R2 (drafted; gaps or inconsistencies remain). It is not accepted for activation (9.1): 9 finding(s) above Minor are open against it (F-012, F-017, F-031, F-033, F-043, F-044, F-054, F-062, F-070).
