```yaml
id: AICC-ORG-01-EN
title: Operating Model
status: active
revision: 6.1
created: 2026-09-29
revised: 2026-10-01
```

# Operating Model

## 1. Purpose and scope

1.1. This Operating Model states how AICC works: who does what, how work flows, how Decisions are taken, and what is
kept on record.

1.2. It applies to AICC and to the Domains and Control Functions of the Bank and of each Participating Entity that work with
AICC.

1.3. The workflows of the charter show how the loops run: the unit governance, the portfolio and service delivery, and the
cadence. They state no rule of their own, and this Operating Model prevails.

## 2. What AICC is

2.1. AICC is a small team of engineers that provides the governance framework and the program office for the adoption of
AI in the Bank and the Group, and builds Solutions with the Domains.

2.2. AICC does not own the AI Platform, the Solutions, or the business results of the Domains. The Domains execute. AICC
directs, guides, and may supply AICC Engineers to build and run Solutions.

2.3. AICC is a first-line function. The Control Functions are independent of it. Each Entity keeps its own regulator,
accountability, Control Functions, and data.

## 3. Principles of work

3.1. AICC works on the following principles.

(a) Decide where the facts are. The person closest to the work decides, on evidence.

(b) Keep decisions reversible where possible, and take reversible decisions quickly.

(c) Make work visible, limit work in progress, and pull work when there is capacity.

(d) Deliver in small steps: pilot, measure against the success Measures, then scale.

(e) Put value first: rank work by value and urgency relative to effort.

(f) Deliver at product speed within bank-grade control.

(g) Keep only the process and the records that someone uses, and remove the rest.

3.2. AICC shall apply the Values and the Principles of the Statement of Intent.

## 4. Roles

4.1. AICC uses seven Roles. One person may hold several Roles, and a Role may have several Holders, within the rules of
separation in section 4.4.

4.2. The following table states each Role and what its Holder does and decides.

| Role | Does | Decides |
| --- | --- | --- |
| Executive Sponsor | Holds the mandate and the funding; appoints the AICC Lead; approves and issues the report to the Board Committee | The Strategic Priorities, the Investment Envelopes, and the Investment Guardrails; the release of a Risk Tier 3 Solution; any risk beyond the AI Risk Appetite Statement; the retirement of an Initiative; the approval of AI output published outside AICC; the acceptance of an item that spans Domains or is enabling work of AICC; the naming of acting Contacts |
| AICC Lead | Leads AICC as its lead engineer and architect; is accountable for this Operating Model and for every document and Record of AICC; prepares the Quarterly Report; presents to the AI Steering Committee | Taking an item into discovery; the approval of Epics; the approval of the use of a Solution in AICC for a data class; the Risk Tier, which the AICC Lead tells to the Domain Owner; the suspension of a Solution; standards, architecture, and Templates; questions between Domains; the activation of every document; an Exception to a requirement set by AICC |
| AICC Engineer | Builds and runs Solutions with the Domains; keeps the work visible; coaches Domain Experts; checks the work of others | How a Solution is built; the approval of Features at IT Planning; the order in which the team pulls work within the agreed priorities |
| Domain Owner | Owns the results of AI adoption in the Domain and acts as product owner of its Solutions; names the Domain Expert | Whether the Domain takes part in an Initiative; funding of the Solutions of the Domain; the approval of the use of a Solution in the Domain for a data class, and the approvals that the rules of the Bank require; the acceptance of an item of the Domain; the release of a Risk Tier 1 or 2 Solution, after the check or the validation; the retirement of a Solution |
| Domain Expert | Explains the routine work; works with the AICC Engineer; tries the Solution in real work; then scales adoption and trains colleagues | Nothing on funding, acceptance, or control |
| Control Function Contact | Advises on requirements; may raise the Risk Tier within its remit, and the Contact of model risk alone may lower it; validates Solutions; may stop a Solution | Validation, raising the Risk Tier, a stop, and an Exception to a control requirement, each within the remit of the Control Function |
| Platform Owner | Provides and operates the AI Platform, outside AICC, to the requirements in the Standards Record; keeps the evidence, logs, and traces on which the validation relies | The design of the AI Platform within those requirements |

4.3. The team of AICC agrees who takes the Hats that the work needs, such as the keeper of the Program Backlog, the facilitator of
the events, or the coach. A Hat is not a Role, changes when the team decides, and needs no appointment.

4.4. The rules of separation are as follows.

(a) No person shall validate or check work that the person built.

(b) The Domain Owner of a Solution accepts it and, for Risk Tier 1 and 2, releases it, and shall not validate it.

(c) A Control Function Contact is not a member of AICC and shall not build Solutions that the Contact reviews.

(d) The AICC Lead may build, and shall not validate a Solution within the remit of a Control Function.

(e) A check by a person other than the builder is done by an engineer of the technology function or the Domain whom the AICC Lead names in the Appointments Record, until AICC has a second engineer.

(f) Internal audit gives assurance only. It shall not validate, release, or stop, and has read access to every Record.

4.5. The AI Steering Committee is the group of the heads of the business, technology, risk, and compliance functions of the
Bank and of the Participating Entities. It advises the Executive Sponsor, who chairs it. It is formed of the heads who are named, and a function joins when its head is named. The Board Committee oversees AI for
the Board and receives the report of the Executive Sponsor. Neither is a Role.

4.6. The Holders of the Roles are named in the Appointments Record. The Executive Sponsor appoints the AICC Lead. The AICC Lead
appoints the AICC Engineers. The head of a Domain names the Domain Owner, and the Domain Owner names the Domain Expert. Each
Control Function names its Control Function Contact for each Entity. The head of technology names the Platform Owner. Each Holder shall name a deputy in the Appointments Record, who acts during an absence, and a delegation of more than two weeks is entered in the Decision Log. An Appointment missing at the activation of this Operating Model shall be made within 60 days, and the Executive Sponsor names acting Holders meanwhile. Until a head of function or the Platform Owner is named, the Executive Sponsor names an acting Holder. For the work of AICC itself, the AICC Lead is the Domain Owner.

## 5. Decisions

5.1. A Decision is taken by the person who does the work, on the facts, at the moment it is needed. A Decision states the
facts that it rests on, such as a measurement, a test result, a cost, or a source.

5.2. A Decision goes to a higher level only when at least one of the following is true.

(a) It affects another Domain or Entity, or sets a standard for others.

(b) It cannot be reversed without significant cost or harm.

(c) It exceeds an Investment Guardrail or changes a Strategic Priority.

(d) It accepts a risk, or concerns a Risk Tier 3 Solution.


5.3. The level is stated in the following table. A Decision goes to the level that section 4.2 names for the matter when a
condition in 5.2 applies.

| Level | Who decides | Examples |
| --- | --- | --- |
| Team | The AICC Engineer, with the Domain Expert and Domain Owner | Design, build, pulling work |
| AICC Lead | The AICC Lead | Taking an item into discovery, standards, Templates, questions between Domains |
| Executive Sponsor | The Executive Sponsor, after asking the AI Steering Committee | Strategic Priorities, funding, release of a Risk Tier 3 Solution, risks beyond appetite, retirement of an Initiative |

5.4. A Control Function decides within its remit, and its validation or stop is final for that remit. Nobody shall override it. A
disagreement goes to the head of that Control Function. The Executive Sponsor may raise it with executive management and shall
not set a validation or a stop aside. A risk beyond the AI Risk Appetite Statement may be accepted only with a report to the
Board Committee. The person who suspended or stopped a Solution lifts the suspension
or stop when the facts allow.

5.5. Where the people concerned do not agree, the person who holds the decision under 5.3 decides after hearing them. The
others then support the Decision. A dissent may be noted in the Decision Log.

5.6. A Decision at the AICC Lead level or above, and any Decision that others will need to find later, shall be entered in the
Decision Log as one line: the date, the Decision, the facts, who decided, and when to revisit it. A Decision of the
Executive Sponsor that is hard to reverse also has a short note. A Decision of the Team is noted in the work item.

5.7. A person with a conflict of interest on a Decision shall declare it and shall not decide. The next level decides.

## 6. How work flows

6.1. The work of AICC is structured in the levels of the following table. A Team delivers the work: an AICC Engineer with the
Domain Expert and the Domain Owner, who is the product owner. AICC has the AICC Team, and a Domain may have its own Team.

| Level | Meaning | Kept in |
| --- | --- | --- |
| Strategic Priority | A strategic theme set with the Board, with an Investment Envelope | Priorities |
| Initiative | A business program: a long-term business service or product that delivers one or more Solutions | Portfolio Backlog |
| Solution | A solution or service that an Initiative delivers for a Domain, with an offering type, a Risk Tier, and an AI Registry entry | The Portfolio, as a Solution Definition |
| Epic | A capability of a Solution, delivered over one or more Program Increments | Program Backlog |
| Feature | A deliverable of an Epic, which closes within one Program Increment | Program Backlog, then IT Backlog |
| Work Item | A task of a Team within a Feature | The Team board |

6.2. AICC keeps three backlogs. The Portfolio Backlog holds the Initiatives. The Program Backlog, also called the PI Backlog, holds
the Epics and the Features. The IT Backlog holds the Features that the Teams work on in the IT. Each is ranked by value and urgency
relative to effort, scored 1 to 5 for value, urgency, risk reduction or opportunity, and effort. The backlogs change continuously,
because much of the work depends on people and events outside AICC. An Epic may run over several Program Increments. A Feature
closes within its Program Increment. The items of a Program Increment state intent and direction, and what is done in an IT is
decided in that IT. Every Initiative is written in a one-page Initiative Brief, which is its business case, and an Initiative that exceeds an Investment Guardrail needs the approval of the Executive Sponsor. An Epic of enabling work may sit directly under an Initiative, without a Solution. Enabling work of
AICC that builds no AI Solution has no Risk Tier.

6.3. Work flows as in Kanban. The Portfolio Kanban shows the Initiatives by state. The Program Kanban shows the Epics and the
Features by state, with the classes of service as lanes: Incident, High priority, and Normal. The Limits on Work in Progress apply
to the states, the lanes, and each Domain. The Team pulls an approved item only when there is capacity. At each IT Planning the Team
selects the Features for the month from the Program Backlog into its IT Backlog, and the Weekly Review keeps them under control.
An item that waits for a person or an event outside AICC is waiting, and names its Dependency.

6.4. Every Initiative, Solution, Epic, and Feature is in one of the states of the Vocabulary. A Strategic Priority is Proposed,
Active, Closed, or Cancelled, as the Executive Sponsor decides. An item moves as the following table states. This table is the only
source of the moves.

| From | To | When |
| --- | --- | --- |
| Proposed | Discovery | The keeper of the backlog of its level takes it in: the AICC Lead for Initiatives, Solutions, and Epics, and for Features at refinement |
| Proposed | Rejected, or Deferred | It is decided against at triage, or put on hold |
| Discovery | Approved | The conditions of its level in section 6.5 are met, and its approver decides |
| Discovery | Waiting, Deferred, Rejected, Pivoted, or Cancelled | A Dependency blocks it; it is put on hold; it is decided against; it is rerouted into a new item; or it is no longer needed |
| Approved | Active | The Team pulls it, when there is capacity and its Dependencies are known |
| Approved | Waiting, Deferred, Pivoted, or Cancelled | As for Discovery |
| Active | Completed | The work is finished |
| Active | Waiting, Deferred, Pivoted, or Cancelled | As for Discovery |
| Active | Discovery | Only for a Solution: a change raises its Risk Tier or the check or the validation named it as requiring a new check, as the AI Policy states |
| Waiting | The state it came from | The Dependency is cleared |
| Waiting | Deferred or Cancelled | The Dependency will not clear, or the item is no longer needed |
| Deferred | Proposed | It is taken up again, and the keeper may resume it at the state it left |
| Deferred | Rejected or Cancelled | It is decided against, if it was never approved, or it is no longer needed |
| Completed | Review | The product owner assesses it against its acceptance criteria |
| Review | Active, or Accepted, or Cancelled | It is returned with what is missing; its criteria are met; or its outcome is no longer wanted |
| Accepted | Closed | The item is finished |

Rejected applies only before an item is approved. Cancelled applies after it. A suspension of a Solution is a flag on it, like waiting,
and does not change its state. A stop by a Control Function cancels the Solution. Retirement closes it. The person who approves an item at
its level also defers, rejects, cancels, or pivots it.

6.5. A Stage is a phase of the work inside the discovery state or the active state of an item. The Stages, the approver, and the
conditions of each level are in the following table. The AICC Lead shall confirm that the conditions are met and note it in the backlog
of the level, or in the Portfolio for a Solution.

| Level | Discovery Stages | Approved by, and conditions | Active Stages | To be completed |
| --- | --- | --- | --- | --- |
| Initiative | Scoping, Business case | The Domain Owner, and the Executive Sponsor above a guardrail. The scope is agreed, and the business case in the Initiative Brief is approved | Implementation | Its Solutions are delivered, and its outcome is reviewed |
| Solution | Definition | The Domain Owner approves the Solution Definition, with its type, Receiver, scope, capabilities, architecture, and data classes. The Risk Tier is assigned by the AICC Lead and told to the Domain Owner; the AI Registry entry is made; for Risk Tier 2 and 3, the Control Function Contact of compliance confirms the applicable law; an Experiment has its time-box and a Service its run cost and sunset | Delivery, then the Stages of its type in section 6.7 | It is delivered, as section 6.7 states |
| Epic | Analysis: define the capability and break it into Features | The AICC Lead, with the Domain Owner consulted. Its Features are defined and ranked in the Program Backlog | Implementation | Its Features are closed |
| Feature | Explore, Design | The Team, at IT Planning. Its acceptance criteria are stated, and its Dependencies are known, with any open one named | Develop, Verify, Deploy | It is deployed |

6.6. The check for Risk Tier 1 and the validation by the Control Function Contacts for Risk Tier 2 and 3 attach to the Solution. They are
taken in Verify of the first Feature that reaches real users or data, they cover the later Features unless a change requires a new
one, and no deployment to real users or data comes before them. The release of a Solution beyond its first users is decided by the
Domain Owner for Risk Tier 1 and 2, and by the Executive Sponsor for Risk Tier 3, after the check or the validation, and is recorded in
the Solution Definition. A Feature that cannot close within its Program Increment is split: the part that is done is a Feature that
goes to review, and the rest is a new Feature in the next Program Increment. The original Feature is Pivoted and linked to both.

6.7. A Solution has one offering type, which sets its life after delivery. A Solution is delivered when its first deployment is
released. The Initiative is complete once its Solutions are delivered and its outcome is reviewed, and a Service and a Product go on
under their own type. A Solution is Active from the start of its delivery to the end of its life, and it is Closed when it is retired,
handed off, or ended. The Receiver is named in the Solution Definition before the Solution is approved, and an Experiment may name
"none yet, to be asked". The following table states the types.

| Type | Owner after delivery | Stages after delivery | End |
| --- | --- | --- | --- |
| Service | AICC, for the whole life cycle, with a business case that states the run cost and a sunset rule. The product owner is the Domain Owner of the Domain it serves, and the Executive Sponsor for a Service across Domains | Operate, Evolve, Retire. New features come as Epics and Features | Retired, or cancelled |
| Product | The consumer owns the version delivered, and AICC supports it on demand | Handover, Support, Revise (a new version comes through the Portfolio Backlog), Retire for that consumer. A Product with many consumers or recurring requests becomes a Service through a business case | Retired for that consumer |
| Experiment | None yet: it is time-boxed to a stated number of ITs, and ends in a Proposal. Its product owner is the Executive Sponsor when it has no Domain | Trial, Proposal, Handoff | At the end of its time-box it goes to review: it is accepted with its lessons and closed, a Proposal is made, or it is cancelled. When a Receiver accepts the Handoff, it is closed and AICC oversees the Adoption |

6.8. AICC oversees and reports on the Adoption of Solutions that others deliver, in the Portfolio. An Adoption is recorded when others
begin to deliver a Solution that AICC proposed or oversees. It uses the states Proposed, Approved, Active, Closed, Rejected, and
Cancelled, and records the Risk Tier when it is known. The owners and the Executive Sponsor decide on a Proposal of a Solution, and the
Bank decides on a Proposal of the AI adoption strategy. The AI adoption strategy is a series of Proposals that AICC shapes from what it
learns.

6.9. Acceptance closes an item, as in agile work. The product owner accepts the delivered outcome against its acceptance criteria,
and the AICC Lead notes the acceptance with who and when in the backlog of the level. The product owner is the Domain Owner for an
item of a Domain, and the Executive Sponsor for an item that spans Domains or is enabling work of AICC. The product owner may accept
the item, return it with what is missing, or cancel it when its outcome is no longer wanted.

6.10. The Roadmap shows three months: the current Program Increment as intent and direction, the next as planned, and the period
beyond as indicative, with its Milestones. The Dependency Map shows, for each item of a Program Increment, what it needs from other
items, Teams, functions, and persons, and breaks the item into the scope of each month. The Dashboard shows the state of the
Program Increment, the flow of the Program Kanban, the Dependencies at risk, the risks, and the Measures. The AICC Lead keeps them
current, and they are Records.

6.11. The Control Function Contacts shall take part when a Solution is defined, in validation, and in the quarterly risk check of the
PI Review. Evidence is taken from the records of the AI Platform.

## 7. Cadence

7.1. Work runs in Program Increments. A Program Increment is one quarter, made of three Iterations. An Iteration is one calendar
month of four or five whole weeks. The last week of the third Iteration of a Program Increment is the IP week.
The Calendar Record states the dates and the blocked and gray days, and the Cadence Record states the general flow of the events by
week, without dates, which is the template for the dated calendar of events. The events of each loop are in the following table, each with its intent. A Team of one holds them short and records them
in the IT Backlog or the Notes.

| Loop | Event | Intent |
| --- | --- | --- |
| Day | Daily Stand-up | Share progress, and clear blockers |
| Week | Weekly Planning | Set the focus of the week from the IT Backlog, and check the Dependencies |
| Week | Weekly Review | Keep control of the flow: review the Program Kanban and the Dependency Map, reorder the Program Backlog, and note what changed |
| Iteration | Backlog Refinement | Keep the next items of the backlogs ready |
| Iteration | IT Planning | Select the Features for the month from the Program Backlog into the IT Backlog, for the Iteration goal |
| Iteration | IT Review and Demo | Show working Solutions to the Domain Owners and Domain Experts, and take acceptance and feedback |
| Iteration | IT Retrospective | Improve the way of working |
| Iteration | Steering, monthly | Review progress, risks, and blockers, and take the Decisions of the Executive Sponsor, in the review week |
| Program Increment | PI Review and Demo | Show what the Program Increment delivered, score the value achieved against the PI Objectives, review the risks (the quarterly risk check), and produce the Quarterly Report |
| Program Increment | Inspect and Adapt | Review the results and the flow, solve the main problems, and put improvements in the Program Backlog |
| Program Increment | PI Planning | Set the intent and direction, the Roadmap, and the Dependencies for the next Program Increment |
| Program Increment | Innovation | Time to learn, explore, and recover |
| Program Increment | Steering, quarterly | Assess the results of the past quarter, confirm priorities and funding, and confirm the Maturity Level reached |

7.2. A meeting runs with those who are named. While the AI Steering Committee is not formed, the Executive Sponsor decides alone.
Notes are kept only for the Decisions and the actions, which go to the Decision Log and the work items.

7.3. The first quarterly Steering of the year also sets the Strategic Priorities, the Investment Envelopes, the Investment
Guardrails, and the Roadmap, and reviews the Statement of Intent, the AICC Charter, this Operating Model, the AI Policy, and the AI
Risk Appetite Statement. The Executive Sponsor calls an extra review on a material change in the use of AI, in a principal
provider, or in regulation, or after an audit or supervisory finding.

7.4. The Executive Sponsor may take a time-critical Decision between meetings after asking the heads of the risk and compliance
functions and recording the answers.

## 8. Engaging a Domain

8.1. The AICC Lead discusses adoption with the Domain Owner, who names a Domain Expert, usually the person who does the routine
work. The first Solution is narrow. An AICC Engineer, or an engineer of the technology function or the Domain under AICC
direction, builds the Solution with the Domain Expert, and the states in section 6.4 follow.

## 9. Records

9.1. Until Jira and Confluence run the work, the Registry is the live state and is kept current by hand. After that, Jira and Confluence hold the live state, and the Registry holds the Records as files: the record of each outcome that audit may ask for, taken when the event happens and at the close of each IT and PI. The history of the files is the audit trail and is not rewritten. A Record is kept by
whoever does the work, and the AICC Lead is accountable for all of them. A Record is closed, not deleted, and is kept for the
period that the record retention rules of the Bank require. Internal audit has read access.

9.2. The Records are as follows.

| Record | Holds |
| --- | --- |
| Priorities | The Strategic Priorities, and references to the Investment Envelopes, the Investment Guardrails, and the Measures of the Maturity Levels, with owner and source of each figure |
| Portfolio Backlog | The ranked Initiatives, with their state, Stage, and the product owner who accepts them |
| Program Backlog | The ranked Epics and Features, with their state, Stage, scores, and the product owner who accepts them |
| Portfolio Kanban and Program Kanban | The Initiatives, and the Epics and Features, by state, with the classes of service as lanes and the Limits on Work in Progress |
| Roadmap | The three-month Roadmap by Program Increment, and the Milestones |
| Calendar | The Program Increments, the Iterations, the weeks, and the blocked and gray days |
| Cadence | The general flow of the events by week, without dates, which is kept in the charter |
| Teams | The Teams, their members, Domains, and capacity |
| Program Increment | For each: the PI Objectives as intent and direction, the Iterations with their IT Backlogs and Weekly Review notes, and the results of the IP week |
| Dependency Map | For each item of a Program Increment: its Dependencies on other items, Teams, functions, and persons, and its scope by month |
| Dashboard | The state of the Program Increment, the flow, the Dependencies at risk, the risks, and the Measures |
| Decision Log | The Decisions, one line each |
| AI Registry | Each Solution, model, and agent, with owner, scope, data access, approval, Risk Tier, model versions, knowledge sources, and reassessment date |
| Risks and Issues | Risks, issues, AI Incidents, Exceptions, and Findings, one line each, with owner and status |
| Appointments | The Holders of the Roles, with the date of appointment |
| Standards | The architecture standards and the requirements that the use of AI places on the AI Platform |
| Reports | The Quarterly Reports |
| Notes | The notes of the events that need them |
| Initiatives | One folder for each Initiative, with its brief and its Epics and Features |
| Portfolio | The catalog of the Solutions, with their Solution Definitions, and of the Adoptions that others deliver |

9.3. The Templates for the Records that need a form are listed in the Document Catalog. Every other Record is a table that its
keeper adapts as needed.

## Change log

| Revision | Date | Change | Decision |
| --- | --- | --- | --- |
| 0.8 to 1.1 | 2026-09-30 | Drafted and revised. | none |
| 2.0 | 2026-09-30 | Rewritten: seven Roles, three meetings, three Decision levels, one Decision Log. Replaces the Roles and Responsibilities, Decision Rights, Governance Forums, Decision Management, Portfolio Management, Registers, Reporting, Service Catalog, and Artifact Standards. | DR-2026-009 |
| 2.1 | 2026-09-30 | Steering is monthly. | none |
| 2.2 | 2026-09-30 | The AI Steering Committee is formed of the heads who are named. | none |
| 2.3 | 2026-09-30 | Fixes from the independent check: separation and release, Risk Tier 3 release, Stages, interim checker, internal audit, deputy, yearly review, Records retention. | DR-2026-010 |
| 3.0 | 2026-09-30 | Second fixes from the independent check: release at the Pilot exit, acting Holders, Stage conditions, return to Discovery, checker wording. | DR-2026-011 |
| 3.1 | 2026-09-30 | Steering is monthly for tactical matters and quarterly for strategic matters. | none |
| 3.2 | 2026-09-30 | Acceptance fixes: Appointments transition, decisions of the AICC Lead and the Executive Sponsor, meetings with those named, Maturity Level confirmed, done for an Initiative. | DR-2026-015 |
| 3.3 | 2026-09-30 | The Domain Owner approves the use of a Solution in the Domain for a data class. | DR-2026-016 |
| 3.4 | 2026-09-30 | The AICC Lead assigns the Risk Tier and tells the Domain Owner. | DR-2026-017 |
| 3.5 | 2026-10-01 | Activated by the AICC Lead; activation of documents no longer goes to the Executive Sponsor. | DR-2026-018 |
| 3.6 | 2026-10-01 | Acceptance by the product owner closes a Backlog item. | DR-2026-019 |
| 4.0 | 2026-10-01 | Program Increments, Iterations, Program Backlog, Iteration Backlog, Program Kanban, Roadmap, Dependency Map, Dashboard, and the events of each loop with their intent. | DR-2026-020 |
| 5.0 | 2026-10-01 | Iterations are calendar months of four or five weeks; Kanban lanes; weekly review; Program Increment items state intent and direction; Cadence Record. | DR-2026-021 |
| 5.1 | 2026-10-01 | Weekly Planning added; the Cadence Record is the general flow without dates. | DR-2026-022 |
| 5.2 | 2026-10-01 | Event names use the short forms IT and IP. | DR-2026-023 |
| 5.3 | 2026-10-01 | The Priorities Record holds references to figures, not figures. | none |
| 5.4 | 2026-10-01 | Refers to the workflows of the charter. | none |
| 6.0 | 2026-10-01 | Initiatives, Solutions, Epics, and Features; the Portfolio, Program, and IT Backlogs; thirteen states with Stages inside discovery and active; offering types Service, Product, and Experiment; Adoption oversight; the live state in Jira and Confluence. | DR-2026-024 |
| 6.1 | 2026-10-01 | One transition table for the states; deciders for Epics, Features, and each exit; Solution lifecycle; validation attaches to the Solution; Experiment and Adoption rules; source of truth. | DR-2026-025 |
