# DR-2026-050 The deployment and the operating flows of the life cycle

| Field | Entry |
| --- | --- |
| Identifier | DR-2026-050 |
| Title | The deployment and the operating flows of the life cycle |
| Date | 2026-10-02 |
| Type | Decision |
| Level | AICC Lead |
| Decided by | AICC Lead (Timur Alimbayev) |
| Status | Decided |

## 1. Facts

- The life cycle had tables and clauses but no flows (Decision Log, DR-2026-050).
- Deployment, operation, support, change, and retirement depend on the change management and the incident management of the Bank (DR-2026-039).

## 2. Options

1. Keep the tables and the clauses.
2. State each flow with a diagram, and make the Bank's change management the path of deployment.

## 3. Decision

1. The life-cycle management of the Solution Lifecycle Model states the life of a Solution by type, the deployment of a Feature, the operating loop of a live Solution, the support of requests and incidents, the loop of a change, and the retirement. Each has its diagram.
2. The deployment follows the change management of the Bank. The Solution Engineer raises the change, enters the ticket and the test result in the Feature, and deploys through the access process of the Bank. A failed deployment is rolled back as the change management of the Bank requires and is handled as an incident.
3. The operation is run by the IT function that operates the Solution, and by the Solution Engineer for a Service that AICC runs. The product owner reviews each live Solution at the Iteration Review and Demo.
4. Requests and incidents come to the queue of AICC in Service Management, and are triaged by class of service. An AI Incident is handled in the incident management of the Bank.
5. The clauses of the life cycle are renumbered: change is 8.6 and retirement is 8.7, and the Operating Model controls cite them.

## 4. Conflicts and advice

None recorded.

## 5. Evidence of the Decision

This Record; the Decision Log entry; the change-log row of the Solution Lifecycle Model 2.5.

## 6. Funding and review

| Field | Entry |
| --- | --- |
| Funding reference | None |
| Revisit | When the first Solution is deployed |
| Supersedes | none |
