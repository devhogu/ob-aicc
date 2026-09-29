---
name: behavioral-testing
description: Design or improve tests that prove observable behavior. Use for test strategy, regression coverage, test-first work, integration tests, or deciding whether tests would detect a named bug. Do not use merely to run an established check or report its result.
---

# Behavioral testing

Use tests to protect a behavior that matters to a real caller or consumer.
The task's existing authority decides whether tests may be added or changed;
this skill supplies the evidence method, not extra permission.

## Method

1. Name the behavior, consumer, and observation boundary. Prefer a stable
   public interface or real integration seam over private implementation.
2. Derive the expected result independently from the implementation: use an
   accepted requirement, worked example, protocol, known-good literal, or
   externally observed outcome. An assertion computed by repeating the code's
   algorithm is not an independent oracle.
3. Choose the smallest case that can distinguish correct from incorrect
   behavior. For a regression, demonstrate that the check detects the named
   failure before relying on its green result when practical and safe.
4. Implement one useful behavior slice, then run the narrow check. Expand only
   when the next risk justifies another case.
5. Run the original scenario and the relevant broader gate when available.
   Report what each result proves and what it does not.

Test-first is useful when behavior can be stated before implementation. It is
not compulsory for exploratory diagnosis, a mechanical behavior-preserving
refactor, generated artifacts, or an unavailable environment. Preserve useful
existing tests unless their behavior contract is intentionally superseded.

## Completion

Return the protected behavior and boundary, the independent source of expected
results, failure-detection evidence where practical, passing evidence, and any
untested risk. A green fixture alone is not evidence of the real path if that
path was not exercised.
