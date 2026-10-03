# AICC portal source

Editable home for the AICC charter site: the interface kit, the page chrome, the messages, and the build tools. The generated site goes to `../html/aicc/` and is never edited by hand.

## How the site is built

| Input | Holds |
| --- | --- |
| `../charter/**/*.md` | The authoritative content of each document, workflow, guide, and template |
| `../portal-scaffolding/sitemap.json` | The structure: sections, pages, addresses, and which sections of a document each page holds |
| `ui/` | The O! UI/UX kit: tokens, fonts, workspace CSS, the O! mark, and icons (copied from `../obank-uiux/site`) |
| `site/charter.css`, `site/site.js` | The additions of the charter site: layout, diagrams, theme switch, search, control filter, template copy |
| `messages/en.json`, `messages/ru.json` | The interface text in English and Russian |
| `content/authored.json` | The authored chrome: section introductions, home text, reading routes (English and Russian) |
| `content/**/*.md` | English explanatory pages, courses, service descriptions, and references; governing rules come from the charter |

The build converts the Markdown with clause anchors, links each cross-reference such as Operating Model 6.6 to its clause, draws each Mermaid diagram to SVG in a light and a dark variant, wraps the tables, and writes `html/aicc/{en,ru}/`. The Russian pages carry the Russian interface and the English text, labelled as English, until a Russian text exists. The language switch is at the top right of every page and leads to the same page in the other language. The theme is light by default and can be switched to dark.

## Build and check

```sh
python3 portal/tools/build.py            # regenerate html/aicc/ (the first run draws the diagrams, which takes about a minute; later runs use portal/.cache)
python3 portal/tools/check.py            # links, anchors, language parity, one h1 per page, no request to another host
```

The diagrams are drawn with Mermaid CLI and the headless browser of this host. The paths are set in `tools/build.py` and can be overridden with `MMDC_NPX`, `MMDC_CHROME`, and `MMDC_LIBS`. `tools/browser_check.py` and `tools/setup_browser*.sh` are the earlier browser checks of the first portal slice and need updating for the new pages.

## English source for translation

The approved English source baseline is **2.2, 3 October 2026**, established by [DR-2026-063](../registry/decisions/DR-2026-063-approved-english-baseline.md). This is the edition of the source set, not the revision of every document. The Business Model, Portfolio Management Model, Solution Lifecycle Model, and Vocabulary carry correction revision 2.1. The other four revised governing documents remain at 2.0, the Statement of Intent at 1.0, the nine previously amended templates at 1.1, and the other templates at 1.0.

`translation-source.json` identifies the English source files and their SHA-256 hashes, including the corpus, Registry, Portfolio, explanatory pages, English interface messages, English fields of the authored content, and page routing. It records the exact source set prepared for translation. Its entries for documents and templates include their identifiers, revisions, and statuses. A later source edit requires reconciliation of the affected translation against that changed source; the manifest is not updated merely because a translation is added.

The charter review is settled, and all four Standing Initiative Briefs are Approved with no open sections. Their initial measures and shared capacity limits are recorded in the Briefs and the Registry boards. Operational states in the Registry and the Portfolio describe execution; they do not reopen the approved charter baseline.

The Russian routes currently show labeled English content where no translation exists. Translated documents retain the source identifier with the language suffix changed and identify the source revision, as the Document Catalog requires. Operational records retain their actual statuses: a proposed Initiative, unapproved AI use, open deficiency, or unverified instrument remains so in every language. The vocabulary distinguishes a service offered by AICC from the defined Solution type Service, an intake mode from a Kanban lane, a service step from a state, and an Investment Guardrail from a platform guardrail.

## Provenance

`ui/` is a copy of the shared O! UI/UX kit of `../obank-uiux` (internal-use fonts: see `ui/assets/FONT-USE.md`). `legacy/` holds the first slice of the portal (a home page and the statement of intent, built from JSON) and is kept until the new site is accepted. Publishing outside the bank network needs a new decision.
