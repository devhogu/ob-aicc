# Backlogs, boards, and Kanbans

The work of delivery is visible in two backlogs and four boards, and it flows as in Kanban: pulled when a limit allows, not pushed when a plan says. This part states what each backlog and board holds, how the Kanbans limit the work, how the Program Board shows the dependencies of a quarter, and how the Roadmap and the Dashboard read the whole.

## 1. The two backlogs

1.1. The Program Backlog, also called the PI Backlog, holds the Capabilities and the Features, grouped under their Initiatives, ranked by value and urgency relative to effort, each term scored from 1 to 5 together with risk reduction or opportunity, and effort. The AICC Lead ranks it, with the Domain Owners stating the value. The Iteration Backlog holds the Features the Teams work on in the Iteration, selected at Iteration Planning. The Portfolio Backlog of the Initiatives sits above both and is the subject of the Portfolio course.

1.2. A Feature is ready to be pulled when it is approved, its acceptance criteria are written, and its Dependencies are known. That is its definition of ready. It is done when it is verified, deployed to its environment of use, and accepted by the product owner against its criteria. That is its definition of done. Backlog Refinement, held within the weekly events, keeps one to two Iterations of ready Features ahead of the Team.

## 2. The boards

| Board | Shows | Columns | Lanes | Limit on Work in Progress | Read at |
| --- | --- | --- | --- | --- | --- |
| Portfolio Kanban | Initiatives | Funnel, Reviewing, Analyzing, Portfolio Backlog, MVP, Implementation, Done | None | The Active Initiatives, set by the AICC Lead | Monthly Steering |
| Program Kanban | Capabilities and Features | Backlog, Ready, Active, Review, Done; Waiting as a flag with its Dependency | Classes of service: Urgent, High priority, Normal | Per state, per lane, and per Domain, set by the Team | Weekly Review |
| Team board | The Work Items of the Iteration | Backlog, Ready, Active, Review, Done | None | Per person, set by the Team | Daily Stand-up |
| Program Board | The Capabilities and Features of the Program Increment by Iteration, their state, their Dependencies, and the Milestones of the Roadmap | One column per Iteration and the IP week | One lane per Feature | None; the Dependencies at risk are raised | PI Planning; Weekly Review; monthly Steering |

## 3. How a Kanban limits the work

3.1. A limit on work in progress is a number on a column, a lane, or a Domain: no more than so many items may be in that state at once. When the limit is reached, the Team finishes before it starts, and a new item is pulled only when a place is free. The limit is set by the Team for the Program Kanban and reviewed at the Weekly Review; it is set by the AICC Lead for the Active Initiatives within the mix of the Executive Sponsor. The classes of service are lanes with their own limits: Urgent, a Service down or wrong output reaching people; High priority, a consumer blocked with a date; Normal, everything else. An item Waiting on a Dependency outside AICC keeps its place and its flag, so that waiting is seen and counted rather than hidden.

3.2. The effect of the limits is the point of the method: the fewer items in progress, the shorter the time each takes, and the sooner the function sees a result. Lead time, work in progress, and throughput move together, as the Measures part explains.

## 4. The Program Board

4.1. The Program Board is the board of the dependencies of a Program Increment. For each Capability and Feature it shows the Iteration in which it is planned, its state, and what it needs from other items, Teams, functions, and persons; it shows the Milestones of the Roadmap at the Iteration in which they fall. The AICC Lead builds it with the Teams at PI Planning and keeps it current at the Weekly Review. A Dependency has a date by which it is needed and a status, Met, Open, or At risk; an At risk Dependency is raised to the monthly Steering. The board is the one place where a quarter can be seen as a whole, and it is what makes a plan of intent honest: a Feature whose Dependency is Open cannot be promised.

| Feature | Capability | Iteration 1 | Iteration 2 | Iteration 3 | IP week | Depends on | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| The form of a lane | The Capability it serves | The Stage planned or reached | | | | The item, Team, function, or person, and the date needed | Met, Open, At risk |

## 5. The Roadmap and the Dashboard

5.1. The Roadmap shows three horizons: the current Program Increment as intent and direction, the next as planned, and the period beyond as indicative, with its Milestones. PI Planning proposes it and the quarterly Steering confirms it. The Dashboard shows the state of the Program Increment, the flow of the Program Kanban, the Dependencies at risk, the risks, and the Measures; the AICC Lead keeps it current at the Weekly Review, and the monthly Steering reads it.

## 6. Rule source

Solution Lifecycle Model 4 and 6.4; Portfolio Management Model 5.4 and 6.5.
