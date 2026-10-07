# Registry

The Registry holds the governance and the evidence of the Competence Center: the living governance records, the decisions, and the closed and dated evidence records. It holds no figures of the Bank, no data, and no code. The Registry names the people who hold the Roles, in the Appointments Record. A comment in brackets marks an open place and states what is expected there. The Operating Model 7 states the rules: the working state of the portfolio and the program is kept in the Portfolio (`portfolio/`), Jira and Confluence run the daily work, and the evidence records are always kept here as closed and dated extracts. Jira, Confluence, and Service Management are not stores of evidence. The Competence Center Lead is accountable for all the Records.

## Working state

The working state is kept in the [Portfolio](../../portfolio/en/README.md): the Discovery catalog, the Portfolio Backlog and Kanban with the Initiative Briefs, the Roadmap, the Program Backlog and Kanban, the Program Board, the Program Increments, the Calendar, the Teams, the Dashboard, and the projects. The Registry keeps an extract of it in each Registry Snapshot, and a closed copy of each record that a decision approves.

## Living records

Current by nature, and always kept here.

| Record | Where | Holds |
| --- | --- | --- |
| Priorities | [priorities.md](priorities.md) | Strategic Priorities, and references to the Investment Envelopes, Guardrails, and Measures |
| Standards | [standards.md](standards.md) | Architecture standards and Platform requirements |
| Risks and Issues | [risks-and-issues.md](risks-and-issues.md) | Risks, issues, AI Incidents, Exceptions, Findings |
| AI Registry | [ai-registry.md](ai-registry.md) | Each Solution, model, and AI agent; a Record of the Competence Center kept by the Competence Center Lead, which the AI Platform feeds when it can |
| Control Matrix | [control-matrix.md](control-matrix.md) | Each control of the Operating Model 8 with its latest evidence and its status, and the populations for sampling; the objective, type, and test of each control are in the Unit governance guide |
| Appointments | [appointments.md](appointments.md) | The Appointments Record: the map of the Roles to the Holders, the appointment log, the declarations, the access, and the delegations of the Executive Sponsor |

## Evidence records

Closed and dated extracts, always kept here. The Operating Model 8 lists the controls and the record that evidences each.

| Record | Where | Holds |
| --- | --- | --- |
| Decision Log | [decision-log.md](decision-log.md) | Decisions, one line each |
| Decisions | [decisions/](decisions) | The Decision Records, from DR-2026-060 |
| Approved records | `approved/` | The closed copy of each Initiative Brief, Service Agreement, and Outcome Report at the decision that approves or accepts it, named with its identifier and the Decision Record. Created with the first one |
| Reports | [reports/](reports) | Quarterly Reports, named `2026-PIQ4.md` |
| Steering | [steering/](steering) | The Steering Summaries |
| Proposals | `proposals/` | The Proposals to adopt a Solution at scale, and the yearly Proposal of the AI adoption strategy. Created with the first one |
| Acceptance Checklists | `checklists/` | The Acceptance Checklist of each Solution at its release beyond the first users, named `ACL-001.md`. Created with the first one |
| Control Sign-Offs | `sign-offs/` | The decisions of the Control Function Contacts, named `SGN-001.md`. Created with the first one |
| AI Incident Reviews | `incident-reviews/` | The review of each AI Incident, named `AIR-001.md`. Created with the first one |
| Registry Snapshots | `snapshots/` | The closed extract at the close of each Iteration and PI, named `SNP-2026-PIQ4-I10.md`. The first is due at the close of I10 |
| Appointments | [appointments.md](appointments.md) | The Part C log of the Appointments Record is the evidence of every appointment, change, and relief |

Identifiers: PRI-n priority, DR-yyyy-nnn Decision, RI-nnn risk or issue, ARC-nnn and PLT-nnn standards, SGN-nnn Control Sign-Off, AIR-nnn AI Incident Review, ACL-nnn Acceptance Checklist, SNP-yyyy-PIQn-Inn (Iteration close) or SNP-yyyy-PIQn (PI close) Registry Snapshot, PRP-nnn Proposal, AP-nnn appointment entry. The identifiers of the working state (INI, CAP, FT, DEP, MS, AGR, OUT, SOL, PKG) are listed in the Portfolio.

The Registry holds the nil statements that an auditor needs. The Risks and Issues states the AI Incidents and Exceptions to date, and the AI Registry states the uses listed to date.

The Solutions, the Initiatives, and the projects are in the Portfolio (`portfolio/`), and the cadence is in the charter workflows.

The charter baseline and the four Standing Initiatives are approved under [DR-2026-063](decisions/DR-2026-063-approved-english-baseline.md). The Registry continues to show actual work and evidence after that baseline; an operational action is kept here until performed, and is not an unresolved charter provision.
