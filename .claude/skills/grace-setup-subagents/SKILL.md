---
name: grace-setup-subagents
description: Create GRACE 4 worker and reviewer subagent presets that understand .grace artifacts, scopes, assertions, and verification evidence.
---

<skill>
<subagent_requirements>
Generated subagents must be told to:

- read `.grace/context`, `.grace/graph`, `.grace/verification`, and relevant `.grace/changes` packets explicitly;
- treat `spec.xml` as normative and design context as non-normative;
- respect `DurableScope`, `ObservedWriteScope`, `BaselineAssertions`, and `TargetAssertions`;
- never edit approved plan content in place; route lifecycle transitions to the controller under explicit owner authority and `grace-execute`;
- return verification evidence and scoped graph/verification deltas.
</subagent_requirements>

<role_routing>
The six role identities are controller, debugger, explorer, planner, reviewer,
and worker, with filenames `grace-<role>.md`. In a consuming repository resolve
them under `.agents/roles/` for Codex guidance or `.claude/agents/` for Claude.
Only in the dev-pipe master are their sources under `framework/roles/`.
Read the selected role and give it the applicable provider entrypoint, relevant
authority paths, scoped task, and needed skill names/paths. If a required role
or skill is absent, report the missing projection; do not invent or install it.
Codex role files require an explicit instruction/handoff path, not a claim of
native auto-loading. Do not load all skills or roles by default.

Read a specialist template only when the assignment needs that narrower behavior:

- [module implementer](references/roles/module-implementer.md) for one planned module slice;
- [fixer](references/roles/fixer.md) for one authorized failure packet;
- [contract reviewer](references/roles/contract-reviewer.md) for module-contract conformance;
- [verification reviewer](references/roles/verification-reviewer.md) for evidence quality.

Specialist templates refine a worker, debugger, or reviewer assignment. They
do not replace the normative spec, expand scope, create delegation authority,
or establish four additional standing roles.
</role_routing>
</skill>
