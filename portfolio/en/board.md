# Kanban boards

The Portfolio Kanban shows the Initiatives by step of the Portfolio Management Model 5. The Program Kanban shows the Capabilities and Features by state, with the classes of service as lanes: Urgent, High priority, and Normal. The limit on the Initiatives that are Active is set by the Competence Center Lead within the mix that the Executive Sponsor sets, and is reviewed at the monthly Steering (Portfolio Management Model 5.4). The Limits on Work in Progress of the Program Kanban apply to the states, the lanes, and each Domain (Solution Lifecycle Model 4.2). Waiting is a state shown as a flag: an item that waits on someone outside the Competence Center carries the flag W and names its Dependency, and a Deferred item is parked in the backlog. The Weekly Review keeps the boards current.

## Portfolio Kanban

| Funnel | Reviewing | Analyzing | Portfolio Backlog | MVP | Implementation | Done |
| --- | --- | --- | --- | --- | --- | --- |
| No WIP cap: intake queue | No WIP cap: discovery queue | No WIP cap: business-case queue | No WIP cap: approved queue | Shared Active limit: 1 | Shared Active limit: 1 | No WIP cap: completed work |
| INI-013 | INI-002 | | | | | |
|  | INI-006 | | | | | |
|  | INI-004 | | | | | |
|  | INI-003 | | | | | |
|  | INI-007 | | | | | |
|  | INI-008 | | | | | |

## Standing Initiatives

These Standing Initiatives are Approved under DR-2026-063 and sit outside the ordinary portfolio Kanban. They become Active when the first run-rate Feature is pulled. No Feature has been admitted under them at establishment.

| Initiative | Service area | State | Approval |
| --- | --- | --- | --- |
| INI-009 | Advise and formulate | Approved | 2026-10-03; DR-2026-063 |
| INI-010 | Build and run | Approved | 2026-10-03; DR-2026-063 |
| INI-011 | Enablement | Approved | 2026-10-03; DR-2026-063 |
| INI-012 | Assurance | Approved | 2026-10-03; DR-2026-063 |

## Program Kanban

The columns are the Jira statuses: Backlog holds the states proposed and discovery, with a Deferred item parked there, Ready holds approved, Active holds active and completed, Review holds review, and Done holds accepted and closed. An item that is Waiting stays in its column and carries the Waiting flag (Solution Lifecycle Model 4.2).

| Lane | Backlog (proposed, discovery, deferred) | Ready (approved) | Active | Review | Done |
| --- | --- | --- | --- | --- | --- |
| Limit | No WIP cap: intake and deferred queue | 2 Features; 1 Capability | Shared in-progress limit: 1 Feature and 1 Capability | Shares the in-progress limit | No WIP cap: completed work |
| Urgent | | | | | |
| High priority | | | | | |
| Normal | | | | | |

Waiting, Deferred, Rejected, and Pivoted items: none.

## Initial operating limits

DR-2026-063 establishes the limits for the existing one-person the Competence Center Team. One Feature in progress is the total across ordinary delivery and all four Standing Initiatives, across every lane and Domain. Active, Completed, Review, and Waiting after work starts share that single place. A blocked Feature continues to use it. A Capability has a separate limit of one in progress and one Ready because it groups Features. The portfolio limit of one Active ordinary Initiative is shared across MVP and Implementation; Standing Initiatives are excluded.

The four service areas share capacity in the order of the ranked Program Backlog. There is no reserved allocation per area and no additional headcount or funding. An urgent request is reordered within the same limits. The Competence Center Lead reviews the limits at monthly Steering, and the Executive Sponsor reviews the mix and Standing Initiatives at quarterly Steering. These are adopted initial settings; a later change is recorded through the normal cadence.
