---
name: grace-execute
description: Execute or resume an approved GRACE 4 GraceChangePlan with recovery-aware preflight and centralized durable apply. Select direct execution or an authorized durable workflow when continuity or handoffs warrant it.
---

<skill>
<preflight>
Require one active bundle with approved, identity-matched `spec.xml` and `plan.xml`. Approved plans are immutable. Read context, projections, assertions, scopes, task dependencies, and verification before editing. Reject phase-incompatible plans before writes: `MustPassCommand` must be leaf project evidence, and neither target assertions nor post-write task verification may invoke `--assertions current` or nest GRACE lifecycle commands. Supersede and replan instead of editing an approved conflict in place.
</preflight>

<assertion_commands>
- Active-baseline preflight before observed writes: `grace lint --path PROJECT --assertions current`
- Selected baseline: `grace lint --path PROJECT --change C-ID --assertions baseline` (add `--run-commands` when the baseline declares `MustPassCommand`)
- Selected target without commands: `grace lint --path PROJECT --change C-ID --assertions target`
- Selected target with command evidence: `grace lint --path PROJECT --change C-ID --assertions target --run-commands`
- Final end-state validation: `grace lint --path PROJECT --change C-ID --assertions final` (add `--run-commands` when the target declares `MustPassCommand`)
- Parallel preflight: `grace lint --path PROJECT --parallel-preflight`
</assertion_commands>

<mode_selection>
Reuse the approved plan or owner's execution-mode choice. Otherwise use
sequential execution; do not ask for a scheduling choice when that safe default
suffices. Parallel-safe execution requires explicit authority and a passing
parallel preflight. Workers never mutate approved plans; durable `.grace`
changes are applied centrally after observed work verifies.
</mode_selection>

<workflow_selection>
For background continuity, explicit handoffs, or repository workflow setup,
read [development workflow guidance](references/development-workflows.md).
It provides scenario selection and an optional BB template, not new lifecycle
authority. Keep small coherent work direct. Propose orchestration for a concrete
benefit; launch only under applicable explicit orchestration authority.
</workflow_selection>

<authority_reuse>
This skill owns execution recovery and lifecycle-approval reuse. Reuse an
explicit authorization for the same change, action, scope, and conditions;
record which instruction supplies it. Approval to implement alone is not
approval to apply/archive, commit, push, deploy, or revert. If the owner already
authorized apply after verification, perform it only after fresh final evidence
passes; do not ask for the same permission again. If that authority is missing,
revoked, or conditional on a new owner decision, stop before that action and ask.
No controller can waive approved-plan immutability: changed approved content
requires an explicitly authorized successor, not an in-place edit.
</authority_reuse>

<recovery_decision_table>
| state | required action |
| clean-to-start | Run selected baseline, then execute tasks. |
| expected-partial-observed-writes | Match the diff to approved tasks and prior baseline evidence, verify completed work, and resume unfinished tasks within continuing execution authority. Do not revert or request the same permission merely because progress exists. |
| expected-durable-reconciliation | Confirm changes are the approved central graph, verification, or context deltas; verify completed tasks and remaining target obligations, then continue to final validation in this change. |
| invalidated-approved-assumptions | Stop the affected execution. Report the invalidated assertion or scope and propose an authorized successor; never rewrite the approved plan to fit drift. |
| target-already-satisfied | Do not reimplement. Verify the target and final state with declared command evidence, reconcile only missing approved durable deltas, then apply/archive only under applicable explicit authority. |
| unsafe-unknown-drift | Hard stop and report unexplained files. |
</recovery_decision_table>

An in-scope file is not automatically expected progress. Establish task
identity, actual diff, prior baseline evidence, and remaining obligations from
available artifacts or bounded inspection. Missing evidence is uncertainty,
not permission to assume or revert. Preserve unrelated work. Do not rerun
`current` or the pre-write baseline as a recovery gate after known authorized
writes have superseded it; keep the original assertions immutable and use
completed-task evidence plus target/final checks at the appropriate stage.

<execution_rules>
1. On a clean start, run the selected baseline before implementation, including explicit `--run-commands` when its assertions declare `MustPassCommand`. On recovery, classify the existing state using the table above before any further writes.
2. Execute one dependency-ready task or one verified parallel-safe batch at a time.
3. Use only the focused engineering capabilities selected by the task: for
   example `diagnosing-bugs` for an unresolved failure, `codebase-design` for
   an interface decision, and `behavioral-testing` for changed behavior. These
   methods do not expand the approved scope or authority.
4. Run each task's acceptance and verification immediately.
5. Apply approved durable context, graph, and verification changes centrally.
6. Reconcile durable state, run leaf plan gates, then run selected `--assertions final` as the outermost lifecycle gate, including `--run-commands` when `MustPassCommand` is declared. Final mode performs full project lint, evaluates the selected target, keeps unrelated approved baselines active, and does not re-evaluate the selected plan's superseded baseline.
7. After fresh end-state evidence passes, confirm applicable explicit apply authority under the authority-reuse rule; ask only if it is missing.
8. Only then set spec and plan to `applied` and archive the complete bundle.
9. Never edit approved assertions/scopes/tasks in place, bypass stale evidence, or continue through unknown drift.
</execution_rules>
</skill>
