# Registry

The Registry holds the Records of AICC: the process records of the work in progress and delivered, the decisions, the proposals, and the governance records. It holds no figures of the Bank, no data, and no code. The Registry names the people who hold the Roles, in the Appointments Record. A comment in brackets marks an open place and states what is expected there. The Operating Model 7 states the rules: the working state moves to Jira and Confluence at the cutover, and the evidence records are always here, as closed and dated extracts. Jira, Confluence, and Service Management are not an evidence store. The AICC Lead is accountable for all the Records.

## Working state

Kept here by hand until the cutover Decision, then held in Jira and Confluence. The Registry keeps an extract of it in each Registry Snapshot.

| Record | Where | Holds |
| --- | --- | --- |
| Portfolio Backlog | [portfolio-backlog.md](portfolio-backlog.md) | The ranked Initiatives, and for each Engagement its client function, phases, support level, Service Agreement, and Outcome Report |
| Program Backlog | [program-backlog.md](program-backlog.md) | The ranked Capabilities and Features |
| Kanban boards | [board.md](board.md) | The Portfolio Kanban by step and the Program Kanban by state, with lanes and Limits on Work in Progress |
| Roadmap | [roadmap.md](roadmap.md) | The Roadmap by Program Increment, in three horizons, and the Milestones |
| Calendar | [calendar.md](calendar.md) | Program Increments, Iterations, weeks, and the blocked and gray days |
| Teams | [teams.md](teams.md) | The Teams, members, and the Hats |
| Program Increment | [pi/](pi/2026-PIQ4/objectives.md) | For each: PI Objectives, monthly Iterations with their Iteration Backlogs and Weekly Review notes, and the IP week |
| Program Board | [dependencies.md](dependencies.md) | The Capabilities and Features and the Milestones by Iteration, the Dependencies of each item, and its scope by month |
| Dashboard | [dashboard.md](dashboard.md) | The state of the Program Increment, flow, Dependencies, risks, and Measures |

## Living records

Current by nature, and always kept here.

| Record | Where | Holds |
| --- | --- | --- |
| Priorities | [priorities.md](priorities.md) | Strategic Priorities, and references to the Investment Envelopes, Guardrails, and Measures |
| Standards | [standards.md](standards.md) | Architecture standards and Platform requirements |
| Risks and Issues | [risks-and-issues.md](risks-and-issues.md) | Risks, issues, AI Incidents, Exceptions, Findings |
| AI Registry | [ai-registry.md](ai-registry.md) | Each Solution, model, and AI agent; a Record of AICC kept by the AICC Lead, which the AI Platform feeds when it can |
| Control Matrix | [control-matrix.md](control-matrix.md) | Each control of the Operating Model 8 with its latest evidence and its status, and the populations for sampling; the objective, type, and test of each control are in the Unit governance guide |
| Appointments | [appointments.md](appointments.md) | The Appointments Record: the map of the Roles to the Holders, the appointment log, the declarations, the access, and the delegations of the Executive Sponsor |

## Evidence records

Closed and dated extracts, always kept here. The Operating Model 8 lists the controls and the record that evidences each.

| Record | Where | Holds |
| --- | --- | --- |
| Decision Log | [decision-log.md](decision-log.md) | Decisions, one line each |
| Decisions | [decisions/](decisions) | The Decision Records, from DR-2026-060 |
| Initiatives | [initiatives/](initiatives) | One folder for each: `INI-nnn-short-title/` with its brief, Service Agreements, Outcome Reports, Capabilities, and Features |
| Reports | [reports/](reports) | Quarterly Reports, named `2026-PIQ4.md` |
| Steering | [steering/](steering) | The Steering Summaries |
| Proposals | `proposals/` | The Proposals to adopt a Solution at scale, and the yearly Proposal of the AI adoption strategy. Created with the first one |
| Acceptance Checklists | `checklists/` | The Acceptance Checklist of each Solution at its release beyond the first users, named `ACL-001.md`. Created with the first one |
| Control Sign-Offs | `sign-offs/` | The decisions of the Control Function Contacts, named `SGN-001.md`. Created with the first one |
| AI Incident Reviews | `incident-reviews/` | The review of each AI Incident, named `AIR-001.md`. Created with the first one |
| Registry Snapshots | `snapshots/` | The closed extract at the close of each Iteration and PI, named `SNP-2026-PIQ4-I10.md`. The first is due at the close of I10 |
| Appointments | [appointments.md](appointments.md) | The Part C log of the Appointments Record is the evidence of every appointment, change, and relief |

Identifiers: PRI-n priority, INI-nnn Initiative, SOL-nnn Solution (in the Portfolio), PKG-nnn Package (in the Portfolio), CAP-nnn Capability, FT-nnn Feature, DEP-nnn Dependency, MS-nnn Milestone, DR-yyyy-nnn Decision, RI-nnn risk or issue, ARC-nnn and PLT-nnn standards, AGR-nnn Service Agreement, OUT-nnn Outcome Report, SGN-nnn Control Sign-Off, AIR-nnn AI Incident Review, ACL-nnn Acceptance Checklist, SNP-yyyy-PIQn-Inn (Iteration close) or SNP-yyyy-PIQn (PI close) Registry Snapshot, PRP-nnn Proposal, AP-nnn appointment entry. A Service Agreement and an Outcome Report are files in the folder of their Initiative, named `AGR-001.md` and `OUT-001.md`.

The Registry holds the nil statements that an auditor needs. The Risks and Issues states the AI Incidents and Exceptions to date, and the AI Registry states the uses listed to date.

The Solutions that AICC defines and tries are in the Portfolio (`portfolio/`), and the cadence is in the charter workflows.

The charter baseline and the four Standing Initiatives are approved under [DR-2026-063](decisions/DR-2026-063-approved-english-baseline.md). The Registry continues to show actual work and evidence after that baseline; an operational action is kept here until performed, and is not an unresolved charter provision.
