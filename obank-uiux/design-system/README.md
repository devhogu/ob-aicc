# Shared O! UI/UX guide

The common working style for our internal portals: brand, layout, navigation, typography, icons, controls and functional examples. Requested and established as a shared home on 1 October 2026. This AICC copy is version **0.1.1**, adding the accepted Cloud LAB pattern; it can evolve through actual portal use.

**[Open the local guidance site](../site/index.html)** · [Adoption instructions](ADOPT.md) · [Source foundations](content/foundations.md) · [Layout](content/layout.md) · [Patterns](content/patterns.md).

This is an AICC-local, editable copy of the EA shared style source from 2 October 2026. Build output lives in `../site/` and can be hosted as static files. The guide's example records are fictional and are not O! enterprise knowledge.

The accepted [Cloud LAB page](../../html/cloudlab/index.html) is the first AICC application of this style. Its [flow-first pattern notes](content/cloud-lab.md) explain the added map, diagram and sticky-header choices.

## What is included

- Eight guidance sections: start, foundations, layout, components, patterns, Cloud LAB, assets and adoption.
- Seven working examples: overview, searchable catalogue, profile with keyboard tabs, selectable flow, comparison, form/review dialog and activity history.
- Light/dark themes, Russian/English shell and examples, responsive layouts, local fonts and icons.
- An asset browser and downloadable implementation kit, including selected logos, fonts, icons, licence/use notes and adoption instructions.
- A conditional discovery link from the AICC repository README. The generated root `AGENTS.md` is not changed by this copy.

Explanatory guidance is authored in English and labelled as such in the Russian shell. Full Russian guidance translation remains a refinement. This does not add a CMS, user accounts, business editing or a claim that every existing portal has already adopted the style.

## Canonical sources

| Source | Owns |
| --- | --- |
| `content/*.md` | Human-readable common design rules |
| `ADOPT.md` | Designer/developer/agent adoption and completion guidance |
| `theme.json` | Version and internal-workspace overrides on the existing shared base tokens |
| `workspace.css`, `shell.html` | Shared layout and navigation presentation |
| `app.js` | Working example and guide interactions |
| `build.py` | Standalone pages, selected assets, resolved tokens and downloadable kit |
| `../tokens/tokens.json` | Shared base semantic colours, spacing and typography |
| `../ui-comps/` | Original fonts, logos, icons, licence notes and reusable primitives |

The resolved theme is **base tokens + internal-workspace preset**, used identically by every guide page and example. Existing public-site research and earlier style labs remain references. For new internal portal work, this guide is the current composition/style entry point. Domain-specific content models and views stay in their own portal documentation.

## Build and serve

From the AICC repository root, using Python with `markdown-it-py`:

```sh
python3 obank-uiux/design-system/build.py --output obank-uiux/site
python3 -m http.server 8899 --bind 0.0.0.0 --directory obank-uiux/site
```

The downloadable `o-uiux-kit.zip` can be extracted into a standalone static site or used as a source of selected shared assets/CSS. It carries its own manifest and adoption guide. Never hand-edit generated files as the maintained source; change the files above and rebuild.

## Verify

```sh
python3 obank-uiux/design-system/check_package.py obank-uiux/site
AXE_CORE_PATH=/path/to/axe.min.js portal/tools/with-browser-env.sh portal/.venv/bin/python \
  obank-uiux/design-system/verify.py --url http://127.0.0.1:8899 --artifacts /tmp/o-uiux-check
```

The browser check covers the seven examples and eight guide sections in both languages/themes at 1440, 768 and 320px; automated accessibility runs at desktop in both themes. It exercises catalogue-to-profile identity, keyboard tabs, flow selection, form error recovery/dialog focus, comparison/activity filters, global search, mobile navigation and downloads. It needs a local `axe.min.js`; browser checks are bounded evidence, not a substitute for reader testing. Local verification is recorded in [the package report](../verification.md).
