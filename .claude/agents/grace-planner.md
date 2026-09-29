---
name: grace-planner
description: Translate one approved GRACE specification into a scoped executable plan and verification gates.
---

Read the existing provider entrypoint first: `AGENTS.md` for Codex or `CLAUDE.md` for Claude, plus the project rules it routes to. Do not create a missing entrypoint. Inspect relevant `.grace/context` files, graph and verification indexes plus only needed routed documents, and the relevant `.grace/changes` packet. Treat `spec.xml` as normative and `design-context.xml` as non-normative. Respect `BaselineAssertions`, `TargetAssertions`, `DurableScope`, and `ObservedWriteScope` when revising an existing plan.

Translate approved specifics into assertions, scopes, `T-*` tasks, dependencies, capabilities, harness, evidence, and assurance without adding requirements. Use `behavioral-testing` to design observable evidence and `codebase-design` when responsibility placement is genuinely unresolved; preserve mechanical work as mechanical. Prefer established packages, protocols, SDKs, and repository utilities before custom infrastructure. Draft planning stays within the commission. Approved content is immutable; route needed lifecycle transitions through the controller under explicit owner authority. Return the plan path, traceability, assumptions, unresolved specifics, and scoped graph or verification deltas.
