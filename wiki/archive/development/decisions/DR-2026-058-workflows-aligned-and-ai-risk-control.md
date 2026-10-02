# DR-2026-058 The workflows aligned with the documents, and the AI risk and control workflow

| Field | Entry |
| --- | --- |
| Identifier | DR-2026-058 |
| Title | The workflows aligned with the documents, and the AI risk and control workflow |
| Date | 2026-10-02 |
| Type | Decision |
| Level | AICC Lead |
| Decided by | AICC Lead (Timur Alimbayev) |
| Status | Decided |

## 1. Facts

- An independent review of the workflows folder against the Operating Model, the Portfolio Management Model, the Solution Lifecycle Model, the AI Policy, the Business Model, and the guides found the workflows mostly sound but not yet aligned with the decisions of DR-2026-050 to DR-2026-057.
- The Unit governance workflow was an index of pointers to the control loops, and the Service delivery workflow lacked the portfolio Kanban, the acceptance chain, the emergency change, and the support flow.
- The AI Policy was the only operating document without a workflow.
- The workflows README named a source framework in a column, and the Service delivery workflow named one in its text. The Operating Model and the Solution Lifecycle Model keep the names of frameworks out of the documents.
- A few workflow tables carried control references and audit wording that are not needed to run the work.

## 2. Options

1. Correct the workflows in place and leave the AI Policy without a workflow.
2. Correct the workflows and add the AI Policy flows as a section of the Service delivery workflow.
3. Correct the workflows and add a workflow of its own for the AI risk and control flows.

## 3. Decision

The AICC Lead takes the third option, and decides the following.

1. D1: A workflow AI risk and control is added: the Risk Tier, the gates before first use, the live review, and the Exception, suspension, and stop, with the two single decisions of the Executive Sponsor. It states no rule of its own.
2. D2: The Unit governance workflow shows the control loops with their deciders, what each Steering carries, the escalation of a decision, the events, a month, a quarter, and a year in sequence, the AI Incident, the reporting chain, and the life of a document. The columns of control references and the control-testing rows are removed.
3. D3: The Service delivery workflow shows the main stream of the states with the routes out, the portfolio Kanban, the verify, acceptance, and release chain, the emergency change, and the support flow. The tool-configuration table is removed, and the Engagement workflow shows the exits of an Engagement.
4. D4: The Cadence workflow has one table of what each event carries, the Steerings of a year with the yearly Steering of December, and the Program Board through a Program Increment. The Collaboration tooling workflow holds the one explanation of the cutover.
5. D5: The workflows carry no control references and no audit wording, and no name of a source framework. The workflows README states when each workflow is read.
6. D6: The names of source frameworks and the abbreviation LPM are removed from the defining documents. The environment of use is defined in the Solution Lifecycle Model 7.1 and the Vocabulary. An Exception states its expiry date and the Executive Sponsor reviews open Exceptions monthly (AI Policy 6.1).
7. D7: Open points that the documents do not yet settle: whether a renewed Exception is a new one, a maximum length of an Exception, and how the lowering of a Risk Tier is recorded.

## 4. Conflicts and advice

None declared. D6 gives a duty to the Executive Sponsor, and no record exists of the agreement of the Executive Sponsor. The AICC Lead tells the Executive Sponsor of the change (Document Catalog 4.2).

## 5. Evidence of the Decision

This Record; the Decision Log entry DR-2026-058; the change-log rows that cite it in the documents revised on the same date; the workflows in the charter, with the new AI risk and control workflow.

## 6. Funding and review

| Field | Entry |
| --- | --- |
| Funding reference | None |
| Revisit | When the first Solution passes the gates before first use, or at the next review of the pack |
| Supersedes | None |
