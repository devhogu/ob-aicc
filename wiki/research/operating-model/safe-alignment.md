# Alignment with SAFe and Kanban

How the cadence and the Records of AICC follow the Scaled Agile Framework and Kanban. This page is lineage. The Operating Model holds the rules, and only the scaffolding of the loops is in place: no process is defined yet for the Iteration or Program level.

| SAFe or Kanban construct | AICC term | Where |
| --- | --- | --- |
| Program Increment (PI) | Program Increment: one quarter | Calendar |
| Iteration | Iteration: one calendar month of four or five whole weeks | Calendar; IT Backlog |
| Innovation and Planning iteration | IP week: the last week of the third Iteration | Calendar; pi/ folder |
| PI Planning | PI Planning | Operating Model 7.1 |
| System Demo, PI review | PI Review and Demo | Operating Model 7.1 |
| Inspect and Adapt | Inspect and Adapt | Operating Model 7.1 |
| IT Planning, Review, Retrospective, Daily Stand-up | the same | Operating Model 7.1 |
| PI Objectives, confidence vote, business value | PI Objective | pi/ folder |
| Portfolio Backlog; Program (PI) Backlog | Portfolio Backlog of Initiatives; Program Backlog of Epics and Features | portfolio-backlog.md; program-backlog.md |
| Team Backlog or IT Backlog | IT Backlog | pi/ folder |
| Program Kanban and Team Kanban, classes of service | Program Kanban with lanes: Incident, High priority, Normal; Team board | board.md |
| WIP limits | Limits on Work in Progress | board.md |
| Roadmap | Roadmap: three months, by Program Increment | roadmap.md |
| Dependency board | Dependency Map | dependencies.md |
| Program dashboard | Dashboard | dashboard.md |
| Strategic theme, portfolio epic, capability, feature, story | Strategic Priority, Initiative, Solution and Epic, Feature, Work Item | Operating Model 6.1 |
| Business Owners | Domain Owners and the Executive Sponsor | Operating Model 4.2 |
| Product Management, Release Train Engineer, System Architect | AICC Lead, the facilitator Hat, and the AICC Lead | Operating Model 4.3 |
| Lean Portfolio Management, funding of value streams | Priorities, Investment Envelopes, Steering | Charter 4 |
| Continuous exploration, integration, deployment, release on demand | The Stages, and the release decided by the product owner | Operating Model 6.4 |

## Choices

- Iterations follow the calendar month, four or five whole weeks (a week belongs to the month of its Thursday), not a fixed two weeks. The work is exploratory and depends on people and events outside AICC, and the Bank works by month. SAFe prefers fixed-length iterations; the Weekly Review gives the short control loop instead.
- A Program Increment is a quarter of three Iterations. Its items state intent and direction, not committed scope. The Dependency Map breaks each into months.
- The Calendar marks blocked and gray days, and events move to the day before.
- A Portfolio Backlog holds the Initiatives, and a Program Backlog holds the Epics and Features, as in full SAFe. The IT Backlog holds the Features in work.
- Acceptance by the product owner closes an item, as in agile work. Control Function validation is independent and is not an acceptance.
- Statuses are kept apart from stages. Thirteen business states apply to every level, with the stages as phases inside discovery and active, and Jira carries five statuses, a flag, and a resolution.
- Offering types (Service, Product, Experiment) decide the life of a solution after delivery, and the receiver is named at definition. This follows the AI center of excellence pattern of embedding, then handing over, with an explicit handoff.
