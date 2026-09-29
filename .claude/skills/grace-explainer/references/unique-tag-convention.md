# Unique Tag Convention

GRACE 4 semantic anchors carry identity in the XML tag and must not declare
attributes. Root document attributes such as `graceVersion` and change `status`
are separate schema fields, not semantic-anchor identity.

## Incorrect identity representation

```xml
<!-- BAD: Generic entity tags and identity attributes are not GRACE anchors. -->
<Module ID="M-CONFIG">Config</Module>
```

## Attribute-free anchors

```xml
<!-- GOOD: Each closing tag carries the identity; meaning stays in children. -->
<M-CONFIG>
  <Purpose>Application configuration</Purpose>
</M-CONFIG>
<M-DB>
  <Purpose>Database access</Purpose>
</M-DB>
<M-AUTH>
  <Purpose>Authentication</Purpose>
</M-AUTH>
```

These are fragments inside the appropriate routed document. Its index must
route their owners; modules also need matching verification entries.

## Canonical identities

| Entity | Anchor |
| --- | --- |
| Module | `M-CONFIG` |
| Data flow | `DF-SEARCH` |
| Graph document | `GD-MAIN` |
| Verification document | `VD-MAIN` |
| Module verification | `V-M-CONFIG` |
| Change bundle | `C-ADD-AUTH` |
| Planned task inside its change | `T-001` |

Use the owning artifact's schema for ordinary repeated data such as `Goal`,
`Criterion`, `File`, and `Command`. Do not invent a unique tag for every
repeated XML element. Source annotations such as `fn-search`, `type-Result`,
and `export-config` are a separate markup convention, not new change fields.

Preserve exact schema field spelling. Do not mechanically rename wrappers or
strip schema-defined non-anchor attributes. Consult `grace lint` for grammar
and the relevant routed graph/verification guide for placement.

Stable, explicit anchors support unambiguous source navigation. They do not
by themselves demonstrate better model behavior or runtime correctness.
