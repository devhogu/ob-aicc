# Adopt the shared O! portal style

Use this guide when creating or materially restyling an internal O! portal, page layout, navigation, component or UI example. It applies across service, knowledge, document and management portals. For content-only edits, preserve the established design and read only the relevant pattern if presentation changes.

## Read and reuse

1. Read [foundations](content/foundations.md) and [layout](content/layout.md), then the relevant [component rules](content/components.md) and [functional pattern](content/patterns.md). For a stage-by-concern map or flow-first workspace, read the [Cloud LAB pattern](content/cloud-lab.md).
2. Use the generated `tokens.css`, `workspace.css`, `primitives.css`, `fonts.css` and selected `assets/` from `obank-uiux/site/`. Build them from `obank-uiux/design-system/`; the curated assets live in `obank-uiux/ui-comps/` and base tokens in `obank-uiux/tokens/tokens.json`.
3. Start with the closest working example. Preserve central content, supporting navigation, readable labels and existing keyboard behaviour. Replace fictional data through the consuming application's content model.
4. Implement only controls that have a real action. Keep business uncertainty, runtime errors and empty search results distinguishable. Role labels do not imply authorization or actual assignments.
5. Check the changed page in light/dark, Russian/English or explicit untranslated-content fallback, desktop and narrow widths. Exercise the relevant keyboard path, empty/error states, real navigation and data interaction. Report what was actually verified and any limitation.

## Shared decisions and authority

The versioned internal-workspace preset owns the common palette/layout values; shared CSS owns the common shell/components; original asset homes own fonts, logos and icons. Modify that source when a reusable design change is needed. A portal may add domain-specific visualizations and content, using these roles and patterns. Explain any necessary deviation beside the component rather than silently creating another theme.

This is the working shared portal standard, not a corporate approval system. It adds no permission ceremony and grants no authority to deploy, publish, contact people or change enterprise facts. Existing user authorization and repository instructions still govern the work.

For another repository, copy the versioned generated kit and these instructions into its shared UI home and provide a conditional entry link there. In AICC, the repository README links this kit for new UI and material restyling. The generated root `AGENTS.md` is owned by dev-pipe and is not edited by this package. Do not claim another application has adopted the style merely because the guide exists.

## Completion evidence

A useful delivery identifies the pattern used, the source of common assets/tokens, the actual functional path checked and the remaining design/content limits. Screenshots alone do not prove keyboard, responsive or data behaviour. Check source and generated output together so that the next build reproduces the result.
