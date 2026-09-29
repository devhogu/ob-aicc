---
name: grace-refactor
description: Refactor GRACE 4 governed code while keeping .grace graph, verification, change scopes, and file-local anchors synchronized.
---

<skill>
<scope>
Use this for rename, move, split, merge, extraction, or boundary cleanup work. Greenfield feature work should go through `grace-spec`, `grace-plan`, and `grace-execute`.
</scope>

<must_do>
- Resolve affected `M-*`, `DF-*`, and `V-M-*` anchors through `.grace/graph/index.xml` and `.grace/verification/index.xml`.
- Check active `.grace/changes` for scope overlap before editing.
- Use `codebase-design` when the refactor changes responsibility, interfaces,
  or caller knowledge. Skip architectural analysis for a mechanical rename or
  formatting-only change.
- Preserve or update file-local `LINKS:`, module contracts, function contracts, and semantic blocks.
- Update durable graph and verification artifacts only when the refactor intentionally changes boundaries, paths, or evidence.
- Preserve useful existing behavioral tests. Use `behavioral-testing` for a
  new or changed behavior contract; a mechanical behavior-preserving refactor
  does not need a manufactured red-green cycle.
- Run targeted tests and the lifecycle-appropriate GRACE lint when available.
</must_do>
</skill>
