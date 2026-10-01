# Kanban boards

The Portfolio Kanban shows the Initiatives by state. The Program Kanban shows the Epics and Features by state, with the classes of service
as lanes: Urgent, High priority, and Normal. The Limits on Work in Progress are [ a number per lane and stage, set by the Team once it has worked a few ITs ] (RI-012). An item that waits on someone outside
AICC is marked with W and its Dependency, and a Deferred item is parked in the backlog. The Weekly Review keeps the boards current.

## Portfolio Kanban

| Proposed | Discovery | Approved | Active | Review | Closed |
| --- | --- | --- | --- | --- | --- |
| **Limit** not set | **Limit** not set | **Limit** not set | **Limit** not set | **Limit** not set | |
|  | INI-002 | | INI-001 | | |
|  | INI-006 | | | | |
|  | INI-004 | | | | |
|  | INI-003 | | | | |
|  | INI-007 | | | | |
|  | INI-008 | | | | |

## Program Kanban

The columns are the Jira statuses: Backlog holds the states proposed, discovery, and deferred, Ready holds approved, Active holds active and waiting, Review holds completed and review, and Done holds accepted and closed.

| Lane | Backlog (proposed, discovery, deferred) | Ready (approved) | Active | Review | Done |
| --- | --- | --- | --- | --- | --- |
| Urgent | | | | | |
| High priority | | | | | |
| Normal | FT-007, FT-005 (deferred) | | EP-001 | | FT-001, FT-002, FT-003, FT-004, FT-006 |

Waiting, Deferred, Rejected, and Cancelled items: none on the Portfolio Kanban. Pivoted: INI-005, merged into INI-003. Deferred on the Program Kanban: FT-005, FT-007.
