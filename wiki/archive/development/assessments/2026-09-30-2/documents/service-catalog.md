# Document assessment report: Service Catalog

## 1. Header

| Field | Entry |
| --- | --- |
| Document | Service Catalog, revision 0.1, charter/service-catalog.md (AICC-OPS-02-EN) |
| Assessment | 2026-09-30, second Assessment (folder 2026-09-30-2) |
| Assessor | Independent assessor, not the author; the Delivery Lead Role has no Holder |
| Author | AICC Lead (owner of every document, Document Catalog 1.2) |
| Readiness Level | R2 |
| Previous Readiness Level | R2 |
| Lines | 75 |

## 2. Scores

Scores follow Corpus Assessment 7.1 from the failed items; severities are those of 6.2.

| Criterion | Score (0 to 3) | Failed items | Evidence |
| --- | --- | --- | --- |
| D-1 Intent fit | 3 | none | none |
| D-2 Structure fit | 3 | none | none |
| D-3 Completeness | 2 | D-3.3 | D-3.3 (Major): No request channel, and no response times: the Request column gives a trigger ("On request of a Domain Owner") and 3.2 refers the times to a Record whose column is empty (F-023). |
| D-4 Vocabulary and style | 2 | D-4.4 | D-4.4 (Major): "Shall" is not used; 3.2 and 4.1 state requirements in the present tense. |
| D-5 Internal consistency | 3 | none | none |
| D-6 Cross-document consistency | 3 | D-6.3 | D-6.3 (Minor): 2.1 restates the three parts of the Service Portfolio that Vocabulary 4.7 defines. |
| D-7 Traceability | 3 | none | none |
| D-8 Operability | 1 | D-8.1, D-8.2, D-8.3, D-8.4 | D-8.1 (Major): The owners of the nine services (AICC Lead, Portfolio Manager, Lead Architect, Enablement Coach, Delivery Lead) have no Holder.; D-8.2 (Major): Nine services for a Hub with no recorded staff; "Available" status in the Record with no capacity (F-023).; D-8.3 (Major): The Service Portfolio Record has never been used; no Solution has entered it.; D-8.4 (Minor): The response time of each service is unset. |
| D-9 Proportionality | 2 | D-9.1, D-9.3 | D-9.1 (Major): A three-part Service Portfolio, nine services, and a Solutions catalog exist before the first Solution; removal of Pipeline and Retired parts would not stop any Stage.; D-9.3 (Minor): All nine services are "Available" in the Record from the first day. |
| D-10 Currency and governance | 3 | none | none |

## 3. Strengths

- Three-part Service Portfolio that follows the life of a service, tied to the Stages (4.3).
- Each AICC Service has a provider Role that agrees with the Roles and the Decision Rights.
- Short document (75 lines), one purpose.

## 4. Findings

| Finding | Category | Severity | Evidence | Recommendation | Owner | Wave |
| --- | --- | --- | --- | --- | --- | --- |
| F-012 (continues) | overengineering | Major | Eight Forums, seven Registers, 23 Templates, and nine AICC Services are active on paper. No document states the Maturity Level from which each is active, so the Level 1 limits (five Forums, four Registers, ten Templates) cannot be met or tested. No Role has a Holder. The Evolution Plan, which is to hold the activation schedule, is a stub. Milestone MS-005 of the Portfolio Roadmap implies three Forums at Level 1 and no other document confirms it. | State in the Governance Forums, the Registers, the Document Catalog (Templates), and the Service Catalog the Maturity Level from which each construct is active, and mark the rest dormant. Start with the AI Steering Committee, Replenishment, and Delivery Review; the Decision, Risk and Issue, and AI Registry Registers; and ten Templates. | AICC Lead | 4 |
| F-017 (continues) | gap | Major | The Register of Appointments holds no Holder for any Role, including the Executive Sponsor and the AICC Lead. No Forum has a named chair or secretary. MS-002 is not evidenced. | Appoint the Executive Sponsor and the AICC Lead first, enter them with a date, then the other mandatory Roles, and record the Roles that the AICC Lead holds. | AICC Lead | 5 |
| F-023 (continues) | gap | Major | Nine AICC Services are listed. Request and Response time are empty in the Record (portfolio/service-portfolio.md), no request channel is stated, and no capacity exists. The Catalog lists "Add a request channel and response times" as a next action. The AICC Hub is not staffed. | State how a service is requested and answered, and keep in the Service Catalog only the services that can be delivered now. | AICC Lead | 3 |
| F-033 (continues) | gap | Major | No procedure has been run. There is no Decision Record, no minutes, no backlog entry, and no register entry. Of 23 Templates only the two assessment Templates have been used, and the first Assessment report did not follow the Corpus Assessment Report Template (its findings table has no Owner and Date columns and its sections are renamed). | Run each core procedure once with its Template (a Decision Record, an AI Steering Committee meeting, an Intake, a Risk Tier assessment) and correct the documents from the experience. | AICC Lead | 5 |
| F-045 (new) | non-conformance | Major | Vocabulary 3.3 states that an obligation is stated with "shall". "Shall" occurs only in the Statement of Intent (17 lines), in the Roles (7 lines, mostly the separation rules), and elsewhere only in quotation. The other written documents, including both policies that bind staff, state obligations in the present tense ("Every employee ... reports it", "A member declares a conflict of interest", "The secretary issues the agenda two working days before"). | Rewrite the requirement clauses with "shall" (or relax Vocabulary 3.3 to say that present tense states an allocation), and add a search for obligations without "shall" to the mechanical checks. | AICC Lead | 4 |
| F-056 (new) | ghost | Major | Design Review approves designs "against the architecture standards of AICC" (Governance Forums 5.4.1; Roles 3.2; Decision Rights 4.2 and 4.4; Service Catalog "Architecture guidance"; Operating Model 9.4 "technical guardrails, standards"). No document, Record, or folder holds the standards or the requirements that the use of AI places on the AI Platform (Operating Model 11.3). The Design Review has no criteria, and nothing states where the standards are kept. | Create a Record for the architecture standards and the platform requirements (a short Standards page in the portfolio folder), owned by the Lead Architect, and name it in the Governance Forums and the Artifact Standards. | AICC Lead | 2 |
| F-005 (continues) | duplication | Minor | Restated content is now measured. Clauses that share six or more eight-word sequences with a clause of another document (Vocabulary excluded): 30 of 487 prose clauses (6.2 percent), above the 5 percent limit; 40 (8.2 percent) at four sequences. Main cases: Control Function Contact duties (Operating Model 11.2 and Roles 5.1, 24 sequences); AI Steering Committee purpose and members (Operating Model 5.2, Roles 2.2, Governance Forums 4.1 and 4.3, Statement of Intent 7.5); AICC Lead (Operating Model 9.1 and Roles 3.1); Domain Owner (Operating Model 10.2, Roles 4.1, Vocabulary); "Domain" (Operating Model 7.4, Statement of Intent 1.1, Vocabulary); the AI Incident definition (AI Incident Policy 2.1 and Vocabulary); Role, Position, and Holder (Roles 1.2, Register of Appointments 2.1, Vocabulary); Register (Registers 1.2, Vocabulary). Also restated: the activation rule (Document Catalog 6, Roles 2.1, Decision Rights 4.6, Decision Management 2.1, Corpus Assessment 3.3); the three parts of the Service Portfolio (Service Catalog 2.1 and Vocabulary 4.7); the list of Records (Artifact Standards 2.2, Portfolio Management 7.1, portfolio/README.md). | Keep each definition in the Vocabulary, each role description in the Roles and Responsibilities, and each Forum membership in the Governance Forums; replace the other copies by a reference. The Statement of Intent may keep its five definitions because it is read alone. | AICC Lead | 2 |
| F-019 (continues) | gap | Minor | Periods, hours, and intervals (two, five, and ten working days; one hour; every two weeks; each six months; each quarter) are stated in six documents and are unconfirmed. The open items page lists them as undecided (items 8, 25, 26, 27). | Gather the parameters in one table in the Governance Forums or the Decision Management and have the Control Functions and the AI Steering Committee confirm them. | AICC Lead | 3 |

## 5. Recommendations

1. (Wave 2, P2) Create a Record for the architecture standards and the platform requirements (a short Standards page in the portfolio folder), owned by the Lead Architect, and name it in the Governance Forums and the Artifact Standards. Closes F-056; raises corpus criteria.
2. (Wave 2, P3) Keep each definition in the Vocabulary, each role description in the Roles and Responsibilities, and each Forum membership in the Governance Forums; replace the other copies by a reference. The Statement of Intent may keep its five definitions because it is read alone. Closes F-005; raises D-6.3.
3. (Wave 3, P2) State how a service is requested and answered, and keep in the Service Catalog only the services that can be delivered now. Closes F-023; raises D-3.3, D-8.4, D-9.1, D-9.3.
4. (Wave 3, P3) Gather the parameters in one table in the Governance Forums or the Decision Management and have the Control Functions and the AI Steering Committee confirm them. Closes F-019; raises D-8.4.
5. (Wave 4, P2) State in the Governance Forums, the Registers, the Document Catalog (Templates), and the Service Catalog the Maturity Level from which each construct is active, and mark the rest dormant. Start with the AI Steering Committee, Replenishment, and Delivery Review; the Decision, Risk and Issue, and AI Registry Registers; and ten Templates. Closes F-012; raises D-9.1, D-9.3.
6. (Wave 4, P2) Rewrite the requirement clauses with "shall" (or relax Vocabulary 3.3 to say that present tense states an allocation), and add a search for obligations without "shall" to the mechanical checks. Closes F-045; raises D-4.4.
7. (Wave 5, P2) Appoint the Executive Sponsor and the AICC Lead first, enter them with a date, then the other mandatory Roles, and record the Roles that the AICC Lead holds. Closes F-017; raises D-8.1, D-8.2.
8. (Wave 5, P2) Run each core procedure once with its Template (a Decision Record, an AI Steering Committee meeting, an Intake, a Risk Tier assessment) and correct the documents from the experience. Closes F-033; raises D-8.3.

## 6. Result

Returned. The document is at Readiness Level R2 (drafted; gaps or inconsistencies remain). It is not accepted for activation (9.1): 6 finding(s) above Minor are open against it (F-012, F-017, F-023, F-033, F-045, F-056).
