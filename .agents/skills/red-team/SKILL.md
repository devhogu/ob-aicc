---
name: red-team
description: Challenge pre-plan proposals, designs, changes, and conclusions for intent drift, real-path fit, unnecessary complexity, boundary failure, and false readiness.
---

# Red-team

Challenge the proposal's assumptions and material failure modes. Offer the
smallest coherent correction only when the causal basis is sufficiently
established; otherwise state the unresolved question or exact missing
evidence. When the proposal is protected independent evidence, route findings
and any correction to the decision owner, never back to its author as coaching.
State what would falsify load-bearing claims. Conclude a review of a
candidate or decision claim offered for judgment with `ACCEPT`, `REVISE`,
`REJECT`, or `INSUFFICIENT EVIDENCE`. When the work is genuinely exploratory
and no candidate is yet offered for judgment, do not manufacture a verdict;
return only material assumptions, tensions, owner decisions, and the next
discriminating observation.

Keep the result short and decision-useful. Findings are considerations for
improving the proposal, not requirements to implement automatically. Omit
empty sections. If the proposal survives, briefly state the strongest causal
counter-case attempted and why it did not overturn the conclusion.

Use the sections below as decision lenses, not a checklist. Scale challenge to
consequence and reversibility. Pursue only lines capable of changing the
standing or owner decision, and stop when further challenge would not change
the disposition, smallest correction, or next discriminating observation.

## Expand before you anchor

Before freezing the review boundary, step back far enough to see the larger
root-cause and impact space. Trace the parent outcome, surrounding integrations
and owners, current reality, and the highest-impact consequence. Test whether
the proposal, inherited anchor, boundary, or existing mechanism is treating a
symptom as the problem. Then return to the smallest coherent decision under
review. Context expansion informs judgment; it does not authorize scope
expansion or a general architecture audit. If the larger context invalidates
the anchor, return that exact owner decision instead of silently changing
scope.

## Anchor the review

For a candidate or decision claim offered for judgment, bind the originally
authorized or explicitly scoped outcome, observable completion, current
baseline, relevant boundary, protected effects, and candidate under review.
Retain that anchor for every revision unless it is explicitly reauthorized.
Earlier findings, accepted deltas, proposal-owned specifications, and passing
tests are evidence; they do not acquire authority through repetition.

During genuine exploration, bind the owner question, current reality, and
authority instead. Do not invent a candidate or disposition merely to satisfy
the review form.

## Protect an independent subject

Before challenge, identify whether the author is a directed worker, the
decision owner, or an independent peer. An independent peer's first complete
submission is a frozen subject: do not ask its author to repair, reconsider, or
align it; do not expose another candidate or the reviewer's emerging answer;
and do not count post-feedback agreement as independent evidence.

Clarification is append-only. It may supply a missing neutral fact or ask what
the author meant, but it must not carry a diagnosis, counterevidence,
alternative, preferred answer, or revision request. Send findings and
synthesis to the decision owner. If the owner later authorizes revision, treat
the result as a new candidate cycle with disclosed influence, not confirmation
of the original independent judgment.

For a candidate or decision claim offered for judgment, judge the cumulative
candidate against the original anchor, not only the latest reasonable delta.
If the anchor is missing or contradictory and that prevents assessment of a
load-bearing claim, name the exact decision or evidence needed and use
`INSUFFICIENT EVIDENCE`.

## Challenge before commitment

For a material plan or architecture proposal, challenge placement before
implementation detail. Require the initiating actor, observable effect,
intended recipient or maintained consumer, existing supported path, and exact
missing edge. Separate a stable outcome or system invariant from a reaction to
one incident, test, audit, or delivery run. If the proposal cannot establish
those facts, return the missing owner decision instead of hardening the
proposed mechanism.

## Trace the functional spine

Name the smallest coherent path from the initiating actor or supported trigger,
through the necessary work, to the intended observable effect and real
recipient or maintained consumer.

For a change or capability expansion in an existing workflow or system, use the
explicitly scoped real path plus only the direct dependencies, recipients,
consumers, and consequences needed to test its end-to-end claim. Follow a
concrete causal path, not general architectural curiosity.

Evidence must follow the kind of real path actually claimed. For human,
knowledge, or document work, trace supplied sources and observations through
the governing method, workflow, human authority or handoff, and intended use.
For executable work, trace the supported entrypoint through packaging,
integration wiring, configuration, admitted inputs, lifecycle preconditions,
effect, and downstream observation. A source import, document cross-reference,
static call graph, test-only caller, mock substitution, or proposal-owned
harness proves only the boundary it exercises, not end-to-end reachability or
usefulness. At proposal time, require the real path to be named concretely; for
a frozen candidate, verify that it exists. Protected or live execution is not
implied: if inspection cannot establish an edge, report it as unproven rather
than inventing a support world.

Identify the relevant existing mechanism or smallest combination of mechanisms
and assess actual fit rather than similarity alone.

**Causal completeness check.** Before accepting a load-bearing claim that a
selected mechanism represents the intended outcome, identify the nearest real
recipient or maintained consumer, or the governing parent outcome. Consider
both disagreement directions and attempt both when material: mechanism pass /
whole outcome reject, and mechanism reject / whole outcome accept. Use the
mechanism's own polarity; for a detector, compare detect/no-detect with the
consumer's complete decision. A different final disposition may be intentional;
preserve the relevant distinctions, not necessarily the verdict. Internal
consistency among the proposal, tests, documents, and mechanism is not
end-to-end evidence. If no recipient or consumer exists, name the missing
composition evidence rather than inventing a harness. Treat a local mechanism
or intermediate conclusion as scoped evidence, not whole-outcome readiness.
When source or version identity is load-bearing, bind the exact source or
baseline and its governing authority. In all cases, check the nearest real
recipient or consumer before accepting the larger claim.

Prefer extending existing mechanisms when they genuinely fit and preserve the
work's ownership, governing meaning or contracts, lifecycle, and real behavior.
Before recommending anything new, state specifically why an existing boundary
cannot satisfy the capability safely and coherently. Do not force reuse when
the existing mechanism caused the problem or would produce a larger or more
fragile change. Judge the smallest coherent end-to-end change, not the smallest
local diff.

## Challenge functional displacement

Treat complexity and defensive depth as costs requiring a traced obligation,
not as quality by accumulation. For each material layer outside the functional
spine, identify:

- the exact outcome, independently governing obligation, or concrete failure it
  addresses;
- the real recipient or maintained consumer that uses it;
- its natural owning boundary and why an existing mechanism cannot own it; and
- what can be removed while preserving the outcome and necessary protection.

Apply the removal counterfactual: if the mechanism did not exist, which real
outcome or independent obligation would fail? If the answer is only that a
test, audit, handoff, or proof would be less complete, subtract it. A new
maintained noun requires a real recipient or consumer, a stable invariant, and
a natural owner; the incident that inspired it is not enough.

Challenge these recurring signals when they lack that causal basis:

- overengineering, speculative generality, and future-proofing beyond the
  selected use case;
- overfitting to one incident, candidate, test, audit finding, reviewer, or
  delivery workflow;
- overcomplication through unnecessary indirection, abstraction, protocols,
  state, or configuration;
- parallel or duplicated methods, workflows, interfaces, authorities,
  selectors, stores, orchestration, validation, lifecycle, recovery,
  publication, or deployment paths;
- provenance, governance, custody, inventory, staging, handoff, assurance, or
  defense layers that become maintained subsystems without a maintained
  recipient or consumer;
- harness or proof displacement, where the supporting world is more complete
  than the maintained functional path; and
- assurance recursion, where one support layer exists mainly to operate,
  custody, validate, or prove another support layer.

A support layer whose need arises mainly from another added support layer is
presumptive drift. Complexity, code size, document volume, and test count are
signals, not findings by themselves. Do not reject defense in depth merely
because controls are numerous: retain controls that address distinct material
failure modes or independent obligations at their natural owning boundaries.
The concern is duplicated authority, candidate-shaped control, or support-layer
recursion without an outcome or risk trace.

## Prevent the audit ratchet

A finding does not authorize its implementation. First classify it against the
original anchor and maintained path as one of:

- an outcome or integrity defect on the functional spine;
- a predecessor defect exposed by the work;
- missing evidence;
- optional hardening; or
- a change to scope, topology, authority, or protected effects.

Only a demonstrated spine defect may justify correction within the current
candidate, and only when the correction stays inside the authorized boundary.
Handle predecessor defects separately. Close evidence gaps with proportionate
evidence rather than product machinery. Keep optional hardening optional.
Return scope, topology, authority, and protected-effect changes for explicit
decision; do not issue them as audit repairs. When more than one coherent
boundary could resolve a finding, state the decision and constraints instead of
selecting an implementation. Any correction remains advisory and separately
authorized. `REVISE` rejects the current claim or candidate; it does not
authorize the correction, another milestone, or protected execution.

A material `REVISE` finding must identify at least one concrete broken outcome
edge, existing outcome or system invariant, affected real recipient or
consumer, or independent obligation. Missing ceremony, documentation breadth,
hashes, optional hardening, or more proof is not material by itself. For an
owner-authorized revision cycle, review the material revision's causal delta;
do not reopen accepted decisions unless new
observed truth creates a contradiction.

Treat verification and cleanup as authority-bearing actions. A proposed test
or exercise is not proportionate if its effects exceed the owned boundary for
people, data, or resources. Anything present in the pre-action baseline is
protected; cleanup may remove only exact current-task identities created
afterward and must stop when identity or ownership cannot be revalidated.

Treat a correction as a material expansion when it adds or changes governing
meaning, intended actor or recipient, method or workflow, human authority,
supported entrypoint, public interface, runtime component, authority,
persistent store, protocol or schema boundary, lifecycle or state machine,
publication or release unit, deployment path, or intended outcome—even if the
implementation change is small. A finding caused only by an added mechanism is
a consequence of retaining that mechanism, not an independent requirement.

Pause descendant hardening and test whether subtraction or maintained reuse is
sufficient when:

- the only recipient or consumer is a test, audit, harness, staging, or handoff
  mechanism;
- the functional path remains unexercised or unchanged while support machinery
  grows;
- an assurance or governance layer mainly supports another added layer;
- accumulated fixes alter the original premise or topology; or
- removing an added layer preserves both the intended outcome and required risk
  control.

Prefer, in order, removal, direct reuse, a task-local evidence mechanism, and
then the smallest necessary maintained-system addition.

Do not broaden the review into a general architecture audit. If the scoped
evidence is insufficient, say so rather than inventing system behavior or a
replacement design. Use `INSUFFICIENT EVIDENCE` only when missing evidence
prevents assessment of a load-bearing claim; name that claim and the exact
evidence needed rather than using uncertainty to avoid judgment.

Return only what is material:

- the anchor and claimed outcome edge, or the exploratory owner question;
- material findings and failure modes;
- the smallest correction, if one is supported;
- explicit non-requirements;
- falsifiers for load-bearing claims, including the cross-boundary counter-case
  when applicable;
- for a candidate or decision claim offered for judgment, final disposition:
  `ACCEPT`, `REVISE`, `REJECT`, or `INSUFFICIENT EVIDENCE`; otherwise, the next
  discriminating observation.

Before communicating findings, ask: am I reporting judgment to the decision
owner, or shaping the subject until it agrees with me? If the latter, stop.

Before issuing a disposition or closing an exploratory challenge, apply this
real-path question whenever a mechanism is actually proposed:

> Which real actor reaches or uses this mechanism through the actual workflow
> or integration and supplied inputs; which real recipient or maintained
> consumer uses its result; and which exact intended outcome edge does it close?

For an executable claim, identify the supported entrypoint and real wiring
without load-bearing test substitution. For a human, knowledge, or document
claim, identify the governing source, method, authority or handoff without
proposal-only narrative substitution.

If no such path exists, treat that absence as material evidence against
maintained placement. Do not add maintained machinery merely to manufacture
completion or proof.
