# AICC portal source

Editable home for the AICC portal: the interface kit, page chrome, messages, neighbouring sections and build tools. The generated site goes to `../html/aicc/` and is never edited by hand.

## Branches

The site has one language-first layout. `html/aicc/index.html` forwards to `en/`; `html/aicc/{en,ru}/index.html` is the router of each language, which holds only the five branch doors. There are no other routes and no redirect stubs. The five branches share one O!Bank shell: branding, the left navigation of all branches with the current one marked, the language switch to the same page in the other language, the theme switch, page feedback and search. Each branch owns its source, content, local navigation, search index and checks. Content bodies do not link across branches except the recorded Initiative–project relationship between Portfolio and Program, and charter terminology links or document status are not added to the other branches.

| Branch | Route within each language | Source | Builder |
| --- | --- | --- | --- |
| Center | `center/` | `../charter/{en,ru}/`, `../registry/{en,ru}/`, `content/` and `sections/center/sitemap.json` | `tools/build.py` |
| Discovery Catalog | `discovery/` | `../portfolio/{en,ru}/discovery/`: one Markdown record for each of the 76 pages per language | `tools/discovery.py`, `tools/neighbours.py` |
| Portfolio | `portfolio/` | `../portfolio/{en,ru}/`: the Portfolio Backlog, board, Initiative Briefs and roadmap | `tools/portfolio.py` |
| Program | `program/` | `../portfolio/{en,ru}/`: the Program Backlog, and `../portfolio/{en,ru}/projects/<key>/` for the documents of each project | `tools/delivery.py`, `tools/project.py` |
| AI Lab | `lab/` | `../lab/{en,ru}/lab.md` | `tools/lab.py` |

`sections/navigation.json` defines the five branches, their routes and icons; `sections/pages.json` lists the branch landing pages. `sections/portfolio/` and `sections/program/` hold the authored landing text and the project mapping. `tools/workspace.py` renders the common shell, `tools/router.py` the routers, and `tools/neighbours.py` composes Discovery, Portfolio, Program and AI Lab. Every count on the router is taken from the branch's sources when the site is built.

Search covers the current branch by default. The box beside it, "All of AICC" (Russian «Весь сайт AICC»), adds every branch index and names the branch of each result; on the routers it is on by default. Without scripts the box has no effect and every page remains reachable through links. Page feedback references are stable: a page whose route changed keeps the reference of its former route.

## How the site is built

| Input | Holds |
| --- | --- |
| `../charter/{en,ru}/**/*.md` | The content of each document, workflow, guide, and template |
| `sections/center/sitemap.json` | The structure: sections, pages, addresses, and which sections of a document each page holds |
| `ui/` | The O! UI/UX kit: tokens, fonts, workspace CSS, the O! mark, and icons (copied from `../obank-uiux/site`) |
| `site/charter.css`, `site/site.js` | The additions of the charter site: layout, diagrams, theme switch, search, control filter, template copy |
| `messages/en.json`, `messages/ru.json` | The interface text in English and Russian |
| `content/authored.json` | The authored chrome: section introductions, home text, reading routes (English and Russian) |
| `content/{en,ru}/**/*.md` | Explanatory pages, courses, service descriptions, and references; governing rules come from the charter |

The build converts the Markdown with clause anchors, links each cross-reference such as Operating Model 6.6 to its clause, draws each Mermaid diagram to SVG in a light and a dark variant, wraps the tables, and writes the Center branch to `html/aicc/{en,ru}/center/`. The build selects reviewed Russian source files when available. Missing or draft translations show the English source with an explicit language notice. A reviewed translation whose source has changed fails validation until it is reconciled. The language switch is at the top right of every page and leads to the same page in the other language. The theme is light by default and can be switched to dark.

## Build and check

```sh
python3 portal/tools/build.py            # regenerate html/aicc/ (the first run draws the diagrams, which takes about a minute; later runs use portal/.cache)
python3 portal/tools/check_sources.py    # pinned English sources and all Russian translation metadata
python3 -m unittest discover -s portal/tests  # language selection through the real renderer
python3 portal/tools/check.py            # layout, every href/src and search result, anchors, language parity, one h1 per page, no external resource loads (citations allowed)
python3 portal/tools/check_neighbours.py # router doors, branch boundaries, branch and global search, retained scenario content
python3 portal/tools/check.py --idempotent # complete-site repeatability; run before the browser sweep
portal/tools/with-browser-env.sh portal/.venv/bin/python portal/tools/check_neighbours_browser.py
```

The complete-site build includes the routers and all five branches. Run the browser sweep after the build and freshness check finish; rebuilding concurrently removes files that the browser is reading. The sweep covers the new pages in both languages, desktop/mobile layouts, light/dark themes, retained interactions, branch navigation, the router doors, branch and global search, and the Center controls. It also verifies a disposable direct-file export without refreshing `published/`. Its report is written to `.runtime/portal-neighbours/browser-report.json` at the repository root. Regeneration of the corporate-share package remains an explicit action; see [PORTABLE-HOWTO.txt](PORTABLE-HOWTO.txt).

The diagrams are drawn with Mermaid CLI and the headless browser of this host. The paths are set in `tools/build.py` and can be overridden with `MMDC_NPX`, `MMDC_CHROME`, and `MMDC_LIBS`. `tools/browser_check.py` and `tools/setup_browser*.sh` are the earlier browser checks of the first portal slice. Language selection is covered by `tests/test_localization.py`; the static check covers the current full page set.

## Language sources

The language source trees are `charter/{en,ru}/`, `registry/{en,ru}/`, `portfolio/{en,ru}/`, and `portal/content/{en,ru}/`. Matching language versions use the same filenames and folders. The root READMEs provide navigation. The Russian charter, Registry, and Portfolio READMEs are reviewed translations of their reading maps; `.gitkeep` files remain scaffolding. Shared UI strings remain in `messages/{en,ru}.json`, and authored bilingual chrome remains in `content/authored.json`.

No language is designated authoritative. Language versions share record identities, dates, decisions, statuses, and quantities. Changes may originate in either language. Divergence is reconciled against approved decisions and change history to establish which version has drifted; language alone does not determine which wording is retained. Translating a record never grants an approval or creates a second decision history. The build validates record identifiers and ISO dates; semantic equivalence of translated statuses and wording is part of the translation review.

The current build uses English paths and hashes as comparison references for the initial Russian translation. This technical arrangement does not establish language precedence. A mismatch requires reconciliation of both versions; the comparison reference may need correction.

A translation preserves the source revision, status and dates when present, translates the title, changes the identifier's language suffix, and adds the following fields in the opening YAML fence:

```yaml
source: charter/en/documents/business-model.md
source_revision: 2.1
source_sha256: <SHA-256 of the exact English file bytes>
translation_status: draft
```

`source_revision` is required for a versioned source. Every translation, including explanatory Markdown without a document identifier, records `source`, `source_sha256`, and `translation_status`. Obtain the digest with `sha256sum` on the English file. Set `translation_status: reviewed` only after the translation is reviewed for the professional terminology, normative force, references, and factual equivalence. Drafts remain out of the published body. A stale reviewed source fails the build instead of silently serving an outdated translation.

Preserve filenames, numbered headings, clause numbers, and table row/column order. Table headings and text may be translated; the generator keeps canonical column identities. The shared terminology reference has a declared exception: its Russian term tables add «Русскоязычный термин» immediately after «Универсальный термин». The validator checks that column, the universal row identities and the remaining table structure; other tables retain exact row and column parity. Ordinary Markdown links use the matching relative language tree. `page:` references use stable sitemap page IDs, which are language independent. Cross-references recognize English document aliases and the titles of reviewed Russian documents; explicit Markdown links remain available for other wording. Mermaid labels may be translated while node IDs and edges stay the same.

The build renders each language independently, including clause links, search, diagrams, metadata, and template copy text. Generated control and role views use translated sources once all their contributing documents are reviewed; until then the whole generated view remains marked English. The corpus baseline remains edition 2.2. The language migration preserved the nine governing documents; the subsequent wording correction is recorded as Document Catalog revision 2.1, and Russian availability of the governing documents as revisions 2.2 through 2.5.

The complete generated `html/aicc/` tree is promoted to the existing deployment repository when publication is requested. Registry and Portfolio corpus translations do not populate the independent live registers.

## Baseline for translation

The approved corpus baseline is **2.2, 3 October 2026**, initially prepared in English, established by [DR-2026-063](../registry/en/decisions/DR-2026-063-approved-english-baseline.md). This is the edition of the source set, not the revision of every document. The Business Model and Solution Lifecycle Model carry correction revision 2.1. DR-2026-064 subsequently reconciled industry terminology: Vocabulary and Style and Document Catalog are at 3.1, including the correction for separate terminology editions, and Portfolio Management Model is at correction revision 2.2. All nine governing documents remain available in English and Russian. The other three revised governing documents remain at 2.0, the Statement of Intent at 1.0, the nine previously amended templates at 1.1, and the other templates at 1.0.

`translation-source.json` identifies the English source files and their SHA-256 hashes, including the corpus, Registry, Portfolio, explanatory pages, English interface messages, English fields of the authored content, and page routing. It records the exact source set prepared for translation. Its entries for documents and templates include their identifiers, revisions, and statuses. A later edit requires reconciliation of the affected language versions against recorded decisions and change history; this manifest does not give English precedence and is not updated merely because a translation is added.

The charter review is settled, and all four Standing Initiative Briefs are Approved with no open sections. Their initial measures and shared capacity limits are recorded in the Briefs and the Registry boards. Operational states in the Registry and the Portfolio describe execution; they do not reopen the approved charter baseline.

All 39 original charter files are translated and reviewed in Russian: nine governing documents, five guides and their index, six workflows and their index, fourteen templates and their index, the executive summary, and the charter reading map. Corpus-derived pages, document references, diagrams, search and template copies follow the Russian sources. All 42 Registry files and all 15 Portfolio files are now translated and reviewed, preserving their recorded dates, identifiers, decisions and operational states. All user-facing strings in `content/authored.json` have Russian counterparts. All 117 independently authored Markdown pages are translated: About (2), Services (23), Organization (6), Governance (7), Knowledge base (7), Delivery (14), Portfolio (9), Responsible AI (7), Reference (40), and the two legal pages. The complete inventory is in [the Russian content index](content/ru/README.md). The 229 original Russian routes use reviewed Russian content; composite pages also use the selected Russian sources. The new Shared Business and Technology Terminology companion adds a 230th route in each language. Both editions contain all 71 terms, with definitions and application in the language of their corpus. The Russian route uses its reviewed Russian source without an English-content notice. Each charter language directory now contains 40 files. The core terminology amendments are paired in English and Russian; a full rewrite of existing Russian prose using every selected shared form is a subsequent pass. Translated documents retain the source identifier with the language suffix changed and identify the source revision, as the Document Catalog requires. Operational records retain their actual statuses: a proposed Initiative, unapproved AI use, open deficiency, or unverified instrument remains so in every language. The vocabulary distinguishes a service offered by AICC from the defined Solution type Service, an intake mode from a Kanban lane, a service step from a state, and an Investment Guardrail from a platform guardrail.

## Provenance

`ui/` is a copy of the shared O! UI/UX kit of `../obank-uiux` (internal-use fonts: see `ui/assets/FONT-USE.md`). `legacy/` holds the first slice of the portal (a home page and the statement of intent, built from JSON) and is kept until the new site is accepted. Publishing outside the bank network needs a new decision.

The following batch notes describe the state at each completed step; the current inventory is above.

## Russian foundation batch

The first batch translates the complete Vocabulary (169 defined terms, 13 states and 12 stages) and Document Catalog. Spelling, obligation wording and heading capitalization follow Russian usage; identifiers, decision rights, definitions and clause numbers remain aligned. The site derives Russian document-reference titles from the translated Catalog, including references to documents whose body is still available only in English. Common Russian inflections resolve to the same clauses. Document status labels and the surrounding source-file controls use Russian interface text.

This batch is prepared in the source checkout and generated output; it does not by itself record a live deployment. Other corpus documents, records and explanatory site content remain to be translated.

## Russian mandate batch

The second batch translates the complete Statement of Intent (revision 1.0) and AICC Charter (revision 2.0), retaining obligations, decision rights, risk appetite, funding limits, measures and reporting. Both Catalog versions record their availability at revision 2.3. The home, about and strategy pages use Russian priorities and maturity tables from the Statement; the values page reads the mission directly from Charter 2.1 and the values and principles from Statement sections 4–6. Other source documents and authored explanatory text on these composite pages remain to be translated and retain their language identification.

The translations and generated pages are available in the source checkout and private preview. No live deployment is recorded for this batch.

## Russian business and operating batch

The third batch translates the Business Model (revision 2.1) and Operating Model (revision 2.0), including all 15 service categories, seven Roles, five control loops, ten governance measures, 32 controls and eight diagrams. Clause numbers, control and decision identifiers, dates, diagram node identifiers and transitions remain aligned. Source-language business rules are unchanged. Both Catalog versions record availability at revision 2.4.

The site renders the two documents and Operating Model sections across Organization and Governance from the Russian corpus. Work principles on the values page now follow the Russian Operating Model. Russian figure captions supply visible captions and accessible diagram names. Detailed role and control profiles still use English while their explanatory guides remain untranslated; the mixed controls overview identifies this explicitly. The source checkout and private preview are updated, with no live deployment recorded.

## Russian governing-document completion batch

The fourth batch translates the Portfolio Management Model and Solution Lifecycle Model (revision 2.1) and AI Policy (revision 2.0), completing all nine governing documents. Both Catalog versions record availability at revision 2.5. Investment decisions, all state transitions, three acceptance levels, release authority, risk-tier requirements, service operations, measures and 21 diagrams retain the source meaning and structure. Delivery principles on the values page now follow the Russian lifecycle model.

Guides, workflows, templates, operational records and authored explanatory pages remain to be translated. Corpus-derived pages use the reviewed Russian documents, while untranslated material keeps its language identification. The source checkout and private preview are updated; this batch does not include live deployment.

## Russian organization and governance guidance batch

The fifth batch translates the Organization guide, Unit governance guide and Unit governance workflow, together with the guide and workflow indexes that supply portal descriptions. All RACI assignments, 32 control objectives and audit checks, reporting and incident sequences, and diagram connections preserve the comparison sources. The seven role profiles, 32 control profiles, control catalogue and their navigation now render from the reviewed Russian corpus; split guide and workflow tabs follow Russian headings.

This brings the reviewed translation inventory to 14 files: nine governing documents, two guides, one workflow and two indexes. Remaining guides and workflows, templates, operational records and authored explanatory content remain untranslated. Sources and private preview are updated; this batch is uncommitted and not deployed.

## Russian charter completion batch

The sixth batch completes the remaining 25 charter files: three guides, five workflows, fourteen templates and their index, the executive summary, and the charter reading map. All 36 diagrams in the new guides and workflows preserve node identities and connections. Table structures, numbered references, decision rights, time periods, template fields and the Steering review schedule are retained. Terminology follows the Russian Vocabulary and governing documents; comparison-source hashes remain unchanged.

The portal uses the translated corpus for guide, workflow and template pages and record-form descriptions. Split-page tabs use concise Russian labels. Template copy starts at the title and excludes metadata in both languages, as Document Catalog 6.1 requires. Translated descriptions on mixed navigation pages identify their actual language. Forms without section headings, including Control Sign-Off, remain discoverable in both language search indexes.

The source checkout and generated output are updated. This batch is uncommitted and not deployed; charter completion does not imply that the Registry, Portfolio or all authored site explanations are translated.

## Russian records and authored-content continuation

The first part of the continuation translated the complete Registry and Portfolio, all authored JSON, and 47 authored Markdown pages. Historical approval quotations were retained with Russian translations; unverified external references, proposed Solutions, open operational deficiencies, and blank template fields retained their source state. New explanatory pages followed the reviewed charter vocabulary, decision rights and support commitments.

Generated Strategy tables, Values, record-system descriptions, reference headings, service tabs and navigation used Russian text. Language notices followed the sources actually selected; unfinished explanatory pages retained their English notice. English source fingerprints remained unchanged. At that point, C-RU-CORPUS-PORTAL still had 70 explanatory pages and final verification to complete. This batch was uncommitted and not deployed.

Verification of the earlier records and authored-content batch: 215 pinned English sources verified; 142 reviewed Russian counterparts validated; 13 localization tests passed; all 458 pages and 178 diagrams rendered; source scaffolding and generated-site checks passed; a repeat build left all 475 output files unchanged. Browser checks covered all 47 new source pages at desktop and mobile widths, the generated bilingual pages, search results, diagram zoom and language counterparts (115 page checks including English references). The new translated Markdown preserved link targets, empty table cells and diagram connections. GRACE lint reported no errors and the same six existing heuristic warnings. This recorded the intermediate batch; the completion below supersedes its outstanding translation count.

## Russian corpus and portal completion

The final part completes the remaining 70 explanatory pages: Reference (40), Delivery (14), Portfolio (9), and Responsible AI (7). All 117 authored Markdown pages and 237 authored JSON fields now have Russian counterparts, alongside the 39 charter, 41 Registry, and 15 Portfolio files. Terminology follows the Russian corpus, including accountability, control loops, verification, benefits, operating costs, Initiative Mix, and retirement rules. Markdown link targets, numbered clauses, table structures and empty fields, and Mermaid node and edge identities are preserved.

Every Russian HTML page now uses reviewed Russian sources or Russian authored content. The 229 routes include translated navigation, search, document references, diagrams, control and role profiles, and copyable templates. There are no English fallback bodies or language notices in the generated Russian tree. Product names, identifiers, source filenames and addresses retain their original forms. References such as «Операционная модель, раздел 4» resolve to the named document's section. Generated pages without source headings are also searchable by title.

Search reads the current query after its index loads, so a late response cannot replace results with those for an earlier query or reopen results after the query is cleared. The regression checks exercise the actual site script with reversed response order and a cleared query; the same delayed-response scenario is verified in the browser.

Final verification on 3 October 2026: all 215 comparison-source fingerprints and 212 reviewed Russian files validated; 15 tests passed, including two site-script search regression cases; 458 pages and 196 diagrams rendered with none missing; all links and anchors resolved; all 475 output files remained identical on a repeat build. Browser inspection covered every Russian page at 1440 and 390 pixels, plus three English reference pages (461 page checks), with no layout overflow, fallback notices, wrong-language navigation or script errors. Follow-up interactions verified all 229 Russian routes in search, result destinations, document-section links, mobile navigation, control filtering, template copying, theme switching, and diagram zoom. The selected GRACE final gate passed all five command assertions with zero errors and the same six existing heuristic warnings. Its command evidence is recorded in the run `2026-10-03T23-11-44_C-RU-CORPUS-PORTAL`.

The source checkout and generated output are updated; this continuation does not include commit, push or deployment.

## Shared industry terminology reconciliation

DR-2026-064 records the owner-approved industry-first naming rule. Vocabulary and Style 3.0 replaces blanket word exclusions with Related terms and adds metric, KPI, SLA, WIP, business case and value stream definitions. The existing WIP limit is an accepted short form. Document Catalog 3.0 and Portfolio Management Model 2.2 align their terminology checks and Jira mapping. Commitments, measurement populations and decision rights are preserved. Edition 1.4 of the shared terminology reference has separate English and Russian sources projected at `reference/shared-terminology`. Each source contains local-language definitions and application. The Russian edition also provides researched Russian-language names after each universal term; search indexes both names from that source. Vocabulary and Style and Document Catalog revision 3.2 retain this language structure and clarify the governing vocabulary’s interpretive purpose. Both vocabulary editions define 176 concepts, 13 states and 12 stage groups with equivalent scope and explicit distinctions. The reconciliation covers acceptance authority, delegation, record classes and business-case meaning against the existing governing clauses. The shared reference remains one accepted set of 71 entries without gray/white classifications.

The international terminology sweep applies the shared reference’s fixed names across both language sources, authored content, navigation and diagrams. Russian definitions and permitted language variants remain local. The current shared reference is edition 1.5; Vocabulary and Style and Document Catalog are revision 3.3. Source correction includes business-acceptor exceptions, evaluation-set scope and record locations in explanatory pages.
