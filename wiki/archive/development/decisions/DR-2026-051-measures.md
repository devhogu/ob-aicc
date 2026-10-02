# DR-2026-051 The measures of the Solution Lifecycle Model

| Field | Entry |
| --- | --- |
| Identifier | DR-2026-051 |
| Title | The measures of the Solution Lifecycle Model |
| Date | 2026-10-02 |
| Type | Decision |
| Level | AICC Lead |
| Decided by | AICC Lead (Timur Alimbayev) |
| Status | Decided |

## 1. Facts

- The method had no way to see how each stage performs (Decision Log, DR-2026-051).
- AICC works on Kanban, so the measures of flow apply and the measures of velocity do not.

## 2. Options

1. Leave the measures to each Team.
2. State the measures by stage in the model, show the flow measures on the Dashboard, and set the targets in the Service Agreements.

## 3. Decision

1. The Solution Lifecycle Model ends with its measures: how each stage is measured and where the measure is read, the definitions, and the service levels of a live Solution as examples.
2. AICC works on Kanban. It measures flow: lead time, cycle time, throughput, work in progress and its age, waiting time, first-time-right rate, PI predictability, and Dependency timeliness. It does not measure velocity, story points, or the output of a person.
3. The operation is measured by availability, incidents and the time to restore, the response and the resolution time against the target of the class of service, the human override and correction rate, use, and the success of changes. The targets are set in each Service Agreement, and they are targets and not guarantees.
4. The Dashboard shows the flow measures.

## 4. Conflicts and advice

None recorded.

## 5. Evidence of the Decision

This Record; the Decision Log entry; the change-log row of the Solution Lifecycle Model 2.6; the Dashboard (`dashboard.md`).

## 6. Funding and review

| Field | Entry |
| --- | --- |
| Funding reference | None |
| Revisit | When the Teams have a baseline for each measure |
| Supersedes | none |
