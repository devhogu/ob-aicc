# Brief: validation of the English content of the new portal sections

The AICC portal now has four neighbouring sections next to the charter: Discovery Catalog, Portfolio, Delivery Pipeline, CloudLab. Their English content came from a different corpus and has not been validated. The owner wants every page, every box and every statement read for completeness, sense and sound, and a fix map prepared so that all fixes can be applied in one later round. This task is READ-ONLY on content: do not edit anything except your own notes file and fix-map file.

## Where the content lives

- Discovery Catalog is generated from `html-alt/financial-services/en/**/index.html` (76 pages, 1,101 scenario cards). That folder is the editable source. `html/financial-services` and `html/aicc/en/discovery` are generated from it; do not review them.
- A plain-text extract of every page is in `wiki/research/discovery-review/extract/<area>__<page>.md` (`_root.md` is the overview page). Each scenario card appears as `### CARD n [Lens|Complexity] Title`, with its `urn`, `intent`, `Problem to solve`, `Solution`, and `OKR objective` plus three `OKR KR [Adoption|Acceptance|Cycle]` lines; `(EMPTY)` marks a missing OKR. `[PAGE TEXT]` blocks hold everything outside the cards (page intent, problem rows, section headings and intents, counts, navigation text, stage dialogs). Use the extract for reading; open the source HTML when you need exact wording or structure.
- The anatomy of a page: an area (level 1) has sub-areas (level 2 pages); a page has a header intent, "problems" rows by lens, level-3 sections (title + intent), and scenario cards under each section. A card has a lens (Insights, Automation, Enablement, Optimize, New opps), a complexity (S, M, L, XL), a title, an intent, a problem, a solution, and an OKR (one objective and three key results: Adoption, Acceptance, Cycle).

## What to check, for every page and every card

1. Completeness: missing or empty fields (empty OKR, missing intent, problem, solution, section intent), sections with no cards, counts on the page that do not match what is there (e.g. "(18)" next to a sub-area that has a different number of cards).
2. Broken content: truncated sentences, placeholders (`service.eyebrow`, template tokens), duplicated paragraphs or cards, text pasted into the wrong field, a title that does not match its body, wrong or dangling references.
3. Sense and logic: does the intent say what the scenario does; does the problem state a real problem that the solution answers; does the OKR measure this scenario and not another; is the lens right for what the card does; is the complexity plausible next to its neighbours; does the section intent cover its cards; does the page intent cover its sections; is anything in the wrong sub-area.
4. Sound: clumsy, inflated, or unclear English; sentences that say nothing; over-long sentences; inconsistent naming of the same thing within the page.
5. Fit for O!Bank (a commercial bank in the Kyrgyz Republic, supervised by the NBKR): claims that assume another jurisdiction, product, or scale; regulators or laws cited as if they bind the Bank. Do not rewrite these one by one — see "Global patterns" below — but do flag a card where the scenario itself only makes sense under another jurisdiction.

## Global patterns — do NOT list occurrences one by one

These are already measured across the whole catalog and will be decided once for all pages. Mention them in your notes only if your area has a special case:
- Mixed British and American spelling (optimisation / optimization).
- "CBR" (Bank of Russia) cited next to "NBKR" throughout (449 and 544 times).
- "Agent" used as the actor ("Agent reads…", about 1,500 times) where the AICC corpus says "AI agent".
- "the bank" in lower case.
- The `service.eyebrow` breadcrumb placeholder on every page.

## Empty OKRs

About 319 cards have an empty OKR (areas: customer-channels, customer-market-intelligence, finance-treasury, risk-control). For every such card in your area, DRAFT the OKR in the fix map, in exactly the pattern of the filled cards of the same catalog: one objective (one sentence stating the outcome and who receives it), and three key results — Adoption (how consistently the scenario runs or is used), Acceptance (how often its output is accepted or acted on by the named reviewer), Cycle (the before → after of time or cadence). Ground each draft only in that card's own intent, problem and solution: name the same roles, outputs and cadences. Use target figures in the same illustrative style as the filled cards (e.g. "≥90% of …", "within 48 hours of …"); they are illustrative targets, as in the rest of the catalog. Read several filled cards first (areas such as strategic-portfolio or banking-data-analytics are fully filled) to match voice and length.

## Outputs (write both; nothing else)

1. `wiki/research/discovery-review/notes/<your-id>.md` — notes for a human: a 6–10 line summary of the state of your area; then per page: what is on it (counts), and the findings in plain words, most serious first; then "Questions for the owner".
2. `wiki/research/discovery-review/fixmap/<your-id>.jsonl` — one JSON object per line, each a single fix that can be applied mechanically: `{"id": "<your-id>-NNN", "file": "html-alt/financial-services/en/<path>/index.html", "urn": "<card urn or empty>", "locator": "<for non-card content: the nearest heading or a unique quoted phrase>", "field": "title|intent|problem|solution|okr|lens|complexity|section_title|section_intent|page_intent|problem_row|count|structure|other", "type": "missing|broken|logic|clarity|consistency|duplicate|fit", "severity": "high|medium|low", "current": "<exact current text, or the first 200 characters of it; empty if missing>", "proposed": "<the full replacement text; for field okr an object {\"objective\": \"…\", \"adoption\": \"…\", \"acceptance\": \"…\", \"cycle\": \"…\"}; for lens/complexity the new value>", "note": "<one line: why>"}` Write valid JSON (escape quotes; one object per line). Every finding that has a concrete fix goes here with its proposed text written out in full — the fix round will apply it without rethinking. A finding that needs an owner decision goes to the notes "Questions" instead.

Severity: high = missing or wrong content a reader would notice (empty OKR, wrong field, contradiction, broken sentence); medium = logic or clarity that weakens the card; low = polish. Do not propose rewrites for style alone when the text is correct and clear. Keep the catalog's voice in proposed text (third person, present tense, concrete roles and artifacts) and keep proposed text about the same length as what it replaces.
