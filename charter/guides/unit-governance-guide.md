# Guide: Unit governance

## 1. Purpose and when it applies

This guide explains how AICC is directed, reported, and controlled as an organizational unit: the mandate, the planning, the reporting, the decisions, the controls, and the assurance. It is the answer to the question "how does your unit operate?". It applies throughout.

## 2. The mandate and the authority

AICC acts under the mandate of the Executive Sponsor, and the Charter states its limits: it does not own the AI Platform, it does not own the results of a Domain, it does not set the rules of a Control Function, it does not validate its own work, and it does not decide a matter that the regulation of the Bank reserves to the Board, to the management, or to a Control Function. The appointment of the AICC Lead and the decision reference of the mandate are entered in the Appointments Record. The Executive Sponsor may delegate a decision in writing, for a scope and a period, and each delegation is entered there.

## 3. The yearly, quarterly, monthly, and weekly loops

| Loop | What is set or reviewed | By whom | Record |
| --- | --- | --- | --- |
| Yearly, at the first quarterly Steering | The Strategic Priorities, the Investment Envelopes and Guardrails, the documents, the AI Risk Appetite Statement, and the yearly Proposal of the strategy | Executive Sponsor; the AICC Lead owns the documents | Decision Records; Priorities |
| Quarterly | The results of the PI, the risk check with the Control Function Contacts, the Maturity Level, and the report to the Board Committee | Executive Sponsor | Quarterly Report; Registry Snapshot; Steering Summary |
| Monthly | Progress, risks, and blockers, and a sample of the Decisions of the AICC Lead | Executive Sponsor | Steering Summary |
| Weekly | The flow and the Dependencies | AICC Lead | The working state |
| On an event | An AI Incident, an Exception, a stop, a risk beyond appetite, a change of provider or regulation, or a change of Holder | As the Operating Model states | Decision Record; Risks and Issues; Appointments |

## 4. How a decision moves

The person who does the work decides on the facts. A decision goes to the AICC Lead, or to the Executive Sponsor, only when it affects another Domain or reaches outside the Bank, cannot be reversed without significant cost, exceeds a guardrail or changes a Strategic Priority, or accepts a risk or concerns a Risk Tier 3 Solution. A Control Function decides within its remit, and nobody overrides it. A decision at the level of the AICC Lead or above is entered in the Decision Log, and a Decision of the Executive Sponsor that is hard to reverse also has a Decision Record.

## 5. Reporting and assurance

Reporting runs from the Teams to the AICC Lead, to the Steering, and to the Board Committee. The Control Functions stand beside it, independent of AICC. Internal audit gives assurance only, and has read access to the Registry and, read only, to Jira, Confluence, and Service Management. The Executive Sponsor tells the Board Committee of an AI Incident that the incident management of the Bank classifies as major, as it requires, and of any risk accepted beyond the appetite, without waiting for the next report.

## 6. Where the evidence is

The working state is in the Registry until the cutover and then in Jira and Confluence. The evidence records are always in the Registry as closed and dated extracts. The Operating Model 8 lists each control with its evidence record, and the Registry README lists the Records by class. The AICC portal links to the evidence records on the corporate share. The Document Catalog states how a document is activated, changed, and checked.

## 7. The controls and how to test them

The Operating Model 8 lists each control with its rule, owner, timing, and evidence record. The table below gives, for each control, its objective, its type, and how an auditor tests it. Type is Directive (sets a rule or a direction), Preventive (stops an error before it happens), or Detective (finds an error after it happens). The test and the status of each control at a date are in the Control Matrix in the Registry.

| Ref | Control | Objective | Type | How to test |
| --- | --- | --- | --- | --- |
| C-01 | Mandate and appointment of the AICC Lead | AICC acts only under a documented authority | Directive | Compare the decision reference with the mandate and the appointment order |
| C-02 | Priorities, funding, and guardrails | Funding and commitments stay within a limit that the Executive Sponsor sets | Directive | Read the Priorities against the Guardrails and the Decision Records of the year |
| C-03 | Yearly review of the risk appetite and the policy | The use of AI stays within the appetite of the Bank | Directive | Read the Statement and the Decision Record of its review |
| C-04 | Review of the documents | The documents stay consistent and in force | Detective | Read the report of the check and the Decision Record that closes its findings |
| C-05 | Monthly review of progress, risks, and blockers, with a sample of the Decisions of the AICC Lead | A single person's decisions are reviewed by another | Detective | Read the Summary of each month and the sample it records |
| C-06 | Results, risk check, and Maturity Level | The Executive Sponsor sees results and risk each quarter | Detective | Read the Report and the Snapshot of the quarter |
| C-07 | Report to the Board Committee | The Board Committee is informed | Detective | Read the issuance block: approver, date, recipient |
| C-08 | Service Agreement for an Engagement | The commitment to a function is written before the work | Preventive | Compare the Agreement with the Initiative and its dates |
| C-09 | Approval of the business case | An Initiative is funded only on a complete case that the Control Functions have cleared | Preventive | Read the Completeness table, the clearances of the Control Function Contacts, and the Decision Record |
| C-10 | Outcome Report, acceptance, and confirmation of the benefit | The outcome is reported, accepted by its owner, and the benefit is confirmed by the function, not by AICC | Detective | Read the Report, the acceptance with who and when, and the confirmation with its source |
| C-11 | Capacity used and benefit confirmed | AICC does not overcommit and claims only confirmed benefit | Detective | Compare capacity used with the Agreements and the benefit with the Outcome Report |
| C-12 | Risk Tier assignment | Every Solution has a Tier that sets its checks | Preventive | Read the Tier, who assigned it, and when |
| C-13 | Check or validation before the first deployment | Nothing reaches real users or data unchecked | Preventive | Compare the date of the check with the first deployment |
| C-14 | Release | Use beyond the first users is decided by the right owner | Preventive | Compare the release with the check and the Tier |
| C-15 | Approval of the use of a Solution for a data class | Data is used only where its owner approved | Preventive | Read the approval, who gave it, and when |
| C-16 | AI Incident | Incidents are handled in the incident management of the Bank, with AICC taking part, and reviewed | Detective | Read the nil statement; for an Incident, the ticket in Service Management and the AI Incident Review; read the quarterly reconciliation with the incident management of the Bank |
| C-17 | Exception | A departure from a requirement is decided, limited, and recorded | Preventive | Read the nil statement; for an Exception, its expiry and its monthly review |
| C-18 | Check of a provider | A provider is checked for data, terms, and exit before use | Preventive | Compare the date of the check with the first use of the provider |
| C-19 | Sharing outside the Bank | Data and decisions stay within the Bank unless permitted | Preventive | Read the Data Sharing Arrangement and its Decision Record |
| C-20 | Proposal to adopt a Solution at scale | Adoption is decided by its owners | Directive | Read the Proposal and the decision |
| C-21 | Output published to the Board or investors | Published output is approved before it is issued | Preventive | Read the approval for each edition |
| C-22 | Separation of duties and independence | No person checks, accepts, or releases their own work | Preventive | At a release, compare the builder, the Checker, and the releaser; compare the Holders of the Roles with the rules of separation and the accepted limits |
| C-23 | Capacity ceiling and intake | AICC commits no more than it can deliver | Preventive | Compare the capacity of the Agreements with the capacity available |
| C-24 | Completeness of the Outcome Reports | Closed Engagements are reported | Detective | Read section 8 of the Summary |
| C-25 | Access of internal audit | Internal audit can see the records | Directive | Test read access to the Registry, and read-only access to Jira, Confluence, and Service Management |
| C-26 | Access review of the Registry and the tools | Access follows the Roles | Preventive | Read the result of the quarterly comparison with the Appointments Record |
| C-27 | Acceptance of a risk beyond the appetite | Only the Executive Sponsor accepts a risk beyond the appetite, and the Board Committee is told | Preventive | Read the Decision Record and the report to the Board Committee |
| C-28 | Reassessment of the Risk Tier and expiry of a validation | A Solution is not used on a validation that has expired or on a stale Risk Tier | Preventive | Compare the dates in the AI Registry with the dates of the reassessment and the validation |
| C-29 | Review of live Solutions | Live Solutions are monitored by their owners | Detective | Read the note of the review in the Solution Definition at each IT Review and Demo |
| C-30 | Change to a released Solution | A change is decided, tested, and released by the right owner | Preventive | Take a change: read the decision on a new check, the change ticket, the test result, and the release |
| C-31 | Retirement of a Solution | A retired Solution leaves no access, data, or registry entry behind | Preventive | Read the approval, and compare access, data, and the AI Registry entry with the retirement |
| C-32 | Deficiencies and findings | A failed control or a finding is followed up to closure | Detective | Take a finding: read its owner, its due date, and the monthly review |

## 8. What an auditor will ask, and the record that answers

| Question | Answer |
| --- | --- |
| What is the source of your authority? | The mandate and its decision reference in the Appointments Record |
| Who may decide what, and what are the limits? | Operating Model 4.2 and 5.3 and the Charter 3; the delegations in the Appointments Record |
| How are decisions recorded and reviewed? | The Decision Log and Decision Records; the monthly sample in the Steering Summary |
| How do you control risk? | The AI Policy, the Control Sign-Offs, and the Risks and Issues |
| How is independence kept? | The rules of separation, and the Appointments |
| What did you report, and to whom? | The Quarterly Report and its issuance block |

## 9. Rule source

Charter 3 to 7; Operating Model 4 to 8; AI Policy 5 to 7; Document Catalog 3, 4, 7; the Unit governance workflow.
