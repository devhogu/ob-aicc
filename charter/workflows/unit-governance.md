# Unit governance workflow

## 1. Intent and scope

This workflow shows how AICC is directed, reported, and controlled as a unit of the Bank, and who does what in sequence. It answers the question "how does your unit operate?". The loops, the states, and the controls are drawn in the Operating Model, and this workflow does not draw them again. It adds the sequences between the Roles, which show the flow in time.

The rules are in the Operating Model, the AICC Charter, and the AI Policy. This workflow shows the flow and the intent, and states no rule of its own.

## 2. Where each loop is drawn

The control of the unit runs as four loops that apply one control cycle. The following table says where each loop and each state machine is drawn.

| Loop | What it answers | Where it is drawn | Controls it carries |
| --- | --- | --- | --- |
| The cycle of a control | Trigger, decision, record, review, and correction | Operating Model, Figure 5 | Every control |
| Direction, by horizon | Who sets direction, and who sees the results, and when | Operating Model, Figure 2 | C-02 to C-07, C-11, C-24 |
| Decision | Who decides, and how a Decision is logged and sampled | Operating Model, Figure 1 | C-01, C-05, C-08, C-09, C-14, C-27 |
| Event | What happens when something goes wrong or changes | Operating Model, Figure 3 | C-16, C-17, C-19, C-30, C-32 |
| Evidence and assurance | How an auditor sees that the controls operate | Operating Model 7 and the Control Matrix | C-25, C-26, C-29 and the Control Matrix |
| The life of a Risks and Issues item, and of a control status | The states of each | Operating Model, Figures 4 and 6 | C-32 and the Control Matrix |

## 3. A month and a quarter in sequence

The Teams, the AICC Lead, the Executive Sponsor, the Control Function Contacts, and the Board Committee exchange the following each month and each quarter. Figure 1 shows the sequence.

```mermaid
sequenceDiagram
  participant T as Teams
  participant L as AICC Lead
  participant ES as Executive Sponsor
  participant CF as Control Function Contacts
  participant BC as Board Committee
  participant R as Registry
  T->>L: Weekly Review: flow, limits, Dependencies
  L->>R: Dashboard kept current
  T->>L: IT Review and Demo: results and acceptances
  L->>ES: Monthly Steering: progress, risks, blockers
  ES->>L: Samples the Decisions of the AICC Lead
  ES-->>R: Steering Summary
  Note over L,BC: Each quarter
  L->>CF: Quarterly risk check
  CF-->>ES: View within their remit
  L->>ES: Quarterly Report
  ES->>BC: Report approved and issued
  L->>R: Registry Snapshot
```

Figure 1: a month and a quarter in sequence.

## 4. An AI Incident in sequence

The incident is owned by the incident management of the Bank, and the AICC Lead is a stakeholder. Figure 2 shows who does what, in order.

```mermaid
sequenceDiagram
  participant U as Anyone aware
  participant IM as Incident management of the Bank
  participant IT as IT function that operates the Solution
  participant L as AICC Lead
  participant CF as Control Function Contacts
  participant ES as Executive Sponsor
  participant BC as Board Committee
  participant R as Registry
  U->>IM: Reports the incident and says that AI is involved
  IM->>L: Notifies the AICC Lead
  IM->>IT: Handles and contains
  L->>IT: Advises on the AI aspects, may bring the Solution Engineers
  L->>CF: Informs
  CF->>CF: Compliance decides on the regulator, data protection on the persons
  opt Classified as major
    L->>ES: Informs
    ES->>BC: Tells the Board Committee
  end
  IM->>L: Post-incident review
  L->>R: Risks and Issues entry and AI Incident Review
```

Figure 2: an AI Incident in sequence.

## 5. The reporting chain

Reporting flows from the Teams up to the Board Committee, and the Control Functions and internal audit stand beside it, independent of it. Figure 3 shows the reporting chain and the independent lines.

```mermaid
flowchart LR
  T["Teams"] --> L["AICC Lead"] --> S["Steering: Executive Sponsor and the AI Steering Committee"] --> B["Board Committee"]
  CF["Control Functions: validate, may stop"] -.independent.-> L
  CF -.report on their remit.-> S
  IA["Internal audit: assurance only"] -.read access to the records.-> L
  IA -.assurance.-> B
```

Figure 3: the reporting chain.

## 6. The life of a document

The Document Catalog 3 and 4 state the life of a document. Figure 4 shows it.

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

## 7. Where it runs

The loop will run in Jira and Confluence from the cutover of the working state (Operating Model 7.1): Confluence for the notes and reports, and Jira for the dashboards and the board. Until then the Registry holds the working state. The charter holds this schema. The Registry always holds the evidence record of each outcome that an auditor may ask for, and the raw material stays in the tools or in the systems of the functions.
