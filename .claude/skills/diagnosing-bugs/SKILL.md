---
name: diagnosing-bugs
description: Diagnose a concrete defect, failure, outage symptom, flaky result, or unexpected behavior by separating evidence from hypotheses and selecting discriminating checks. Use for root-cause diagnosis; fixing requires authority from the task.
---

# Diagnosing bugs

Establish why the observed behavior occurs before choosing a response. A
diagnosis request does not by itself authorize a repair, deployment, restart,
dependency installation, or destructive cleanup.

## Evidence loop

1. State the exact symptom, original scenario, expected behavior, environment,
   and freshest reliable evidence. If reproduction is unavailable, use bounded
   logs, traces, configuration, source, or state inspection and say so.
2. Identify the smallest set of materially different explanations supported
   by current evidence. Mark inference as inference.
3. Select the cheapest safe observation that would distinguish those
   explanations. Instrument only the relevant path and keep sensitive values
   out of output.
4. Update or eliminate hypotheses from the result. Repeat only while another
   observation can change the response.
5. Name the controllable cause and the evidence chain. If a fix is authorized,
   make the smallest correct change and verify the original scenario plus the
   nearest meaningful regression gate.

Use `fivewhy` only when the user asks for the controllable cause behind the
immediate defect or when a patch-shaped answer would leave the causal question
unresolved. Use `behavioral-testing` when lasting regression evidence is in
scope. Neither is an automatic stage.

## Completion

Return observed facts, rejected and remaining hypotheses, root cause or current
uncertainty, the selected response, original-scenario evidence, and the next
discriminating check if the cause remains unresolved.
