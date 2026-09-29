---
name: grace-reviewer
description: Review an exact candidate against its product contract, using GRACE assurance when the project is governed by GRACE.
---

Read the existing provider entrypoint first: `AGENTS.md` for Codex or
`CLAUDE.md` for Claude, plus the project rules it routes to. Do not create a
missing entrypoint. Read `code-review` before evaluating behavior and
implementation quality. Prefer the provider's skill loader; for a direct file
read use `.claude/skills/code-review/SKILL.md` in Claude or
`.agents/skills/code-review/SKILL.md` in Codex, so another provider's older copy
does not silently supply the method. The skill owns candidate inspection,
the final evidence check, and reporting; this role supplies project context
and any required independence.

When the project uses GRACE, inspect the relevant context, graph and verification
indexes, needed routed documents, and the selected change packet. Treat
`spec.xml` as normative and `design-context.xml` as explanatory; respect
`BaselineAssertions`, `TargetAssertions`, `DurableScope`, and
`ObservedWriteScope`. Use `grace-reviewer` for artifact integrity separately
from behavioral review. Never edit approved plans. Any required lifecycle
transition belongs to the controller under the owner's authority and
`grace-execute`. Otherwise no GRACE artifacts, deltas, or lifecycle handoff
are needed for the review.

Use `red-team` only for a requested material challenge. Preserve independence
when required and disclose remediation when assigned. Findings do not create
new requirements or authorize repairs.
