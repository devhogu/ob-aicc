# Curated assets and use

The [human asset catalogue](ui-comps/CATALOG.md) and `ui-comps/manifest.json` inventory the same 108 curated source assets; the manifest owns IDs, source URLs, intended use, background and hashes. `site/assets/` contains only the selection used by the standalone guide, not every optional source asset. Use original files and semantic CSS roles; do not redraw provider marks or infer a service's ownership from a logo.

| Source | Use |
| --- | --- |
| `ui-comps/logos/` | O! identity and contextual provider marks, with light/dark variants where supplied |
| `ui-comps/icons/` | Lucide outline UI icons; pair unfamiliar icons with labels |
| `ui-comps/service-icons/`, `web-icons/`, `illustrations/` | Optional contextual illustrations; inspect relevance before use |
| `ui-comps/fonts/tt-norms-pro/` | Shared internal O! headings, 400/500/700 |
| `ui-comps/fonts/golos-text/` | Shared body/UI text, variable font; OFL licence included |
| `ui-comps/fonts/tt-travels-text/` | Compatibility for the existing AICC portal; not the default new-site pair |
| `ui-comps/ui.css`, `tokens/` | Reusable primitives and semantic values |

TT Norms Pro and TT Travels Text follow the practitioner's internal O! portal-use authorization; keep them in internal distributions. Golos Text and Lucide retain their licence files. The generated kit includes an `assets/FONT-USE.md` note. Raw reference captures and SF Pro files are outside this curated kit.

The O! mark is a family identity, not proof of a legal group entity. A provider mark identifies only its named subject. The O!Business menu symbol is not a full wordmark; the My O! mark is not a verified PAM/GTS logo. When the right mark is missing, show the readable name rather than inventing one. The catalogue is generated from the manifest; regenerate it when assets change.
