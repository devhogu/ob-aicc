# Workspace layout and navigation

## Common shell

A 56–64px header carries identity and global context. Keep it to one level unless an actual second level of global context requires more. Show only actions the portal implements. Keep global scope, page view and local filters distinguishable.

Left navigation is normally 200–232px with icons and text labels. It provides stable primary sections. Use one selected item with a tinted surface and a marker. Nested groups can disclose inside the same column. A second permanent application rail is justified only by multiple real workspaces.

The central surface owns the selected subject. Right context is usually 200–240px and contains a page outline or relevant links. Collapse it before squeezing a diagram or comparison. A service/document profile must not become a narrow side panel beside a large navigation map.

## Page anatomy

1. Breadcrumb or scope context.
2. Clear title and short purpose; important status/qualification nearby.
3. Relevant page actions.
4. Horizontal views or tabs, where the same subject has alternate content.
5. Central reading/working content with optional right context.

Reserve stable space for the initial layout. Font/data loading should not move a small central panel into a large one after paint. Load fonts locally with `font-display: swap`; keep sensible fallbacks and avoid vertical centring of the whole working region.

## Navigation versus tabs

Use links for navigation to another page or URL-addressable view. Show `aria-current="page"` on the active link. Use tabs for alternate panels within one page: tablist, tab, tabpanel, selected state, arrow/Home/End keyboard movement and one active tab stop. A visual underline alone does not implement tab semantics.

Provide a skip link before the header. A language change should retain the same subject, view, filters and selection when they remain meaningful; update the document language and label any untranslated-content fallback. Keep global scope, view/lens selection and local filtering as distinct controls. A scope change must not silently imply a different legal or provider boundary.

Keep selection when changing view where the subject remains meaningful. Browser history should return to the previous page and context. Label back/close actions by what they return to. Do not turn every card surface into a competing click target; use a clear main link and separate secondary controls.

## Context and responsive behaviour

| Available width | Adaptation |
| --- | --- |
| Wide desktop | Left navigation, central content and optional right context |
| Medium desktop | Collapse right context; preserve useful central width |
| Tablet/narrow | Collapse primary navigation into a labelled disclosure |
| Mobile | One reading column, stacked tools, 16px gutters; allow nav links to wrap |

A table/diagram may scroll inside its labelled region when genuinely two-dimensional. The whole page must not overflow sideways. Support 320px layouts and text zoom. Keep keyboard focus visible; sticky headers must not cover anchored headings or focused controls.

## Supporting material

A right-hand contents list should not repeat the entire profile. A details disclosure can hold secondary explanation. A dialog is for a focused decision or short task and returns focus to its trigger. A drawer is useful for supplementary inspection only when the main task remains legible. Prefer a normal page for a long record or form.
