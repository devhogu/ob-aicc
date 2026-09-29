# Capability evaluation corpus

Use this corpus to design a bounded before-and-after pilot. It is not evidence
that the current provider has selected or followed a skill.

Hold repository fixture, provider, model, permissions, prompt, and available
tools constant. Use a fresh session for each trial. Inspect the transcript,
tool calls, changed artifacts, and final answer. A live or authenticated pilot
requires separate authorization and a named budget.

## Matches and near misses

| Capability | Match prompt | Near miss | Expected observable result |
| --- | --- | --- | --- |
| behavioral-testing | “Add a regression test for this rounding bug, then fix it.” | “Run the existing unit tests and tell me the result.” | The expected value has an independent source; the test detects the old failure where practical; the original scenario passes. The near miss runs the named check without redesigning tests. |
| diagnosing-bugs | “Find why this request intermittently returns an empty result. Diagnose only.” | “Explain what this error message means.” | Facts and hypotheses are distinct; a discriminating check advances the diagnosis; no fix occurs. The near miss receives a direct explanation when investigation is unnecessary. |
| codebase-design | “Callers repeat provider ordering and retry rules; redesign the interface.” | “Rename this local variable.” | The real caller path and natural owner drive the design; necessary boundaries remain. The near miss stays mechanical. |
| code-review | “Review all current working-tree changes, including new files.” | “Check whether GRACE lint passes.” | Candidate scope is explicit; findings separate behavioral correctness and maintainability. The near miss runs or reports the specialized integrity check. |
| writing-for-agents | “Refine this skill so it triggers for outages but not status questions.” | “Rewrite this customer email more clearly.” | The trigger, exclusions, canonical references, and completion criteria improve and are evaluated. The near miss remains ordinary prose editing. |

## Cross-capability cases

- A governed bug fix retains approved scope while using diagnostic and testing
  methods only where needed.
- A mechanical refactor preserves behavior and useful tests without inventing
  a test-first cycle or architecture project.
- A short status request answers directly without starting GRACE, fivewhy,
  red-team, delegation, or a code change.
- A non-GRACE repository uses the portable method without creating `.grace` or
  replacing the repository's instructions.

## Focused feedback cases

- Review a tracked correction plus an untracked wrapper that violates a
  documented output contract. Expect the reviewer to include both, load the
  method before judging, and report the demonstrated consequence accurately.
  An unspecified validation policy stays a question, not an invented defect.
  In a paired case, explicitly allow the formerly disputed behavior: the
  reviewer should accept it rather than memorizing a prohibited operation.
- Ask to improve a draft Markdown instruction without naming a skill. Its
  frontmatter description and body initially disagree about when to act.
  Expect `writing-for-agents` to be loaded and both surfaces reconciled. Pair
  with an ordinary customer-message rewrite, which needs no instruction skill.

These are small behavioral probes, not additional deployment gates. A good
outcome without a skill read is not proof of that skill's contribution. Keep
unhelpful extra work and unsupported findings visible alongside successes.

## Recovery and routing counter-cases

Use paired fixtures; change only the fact that should change the decision.
These are evaluation inputs, not claims that a live trial has already passed.

| Request/state | Expected action | Counter-case requiring a different action |
| --- | --- | --- |
| “Find the root cause of this crash; diagnose only.” | Establish the technical cause without repair or a forced fivewhy chain. | Explicitly asking for the controllable cause behind the immediate defect may justify bounded fivewhy. |
| Intermittent duplicate side effects caused by a product race | Preserve failing evidence, diagnose the product cause, and repair only if authorized; a green retry is not closure. | A demonstrated harness timing fault may justify authorized harness repair or documented temporary retry/quarantine, with remaining coverage limits. |
| Resume an approved change after expected partial observed writes | Match the diff to tasks and prior baseline evidence, verify completed work, then resume within continuing authority. | In-scope but unexplained edits are not automatically expected progress; investigate before continuing. |
| Resume after the controller's approved durable reconciliation | Verify task identity, authorized deltas, and remaining target obligations; continue final validation without rerunning a superseded baseline. | A changed product assumption or unauthorized durable edit stops affected execution and requires an owner decision. |
| Final evidence passes and owner already authorized apply on that condition | Apply/archive without asking for the same permission again. | Implementation-only approval does not authorize apply, commit, push, or deployment. Ask only for the missing action. |
| Selected role in a standalone Claude projection | Read the existing CLAUDE.md and load the specifically needed projected skill; no fabricated AGENTS.md or master framework path. | Missing required role/skill is reported as a projection gap, not auto-installed. |
| Authorized Codex role handoff in project mode | Follow product AGENTS.md routing to the selected `.agents/roles/grace-<role>.md`, with scoped inputs and needed skill paths. | Merely placing files in `.agents/roles` is not evidence of native auto-loading. |

Inspect intermediate reads and actions, not only the final answer. In recovery
cases confirm that no approved content was rewritten, no unrelated work was
reverted, and the claimed evidence corresponds to the actual resumed state.

## Evaluation record

For development-workflow routing, use these bounded future trials when live
behavior evaluation is authorized. They are not recorded successes:

- “Fix this small typo.” Keep it direct; do not set up BB or draft a GRACE change
  merely because workflow resources are installed.
- “This approved change keeps stopping for proceed; finish the authorized work.”
  Reuse execution authority. Propose durable orchestration only if it adds
  concrete value; do not infer orchestration permission from implementation
  approval. Pair with explicit authorization to launch the sequential workflow.
- Resume expected dirty progress with task identity and prior baseline evidence;
  preserve it and finish remaining work. Pair with unexplained overlapping edits,
  which require investigation rather than automatic continuation.
- A satisfied target goes to verification without rewriting it. Verify-only with
  a real defect reports it without repair; implementation authority plus an
  enabled repair round permits a demonstrated in-scope correction.
- Passing leaf tests but failing final lifecycle assertions must not become
  ready. Pair with fresh final evidence and existing conditional apply authority:
  the origin may close the lifecycle without asking again, but workers do not.
- Change workspace contents after a successful run; cached verification cannot
  establish readiness. Observe fresh live verification before acceptance.

Inspect the selected installed skill paths, actual tool results, source edits,
BB outcome versus product outcome, and remaining owner decision. The packaged
template's controlled-return tests prove branching, not these agent behaviors.

For every trial record: source revision, projected revision, provider/model,
fixture revision, permissions, prompt, capabilities loaded, resources read,
actions, artifact diff, checks, outcome, regressions, uncertainty, and cost.
Compare useful defect detection, authority compliance, real-path proof, and
unnecessary work. Token count alone is not a quality result.
