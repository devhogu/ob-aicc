---
name: codebase-design
description: Improve the design of code modules and interfaces when callers know too much, responsibilities are misplaced, change is scattered, or a refactor needs an architectural decision. Do not use for a purely mechanical rename or formatting-only change.
---

# Codebase design

Improve a real consumer path by placing knowledge and responsibility with the
component that naturally owns them. The outcome is easier correct use, not a
particular number of layers or abstractions.

## Design method

1. Trace the current caller-to-outcome path. When a valid code-only Graphify
   graph already exists, use `graphify-code` for structural navigation. If it
   does not exist, inspect the relevant source directly; graph construction is
   a separate authorized action.
2. List what each caller must know: ordering, configuration, error recovery,
   data shape, policy, persistence, or provider details.
3. Identify the natural owner for that knowledge and the smallest interface
   that lets callers express intent without reconstructing internal rules.
4. Compare the proposal with existing maintained packages, SDKs, protocols,
   and repository utilities. Keep custom code for actual domain semantics or a
   demonstrated integration gap.
5. Preserve necessary authorization, transaction, consistency, deployment,
   and trust boundaries. Do not merge them merely to reduce indirection.
6. Validate the changed interface through a real caller and protect observable
   behavior with existing or justified new tests.

Add an adapter or abstraction when it has a current consumer, isolates real
volatility, or removes duplicated caller knowledge. A speculative future
consumer is not sufficient evidence.

## Completion

Return the real path, caller knowledge removed, responsibility owner, retained
boundaries, reused foundations, migration impact, and behavioral evidence.
