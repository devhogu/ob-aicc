---
name: grace-debugger
description: Diagnose a named failing GRACE assertion or verification and repair only an approved bounded scope.
---

Read the existing provider entrypoint first: `AGENTS.md` for Codex or `CLAUDE.md` for Claude, plus the project rules it routes to. Do not create a missing entrypoint. For a governed failure, inspect the relevant `.grace/changes` packet and only the authority it routes to. For a standalone failure, inspect only the failing evidence and directly needed source or enduring context; do not load empty projections by default. Treat `spec.xml` as normative and `design-context.xml` as non-normative. When present, respect `BaselineAssertions`, `TargetAssertions`, `DurableScope`, and `ObservedWriteScope`.

Use `diagnosing-bugs` to establish the symptom, distinguish competing explanations, and select discriminating checks. Reproduce and isolate the named failure when possible; bounded logs and source inspection are valid when it is not. Implement only when the specifics authorize repair, and use `behavioral-testing` when a durable regression check is in scope. Return missing specifics instead of silently narrowing future work. Never edit approved plan content in place. Route required lifecycle transitions to the controller under explicit owner authority and `grace-execute`. Return root cause, response, original-scenario evidence, uncertainty, and scoped graph or verification deltas.
