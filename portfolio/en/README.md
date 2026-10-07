# Portfolio

The Portfolio is the persistent source of truth for what the Competence Center offers and for the working state of its portfolio and program, from the Discovery catalog to delivery (Operating Model 7.1). It holds the catalog of the Solutions and the Packages, the Discovery catalog, the Portfolio Backlog and Kanban with the Initiative Briefs, the Program Backlog and Kanban, the plans of the Program Increments, and the register of the projects. It holds no figures of the Bank, no data, no documents of the functions, and no code. The decisions and the evidence are in the Registry (`registry/`), and the rules are in the charter (`charter/`).

## What is kept here

| Level | Record | Where | Holds |
| --- | --- | --- | --- |
| Catalog | Solutions | [solutions/](solutions/SOL-001-fpa-board-reporting-pipeline.md) | One Solution Definition for each Solution, from the Solution Definition Template, with its type (Service, Product, or Experiment), its receiver, and its state |
| Catalog | Packages | [packages.md](packages.md), [packages/](packages.md) | The catalog of the Packages, and one Package Definition for each |
| Catalog | Adopted Solutions | `adopted-solutions/` | One entry for each Solution that others deliver and the Competence Center oversees. Created with the first one |
| Discovery | Discovery catalog | [discovery/](discovery/README.md) | The scenarios by service area and capability, which feed the Funnel |
| Portfolio | Portfolio Backlog | [portfolio-backlog.md](portfolio-backlog.md) | The one ranked list of the Initiatives, with the service area, state, Stage, scores, and the date of each state |
| Portfolio | Initiatives | [initiatives/](initiatives/README.md) | One folder for each: `INI-nnn-short-title/` with its Initiative Brief, and its Service Agreements and Outcome Reports while they are worked on |
| Portfolio | Kanban boards | [board.md](board.md) | The Portfolio Kanban by step and the Program Kanban by state, with lanes and Limits on Work in Progress |
| Portfolio | Roadmap | [roadmap.md](roadmap.md) | The Roadmap by Program Increment, in three horizons, and the Milestones |
| Program | Program Backlog | [program-backlog.md](program-backlog.md) | The ranked Capabilities and Features, each with its parent, service area, class of service, state, and the date of each state |
| Program | Program Board | [dependencies.md](dependencies.md) | The Capabilities, Features, and Milestones by Iteration, and the Dependencies of each item |
| Program | Program Increments | [pi/](pi/2026-PIQ4/objectives.md) | For each: PI Objectives, monthly Iterations with their Iteration Backlogs and Weekly Review notes, and the IP week |
| Program | Calendar | [calendar.md](calendar.md) | Program Increments, Iterations, weeks, and the blocked and gray days |
| Program | Teams | [teams.md](teams.md) | The Teams, members, and the Hats |
| Program | Dashboard | [dashboard.md](dashboard.md) | The state of the Program Increment, flow, Dependencies, risks, and Measures |
| Delivery | Projects | [projects/](projects/README.md) | The register of the projects: for each Initiative in delivery, its project documents |

There is one Portfolio Backlog and Kanban and one Program Backlog and Kanban, with one rank and one set of limits (Portfolio Management Model 5.4, 6.5; Solution Lifecycle Model 4.2). The service area of the Business Model 4.5 (Advise and formulate, Build and run, Enablement, Assurance) is a field of each item, not a separate backlog. Each item keeps one path for its whole life; its state is a field with the date of each state (Portfolio Management Model 9.4), and no folder stands for a state.

## The Portfolio, the Registry, and Jira

| What | Source of truth | Jira and Confluence |
| --- | --- | --- |
| Initiative: definition, business case, service area, rank, state and its dates | The Portfolio; each gate decision also in the Registry | A mirror of the Initiative |
| Capability and Feature: definition, parent, acceptance criteria, class of service, admission, acceptance | The Portfolio | A mirror: the Capability as an Epic, the Feature as an issue |
| Progress of a Feature between Weekly Reviews: Active, Completed, Waiting | Jira; recorded in the Portfolio at each Weekly Review, and at once at a gate | Owns it day to day |
| Stories, Spikes, Tasks, and Bugs | Jira only | The team backlogs and boards |
| Decisions, approvals, sign-offs, acceptances, Outcome Reports, Registry Snapshots | The Registry, as closed and dated extracts | References only |

A gate decision is recorded in the Portfolio and in the Registry first, and only then in Jira; Jira never decides a gate. At each Weekly Review the Competence Center Lead records the progress of the Features from Jira in the Portfolio, and corrects and notes any difference. At each decision a closed and dated extract goes from the Portfolio to the Registry, and the Registry is not changed after the fact (Operating Model 7.2, 7.4).

The Portfolio is kept in a repository with a protected main branch and restricted visibility, and its history is not rewritten. Only the Competence Center Lead and the named deputy merge to the main branch; internal audit reads it (Operating Model 7.4, 7.5). It is promoted to the corporate share at `aicc/portfolio/`.

Identifiers: SOL-nnn Solution, PKG-nnn Package, INI-nnn Initiative, CAP-nnn Capability, FT-nnn Feature, DEP-nnn Dependency, MS-nnn Milestone, AGR-nnn Service Agreement, OUT-nnn Outcome Report. The identifiers of the Registry are in its [README](../../registry/en/README.md).
