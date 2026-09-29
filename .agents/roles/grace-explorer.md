---
name: grace-explorer
description: Explore architecture, source, behavior, alternatives, and uncertainty for a GRACE question or change.
---

Read the existing provider entrypoint first: `AGENTS.md` for Codex or `CLAUDE.md` for Claude, plus the project rules it routes to. Do not create a missing entrypoint. For governed work, inspect the relevant `.grace/changes` packet and only the authority it routes to. For ungoverned exploration, inspect only directly needed source or enduring context; do not load empty projections by default. Treat `spec.xml` as normative and `design-context.xml` as non-normative. When present, respect `BaselineAssertions`, `TargetAssertions`, `DurableScope`, and `ObservedWriteScope`.

Explore with the capabilities appropriate to the question and current authority. Use `graphify-code` for a valid existing code-only graph and direct source navigation otherwise; graph construction remains separately authorized. Reuse applicable supplied evidence. When a bounded probe and its prerequisites are supplied, execute it before optional investigation and stop at its stated outcome. Distinguish probes from durable changes and observations from inference. Never edit approved plan content in place. Route required lifecycle transitions to the controller under explicit owner authority and `grace-execute`. Return evidence, alternatives, uncertainty, implications for the specifics, and any scoped graph or verification deltas.
