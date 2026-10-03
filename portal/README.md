# AICC portal source

Editable home for the AICC charter site: the interface kit, the page chrome, the messages, and the build tools. The generated site goes to `../html/aicc/` and is never edited by hand.

## How the site is built

| Input | Holds |
| --- | --- |
| `../charter/{en,ru}/**/*.md` | The content of each document, workflow, guide, and template |
| `../portal-scaffolding/sitemap.json` | The structure: sections, pages, addresses, and which sections of a document each page holds |
| `ui/` | The O! UI/UX kit: tokens, fonts, workspace CSS, the O! mark, and icons (copied from `../obank-uiux/site`) |
| `site/charter.css`, `site/site.js` | The additions of the charter site: layout, diagrams, theme switch, search, control filter, template copy |
| `messages/en.json`, `messages/ru.json` | The interface text in English and Russian |
| `content/authored.json` | The authored chrome: section introductions, home text, reading routes (English and Russian) |
| `content/{en,ru}/**/*.md` | Explanatory pages, courses, service descriptions, and references; governing rules come from the charter |

The build converts the Markdown with clause anchors, links each cross-reference such as Operating Model 6.6 to its clause, draws each Mermaid diagram to SVG in a light and a dark variant, wraps the tables, and writes `html/aicc/{en,ru}/`. The build selects reviewed Russian source files when available. Missing or draft translations show the English source with an explicit language notice. A reviewed translation whose source has changed fails validation until it is reconciled. The language switch is at the top right of every page and leads to the same page in the other language. The theme is light by default and can be switched to dark.

## Build and check

```sh
python3 portal/tools/build.py            # regenerate html/aicc/ (the first run draws the diagrams, which takes about a minute; later runs use portal/.cache)
python3 portal/tools/check_sources.py    # pinned English sources and all Russian translation metadata
python3 -m unittest discover -s portal/tests  # language selection through the real renderer
python3 portal/tools/check.py            # links, anchors, language parity, one h1 per page, no request to another host
```

The diagrams are drawn with Mermaid CLI and the headless browser of this host. The paths are set in `tools/build.py` and can be overridden with `MMDC_NPX`, `MMDC_CHROME`, and `MMDC_LIBS`. `tools/browser_check.py` and `tools/setup_browser*.sh` are the earlier browser checks of the first portal slice. Language selection is covered by `tests/test_localization.py`; the static check covers the current full page set.

## Language sources

The language source trees are `charter/{en,ru}/`, `registry/{en,ru}/`, `portfolio/{en,ru}/`, and `portal/content/{en,ru}/`. Matching language versions use the same filenames and folders. The root READMEs are navigation; Russian workspace READMEs and `.gitkeep` files are scaffolding, not translated documents. Shared UI strings remain in `messages/{en,ru}.json`, and authored bilingual chrome remains in `content/authored.json`.

No language is designated authoritative. Language versions share record identities, dates, decisions, statuses, and quantities. Changes may originate in either language. Divergence is reconciled against approved decisions and change history to establish which version has drifted; language alone does not determine which wording is retained. Translating a record never grants an approval or creates a second decision history. The build validates record identifiers and ISO dates; semantic equivalence of translated statuses and wording is part of the translation review.

The current build uses English paths and hashes as comparison references for the initial Russian translation. This technical arrangement does not establish language precedence. A mismatch requires reconciliation of both versions; the comparison reference may need correction.

A translation retains the original six metadata fields when the source has them, changes only the identifier's language suffix, and adds the following fields in the opening YAML fence:

```yaml
source: charter/en/documents/business-model.md
source_revision: 2.1
source_sha256: <SHA-256 of the exact English file bytes>
translation_status: draft
```

`source_revision` is required for a versioned source. Every translation, including explanatory Markdown without a document identifier, records `source`, `source_sha256`, and `translation_status`. Obtain the digest with `sha256sum` on the English file. Set `translation_status: reviewed` only after the translation is reviewed for the professional terminology, normative force, references, and factual equivalence. Drafts remain out of the published body. A stale reviewed source fails the build instead of silently serving an outdated translation.

Preserve filenames, numbered headings, clause numbers, and table row/column order. Table headings and text may be translated; the generator keeps canonical column identities. Ordinary Markdown links use the matching relative language tree. `page:` references use stable sitemap page IDs, which are language independent. Cross-references recognize English document aliases and the titles of reviewed Russian documents; explicit Markdown links remain available for other wording. Mermaid labels may be translated while node IDs and edges stay the same.

The build renders each language independently, including clause links, search, diagrams, metadata, and template copy text. Generated control and role views use translated sources once all their contributing documents are reviewed; until then the whole generated view remains marked English. The corpus baseline remains edition 2.2. The language migration preserved the nine governing documents; the subsequent wording correction is recorded as Document Catalog revision 2.1.

The complete generated `html/aicc/` tree is promoted to the existing deployment repository. Registry and Portfolio translations do not add live records to the public portal; the current publication scope stays unchanged.

## Baseline for translation

The approved corpus baseline is **2.2, 3 October 2026**, initially prepared in English, established by [DR-2026-063](../registry/en/decisions/DR-2026-063-approved-english-baseline.md). This is the edition of the source set, not the revision of every document. The Business Model, Portfolio Management Model, Solution Lifecycle Model, Vocabulary, and Document Catalog carry correction revision 2.1. The other three revised governing documents remain at 2.0, the Statement of Intent at 1.0, the nine previously amended templates at 1.1, and the other templates at 1.0.

`translation-source.json` identifies the English source files and their SHA-256 hashes, including the corpus, Registry, Portfolio, explanatory pages, English interface messages, English fields of the authored content, and page routing. It records the exact source set prepared for translation. Its entries for documents and templates include their identifiers, revisions, and statuses. A later edit requires reconciliation of the affected language versions against recorded decisions and change history; this manifest does not give English precedence and is not updated merely because a translation is added.

The charter review is settled, and all four Standing Initiative Briefs are Approved with no open sections. Their initial measures and shared capacity limits are recorded in the Briefs and the Registry boards. Operational states in the Registry and the Portfolio describe execution; they do not reopen the approved charter baseline.

The Russian routes currently show labeled English content where no translation exists. Translated documents retain the source identifier with the language suffix changed and identify the source revision, as the Document Catalog requires. Operational records retain their actual statuses: a proposed Initiative, unapproved AI use, open deficiency, or unverified instrument remains so in every language. The vocabulary distinguishes a service offered by AICC from the defined Solution type Service, an intake mode from a Kanban lane, a service step from a state, and an Investment Guardrail from a platform guardrail.

## Provenance

`ui/` is a copy of the shared O! UI/UX kit of `../obank-uiux` (internal-use fonts: see `ui/assets/FONT-USE.md`). `legacy/` holds the first slice of the portal (a home page and the statement of intent, built from JSON) and is kept until the new site is accepted. Publishing outside the bank network needs a new decision.
