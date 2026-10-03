# Controls and the control catalogue

A control is a rule the unit follows anyway, written so that an auditor can test it: an objective, the rule and its clause, an owner, a timing, the evidence record it leaves, and the way it is tested. AICC has thirty-two, each with a reference, carried by the five control loops and kept in a catalogue; their status at any date is in the Control Matrix of the Registry. This part explains what a control is, how the catalogue is built, and how a control lives.

## 1. What a control is

1.1. Each control is a rule of the Operating Model, the Solution Lifecycle Model, the AI Policy, or the Business Model, or an event of the control loop, and it leaves an evidence record. It has a reference, C-01 to C-32; a title and an objective; the rule, with the clause that states it; an owner, the Role accountable for it; a timing, when it operates; an evidence record and, where one applies, a template; a type; and a test, the way an auditor or the AICC Lead confirms it operated. The controls are not added to the work; they are the work, named.

## 2. The catalogue by loop

| Loop | Controls it carries | What they cover, in short |
| --- | --- | --- |
| Direction, yearly | C-01, C-02, C-03, C-04, C-20 | The activation and review of the documents; the AI Risk Appetite Statement; the appointments; the Strategic Priorities, the Envelopes, and the Guardrails; the Proposal to the Bank |
| Assurance, quarterly | C-06, C-07, C-11, C-16, C-20, C-24, C-26, C-27, C-28 | The Quarterly Report and the report to the Board Committee; the quarterly risk check; the Risk Tier reassessments; the validations; the access review; the reconciliation of the AI Incidents; the Registry Snapshot |
| Control, monthly | C-05, C-17, C-29, C-32 | The sample of Decisions; the deficiencies; the acceptances; the live review of the Solutions |
| Operating, weekly | None; the Dashboard is a working record | The flow, the limits, the Dependencies |
| Event | C-01, C-16, C-17, C-19, C-27, C-30, C-31, C-32 | An AI Incident; an Exception; a stop or a suspension; a risk beyond appetite; a finding; a change of Holder; a change of provider or regulation |

2.1. The page Controls and the control catalogue, under the rule, lists all thirty-two with their rule, owner, timing, evidence, template, objective, type, and test, with a page for each, and the Unit governance guide states how each is tested. The references are stable: a control is cited by its reference in the documents, in the Control Matrix, in a finding, and in this site.

## 3. The life of a control

3.1. Each control follows one cycle: a trigger, which is its timing or its event; a decision at the level the Operating Model names; a record, the evidence it leaves; and a review, at the Steering of its loop. The Control Matrix gives each control one of five statuses at a date: Operating, when it operated and left its evidence; Open, when it is due and its evidence is not yet in; Deficiency, when it did not operate or its evidence shows a failure; No occurrence yet, when its event has not happened; and Not yet due, when its first timing has not come.

```mermaid
flowchart LR
  T(["Trigger<br/>the timing of the control,<br/>or its event"]) --> D["Decision<br/>at the level the<br/>Operating Model names"]
  D --> R["Record<br/>the evidence record,<br/>closed and dated,<br/>in the Registry"]
  R --> V["Review<br/>at the Steering of its loop;<br/>status in the Control Matrix"]
  V -->|"operated"| OK(["Operating"])
  V -->|"did not operate,<br/>or a failure found"| DF["Deficiency<br/>Risks and Issues, owner,<br/>due date; reviewed monthly<br/>until closed"]
  DF -.-> T
```

Figure 1: the cycle of a control, and a deficiency.

## 4. Deficiencies and findings

4.1. A control that did not operate, and each finding of an audit or a supervisor, enters the Risks and Issues Record with an owner and a due date, and the monthly Steering reviews it until it is closed; an overdue deficiency is decided at once. A deficiency is not a failure of governance; it is governance working. What would be a failure is a deficiency nobody recorded.

## 5. Rule source

Operating Model 6.1 and 8; the Control Matrix of the Registry; the Unit governance guide 7; the Control Sign-Off and Acceptance Checklist templates.
