# Unit governance workflow

## 1. Intent and scope

This workflow shows how AICC is directed, reported, and controlled as a unit of the Bank, and who does what in sequence. It answers the question "how does your unit operate?". It shows how the loops of the unit and of the portfolio stack on the Steerings and the Weekly Review, how a decision moves up and what each Steering carries, what happens on an event, and the sequences between the Roles for a month, a quarter, a year, and an AI Incident.

The rules are in the Operating Model, the Portfolio Management Model, the Solution Lifecycle Model, the AICC Charter, and the AI Policy. This workflow shows the flow and the intent, and states no rule of its own. The controls of an AI Solution, from the Risk Tier to the Exception and the stop, are in the AI risk and control workflow.

## 2. The loops on the Steerings

The control of the unit runs as five loops (Operating Model 6), and the portfolio runs as four loops (Portfolio Management Model 4). They run on the same Steerings and on the Weekly Review, and they add no meeting. The strategic loop runs with the direction loop at the yearly Steering, the portfolio review loop with the assurance loop at the quarterly Steering, the portfolio sync loop with the control loop at the monthly Steering, and the backlog care loop with the operating loop at the Weekly Review.

Figure 1 shows the loops with the person who decides in each, and how the frame passes down and the evidence passes up between neighbors.

```mermaid
flowchart TB
  DI["Direction loop, yearly<br/>yearly Steering: the monthly Steering of December, in its first two weeks<br/>decides: Executive Sponsor"]
  AS["Assurance loop, quarterly<br/>quarterly Steering<br/>decides: Executive Sponsor"]
  CO["Control loop, monthly<br/>monthly Steering<br/>decides: Executive Sponsor"]
  OP["Operating loop, weekly<br/>Weekly Review<br/>decides: AICC Lead"]
  DI <-->|"frame down: appetite, Priorities, Guardrails<br/>evidence up: Quarterly Report"| AS
  AS <-->|"frame down: corrective actions<br/>evidence up: Steering Summary"| CO
  CO <-->|"frame down: Steering Summary, limits, priorities<br/>evidence up: Dashboard, Dependencies"| OP
  EV["Event loop, when it happens<br/>an AI Incident, an Exception, a stop, a risk beyond appetite,<br/>a change of provider or regulation, a finding, a change of Holder,<br/>and the controls that a step of the work triggers"]
  EV -.->|"entered in Risks and Issues<br/>or a Decision Record, then reviewed"| CO
```

Figure 1: the control loops, their deciders, and the frame and the evidence between them.

The Steerings are not three meetings: the quarterly Steering carries the monthly core and adds to it, and the yearly Steering is the monthly Steering of December and adds to it. Each Steering reviews the controls of the loops it carries (Operating Model 6.1). The following table states what each Steering carries (Operating Model 6.5 to 6.7 and 6.11; Portfolio Management Model 4.2 to 4.4).

| Steering | Loops it carries | What it carries |
| --- | --- | --- |
| Monthly | Control, and portfolio sync; the controls of the operating loop and the event loop | The core: progress, risks, and blockers; a sample of the Decisions of the AICC Lead and the share found in order; the events of the month and the controls that they triggered; the acceptances and the review of the live Solutions; the open Exceptions and the deficiencies; the gate decisions that are due; the Active Initiatives against the limit; the portfolio sync; the governance measures read monthly; the Registry Snapshot of the Iteration |
| Quarterly | Assurance, and portfolio review, in addition to the monthly core | The decision on each Active Initiative; the quarterly risk check and the review of each Risk Tier 3 Solution; the access review; the reconciliation of the AI Incidents with the incident management of the Bank; the status of each control in the Control Matrix and the governance measures read quarterly; the Maturity Level of each Strategic Priority; the report to the Board Committee; the Active Initiatives against the limit and the completeness of the Outcome Reports; the review of the Adopted Solutions; the confirmation of the PI Objectives and the Roadmap |
| Yearly, in December | Direction, and strategic, in addition to the monthly core | The appointments in order; the documents and the AI Risk Appetite Statement; the targets of the Measures of the Maturity Levels for the next year; the governance measures read yearly; the Strategic Priorities, the Investment Envelopes, and the Investment Guardrails; the yearly Proposal of the AI adoption strategy, which the Executive Sponsor presents and the Bank decides; the Quarterly Report of PIQ3 as its input |

In the month that holds the IP week (March, June, and September), the quarterly Steering is also that month's Steering, and no separate monthly Steering is held. In December, the monthly Steering is held in the first two weeks as the yearly Steering, and the quarterly Steering of the IP week carries only the assurance loop and the portfolio review.

## 3. How a decision escalates

Figure 2 shows how the level of a decision is chosen and what it leaves on record (Operating Model 5).

```mermaid
flowchart LR
  DEC(["A decision is needed"]) --> Q1["Is it within the remit<br/>of a Control Function?"]
  Q1 -->|"yes"| CFD["The Control Function decides<br/>nobody overrides it<br/>Control Sign-Off"]
  Q1 -->|"no"| Q2["Does a condition of<br/>Operating Model 5.2 apply?"]
  Q2 -->|"no"| TMD["The person who does the work<br/>decides on the facts<br/>noted in the work item"]
  Q2 -->|"yes"| LV["The AICC Lead, or the Executive Sponsor<br/>at the level that Operating Model 5.3 names"]
  LV --> LOG["Decision Log, one line<br/>and a Decision Record when it is a hard-to-reverse<br/>Decision of the Executive Sponsor or is named in section 8"]
  LOG --> REV["Reviewed in the monthly sample<br/>and at the date to revisit"]
  classDef gate fill:#e8eefc,stroke:#5a6fa8,color:#111
  class Q1,Q2 gate
```

Figure 2: the choice of the level of a decision, and its record.

## 4. Events

An event that is not on the calendar enters the Risks and Issues Record with an owner and a due date, and it runs the same cycle until it is closed (Operating Model 6.9, Figure 6 of the Operating Model). Anyone may raise an event. The following table states what happens for each kind of event.

| Event | What happens | Read |
| --- | --- | --- |
| An AI Incident | It is handled in the incident management of the Bank, and the AICC Lead is a stakeholder, enters it in the Risks and Issues Record with the ticket key, and reviews it afterwards | Section 6, Figure 4; AI Policy 5 |
| An Exception | The Control Function Contact for the remit decides, for a limited time, and the Exception is entered in the Risks and Issues Record and reviewed monthly until it expires | The AI risk and control workflow; AI Policy 6 |
| A suspension or a stop | The AICC Lead or a Contact may suspend, and the suspension is entered in the Decision Log; a stop by a Control Function is final | The AI risk and control workflow; Operating Model 5.4 |
| A risk beyond the appetite | The Executive Sponsor decides, with a Decision Record, and the Board Committee is told without waiting for the next report | Operating Model 5.4; Charter 7.2 |
| A change of provider or regulation | The provider is checked again, and the AICC Lead decides whether the change needs a new check or validation; the Executive Sponsor may call an extra review of the documents and the appetite | AI Policy 4.1; Solution Lifecycle Model 8.6; Operating Model 6.5 |
| A finding or a deficiency | It is entered in the Risks and Issues Record with an owner and a due date, and the monthly Steering reviews it until it is closed | Operating Model 8.2 |
| A change of Holder | The AICC Lead enters the appointment, the change, or the relief in the Appointments Record with its date and its decision reference; the new Holder accepts the Role, names a deputy, receives the access, and completes the training; the access of the previous Holder is removed | Operating Model 4.8, 4.9 |
| A step of the work that triggers a control | A Service Agreement, a business case, a Risk Tier, a check or a validation, a release, a use for a data class, a provider check, a deployment or a change, a sharing of data, a published output, or a retirement leaves its own evidence record; it enters the Risks and Issues Record only when the control is Open or in Deficiency, and the monthly Steering reviews it among the events of the month | Operating Model 6.9, 8.5 |

## 5. A month, a quarter, and a year in sequence

The Teams, the AICC Lead, the Executive Sponsor, the Control Function Contacts, the Board Committee, and the Bank exchange the following each month, each quarter, and each year. Figure 3 shows the sequence.

```mermaid
sequenceDiagram
  participant T as Teams
  participant L as AICC Lead
  participant ES as Executive Sponsor
  participant CF as Control Function Contacts
  participant BC as Board Committee
  participant BK as The Bank
  participant R as Registry
  Note over T,R: Each month
  T->>L: Weekly Review: flow, limits, Dependencies
  L->>R: Dashboard kept current
  T->>L: Iteration Review and Demo: results and acceptances
  L->>ES: Monthly Steering: progress, risks, blockers, events of the month
  ES->>L: Samples the Decisions of the AICC Lead
  L->>R: Steering Summary recorded
  L->>R: Registry Snapshot at the Iteration close
  Note over T,R: Each quarter
  L->>CF: Quarterly risk check
  CF-->>ES: View within their remit
  L->>ES: Quarterly Report
  ES->>BC: Report approved and issued
  L->>R: Registry Snapshot at the PI close
  Note over T,R: Each year, at the yearly Steering in December
  L->>ES: Documents checked, findings of the year
  ES->>L: Appetite decided, appointments in order, Maturity targets set
  L->>R: Changes to the documents activated
  ES->>L: Priorities, Envelopes, Guardrails set
  ES->>BK: Yearly Proposal of the AI adoption strategy presented
  BK-->>ES: The Bank decides the Proposal
```

Figure 3: a month, a quarter, and a year in sequence.

## 6. An AI Incident in sequence

The incident is owned by the incident management of the Bank, and the AICC Lead is a stakeholder (AI Policy 5). Figure 4 shows who does what, in order.

```mermaid
sequenceDiagram
  participant U as Anyone aware
  participant IM as Incident management of the Bank
  participant OPS as IT function that operates the Solution
  participant L as AICC Lead
  participant CF as Control Function Contacts
  participant ES as Executive Sponsor
  participant BC as Board Committee
  participant R as Registry
  U->>IM: Reports the incident and says that AI is involved
  IM->>L: Notifies the AICC Lead
  L->>R: Enters it in Risks and Issues with the ticket key
  IM->>OPS: Handles
  L->>OPS: Advises on the AI aspects, may bring the Solution Engineers
  Note over CF: Assess within their remits. Compliance decides on the regulator, data protection on the persons
  opt A suspension is decided
    Note over L,CF: The AICC Lead or a Contact suspends, entered in the Decision Log
  end
  opt Classified as major by the incident management of the Bank
    L->>ES: Informs
    ES->>BC: Tells the Board Committee without waiting for the next report
  end
  IM->>L: Post-incident review in the incident management
  L->>R: AI Incident Review: cause, controls that failed, Risk Tier reassessed
  Note over L,ES: The monthly Steering reviews the open items until they are closed
```

Figure 4: an AI Incident in sequence.

## 7. The reporting chain

Reporting flows from the Teams up to the Board Committee, and the Control Functions stand beside it, independent of AICC. Internal audit stands outside the chain (Operating Model 2.4, 6.3, 6.10). Figure 5 shows the chain and who sits at the Steering.

```mermaid
flowchart LR
  T["Teams"] --> L["AICC Lead"] --> S["Steering: the Executive Sponsor chairs; the AICC Lead prepares and attends;<br/>the Domain Owners concerned and the Control Function Contacts attend;<br/>the AI Steering Committee advises"] --> B["Board Committee"]
  CF["Control Functions: set the rules of their remit, clear, validate, decide Exceptions, may stop"] -.->|"independent of AICC"| L
  CF -.->|"report on their remit"| S
  IA["Internal audit: independent assurance"] -.->|"outside the chain"| S
```

Figure 5: the reporting chain.

## 8. The life of a document

The Document Catalog 3, 4, and 7 state the life of a document. Figure 6 shows it.

```mermaid
flowchart LR
  D["Draft"] --> K["Check: the ten questions"] --> A["Activation by the AICC Lead"] --> V["Active: in force"]
  AP["AI Risk Appetite Statement: the Executive Sponsor decides"] -.-> A
  V -->|"change of meaning"| N["Next whole revision, checked and activated the same way"]
  V -->|"correction"| CL["Change log row only"]
  V -->|"each year"| Y["Check of the documents together"] --> YS["Yearly Steering reviews the documents and the appetite"]
  YS -->|"changes needed"| N
  V --> DP["Deprecated: kept for history"]
  classDef gate fill:#e8eefc,stroke:#5a6fa8,color:#111
  class K gate
```

Figure 6: the life of a document.

## 9. Where it runs

The loops run in Jira and Confluence from the cutover of the working state (Operating Model 7.1), and until then the Registry holds the working state. The charter holds this schema.
