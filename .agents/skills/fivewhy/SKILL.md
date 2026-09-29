---
name: fivewhy
description: Trace one observed failure to its real controllable parent through a bounded five-step causal loop. Use when the user asks for five whys, root cause, the problem behind a problem, or asks to step back from a patch-shaped solution. It uses a lightweight in-house causal challenger, shows the growing chain after every cycle, and validates it backwards with “therefore.”
---

# Fivewhy

Use this skill to move from a visible symptom to the nearest supported,
controllable parent cause without widening into a general architecture review.
It is a causal-discovery tool, not a solution generator or an audit. Its
in-house challenger tests one causal link at a time. Use the real `red-team`
skill only after a root is supported and there is a concrete response or owner
decision to challenge.

## Define and freeze the outcome box

State one concrete outcome box before asking a why:

```text
ACTOR
[who initiates the supported path]

PATH
[the actual path in scope]

FAILED EDGE
[the one observed state or effect that failed]

CONSUMER
[who or what needs the outcome]

AUTHORITY
[what may be inspected and what is protected]
```

If actor, path, failed edge, or consumer is unknown, return:

```text
OUTCOME BOX NEEDED
[the exact missing field and smallest fact needed]
```

Do not begin the loop or silently broaden the incident. The outcome box stays
fixed. A cause that changes its actor, consumer, product, topology, or protected
effect is an owner or authority boundary, not the next why.

## Split a compound failed edge before walking

One spine explains one failed edge. When one report contains separate sequential
failures—for example, an invocation never reaches a service and a later retry
misclassifies the service result—name them as `SPINE A`, `SPINE B`, and so on.
Keep the same outcome box when actor, path, consumer, and authority truly stay
the same, but start each spine at its own physical observation. Do not make one
task-local failure the parent cause of a later independent failure.

Reconstruct and classify each spine separately. A shared pattern may be stated
only after the separate reconstructions hold.

## Bind the baseline and evidence budget

When present truth, source identity, dates, or code behavior matter, name the
exact baseline first: an observed service state, release tuple, commit,
checkout, or supplied record. A fresh worktree or old committed checkout proves
only itself, never uncommitted or newer current state. If the needed baseline
is unavailable, stop with **baseline unavailable**.

Inspect only evidence that can prove or falsify the current direct link. Do not
map the whole repository, organisation, or history in search of a grander root.
When a codebase graph already exists, query it; do not build one just for this
loop. Stop gathering evidence once the current link can be accepted, rejected,
or marked unknown.

## Walk one bounded causal spine

Use at most five cycles, in this order. Five is a ceiling, not a target.

```text
Observed problem
  <- 1. Physical component or state
  <- 2. Technical mechanism
  <- 3. Process action or omission
  <- 4. Policy or standard gap
  <- 5. System-design condition
```

At each cycle, run the **in-house root-link challenger** below with only the
fixed outcome box, the current child, its named level, and admissible evidence.
It is deliberately smaller than `red-team`: it checks whether one parent
directly caused one child. It does not design a solution, compare proposals,
invent an architecture, or issue an audit disposition.

Ask it:

> Within this fixed outcome box, name one direct parent cause at the given
> causal level that materially explains the child. Keep it concrete and
> evidenced. Do not propose a remedy, introduce another problem, change the
> outcome, or continue to a wider system. If no single parent is supported,
> stop and name the smallest discriminating observation.

### In-house root-link challenger form

```text
LEVEL: [Physical | Technical | Process | Policy | System design]
CHILD: [the problem or prior-level cause being explained]
PARENT: [one concrete direct cause at this level]
THEREFORE: [PARENT], therefore [CHILD].
EVIDENCE: [observed fact/source] | INFERENCE: [what is not observed]
BREAK: [nearest credible counter-case, or smallest observation that disproves the link]
RESULT: [advance | insufficient evidence | boundary | owner decision | controllable design cause]
```

`PARENT` is a cause, never an action such as “add a registry,” “document it,”
or “test more.” `BREAK` keeps the challenge honest: it must be close enough to
overturn this particular link, not a philosophical objection. `RESULT: advance`
is the only reason to ask the next why.

Use `controllable design cause` only for a specific System-design-level parent.
If an earlier link exposes a locally correctable condition but the evidence
cannot support its next parent, use `RESULT: insufficient evidence` and record
**local correction** later as the intervention category. That distinguishes a
useful correction from a claimed systemic root.

This six-label block is a closed handoff interface. Use these labels exactly;
do not append or substitute legacy fields such as `OWNER AND PATH`,
`FALSIFIER`, or `STOP`. The fixed shape makes separate spines comparable and
lets the next cycle receive causal context rather than an improvised report.

## Show the full causal context after every cycle

After every accepted cycle, return the complete growing chain before asking the
next question. Keep already accepted link statements intact; do not silently
compress, rewrite, or reopen them. The headings below are part of the handoff;
do not rename them to a narrative alternative.

```text
CYCLE [1–5]
[complete in-house root-link challenger block]

CAUSAL CHAIN SO FAR
[newest accepted parent] therefore ... therefore [observed problem].

NEXT QUESTION
[next named level]: Why did [current parent] occur?
```

The chain is the context handoff. It lets the caller see how an immediate
patch-shaped symptom is related to the larger but still bounded cause space.
If a cycle stops, show the chain through the last supported link and replace
`NEXT QUESTION` with the exact stop reason or discriminating observation.
Finish every stopped spine with its `THEREFORE RECONSTRUCTION` and `STOP AND
STANDING`; do not leave a dangling final next-question block.

## Apply the therefore test and stop cleanly

Accept a link only when reading it backwards produces a direct statement about
the real service or workflow:

```text
[parent], therefore [child].
```

Stop at the last supported link when:

- the sentence needs a philosophical claim, a claim about human nature, an
  invented dependency, or an unobserved mechanism;
- the proposed parent is a remedy, a documentation request, a test, or a
  restatement of the child;
- evidence cannot select a single parent, or a near observation cannot
  discriminate between material competing parents;
- the next parent crosses the fixed outcome or owner/authority boundary;
- a policy or owner decision is already the actionable parent; or
- cycle five identifies a specific, controllable system-design condition.

Never ask a sixth why. “People are flawed” or “the organisation is immature”
is not a usable parent. Return to the last concrete condition an owner can
choose or change.

## Challenge a previously accepted link without reopening the loop

A later fivewhy pass may challenge one named link only. Inspect its falsifier,
then retain, replace, or stop. It may not change the outcome box, append extra
whys, or revise unrelated accepted links. If a replacement changes the causal
standing, reconstruct the whole surviving chain.

```text
CHALLENGED LINK: [level and original PARENT -> CHILD]
CHALLENGE: [one concrete counter-case]
LINK STATUS: [retained | replaced | insufficient evidence]
FALSIFIER RESULT: [what the permitted evidence showed]
```

`LINK STATUS` is causal handover only, never an audit disposition.

## Reconstruct and classify the result

When the loop stops, read every supported link backwards, newest parent to
observed problem, using “therefore.” Include the cycle that established each
link. Then state only:

- the deepest supported parent, or the exact unresolved competing parent;
- whether it is observed or inferred;
- the intervention category: **subtraction**, **local correction**,
  **operational/policy decision**, **missing evidence**, or **new maintained
  capability**; and
- the next discriminating observation or owner decision.

A causal finding does not authorize implementation or turn an owner decision
into a requirement.

## Prepare a bounded real red-team handoff only after a root

Once a supported root exists, prepare this handoff for an actual `red-team`
run. Do not invoke it merely to find more whys. If no plausible response or
owner decision exists yet, stop at the causal finding; the owner must first
choose a response boundary.

```text
BOUNDED RED-TEAM HANDOFF
OUTCOME BOX
[fixed box]

ACCEPTED CAUSAL CHAIN
[full therefore reconstruction]

FINAL ROOT AND NATURAL OWNER
[supported root]

INTERVENTION CATEGORY
[classification]

QUESTION
Challenge the smallest plausible response at this natural owner. Validate the
real path, exact missing edge, and strongest near counter-case. Do not reopen
the causal chain, broaden the outcome box, invent topology, or prescribe a
larger solution.
```

The subsequent real `red-team` review evaluates a response; it does not repair
or extend this causal investigation.

## Compact report shape

```text
OUTCOME BOX
[actor -> path -> failed edge -> consumer]

CAUSAL SPINE
[one complete in-house link block for every reached cycle; separate SPINE A/B
only when the original failed edge was compound]

CYCLE HANDOFFS
[the causal chain so far and next question after each cycle]

THEREFORE RECONSTRUCTION
[cycle-labelled final chain]

STOP AND STANDING
[why the loop stopped; observed/inferred; intervention category; next fact or owner decision]

BOUNDED RED-TEAM HANDOFF
[only when a supported root and plausible response boundary exist]
```

Omit unreached levels. Keep it short: the value is the cumulative, validated
causal chain and disciplined stop, not five filled rows.
