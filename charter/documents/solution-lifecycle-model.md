```yaml
id: AICC-ORG-02-EN
title: Solution Lifecycle Model
status: active
revision: 1.1
created: 2026-10-01
revised: 2026-10-01
```

# Solution Lifecycle Model

## 1. Purpose and scope

1.1. This Solution Lifecycle Model states how a Solution moves from a business need to its retirement, and how the work is organized and paced on the way: the portfolio, the design, the delivery, and the management of the life cycle. Section 3 states the portfolio, section 4 the states and the Stages through design and delivery, section 5 the cadence, section 6 verification, release, and acceptance, and section 7 the life cycle.

1.2. It applies to AICC and to the Domains and Control Functions of the Bank that work with AICC.

1.3. The Operating Model states how AICC is governed and controlled as a unit of the Bank: its Roles, its Decisions, its control loop, its records, and its controls. This model works within them, and the Operating Model prevails. The workflows of the charter show how the loops run: the engagement, the portfolio and service delivery, the cadence, the collaboration tooling, and the unit governance. They state no rule of their own.

## 2. Principles of delivery

2.1. AICC delivers on the following principles.

(a) Make work visible, limit work in progress, and pull work when there is capacity.

(b) Deliver in small steps: pilot, measure against the success Measures, then scale.

(c) Put value first: rank work by value and urgency relative to effort.

## 3. Portfolio

3.1. The work of AICC is structured in the levels of the following table. A Team delivers the work: a Solution Engineer with the Domain Expert and the Domain Owner, who is the product owner. AICC has the AICC Team, and a Domain may have its own Team.

| Level | Meaning | Kept in |
| --- | --- | --- |
| Strategic Priority | A strategic theme set with the Board, with an Investment Envelope | Priorities |
| Initiative | A business program: a long-term business service or product that delivers one or more Solutions. An Initiative that has a client function is an Engagement, with one Service Agreement for each client function; the client of enabling work is the Executive Sponsor | Portfolio Backlog |
| Solution | A solution or service that an Initiative delivers for a Domain, with an offering type, a Risk Tier, and an AI Registry entry | The Portfolio, as a Solution Definition |
| Capability | A capability of a Solution, delivered over one or more Program Increments | Program Backlog |
| Feature | A deliverable of an Epic, which closes within one Program Increment | Program Backlog, then IT Backlog |
| Work Item | A task of a Team within a Feature | The Team board |

3.2. AICC keeps three backlogs. The Portfolio Backlog holds the Initiatives. The Program Backlog, also called the PI Backlog, holds the Capabilities and the Features. The IT Backlog holds the Features that the Teams work on in the IT. Each is ranked by value and urgency relative to effort, scored 1 to 5 for value, urgency, risk reduction or opportunity, and effort. The backlogs change continuously, because much of the work depends on people and events outside AICC. An Epic may run over several Program Increments. A Feature closes within its Program Increment. The items of a Program Increment state intent and direction, and what is done in an IT is decided in that IT. Every Initiative is written in a one-page Initiative Brief, which is its business case, and an Initiative that exceeds an Investment Guardrail needs the approval of the Executive Sponsor. A Capability of enabling work may sit directly under an Initiative, without a Solution. Enabling work of AICC that builds no AI Solution has no Risk Tier.

3.3. Work flows as in Kanban. The Portfolio Kanban shows the Initiatives by state. The Program Kanban shows the Capabilites and the Features by state, with the classes of service as lanes: Urgent, High priority, and Normal. The Limits on Work in Progress apply to the states, the lanes, and each Domain. The Team pulls an approved item only when there is capacity. At each IT Planning the Team selects the Features for the month from the Program Backlog into its IT Backlog, and the Weekly Review keeps them under control. An item that waits for a person or an event outside AICC is waiting, and names its Dependency.

3.4. AICC engages a Domain through a Service Agreement, as the Business Model states. The Domain Owner names a Domain Expert, usually the person who does the routine work. The first Solution is narrow. A Solution Engineer, appointed from AICC, the technology function, or the Domain under AICC direction, builds the Solution with the Domain Expert, and the states in section 4.1 follow.

## 4. States and Stages

4.1. Every Initiative, Solution, Epic, and Feature is in one of the states of the Vocabulary. A Strategic Priority is Proposed, Active, Closed, or Cancelled, as the Executive Sponsor decides. An item moves as the following table states. This table is the only source of the moves.

| From | To | When |
| --- | --- | --- |
| Proposed | Discovery | The AICC Lead takes it in: Initiatives, Solutions, and Epics, and Features at refinement |
| Proposed | Rejected, or Deferred | It is decided against at triage, or put on hold |
| Discovery | Approved | The conditions of its level in section 4.2 are met, and its approver decides |
| Discovery | Waiting, Deferred, Rejected, Pivoted, or Cancelled | A Dependency blocks it; it is put on hold; it is decided against; it is rerouted into a new item; or it is no longer needed |
| Approved | Active | The Team pulls it, when there is capacity and its Dependencies are known. An Initiative or a Solution becomes active when its first Epic or Feature is pulled |
| Approved | Waiting, Deferred, Pivoted, or Cancelled | As for Discovery |
| Active | Completed | The work is finished |
| Active | Waiting, Deferred, Pivoted, or Cancelled | As for Discovery |
| Active | Closed | Only for a Solution: it is retired, handed off, or ended, as section 7.1 states |
| Active | Discovery | Only for a Solution: a change raises its Risk Tier or the check or the validation named it as requiring a new check, as the AI Policy states |
| Waiting | The state it came from | The Dependency is cleared |
| Waiting | Deferred or Cancelled | The Dependency will not clear, or the item is no longer needed |
| Deferred | Proposed | It is taken up again, and the keeper may resume it at the state it left |
| Deferred | Rejected or Cancelled | It is decided against, if it was never approved, or it is no longer needed |
| Completed | Review | The product owner assesses it against its acceptance criteria |
| Review | Active, or Accepted, or Cancelled | It is returned with what is missing; its criteria are met; or its outcome is no longer wanted |
| Accepted | Closed | The item is finished |

Rejected means decided against on its merits, and applies only before an item is approved. Cancelled means no longer needed, and applies in any state from Discovery to Review except Completed. A suspension of a Solution is a flag on it, like waiting, and does not change its state. A stop by a Control Function cancels the Solution. Retirement closes it, with no acceptance. The person who approves an item at its level also defers, rejects, cancels, or pivots it.

4.2. A Stage is a phase of the work inside the discovery state or the active state of an item. The Stages, the approver, and the conditions of each level are in the following table. The AICC Lead shall confirm that the conditions are met and note it in the backlog of the level, or in the Portfolio for a Solution.

| Level | Discovery Stages | Approved by, and conditions | Active Stages | To be completed |
| --- | --- | --- | --- | --- |
| Initiative | Scoping, Business case | The Domain Owner, or the Executive Sponsor for an Initiative that spans Domains, and the Executive Sponsor above a guardrail. Until the Guardrails are set, the Executive Sponsor approves any commitment. The scope is agreed, the Initiative Brief is complete in its six sections, and the business case in it is approved | Implementation | Its Solutions are delivered, and its outcome is reviewed |
| Solution | Definition | The Domain Owner approves the Solution Definition, with its type, Receiver, scope, capabilities, architecture, and data classes. The Risk Tier is assigned by the AICC Lead and told to the Domain Owner; the AI Registry entry is made; for Risk Tier 2 and 3, the Control Function Contact of compliance confirms the applicable law; an Experiment has its time-box and a Service its run cost and sunset | Delivery, then the Stages of its type in section 7.1 | It is delivered, as section 7.1 states |
| Epic | Analysis: define the capability and break it into Features | The AICC Lead, with the Domain Owner consulted. Its Features are defined and ranked in the Program Backlog | Implementation | Its Features are closed |
| Feature | Explore, Design | The Team, at IT Planning. Its acceptance criteria are stated, and its Dependencies are known, with any open one named | Develop, Verify, Deploy | It is deployed |

## 5. Cadence

5.1. Work runs in Program Increments. A Program Increment is one quarter, made of three Iterations. An Iteration is one calendar month of four or five whole weeks. The last week of the third Iteration of a Program Increment is the IP week. The Calendar Record states the dates and the blocked and gray days, and the Cadence workflow of the charter states the general flow of the events by week, without dates, which is the template for the dated calendar of events. The events of each loop are listed below. A Team of one holds them short and records them in the IT Backlog.

The events of the delivery loops are the Daily Stand-up, the Weekly Planning, the Weekly Review, the Backlog Refinement, the IT Planning, the IT Review and Demo, the IT Retrospective, the PI Review and Demo, Inspect and Adapt, the PI Planning, and the Innovation. The monthly Steering and the quarterly Steering are the events of the control loop of the Operating Model 6, and they take the results of the IT Review and Demo and of the PI Review and Demo. The Cadence states the intent, the inputs, and the outputs of each.

5.2. An event that falls on a blocked or gray day moves to the working day before it, and never after. When moved events meet on one day, the larger event keeps the day and the smaller one moves to the working day before it. An event that is missed is not held later, and its intent is covered at the next event. The Weekly Review may be held in writing.

5.3. While the AICC Team has up to three people, AICC runs in light mode. The Weekly Planning and the Weekly Review are one session, held on the day of the Weekly Planning. The IT Retrospective and the monthly Steering are held in the IT Review and Demo, and Inspect and Adapt is held in the PI Review and Demo. The Daily Stand-up, the Backlog Refinement, and the Innovation are optional. In light mode Waiting is a flag, Completed is skipped and an item goes from Active to Review, Accepted and Closed are one step with the acceptance recorded, Pivoted is recorded as Cancelled with a link to the new item, Stages are used for Initiatives and Solutions only, and Work Items are not tracked in the charter. Everything else stays as stated.

5.4. The PI Planning proposes the Roadmap, and the quarterly Steering confirms it (Operating Model 6.2). The Roadmap shows three months: the current Program Increment as intent and direction, the next as planned, and the period beyond as indicative, with its Milestones. The Dependency Map shows, for each item of a Program Increment, what it needs from other items, Teams, functions, and persons, and breaks the item into the scope of each month. The Dashboard shows the state of the Program Increment, the flow of the Program Kanban, the Dependencies at risk, the risks, and the Measures. The AICC Lead keeps them current, and they are Records.

## 6. Verification, release, and acceptance

6.1. The check for Risk Tier 1 and the validation by the Control Function Contacts for Risk Tier 2 and 3 attach to the Solution. They are taken in Verify of the first Feature that reaches real users or data, they cover the later Features unless a change requires a new one, and no deployment to real users or data comes before them. The release of a Solution beyond its first users is decided by the Domain Owner for Risk Tier 1 and 2, and by the Executive Sponsor for Risk Tier 3, after the check or the validation, and is recorded in the Solution Definition. A Feature that cannot close within its Program Increment is split: the part that is done is a Feature that goes to review, and the rest is a new Feature in the next Program Increment. The original Feature is Pivoted and linked to both.

6.2. The Control Function Contacts shall take part when a Solution is defined and in validation. Evidence is taken from the records of the AI Platform.

6.3. Acceptance closes an item. The product owner accepts the delivered outcome against its acceptance criteria, and the AICC Lead notes the acceptance with who and when in the backlog of the level. The product owner is the Domain Owner for an item of a Domain, and the Executive Sponsor for an item that spans Domains or is enabling work of AICC. The product owner may accept the item, return it with what is missing, or cancel it when its outcome is no longer wanted. The acceptance of an Engagement is recorded in its Outcome Report.

6.4. When AICC hands a Solution to a Domain as ready for use at scale, before its release beyond the first users, the AICC Lead completes the Acceptance Checklist of the Solution. The checklist lists, for each party concerned, the items that the party confirms within its remit and signs: the Domain Owner, the Solution Engineer, the AICC Lead, the Checker, the Control Functions (model risk, compliance, information security, data protection, and legal), and the IT function that operates the Solution with the Platform Owner. An item that is not met stops the release. The Domain Owner receives the checklist signed and signs the acceptance of the package. A Domain adopts a Solution of Risk Tier 1 or 2 on its own risk, within the AI Risk Appetite Statement. A Solution of Risk Tier 3, which is of high impact and risk, is adopted only with the signature of the Executive Sponsor, who accepts the risk and releases it. The checklist is not used during development or trials, where 6.1 applies, and a change after the release that requires a new check or validation brings a new checklist. It adds no approval of its own: the decisions are those that the AI Policy and this model state.

## 7. Life-cycle management

7.1. A Solution has one offering type, which sets its life after delivery. A Solution is delivered when its first deployment is released. The Initiative is complete once its Solutions are delivered and its outcome is reviewed, and a Service and a Product go on under their own type. A Solution is Active from the start of its delivery to the end of its life, and it is Closed when it is retired, handed off, or ended. The Receiver is named in the Solution Definition before the Solution is approved, and an Experiment may name "none yet, to be asked". The following table states the types.

| Type | Owner after delivery | Stages after delivery | End |
| --- | --- | --- | --- |
| Service | AICC, for the whole life cycle, with a business case that states the run cost and a sunset rule. The product owner is the Domain Owner of the Domain it serves, and the Executive Sponsor for a Service across Domains | Operate, Evolve, Retire. New features come as Epics and Features | Retired, or cancelled |
| Product | The consumer owns the version delivered, and AICC supports it on demand | Handover, Support, Revise (a new version comes through the Portfolio Backlog), Retire for that consumer. A Product with many consumers or recurring requests becomes a Service through a business case | Retired for that consumer |
| Experiment | None yet: it is time-boxed to a stated number of ITs, and ends in a Proposal. Its product owner is the Executive Sponsor when it has no Domain | Trial, Proposal, Handover | At the end of its time-box it goes to review: it is accepted with its lessons and closed, a Proposal is made, or it is cancelled. When a Receiver accepts the Handover, it is closed and AICC oversees the Adopted Solution |

The phases of an Engagement map to the items as follows: the study is the discovery of the Initiative, the proof is the Experiment or the first Features of the Solution, delivery is the active state of the Epics and Features, and support is the life of the Solution after delivery.

7.2. AICC oversees and reports on the Adopted Solutions that others deliver, in the Portfolio, as a Solution Definition marked as an Adopted Solution with its Receiver as owner. It is recorded when others begin to deliver a Solution that AICC proposed or oversees. It uses the states Proposed, Approved, Active, Closed, Rejected, and Cancelled, and records the Risk Tier when it is known. The owners and the Executive Sponsor decide on a Proposal of a Solution, and the Bank decides on a Proposal of the AI adoption strategy. The AI adoption strategy is a series of Proposals that AICC shapes from what it learns.

## Change log

| Revision | Date | Change | Decision |
| --- | --- | --- | --- |
| 1.0 | 2026-10-01 | Created from the Operating Model: the flow of work, the states and Stages, the cadence of the delivery loops, verification, release, acceptance, and the life cycle of a Solution. | DR-2026-040 |
| 1.1 | 2026-10-01 | The Acceptance Checklist at the handover of a ready Solution to a Domain for use at scale; the Executive Sponsor signs for Risk Tier 3. | DR-2026-041 |
