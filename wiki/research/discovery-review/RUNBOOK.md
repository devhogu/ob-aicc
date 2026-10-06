# Fix round for the Discovery Catalog (English): runbook

Prepared 6 October 2026. The round starts when the style work on the portal is paused, because both regenerate `html/aicc`. Scope of this round: the Discovery Catalog, English only. The Russian edition, and the redefinition of Portfolio, Delivery Pipeline and CloudLab, follow as separate rounds.

## Decisions in force

| # | Decision | In force |
| --- | --- | --- |
| D1 | Jurisdiction | **Neutral core, one wrap.** Each card states its concern in terms that hold for any bank ("the regulator", "the financial intelligence unit", "local currency"); the Bank's equivalents are given once on the landing page. No Kyrgyz specifics are written into cards. |
| D2 | Numbered national citations | Removed in favor of the subject of the rule. A list of the citations removed is kept for Compliance. |
| D3 | Facts asserted about a particular bank | Reworded as general patterns or deleted. |
| D4 | Scenarios assuming a business or regime the Bank may not have | Kept, with the condition stated ("Where the Bank uses internal models…"). |
| D5 | Wording | American spelling; "the AI agent" as the actor, human agents keep their names; "the Bank"; "100%" for "≥100%"; placeholders and authoring notes removed. |
| D6 | Overview map | Eight cycles boxes added; area totals corrected; 1,101 in all. |
| D7 | Duplicates | No card is merged or removed in this round; near-duplicates are differentiated in wording where the fix map says. All identifiers stay. |
| D8 | Structure | Identifier-derived labels corrected; drafted problem rows added; no card is moved between sections, except the two flagged as plainly misplaced. |
| D9 | Lens and complexity | The 26 lens and 23 complexity corrections are applied; both are defined on the landing page. |
| D10 | OKRs | The 319 drafts are inserted; the 249 corrected OKRs replace the ones that contradicted their card. |
| D11 | Roles and committees | Generic banking roles stay. |
| D13 | Landing introduction | The text below. International standards stay named as references. |

Open, not blocking this round: whether a per-area note "applies today / later / not in scope for O!Bank" is added to the wrap.

## Steps

All commands run from the repository root. `T=wiki/research/discovery-review/tools/dc.py`, `R=html-alt/financial-services/en`.

1. **Freeze.** Confirm the style work is paused and the tree is clean; `git pull --ff-only`. Tag the starting point: `git tag discovery-fix-start`.
2. **Structured fixes (script, seconds).** `python3 $T structured --root $R --fixmap wiki/research/discovery-review/fixmap` inserts the 319 OKRs, replaces the 249 corrected OKRs, sets 26 lenses and 23 complexities. Expected output: `applied {'okr': 568, 'complexity': 23, 'lens': 26}`, `failed 0`. Then `python3 $T verify --root $R --baseline <copy of the start>`: 1,101 cards, 1,101 identifiers in the same order, no empty OKR, every OKR one objective and three key results.
3. **Structural fixes (by hand and small scripts, listed in `fixmap/_structural.json`, 77 entries).** The overview map: eight area totals and eight cycles boxes. The 32 drafted problem rows: a second tab on eight pages, and the whole problems block on the six Strategic Banking Portfolio sub-area pages (copy the block's markup and its style rule from a page that has it). The cycle descriptions split into three paragraphs on the five finance cycles. The two misplaced cards. The remaining section-order entries are recorded as not applied (D8).
4. **Export.** `python3 $T export --root $R --out <work>/json` writes one JSON per page: every text node of the body (without the footer), the page title, and the stage texts. About 15,000 text nodes.
5. **Rewording (agents, one per area, pages in parallel within the area).** Each agent gets, per page, the page JSON, the fix entries of that page (`fixmap` split by page), and [REWORD-RULES.md](REWORD-RULES.md). It writes the edited JSON and a report per page (fix ids applied or not, notes). Areas: strategic-portfolio, strategic-initiatives, value-streams with the overview, customer-market-intelligence, customer-channels, risk-control (two halves), shared-banking-capabilities, finance-treasury, banking-data-analytics.
6. **Import.** `python3 $T import --root $R --in <work>/out`. The tool refuses a page whose node set differs from the source; such a page is returned to its agent.
7. **Verification.** `python3 $T verify --root $R --baseline <copy of the start>`: counts and identifiers unchanged; the wording scan (regulators, countries, currencies, foreign officers, "≥100%", placeholder, British spelling, bare "Agent", "the bank") reads zero or every remaining hit is listed with its reason (human agents on the contact-center page; named international standards). All fix ids accounted for across the reports. A read of ten random cards per area, before and after. The list of removed citations is written to `notes/citations-removed.md` for Compliance.
8. **Landing page.** The introduction and the table below replace the two-sentence `INTRO` in `portal/tools/neighbours.py` (English; the Russian follows with the Russian round), and the original page intent in `html-alt/financial-services/en/index.html` is aligned with it.
9. **Build and checks.** `python3 portal/tools/build.py`; `python3 portal/tools/check.py --idempotent`; `python3 portal/tools/check_neighbours.py`; `python3 -m unittest discover -s portal/tests`; `python3 portal/tools/check_sources.py` (refresh the English pins if they cover the catalog source). The expected number of Discovery pages stays 76.
10. **Commit, push, publish** on the owner's word: one commit for the catalog source, one for the regenerated portal.

Files touched: `html-alt/financial-services/en/**` (76 files), the `INTRO` string in `portal/tools/neighbours.py`, the regenerated `html/aicc`. `html/financial-services` (the stand-alone styled copy) is regenerated with `python3 finance-portal/build.py` if it is still kept.

## Landing page text (English)

**Discovery Catalog**

The Discovery Catalog is a map of a bank and, for each part of the map, a list of scenarios in which AI could help. It gives a uniform view of the Bank's primary value chains, shared capabilities, steering and control, and for each it shows where AI can increase visibility and insight, automate operational flows, enable people at the point of work, and open new offerings. It holds 1,101 scenarios in nine areas. Use it to find and compare opportunities; nothing in it has been selected or approved.

**How to read the map.** A box is a part of the bank; the number after it is the number of scenarios inside. The same subject can appear in more than one box because the map looks at the bank three ways: what it does (value streams and capabilities), what it measures and steers (strategy, finance, intelligence), and how it is controlled (risk and audit).

**How to read a scenario.** The lens says what kind of help it is: *Insights* gives people a view or an analysis they lack today; *Automation* has an AI agent carry out a repeatable task while people review the result; *Enablement* supports a person at the moment of work with guidance or a prepared draft; *Optimize* retunes routing, sequencing or allocation from observed results; *New opps* opens a service or capability the Bank does not yet have. Complexity (S, M, L, XL) is a first, relative estimate of the effort to implement. The card then states the problem and the solution. The OKR says how success would be judged: one objective and three key results — Adoption (how consistently the scenario is used), Acceptance (how often the named reviewer accepts its output) and Cycle (the time or cadence before and after).

**How this reads for O!Bank.** The scenarios describe concerns that every bank has, in terms that hold for any bank. For O!Bank they read as follows.

| In the catalog | For O!Bank |
| --- | --- |
| the regulator, the supervisor | the National Bank of the Kyrgyz Republic |
| the financial intelligence unit | the financial intelligence service of the Kyrgyz Republic (name to be confirmed by Compliance) |
| applicable law on personal data, consumer protection, AML | the law of the Kyrgyz Republic and the regulations of the National Bank on the subject (see Reference, Regulators and acts) |
| local currency | the Kyrgyz som |
| the national card scheme, the domestic payment systems | the national systems operated or overseen by the National Bank (names to be confirmed) |
| international standards named in a scenario (Basel, IFRS 9, BCBS 239, FATF) | references; what binds the Bank is confirmed by the Control Function Contacts |
| "where the Bank uses…" (internal models, a trading book, wealth mandates, an open-banking platform) | applies only if the Bank has that business or method |

**Status of this content.** The scenarios come from a general banking framework. Target figures are illustrative. A scenario commits nobody: it becomes an Initiative only after assessment and selection in the Portfolio.

## After this round

- Russian edition of the catalog: the same structured fixes (the 319 OKRs are empty there too), then the rewording in natural Russian with the terminology and the translation map.
- Editorial pass on the fifty groups of near-duplicate cards.
- Portfolio, Delivery Pipeline, CloudLab: definition with the owner (see `notes/sections.md`), then the 42 prepared text fixes.

## Run record, 6 October 2026 (English)

The round ran from tag `discovery-fix-start` and followed the steps above, with these particulars.

- **Structured fixes:** 568 OKRs inserted or replaced, 26 lenses, 23 complexities; none failed.
- **Structural fixes** (`tools/structural.py`): eight area totals, eight cycles boxes, eight problem tabs (32 rows), five cycle descriptions split, two cards exchanged between sections on the innovation-portfolio page. The ten section-order entries were not applied (D8).
- **Rewording:** the exported text was cut into 100 parts and given to 29 workers (`tools/batch.py view`, brief in [REWORD-BRIEF.md](REWORD-BRIEF.md), self-check `tools/scan.py`). Each worker wrote a patch of changed lines and a report. 6,002 of 15,096 texts changed; 575 text fixes applied. The paths under `/tmp/dc-run` named in the brief and the scanner are the working directory of the run.
- **After the import** (`tools/sync.py`): link labels and tab names follow the titles they repeat. Two terms were unified across the catalog: "STR" (suspicious transaction report, the FATF term) for "SAR", and "accumulated OCI" for "AOCI".
- **Not applied:** the breadcrumb token `service.eyebrow` stays in the source because both builders replace it; the two peer-framework boxes keep "(deferred)" in the source because the portal turns it into its "In progress" mark; fix 025 of the overview is replaced by the landing text.
- **Verification:** 76 pages, 1,101 cards, 1,101 identifiers, every OKR one objective and three key results; no named regulator, country, currency, foreign officer, British spelling, bare "Agent" or lower-case "the bank" left. Remaining by design: human agents on the contact-center page, the CIS control framework on the cyber page, and foreign regimes kept once as "such as" examples (36 mentions). Link labels equal their target titles on every page; stage buttons equal the stage data.
- **Landing page:** the introduction is `INTRO` in `portal/tools/neighbours.py`; the reading aid is `portal/sections/discovery/en/guide.md`, shown as a collapsed block under the introduction. A Discovery page may not link into the AICC section, so the reference to Regulators and acts is plain text.
- **For people to read:** [notes/citations-removed.md](notes/citations-removed.md) (512 references, for Compliance) and [notes/reword-notes.md](notes/reword-notes.md) (292 points the workers raised).

## Regulatory Horizon, 6 October 2026

The rewording removed the foreign regimes from the cards. Because some of them signal rules that will reach the Bank, the catalog gained a cross-cutting section that names them on purpose and links each to the scenarios that prepare the Bank for it.

- **Grounding:** the themes and their standing for the Bank are the section "Regulatory horizon" of the Standards record of the Registry (HZ-001 to HZ-012, both editions), to be confirmed by the Control Function Contacts (RI-006).
- **Links:** `portal/sections/discovery/horizon.json` holds, per theme, what such rules ask of a bank, how the scenarios prepare for it, and the linked scenarios (147 links to 145 scenarios). Candidates were drawn from the original text ([horizon/candidates.md](horizon/candidates.md)) and curated ([horizon/curation-notes.md](horizon/curation-notes.md)).
- **New scenarios:** two themes had almost none, so nine scenarios were added ([horizon/new-scenarios.json](horizon/new-scenarios.json), `tools/add_scenarios.py`): a section "AI governance" (5) on the model-risk page and "Payments modernization" (4) on the transaction-processing page. The English catalog holds 1,110 scenarios; the Russian edition receives them in its own round and meanwhile links only the scenarios it holds.
- **Portal:** a page "Regulatory Horizon" in both editions, a box on the overview grouped by standing, and on each linked card a mark that leads to its themes.

