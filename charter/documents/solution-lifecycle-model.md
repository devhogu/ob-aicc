```yaml
id: AICC-ORG-03-EN
title: Solution Lifecycle Model
status: active
revision: 1.6
created: 2026-10-01
revised: 2026-10-01
```

# Solution Lifecycle Model

## 1. Purpose and scope

1.1. This Solution Lifecycle Model states how the work of AICC moves from the Program Backlog to the retirement of a Solution, and how it is organized and paced on the way: the levels and the backlogs, the states and the Stages, the cadence of the program and the iteration, verification, release, and acceptance, and the management of the life cycle. The portfolio level, which decides which Initiatives are taken in, funded, and stopped, is in the Portfolio Management Model.

1.2. It applies to AICC and to the Domains and Control Functions of the Bank that work with AICC.

1.3. The Operating Model states how AICC is governed and controlled as a unit of the Bank: its Roles, its Decisions, its control loop, its records, and its controls. This model works within them, and the Operating Model prevails. The Portfolio Management Model states how the Initiatives are decided; this model takes the work from the Capabilities of an Initiative. The workflows of the charter show how the loops run: the engagement, the portfolio and service delivery, the cadence, the collaboration tooling, and the unit governance. They state no rule of their own.

## 2. Principles of delivery

2.1. AICC delivers on the following principles.

(a) Make work visible, limit work in progress, and pull work when there is capacity.

(b) Deliver in small steps: probe with a minimum viable product, measure against the success Measures, then scale.

(c) Put value first: rank work by value and urgency relative to effort.

## 3. Levels and backlogs

3.1. The work of AICC is structured in the levels of the following table. The Strategic Priority and the Initiative are managed by the Portfolio Management Model. A Team delivers the work: a Solution Engineer with the Domain Expert and the Domain Owner, who is the product owner. AICC has the AICC Team, and a Domain may have its own Team.

| Level | Meaning | Kept in |
| --- | --- | --- |
| Strategic Priority | A strategic theme set with the Board, with an Investment Envelope | Priorities |
| Initiative | A business program: a long-term business service or product that delivers one or more Solutions. An Initiative that has a client function is an Engagement, with one Service Agreement for each client function; the client of enabling work is the Executive Sponsor | Portfolio Backlog |
| Solution | A solution or service that an Initiative delivers for a Domain, with an offering type, a Risk Tier, and an AI Registry entry | The Portfolio, as a Solution Definition |
| Capability | A capability of a Solution, delivered over one or more Program Increments (PI) | Program Backlog |
| Feature | A deliverable of a Capability, which closes within one Program Increment and delivered over one or more Iterations | Program Backlog, then Iteration Backlog |
| Work Item | A task of a Team within a Feature | The Team board |

3.2. At this level AICC keeps two backlogs; the Portfolio Backlog is in the Portfolio Management Model. The Program Backlog, also called the PI Backlog, holds the Capabilities and the Features, grouped under their Initiatives. The Iteration Backlog holds the Features that the Teams work on in the Iteration. Each is ranked by value and urgency relative to effort, scored 1 to 5 for value, urgency, risk reduction or opportunity, and effort. The backlogs change continuously, because much of the work depends on people and events outside AICC. A Capability may run over several Program Increments. A Feature closes within its Program Increment. The items of a Program Increment state intent and direction, and what is done in an Iteration is decided in that Iteration.

3.3. Work flows as in Kanban. The Program Kanban shows the Capabilities and the Features by state, with the classes of service as lanes: Urgent, High priority, and Normal. The Limits on Work in Progress apply to the states, the lanes, and each Domain. The Team pulls an approved item only when there is capacity. At each Iteration Planning the Team selects the Features for the month from the Program Backlog into its Iteration Backlog, and the Weekly Review keeps them under control. An item that waits for a person or an event outside AICC is waiting, and names its Dependency.

## 4. States and Stages

4.1. Every Initiative, Solution, Capability, and Feature is in one of the states of the Vocabulary. A Strategic Priority is Proposed, Active, Closed, or Cancelled, as the Executive Sponsor decides. An item moves as the following table states. This table is the only source of the moves.

| From | To | When |
| --- | --- | --- |
| Proposed | Discovery | The AICC Lead takes it in: Initiatives, Solutions, and Capabilities, and Features at refinement |
| Proposed | Rejected, or Deferred | It is decided against at triage, or put on hold |
| Discovery | Approved | The conditions of its level in section 4.2 are met, and its approver decides |
| Discovery | Waiting, Deferred, Rejected, Pivoted, or Cancelled | A Dependency blocks it; it is put on hold; it is decided against; it is rerouted into a new item; or it is withdrawn without a decision on the merits |
| Approved | Active | The Team pulls it, when there is capacity and its Dependencies are known. An Initiative becomes active when the AICC Lead pulls it into its MVP (Portfolio Management Model 5.2). A Solution becomes active when its first Capability or Feature is pulled |
| Approved | Waiting, Deferred, Pivoted, or Cancelled | As for Discovery |
| Active | Completed | The work is finished |
| Active | Waiting, Deferred, Pivoted, or Cancelled | As for Discovery |
| Active | Rejected | Only for an Initiative at the end of its MVP: the value is not seen (Portfolio Management Model 7.2) |
| Active | Closed | Only for a Solution: it is retired, handed off, or ended, as section 7.1 states |
| Active | Discovery | Only for a Solution: a change raises its Risk Tier or the check or the validation named it as requiring a new check, as the AI Policy states |
| Waiting | The state it came from | The Dependency is cleared |
| Waiting | Deferred or Cancelled | The Dependency will not clear, or the item is withdrawn without a decision on the merits |
| Deferred | Proposed | It is taken up again, and the keeper may resume it at the state it left |
| Deferred | Rejected or Cancelled | It is decided against, if it was never approved, or it is withdrawn without a decision on the merits |
| Completed | Review | The product owner assesses it against its acceptance criteria |
| Review | Active, or Accepted, or Rejected | It is returned with what is missing; its criteria are met; or its outcome is not wanted |
| Accepted | Closed | The item is finished |

4.2. A Stage is a phase of the work inside the discovery state or the active state of an item. The Stages of an Initiative are in the Portfolio Management Model 5.2. The Stages, the approver, and the conditions of each level are in the following table. The AICC Lead shall confirm that the conditions are met and note it in the backlog of the level, or in the Portfolio for a Solution.

| Level | Discovery Stages | Approved by, and conditions | Active Stages | To be completed |
| --- | --- | --- | --- | --- |
| Solution | Definition | The Domain Owner approves the Solution Definition, with its type, Receiver, scope, capabilities, architecture, and data classes. The Risk Tier is assigned by the AICC Lead and told to the Domain Owner; the AI Registry entry is made; for Risk Tier 2 and 3, the Control Function Contact of compliance confirms the applicable law; an Experiment has its time-box and a Service its run cost and sunset | Delivery, then the Stages of its type in section 7.1 | It is delivered, as section 7.1 states |
| Capability | Analysis: define the capability and break it into Features | The AICC Lead, with the Domain Owner consulted. Its Features are defined and ranked in the Program Backlog | Implementation | Its Features are closed |
| Feature | Explore, Design | The Team, at Iteration Planning. Its acceptance criteria are stated, and its Dependencies are known, with any open one named | Develop, Verify, Deploy | It is deployed |

4.3. Rejected means decided against on the merits because the value is not seen, before approval or after the MVP of an Initiative, or when the outcome under review is not wanted. Cancelled means withdrawn without a decision on the merits, such as an error, a mistake, or a duplicate, and applies in any state from Discovery to Review except Completed. A suspension of a Solution is a flag on it, like waiting, and does not change its state. A stop by a Control Function is final and cancels the Solution. Retirement closes it, with no acceptance. The person who approves an item at its level also defers, rejects, cancels, or pivots it.

## 5. Cadence

5.1. Work runs in Program Increments. A Program Increment is one quarter, made of three Iterations. An Iteration is one calendar month of four or five whole weeks. The last week of the third Iteration of a Program Increment is the IP week. The Calendar Record states the dates and the blocked and gray days, and the Cadence workflow of the charter states the general flow of the events by week, without dates, which is the template for the dated calendar of events. The events of each loop are listed below. A Team of one holds them short and records them in the Iteration Backlog.

The events of the delivery loops are the Daily Stand-up, the Weekly Planning, the Weekly Review, the Backlog Refinement, the Iteration Planning, the Iteration Review and Demo, the Iteration Retrospective, the PI Review and Demo, Inspect and Adapt, the PI Planning, and the Innovation. The monthly Steering and the quarterly Steering are the events of the control loops of the Operating Model 6 and of the portfolio loops of the Portfolio Management Model 4, and they take the results of the Iteration Review and Demo and of the PI Review and Demo. The Cadence states the intent, the inputs, and the outputs of each.

5.2. An event that falls on a blocked or gray day moves to the working day before it, and never after. When moved events meet on one day, the larger event keeps the day and the smaller one moves to the working day before it. An event that is missed is not held later, and its intent is covered at the next event. The Weekly Review may be held in writing.

5.3. While the AICC Team has up to three people, AICC runs in light mode. The Weekly Planning and the Weekly Review are one session, held on the day of the Weekly Planning. The Iteration Retrospective and the monthly Steering are held in the Iteration Review and Demo, and Inspect and Adapt is held in the PI Review and Demo. The Daily Stand-up, the Backlog Refinement, and the Innovation are optional. In light mode Waiting is a flag, Completed is skipped and an item goes from Active to Review, Accepted and Closed are one step with the acceptance recorded, Stages are used for Initiatives and Solutions only, and Work Items are not tracked in the charter. Everything else stays as stated.

5.4. The PI Planning proposes the Roadmap, and the quarterly Steering confirms it (Operating Model 6.6). The Roadmap shows three months: the current Program Increment as intent and direction, the next as planned, and the period beyond as indicative, with its Milestones. The Dependency Map shows, for each item of a Program Increment, what it needs from other items, Teams, functions, and persons, and breaks the item into the scope of each month. The Dashboard shows the state of the Program Increment, the flow of the Program Kanban, the Dependencies at risk, the risks, and the Measures. The AICC Lead keeps them current, and they are Records.

## 6. Verification, release, and acceptance

6.1. The check for Risk Tier 1 and the validation by the Control Function Contacts for Risk Tier 2 and 3 attach to the Solution. They are taken in Verify of the first Feature that reaches real users or data, they cover the later Features unless a change requires a new one, which the AICC Lead shall decide and enter, with the reason, in the Solution Definition, and no deployment to real users or data comes before them. A deployment to production follows the change management of the Bank, the Solution Engineer shall enter the change ticket and the test result in the Feature, and the access of a Solution Engineer to production is granted through the access process of the Bank. The release of a Solution beyond its first users is decided by the Domain Owner for Risk Tier 1 and 2, and by the Executive Sponsor for Risk Tier 3, after the check or the validation, and is recorded in the Solution Definition. A Feature that cannot close within its Program Increment is split: the part that is done is a Feature that goes to review, and the rest is a new Feature in the next Program Increment. The original Feature is Pivoted and linked to both.

6.2. The Control Function Contacts that this model and the AI Policy name shall take part when a Solution of Risk Tier 2 or 3 is defined and in its validation. The validation relies on the evidence, the logs, and the traces that the Platform Owner keeps.

6.3. Acceptance closes an item. The product owner accepts the delivered outcome against its acceptance criteria, and the AICC Lead notes the acceptance with who and when in the backlog of the level. The product owner is the Domain Owner for an item of a Domain, and the Executive Sponsor for an item that spans Domains or is enabling work of AICC. The product owner may accept the item, return it with what is missing, or reject it when its outcome is not wanted. The acceptance of an Engagement is recorded in its Outcome Report.

6.4. When AICC hands a Solution to a Domain as ready for use at scale, before its release beyond the first users, the AICC Lead completes the Acceptance Checklist of the Solution. The checklist lists, for each party concerned, the items that the party confirms within its remit and signs: the Domain Owner, the Solution Engineer, the AICC Lead, the Checker, the Control Functions (model risk, compliance, information security, data protection, and legal), and the IT function that operates the Solution with the Platform Owner. An item that is not met shall stop the release. The Domain Owner receives the checklist signed and signs the acceptance of the package. A Domain adopts a Solution of Risk Tier 1 or 2 on its own risk, within the AI Risk Appetite Statement. A Solution of Risk Tier 3, which is of high impact and risk, is adopted only with the signature of the Executive Sponsor, who accepts the risk and releases it. The checklist is not used during development or trials, where 6.1 applies, and a change after the release that requires a new check or validation brings a new checklist. It adds no approval of its own: the decisions are those that the AI Policy and this model state.

## 7. Life-cycle management

7.1. A Solution has one offering type, which sets its life after delivery. A Solution is delivered when its first deployment is released. The Initiative is complete once its Solutions are delivered and its outcome is reviewed, and a Service and a Product go on under their own type. A Solution is Active from the start of its delivery to the end of its life, and it is Closed when it is retired, handed off, or ended. The Receiver is named in the Solution Definition before the Solution is approved, and an Experiment may name "none yet, to be asked". The following table states the types.

| Type | Owner after delivery | Stages after delivery | End |
| --- | --- | --- | --- |
| Service | AICC, for the whole life cycle, with a business case that states the run cost and a sunset rule. The product owner is the Domain Owner of the Domain it serves, and the Executive Sponsor for a Service across Domains | Operate, Evolve, Retire. New features come as Capabilities and Features | Retired, or cancelled |
| Product | The consumer owns the version delivered, and AICC supports it on demand | Handover, Support, Revise (a new version comes through the Portfolio Backlog), Retire for that consumer. A Product with many consumers or recurring requests becomes a Service through a business case | Retired for that consumer |
| Experiment | None yet: it is time-boxed to a stated number of Iterations, and ends in a Proposal. Its product owner is the Executive Sponsor when it has no Domain | Trial, Proposal, Handover | At the end of its time-box it goes to review: it is accepted with its lessons and closed, a Proposal is made, or it is cancelled. When a Receiver accepts the Handover, it is closed and AICC oversees the Adopted Solution |

The phases of an Engagement map to the items as follows: the study is the discovery of the Initiative, the proof is the Experiment or the first Features of the Solution, delivery is the active state of the Capabilities and Features, and support is the life of the Solution after delivery.

7.2. AICC oversees and reports on the Adopted Solutions that others deliver, in the Portfolio, as a Solution Definition marked as an Adopted Solution with its Receiver as owner. It is recorded when others begin to deliver a Solution that AICC proposed or oversees. It uses the states Proposed, Approved, Active, Closed, Rejected, and Cancelled, and records the Risk Tier when it is known. The owners and the Executive Sponsor decide on a Proposal of a Solution, and the Bank decides on a Proposal of the AI adoption strategy. The AI adoption strategy is a series of Proposals that AICC shapes from what it learns.

7.3. A change to a released Solution is a Feature. A change of model, provider, data class, degree of autonomy, or any attribute of the Risk Tier is significant. The AICC Lead shall decide whether a change requires a new check or validation, and the Domain Owner, or the Executive Sponsor for Risk Tier 3, releases it. A change to a Solution in production follows the change management of the Bank, and the Solution Engineer shall enter the change ticket and the test result in the Feature. An emergency change may be deployed on the decision of the AICC Lead, and shall be reviewed and entered in the Decision Log within five working days. A change of terms or of model by a provider is a change under this clause.

7.4. The product owner of a live Solution shall review its monitoring, its incidents, its use, and the notices of its providers at each Iteration Review and Demo, and shall note the review in the Solution Definition.

7.5. Before a Solution is Closed as retired, the Solution Engineer shall remove the access and the credentials, the data and the logs shall be kept or deleted under the retention rules of the Bank, and the AI Registry entry shall be marked retired. The Domain Owner, or the Executive Sponsor for a Service across Domains, approves the retirement, and the approval is entered in the Solution Definition.

## Change log

| Revision | Date | Change | Decision |
| --- | --- | --- | --- |
| 1.0 | 2026-10-01 | Created from the Operating Model: the flow of work, the states and Stages, the cadence of the delivery loops, verification, release, acceptance, and the life cycle of a Solution. | DR-2026-040 |
| 1.1 | 2026-10-01 | The Acceptance Checklist at the handover of a ready Solution to a Domain for use at scale; the Executive Sponsor signs for Risk Tier 3. | DR-2026-041 |
| 1.2 | 2026-10-01 | Auditor review: change after release (7.3), review of live Solutions (7.4), retirement (7.5), production deployment, a stop is final (4.3), and clauses split. | DR-2026-042 |
| 1.3 | 2026-10-01 | The portfolio layer moved to the Portfolio Management Model; Capability replaces Epic outside Jira; an Initiative becomes active when it is pulled into its MVP. | DR-2026-044 |
| 1.4 | 2026-10-01 | Rejected is a decision on the merits, including after the MVP and in review; Cancelled is a withdrawal without such a decision. | DR-2026-045 |
| 1.5 | 2026-10-01 | Citations of the Portfolio Management Model follow its new numbering. | DR-2026-047 |
| 1.6 | 2026-10-01 | Iteration written in full; the review outcome is Rejected; the pilot becomes a probe; light mode keeps Pivoted. | DR-2026-048 |
