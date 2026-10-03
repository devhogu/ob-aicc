# Measures and tracking

Delivery is measured to control the flow and to improve it, not to rank people. The Team works on Kanban, so it measures flow and quality and does not measure velocity, story points, or the output of a person. This part states what is measured at each loop, in four families, the flow of the work, the quality of what is built, the health of what is live, and the value that arrived, and where each is read. The definitions and the formulas are on the page Delivery measures: definitions and formulas.

## 1. What each loop reads

| Loop | What it reads | From | Decides on it |
| --- | --- | --- | --- |
| Day | Blockers; the Work Items in progress against the per-person limit | The Team board | Clear the blocker today or raise it |
| Week | Work in progress and its age; cycle time; Waiting items and days Waiting; items by lane; first-time pass at the test; Dependencies at risk; the age of the oldest item in the funnel | The Program Kanban; the Dashboard | Reorder the Program Backlog; adjust a limit; unblock; raise a Dependency |
| Iteration | Features accepted against Features selected; accepted first time; time from Completed to Accepted; change failure rate and rollbacks; items of the Acceptance Checklist not met; for each live Solution its availability, incidents, time to restore, requests within target, override rate | The Iteration Review and Demo; the live review | Accept or return; an improvement at the Retrospective; a change, a re-check, or a retirement |
| Program Increment | PI Objectives achieved against planned, with the business value scored; Dependencies met by their date; throughput of the quarter; lead time from Approved to Accepted; the trend of each measure above | The PI Review and Demo; Inspect and Adapt | The improvement items of the quarter; the next PI Planning; the Quarterly Report |

## 2. The flow of the work

2.1. Flow is measured on the Program Kanban, per Feature. Work in progress and its age say how much is open and for how long; cycle time says how long the work takes once started; lead time says how long the function waits from approval to acceptance; throughput says how many Features are accepted per Iteration; Waiting time says how much of the wait is outside AICC. The five move together: when work in progress is held and blockers removed, cycle time falls, throughput rises, and lead time follows. They are read as distributions and trends, and the Team sets the targets with the product owner once it has a baseline.

## 3. The quality of what is built

3.1. Quality is measured at the gates. The first-time pass rate at the test and at the acceptance says whether quality is built in or inspected in. Defects found in operation after the check say what the check missed. The change failure rate, deployments and changes rolled back or causing an incident, says whether deployment is safe. Items of the Acceptance Checklist not met at release say whether the Solution was ready. A falling first-time pass or a rising change failure rate is a problem for the Retrospective and Inspect and Adapt, not a reason for another gate.

## 4. The health of what is live

4.1. A live Solution is read at each Iteration Review and Demo on its availability against the agreed service time, its incidents by severity and the repeat incidents, its time to restore, its requests handled within the target of their class, and, for AI, the rate at which people override or correct its output against the baseline. The four signals of the life of a Service, service levels, incidents, adoption, and cost, are read from the same measures. A Solution whose signals fall is reviewed for a change, a re-check, or its sunset.

## 5. The value that arrived

5.1. The value is read at two levels. At the Program Increment, the PI Objectives are scored for the business value they delivered against what was planned, and the ratio, read as a trend without a target, is the predictability of delivery: it says whether the plan of a quarter can be trusted. At the Initiative, the key results of the Initiative Brief and the benefit the Domain Owner confirms say whether the hypothesis held; they are the measures of the Portfolio, and delivery feeds them.

## 6. How it is tracked

6.1. The measures are read from three places and no other is added: the boards, from which flow is read live; the Dashboard, which the AICC Lead keeps current at the Weekly Review and the monthly Steering reads; and the records of the events, the acceptances in the backlogs, the live review notes in the Solution Definitions, the PI Objectives with their scores, and the Registry Snapshot at the close of each Iteration and Program Increment. A figure of the Bank stays in its source system, and the records point to it. The live portal of AICC will present the measures; this site states what they are.

## 7. Rule source

Solution Lifecycle Model 10; AI Competence Center Charter 7.1; Statement of Intent 11.3; Portfolio Management Model 9.
