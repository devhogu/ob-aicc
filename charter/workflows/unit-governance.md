# Unit governance workflow

## 1. Intent and scope

This workflow is the control loop of AICC as an organizational unit: how the unit is directed, how its work is organized and
reported, and how it is controlled. It is the governance and administration that an auditor expects to find in a bank, and the
answer to the question "how does your unit operate?". It covers the mandate, the planning, the reporting, the decisions, the
controls, and the assurance. It does not cover how a solution is delivered, which is in the service delivery workflow.

The rules are in the Operating Model, the AICC Charter, and the AI Policy. This workflow shows the flow and the intent. It states no
rule of its own. The events are those of the Cadence. Each control produces a record, and the guide to the Registry, when it exists, states which.

## 2. The control loop by horizon

The loop runs on four horizons and on events. Each horizon takes the result of the shorter one below it and sets the direction of
the next.

Figure 1 shows the loop. Direction flows down, from the yearly horizon to the weekly one, and control flows up, from the weekly
review to the yearly strategy.

```mermaid
flowchart TB
  Y["Yearly: priorities, funding, guardrails, risk appetite, review of the documents, strategy proposal"]
  Q["Quarterly: results of the PI, risk check, Maturity Level, report to the Board Committee"]
  M["Monthly: progress, risks, blockers, decisions of the Executive Sponsor"]
  W["Weekly: control of the flow and the Dependencies"]
  E["On an event: AI Incident, Exception, stop, risk beyond appetite, change of provider or regulation, change of a Role holder"]
  Y --> Q --> M --> W
  W -.-> M -.-> Q -.-> Y
  E -.-> M
  E -.-> Q
```

Figure 1: the control loop of the unit.

The following table states each horizon.

| Horizon | Events of the Cadence | What is set or reviewed | Decided by | Record produced |
| --- | --- | --- | --- | --- |
| Yearly | The first quarterly Steering of the year | Strategic Priorities, Investment Envelopes, Guardrails, the Roadmap, the AI Risk Appetite Statement, the documents, and the strategy proposal | Executive Sponsor, with the AICC Lead owning the documents | Decision Log; Priorities; strategy proposal |
| Quarterly | PI Review and Demo, Inspect and Adapt, PI Planning, quarterly Steering | The results of the PI, the quarterly risk check with the Control Function Contacts, the Maturity Level, the next PI | Executive Sponsor | Quarterly Report; report to the Board Committee; PI snapshot; Decision Log |
| Monthly | IT Review and Demo, monthly Steering | Progress, risks, blockers, acceptances | Executive Sponsor for his decisions; product owners for acceptance | Decision Log; Notes |
| Weekly | Weekly Planning, Weekly Review | The flow, the Limits on Work in Progress, the Dependencies | AICC Lead | Dashboard |
| On an event | Not scheduled | An AI Incident, an Exception, a stop, a risk beyond appetite, a change of provider or regulation, a change of a Role holder | As the Operating Model states | Decision Log; Risks and Issues; Appointments |

## 3. The reporting chain

Reporting flows from the Team up to the Board Committee, and the Control Functions and internal audit stand beside it, independent
of it.

Figure 2 shows the reporting chain and the independent lines.

```mermaid
flowchart LR
  T["Teams"] --> L["AICC Lead"] --> S["Steering: Executive Sponsor and the AI Steering Committee"] --> B["Board Committee"]
  CF["Control Functions: validate, may stop"] -.independent.-> L
  CF -.report on their remit.-> S
  IA["Internal audit: assurance only"] -.read access to the records.-> L
  IA -.assurance.-> B
```

Figure 2: the reporting chain.

## 4. How a decision moves

A decision is taken by the person doing the work, on the facts. It goes up only when one of the conditions of the Operating Model
applies. A Control Function decides within its remit, and nobody overrides it.

Figure 3 shows how a decision moves.

```mermaid
flowchart TB
  A["A decision arises in the work"] --> B["The person doing the work decides on the facts"]
  B --> C{"Crosses a Domain or Entity, hard to reverse, exceeds a guardrail, accepts a risk, or is Tier 3?"}
  C -->|No| D["Noted in the work item"]
  C -->|Yes| E["AICC Lead decides, or the Executive Sponsor for the strategic matters"]
  E --> F["Entered in the Decision Log"]
  B --> G{"Within the remit of a Control Function?"}
  G -->|Yes| H["The Control Function decides; nobody overrides it"]
  H --> F
```

Figure 3: the movement of a decision.

## 5. The controls an auditor can test

Each control is an event that already exists, and each leaves a record. The Operating Model 10 lists the controls, with their rule, their
owner, their timing, and their evidence record. The loop above shows where they sit: the yearly controls on the strategy horizon, the
quarterly ones on the results, the monthly ones on the review, and the event-driven ones when an incident, an exception, or a change occurs.

## 6. Separation and independence

| Who | May not |
| --- | --- |
| Anyone | Validate or check work they built |
| The owner of a Solution | Validate it |
| The AICC Lead | Validate a Solution within the remit of a Control Function |
| A Control Function Contact | Be a member of AICC, or build what the Contact reviews |
| Internal audit | Validate, release, or stop; it gives assurance only |
| The Executive Sponsor | Set aside a validation or a stop |

## 7. The life of a document

Documents are changed like software. A change that alters the meaning is a new draft revision that does not replace the active text
until it is activated, and every activation is entered in the Decision Log.

Figure 4 shows the life of a document.

```mermaid
stateDiagram-v2
  [*] --> Draft
  Draft --> Active: activated by the AICC Lead
  Active --> Draft: meaning changes, new revision
  Active --> Active: correction, change log row only
  Active --> Deprecated: replaced or withdrawn
  Deprecated --> [*]
```

Figure 4: the life of a document.

## 8. Where it runs

The loop will run in Jira and Confluence from the cutover of the Operating Model 9: Confluence for the notes and reports, and Jira for the
dashboards and the board. Until then the Registry holds the working state. The charter holds this schema. The Registry always holds the
evidence record of each outcome that an auditor may ask for, and the raw material stays in the tools or in the systems of the functions.
