# Document assessment report: AI Incident Policy

## 1. Header

| Field | Entry |
| --- | --- |
| Document | AI Incident Policy, revision 0.1, charter/policies/ai-incidents.md (AICC-POL-05-EN) |
| Assessment | 2026-09-30, second Assessment (folder 2026-09-30-2) |
| Assessor | Independent assessor, not the author; the Delivery Lead Role has no Holder |
| Author | AICC Lead (owner of every document, Document Catalog 1.2) |
| Readiness Level | R2 |
| Previous Readiness Level | R2 |
| Lines | 91 |

## 2. Scores

Scores follow Corpus Assessment 7.1 from the failed items; severities are those of 6.2.

| Criterion | Score (0 to 3) | Failed items | Evidence |
| --- | --- | --- | --- |
| D-1 Intent fit | 3 | none | none |
| D-2 Structure fit | 3 | none | none |
| D-3 Completeness | 2 | D-3.3, D-3.5 | D-3.3 (Major): No reporting channel is named for the report within one hour of a Severity 1 AI Incident (5.1(a)); no link to the incident process of the Bank (F-035).; D-3.5 (Major): The notification periods of the regulators of each Entity are "as the law requires"; no place is stated where they are listed (F-035). |
| D-4 Vocabulary and style | 2 | D-4.2, D-4.3, D-4.4 | D-4.2 (Minor): "AI Incident report" (6.1) for the Template "AI Incident Report".; D-4.3 (Major): "Severity" is capitalized and not defined; the scale (Critical, Major, Minor) duplicates the names of the Finding severities of the Corpus Assessment (F-071).; D-4.4 (Major): "Shall" is not used in a policy that binds staff; 4.1 ("Every employee ... reports it") and 5.1 state obligations in the present tense. |
| D-5 Internal consistency | 3 | none | none |
| D-6 Cross-document consistency | 3 | D-6.3 | D-6.3 (Minor): 2.1 restates the definition of an AI Incident in Vocabulary 4.5. |
| D-7 Traceability | 3 | none | none |
| D-8 Operability | 1 | D-8.1, D-8.2, D-8.3, D-8.4 | D-8.1 (Major): The AI Solution Engineer, Domain Owner, Platform Owner, AICC Lead, and the Control Function Contacts of compliance and data protection have no Holder.; D-8.2 (Major): A one-hour report for Severity 1 needs a staffed channel that does not exist.; D-8.3 (Major): No AI Incident Report or Register entry has been made.; D-8.4 (Minor): One hour for a report and ten working days for a review are unconfirmed (open item 27). |
| D-9 Proportionality | 3 | none | none |
| D-10 Currency and governance | 3 | none | none |

## 3. Strengths

- Definition, severity scale, responsibilities, steps (report, contain, assess, notify, remedy, review), and Records in one short policy.
- Notification decisions are given to the Control Function Contacts of compliance and data protection (4.3), which agrees with the Decision Rights.
- A near miss is an AI Incident (2.1(g)), which favors reporting.

## 4. Findings

| Finding | Category | Severity | Evidence | Recommendation | Owner | Wave |
| --- | --- | --- | --- | --- | --- | --- |
| F-016 (continues) | non-conformance | Major | Capitalized terms used and not defined: Chair (Governance Forums 4.2, 4.4, 5.x; Templates), Quarterly Report (Reporting, Forums, Decision Rights, Templates), Board Committee report, Domain scorecard, Control summary, Severity (AI Incident Policy 3.1), and the lower-case concept "written procedure" (Governance Forums 4.6, Decision Management). The four Registers other than the Decision Register are named and not defined in the Vocabulary. "Change history" is removed. The Catalog lists "Define Chair and written procedure" as a next action. | Define Chair, Quarterly Report, Written procedure, and Severity in the Vocabulary, or replace them by defined terms; add the Register names. | AICC Lead | 1 |
| F-017 (continues) | gap | Major | The Register of Appointments holds no Holder for any Role, including the Executive Sponsor and the AICC Lead. No Forum has a named chair or secretary. MS-002 is not evidenced. | Appoint the Executive Sponsor and the AICC Lead first, enter them with a date, then the other mandatory Roles, and record the Roles that the AICC Lead holds. | AICC Lead | 5 |
| F-033 (continues) | gap | Major | No procedure has been run. There is no Decision Record, no minutes, no backlog entry, and no register entry. Of 23 Templates only the two assessment Templates have been used, and the first Assessment report did not follow the Corpus Assessment Report Template (its findings table has no Owner and Date columns and its sections are renamed). | Run each core procedure once with its Template (a Decision Record, an AI Steering Committee meeting, an Intake, a Risk Tier assessment) and correct the documents from the experience. | AICC Lead | 5 |
| F-035 (changed) | gap | Major | AI Incident Policy 3.1 now describes each severity. The criteria still use judgment words ("serious", "limited or reversible", "material"), no reporting channel is named for the report within one hour (5.1(a)), no link is made to the incident process of the Bank, and the notification periods of the regulators of each Entity are not listed ("as the law requires"). | Name the channel and a staffed contact, refer to the incident process of the Bank, and list the notification periods for each Entity. | AICC Lead | 3 |
| F-045 (new) | non-conformance | Major | Vocabulary 3.3 states that an obligation is stated with "shall". "Shall" occurs only in the Statement of Intent (17 lines), in the Roles (7 lines, mostly the separation rules), and elsewhere only in quotation. The other written documents, including both policies that bind staff, state obligations in the present tense ("Every employee ... reports it", "A member declares a conflict of interest", "The secretary issues the agenda two working days before"). | Rewrite the requirement clauses with "shall" (or relax Vocabulary 3.3 to say that present tense states an allocation), and add a search for obligations without "shall" to the mechanical checks. | AICC Lead | 4 |
| F-054 (new) | gap | Major | Artifact Standards gives no location or identifier for the Domain Engagement Record, the AI Incident Report, and the Exception Request (the Use Case folder README lists the Records of a Use Case, but Figure 7 of the Artifact Standards does not). The seeded Records use identifiers that Artifact Standards 3.1 does not define: PRI, RMP, PBL, SPF, REG-DEC, REG-AI, REG-RSK, REG-INC, REG-EXC, REG-BEN, PRG-main, DBL-main, PRM-main, ROS-main. No status values are defined for a Record header (4.1) and all Records hold "Active". | Extend the Artifact Standards folder structure and identifier table to every Template and Record, and define the Record status values. | AICC Lead | 2 |
| F-003 (continues) | non-conformance | Minor | Defined terms and titles are still in lower case: "delivery backlog" (Operating Model 12.1), "AI incident policy" (8.1), "stand-up" (14.6), "Portfolio backlog" and "Delivery backlog" (7.1 table), "objectives" (12.2); "Group arrangement", "Board committee", "entity", "AI use policy", "data classification rules" (Statement of Intent 5.6, 7.2, 12.2, 11.3); "secretary" and "decider" in lower case (Governance Forums, Decision Management, Registers); "metadata block" (Document Catalog 5.3, 8.1); "role" in the definition of the AICC Lead (Vocabulary 4.2). Template names in lower case: "Use Case card", "Risk Tier assessment", "Domain engagement record" (Portfolio Management 4.1, 5.3); "AI Incident report" (AI Incident Policy 6.1). | Use the defined term or the document title with capitals, and run the lower-case check again after the change. | AICC Lead | 1 |
| F-005 (continues) | duplication | Minor | Restated content is now measured. Clauses that share six or more eight-word sequences with a clause of another document (Vocabulary excluded): 30 of 487 prose clauses (6.2 percent), above the 5 percent limit; 40 (8.2 percent) at four sequences. Main cases: Control Function Contact duties (Operating Model 11.2 and Roles 5.1, 24 sequences); AI Steering Committee purpose and members (Operating Model 5.2, Roles 2.2, Governance Forums 4.1 and 4.3, Statement of Intent 7.5); AICC Lead (Operating Model 9.1 and Roles 3.1); Domain Owner (Operating Model 10.2, Roles 4.1, Vocabulary); "Domain" (Operating Model 7.4, Statement of Intent 1.1, Vocabulary); the AI Incident definition (AI Incident Policy 2.1 and Vocabulary); Role, Position, and Holder (Roles 1.2, Register of Appointments 2.1, Vocabulary); Register (Registers 1.2, Vocabulary). Also restated: the activation rule (Document Catalog 6, Roles 2.1, Decision Rights 4.6, Decision Management 2.1, Corpus Assessment 3.3); the three parts of the Service Portfolio (Service Catalog 2.1 and Vocabulary 4.7); the list of Records (Artifact Standards 2.2, Portfolio Management 7.1, portfolio/README.md). | Keep each definition in the Vocabulary, each role description in the Roles and Responsibilities, and each Forum membership in the Governance Forums; replace the other copies by a reference. The Statement of Intent may keep its five definitions because it is read alone. | AICC Lead | 2 |
| F-019 (continues) | gap | Minor | Periods, hours, and intervals (two, five, and ten working days; one hour; every two weeks; each six months; each quarter) are stated in six documents and are unconfirmed. The open items page lists them as undecided (items 8, 25, 26, 27). | Gather the parameters in one table in the Governance Forums or the Decision Management and have the Control Functions and the AI Steering Committee confirm them. | AICC Lead | 3 |
| F-071 (new) | incoherence | Minor | Two severity scales use the same names: AI Incident Policy 3.1 (1 Critical, 2 Major, 3 Minor) and Corpus Assessment 10.3 (Blocker, Major, Minor). "Severity" is not defined in the Vocabulary. | Rename one scale (for example High, Medium, Low for incidents) and define Severity for each. | AICC Lead | 1 |

## 5. Recommendations

1. (Wave 1, P2) Define Chair, Quarterly Report, Written procedure, and Severity in the Vocabulary, or replace them by defined terms; add the Register names. Closes F-016; raises D-4.3.
2. (Wave 1, P3) Use the defined term or the document title with capitals, and run the lower-case check again after the change. Closes F-003; raises D-4.2.
3. (Wave 1, P3) Rename one scale (for example High, Medium, Low for incidents) and define Severity for each. Closes F-071; raises D-4.3.
4. (Wave 2, P2) Extend the Artifact Standards folder structure and identifier table to every Template and Record, and define the Record status values. Closes F-054; raises D-3.3, D-3.5.
5. (Wave 2, P3) Keep each definition in the Vocabulary, each role description in the Roles and Responsibilities, and each Forum membership in the Governance Forums; replace the other copies by a reference. The Statement of Intent may keep its five definitions because it is read alone. Closes F-005; raises D-6.3.
6. (Wave 3, P2) Name the channel and a staffed contact, refer to the incident process of the Bank, and list the notification periods for each Entity. Closes F-035; raises D-3.3, D-3.5.
7. (Wave 3, P3) Gather the parameters in one table in the Governance Forums or the Decision Management and have the Control Functions and the AI Steering Committee confirm them. Closes F-019; raises D-8.4.
8. (Wave 4, P2) Rewrite the requirement clauses with "shall" (or relax Vocabulary 3.3 to say that present tense states an allocation), and add a search for obligations without "shall" to the mechanical checks. Closes F-045; raises D-4.4.
9. (Wave 5, P2) Appoint the Executive Sponsor and the AICC Lead first, enter them with a date, then the other mandatory Roles, and record the Roles that the AICC Lead holds. Closes F-017; raises D-8.1, D-8.2.
10. (Wave 5, P2) Run each core procedure once with its Template (a Decision Record, an AI Steering Committee meeting, an Intake, a Risk Tier assessment) and correct the documents from the experience. Closes F-033; raises D-8.3.

## 6. Result

Returned. The document is at Readiness Level R2 (drafted; gaps or inconsistencies remain). It is not accepted for activation (9.1): 6 finding(s) above Minor are open against it (F-016, F-017, F-033, F-035, F-045, F-054).
