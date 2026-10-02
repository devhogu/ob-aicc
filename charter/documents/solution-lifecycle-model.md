```yaml
id: AICC-ORG-03-EN
title: Solution Lifecycle Model
status: active
revision: 3.1
created: 2026-10-01
revised: 2026-10-02
```

# Solution Lifecycle Model

## 1. Purpose and scope

1.1. This Solution Lifecycle Model states how AICC delivers. It states how the work that the portfolio approves moves through the program and the iteration to a released Solution, and how the Solution is looked after until it is retired. It is the method of the Teams, stated as operating instructions: the principles, the intake, the levels and the backlogs, the states, the cadence with its loops, verification and release, the management of the life cycle, and the measures.

1.2. It applies to AICC and to the Domains and Control Functions of the Bank that work with AICC.

1.3. The Operating Model states how AICC is governed and controlled as a unit, and it prevails. The Portfolio Management Model decides which Initiatives are taken in, funded, and stopped, and it ends where the Capabilities of an Initiative enter the Program Backlog, where this model begins. The workflows of the charter show how the loops run, and the Calendar Record holds the dates. They state no rule of their own. Figures illustrate and state no rule of their own.

## 2. Principles and values

2.1. AICC delivers on the values of the Statement of Intent: integrity, prudence, and respect for people. In delivery they mean working Solutions over documents, collaboration with the function over negotiation, response to change over adherence to a fixed plan, and evidence over opinion.

2.2. AICC delivers on the following principles.

(a) Make work visible, limit work in progress, and pull work when there is capacity.

(b) Deliver in small steps: probe with a minimum viable product, measure against the success Measures, then scale.

(c) Put value first: rank work by value and urgency relative to effort.

(d) Plan on a cadence. Work is paced by Program Increments and Iterations that start and end on fixed dates, and the plan of a Program Increment states intent and direction and not a promise of scope.

(e) Build quality in. The check or the validation and the controls of the AI Policy are steps of the flow, and not a stage after it.

(f) Decide where the facts are. The Team decides how the work is built, the product owner decides whether a Feature or a Capability is accepted during development, and the Domain Owner decides whether the Solution is accepted.

(g) Make dependencies visible, and manage them as work.

(h) Improve continuously. Each Iteration and each Program Increment ends with a review and an improvement.

## 3. The flow of value

3.1. Work enters the program in three ways. The Capabilities of an Initiative enter the Program Backlog after the decision to continue at the end of its MVP (Portfolio Management Model 7.2). A change or a new feature of a released Solution is raised by its Domain Owner or its product owner and enters the Program Backlog under the Capability of that Solution. Enabling work of AICC enters under an Initiative of enabling work. Every item is ranked in the Program Backlog before a Team takes it.

3.2. The work is structured in the levels of the following table. The Strategic Priority and the Initiative are managed by the Portfolio Management Model.

| Level | Meaning | Kept in |
| --- | --- | --- |
| Strategic Priority | A strategic theme set with the Board, with an Investment Envelope | Priorities |
| Initiative | A business program: a long-term business service or product that delivers one or more Solutions. An Initiative that has a client function is an Engagement, with one Service Agreement for each client function; the client of enabling work is the Executive Sponsor | Portfolio Backlog |
| Solution | A solution or service that an Initiative delivers for a Domain, with an offering type, a Risk Tier, and an AI Registry entry | The Portfolio, as a Solution Definition |
| Capability | A capability of a Solution, delivered over one or more Program Increments | Program Backlog |
| Feature | A deliverable of a Capability, which closes within one Program Increment and is delivered over one or more Iterations | Program Backlog, then Iteration Backlog |
| Work Item | A task of a Team within a Feature | The Team board |

Figure 1 shows how the levels follow from one another, with the intent of each level, where it is kept, and who decides.

```mermaid
flowchart LR
  subgraph PORT["Portfolio layer: decided by the business"]
    direction TB
    SP["Strategic Priority<br/>Intent: where AI creates value<br/>Kept in: Priorities<br/>Decides: Executive Sponsor"]
    INI["Initiative<br/>Intent: a business outcome<br/>Backlog: Portfolio Backlog<br/>Decides: Domain Owner or Executive Sponsor"]
    SP -->|funds and directs| INI
  end
  subgraph PROG["Program layer: decided with the product owner"]
    direction TB
    CAP["Capability (Epic in Jira)<br/>Intent: what the Solution can do<br/>Backlog: Program Backlog<br/>Decides: AICC Lead"]
    FT["Feature<br/>Intent: a deliverable the user notices<br/>Backlog: Program, then Iteration<br/>Decides: the Team"]
    CAP -->|broken into| FT
  end
  subgraph ITER["Iteration layer: decided by the Team"]
    direction TB
    WI["Work Item<br/>Intent: a task of the Team<br/>Board: Team board"]
  end
  INI -->|after the decision to continue| CAP
  FT -->|broken into| WI
  INI -.->|delivers| SOL["Solution<br/>what the Domain uses"]
  CAP -.->|builds| SOL
```

Figure 1: the levels of the work, by intent and by backlog.

3.3. Each level is worded as a short contract in the language of the business, so that the client, the Team, and the product owner read the same words. An Initiative and a Capability are worded as a hypothesis, which the work tests. A Feature is worded as a benefit hypothesis with its acceptance criteria. Acceptance criteria are written in the form Given, When, Then. The first of the following tables gives the parts of the wording and what each means, the second gives the wording of each level, and the third illustrates it.

| Part | Meaning | The question it answers |
| --- | --- | --- |
| For | The client or the user | Who is it for? |
| Need | The situation or the job to be done | What problem does it solve? |
| Proposal | The thing that is proposed, and its kind | What is it? |
| Value hypothesis | The benefit that we believe it will bring | Why does it matter? |
| Difference | How it is better than the way things are done now | Why is it better? |
| Leading indicator | An early measure, with its source, baseline, and target | How will we know early that it holds? |
| Scope | The smallest version that tests the hypothesis, and what is out | What is tried first? |
| Acceptance criteria | Given a situation, when an action is taken, then a result that can be observed | How is it accepted, by the product owner for a Feature or a Capability and by the Domain Owner for a Solution? |

| Level | For | Need | Proposal | Value hypothesis | Difference | Leading indicator | Scope | Acceptance criteria |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Initiative | [The client function] | who [need] | the [Initiative] is a [type of Solution] | that [value] | Unlike [the current way], ours [difference] | [Measure, source, baseline, target] | The MVP: [the smallest version, and what is out] | The outcome meets the leading indicators when it is reviewed, and the Domain Owner, or the Executive Sponsor for enabling work, accepts it |
| Capability | [The users of the Solution] | who [need] | the Solution can [capability] | so that [benefit] | | [Measure] | The Features that deliver it | Given [situation], when [action], then [result], for the Capability as a whole |
| Feature | [The user] | | [Feature] | We believe that it will [benefit] | | [Measure] | One Program Increment at most | Given [situation], when [action], then [result that can be observed] |

An illustration of the wording follows. It shows the form and is not a record.

| Level | Wording |
| --- | --- |
| Initiative | For the heads of functions who spend days each month compiling a recurring report by hand, the Reporting Service is a Service that drafts and publishes it. Unlike the manual compilation, ours is consistent and takes hours. We will know by the share of editions issued on time |
| Capability | For the analysts who prepare the report, the Solution can collect the figures from their governed sources, so that no figure is copied by hand |
| Feature | We believe that collecting the first three measures automatically will remove the hand copying of those measures for the analysts. Given a monthly cycle with the sources available, when the collection runs, then the three measures appear in the draft with their source and their date |

3.4. Figure 2 shows the flow of value from the intake to the life cycle of a Solution.

```mermaid
flowchart LR
  IN(["From above<br/>an Initiative continues, or a change is raised"]):::iface --> PB["Program Backlog<br/>Capabilities and Features, ranked"]
  PB --> RF["Refinement<br/>Features ready, acceptance criteria stated"]
  RF --> IB["Iteration Backlog<br/>selected at Iteration Planning"]
  IB --> DV["Develop<br/>Work Items of the Team"]
  DV --> VF["Verify<br/>check or validation"]
  VF --> DP["Deploy<br/>to the environment of use"]
  DP --> AC["Accept the Feature<br/>the product owner"]
  AC --> TF["Team final acceptance<br/>the AICC Lead, before the first users"]
  TF --> FU["First users<br/>the Domain Owner judges and accepts the Solution"]
  FU --> RL["Release<br/>beyond the first users"]
  RL --> LC["Life cycle<br/>operate, evolve, retire"]
  LC -.new Capabilities and Features.-> PB
  AC -.returned.-> IB
  FU -.returned.-> IB
  classDef iface fill:#e8eefc,stroke:#5a6fa8,color:#111
```

Figure 2: the flow of value.

3.5. A Team delivers the work: a Solution Engineer with the Domain Expert, the Domain Owner, and the product owner. While the Team has up to three people (6.6) the AICC Lead is the product owner of the Team, and later the AICC Lead may name another person in the Appointments Record. AICC has the AICC Team, and a Domain may have its own Team. The AICC Lead ranks the Program Backlog. The Team pulls the Features in the order that the Solution Engineer decides within that ranking, decides how they are built, keeps the Iteration Backlog and the Team board current, and holds the events of the Iteration. The product owner states the value of an item and accepts the Features and the Capabilities during development, and the Domain Owner accepts the Solution (7.3). The Team agrees who takes the Hats that the work needs (Operating Model 4.3).

## 4. Backlogs and boards

4.1. AICC keeps two backlogs at this level. The Program Backlog, also called the PI Backlog, holds the Capabilities and the Features, grouped under their Initiatives. The Iteration Backlog holds the Features that the Teams work on in the Iteration. Each is ranked by value and urgency relative to effort, scored 1 to 5 for value, urgency, risk reduction or opportunity, and effort. The AICC Lead ranks the Program Backlog, and the product owner states the value. The backlogs change continuously, because much of the work depends on people and events outside AICC. A Capability may run over several Program Increments. A Feature closes within its Program Increment, or is split: the part that is done is a Feature that goes to review, and the rest is a new Feature in the next Program Increment, and the original Feature is Pivoted and linked to both. The items of a Program Increment state intent and direction, and what is done in an Iteration is decided in that Iteration.

4.2. Work flows as in Kanban. The Program Kanban shows the Capabilities and the Features by state, with the classes of service as lanes: Urgent, High priority, and Normal. The Limits on Work in Progress apply to the states, the lanes, and each Domain. The Team pulls an approved item only when there is capacity, and a Feature is approved only when its Dependencies are known. At each Iteration Planning the Team selects the Features for the month from the Program Backlog into its Iteration Backlog, and the Weekly Review keeps them under control. An item that waits for a person or an event outside AICC is Waiting, and names its Dependency. The columns of the Program Kanban are the states: Backlog is Proposed and Discovery, Ready is Approved, Active is Active and Completed, Review is Review, and Done is Accepted and Closed. The Team board shows the Work Items of the Iteration.

The following table outlines the boards, their steps, their lanes, their limits, and the measures that are read from them.

| Board | Shows | Columns | Stages shown | Lanes | Limit on Work in Progress | Measures |
| --- | --- | --- | --- | --- | --- | --- |
| Portfolio Kanban | Initiatives | Funnel, Reviewing, Analyzing, Portfolio Backlog, MVP, Implementation, Done; Deferred, Rejected, and Pivoted are off the flow | Scoping, Business case, MVP, Implementation | None | The Initiatives that are Active, set by the AICC Lead | Time from a proposal to its approval, time from approval to acceptance, Active against the limit |
| Program Kanban | Capabilities and Features | Backlog, Ready, Active, Review, Done; Waiting is a state, shown as a flag on the boards, with its Dependency | Capability: Analysis, Implementation. Feature: Explore, Design, Develop, Verify, Deploy | Urgent, High priority, Normal | Per state, per lane, and per Domain, set by the Team | Features accepted in the Iteration, lead time from Approved to Accepted, cycle time, items by lane, Waiting items |
| Team board | Work Items of the Iteration | Backlog, Ready, Active, Review, Done | The Stages of the Feature | None | Per person, set by the Team | Work Items closed, blockers |

4.3. The Program Board is the board of the dependencies of a Program Increment. It shows, for each Capability and Feature, the Iteration in which it is planned, its state, and what it needs from other items, Teams, functions, and persons. It also shows the Milestones of the Roadmap at the Iteration in which they fall. The AICC Lead builds it with the Teams at the PI Planning, and keeps it current at the Weekly Review. A Dependency is Open, Met, or At risk. A Milestone is At risk when a Feature or a Dependency that it needs is At risk, and what is At risk is raised to the monthly Steering. Figure 3 shows how the Program Board, its Dependencies, and the Milestones flow through a Program Increment, and the following table shows the form of the Program Board.

```mermaid
flowchart LR
  PL["PI Planning<br/>Features placed by Iteration, Dependencies entered, Milestones taken from the Roadmap"] --> PBD["Program Board<br/>lanes of Features, states, Dependencies, Milestones"]
  PBD --> WR["Weekly Review<br/>states and Dependencies updated"]
  WR --> MC{"Milestone and Dependencies on track?"}
  MC -->|yes| PBD
  MC -->|at risk| ST["Monthly Steering<br/>re-plan, unblock, or defer"]
  ST --> PBD
  PBD --> PR["PI Review and Demo<br/>Features done, Milestones met or missed"]
  PR --> RM["Roadmap updated<br/>Inspect and Adapt"]
  RM --> PL
```

Figure 3: the Program Board through a Program Increment.

| Lane: Feature | Capability | Iteration 1 | Iteration 2 | Iteration 3 | IP week | Depends on | Dependency status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Milestone | The Roadmap | [Milestone and date] | | [Milestone and date] | | | |
| [Feature A] | [Capability X] | Active | Review | Done | | None | |
| [Feature B] | [Capability X] | Approved | Active | Review | Done | [Feature A] | Met |
| [Feature C] | [Capability Y] | Waiting | Active | Review | | [A function, a person, or another Team] | At risk |
| [Feature D] | [Capability Y] | | Approved | Active | Review | [Feature C] | Open |

The table is the form and holds no real data. A lane is one Feature, and a cell holds the state that the Feature is planned to reach, or has reached, in that Iteration. A Feature that is Waiting names its Dependency, and a Dependency that is At risk is raised to the monthly Steering.

4.4. The Roadmap shows three horizons: the current Program Increment as intent and direction, the next as planned, and the period beyond as indicative, with its Milestones. The PI Planning proposes it, and the quarterly Steering confirms it (Portfolio Management Model 4.3). The Dashboard shows the state of the Program Increment, the flow of the Program Kanban, the Dependencies at risk, the risks, and the Measures. The AICC Lead keeps the Roadmap, the Program Board, and the Dashboard current, and they are Records.

## 5. States and Stages

5.1. Every Initiative, Solution, Capability, and Feature is in one of the states of the Vocabulary. A Strategic Priority is Proposed, Active, Closed, or Cancelled, as the Executive Sponsor decides. An item moves as the following table states. This table is the only source of the moves.

| From | To | When |
| --- | --- | --- |
| Proposed | Discovery | The AICC Lead takes it in: Initiatives, Solutions, and Capabilities, and Features at refinement |
| Proposed | Rejected, or Deferred | It is decided against at triage, or put on hold |
| Proposed | Cancelled | It is withdrawn without a decision on the merits |
| Discovery | Approved | The conditions of its level in section 5.2 are met, and its approver decides |
| Discovery | Waiting, Deferred, Rejected, Pivoted, or Cancelled | A Dependency blocks it; it is put on hold; it is decided against; it is rerouted into a new item; or it is withdrawn without a decision on the merits |
| Approved | Active | The Team pulls it, when there is capacity and its Dependencies are known. An Initiative becomes active when the AICC Lead pulls it into its MVP (Portfolio Management Model 5.2). A Solution becomes active when its first Capability or Feature is pulled |
| Approved | Waiting, Deferred, Pivoted, or Cancelled | As for Discovery |
| Active | Completed | The work is finished |
| Active | Waiting, Deferred, Pivoted, or Cancelled | As for Discovery |
| Active | Rejected | Only for an Initiative at the end of its MVP: the value is not seen (Portfolio Management Model 7.2) |
| Active | Closed | Only for a Solution: it is retired, handed off, or ended, as section 8.1 states |
| Active | Discovery | Only for a Solution: a change raises its Risk Tier or the check or the validation named it as requiring a new check, as the AI Policy states |
| Waiting | The state it came from | The Dependency is cleared |
| Waiting | Deferred or Cancelled | The Dependency will not clear, or the item is withdrawn without a decision on the merits |
| Deferred | Proposed | It is taken up again, and the keeper may resume it at the state it left |
| Deferred | Rejected or Cancelled | It is decided against, if it was never approved, or it is withdrawn without a decision on the merits |
| Completed | Review | The product owner assesses a Feature or a Capability against its acceptance criteria, and the Domain Owner, or the Executive Sponsor for enabling work, assesses the outcome of an Initiative against its criteria (7.3) |
| Review | Active, or Accepted, or Rejected | It is returned with what is missing; its criteria are met; or its outcome is not wanted |
| Review | Cancelled | It is withdrawn without a decision on the merits |
| Accepted | Closed | The item is finished |

5.2. A Stage is a phase of the work inside the discovery state or the active state of an item. The Stages of an Initiative are in the Portfolio Management Model 5.2. The Stages, the approver, and the conditions of each level are in the following table. The AICC Lead shall confirm that the conditions are met and note it in the backlog of the level, or in the Portfolio for a Solution.

| Level | Discovery Stages | Approved by, and conditions | Active Stages | To be completed |
| --- | --- | --- | --- | --- |
| Solution | Definition | The Domain Owner approves the Solution Definition, with its type, Receiver, scope, capabilities, architecture, and data classes. The Risk Tier is assigned by the AICC Lead and told to the Domain Owner; the AI Registry entry is made; for Risk Tier 2 and 3, the Control Function Contact of compliance confirms the applicable law; an Experiment has its time-box and a Service its run cost and sunset; for a Solution that the AICC Lead built, the Executive Sponsor approves the Solution Definition and assigns the Risk Tier (Operating Model 4.4) | Delivery, then the Stages of its type in section 8.1 | It is delivered, as section 8.1 states |
| Capability | Analysis: define the capability and break it into Features | The AICC Lead, with the Domain Owner consulted. Its Features are defined and ranked in the Program Backlog | Implementation | Its Features are closed |
| Feature | Explore, Design | The Team, at Iteration Planning. Its acceptance criteria are stated, and its Dependencies are known, with any open one named | Develop, Verify, Deploy | It is deployed |

Figure 4 shows the staging workflow of each level, from left to right: the Stages in boxes, the conditions that must be met to move on in diamonds, and the returns. Each condition is a condition of the Stages table, and in the tracker it is a condition of the workflow, with the Stage held in a field and the state in the status.

```mermaid
flowchart TB
  subgraph FEATURE["Feature"]
    direction LR
    F0(["Proposed"]) --> F1["Explore"] --> F2["Design"] --> FC1{"Acceptance criteria stated, Dependencies known?"}
    FC1 -->|yes| F3(["Approved"]) --> F4["Develop"] --> F5["Verify"] --> FC2{"Check or validation met?"}
    FC2 -->|yes| F6["Deploy"] --> F7(["Completed"]) --> F8(["Review"]) --> FC3{"Criteria met?"}
    FC3 -->|yes| F9(["Accepted, then Closed"])
    FC3 -->|returned| F4
    FC3 -->|not wanted| F10(["Rejected"])
    FC2 -->|no| F4
    FC1 -->|no| F11(["Waiting or Deferred"])
  end
  subgraph CAPABILITY["Capability"]
    direction LR
    C0(["Proposed"]) --> C1["Analysis"] --> CC1{"Features defined and ranked, AICC Lead approves?"}
    CC1 -->|yes| C2(["Approved"]) --> C3["Implementation"] --> CC2{"All Features closed?"}
    CC2 -->|yes| C4(["Completed"]) --> C5(["Review"]) --> C6(["Accepted, then Closed"])
    CC1 -->|no| C7(["Deferred or Rejected"])
  end
  subgraph SOLUTION["Solution"]
    direction LR
    S0(["Proposed"]) --> S1["Definition"] --> SC1{"Domain Owner approves, Risk Tier assigned, AI Registry entry made?"}
    SC1 -->|yes| S2(["Approved"]) --> S3["Delivery"] --> SC2{"Team final acceptance given, Domain Owner accepts, first deployment released?"}
    SC2 -->|yes| S4["Stages of its type: operate, evolve, retire"] --> S5(["Closed"])
    SC1 -->|no| S6(["Deferred or Rejected"])
  end
  FEATURE ~~~ CAPABILITY
  CAPABILITY ~~~ SOLUTION
```

Figure 4: the staging workflow of the Feature, the Capability, and the Solution.

5.3. Rejected means decided against on the merits because the value is not seen, before approval or after the MVP of an Initiative, or when the outcome under review is not wanted. Cancelled means withdrawn without a decision on the merits, such as an error, a mistake, or a duplicate, and applies in any state from Proposed to Review except Completed. A suspension of a Solution is a flag on it and does not change its state. A stop by a Control Function is final and cancels the Solution. Retirement closes it, with no acceptance. The person who approves an item at its level also defers, rejects, cancels, or pivots it.

## 6. The cadence

6.1. Work runs in Program Increments. A Program Increment is one quarter, made of three Iterations. An Iteration is one calendar month of four or five whole weeks. The last week of the third Iteration of a Program Increment is the IP week, except that the Calendar Record may place it earlier and keep a year-end week free of events, as in an I12 of five weeks whose last week is the year-end week. The names are PIQ1 to PIQ4 with the year, I01 to I12, and W1 to W5. The Calendar Record states the dates of the whole year with the blocked and gray days, and the Cadence workflow states the general flow of the events by week, without dates, which is the template for the dated calendar of events. The work runs on four loops, each starting with planning and ending with review, and each loop takes its frame from the loop above it and returns its evidence to it. The following table states them.

| Loop | Cadence | Events | Decider | Records |
| --- | --- | --- | --- | --- |
| Program Increment | Quarterly | PI Planning, PI Review and Demo, Inspect and Adapt, Innovation | The Teams and the Domain Owners for the intent; the Executive Sponsor confirms the Roadmap | PI Objectives, Roadmap, Program Board, Quarterly Report |
| Iteration | Monthly | Iteration Planning, Iteration Review and Demo, Iteration Retrospective, Backlog Refinement | The Team; the product owner accepts the Features and the Capabilities | Iteration Backlog, acceptances |
| Week | Weekly | Weekly Planning, Weekly Review | The AICC Lead | Dashboard, Program Board |
| Day | Daily | Daily Stand-up | The Team | The work items |

6.2. The Program Increment loop is the loop of the quarter. The PI Planning sets the intent and the direction of the Program Increment: the PI Objectives, the Features that the Program Increment aims at, the Program Board, and the proposed Roadmap. The three Iterations carry the work out. The PI Review and Demo shows what the Program Increment delivered and scores its value against the PI Objectives. Inspect and Adapt solves the main problems of the Program Increment, and the Innovation gives time to learn and recover. The IP week holds the PI Review and Demo, Inspect and Adapt, Innovation, and PI Planning in that order, and the quarterly Steering that ends the week confirms the PI Objectives and the Roadmap that the PI Planning proposed. The quarterly Steering that ends the IP week of PIQ4 does the same, and carries only the assurance loop and the portfolio review, because the yearly Steering of December has set the frame of the next year. The loop takes the Roadmap and the priorities of the portfolio review and the direction of the yearly Steering, hands the PI Objectives and the Program Board down to the Iteration loop, and returns the value scored and the data of the Quarterly Report to the quarterly Steering.

```mermaid
flowchart LR
  IN(["From above<br/>Roadmap, priorities, and the frame of the quarterly Steering"]):::iface --> P
  P["Plan<br/>PI Planning: PI Objectives, Features, Program Board, proposed Roadmap"] --> D["Do<br/>three Iterations"] --> C["Check<br/>PI Review and Demo: value scored against the PI Objectives"] --> A["Act<br/>Inspect and Adapt, Innovation, then the next PI Planning"] --> P
  P --> OUT(["To below<br/>PI Objectives and Program Board"]):::iface
  EV(["From below<br/>results of the Iterations"]):::iface --> C
  C --> UP(["To above<br/>value scored and data for the Quarterly Report"]):::iface
  classDef iface fill:#e8eefc,stroke:#5a6fa8,color:#111
```

Figure 5: the Program Increment loop.

6.3. The Iteration loop is the loop of the month. The Iteration Planning selects the Features for the month into the Iteration Backlog and sets the Iteration goal. The weeks carry the work out. The Iteration Review and Demo shows the working Features and Solutions to the product owner and takes the acceptance of the Features and the Capabilities, and the Iteration Retrospective improves the way the Team works. The Backlog Refinement keeps the next items ready, within the weekly sessions. The last week of an Iteration is its review week, except in the third Iteration of a Program Increment, where the IP week holds the review. The loop takes the PI Objectives and the Program Board, and returns the acceptances and the results to the Program Increment loop and to the monthly Steering.

```mermaid
flowchart LR
  IN(["From above<br/>PI Objectives, Program Board, Program Backlog"]):::iface --> P
  P["Plan<br/>Iteration Planning: Features into the Iteration Backlog, Iteration goal"] --> D["Do<br/>the weeks of the Iteration"] --> C["Check<br/>Iteration Review and Demo: acceptance of the Features by the product owner"] --> A["Act<br/>Iteration Retrospective: improve the way of working"] --> P
  EV(["From below<br/>Weekly Reviews and the Dashboard"]):::iface --> C
  C --> UP(["To above<br/>acceptances and results to the PI loop and the monthly Steering"]):::iface
  classDef iface fill:#e8eefc,stroke:#5a6fa8,color:#111
```

Figure 6: the Iteration loop.

6.4. The week loop and the day loop are the loops of the work. The Weekly Planning sets the focus of the week and checks the Dependencies. The Weekly Review controls the flow. It reads the Program Kanban, the Limits on Work in Progress, and the Dependencies. The AICC Lead reorders the Program Backlog and keeps the Dashboard current. The Daily Stand-up shares progress and clears blockers. The loop takes the Iteration Backlog and the Iteration goal, and returns the Dashboard and the open Dependencies to the Iteration loop.

```mermaid
flowchart LR
  IN(["From above<br/>Iteration Backlog and Iteration goal"]):::iface --> P
  P["Plan<br/>Weekly Planning: focus of the week, Dependencies"] --> D["Do<br/>the Team works, Daily Stand-up each day"] --> C["Check<br/>Weekly Review: flow, limits, Dependencies, Dashboard"] --> A["Act<br/>reorder the backlog, raise what cannot be settled"] --> P
  C --> UP(["To above<br/>Dashboard and open Dependencies"]):::iface
  classDef iface fill:#e8eefc,stroke:#5a6fa8,color:#111
```

Figure 7: the week loop.

6.5. An event that falls on a blocked or gray day moves to the working day before it, and never after. When moved events meet on one day, the larger event keeps the day and the smaller one moves to the working day before it. Innovation is optional and is dropped first when days are lost. An event that is missed is not held later, and its intent is covered at the next event. The Weekly Review may be held in writing.

6.6. While the AICC Team has up to three people, AICC runs in light mode. The Weekly Planning and the Weekly Review are one session, held on the day of the Weekly Planning. The Iteration Retrospective and the monthly Steering are held in the Iteration Review and Demo, and Inspect and Adapt is held in the PI Review and Demo. The Daily Stand-up, the Backlog Refinement, and the Innovation are optional. In light mode Waiting stays a state, shown as a flag on the boards, Completed is skipped and an item goes from Active to Review, Accepted and Closed are one step with the acceptance recorded, Stages are used for Initiatives and Solutions only, and Work Items are not tracked in the charter. The AICC Lead is the product owner of the Team (3.5, 7.3). Everything else stays as stated.

6.7. The loops of this model run on the events that the control loops of the Operating Model 6 and the portfolio loops of the Portfolio Management Model 4 also use, and add no meeting. The Weekly Review is the operating loop and the backlog care loop, the monthly Steering takes the results of the Iteration Review and Demo, and the quarterly Steering takes the results of the PI Review and Demo. In the month that holds the IP week the quarterly Steering that ends the IP week is also the Steering of that month, and it carries the monthly control loop. The exception is December: the monthly Steering of December is held in the first two weeks as the yearly Steering (Operating Model 6.5), and the quarterly Steering that ends the IP week carries only the assurance loop and the portfolio review.

## 7. Verification, release, and acceptance

Figure 8 shows how a Feature is verified, deployed, and accepted by the product owner, and how a Solution passes the final acceptance of the Team and the judgment of the Domain Owner before it is released beyond its first users.

```mermaid
flowchart LR
  F["Feature developed"] --> V{"Verify<br/>tested by another person; the check or validation of the Solution is in place"}
  V -->|not met| FD["Returned to develop"]
  V -->|met| D["Deploy<br/>change management of the Bank<br/>to the environment of use"]
  D --> A{"Review<br/>the product owner accepts the Feature<br/>at the Iteration Review and Demo"}
  A -->|returned| FD
  A -->|rejected| RJ["Rejected"]
  A -->|accepted| OK["Feature accepted"]
  OK --> TF{"Team final acceptance<br/>the AICC Lead, for the Solution"}
  TF -->|not met| FD
  TF -->|accepted| FU["Deployed to the first users<br/>change management of the Bank"]
  FU --> DJ{"Business acceptance<br/>the Domain Owner, or the Executive Sponsor,<br/>judges the Solution against its criteria"}
  DJ -->|returned| FD
  DJ -->|rejected| RJ2["Solution rejected"]
  DJ -->|accepted| R{"Release of the Solution<br/>beyond the first users<br/>Acceptance Checklist signed"}
  R -->|not met| FU
  R -->|met| LC["Released, then life cycle"]
```

Figure 8: verification, deployment, the three levels of acceptance, and release.

7.1. Every Feature, and the MVP of an Initiative, shall be tested by a person other than its builder in an environment that is not production before it is deployed, and the result is referenced in the Feature. The check for Risk Tier 1 and the validation by the Control Function Contacts for Risk Tier 2 and 3 attach to the Solution. They are taken in Verify of the first Feature that reaches real users or data, they cover the later Features unless a change requires a new one, which the AICC Lead shall decide and enter, with the reason, in the Solution Definition, and no deployment to real users or data comes before them.

A deployment to production is made under 8.3, and the access of a Solution Engineer to production is granted through the access process of the Bank. The first users are the users whom the Domain Owner names in the Solution Definition for the judgment of the Solution (7.3), and they shall be trained before use (AI Policy 2.1). The Team's final acceptance (7.3) comes before the first deployment of a Solution to its first users and before the deployment of each significant change (8.6). The release of a Solution beyond its first users is decided by the Domain Owner for Risk Tier 1 and 2 (the Executive Sponsor where the AICC Lead is the Domain Owner, Operating Model 4.4(d)), and by the Executive Sponsor for Risk Tier 3, after the check or the validation and the acceptance of the Solution (7.3), and is recorded in the release block of the Solution Definition. The Acceptance Checklist (7.4) is the record of every release beyond the first users, for a Service and a Product as for any Solution that AICC hands to a Domain.

7.2. The Control Function Contacts that this model and the AI Policy name shall take part when a Solution of Risk Tier 2 or 3 is defined and in its validation. The validation relies on the evidence, the logs, and the traces that the Platform Owner keeps.

7.3. Acceptance closes an item. It is given at three levels, each against the acceptance criteria and each noted with who and when.

(a) During development the product owner accepts each Feature and each Capability against its acceptance criteria, at the Iteration Review and Demo. The product owner may accept the item, return it with what is missing, or reject it when its outcome is not wanted, and the AICC Lead notes the acceptance in the backlog of the level. While the Team has up to three people (6.6) the AICC Lead is the product owner of the Team, and later the AICC Lead may name another person in the Appointments Record.

(b) Before a Solution, whether its working prototype or its final version, is provided and deployed to the Domain Owner for judgment, the AICC Lead shall give the final acceptance of the Team. The AICC Lead shall confirm that the Solution meets the acceptance criteria of its Solution Definition, that its tests are referenced (7.1), and that its check or validation is in place, and shall record who gave the acceptance and the date in the release block of the Solution Definition. It comes before the first deployment of the Solution to its first users and before the deployment of each significant change (8.6).

(c) The requester judges the working Solution deployed to its first users against the acceptance criteria in the Solution Definition, and shall accept it, return it with what is missing, or reject it when its outcome is not wanted. The requester is the Domain Owner for a Solution of a Domain, and the Executive Sponsor for an item that spans Domains, is enabling work of AICC, or is an Experiment that has no Domain. The decision is the acceptance of the Solution and, for an Engagement, of its Outcome Report, which records it, and it is entered in the release block of the Solution Definition with who decided and the date. The release beyond the first users is a separate decision (7.1, 7.4).

(d) The AICC Lead may give the acceptance of (a) and (b) for a Solution that the AICC Lead built, and shall not give the acceptance of (c), check or validate it, or release it (Operating Model 4.4(d)). This is an accepted limit while the Team is small, and it is recorded in the Risks and Issues. The controls that compensate for it are the test by a person other than the builder (7.1), the check or the validation by another person, the acceptance of the Domain Owner, the release decision, and the monthly sample of the Decisions of the AICC Lead by the Executive Sponsor.

7.4. When AICC hands a Solution to a Domain as ready for use at scale, before its release beyond the first users, the AICC Lead completes the Acceptance Checklist of the Solution. The checklist lists, for each party concerned, the items that the party confirms within its remit and signs: the Domain Owner, the Solution Engineer, the AICC Lead, the Checker, the Control Functions (model risk, compliance, information security, data protection, and legal), and the IT function that operates the Solution with the Platform Owner. For Risk Tier 1 the signatories are the Domain Owner, the Solution Engineer, and the Checker, and for Risk Tier 2 and 3 they also include the Control Functions of each remit concerned and the IT function (AI Policy 3.3). An item that is not met shall stop the release. The Domain Owner, who has accepted the Solution (7.3(c)), receives the checklist signed. A Domain adopts a Solution of Risk Tier 1 or 2 on its own risk, within the AI Risk Appetite Statement. A Solution of Risk Tier 3, which is of high impact and risk, is adopted only with the signature of the Executive Sponsor, who accepts the risk and releases it. The checklist is not used during development or trials, where 7.1 applies, and a change after the release that requires a new check or validation brings a new checklist. It adds no approval of its own: the decisions are those that the AI Policy and this model state.

## 8. Life-cycle management

8.1. A Solution has one offering type, which sets its life after delivery. A Solution is delivered when its first deployment is released. The Initiative is complete once its Solutions are delivered and its outcome is reviewed, and a Service and a Product go on under their own type. A Solution is Active from the start of its delivery to the end of its life, and it is Closed when it is retired, handed off, or ended. The Receiver is named in the Solution Definition before the Solution is approved, and an Experiment may name "none yet, to be asked". The following table states the types.

| Type | Owner after delivery | Stages after delivery | End |
| --- | --- | --- | --- |
| Service | AICC, for the whole life cycle, with a business case that states the run cost and a sunset rule. The Domain Owner of the Domain it serves accepts and reviews it, and the Executive Sponsor does for a Service across Domains | Operate, Evolve, Retire. New features come as Capabilities and Features | Retired, or cancelled |
| Product | The consumer owns the version delivered, and AICC supports it on demand | Handover, Support, Revise (a new version comes through the Portfolio Backlog), Retire for that consumer. A Product with many consumers or recurring requests becomes a Service through a business case | Retired for that consumer |
| Experiment | None yet: it is time-boxed to a stated number of Iterations, and ends in a Proposal. The Executive Sponsor accepts it when it has no Domain, and otherwise the Domain Owner does | Trial, Proposal, Handover | At the end of its time-box it goes to review: it is accepted with its lessons and closed, a Proposal is made, or it is rejected. When a Receiver accepts the Handover, it is closed and AICC oversees the Adopted Solution |

The phases of an Engagement map to the items as follows: the study is the discovery of the Initiative, the proof is the Experiment or the first Features of the Solution, delivery is the active state of the Capabilities and Features, and support is the life of the Solution after delivery.

Figure 9 shows the life of a Solution by type, as the Stages in sequence, with the exits.

```mermaid
flowchart TB
  subgraph SERVICE["Service: AICC runs it for its whole life"]
    direction LR
    V0(["Released"]) --> V1["Operate"] --> V2["Evolve"] --> VC{"Still worth running?"}
    VC -->|yes| V1
    VC -->|no, the sunset rule| V3["Retire"] --> V4(["Closed"])
  end
  subgraph PRODUCT["Product: built for one consumer"]
    direction LR
    P0(["Released"]) --> P1["Handover"] --> P2["Support on demand"] --> PC{"A new version needed?"}
    PC -->|yes, through the Portfolio Backlog| P3["Revise"] --> P2
    PC -->|no longer used| P4["Retire for the consumer"] --> P5(["Closed"])
  end
  subgraph EXPERIMENT["Experiment: time-boxed, no consumer yet"]
    direction LR
    E0(["Active"]) --> E1["Trial"] --> E2["Proposal"] --> EC{"A Receiver accepts the Handover?"}
    EC -->|yes| E3["Handover"] --> E4(["Closed, AICC oversees the Adopted Solution"])
    EC -->|no| E5(["Closed with its lessons, or rejected"])
  end
  SERVICE ~~~ PRODUCT
  PRODUCT ~~~ EXPERIMENT
```

Figure 9: the life of a Solution by type.

8.2. AICC oversees and reports on the Adopted Solutions that others deliver, in the Portfolio, as a Solution Definition marked as an Adopted Solution with its Receiver as owner. It is recorded when others begin to deliver a Solution that AICC proposed or oversees. It uses the states Proposed, Approved, Active, Closed, Rejected, and Cancelled, and records the Risk Tier when it is known. The owners and the Executive Sponsor decide on a Proposal of a Solution, and the Bank decides on a Proposal of the AI adoption strategy. The AI adoption strategy is a series of Proposals that AICC shapes from what it learns, and the AICC Lead prepares its yearly Proposal and the Executive Sponsor presents it (Operating Model 6.5). The AICC Lead reviews the Adopted Solutions at each quarterly Steering, and the Quarterly Report records the review (C-20).

### Deployment

8.3. A Feature is deployed after its check or validation (7.1). A deployment to production follows the change management of the Bank. The Solution Engineer shall raise the change in it, enter the change ticket and the test result in the Feature, and deploy through the access process of the Bank. For the first deployment of a Solution the key of the change ticket and the reference of the test are also entered in the release block of the Solution Definition. The Platform Owner provides the logging and the monitoring (AI Policy 3.5). If a deployment fails or does harm, it is rolled back as the change management of the Bank requires, and the event is handled as an incident. A deployment to production makes the Feature available to its first users, after the Team's final acceptance where 7.3(b) requires it, and the release beyond them is decided under 7.4. Figure 10 shows the flow.

```mermaid
flowchart LR
  VF(["Verified<br/>check or validation met"]):::iface --> CR["Change raised<br/>in the change management of the Bank"]
  CR --> TK["Change ticket and test result<br/>entered in the Feature"]
  TK --> AP{"Approved by the<br/>change management?"}
  AP -->|no| CR
  AP -->|yes| DP["Deploy to production<br/>through the access process of the Bank"]
  DP --> CF{"Logging and monitoring on,<br/>Feature works?"}
  CF -->|yes| FU(["Deployed to the first users<br/>release decided under 7.4"]):::iface
  CF -->|no| RB["Roll back<br/>handled as an incident"]
  RB --> CR
  classDef iface fill:#e8eefc,stroke:#5a6fa8,color:#111
```

Figure 10: the deployment of a Feature.

### Operation

8.4. The IT function that operates a Solution runs it (AI Policy 5.3). For a Service that AICC runs, the Solution Engineer acts as that function. The operation is a loop. The plan sets the support level of the Service Agreement and the monitoring at the release. The do runs the Solution, answers the requests, and handles the incidents. The check is the review by the Domain Owner, or by the Executive Sponsor for a Service across Domains, of the monitoring, the incidents, the use, and the notices of the providers at each Iteration Review and Demo, which the reviewer shall note in the Solution Definition. The act fixes, changes (8.6), or retires (8.7) the Solution. The loop takes the support level and the release, returns the review to the Iteration loop, and passes an AI Incident to the event loop of the Operating Model 6. The change management of the Bank approves each production change of a Service that AICC runs, and the monitoring of the Platform Owner and the review of the Domain Owner are its independent checks. Backup and recovery are those of the AI Platform and of the Bank, and are named in the Solution Definition.

```mermaid
flowchart LR
  IN(["From above<br/>support level of the Service Agreement, the release"]):::iface --> P
  P["Plan<br/>support level, monitoring, Limits"] --> D["Do<br/>run the Solution, answer requests, handle incidents"] --> C["Check<br/>review at each Iteration Review and Demo: monitoring, incidents, use, provider notices"] --> A["Act<br/>fix, change, or retire"] --> P
  D --> EV(["To above<br/>an AI Incident to the event loop of the Operating Model"]):::iface
  C --> UP(["To above<br/>the review noted in the Solution Definition"]):::iface
  classDef iface fill:#e8eefc,stroke:#5a6fa8,color:#111
```

Figure 11: the operating loop of a live Solution.

8.5. Requests and incidents about a Solution come to the queue of AICC in Service Management, and the response targets of the Service Agreement are targets and not guarantees. A request is triaged by its class of service (Urgent, High priority, or Normal), handled, and closed. Every outage or failure of a Solution is raised in the incident management of the Bank, and an AI Incident is handled there, with the AICC Lead as a stakeholder (AI Policy 5). A request for a new feature enters the Program Backlog. A Product is supported on demand, and a Service at the agreed response targets. Figure 12 shows the flow.

```mermaid
flowchart LR
  RQ(["A request or an incident<br/>arrives in Service Management"]):::iface --> TR["Triage<br/>kind and class of service"]
  TR --> K{"Kind?"}
  K -->|AI Incident| IM["Incident management of the Bank<br/>the AICC Lead is a stakeholder"]
  K -->|question or fault| HD["Handled<br/>answered or fixed"]
  K -->|new feature| PB["Program Backlog<br/>ranked with the other items"]
  HD --> CL["Closed and recorded<br/>the ticket"]
  IM --> CL
  PB --> CL
  CL -.counted in the review at the Iteration Review and Demo.-> RV(["Review of the live Solution"]):::iface
  classDef iface fill:#e8eefc,stroke:#5a6fa8,color:#111
```

Figure 12: the support of a live Solution.

### Change and retirement

8.6. A change to a released Solution is a Feature, and it is verified and deployed as any Feature is. A change of model, provider, data class, degree of autonomy, or any attribute of the Risk Tier is significant. The AICC Lead shall decide whether a change requires a new check or validation, and shall enter the decision in the Decision Log. A significant change is released as 7.1 states, by the Domain Owner, or by the Executive Sponsor for Risk Tier 3, and any other change is accepted as a Feature. An emergency change follows the emergency procedure of the change management of the Bank (8.3), and the AICC Lead authorizes it for AICC. The Executive Sponsor reviews it within five working days and it is entered in the Decision Log, and for Risk Tier 3 the Control Function Contacts are told. A change of terms or of model by a provider is a change under this clause. Figure 13 shows the loop of a change.

```mermaid
flowchart LR
  RS(["Raised<br/>by the Domain Owner, the product owner, a provider, or an incident"]):::iface --> CLS{"Significant?<br/>model, provider, data class, autonomy, Risk Tier"}
  CLS -->|no| FT["A Feature<br/>in the Program Backlog"]
  CLS -->|yes| DC["The AICC Lead decides<br/>whether a new check or validation is needed"]
  DC --> FT
  FT --> BV["Build and verify<br/>as for any Feature"]
  BV --> DPL["Deploy under 8.3"]
  DPL --> RLS{"Significant?<br/>release as 7.1, otherwise accepted as a Feature"}
  RLS -->|done| NT["Noted in the Solution Definition<br/>and the AI Registry"]
  EM(["Emergency change"]):::iface -.emergency procedure of the Bank, the Executive Sponsor reviews within five working days.-> DPL
  classDef iface fill:#e8eefc,stroke:#5a6fa8,color:#111
```

Figure 13: the loop of a change to a released Solution.

8.7. Before a Solution is Closed as retired, the Solution Engineer shall remove the access and the credentials, the data and the logs shall be kept or deleted under the retention rules of the Bank, and the AI Registry entry shall be marked retired. The Domain Owner, or the Executive Sponsor for a Service across Domains, approves the retirement, and the approval is entered in the Solution Definition. The same steps apply before a Solution that had real users or data is Cancelled, and the Solution Engineer enters in the Solution Definition the date on which the access was removed and the data was handled.

## 9. Records and controls

9.1. The records of this model are the Program Backlog, the Iteration Backlogs, the Program Board, the Roadmap, the Dashboard, and the Calendar, kept in the Registry; the Solution Definitions, kept in the Portfolio; and the Acceptance Checklists, the Control Sign-Offs, and the Registry Snapshots, which are the evidence records.

9.2. The controls that this model carries, whose rules it states or whose evidence it keeps, are C-10, C-12, C-13, C-14, C-15, C-16, C-20, C-22, C-26, C-28, C-29, C-30, and C-31 of the Operating Model 8. The following table shows where each step of the life of a Solution is controlled.

| Step | Clause | Decides | Evidence | Control |
| --- | --- | --- | --- | --- |
| Approval of a Capability or a Feature | 3.1, 5.1 | AICC Lead; the Team | Program Backlog | None; working state, in the Registry until the cutover and then in Jira |
| Solution Definition and Risk Tier | 5.2 | Domain Owner approves; AICC Lead assigns the Tier; the Executive Sponsor for a Solution that the AICC Lead built | Solution Definition; AI Registry | C-12, C-15 |
| Verify, check or validation | 7.1 | Checker; Control Function Contacts | AI Registry entry; Control Sign-Off | C-13 |
| Deployment to production, and change | 8.3, 8.6 | Change management of the Bank; AICC Lead | Change ticket; Solution Definition | C-30 |
| Release | 7.1, 7.4 | Domain Owner; Executive Sponsor for Risk Tier 3, and where the AICC Lead is the Domain Owner | Release block; Acceptance Checklist | C-14, C-22 |
| Acceptance of a Feature or a Capability | 7.3(a) | Product owner | Backlog note | C-10 |
| Team final acceptance of a Solution | 7.3(b) | AICC Lead | Release block | C-10 |
| Business acceptance of a Solution | 7.3(c) | Domain Owner; Executive Sponsor for an item across Domains, enabling work, or an Experiment with no Domain | Release block; Outcome Report | C-10 |
| Operation and review | 8.4, 8.5 | IT function; Domain Owner; Executive Sponsor for a Service across Domains | Service Management; Solution Definition | C-16, C-29 |
| Retirement | 8.7 | Domain Owner; Executive Sponsor | Solution Definition; AI Registry | C-31 |

## 10. Measures

10.1. AICC measures its flow to control it and to improve it, and not to rank people. It works on Kanban, so it measures flow and does not measure velocity, story points, or the output of a person. A measure has a definition, a source, a place where it is read, and a target that the Team sets with the product owner once it has a baseline. A figure of the Bank stays in its source, and the records point to it. The Dashboard shows the measures (4.4). In light mode (6.6) cycle time runs from Active to Review, and Verify and Deploy are read from the check record and the change ticket.

10.2. The following table states how each stage is measured and where the measure is read.

| Stage | What is measured | Measure | Read at |
| --- | --- | --- | --- |
| Funnel | How long a need waits | The age of the oldest item; the items in the funnel | Weekly Review |
| Reviewing, Analyzing | How long a business case takes to be decided | Time from a proposal to its approval; business cases returned | Monthly Steering |
| Portfolio Backlog | Demand against capacity | Approved Initiatives waiting; days waiting; Active against the limit | Monthly Steering |
| MVP | Whether the hypothesis holds | The leading indicators against the plan; the capacity used against the capacity allowed | End of the MVP; quarterly Steering |
| Implementation, Done | Whether the value arrived | The benefit confirmed against the benefit claimed and against the Envelope | Quarterly Steering |
| Explore, Design | Readiness for the next Iteration | The Features that are ready, in Iterations of work ahead | Backlog Refinement; Iteration Planning |
| Develop | The flow of the work | Cycle time; work in progress and its age; Waiting items and days Waiting | Weekly Review |
| Verify | Quality at the gate | The share that meets the check or the validation first time; the items returned; the defects found in operation after the check | Weekly Review; Iteration Review and Demo |
| Deploy | The safety of the change | The change failure rate; rollbacks; emergency changes | Iteration Review and Demo |
| Release | The readiness to go beyond the first users | Time from verified to released; items of the Acceptance Checklist not met | Iteration Review and Demo |
| Review | Value accepted | Features accepted by the product owner against Features selected; accepted first time; time from Completed to Accepted | Iteration Review and Demo |
| Program Increment | Predictability | PI Objectives achieved against planned, with the business value scored; Dependencies Met by their date | PI Review and Demo |
| Operate | The health of the service | Availability; incidents by severity and repeat incidents; time to restore; requests handled within target | Iteration Review and Demo |
| Evolve | The health of change | Lead time of a change | Iteration Review and Demo |
| Retire | Completeness | Retirements complete: access removed, data handled, registry entry marked | When the Solution is retired |

10.3. The measures are defined as follows.

| Measure | Definition |
| --- | --- |
| Lead time | Days from Approved to Accepted |
| Cycle time | Days from Active to Completed, or to Review in light mode |
| Throughput | The Features accepted in an Iteration |
| Work in progress, and its age | The items that are Active, and the days that each has been Active |
| Waiting time | The days that an item is Waiting on a Dependency |
| First-time-right rate | The share of items that meet the Verify or the Review at the first attempt |
| PI predictability | The share of the PI Objectives that are achieved of those that were planned, read as a trend and with no target, as the PI Objectives are not a promise (2.2) |
| Dependency timeliness | The share of the Dependencies that are Met by the date on which they are needed |
| Change failure rate | The share of deployments and changes that are rolled back or cause an incident |
| Availability | The share of the agreed service time during which the Solution is available |
| Time to restore | The time from the detection of an incident to the restoration of the service |
| Response time, and resolution time | The time from a request to its first answer, and to its closure, against the target of its class |
| Human override and correction rate | The share of AI outputs that a person overrides or corrects, against the baseline |

10.4. The service levels of a live Solution are set in its Service Agreement, and they are targets and not guarantees (Business Model 4.2). The following table gives examples of the service levels and of the measures of the operation, with the targets left to each Service Agreement.

| Service level | Example measure | Target |
| --- | --- | --- |
| Availability | The share of the agreed hours in which the service is available | [Set in the Service Agreement] |
| Response to a request | Time to the first answer, by class of service: Urgent, High priority, Normal | [Set per class] |
| Resolution of a request | Time to closure, by class of service | [Set per class] |
| Restoration after an incident | Time to restore, by severity | [Set per severity] |
| Quality of the output | The human override and correction rate, and the error rate against the baseline | [Baseline and trend] |
| Use | The users who use the Solution each week | [Trend] |
| Change | The change failure rate | [Set in the Service Agreement] |

## Change log

| Revision | Date | Change | Decision |
| --- | --- | --- | --- |
| 1.0 | 2026-10-01 | Created from the Operating Model: the flow of work, the states and Stages, the cadence of the delivery loops, verification, release, acceptance, and the life cycle of a Solution. | DR-2026-040 |
| 1.1 | 2026-10-01 | The Acceptance Checklist at the handover of a ready Solution to a Domain for use at scale; the Executive Sponsor signs for Risk Tier 3. | DR-2026-041 |
| 1.2 | 2026-10-01 | Auditor review: change after release (7.3), review of live Solutions (7.4), retirement (7.5), production deployment, a stop is final (4.3), and clauses split. | DR-2026-042 |
| 2.0 | 2026-10-02 | Restructured top to bottom as the method of the Teams: principles and values, the intake, the flow of value, the backlogs and the boards, the Program Board, the states, the cadence with the Program Increment, Iteration, and week loops, verification and release, the life cycle, and the records and controls. | DR-2026-049 |
| 2.1 | 2026-10-02 | The levels of the work as a diagram by intent, backlog, and decider; the table of the boards with their columns, Stages, lanes, limits, and measures. | DR-2026-049 |
| 2.2 | 2026-10-02 | The Program Board with its Milestones and a table of its form; the flow of the Program Board, the Dependencies, and the Milestones through a Program Increment. | DR-2026-049 |
| 2.3 | 2026-10-02 | The staging workflow of the Feature, the Capability, and the Solution, with the conditions between the Stages. | DR-2026-049 |
| 2.4 | 2026-10-02 | The wording of the Initiative, the Capability, and the Feature: the parts of the wording, the wording of each level, and an illustration. | DR-2026-049 |
| 2.5 | 2026-10-02 | Life-cycle management with the life of a Solution by type, the deployment, the operating loop, the support, the change, and the retirement, each with its diagram. | DR-2026-050 |
| 2.6 | 2026-10-02 | The measures: how each stage is measured, the definitions, and the service levels of a live Solution. | DR-2026-051 |
| 2.7 | 2026-10-02 | Auditor evaluation end to end: the test of every Feature and the MVP, first users and the release record, deployment evidence, emergency change under the change management of the Bank, release separated from acceptance in Figure 8, the controls table, the measures aligned. | DR-2026-052 |
| 2.8 | 2026-10-02 | Review of the independent findings: Waiting is a state shown as a flag; Cancelled from Proposed and from Review; the IP week and the Steering of its month; priority and the order of pulling; the signatories of the Acceptance Checklist by Risk Tier; the quarterly review of the Adopted Solutions; the controls list; measures in the illustration; change log dates aligned with the Decision Log. | DR-2026-055 |
| 2.9 | 2026-10-02 | The release decider where the AICC Lead is the Domain Owner; the review week of the third Iteration; the controls the model carries. | DR-2026-055 |
| 3.0 | 2026-10-02 | Acceptance at three levels: the product owner accepts Features and Capabilities, the AICC Lead gives the final acceptance of the Team before a Solution is deployed to its first users, and the Domain Owner, or the Executive Sponsor, accepts the Solution; the accepted limit for the AICC Lead; Figures 2 and 8, the states, the review of live Solutions, and the controls table aligned. | DR-2026-056 |
| 3.1 | 2026-10-02 | The yearly Steering of December, held in the first two weeks, sets the frame of the next year; the exception to the single Steering of the IP-week month in December. | DR-2026-057 |
