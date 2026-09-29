# GRACE 4 Project Engineering Protocol

## Keywords
aicc, o-bank, kyrgyzstan, genai, ai-competence-center, portal, static-site, knowledge-base, roadmap, strategy

## Annotation
Source repository for the static HTML portal of the AI Competence Center (AICC) at O!Bank Kyrgyzstan. The portal projects the center's strategy, statement of intent, roadmap, knowledge base, and lifecycle-management processes. This repository develops and shapes the portal; clean static output is rendered to a separate deployment repository, which is never a second source.

## GRACE 4 Source of Truth

This project uses the GRACE 4 `.grace` artifact model.

- Product and technical context: `.grace/context/*.xml`
- Current graph projection source: `.grace/graph/index.xml` plus routed graph documents such as `.grace/graph/main.xml`
- Current verification projection source: `.grace/verification/index.xml` plus routed verification documents such as `.grace/verification/main.xml`
- Active work: `.grace/changes/active/C-*/spec.xml` and `.grace/changes/active/C-*/plan.xml`
- Completed or terminal work: `.grace/changes/archive/C-*/*`

Legacy `docs/*.xml` files are not GRACE 4 state. If legacy GRACE 3 docs appear, use `grace-migrate`; do not silently validate, convert, or delete them.

## Workflow Rules

1. Do not implement source behavior before an approved active `GraceChangeSpec` and `GraceChangePlan` exist, unless the user explicitly requests a small direct fix.
2. Treat `spec.xml` as normative. Treat `design-context.xml` as explanatory memory only.
3. Before execution, check `BaselineAssertions`, `TargetAssertions`, `DurableScope`, and `ObservedWriteScope` in the plan.
4. Update durable `.grace` graph and verification state only as part of the approved change lifecycle.
5. Never store transient run state by mutating approved XML statuses. Runtime states are derived from current files, assertions, and scopes.

## Semantic Anchor Rules

- GRACE semantic anchors are XML tags, never attributes: use `<M-EXAMPLE />`, not `<Module ref="M-EXAMPLE" />`.
- Module IDs use `M-*`; data-flow IDs use `DF-*`; graph document wrappers use `GD-*`; verification entries use deterministic `V-M-*`; verification document wrappers use `VD-*`; change bundles use `C-*`.
- Code-level semantic markup remains grep-stable: `START_MODULE_CONTRACT`, `START_MODULE_MAP`, `START_CONTRACT:`, `START_BLOCK_`, and `START_CHANGE_SUMMARY`.

## Grep-First Navigation

1. Locate module ownership through `.grace/graph/index.xml`, then open the routed graph document.
2. Locate verification through `.grace/verification/index.xml`, then open the routed verification document.
3. Locate active work through `.grace/changes/active/C-*`.
4. Use file-local `LINKS:` fields and `START_BLOCK_` anchors to narrow code reads before loading whole files.

## CLI Checks

- `grace lint --path .` validates `.grace` grammar, projections, assertions, lifecycle locations, and scope overlaps.
- `grace status --path .` summarizes durable and operational GRACE 4 health.
- `grace module`, `grace verification`, and `grace file` navigate graph, verification, and file-local anchors.

## File-Local Markup Reference

```ts
// START_MODULE_CONTRACT
//   PURPOSE: [What this module does]
//   SCOPE: [Bounded responsibility]
//   DEPENDS: [M-* dependencies or none]
//   LINKS: [Related M-* and V-M-* anchors]
// END_MODULE_CONTRACT
//
// START_MODULE_MAP
//   exportedSymbol - one-line responsibility
// END_MODULE_MAP
//
// START_CONTRACT: functionName
//   PURPOSE: [What it does]
//   INPUTS: { paramName: Type - description }
//   OUTPUTS: { ReturnType - description }
//   SIDE_EFFECTS: [External state changes or none]
// END_CONTRACT: functionName
//
// START_BLOCK_EXAMPLE
// ... implementation slice ...
// END_BLOCK_EXAMPLE
```

---

# Generated dev-pipe Codex projection

This standalone entrypoint and the individual files recorded in
`.agents/dev-pipe-manifest.tsv` are generated from dev-pipe. Change those
sources in dev-pipe and intentionally project again. Unrelated custom skills,
roles, and provider configuration remain product-owned; the manifest does not
claim the entire provider directory.

## Select focused capabilities

Use only a skill whose trigger matches the current work. Skills are available
under `.agents/skills/<name>/SKILL.md`. They are optional capabilities, not a
mandatory sequence. This package supplies 24 skills and six optional roles.
When a selected role or skill names another needed method, load its entry
through the provider's available skill mechanism or read the path above.
Do not treat a name mention as loaded content. Report a missing capability
instead of installing it or inventing a source path.

For a code review, read `code-review` before evaluating the candidate. For
changes to instructions that guide an assistant, including draft Markdown,
read `writing-for-agents` before editing. Ordinary prose rewrites, running an
existing check, and routine status requests stay direct tasks.

- Use `diagnosing-bugs` for evidence-led diagnosis, `behavioral-testing` for
  independently justified tests, `codebase-design` for responsibility/interface
  decisions, `code-review` for implementation review, and `writing-for-agents`
  for agent instructions. They do not create authority or extra stages.
- Use the GRACE skills for governed project context, specifications, plans,
  execution, verification, review, migration, repair, and navigation.
- Use `outcome-tasking` to bind the real actor, consumer, path, missing edge,
  authority, and proof before material work.
- Use `fivewhy` for a bounded causal spine and `red-team` for an independent
  challenge of a concrete proposal or candidate.
- Use only `graphify-code` for Graphify work from this projection. Query an
  existing code-only graph first. Build or update only when explicitly
  authorized; do not perform semantic document or media extraction.

Role documents are under `.agents/roles/`. Select controller, debugger,
explorer, planner, reviewer, or worker explicitly when bounded delegation is
useful. This guidance does not claim that Codex auto-loads that directory.

If the target repository uses GRACE 4, treat its local `.grace/` as project
authority: context, approved specification and plan, bounded execution,
verification, then apply/archive. A deployed skill does not impose GRACE on an
unrelated task or create a standing management layer. `grace-execute` owns
execution recovery and lifecycle-approval reuse; no role may edit approved
plan content in place.

This projection never updates itself. Deployment requires an intentional
dev-pipe command with this target named explicitly.

When approved work would benefit from background continuity or explicit
handoffs, or when setting up repository workflows, read the installed
[development workflow guide](.agents/skills/grace-execute/references/development-workflows.md).
It routes scenarios and supplies an optional BB starter. Small tasks stay
direct; creating or running orchestration needs applicable explicit authority.
