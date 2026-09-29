---
name: grace-fix
description: Debug and fix issues in a GRACE 4 project using .grace semantic navigation, assertions, and verification evidence.
---

<skill>
<investigation_path>
1. Start from the failure, pasted error, failing command, or user report.
2. Load relevant `.grace/graph` module anchors and `.grace/verification` entries.
3. Check active `.grace/changes` for overlapping or stale planned work.
4. Inspect file-local contracts and semantic blocks before editing.
5. Use `diagnosing-bugs` to separate observed facts from hypotheses and choose
   a discriminating check. A diagnosis-only request stops before repair.
6. When repair is authorized, make the smallest correct fix inside the approved
   scope and use `behavioral-testing` for lasting regression evidence when it
   can protect the original scenario.
</investigation_path>

<verification>
Run the original scenario where practical, then the specific `V-M-*` commands
or closest deterministic tests. State what the evidence does not cover. If
verification expectations are stale, update or propose changes through the
GRACE 4 change lifecycle.
</verification>
</skill>
