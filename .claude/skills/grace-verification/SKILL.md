---
name: grace-verification
description: Design and maintain GRACE 4 verification entries, commands, scenarios, markers, and assertion evidence under .grace/verification.
---

<skill>
<purpose>
Strengthen deterministic verification for modules and changes. Verification state lives in `.grace/verification/index.xml` and routed verification documents. Each durable module should have deterministic `V-M-*` coverage unless an explicit exception is planned.
</purpose>

<workflow>
1. Read relevant `.grace/graph` anchors and current `V-M-*` entries.
2. Identify scenarios, commands, test files, required log markers, and trace assertions. Use `behavioral-testing` when designing or changing tests: choose a meaningful observation boundary, derive expectations independently, and establish that the check detects the relevant failure where practical.
3. Ensure commands are deterministic and runnable from the project root or documented cwd.
4. Update or propose `.grace/verification` changes through the active change plan.
5. Run the commands and record fresh evidence in the response.
6. Exercise the original consumer scenario when available and state explicitly when a deterministic fixture does not reach the deployed or integration path.
</workflow>
<cwd_contract>
When verification commands run from a workspace or package directory, add one direct `<Cwd>relative/project/path</Cwd>` child to the owning `V-M-*` entry. Keep declared `<TestFiles><File>...</File></TestFiles>` paths project-root-relative; the CLI uses `Cwd` only to compare them with cwd-relative command arguments.
</cwd_contract>
<evidence_contract>
Use `<Marker>` when module health must prove a runtime log or trace emission from linked implementation code. Use `<TraceAssertion>` for deterministic test or trace evidence that does not require runtime logging, such as pure functions, type-level modules, and core libraries. A non-empty marker or trace assertion satisfies the module-health evidence requirement; only authored markers require matching runtime emission and `BLOCK_*` evidence.
</evidence_contract>
<gate_task_contract>
Reference named project tasks in `MustPassCommand` and `ExpectedCommand` (for example `bun run gate:e2e`) instead of inline `;`-chains. Decompose full gates into granular named tasks (`gate:test`, `gate:typecheck`, `gate:build`, `gate:e2e`) so a selective re-run is just running that task, timeouts map to one coherent unit, and `grace lint --run-commands` reports each gate step with its own timing and log.
</gate_task_contract>
<flake_contract>
An intermittent failure may reveal a product race, environment fault, or
verification-harness defect. Use `diagnosing-bugs` to distinguish those causes
from per-attempt evidence, including `~/.cache/grace/run-commands/` logs. Preserve
failed attempts; a later green retry does not cancel them or prove a repair.

Fix the demonstrated cause within authorized scope and verify the original
scenario. Runner retries or quarantine are allowed only with an explicit
rationale, applicable authority, and a report of reduced coverage, unresolved
product risk, and the remaining repair owner or action. Treat them as mitigation
unless evidence establishes a repaired cause. Do not weaken an assertion to
hide nondeterministic product behavior or rerun silently until green.
</flake_contract>
</skill>
