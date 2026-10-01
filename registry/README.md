# Registry

The Registry holds the Records of AICC: the process records of the work in progress and delivered, the decisions, the proposals, and the
governance records. It holds no figures of the Bank, no data, and no code. The Operating Model 9 states the rules: the working state
moves to Jira and Confluence at the cutover, and the evidence records are always here, as closed and dated extracts. Jira, Confluence,
and Service Management are not an evidence store. The AICC Lead is accountable for all the Records.

## Working state

Kept here by hand until the cutover Decision, then held in Jira and Confluence. The Registry keeps an extract of it in each Registry
Snapshot.

| Record | Where | Holds |
| --- | --- | --- |
| Portfolio Backlog | [portfolio-backlog.md](portfolio-backlog.md) | The ranked Initiatives, and for each Engagement its client function, phases, support level, Service Agreement, and Outcome Report |
| Program Backlog | [program-backlog.md](program-backlog.md) | The ranked Epics and Features |
| Kanban boards | [board.md](board.md) | The Portfolio Kanban and the Program Kanban, by state, with lanes and Limits on Work in Progress |
| Roadmap | [roadmap.md](roadmap.md) | The three-month Roadmap by Program Increment, and the Milestones |
| Calendar | [calendar.md](calendar.md) | Program Increments, Iterations, weeks, and the blocked and gray days |
| Teams | [teams.md](teams.md) | The Teams, members, and capacity |
| Program Increment | [pi/](pi/2026-PIQ4/objectives.md) | For each: PI Objectives, monthly Iterations with their IT Backlogs and Weekly Review notes, and the IP week |
| Dependency Map | [dependencies.md](dependencies.md) | Dependencies of each item, and its scope by month |
| Dashboard | [dashboard.md](dashboard.md) | The state of the Program Increment, flow, Dependencies, risks, and Measures |

## Living records

Current by nature, and always kept here.

| Record | Where | Holds |
| --- | --- | --- |
| Priorities | [priorities.md](priorities.md) | Strategic Priorities, and references to the Investment Envelopes, Guardrails, and Measures |
| Standards | [standards.md](standards.md) | Architecture standards and Platform requirements |
| Risks and Issues | [risks-and-issues.md](risks-and-issues.md) | Risks, issues, AI Incidents, Exceptions, Findings |
| AI Registry | [ai-registry.md](ai-registry.md) | Each Solution, model, and agent |
| Appointments | [appointments.md](appointments.md) | Holders of the Roles, with the decision reference, and the delegations of the Executive Sponsor |

## Evidence records

Closed and dated extracts, always kept here. The Operating Model 10 lists the controls and the record that evidences each.

| Record | Where | Holds |
| --- | --- | --- |
| Decision Log | [decision-log.md](decision-log.md) | Decisions, one line each; the Decision Records are in [decisions/](decisions/) |
| Initiatives | [initiatives/](initiatives/) | One folder for each: `INI-001-short-title/` with its brief, Service Agreements, Outcome Reports, Epics, and Features |
| Reports | [reports/](reports/) | Quarterly Reports, named `2026-PIQ4.md` |
| Notes | [notes/](notes/) | Notes of the events that need them, named `2027-01-15-it-review.md` |
| Assessments | [assessments/](assessments/) | Earlier checks of the documents, kept for history |

Identifiers: PRI-n priority, INI-nnn Initiative, SOL-nnn Solution (in the Portfolio), EP-nnn Epic, FT-nnn Feature, DEP-nnn Dependency, MS-nnn Milestone, DR-yyyy-nnn Decision, RI-nnn risk or issue, ARC-nnn and PLT-nnn standards, AGR-nnn Service Agreement, OUT-nnn Outcome Report.

The Solutions that AICC defines and tries are in the Portfolio (`portfolio/`), and the cadence is in the charter workflows. Earlier versions of the Records are in `wiki/archive/records-v1/`.
