# Choosing and using development workflows

Read this when selecting durable execution for an approved change, setting up
repository workflow guidance, or recovering a BB run. It is not a prerequisite
for routine edits, status, or running an existing check.

## Purpose and selection

Help a repository agent carry an authorized development outcome to its real
terminal state without requiring the user to manage each handoff. A workflow
automates dispatch and branching; skills supply methods, the repository owns
requirements, and the responsible owner retains decisions and authority.

Choose the smallest execution shape that materially helps. Do not create a
workflow merely because BB is available, a role exists, or a task uses several
skills. Repeated unnecessary requests to proceed should first be corrected by
reusing existing authority; orchestration is useful when durable continuity or
handoffs add value, not as a substitute for following instructions.

| Situation | Appropriate shape | Entry and terminal boundary |
| --- | --- | --- |
| Small coherent edit, explanation, status, or existing check | Direct agent work | Finish the requested outcome without workflow setup. |
| Material outcome or design is unresolved | Outcome clarification and, when needed, bounded design exploration | Return the owner-decidable question or approved specification/plan. Do not start implementation from exploration conclusions alone. |
| Approved change benefits from background continuity or explicit handoff | Execute/resume approved change | Classify current state, finish remaining tasks, verify, and return ready, blocked, or needs-decision. |
| Change is implemented or the owner asks only for verification | Verify-only | Inspect actual candidate and evidence without source repairs; report readiness or concrete remaining obligations. |
| Independent design alternatives or separate review dimensions are explicitly useful and authorized | Bounded read-only parallel work | Preserve independent first submissions and return differences to the decision owner. No vote-based automatic approval. |
| Approved implementation has disjoint safe write scopes | Explicit parallel-safe plan | Use GRACE parallel preflight and one integration owner. A BB parallel call does not make shared files safe. |

Only execute/resume and verify-only need a supplied executable starter now.
The other scenarios explain selection; they do not justify a catalog of unused
scripts. Use the installed BB workflow instructions for runtime-specific
authoring. Do not duplicate those API instructions in each product.

Agents should recognize these scenarios from ordinary requests. Explain the
specific benefit and boundary when proposing orchestration, and obtain or cite
applicable explicit authorization before launch. Installing guidance does not
authorize background workers. A user should not need to name this guide.

## Method obligations, not a compulsory agent sequence

The development path remains: establish intent and current reality; obtain
the required specification/plan approvals; implement within scope; verify the
actual result; reconcile durable state; close under applicable authority.

Enter at the stage the project has reached. Do not reproduce approved planning,
rerun superseded pre-write assertions as a recovery gate, or reimplement a
satisfied target just to fill workflow phases. Load `grace-execute` for those
decisions, and focused engineering skills only when the work needs them.

A phase can contain several method obligations, and one agent can perform
several phases. Conversely, a second agent is not automatically an independent
reviewer. Verification-plus-repair is useful but should be named honestly.

## One accountable owner

The origin agent/controller selects the scenario, confirms the actual target,
installed capability paths and source identity, and gives workers a bounded
commission using `outcome-tasking` where appropriate. It receives the final
result, checks evidence, and returns one integrated report. Do not add a
standing manager or require another agent solely to aggregate outputs.

Worker instructions identify:

- repository, approved change, and current candidate/worktree;
- applicable authorization and protected work;
- selected methods and real acceptance evidence;
- permitted effects, effort bound, and stop condition.

The template is not a second plan. Task dependencies, write scopes, tests, and
acceptance criteria come from the approved project artifacts. Missing installed
skills are deployment gaps, not permission to fetch a different host copy.

## Execute/resume starter contract

Use the [BB template](../assets/execute-approved-change.js) only for one active,
approved GRACE change. Non-GRACE tasks should not manufacture GRACE artifacts
to use it.

Inputs are `repoPath` (absolute Unix path), `changeId`, `skillRoot`
(`.agents/skills` or `.claude/skills`), `corpusRevision`, `authority`, `mode`
(`execute` or `verify-only`), and `maxRepairRounds` (zero or one). Record source
identity through the existing deployment handoff; do not invent provenance.
Verification-only requires zero repair rounds. The origin checks these inputs
before launch; workers confirm the referenced facts rather than treating
argument strings as proof of authority.

The ordinary path uses two assignments:

1. **Work:** inspect current state using GRACE recovery guidance. On a clean
   start, establish the required baseline. On recovery, verify prior progress
   and remaining obligations. Implement only what remains and reconcile the
   approved durable deltas as the designated sequential writer. If already
   satisfied, do not rewrite it. Return `ready-for-verification`, `blocked`, or
   `needs-decision`, with evidence and unresolved obligations. Work readiness is
   not final acceptance.
2. **Verify:** inspect the actual resulting candidate, not just the handoff.
   Load `code-review` when reviewing code; use the declared behavioral and
   GRACE checks. Do not repair the candidate or revise its authority. Running
   permitted checks may create ordinary test outputs; this is not a claim of
   filesystem-enforced read-only execution.

Skip Work in verify-only mode. Work that reports a blocker or decision does
not automatically trigger a verifier tasked to finish it. Verification may
request one bounded implementation repair when it demonstrates an ordinary
in-scope defect and repair was authorized; then verify again. Stop when the
bound is reached rather than silently declaring done or looping indefinitely.

The starter's maximum is four worker calls (Work, Verify, Repair, Verify), not
one agent per plan task. That does not bound tokens inside a worker: include a
proportionate effort bound in the commission and inspect BB's inherited call
and timeout limits before launch. If those limits are unsuitable, return the
configuration decision rather than changing global settings. The template uses
the inherited provider tuple unless the owner selects a validated override.

## Outcomes and evidence

Structured outcomes distinguish:

- **ready:** the authorized segment has its required evidence and no remaining
  acceptance obligation; ready is not applied, committed, deployed, or live-proven;
- **blocked:** an observed condition prevents completion, with evidence and the
  smallest next action;
- **needs-decision:** the exact missing owner choice or authority;
- **repairable:** an internal verification result identifying a demonstrated
  in-scope defect, not an instruction to broaden scope.

Every handoff contains a concise summary, evidence references, and remaining
obligations. Verification records whether the required final gate passed,
failed, or was not run. The starter refuses a readiness claim paired with a
failed/missing final gate, empty evidence, or remaining obligations. Structured
output prevents ambiguous branching; it does not prove the agent's statements
true.

The origin checks cited command results and evidence limits before accepting
the result. BB's successful run means orchestration completed, not that the
change passed. A failed worker or missing parallel result remains explicit
incomplete coverage; do not filter it out and claim comprehensive success.

## Authority and lifecycle closure

The starter's workers stop before apply/archive, commit, push, deployment,
credential access, live providers, or destructive cleanup. These are prompt
boundaries, not technical sandbox guarantees. Inspect actual BB permissions;
use permitted offline checks and least necessary access where available.

The origin handles lifecycle closure using `grace-execute`. If the owner already
authorized apply after fresh final validation, use that authority rather than
asking again. Otherwise return the missing approval. The worker template's
stop-before-apply boundary does not force an unnecessary human checkpoint in
a workflow whose origin already has conditional apply authority.

Resolve predecessor/replacement lifecycle order before making an end-to-end
completion claim. If the proposed retirement waits for a final gate which
itself checks incompatible predecessor assertions, expose that ordering issue
to the authorized lifecycle owner. Do not suppress errors, rewrite approved
assertions, archive unrelated work, or endlessly rerun the same checks.

## Packaging, installation, and recovery

The guide and asset travel with the existing Codex/Claude skill projections.
Projection does not create or overwrite product `.bb/workflows` files. When
authorized, adapt the installed asset into a named product workflow, recording
the source revision and intentional local differences. Do not hand-edit the
managed asset. Reconcile changes deliberately on the next corpus upgrade.

Inspect installed BB workflow documentation and validate the exact adapted
source before running it. Start it in the intended BB project/environment;
changing shell working directory alone is not a reliable context switch.
Preserve product-specific models, commands, domain rules, and permission
decisions rather than inheriting recorder's path or assumptions.

On interruption, inspect the workspace and durable evidence before choosing
resume. BB can replay successful calls, including writes, from an unchanged
prefix; a cached verification is not fresh proof of the current files. For
this small starter, a new run using GRACE recovery is the simple safe default
after intervening changes. Deliberate cached resume must include fresh live
verification after the replayed prefix before readiness is accepted.

Keep the concise accepted handoff in the project's existing change/evidence
location. BB history is useful execution history with configured retention,
not the sole long-term record. Do not create a parallel evidence registry.

If BB is unavailable, ordinary authorized agent execution can still follow the
same method. Report that durable orchestration was not used; do not silently
replace an explicitly requested BB run with another runner.

## Adopting the starter

Read the installed BB `workflows` skill and applicable authoring/run references;
they own the current runtime API. Within authorized setup, copy/adapt the asset
to a product-owned file. Check for an existing file first and preserve its
customizations. Example for Codex in the confirmed target repository (use
`.claude` for Claude):

```sh
mkdir -p .bb/workflows
test ! -e .bb/workflows/execute-approved-change.js &&
  cp .agents/skills/grace-execute/assets/execute-approved-change.js \
    .bb/workflows/execute-approved-change.js
bb status --json
bb workflows validate --file .bb/workflows/execute-approved-change.js
```

Confirm BB's project/environment and physical repository root match the target
before launch. Inspect inherited provider/model/reasoning and actual permissions.
Use installed BB guidance to validate any explicit override; do not guess IDs.
Example input shape (replace the illustrative path, change, and records):

```json
{
  "repoPath": "/absolute/product-repository",
  "changeId": "C-APPROVED-CHANGE",
  "skillRoot": ".agents/skills",
  "corpusRevision": "source commit recorded in the deployment handoff",
  "authority": "owner instruction and reference authorizing orchestration and implementation, offline only, no apply",
  "mode": "execute",
  "maxRepairRounds": 1
}
```

Use the BB run tool with the exact script path and JSON arguments, or the
documented CLI equivalent. Emit its returned preview, observe compact status,
and inspect bounded history as the installed workflow skill prescribes.
Loading this guide does not authorize a run.

For independent design use `outcome-tasking` and preserve first submissions;
for code review load `code-review` and substantiate findings. Do not adopt BB's
optional panels or repeated critic loops as mandatory quality gates. Product
requirements and authorized assurance decide what review is needed.

## Proving the integration

Test the actual asset with controlled worker results for ordinary success,
blockers, missing decisions, verification-only, repair success and exhaustion,
inconsistent readiness, invalid inputs, and worker failure. Check both provider
projections and validate the exact JavaScript with installed BB without launch.

Keep later behavioral trials small and explicitly authorized: direct-task
near miss, expected dirty recovery, already-satisfied target, and local checks
passing while lifecycle completion is blocked. Inspect worker reads and actions,
not just final prose. Deterministic branch tests do not establish skill
selection, correct repairs, or provider permission enforcement.
