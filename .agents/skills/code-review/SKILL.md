---
name: code-review
description: Review a concrete code change, patch, branch, pull request, commit range, or working tree for requirement fit, behavioral defects, regressions, and maintainability. Do not use for GRACE artifact integrity alone or an unconstrained architecture survey.
---

# Code review

Review the exact candidate against its intended behavior and real consumers.
Review does not authorize fixes, commits, pushes, merges, or reviewer
delegation.

## Review method

1. Resolve the candidate precisely: named range or revision, staged changes,
   unstaged changes, and relevant untracked files. Record exclusions. Do not
   assume `base...HEAD` represents a working tree.
2. Read the governing requirement or task and the affected real path. Establish
   the expected behavior and distinguish it from assumptions or preferences.
3. Check behavior along the affected path, including plausible boundary and
   error cases and whether tests could pass while that path fails. Follow a
   concern when it can materially change the review's conclusion.
4. Check implementation quality: responsibility placement, caller knowledge,
   duplicated rules, unnecessary complexity, compatibility, observability,
   and maintainability.
5. Inspect relevant evidence and use bounded checks where they resolve
   uncertainty. Static reasoning can establish a defect; execution is not
   required for every finding. Compare prior behavior before calling an issue
   a regression; otherwise state that its introduction is unverified.
6. If GRACE applies, leave lifecycle, scope, anchor, and assertion integrity to
   `grace-reviewer` and report that evidence separately. Use `red-team` only to
   challenge a material proposal or readiness conclusion, not as a synonym for
   ordinary code review.

## Finish the review

Before sending the report, the same reviewer briefly checks each material
finding against the evidence already gathered:

- **Expected:** Which requirement, established caller behavior, or concrete
  safety/correctness obligation is violated?
- **Observed:** What does the code or executed check actually establish?
- **Consequence:** Does that observation support the impact being claimed?

Narrow or drop claims the evidence does not support. An unestablished policy
belongs with questions or suggestions, not confirmed defects or automatic
blockers. Recommend restoring a clear contract unless the task or a concrete
obligation warrants changing it. Keep useful exploration open; this is a short
check of the conclusions, not another review stage or a required report form.

Lead with actionable findings ordered by impact, giving the location,
expected versus observed behavior, consequence, and correction in ordinary
prose. Include relevant questions and evidence limits. There is no finding
quota: if no defects were found, say so and briefly name what was checked.
