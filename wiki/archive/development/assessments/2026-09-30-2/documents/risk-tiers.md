# Document assessment report: Risk Tier Policy

## 1. Header

| Field | Entry |
| --- | --- |
| Document | Risk Tier Policy, revision 0.1, charter/policies/risk-tiers.md (AICC-POL-03-EN) |
| Assessment | 2026-09-30, second Assessment (folder 2026-09-30-2) |
| Assessor | Independent assessor, not the author; the Delivery Lead Role has no Holder |
| Author | AICC Lead (owner of every document, Document Catalog 1.2) |
| Readiness Level | R2 |
| Previous Readiness Level | R2 |
| Lines | 77 |

## 2. Scores

Scores follow Corpus Assessment 7.1 from the failed items; severities are those of 6.2.

| Criterion | Score (0 to 3) | Failed items | Evidence |
| --- | --- | --- | --- |
| D-1 Intent fit | 3 | none | none |
| D-2 Structure fit | 3 | none | none |
| D-3 Completeness | 2 | D-3.3 | D-3.3 (Major): The release of a Tier 4 Use Case by the AI Steering Committee has no Role, trigger, input, or Record (F-009); the reassessment each year or six months has no owner, trigger, or calendar (F-064). |
| D-4 Vocabulary and style | 2 | D-4.4 | D-4.4 (Major): "Shall" is not used in a policy that binds staff; 3.1 to 3.5 and 5.1 state requirements in the present tense. |
| D-5 Internal consistency | 3 | none | none |
| D-6 Cross-document consistency | 1 | D-6.1, D-6.4 | D-6.1 (Blocker): Tier 1 validation "By the owner" contradicts Roles 8.1 and Statement of Intent 7.3 (F-038); testing for bias and disclosure by Tier contradict Statement of Intent 6.2 and 6.3 (F-039); the Tier 4 release is not in Decision Management or the Decision Rights (F-009).; D-6.4 (Major): The policy contradicts the two higher documents on separation of duties and on bias testing (Vocabulary 2.2). |
| D-7 Traceability | 2 | D-7.4 | D-7.4 (Major): The AI Steering Committee decision for Tier 4 has no row in the Decision Rights. |
| D-8 Operability | 1 | D-8.1, D-8.2, D-8.3, D-8.4 | D-8.1 (Major): The Control Function Contact of model risk, who assigns every Risk Tier at Intake, has no Holder.; D-8.2 (Major): One Control Function Contact assigns each Tier at Intake; no capacity or deputy is recorded.; D-8.3 (Major): No Risk Tier assessment has been made; the Template has never been used.; D-8.4 (Minor): Reassessment each six months for Tier 4 and each year for Tier 3 has no calendar. |
| D-9 Proportionality | 3 | D-9.4 | D-9.4 (Minor): A requirements matrix of 11 rows by four Tiers for an AICC with no Use Case. |
| D-10 Currency and governance | 3 | none | none |

## 3. Strengths

- Four Tiers with stated attributes, a highest-attribute rule, and a rule that a higher Tier includes the requirements of the lower.
- Who assigns, who may raise, and who may lower a Tier is stated (3.1 to 3.3).
- Reassessment and return to Discovery on a change (5).

## 4. Findings

| Finding | Category | Severity | Evidence | Recommendation | Owner | Wave |
| --- | --- | --- | --- | --- | --- | --- |
| F-009 (continues) | misalignment | Blocker | Risk Tier Policy 4.1 requires "the decision of the AI Steering Committee" before a Risk Tier 4 Use Case is released. No Decision Category lists it (Decision Management 2.1, Portfolio), no row of the Decision Rights carries it, the AI Steering Committee agenda Template has no item for it, and the Scale exit in Portfolio Management 4.1 names the Domain Owner alone. The Document Catalog lists the gap as a next action in three documents (Decision Rights, Decision Management, Risk Tier Policy). | Add the decision to the Portfolio Decision Category, add a row to the Decision Rights (accountable: AI Steering Committee), add an item to the AI Steering Committee agenda Template, and state it in the Scale exit of Portfolio Management. | AICC Lead | 2 |
| F-038 (new) | misalignment | Blocker | Risk Tier Policy 4.1 (Validation, Tier 1) reads "By the owner". Roles 8.1 states that no person validates a Use Case that the person owns, and Statement of Intent 7.3 states that no person validates their own work. The lower document contradicts the two higher documents on separation of duties. | Change the Tier 1 validation to a check by a person other than the owner, or state that Tier 1 has no validation and is covered by the AI Use Policy; state the exception in the Roles if it is intended. | AICC Lead | 2 |
| F-017 (continues) | gap | Major | The Register of Appointments holds no Holder for any Role, including the Executive Sponsor and the AICC Lead. No Forum has a named chair or secretary. MS-002 is not evidenced. | Appoint the Executive Sponsor and the AICC Lead first, enter them with a date, then the other mandatory Roles, and record the Roles that the AICC Lead holds. | AICC Lead | 5 |
| F-033 (continues) | gap | Major | No procedure has been run. There is no Decision Record, no minutes, no backlog entry, and no register entry. Of 23 Templates only the two assessment Templates have been used, and the first Assessment report did not follow the Corpus Assessment Report Template (its findings table has no Owner and Date columns and its sections are renamed). | Run each core procedure once with its Template (a Decision Record, an AI Steering Committee meeting, an Intake, a Risk Tier assessment) and correct the documents from the experience. | AICC Lead | 5 |
| F-039 (new) | misalignment | Major | Statement of Intent 6.2 requires every AI to be tested for bias before release and 6.3 requires individuals to be told that they interact with AI. Risk Tier Policy 4.1 marks testing for bias "Not required" for Tier 1 and "Required for material use" for Tier 2, and disclosure "Not applicable" for Tiers 1 and 2. The Statement prevails (Vocabulary 2.2). | Either qualify 6.2 and 6.3 of the Statement by Risk Tier or raise the Tier 1 and 2 requirements in the Policy. | AICC Lead | 2 |
| F-045 (new) | non-conformance | Major | Vocabulary 3.3 states that an obligation is stated with "shall". "Shall" occurs only in the Statement of Intent (17 lines), in the Roles (7 lines, mostly the separation rules), and elsewhere only in quotation. The other written documents, including both policies that bind staff, state obligations in the present tense ("Every employee ... reports it", "A member declares a conflict of interest", "The secretary issues the agenda two working days before"). | Rewrite the requirement clauses with "shall" (or relax Vocabulary 3.3 to say that present tense states an allocation), and add a search for obligations without "shall" to the mechanical checks. | AICC Lead | 4 |
| F-064 (new) | gap | Major | Several requirements of the Risk Tiers are checked at no Stage and in no Forum: disclosure to customers, contestability, logging, the design of human oversight, bias testing for Tier 2, and the reassessment each year or six months (Risk Tier Policy 4.1, 5.1). The Stage exits in Portfolio Management 4.1 check the Use Case card, Risk Tier assessment, Impact Assessment, validation sign-off, and monitoring. The recording in the AI Registry is an exit condition only at Retire. The design approval of the Design Review is an exit condition of no Stage. No Record or calendar triggers a reassessment. | Add to the Stage exit policies the checks of Tier 3 and 4 requirements (or refer to a checklist in the validation sign-off), make the AI Registry entry an exit condition of Intake, and add a reassessment date to the AI Registry. | AICC Lead | 2 |
| F-019 (continues) | gap | Minor | Periods, hours, and intervals (two, five, and ten working days; one hour; every two weeks; each six months; each quarter) are stated in six documents and are unconfirmed. The open items page lists them as undecided (items 8, 25, 26, 27). | Gather the parameters in one table in the Governance Forums or the Decision Management and have the Control Functions and the AI Steering Committee confirm them. | AICC Lead | 3 |
| F-052 (new) | misalignment | Minor | Smaller differences between documents. Governance Forums 5.4.3 requires a Decision Record for every design approval; Decision Management 2.1 and 3.1 require one only where more than one Domain is affected. Portfolio Management 3.3 has the Portfolio Manager keep the Delivery Backlog; Decision Rights 4.3 makes the Portfolio Manager only consulted. Decision Management 10.1 gives the identifier as "DR-year-number" and Artifact Standards as "DR-yyyy-nnn". portfolio/README.md makes the Portfolio Manager the owner of the Decision Records; Decision Management 4.6 has the secretary or Proposer write them. Decision Rights 2.3 lets each Control Function decide for itself; Risk Tier Policy 3.3 lets only model risk lower a Risk Tier. | Align the pairs in one change, with the Decision Rights as the source. | AICC Lead | 1 |
| F-073 (new) | overcomplexity | Minor | The detail exceeds the risk that it controls while the portfolio holds no item: five blocks by Entity, Domain, and regime in the Register of Appointments; a 16-field Decision Record and four-step escalation; 13 identifier families and fifteen folders; a requirements matrix of 11 rows by four Risk Tiers; an excluded-terms column for 75 terms; 81 checklist items; about 3,600 lines of wiki research for 25 documents. | Keep the core (one Decision Record form of nine fields, three identifier families, two Risk Tier checks) and mark the rest dormant until a first Use Case passes the Stage concerned. | AICC Lead | 4 |

## 5. Recommendations

1. (Wave 1, P3) Align the pairs in one change, with the Decision Rights as the source. Closes F-052; raises D-6.1.
2. (Wave 2, P1) Add the decision to the Portfolio Decision Category, add a row to the Decision Rights (accountable: AI Steering Committee), add an item to the AI Steering Committee agenda Template, and state it in the Scale exit of Portfolio Management. Closes F-009; raises D-3.3, D-6.1, D-7.4.
3. (Wave 2, P1) Change the Tier 1 validation to a check by a person other than the owner, or state that Tier 1 has no validation and is covered by the AI Use Policy; state the exception in the Roles if it is intended. Closes F-038; raises D-6.1, D-6.4.
4. (Wave 2, P2) Either qualify 6.2 and 6.3 of the Statement by Risk Tier or raise the Tier 1 and 2 requirements in the Policy. Closes F-039; raises D-6.1, D-6.4.
5. (Wave 2, P2) Add to the Stage exit policies the checks of Tier 3 and 4 requirements (or refer to a checklist in the validation sign-off), make the AI Registry entry an exit condition of Intake, and add a reassessment date to the AI Registry. Closes F-064; raises D-3.3.
6. (Wave 3, P3) Gather the parameters in one table in the Governance Forums or the Decision Management and have the Control Functions and the AI Steering Committee confirm them. Closes F-019; raises D-8.4.
7. (Wave 4, P2) Rewrite the requirement clauses with "shall" (or relax Vocabulary 3.3 to say that present tense states an allocation), and add a search for obligations without "shall" to the mechanical checks. Closes F-045; raises D-4.4.
8. (Wave 4, P3) Keep the core (one Decision Record form of nine fields, three identifier families, two Risk Tier checks) and mark the rest dormant until a first Use Case passes the Stage concerned. Closes F-073; raises D-9.4.
9. (Wave 5, P2) Appoint the Executive Sponsor and the AICC Lead first, enter them with a date, then the other mandatory Roles, and record the Roles that the AICC Lead holds. Closes F-017; raises D-8.1, D-8.2.
10. (Wave 5, P2) Run each core procedure once with its Template (a Decision Record, an AI Steering Committee meeting, an Intake, a Risk Tier assessment) and correct the documents from the experience. Closes F-033; raises D-8.3.

## 6. Result

Returned. The document is at Readiness Level R2 (drafted; gaps or inconsistencies remain). It is not accepted for activation (9.1): 7 finding(s) above Minor are open against it (F-009, F-038, F-017, F-033, F-039, F-045, F-064).
