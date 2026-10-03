# PKG-003 Portal generator

This is a Package Definition under Business Model 4.4, using AICC-TPL-14. Available in the AICC repository and used for the AICC charter, governance records, or portal as specified below. Availability of the material does not grant approval for a new AI use.

| Field | Entry |
| --- | --- |
| Identifier | PKG-003 |
| Title | Portal generator |
| Kind | Engine |
| Service area and category | Build and run; Platforms |
| Status | Available |
| Owner | AICC Lead |
| Produced by | AICC portal development; no originating Initiative or Service Agreement identifier is recorded. |
| Used by or intended use | AICC |
| Needs to re-deploy | A charter pack in the form of PKG-001, a keeper, and a web server of the Bank |
| Risk Tier of its uses | No Risk Tier is assigned to a description or template set alone. Each use that involves AI is tiered under AI Policy 3; the data class, influence on a decision, customer effect, and autonomy determine the tier. |
| Where it is kept | The source references in section 2; English source edition 2.2, with the revision of each document stated in that document. The receiving owner records the repository revision used for an adaptation. |
| Date of last change | 2026-10-03 |

## 1. What it is and what problem it answers

Generates a portal from a charter pack: sections, documents in parts, clause anchors, cross-references, defined terms, diagrams, search, two languages.

## 2. What it contains

- [Portal source and build instructions](../../../portal/README.md).
- [Site map](../../../portal-scaffolding/sitemap.json) and [page scaffolding](../../../portal-scaffolding/README.md).
- [Build tool](../../../portal/tools/build.py) and [static checks](../../../portal/tools/check.py).
- Interface messages, page content, local assets, and the O! UI kit under `portal/`. Source references describe the implementation; no code is embedded in this record.

## 3. How a function re-deploys it

1. The receiving owner provides a charter in the documented Markdown structure, with identifiers, revisions, numbered clauses, tables, and Mermaid diagrams.
2. The tooling keeper adapts the site map, page routing, AICC-specific record parsers, interface messages, and explanatory content to the receiving charter. The generator expects the AICC schema and English source headings; another schema requires adaptation.
3. The keeper prepares Python with markdown-it-py, Node, Mermaid, Chromium, and the local font assets according to the portal build instructions.
4. The keeper generates the static output, checks links, anchors, page parity, and build repeatability, and reviews the rendered pages.
5. The receiving owner authorizes publication through its own access and deployment process. Translation is authored and reviewed separately; the generator does not translate source text.

## 4. Limits and risks

The generated site has English and Russian routes; an untranslated page on the Russian route still contains labeled English text. The tooling is available and used for AICC, but adapting it to another charter is engineering work. Fonts and brand assets retain their existing internal-use terms.

## 5. History

| Date | Engagement or Initiative | Change |
| --- | --- | --- |
| 2026-10-03 | No originating identifier recorded | Definition completed from the existing package catalog and the source references above during English reconciliation. Status retained; no new approval or deployment is asserted. |
