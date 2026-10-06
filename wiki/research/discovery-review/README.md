# Validation of the new portal sections: discovery, 6 October 2026

Working record of the English content review of the four sections added next to the charter: Discovery Catalog, Portfolio, Delivery Pipeline, CloudLab. Read-only so far; the fixes are prepared as a fix map and applied in one later round.

## 1. Orientation: what is the source of what

| On the portal | Route | Generated from | Editable source |
| --- | --- | --- | --- |
| Discovery Catalog | `html/aicc/{en,ru}/discovery/` (76 pages per language) | `portal/tools/neighbours.py` reading `html-alt/financial-services/{en,ru}` | `html-alt/financial-services/{en,ru}/**/index.html` |
| Portfolio | `html/aicc/{en,ru}/initiatives/` (3 pages) | `portal/sections/initiatives/{en,ru}/*.md` | the same Markdown |
| Delivery Pipeline | `html/aicc/{en,ru}/projects/` (2 pages) | `portal/sections/projects/{en,ru}/*.md` | the same Markdown; origin `html-alt/intelligent-customer-service-resolution/` |
| CloudLab | `html/aicc/{en,ru}/lab/` (1 page) | `portal/sections/lab/{en,ru}/index.md` | the same Markdown; origin `html-alt/cloudlab/` |

- `html-alt/` is the original. `html/financial-services`, `html/csr`, `html/cloudlab`, `html/sts` are style-converted copies built by `finance-portal/`, `csr-portal/`, `sts-portal/`. The integrated portal does not read them: Discovery is built straight from `html-alt/financial-services`.
- Content parity, measured: the 1,101 scenario cards are identical, by identifier and by text, in `html-alt/financial-services/en`, in `html/financial-services/en`, and in `html/aicc/en/discovery`. Nothing was lost or altered in the conversion or the integration.
- The other agent's work since the integration (commits `824030b` to `d7e38d3`) changes only `portal/tools/neighbours.py`, the section style sheets and the regenerated `html/aicc`. It has not touched `html-alt` or `portal/sections/*.md`. The content fix round therefore edits files the style work does not edit; the only shared output is the regenerated `html/aicc`, which is why the two rounds must not run at the same time.
- STS (`html-alt/sts`, 8 pages) is not integrated into the portal.

## 2. Discovery Catalog in numbers

- 76 English pages: one overview, nine areas (each an area page plus its sub-area pages), one value-streams page.
- 1,101 scenario cards. Every card has a lens (Insights 399, Automation 353, Enablement 187, Optimize 90, New opps 72), a complexity (M 608, S 441, L 46, XL 6), a title, an intent, a problem and a solution: none of these is missing anywhere.
- OKRs: 782 cards carry a complete OKR, always one objective and three key results (Adoption, Acceptance, Cycle). **319 cards (29%) have an empty OKR**, all in four areas:

| Area | Pages | Cards | Empty OKR |
| --- | --- | --- | --- |
| Customer Channels | 8 | 97 | 61 (62%) |
| Customer & Market Intelligence | 9 | 128 | 86 (67%) |
| Finance & Treasury | 10 | 126 | 74 (58%) |
| Risk & Control | 12 | 164 | 98 (59%) |
| Strategic Banking Portfolio | 8 | 135 | 0 |
| Strategic Initiatives & Transformation | 8 | 130 | 0 |
| Shared Banking Capabilities | 10 | 132 | 0 |
| Banking Data & Analytics | 9 | 134 | 0 |
| Operational Value Streams | 1 | 55 | 0 |

## 3. Patterns across the whole catalog (one decision each, not per card)

| Pattern | Measure | Question |
| --- | --- | --- |
| Spelling | British forms about 500 (-isation) against American about 190 (-ization), mixed within pages | One variant for the portal; the charter uses American |
| Regulators | "CBR" (Bank of Russia) 449 times, "NBKR" 544 times, usually together ("NBKR and CBR") | O!Bank is supervised by the NBKR; keep, drop, or generalize the Bank of Russia references |
| Actor | "Agent reads / drafts / analyses…" about 1,500 times | The charter's term is "AI agent" |
| The bank | "the bank" 679 times, "the Bank" once; "O!Bank" never | The charter writes "the Bank" |
| Placeholder | `service.eyebrow` in the breadcrumb of every source page (76) | Remove at source; the integrated shell already replaces it |
| Other regulators and standards cited | IFRS 160, AML 216, Basel 58, DORA 41, EBA 36, FATF 33, SR 11-7 31 | Which are references and which are stated as binding |
| Counts on the overview map | e.g. "Strategic Banking Portfolio (116)" where the area holds 135 cards | Reviewed in `notes/overview-value-streams.md` |

## 4. The review

Method and rules: [BRIEF.md](BRIEF.md). Plain-text extracts of every page: `extract/`. Each reviewer writes `notes/<id>.md` (findings in plain words, questions for the owner) and `fixmap/<id>.jsonl` (one mechanical fix per line, with the replacement text written out, including a drafted OKR for every empty one).

| Reviewer | Scope |
| --- | --- |
| strategic-portfolio | Strategic Banking Portfolio |
| strategic-initiatives | Strategic Initiatives & Transformation |
| overview-value-streams | The overview map, its counts, the value streams page, the landing introduction |
| customer-market-intelligence | Customer & Market Intelligence |
| customer-channels | Customer Channels |
| risk-control-1, risk-control-2 | Risk & Control |
| shared-banking-capabilities | Shared Banking Capabilities |
| finance-treasury | Finance & Treasury |
| banking-data-analytics | Banking Data & Analytics |
| sections | Portfolio, Delivery Pipeline, CloudLab, and their originals (CloudLab, CSR, STS) |


## 5. Results

All eleven reviewers read their scope in full, including the page header intents, the problem rows and the stage texts of the cycles, which the plain-text extracts omit and which they read from the source pages. Every one of the 1,101 cards was read.

| Reviewer | Pages | Cards | OKRs drafted | Other fixes | Fix-map entries |
| --- | --- | --- | --- | --- | --- |
| strategic-portfolio | 8 | 135 | 0 | 140 | 140 |
| strategic-initiatives | 8 | 130 | 0 | 89 | 89 |
| overview-value-streams | 2 | 55 | 0 | 97 | 97 |
| customer-market-intelligence | 9 | 128 | 86 | 83 | 169 |
| customer-channels | 8 | 97 | 61 | 67 | 128 |
| risk-control-1 | 7 | 84 | 58 | 72 | 130 |
| risk-control-2 | 5 | 80 | 40 | 82 | 122 |
| shared-banking-capabilities | 10 | 132 | 0 | 86 | 86 |
| finance-treasury | 10 | 126 | 74 | 85 | 159 |
| banking-data-analytics | 9 | 134 | 0 | 124 | 124 |
| sections (Portfolio, Delivery Pipeline, CloudLab) | 6 | — | — | 42 | 42 |
| **Total** | **82** | **1,101** | **319** | **967** | **1,286** |

- Severity: 434 high (of which 319 are the missing OKRs), 426 medium, 426 low.
- Kind: 373 missing, 222 clarity, 213 logic, 167 consistency, 163 broken, 137 fit, 11 duplicate.
- Applicability, dry run: all 319 empty OKRs are confirmed empty at the card each draft names; of the 927 fixes that quote current text, 913 match the source exactly after whitespace normalization; the remaining 14 are structural (reordering sections, moving a card) and are applied by hand. All 1,286 lines are valid JSON.
- The Russian edition has the same 319 empty OKRs; it follows once the English is settled.

## 6. What the review found, in order of weight

1. **A third of the OKRs are missing** (319), all drafted in the fix map in the catalog's own pattern.
2. **The catalog is written for a regional bank group, not for a Kyrgyz bank.** NBKR 544 mentions, Bank of Russia 449, National Bank of Kazakhstan 278, the Kazakh regulator ARDFM 187; KASE, MOEX, tenge and ruble curves; US and UK texts in places (FinCEN, BSA officer, state money-transmitter licences, CFPB, FCA, Consumer Duty); EU reporting (COREP, FINREP, EBA, DORA) stated as binding. The som does not appear once.
3. **Statements of fact about the Bank that nobody supplied**: repeated supervisory findings against the Bank's risk assessments, capital narrative, limits and model inventory; managers, obligations and licence plans in Kazakhstan and Russia; the tenge as the Bank's currency; "three jurisdictions".
4. **Regulatory citations that could not be verified** and look relabelled from Kazakh or Basel sources: "NBKR Form 700", "NBKR Regulation No. 9 / 12 / 16", "NBKR Resolution No. 40", "AML/CFT Regulation No. 2"; the financial intelligence unit named "NBKR FIU"; BCBS 239 principles misnumbered; a Bank of Russia ordinance cited for the wrong subject.
5. **Scale assumptions**: internal-ratings credit models, a multi-desk trading book, advanced operational-risk capital, AT1 issuance, a sell-side research desk, private banking and wealth books, an open-banking API platform, M&A, analyst earnings calls.
6. **The overview map hides 160 scenarios**: the eight "cycles" pages have no box and are not counted (941 shown of 1,101).
7. **Duplication**: about fifty groups of near-duplicate cards, within pages, between a sub-area page and its area page, and between sub-area pages and the cycles pages; some disagree on complexity and figures.
8. **Broken content**: truncated text, text pasted from the neighbouring card, authoring notes left in intents ("L complexity is retained because…"), a stray label ("Target dd"), contradictions inside a card (thresholds, cadences, counts), "≥100%" as a target (55 times).
9. **Structure**: group and tab labels printed from identifiers ("Aml investigations sar", "Rm productivity"); a single problems tab covering only the first of two groups on most pages (39 of 66); problem rows missing on whole areas; sections alternating between groups; a few cards under the wrong section.
10. **OKR quality where filled**: about sixty OKRs contradict their own card on baseline, cadence or recipient, or measure another card; corrected in the fix map.
11. **Reading aids are missing**: lens, complexity and OKR are defined nowhere; the landing introduction is two sentences.
12. **Portfolio, Delivery Pipeline, CloudLab are not defined**: Portfolio says "0 initiatives" while the Registry holds ten; the pipeline has no stages and one unapproved entry; CloudLab does not say whether it is the charter's Lab; the CSR page keeps about 2.5% of its original; names collide with the charter (two "Portfolio"s, "Delivery Pipeline" and "Delivery", "CloudLab" and "Lab", the status "Proposal").

## 7. Decisions needed before the fix round

Each decision settles a family of fixes. The recommendation is what the fix round will apply unless decided otherwise.

| # | Decision | Recommendation |
| --- | --- | --- |
| D1 | Jurisdiction: one-country catalog for O!Bank, or a regional reference | One country. Replace Bank of Russia, National Bank of Kazakhstan and ARDFM references with the NBKR or with neutral wording ("the regulator", "applicable NBKR requirements"); remove KZT, RUB, KASE, MOEX, "three jurisdictions"; neutralize US, UK and EU texts stated as binding. |
| D2 | Unverified NBKR citations and the name of the financial intelligence unit | Replace numbered citations with generic wording until Compliance supplies the instruments; list them for Compliance. |
| D3 | Statements of fact about the Bank (supervisory history, foreign operations) | Remove or reword as general patterns. No decision needed beyond confirmation. |
| D4 | Scenarios that assume a business or regime the Bank may not have | Keep them as a general banking map, fix what is factually wrong, and say in the introduction that applicability to the Bank is assessed per scenario. Alternative: drop the fifteen to thirty regime-dependent cards. |
| D5 | Wording across the catalog | American spelling; "AI agent" for the actor (human contact-center agents excepted, handled per sentence); "the Bank"; remove the breadcrumb placeholder; "≥100%" → "100%". |
| D6 | Overview map and the cycles pages | Add the eight cycles boxes and correct the eight area totals (1,101 in all). |
| D7 | Duplicate cards | Merge only true duplicates within one page; differentiate the wording of the rest; keep all identifiers. A list of the fifty groups stays for a later editorial pass. |
| D8 | Structure | Fix the identifier-derived labels; add the drafted problem rows; do not move cards between sections in this round (moving changes identifiers), except the two flagged as plainly misplaced. |
| D9 | Lens and complexity | Define both once on the landing page; apply the 26 lens and 23 complexity corrections proposed. |
| D10 | OKR policy | Fix contradictions and wrong-card OKRs (in the map); leave key results that state a business outcome where the card supports it. |
| D11 | Roles and committees | Keep the generic banking roles; do not map to O!Bank's actual bodies in this round. |
| D12 | Portfolio, Delivery Pipeline, CloudLab | Needs the owner: is the Portfolio the reader's view of the Portfolio Backlog; is CloudLab the charter's Lab; where does CSR sit; the three section names; whether neighbours may cite the charter. The 42 text fixes can be applied now; the redefinition is a separate piece of work. |
| D13 | Discovery landing introduction | Use the four-paragraph introduction drafted in `notes/overview-value-streams.md`; the string lives in `portal/tools/neighbours.py`, which the other agent is editing, so it is handed over or applied in the fix round. |

The full questions, about 120, are at the end of each file in `notes/`.

## 8. The fix round

Applied in one pass while the style work is paused, because both regenerate `html/aicc`.

1. **Per-card fixes from the fix maps** (1,286): an applier reads `fixmap/*.jsonl` and edits `html-alt/financial-services/en/**/index.html` by card identifier and field: inserts each OKR in the existing markup (objective, then Adoption, Acceptance, Cycle), replaces quoted text matched on normalized whitespace, edits the stage texts inside each page's script block, sets lens and complexity. The 14 structural entries and the 42 section entries (`portal/sections/**/en/*.md`, three status values in `pages.json`) are applied by hand.
2. **Catalog-wide sweeps**, after the per-card fixes and according to D1–D5: jurisdiction, spelling, "AI agent", "the Bank", placeholder, "≥100%". Each sweep is reviewed against a diff, not applied blind; the contact-center page is excluded from the "AI agent" sweep.
3. **Overview map** (D6): corrected totals and eight boxes.
4. **Verification**: 1,101 cards and identifiers unchanged; no empty OKR; every OKR has one objective and three key results; no placeholder; counts on the map equal the cards; the pages parse; `python3 portal/tools/build.py`, `check.py --idempotent`, `check_neighbours.py`, the unit tests; a read of ten random cards per area.
5. **Then**: the Russian edition of the catalog (same 319 OKRs, same fixes, in natural Russian using the terminology and the translation map), and the redefinition of Portfolio and CloudLab.

Files touched by the fix round: `html-alt/financial-services/en/**` (76 files), `portal/sections/{initiatives,projects,lab}/en/*.md` (6 files), `portal/sections/pages.json`, and the regenerated `html/aicc`. Not touched: `portal/tools/neighbours.py` and the style sheets, except the introduction string if handed over.

## 9. Original versus restyled versus integrated: was anything left behind

Checked on 6 October 2026 by comparing every text block of the originals in `html-alt/` (visible text and the strings held in page scripts, where the stage texts live) with the restyled copies in `html/` and with the integrated portal pages.

| Original | Restyled copy | Result |
| --- | --- | --- |
| `html-alt/financial-services/en` (76 pages, 9,928 text blocks) | `html/financial-services/en` | Nothing lost: every block is present. |
| `html-alt/financial-services/ru` (76 pages, 10,294 text blocks) | `html/financial-services/ru` | Nothing lost. The only difference: 31 breadcrumbs that the original leaves in English ("Strategic Banking Portfolio") are shown in Russian by the copy. |
| `html-alt/cloudlab` (1 page) | `html/cloudlab` | Nothing lost. |
| `html-alt/intelligent-customer-service-resolution` (EN and RU) | `html/csr` | Nothing lost (the only differences are script code). |
| `html-alt/sts` (8 pages) | `html/sts` | Nothing lost. |

The restyling therefore dropped no content. What was dropped happened at the **integration** into the portal:

| Section | What the integrated portal leaves out of the original |
| --- | --- |
| Discovery Catalog | All 1,101 cards, sections, problem rows, counts, tabs and stage texts are carried over intact. Dropped: the original overview title and introduction ("GenAI-enabled Banking and Financial Services Framework — A uniform view of the top-level banking and operational aspects of the institution: its primary value chains, shared capabilities, and control flows. The intent is to adopt GenAI as an enabler and accelerator across every aspect: increasing visibility and insight, automating operational flows, enabling new capabilities, and unlocking new offerings and opportunities."), replaced by a two-sentence introduction; and the framework name and version line at the foot of every page ("… Framework · v11i"). The original introduction is the only place that says what the four lenses mean. |
| Delivery Pipeline (CSR) | The page is a hand-written summary of about 400 words; the original proposal is about 2.5% represented. Left out: the problem statement, the customer outcome, every figure, the decision requested, roles and responsibilities, the architecture and all technical content. The full proposal is not reachable from the portal. |
| CloudLab | A hand-written summary of about 240 words. Left out: the grid of stages by concerns with its 41 activities, the scorecard of 20 guardrails, the read-only data rule. |
| STS | Not integrated. |

Details of the CSR and CloudLab losses are in `notes/sections.md`.
