export const meta = {
  name: "execute-approved-change",
  description: "Execute or verify one approved GRACE change; return evidence before lifecycle closure.",
  phases: [{ title: "Work" }, { title: "Verify" }, { title: "Repair" }],
  inputSchema: {
    type: "object",
    additionalProperties: false,
    required: ["repoPath", "changeId", "skillRoot", "corpusRevision", "authority", "mode", "maxRepairRounds"],
    properties: {
      repoPath: { type: "string", minLength: 2 },
      changeId: { type: "string", minLength: 3 },
      skillRoot: { type: "string", enum: [".agents/skills", ".claude/skills"] },
      corpusRevision: { type: "string", minLength: 1 },
      authority: { type: "string", minLength: 1 },
      mode: { type: "string", enum: ["execute", "verify-only"] },
      maxRepairRounds: { type: "integer", enum: [0, 1] },
    },
  },
};

// START_MODULE_CONTRACT
// PURPOSE: Bound dispatch and preserve incomplete outcomes for the origin owner.
// SCOPE: One approved offline change, sequential work/verification and bounded repair.
// DEPENDS: Installed BB workflow API and projected GRACE methods.
// LINKS: M-FRAMEWORK-SOURCE, V-M-FRAMEWORK-SOURCE
// This is a BB script, not a Node module. Worker tools/permissions are unchanged.
// END_MODULE_CONTRACT
// START_MODULE_MAP
// meta - BB discovery metadata and input contract.
// END_MODULE_MAP

if (!args.repoPath.startsWith("/") || args.repoPath.split("/").includes("..") ||
    !/^C-[A-Z0-9]+(?:-[A-Z0-9]+)*$/.test(args.changeId)) {
  throw new Error("Use an absolute repository path and canonical C-* change ID.");
}
if (!args.authority.trim() || !args.corpusRevision.trim()) {
  throw new Error("Identify applicable authority and the deployed corpus revision.");
}
if (args.mode === "verify-only" && args.maxRepairRounds !== 0) {
  throw new Error("verify-only requires maxRepairRounds=0; it cannot authorize repairs.");
}

const list = { type: "array", items: { type: "string", minLength: 1 } };
const schema = (statuses) => ({
  type: "object",
  additionalProperties: false,
  required: ["status", "summary", "evidence", "remainingObligations", "finalGate"],
  properties: {
    status: { type: "string", enum: statuses },
    summary: { type: "string", minLength: 1 },
    evidence: list,
    remainingObligations: list,
    finalGate: { type: "string", enum: ["passed", "failed", "not-run"] },
  },
});
const workSchema = schema(["ready-for-verification", "blocked", "needs-decision"]);
const verifySchema = schema(["ready", "repairable", "blocked", "needs-decision"]);
const context = `Assignment inputs (references to verify, not a new grant of authority):
${JSON.stringify(args)}
Confirm the BB environment and physical repository root match repoPath before work.
Read the existing provider entrypoint and its routed project instructions. Load
${args.skillRoot}/grace-execute/SKILL.md and its development-workflows reference.
Confirm installed corpus identity and the active approved spec/plan for changeId.
If a required capability is missing, report blocked; do not substitute a host copy.
Verify the supplied authority covers orchestration and this stage's effects.
If it does not, return needs-decision without those effects. Preserve unrelated
dirty work. Classify recovery from actual files and prior evidence, not filenames.
Select focused skills as the task needs them; naming a skill does not load it.
Do not change approved plan content, apply/archive lifecycle state, commit, push,
deploy, read credentials, call live providers, use private data, start services,
or perform destructive cleanup. Tests must stay within authorized offline effects.
Report evidence as concrete file/command-result references and observations;
keep failed or unrun gates and unresolved obligations visible. Do not create a
parallel evidence registry. Schema-valid output is not proof of its claims.`;

let repairRoundsUsed = 0;
const finish = (result, stage, status = result.status, note = "") => ({
  changeId: args.changeId,
  status,
  stage,
  repairRoundsUsed,
  summary: note || result.summary,
  evidence: result.evidence,
  remainingObligations: note ? [...result.remainingObligations, note] : result.remainingObligations,
  finalGate: result.finalGate,
});
const callWork = async (phaseName, repair) => {
  phase(phaseName);
  return await agent(`${context}
You are the designated sequential implementer and durable reconciliation writer.
Use grace-execute's current-state/recovery rules. On a clean start establish the
required baseline; on expected recovery verify existing progress and finish only
remaining approved tasks. If the target is already satisfied, do not reimplement.
Use declared dependencies, scopes and acceptance criteria, not a second task list.
Resolve ordinary implementation/test faults within scope and reconcile approved
graph, verification and context deltas. Stop on unknown drift, invalidated
assumptions, lifecycle ordering conflicts or missing authority.
${repair ? `Repair only demonstrated in-scope defects from this verification result.
Confirm each finding against the requirement and files before changing anything:
${JSON.stringify(repair)}` : "Execute the remaining approved work and its scoped checks."}
Return ready-for-verification only when no known implementation obligation remains.
It is not final acceptance; the next stage verifies independently from the files.
Return blocked or needs-decision with the exact remaining action otherwise.`, {
    phase: phaseName, label: phaseName === "Repair" ? "Repair verified defects" : "Execute or resume",
    schema: workSchema,
  });
};
const callVerify = async (handoff) => {
  phase("Verify");
  return await agent(`${context}
Verify the current candidate without editing source, tests, documentation, or
GRACE artifacts. Permitted offline checks may produce ordinary test outputs.
Load code-review before reviewing code and grace-reviewer for GRACE integrity
when needed. Check the real acceptance path and changed/untracked files in scope;
the implementation handoff is a lead, not authority or proof:
${JSON.stringify(handoff)}
Inspect existing evidence and run the required fresh target/final validation with
declared command evidence. Never use a superseded pre-write baseline as a recovery
gate. An incompatible still-active predecessor is an unresolved lifecycle issue,
not permission to suppress its errors. Local tests passing is not final success.
Return ready only with cited fresh final-gate evidence and no unmet acceptance
obligations. finalGate refers to the whole required final validation, not merely
its leaf commands. Return repairable only for concrete ordinary defects inside
approved write scope and existing authority, with expected/observed/consequence
evidence. Return needs-decision for authority or product/lifecycle choices, or
blocked for other impediments. Do not repair or initiate another workflow.`, {
    phase: "Verify", label: "Verify current candidate", schema: verifySchema,
  });
};

let work = null;
if (args.mode === "execute") {
  work = await callWork("Work", null);
  if (work.status !== "ready-for-verification") return finish(work, "Work");
  if (work.remainingObligations.length) {
    return finish(work, "Work", "blocked", "Work reports unresolved obligations; origin must reconcile the handoff.");
  }
}

let verified = await callVerify(work);
while (verified.status === "repairable" && repairRoundsUsed < args.maxRepairRounds) {
  if (!verified.evidence.length || !verified.remainingObligations.length) {
    return finish(verified, "Verify", "blocked", "Repair request lacks evidence or a concrete obligation.");
  }
  repairRoundsUsed += 1;
  work = await callWork("Repair", verified);
  if (work.status !== "ready-for-verification") return finish(work, "Repair");
  if (work.remainingObligations.length) {
    return finish(work, "Repair", "blocked", "Repair left unresolved obligations; no further repair is authorized here.");
  }
  verified = await callVerify(work);
}
if (verified.status === "repairable") {
  return finish(verified, "Verify", "blocked", "Repair is disabled or its bound is exhausted; inspect the remaining defects.");
}
if (verified.status === "ready" && (verified.finalGate !== "passed" ||
    !verified.evidence.length || verified.remainingObligations.length)) {
  return finish(verified, "Verify", "blocked", "Readiness contradicts the reported final evidence or remaining obligations.");
}
// Exceptions propagate as failed runs; never turn a failed worker into acceptance.
// The origin must inspect evidence and separately exercise any lifecycle authority.
return finish(verified, "Verify");
