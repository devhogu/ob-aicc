# Kit evaluation against the collected O! UI/UX material

2 October 2026. Compared this kit with EA's public-site brand research, internal-site screenshot interpretation, component contracts, asset catalogue and the accepted Cloud LAB C page, plus AICC's current portal theme. This is a working design evaluation, not an official group-brand certification.

## Assessment

The kit is a usable common **visual and interaction foundation**: one O! identity, semantic light/dark tokens, TT Norms Pro + Golos Text, central working space, responsive navigation, local assets, seven functional examples and a flow-first Cloud LAB recipe. It captures the practitioner's preferred convergence of the O! workspace shell with a visible map. The guide's browser checks establish its own behaviour; they do not establish that every consuming portal has adopted or passed the same checks.

| Collected material | What it adds without competing | Disposition |
| --- | --- | --- |
| EA `portal/docs/components/` | Precise semantics for scope/search, records, states and visual types | Distilled the missing visual-meaning and language/navigation rules into the kit's existing Components and Layout pages; detailed contracts remain EA references for real product work. |
| EA `portal/ui-comps/CATALOG.md` and manifest | Human asset names, intended use and source context for 108 curated visuals | Copied the manifest-matched catalogue into `ui-comps/`; `ASSETS.md` now distinguishes source inventory from the smaller downloadable guide selection. |
| EA public-site captures, 12 September | Evidence of family resemblance and provider differences | Keep as research in EA. Copying screenshots, source CSS, raw fonts or provider themes into the default kit would confuse observation with shared style. |
| Five supplied internal-site screenshots, 1 October | Compact branded header, quiet work surface, dense lists, broad map canvas | Already reflected in the preset and layout. They are one themed platform plus a separate document-layout reference, not proof of an official group system. |
| Cloud LAB A/B/C comparison | B's O! shell with A's visible six-stage map, capability strip, loop and two-system view | C is the concrete accepted example. Its six stages, five concerns, 41 cards and narrative are not universal rules. The trial's cards lack durable record IDs; a data-driven map will need them. |
| AICC `portal/` theme | Existing active portal uses TT Travels Text and its own copied tokens | Leave its current implementation intact. New work can use this kit; migrating that portal is a separate restyle, with one token owner chosen for the result. |

## Practical limits and next use

- The standalone `site/o-uiux-kit.zip` is a **selected implementation kit**, not the complete 108-asset research inventory or the Cloud LAB page source. This repository holds the full curated asset source, and `html/cloudlab/` holds the accepted page.
- The shell and examples have RU/EN UI; the explanatory guidance is currently English. A Russian-first product still needs its actual content and UI messages localized from one source of identities and facts.
- Visual grammar is now explicit, but this kit does not implement a production graph, catalogue backend, CMS, identity/permissions, export or content publication boundary. Those belong to a consuming portal and its own verified task.
- The [STS design trial](../sts-portal/README.md) now provides a second page-family proof: eight retained pages under the common shell, a lifecycle front door, preserved outer/inner model and practice references, and verified mobile/keyboard behaviour. Its practice catalogue remains a classification, not a process flow. This establishes reuse on that conceptual corpus, not adoption by AICC's current production portal.

Detailed source context: EA `portal/research/brand-2026-09-12/README.md`, `portal/docs/internal-workspace-style.md`, `portal/docs/components/`, `portal/ui-comps/README.md`, and `html-obank/convergence-notes.md`.
