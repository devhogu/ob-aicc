# Kanban boards

The Portfolio Kanban shows the Initiatives by step of the Portfolio Management Model 5. The Program Kanban shows the Capabilities and Features by state, with the classes of service as lanes: Urgent, High priority, and Normal. The limit on the Initiatives that are Active is [ a number, set by the AICC Lead within the mix that the Executive Sponsor sets, and reviewed at the monthly Steering ] (RI-012). The Limits on Work in Progress of the Program Kanban are [ a number per lane and stage, set by the Team once it has worked a few Iterations ]. Waiting is a state shown as a flag: an item that waits on someone outside AICC carries the flag W and names its Dependency, and a Deferred item is parked in the backlog. The Weekly Review keeps the boards current.

## Portfolio Kanban

| Funnel | Reviewing | Analyzing | Portfolio Backlog | MVP | Implementation | Done |
| --- | --- | --- | --- | --- | --- | --- |
| **Limit** not set | **Limit** not set | **Limit** not set | | **Limit** of Active not set | **Limit** of Active not set | |
|  | INI-002 | | | | INI-001 (development mode, DR-2026-054) | |
|  | INI-006 | | | | | |
|  | INI-004 | | | | | |
|  | INI-003 | | | | | |
|  | INI-007 | | | | | |
|  | INI-008 | | | | | |

## Program Kanban

The columns are the Jira statuses: Backlog holds the states proposed and discovery, with a Deferred item parked there, Ready holds approved, Active holds active and completed, Review holds review, and Done holds accepted and closed. An item that is Waiting stays in its column and carries the Waiting flag (Solution Lifecycle Model 4.2).

| Lane | Backlog (proposed, discovery, deferred) | Ready (approved) | Active | Review | Done |
| --- | --- | --- | --- | --- | --- |
| Urgent | | | | | |
| High priority | | | | | |
| Normal | FT-007, FT-005 (deferred) | | CAP-001 | | FT-001, FT-004, FT-006 |

Waiting, Deferred, Rejected, and Pivoted items: none on the Portfolio Kanban. Cancelled: INI-005, withdrawn and linked to INI-003. Deferred on the Program Kanban: FT-005, FT-007. Cancelled on the Program Kanban: FT-002, FT-003, superseded by the simplification (DR-2026-009).
