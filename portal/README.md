# AICC portal source

Editable home for the AICC charter site: the interface kit, the page chrome, the messages, and the build tools. The generated site goes to `../html/aicc/` and is never edited by hand.

## How the site is built

| Input | Holds |
| --- | --- |
| `../charter/**/*.md` | The content of every document, workflow, guide, and template. The only authored source of the text |
| `../portal-scaffolding/sitemap.json` | The structure: sections, pages, addresses, and which sections of a document each page holds |
| `ui/` | The O! UI/UX kit: tokens, fonts, workspace CSS, the O! mark, and icons (copied from `../obank-uiux/site`) |
| `site/charter.css`, `site/site.js` | The additions of the charter site: layout, diagrams, theme switch, search, control filter, template copy |
| `messages/en.json`, `messages/ru.json` | The interface text in English and Russian |
| `content/authored.json` | The authored chrome: section introductions, home text, reading routes (English and Russian) |

The build converts the Markdown with clause anchors, links each cross-reference such as Operating Model 6.6 to its clause, draws each Mermaid diagram to SVG in a light and a dark variant, wraps the tables, and writes `html/aicc/{en,ru}/`. The Russian pages carry the Russian interface and the English text, labelled as English, until a Russian text exists. The language switch is at the top right of every page and leads to the same page in the other language. The theme is dark by default and switches to light.

## Build and check

```sh
python3 portal/tools/build.py            # regenerate html/aicc/ (the first run draws the diagrams, which takes about a minute; later runs use portal/.cache)
python3 portal/tools/check.py            # links, anchors, language parity, one h1 per page, no request to another host
```

The diagrams are drawn with Mermaid CLI and the headless browser of this host. The paths are set in `tools/build.py` and can be overridden with `MMDC`, `MMDC_PUPPETEER`, and `MMDC_LIBS`. `tools/browser_check.py` and `tools/setup_browser*.sh` are the earlier browser checks of the first portal slice and need updating for the new pages.

## Provenance

`ui/` is a copy of the shared O! UI/UX kit of `../obank-uiux` (internal-use fonts: see `ui/assets/FONT-USE.md`). `legacy/` holds the first slice of the portal (a home page and the statement of intent, built from JSON) and is kept until the new site is accepted. Publishing outside the bank network needs a new decision.
