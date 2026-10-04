# O! UI/UX kit for AICC

This is the AICC-local home for the shared O! portal style: guidance, semantic tokens, local fonts, curated marks and icons, reusable CSS, working examples and the Cloud LAB flow-first recipe. Use it when creating a new internal O! site or materially changing layout, navigation or components. For content-only edits, keep the page's existing presentation.

Start with [ADOPT.md](ADOPT.md). The [interactive guidance site](site/index.html) renders the editable [design-system sources](design-system/README.md), including [brand foundations](design-system/content/foundations.md), [layout](design-system/content/layout.md), [patterns](design-system/content/patterns.md) and the [Cloud LAB recipe](design-system/content/cloud-lab.md). The accepted [Cloud LAB page](../html/cloudlab/index.html) is the concrete AICC reference.

| Home | Role |
| --- | --- |
| `design-system/content/*.md`, `design-system/ADOPT.md` | Canonical explanations and adoption method |
| `design-system/{theme.json,workspace.css,shell.html,app.js}` | Guide preset, shell and working examples |
| `tokens/` | Base semantic design tokens |
| `ui-comps/` | Curated source assets, fonts, licences and UI primitives |
| `site/` | Generated static guide, examples and downloadable implementation kit |

The current shared font pair is TT Norms Pro for headings and Golos Text for text/UI. AICC's existing `portal/` still builds with its earlier TT Travels Text theme. This kit guides new work; adopting it in that portal requires an explicit restyle of that portal's own tokens and components. The two token sets are separate editable sources, not a synchronized library. See [asset use](ASSETS.md). The guide text is English; its shell and working examples support Russian and English. The examples use fictional browser-only records.

This is an editable local copy of the EA shared style source taken on 2 October 2026, with the accepted Cloud LAB pattern added here. Changes to this AICC copy need deliberate reconciliation with the EA shared guide; copying a generated page alone does not update its source.

Build and check from the AICC repository root:

```sh
python3 obank-uiux/design-system/build.py --output obank-uiux/site
python3 obank-uiux/design-system/check_package.py obank-uiux/site
```

Edit the source directories above and rebuild; do not hand-edit `site/`. The site can be served as static files, and its `o-uiux-kit.zip` is portable within the stated internal-use restrictions. [Verification](verification.md) records this local package's checks.
