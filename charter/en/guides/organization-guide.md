# Guide: Organization

## 1. Purpose and when it applies

This guide explains how the unit is organized: its place in the Bank, its Roles and their profiles, who is responsible for what, its governing bodies, how people are appointed and changed, how the organization grows, and how the records and the evidence are kept. It is the reference for HR and internal audit. The charter names Roles only. The mapping of Roles to people is the Appointments Record in the Registry, with the log of appointments.

## 2. The place of AICC in the Bank

AICC is an internal consulting and innovation lab. It reports to the Executive Sponsor. The Executive Sponsor may bring its reports and Proposals to the Board Committee or the Board, and always tells the Board Committee of a major AI Incident and of a risk accepted beyond the appetite. It is not a Control Function, and the Control Functions are independent of it. The Control Functions keep their own accountability for their remit. In the three lines of the Bank, AICC and the Domains own the risks of their work, the Control Functions set the rules of their remit, clear, validate, decide Exceptions, and may stop, and internal audit gives independent assurance (Operating Model 2.4). AICC has no administrative line over the people assigned to it, who stay in their own reporting line, or over the partners from the functions.

## 3. The Roles and their profiles

| Role | Purpose | Main responsibilities | Authority | Reports in | Typical competence |
| --- | --- | --- | --- | --- | --- |
| Executive Sponsor | Holds the mandate and the funding | Appoints the AICC Lead and names the members of the AI Steering Committee; sets the Strategic Priorities, the Envelopes, the Guardrails, and the mix of Initiatives; decides the AI Risk Appetite Statement; approves published output; approves the Quarterly Report and decides whether to submit it to the Board Committee or the Board | Strategic Priorities, funding, the mix of Initiatives, the business case above a guardrail or across Domains and the decision after its MVP (continue, pivot, defer, or reject an Initiative), release of a Risk Tier 3 Solution, risks beyond appetite, retirement of a Service across Domains | The line of the Bank | Executive management |
| AICC Lead | Leads AICC as lead engineer and architect | Owns every document and Record; takes items in; acts as the product owner of the Team while it has up to three people and accepts its Features and Capabilities; gives the final acceptance of the Team before a Solution is deployed to its first users; issues Service Agreements and Outcome Reports; assigns and reassesses the Risk Tier; sets the training; leads the AI Incident review; prepares the Quarterly Report, with the concentration on one provider | Taking an item into discovery, deferring or rejecting it at triage, pulling an Initiative and the limit on the Active Initiatives, the rank of the backlogs, the acceptance of Features and Capabilities as product owner, the final acceptance of the Team, standards, Templates, questions between Domains | The Executive Sponsor | Engineering and architecture, delivery, and governance |
| Solution Engineer | Owns a Solution end to end with the Domains | Designs the architecture, builds, deploys, and runs a Solution, checks the work of others, coaches Domain Experts, and keeps work visible | How a Solution is designed and built; the approval of Features at Iteration Planning; the order in which the team pulls work within the agreed ranking | The AICC Lead for AICC; otherwise the own line | Engineering |
| Domain Owner | Owns the results of AI adoption in a Domain | Names the Domain Expert; approves the business case within a Domain and below a guardrail, and the Solution Definition; approves the data classes; releases; judges the working Solution and accepts it as the requester; confirms the benefit; owns oversight in operation, disclosure, and contestability, and reviews monitoring and provider notices at each Iteration Review and Demo | The business case and the decision after the MVP within one Domain and below a guardrail, a Solution Definition, the acceptance of a Solution, retirement of a Solution | The line of the Domain | Business ownership |
| Domain Expert | Early adopter and partner in a Domain | Explains the routine work, tries the Solution, scales adoption | Nothing on funding, acceptance, or control | The line of the Domain | The routine work of the Domain |
| Control Function Contact | Advises, validates, and may stop | Confirms, within the remit, the laws and regulations that apply to the use of AI in the Bank; raises the Risk Tier within the remit; clears a business case that expects Risk Tier 2 or 3; validates; decides Exceptions | The clearance of a business case, validation, raising the Risk Tier, a suspension, a stop, and an Exception to a control requirement, each within the remit of the Control Function | The Control Function | The remit of the function |
| Platform Owner | Provides and operates the AI Platform | Meets the requirements in the Standards; keeps the evidence | The design of the AI Platform within those requirements | The technology line | Platform engineering |

One person may hold several Roles, within the rules of separation of the Operating Model 4.4. A Hat, such as keeper of a backlog or facilitator of the events, is a duty that the team takes for a time and is not a Role.

## 4. Who is responsible for what

The matrix states, for each activity, the part that each Role takes. R, responsible, does the work. A, accountable, is the one Role that answers for the activity and decides it; each activity has one A, and where a row shows no R the A also does the work. C, consulted, is asked before. I, informed, is told after. SP is the Executive Sponsor, SC the AI Steering Committee, AL the AICC Lead, SE the Solution Engineer, DO the Domain Owner, DE the Domain Expert, CFC the Control Function Contact, and PO the Platform Owner. The Board Committee is informed of what the Charter states, and internal audit gives assurance and is outside the table. The Checker of a Risk Tier 1 Solution is a person whom the AICC Lead names in the Appointments Record, who did not build the Solution. The Checker is a designation, not a Role, and is outside the table. The product owner of a Team is also a designation, not a Role: it is the AICC Lead while the Team has up to three people, which the row of the acceptance of a Feature or a Capability shows, and otherwise a person whom the AICC Lead names in the Appointments Record. Where the Team is small and one person holds several Roles, the matrix is read by Role, within the rules of separation and the accepted limits of section 6.

The activities are grouped by family, from the direction of the unit, through the life of an Initiative and a Solution, to the report.

| Activity | SP | SC | AL | SE | DO | DE | CFC | PO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Direction and appointments** | | | | | | | | |
| Set the Strategic Priorities, Envelopes, Guardrails, and the mix of Initiatives | A | C | R | | C | | | |
| Appoint the AICC Lead, name the members of the AI Steering Committee, and name acting persons | A | | I | | | | | |
| Decide the AI Risk Appetite Statement | A | C | R | | | | C | |
| Own and review the AI Risk Appetite Statement, and activate the change | C | C | A | | | | C | |
| Activate and change the documents | I | | A | | | | | |
| Enter an appointment, an acting designation, a change, or a relief in the Appointments Record | I | | A | | | | | |
| Confirm, within the remit of a Control Function, the laws and regulations that apply to the use of AI in the Bank | I | | C | | | | A | |
| **Taking a need in and scoping it** | | | | | | | | |
| Take an item into discovery, or defer or reject it at triage, and scope it with the Domain Owner | I | | A | | C | C | | |
| **The business case and its clearance** | | | | | | | | |
| Approve the business case, below a guardrail and within a Domain; the Control Function Contacts clear it when Risk Tier 2 or 3 is expected | I | | R | | A | C | R | |
| Approve the business case, above a guardrail, across Domains, or for enabling work; the Control Function Contacts clear it when Risk Tier 2 or 3 is expected | A | C | R | | C | | R | |
| **The Service Agreement, the Outcome Report, and the benefit** | | | | | | | | |
| Issue the Service Agreement, and amend it when the business case is approved | | | A | C | C | | | |
| Issue the Outcome Report | | | A | R | C | | | |
| Confirm the benefit of an Engagement | | | R | | A | | | |
| **Ranking and pulling into work** | | | | | | | | |
| Rank the Portfolio Backlog and the Program Backlog, set the limit on the Active Initiatives within the mix, and take an Initiative into its MVP | I | C | A | | C | | | |
| **Design, build, and the MVP** | | | | | | | | |
| Define the Solution, and approve its Solution Definition | | | C | R | A | C | C | |
| Design and build a Solution and its MVP | | | I | A | C | R | C | C |
| Approve a Capability | | | A | | C | | | |
| Approve a Feature at Iteration Planning | | | C | A | C | C | | |
| Decide after the MVP, within a Domain and below a guardrail | I | | R | R | A | C | | |
| Decide after the MVP, above a guardrail, across Domains, or for enabling work | A | C | R | R | C | | | |
| **Test, check, or validation** | | | | | | | | |
| Check a Risk Tier 1 Solution, by the Checker | | | A | | I | | | |
| Validate a Risk Tier 2 or 3 Solution | | | C | C | I | | A | C |
| **Acceptance of Features and Capabilities** | | | | | | | | |
| Accept a Feature or a Capability, as the product owner of the Team (the AICC Lead while the Team has up to three people) | | | A | C | C | | | |
| **Final acceptance of the Team** | | | | | | | | |
| Give the final acceptance of the Team for a Solution, before it is deployed to its first users | | | A | R | I | | | |
| **Business acceptance and release** | | | | | | | | |
| Accept a Solution of a Domain as the requester, after it is deployed to its first users | | | R | | A | | | |
| Accept, as the requester, a Solution or an item that spans Domains, is enabling work of AICC, or is an Experiment with no Domain | A | | R | | C | | | |
| Complete the Acceptance Checklist, with the answers and the signatures of each party | | | A | R | R | | R | R |
| Release a Solution, Risk Tier 1 or 2 (the Executive Sponsor where the AICC Lead is the Domain Owner, Operating Model 4.4(d)) | | | C | R | A | | C | |
| Release a Solution, Risk Tier 3 | A | C | R | | C | | C | |
| **Operation, support, and the live review** | | | | | | | | |
| Run a Service that AICC runs, as the IT function that operates it, and handle its requests and incidents | | | C | A | C | | | C |
| Review the monitoring and the provider notices of a live Solution at each Iteration Review and Demo (the Executive Sponsor for a Service across Domains) | | | I | R | A | | | C |
| Take part in an AI Incident, which the incident management of the Bank owns | I | | A | R | I | | C | C |
| Provide the AI Platform | | | C | | | | | A |
| **Change and retirement** | | | | | | | | |
| Deploy to production, through the change management of the Bank, which approves the change | | | I | A | C | | | C |
| Decide whether a change to a released Solution needs a new check or validation | | | A | R | C | | C | |
| Suspend a Solution, by the AICC Lead | I | | A | R | I | | C | |
| Suspend or stop a Solution within the remit of a Control Function | I | | I | R | I | | A | |
| Retire a Solution of a Domain | | | C | R | A | | | |
| Retire a Service across Domains | A | C | R | R | C | | | |
| **Adoption in the Domain and training** | | | | | | | | |
| Scale adoption in the Domain and train colleagues | I | | C | C | A | R | | |
| Set the training for a Solution, and note in the AI Registry when its users are trained | | | A | R | C | C | | |
| Prepare a Proposal to adopt a Solution at scale; the Domain Owners concerned and the Executive Sponsor decide on it | C | | A | R | C | | | |
| **Oversight, the Risk Tier, and the AI Registry** | | | | | | | | |
| Assign the Risk Tier, and tell it to the Domain Owner (for a Solution that the AICC Lead built, the next row applies) | | | A | | I | | C | |
| For a Solution that the AICC Lead built: approve its Solution Definition, assign its Risk Tier, and approve its use for a data class | A | | R | R | C | | C | |
| Approve the use of a Solution in a Domain for a data class | | | R | R | A | | C | |
| Approve the use of a Solution in AICC for a data class (for a Solution that the AICC Lead built, the row above applies) | | | A | R | I | | C | |
| Keep the AI Registry | I | | A | R | | | C | |
| Meet the requirements for oversight in operation, disclosure, and contestability | | | C | C | A | | C | |
| Decide an Exception to a control requirement | | | C | | I | | A | |
| Approve a Data Sharing Arrangement | A | C | R | | C | | C | |
| Accept a risk beyond the AI Risk Appetite Statement, with notice to the Board Committee | A | C | R | | C | | C | |
| Approve output published to the Board or to investors | A | | R | | C | | C | |
| **The Quarterly Report and the records** | | | | | | | | |
| Prepare the Quarterly Report | I | I | A | | C | | C | |
| Approve the Quarterly Report, and decide whether to submit it to the Board Committee or the Board | A | | R | | | | | |
| Record the Steering Summary | A | C | R | | | | | |
| Keep the Appointments Record and the Registry Snapshot | I | | A | R | | | | |

## 5. The governing bodies

The following table states each body, who sits in it, and what it decides. A body is not a Role.

| Body | Purpose | Members | Rhythm | Decides | How it records |
| --- | --- | --- | --- | --- | --- |
| The Steering | Runs the direction, assurance, and control loops of the unit and the loops of the portfolio | The Executive Sponsor chairs; the AICC Lead prepares it and attends; the Domain Owners concerned and the Control Function Contacts attend; the AI Steering Committee advises (Operating Model 6.3) | Monthly, quarterly, and yearly | The Executive Sponsor decides the matters that the Operating Model 4.2 and 5.3 give to that Role; the Domain Owner decides the acceptance of a Solution | The Steering Summary and the Decision Records |
| AI Steering Committee | Advises the Executive Sponsor on the Portfolio and on conflicts between Domains | The heads of the business, technology, risk, and compliance functions, named in the Appointments Record | With the Steering | Nothing; it advises | Advice and dissent in the Steering Summary |
| The Control Functions | Set the rules of their remit, clear, validate, decide Exceptions, and may stop | Model risk, compliance, information security, data protection, and legal, each through its Control Function Contact | When their remit is concerned, and at the quarterly risk check | Within their remit: the clearance of a business case, validation, raising the Risk Tier, a suspension, a stop, and an Exception; nobody overrides them | The Control Sign-Off |
| Weekly Review | Runs the operating loop and the backlog care | The AICC Lead and the Team | Weekly | The AICC Lead adjusts the work, and raises to the monthly Steering what cannot be settled | The Dashboard and the working state |
| Board Committee | Oversees AI for the Board | As the Board names it | As it meets | Its own matters; it receives what the Executive Sponsor brings to it, and the notice of a major AI Incident and of a risk accepted beyond the appetite | Its own records; a Quarterly Report submitted to it, with its approval block |
| Internal audit | Gives independent assurance, outside the reporting chain | The audit function | As it plans | Nothing on the work of AICC; it does not validate, release, or stop | Its own reports; read access to the Registry and the Portfolio |

## 6. People: appointments, changes, and leavers

The following table states who appoints each Holder and who enters the appointment in the Appointments Record (Operating Model 4.6 to 4.8). An appointer does not appoint themselves to a Role: the next level appoints.

| Role or designation | Appointed or named by | Entered by |
| --- | --- | --- |
| Executive Sponsor | The Board | The AICC Lead, from the decision of the Board |
| AICC Lead | The Executive Sponsor | The AICC Lead |
| Members of the AI Steering Committee | The Executive Sponsor | The AICC Lead |
| Solution Engineer | The AICC Lead, from the people whom the functions assign, with the consent of the line manager and a stated time allocation | The AICC Lead |
| Checker of a Risk Tier 1 Solution, and the engineer who checks until AICC has a second Solution Engineer | The AICC Lead | The AICC Lead |
| Product owner other than the AICC Lead | The AICC Lead | The AICC Lead |
| Domain Owner | The head of the Domain | The AICC Lead |
| Domain Expert | The Domain Owner | The AICC Lead |
| Control Function Contact | The Control Function; the Executive Sponsor names an acting Contact | The AICC Lead |
| Platform Owner | The head of technology | The AICC Lead |
| Acting Holder | The Executive Sponsor | The AICC Lead |
| Deputy | The Holder | The AICC Lead |

The following table states what happens at each event in the life of a Holder.

| Event | What happens | Who | Record |
| --- | --- | --- | --- |
| An appointment | The person accepts the Role, declares any conflict of interest, names a deputy, receives the access that the Role needs, reads the documents, and completes the training that the AICC Lead sets for the Role (Operating Model 4.9) | The appointer named for the Role; the AICC Lead enters it | The Appointments Record, Part C, within five working days |
| An acting designation or a deputy | Each Holder names a deputy, who acts during an absence. A person acts in a vacant Role, marked as acting. A delegation of more than two weeks is entered in the Decision Log, and the Executive Sponsor delegates in writing | The Holder names a deputy; the Executive Sponsor names an acting Holder, and for a Control Function | The Appointments Record, and the Decision Log |
| A change or a relief | The Holder changes or is relieved, the access that the Role gave is removed, and the previous Holder is recorded | The appointer; the keeper of each tool removes the access | The Appointments Record, Part C and Part E |
| An assigned person | The person works for AICC while staying in their own line, with the consent of the line manager and a stated time allocation | The AICC Lead and the line manager | The Appointments Record, Part D |
| Competence and training | The documents are read and the training that a Role needs is completed and recorded | The Holder and the AICC Lead | The Appointments Record, Part D |
| Access to the tools | Access to Jira, Confluence, Service Management, and the repositories of the Registry and the Portfolio follows the Role and is reviewed at each quarterly Steering | The keeper of each tool | The Appointments Record, Part E |

The first week of a Holder runs in this order. The Holder accepts the Role and declares any conflict of interest. The line manager consents and the time allocation is stated, where the Holder is assigned. The AICC Lead enters the appointment in the Appointments Record within five working days, and the Holder names the deputy. Access to the tools is granted for the Role. The Holder reads the documents, following the reading path in the README of the charter, and completes the training that the Role needs as the AICC Lead sets it.

An appointment missing on 2026-10-02 is made by 2026-12-01, and the Executive Sponsor names acting Holders meanwhile (Operating Model 4.8). Its due date is entered in the Appointments Record, Part A.

The rules of separation of the Operating Model 4.4 apply to every appointment.

- Nobody checks or validates work that the person built.
- The owner of a Solution accepts it and does not validate it.
- A Control Function Contact is not a member of AICC.
- The AICC Lead may build a Solution, may accept its Features and Capabilities as product owner, and gives the final acceptance of the Team. The AICC Lead does not check, validate, release, or give the business acceptance of it, and the Executive Sponsor then approves its Solution Definition, assigns its Risk Tier, and approves its use for a data class.
- Until AICC has a second Solution Engineer, the person other than the builder who checks is an engineer of the IT function or the Domain whom the AICC Lead names in the Appointments Record.

While the Team is small, one person holds several Roles within these rules. Two combinations are accepted as limits: the AICC Lead issues the Service Agreement, delivers, and writes the Outcome Report (Business Model 7.5), and the AICC Lead gives the acceptance of the Features and the final acceptance of the Team for a Solution that the AICC Lead built (Solution Lifecycle Model 7.3(d)). Each accepted limit is listed in the Appointments Record, Part B, with its compensating controls, and is tracked in the Risks and Issues Record.

## 7. How the organization grows

The organization grows by adding Holders and Teams, and adds no layer, no meeting, and no Record (Operating Model 4.10). The following table states what changes at each step.

| When | What changes |
| --- | --- |
| AICC has a second Solution Engineer | The check by a person other than the builder is done within AICC, and the Executive Sponsor reviews the accepted limits of the AICC Lead |
| The AICC Lead names another person as the product owner of a Team | The person is entered in the Appointments Record, and accepts the Features and the Capabilities of that Team |
| The AICC Team has a fourth person | Light mode ends, and the events and the states run in full (Solution Lifecycle Model 6.6) |
| A Domain forms its own Team | The Team has its own product owner and runs on the same cadence, boards, and rules; the AICC Lead ranks the Program Backlog across the Teams and keeps the Program Board |
| A Solution is adopted at scale | The Handover goes to its Receiver, such as an IT function of the Bank, and AICC oversees it as an Adopted Solution |

## 8. Records and evidence

The charter holds the rules. The Portfolio holds the working state of the portfolio and the program, and Jira and Confluence run the daily work of the Teams. The Registry holds the governance records and the evidence records as closed and dated extracts, taken when an event happens, and a Registry Snapshot of the working state in the Portfolio at the close of each Iteration and PI and at the cutover. Jira, Confluence, and Service Management are not an evidence store. The Registry and the Portfolio are each kept in a repository with a protected main branch, their history is not rewritten, and each Record is kept for the period that the Bank requires for its type. Personal data in the Registry and in the Portfolio is limited to the names and the posts of the Holders, and the declarations, consents, and access of the Appointments Record (Operating Model 7.4). The Operating Model 8 lists the controls and the record that evidences each.

## 9. Rule source

Charter 3 to 7; Business Model 3 and 7; Operating Model 2, 4, 5, 6, 7, 8; Solution Lifecycle Model 3.5, 6.6, 7.3, 8.2; AI Policy 2 to 6; Document Catalog; the Unit governance workflow.
