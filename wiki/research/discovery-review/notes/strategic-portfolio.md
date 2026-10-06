# Strategic Banking Portfolio — review notes

Reviewer id: `strategic-portfolio`. Source: `html-alt/financial-services/en/strategic-portfolio/` (8 pages, 135 scenario cards). Fix map: `fixmap/strategic-portfolio.jsonl`, 140 entries (15 high, 44 medium, 81 low). Numbers in brackets below, such as [008], are fix-map ids without the `strategic-portfolio-` prefix.

## Summary

- All 8 pages and all 135 cards were read in full. Every card has a title, lens, complexity, intent, problem, solution and a complete OKR; there are no empty fields, no duplicate cards by urn or title, no truncated sentences, and no template tokens other than the known breadcrumb placeholder.
- The extract leaves out three kinds of content, which I read from the source HTML instead: the header intent of every page, the eight "problems by lens" rows on the area page, and the 25 stage dialogs on the Steering Cycles page (they sit in an embedded data block). Other reviewers working only from the extract will not have seen the equivalents in their areas.
- OKRs: 115 of 135 measure their own card without a content problem. One measures a different scenario [008], one carries elements from another card [004], fourteen contradict their own card on a baseline, cadence or recipient or are garbled, and four state only a business outcome where the catalog's pattern asks for acceptance of the output. All twenty have a rewritten OKR in the fix map.
- The overview shows 116 for this area; the pages hold 135. The difference is the 19 Steering Cycles cards, which the overview neither counts nor lists. The same rule holds in all eight areas (see "How the counts add up").
- The six sub-area pages have no "problems by lens" block, which sub-area pages in five other areas carry. I drafted the 24 missing rows from each page's own cards [014–017, 025–028, 059–062, 078–081, 105–108, 121–124]; whether to add them is an owner decision.
- The area was written for a banking group active in Kyrgyzstan, Kazakhstan and Russia. Beyond the known CBR/NBKR pattern, four cards state outright that the Bank has managers, obligations or licence plans in Kazakhstan and Russia, or cite Kazakh authorities for the domestic branch network [089–090, 098–100, 130–132, 134–137]; one domestic card lists three national regulators [125].
- There is heavy overlap between the sub-area pages, the area-level cards and the Steering Cycles page: at least seven groups of cards describe the same scenario twice or three times, in places with different complexity and different figures. I did not merge anything; the groups are listed under Questions.
- Two wording habits are concentrated here and are fixed mechanically: "≥100%" as a target (29 of the catalog's 55 occurrences) and "monthly continuous read" for a monthly refresh (20 of the catalog's 21 occurrences). They account for 38 of the 81 low-severity entries.
- English is generally sound. The weak spots are titles that repeat the lens name instead of naming the output ("… enablement", "… automation"), two titles that contradict their lens, and one obscure title ("rare-position arbitrage") [011].

## How the counts add up

| Where | Shown | Actually present |
|---|---|---|
| Overview page, "Strategic Banking Portfolio" | (116) | 135 cards in the area |
| Overview, six sub-areas listed | 15 + 18 + 18 + 15 + 18 + 18 = 102 | 102, each count matches its page |
| Area page, scenario table | not counted on the page | 14 area-level cards |
| Area page, "Steering Cycles" tile | (19) | 19 cards (5 + 4 + 3 + 3 + 4, each cycle count matches) |

The overview total is the 14 area-level cards plus the 102 cards of the six sub-areas: 116. It leaves out the 19 Steering Cycles cards, and the overview does not show a Steering Cycles link at all, although the area page gives it a tile. A reader who adds up the seven tiles on the area page gets 121; one who also counts the scenario table gets 135; neither matches 116.

This is not specific to this area. In all eight areas the overview total equals area-level cards plus sub-area cards and excludes the cycles page (for example Banking Data & Analytics shows 114 and holds 134; Risk & Control shows 139 and holds 164). Across the catalog 160 cycle cards are outside the overview totals, and no cycles page is linked from the overview. I left this out of the fix map because it is one decision for the whole catalog (Question 1).

Every other count in the area is right: the seven sub-area totals on the area page, and all 39 level-3 counts on the tiles, match the cards on the pages.

## Patterns across the area

These are the special cases for the global-pattern decisions, plus patterns that exist only here.

- Countries named as the Bank's own markets. "KG, KZ, and RU" appears in two cards on Target markets & segments (six mentions) and "KG or KZ" in one card on Geographic footprint. These are fixed in the fix map because they are statements about the Bank, not regulator lists.
- Kazakh authorities. "NBK/ARDFM" is added to the NBKR/CBR lists on six pages (about 14 mentions); AFSA (the Astana regulator) appears seven times on Geographic footprint. The Steering Cycles page names the Kazakh regulator two ways in two consecutive paragraphs ("NBKR / CBR / NBK", then "NBKR / ARDFM / CBR"). The regulator lists should follow the CBR decision; only the places where the text contradicts the card itself are in the fix map.
- European terms. "SREP" (the EU supervisory review process) is used about ten times on Steering Cycles, in one cycle intro, two cards and one stage dialog; "EBA" once [044]; "MiFID-equivalent" once [112].
- "Operating jurisdictions" / "active jurisdictions". Thirteen mentions across six pages assume the Bank works under several national regimes; four Adoption key results measure coverage of "active jurisdictions".
- A numbered foreign regulation. The Investment products section cites "NBK/ARDFM securities licensing, CBR Regulation No. 306" as applicable law [104].
- "Sub-concern". The area page and the Steering Cycles page use "sub-concern" 35 times for what the portal calls a sub-area; no other area uses the word. One card also says "L2" [010].
- Two generations of cards. Twenty-four cards on the six sub-area pages have Title Case titles, American spelling, objectives of 35–50 words that restate the intent, and most of the foreign-jurisdiction references. The other 78 have sentence-case titles and one-sentence objectives of about 24 words. All 19 Steering Cycles cards have the long objective. Nothing is wrong in the long objectives; they are simply a second voice on the same page.
- "≥100%". Twenty-nine Adoption key results set a target of "≥100%"; the fix map changes each to "100%".
- "Continuous" with a cadence. Twenty-four Cycle key results end in "monthly continuous read", "quarterly continuous read" or similar, and five objectives say "in continuous form" for a monthly or quarterly dashboard. The fix map states the cadence only.
- Titles that repeat the lens. Forty-one titles end in "enablement", "automation", "optimisation" or "insights" (or that word plus "tool", "dashboard", "pack"). I renamed only the seven that leave the reader unsure what the card produces or that contradict their lens; nine titles change in all.
- Section order. On all six sub-area pages the sections run in a different order from the tile on the area page (the page interleaves the tile's two groups). The same is true of all 58 sub-area pages in the catalog, so it is a generator rule; not in the fix map.
- Acceptance key results without a reviewer. Besides the four rewritten ones, five more Acceptance key results measure accuracy against actuals or a conversion rate without naming who accepts the output (Tier 2 adequacy monitor, buffer headroom monitor, domestic market share monitor, private banking opportunity detection, public sector tender detection). They are measurable and belong to their cards, so I left them.

## Area page — `strategic-portfolio/index.html`

What is on it: a header intent, seven tiles (six sub-areas and Steering Cycles) with counts, eight problem rows in two tabs, and 14 area-level cards (Insights 4, Automation 4, Enablement 3, New opps 3; S 1, M 3, L 5, XL 5). Thirteen fix-map entries [001–013].

- "Cross-sub-concern impact mapping": the OKR belongs to another scenario. The card is an impact map produced in one pass when rates, FX or capital rules shift, for executives. The OKR measures an annual exercise that maps dependencies for the risk committee, reduced "from 3–4 months of workshops to 4 weeks". Rewritten from the card [008].
- "Board strategic narrative drafting": the OKR speaks of "strategic plan lock" and "external counsel or Chairman" edits, neither of which is in the card, and does not measure the card's main claim, cross-section consistency. Rewritten [004].
- "Integrated what-if engine": the Cycle key result starts from "4-6 weeks of analyst effort" while the problem says "multi-day sequential analysis"; the Adoption key result calls the engine a "sandbox", which is the neighbouring CEO/CFO card [009].
- "Portfolio-coherent expansion guidance": the objective promises a fit assessment "within hours"; both key results say two business days [007].
- "Posture refinement (rare-position arbitrage)": the title does not tell a reader what the card is; the body is about defensible positioning [011, 012].
- Problem row "New business opportunities" (Capital & risk posture): "the bank pursues capital arbitrage opportunities" reads badly for a supervised bank; the cards under it are about reallocation and buffer optimisation [001].
- "Portfolio coherence detection": the objective is an imperative fragment ("Make portfolio misalignments visible…") and the Adoption target is "by Q4" [006].
- Smaller points: no recipient in one objective [003]; "L2" jargon [010]; two "≥100%" and one "continuous monthly scan" [002, 005, 013].
- Overlap on the page itself: "CEO/CFO portfolio-modeling sandbox", "Cross-sub-concern impact mapping", "Integrated what-if engine" and "Multi-dimensional posture stress testing" are four cards about one cross-portfolio simulation capability, three of them XL.
- The header intent and the other seven problem rows are clear and are covered by the cards.

## Capital allocation — `capital-allocation/index.html`

What is on it: header intent, six sections of three cards each, 18 cards (S 6, M 10, L 1, XL 1). No problems block. Nine entries [014–022], the lightest page.

- Missing problems block; four rows drafted [014–017].
- "TCR forecast and threshold alert": the Acceptance key result is not a sentence ("≥85% of quarterly forecast accuracy within ±15 bps…; zero unheralded floor breaches") [022].
- Four "≥100%" [018–021].
- Not fixed, for the owner: "ICAAP narrative drafting" (L, 6–8 weeks to 3 weeks) is the same scenario as "ICAAP narrative drafting from stress outputs" on Steering Cycles (M, "reduced by ≥50%"). "BU capital reallocation scenario engine" and "Dynamic Capital Reallocation Across Business Lines" overlap with each other and with two Steering Cycles cards. "RAROC Narrative per Business Line" is repeated on Risk appetite.
- Not fixed, for the owner: "Tier 2 regulatory limit tracking" attributes a cap of Tier 2 relative to Tier 1 to Basel III. Basel III dropped that cap; if it applies to the Bank it comes from the NBKR rule. Worth one check by the capital team before the wording is touched.
- Fit, not fixed: AT1 issuance windows, buybacks and a "SIFI surcharge" assume a bank that issues capital instruments in the market; "ICAAP stress scenario design support" calibrates scenarios "across CIS and regional markets" and "all operating jurisdictions".
- Section intents are complete and cover their cards. The page intent covers the sections.

## Risk appetite — `risk-appetite/index.html`

What is on it: header intent, six sections of three cards, 18 cards (S 5, M 10, L 3). No problems block. Nineteen entries [023–041].

- Missing problems block; four rows drafted [025–028].
- "Stress-Test Results Interpretation and Narrative": the lens is Optimize, but the card drafts a narrative from model outputs, which is Automation on the RAS and ICAAP narrative cards; and half of its Acceptance key result measures whether the human reviewers "add net new insight" [035, 036].
- "RAS performance continuous insights": the problem is that the executive committee has no read between board meetings, but the Acceptance key result makes the board risk committee the intra-quarter user; the objective alerts on amber only, the solution on amber or red [030].
- "Tolerance Recalibration Scenario Sandbox": intent, solution and OKR each list a different set of impact dimensions [034].
- Page intent promises "a weekly operating signal" and compression "from months to days"; of the monitoring cards only the limits dashboard (daily) and the tolerance narrative (weekly) are faster than monthly [023].
- The Risk-adjusted performance metrics section intent names RAROC and RORAC; its three cards report RAROC and EVA [024].
- Titles: "RAS stress impact scenario enablement" and "Risk-adjusted metrics enablement tool" renamed for clarity [031, 040]. "Bi-annual" is ambiguous [037]. Five "≥100%" and four "continuous read" [029, 032, 033, 038, 039, 041].
- Not fixed, for the owner: "Risk-adjusted performance reporting automation" says the quarterly RAROC pack takes two to three weeks; "RAROC Narrative per Business Line" on Capital allocation says the same pack takes several days. "Risk tolerance recalibration optimisation" and "Tolerance Recalibration Scenario Sandbox" are close but distinguishable (back-test versus what-if).

## Steering Cycles — `strategic-portfolio/steering-cycles/index.html`

What is on it: header intent, two groups, five cycles. Each cycle has a short intent, one to three body paragraphs, four problem rows (Analyze, Optimize, Automate, Enrich), five stages with a dialog each (title, intent, problem), and its cards: Strategic planning 5, Capital management (ICAAP) 4, Portfolio rebalancing 3, Performance review 3, Board & investor communication 4. Nineteen cards (S 12, M 7). Seventeen entries [042–058].

- Portfolio rebalancing, second body paragraph: "Most banks operate with 60-90 day lag between signal and re-deployment; the opportunity is to reduce that to one quarter." Sixty to ninety days is one quarter, so the sentence promises nothing. The drift-detection card on the same cycle targets 20 business days; the sentence is rewritten to agree with it [043].
- Capital management cycle, stage "Plan": guidance "from NBKR or EBA" [044].
- Header intent: the first sentence begins as a fragment, and "cadence and quality determines" [042]. Unlike the other seven headers in the area it has no sentence on the GenAI opportunity; this is the same on every cycles page in the catalog, so I did not add one.
- "Cross-BU variance attribution": actuals are compared with the "prior-period plan"; it should be the plan for the same period [054, 055].
- Clumsy key results in "RAROC-driven rebalancing scenario pack" and "Investor question and analyst theme intelligence" [053, 057]; "GC" unexplained in one stage dialog [045]; eleven "≥100%".
- Problem rows and stages without a card (not fixed, for the owner): the Optimize rows of Strategic planning (alternative-plan exploration) and Capital management (alternative capital actions) have no card on this page; in Portfolio rebalancing the Diagnose and Decide stages have none although the Automate row promises root-cause attribution; in Performance review the Assemble and Adjust stages have none although the Automate row promises corrective-action mandates.
- Lens: three cards that draft packs for others are Enablement ("Strategic plan cascade variant production", "Rebalancing implementation brief", "Distribution and filing execution checklist"), while the page's own Automate rows name exactly these tasks. Not fixed; see Question 5.
- Scale, not fixed: "hundreds of pages of ICAAP narrative", "200–500 pages of model output", "25–100 person-hours per cycle", earnings calls and analyst reports describe a much larger listed bank.
- The 25 stage dialogs are otherwise complete and well written, and each cycle's stages and problem rows describe the same process as its cards.

## Strategic priorities — `strategic-priorities/index.html`

What is on it: header intent, five sections of three cards, 15 cards (S 3, M 9, L 3). No problems block. Eighteen entries [059–076].

- Missing problems block; four rows drafted [059–062].
- "Innovation regulatory horizon scan": the objective and Cycle key result promise an assessment within four weeks of publication, but the only cadence in the solution and Adoption key result is a quarterly scan; the solution also calls the output a "risk map" where the intent says "constraint map" [071, 072].
- "ESG priority data insights dashboard": "visible on a quarterly basis in continuous form" [076]. Three more monthly dashboards are "in continuous form" [065, 068, 070]; one of them compares itself with a "board pack" although its problem names the executive committee pack [065].
- Titles: "Growth Scenario and Whitespace Scan" has no scenario element; "Innovation experiment return automation" is unclear [064, 073]. "Local CB" abbreviation [074, 075]. "Regulatory complaint data" [069]. Three "≥100%" [063, 066, 067].
- Not fixed, for the owner: "Operational Excellence Initiative Portfolio Scan" is Enablement but is a cross-initiative report (Insights), and overlaps with "Operational excellence initiative benefits tracking" on benefit-realisation gaps. "Growth Scenario and Whitespace Scan" overlaps with the area-level "Whitespace detection" card.
- Roles assumed: chief customer officer, chief innovation officer, chief sustainability officer, a board sustainability committee and board "Customer and Strategy committees".

## Target markets & segments — `target-markets-segments/index.html`

What is on it: header intent, six sections of three cards (Retail, Private banking, SME, Wealth management, Corporate, Public sector), 18 cards (S 2, M 15, L 1). No problems block. Twenty-six entries [077–102], the most of any page.

- "SME Segment Opportunity Detection" says segment managers "in KG, KZ, and RU markets" [089, 090].
- "Public-Sector Banking Obligation Monitoring" describes obligations of "banks serving public-sector clients in KG, KZ, and RU" in every field, and uses "TSA" unexplained [098–100].
- Missing problems block; four rows drafted [078–081].
- Page intent promises "on-demand segment-prioritization what-ifs"; none of the 18 cards offers one [077].
- "Private banking segment opportunity detection": the intent lists inheritance events as a signal; the solution uses only public registers [088]. See also Question 9 on personal data.
- "SME Credit-Appetite Cohort Calibration" carries the Enablement lens; calibration cards elsewhere in the area are Optimize [092].
- Three Acceptance key results state only a business result (conversion rate, decline rate) [083, 084, 097]; a duplicated word, "cross-product product penetration" [087]; two titles that do not name the output [086, 095]; one Cycle key result with a baseline the problem does not give [091]; one that compares unlike things [102]; six pattern entries.
- Not fixed, for the owner: Private banking (HNW and UHNW clients, trust and estate services) and Wealth management are two full segments here. "Retail segment churn risk enablement" and "Retail segment product cross-sell optimisation" are operational scenarios that also belong to Customer & Market Intelligence (Retention & churn). "Private banking client needs enablement" and "Wealth management advisory model enablement" are the same pre-meeting briefing for two segments, which is acceptable as parallel cards.

## Product portfolio — `product-portfolio/index.html`

What is on it: header intent, six sections of three cards (Lending, Investment, Deposit, Insurance, Cards, Treasury services), 18 cards (S 7, M 9, L 2). No problems block. Eighteen entries [103–120].

- Missing problems block; four rows drafted [105–108].
- Investment products section intent cites "NBK/ARDFM securities licensing, CBR Regulation No. 306" [104].
- "Investment product regulatory window opportunities": four-week promise against a quarterly cadence, the same flaw as the innovation horizon scan [111].
- "Cards portfolio economics insights": the Cycle key result starts from "ad hoc quarterly assembly"; the problem says the P&L is assembled monthly [118].
- Two titles say "Optimisation" on cards whose lens and content are something else: "Lending Product-Mix Optimisation" is an Enablement what-if sandbox, "Corporate Treasury Product-Mix Optimisation" is a New opps cross-sell list [110, 120].
- "MiFID-equivalent conduct frameworks" [112]; one outcome-only Acceptance key result [113]; "SKU level" in the page intent against "product variant" in the cards [103]; six pattern entries.
- Not fixed, for the owner: "Insurance product regulatory compliance monitor" is Enablement while the two regulatory trackers on Geographic footprint are Automation; "Cross-Product Cannibalization Detection" is Optimize but detects and reports. The Treasury services section defines the product set as FX, money markets, fixed income and derivatives, while its cards count cash management and trade finance as treasury services. The page intent speaks of "CIS and regional market conditions"; one card models "murabaha structures for CIS geographies" (Islamic products are relevant to the Bank; the CIS framing is not).

## Geographic footprint — `geographic-footprint/index.html`

What is on it: header intent, five sections of three cards (Domestic markets, Branch network density, Cross-border / international, Digital presence, Strategic expansion targets), 15 cards (S 4, M 8, L 3). No problems block. Twenty entries [121–140], eight of them high.

- "Branch Rationalization Scenario Modeling" duplicates "Branch density rationalisation scenario" in the same section: same inputs, same cluster-level output, same "four to six weeks" baseline, different lens (Enablement, Optimize) and complexity (L, M). It also annotates the domestic network for "ARDFM and AFSA compliance", both Kazakh authorities. The jurisdiction text is fixed [130–132]; which card stays is Question 3.
- "Digital-Bank License Window Monitoring" monitors "NBKR and AFSA" for a digital-bank licence "in KG or KZ". The wording is fixed [134–137], but the scenario itself is doubtful for a bank that already holds a licence (Question 2).
- "Domestic regulatory change tracker": a domestic card whose problem lists NBKR, NBK/ARDFM and CBR; and an objective of 48 hours against a weekly briefing [125–127].
- Missing problems block; four rows drafted [121–124].
- "Digital Channel-Shift Scenario Simulation": the Cycle key result starts from "4–6 weeks of manual modeling" while the problem says the question is answered qualitatively today [139]. It is also a third card on branch rationalisation thresholds, placed under Digital presence.
- "Domestic competitive positioning scan" sends competitive analysis to ALCO [128, 129]; "Expansion target business case assembly" has two baselines [140]; two pattern entries [133, 138].
- Not fixed, for the owner: "Cross-border regulatory obligation tracker" presumes subsidiaries abroad ("country heads", "group chief compliance officer", "each country compliance team"). The page intent mentions "partnership-based presence" and "exit what-ifs"; no section or card covers either.

## Questions for the owner

1. Overview totals. Should the overview count and list the cycles pages? Today it shows 116 for this area against 135 cards, and the same rule hides 160 cycle cards across the eight areas. My recommendation: add the cycles tile to each overview card and raise the totals (135 here).
2. One jurisdiction or several? If the Bank is to be described as operating only in the Kyrgyz Republic, then, beyond the CBR decision: (a) replace "operating jurisdictions" and "active jurisdictions" (13 mentions, including four Adoption key results); (b) drop "NBK/ARDFM" from the regulator lists; (c) replace "SREP" with "supervisory review" (about ten mentions on Steering Cycles); (d) decide whether "Cross-border regulatory obligation tracker" and "Digital-Bank License Window Monitoring" stay at all; (e) reword the four references to CIS markets.
3. Duplicated scenarios. Which card stays, or should the pairs be kept and cross-referenced? (a) "Branch density rationalisation scenario" / "Branch Rationalization Scenario Modeling" / "Digital Channel-Shift Scenario Simulation"; (b) "ICAAP narrative drafting" (L) / "ICAAP narrative drafting from stress outputs" (M); (c) "Strategic plan production (1y / 3y / 5y)" (L) / "Multi-horizon plan drafting" (M); (d) "RAROC Narrative per Business Line" / "Risk-adjusted performance reporting automation" / "RAROC continuous BU performance insights", with baselines of "several days" and "two to three weeks" for the same pack; (e) "BU capital reallocation scenario engine" / "RAROC-driven rebalancing scenario pack", and "Dynamic Capital Reallocation Across Business Lines" / "Capital deployment drift detection"; (f) "Board strategic narrative drafting" / "Equity story / investor-day pack assembly" / "Board and investor communication first-draft production"; (g) the four cross-portfolio simulation cards on the area page. If the overlap between sub-area cards and cycle cards is intended (one capability seen from the function and from the process), the figures and complexity should at least agree.
4. Problems block on sub-area pages. Add the 24 drafted rows, or leave the six pages without the block, as on the pages of Strategic Initiatives and Customer & Market Intelligence?
5. Lens vocabulary. Cards use Insights, Automation, Enablement, Optimize, New opps; area-page problem rows use Insights & analytics, Enablement, Automation, New business opportunities (no Optimize); cycle problem rows use Analyze, Optimize, Automate, Enrich. Is there a definition of each lens? I changed two lenses where the area contradicts itself [035, 092]. Seven more need the definition: "Multi-dimensional posture stress testing" (Enablement), "Operational Excellence Initiative Portfolio Scan" (Enablement), "Insurance product regulatory compliance monitor" (Enablement), "Cross-Product Cannibalization Detection" (Optimize), and the three Enablement drafting cards on Steering Cycles.
6. Complexity scale. Is S/M/L/XL defined? Cases that look out of line: "Total capital ratio continuous dashboard" and "Limits framework utilisation insights" are S although they need daily cross-system feeds, while monthly dashboards beside them are M; "Retail Segment Economics Dashboard" (daily, S) against the quarterly SME and Corporate dashboards (M); "Stress-Test Results Interpretation and Narrative" (L) against "RAS Board Narrative Pack" (S); and the L/M splits inside the duplicates of Question 3.
7. Things the Bank may not have. Should the catalog keep them as a generic reference or be cut to the Bank? Private banking for UHNW clients as a segment separate from Wealth management; rating-agency relationships; AT1 issuance, buybacks and a SIFI surcharge; earnings calls and sell-side analyst coverage; and the roles chief customer officer, chief innovation officer, chief sustainability officer, Chief Strategy Officer, group chief compliance officer.
8. "Sub-concern". Replace with "sub-area" on the area page and Steering Cycles (35 mentions, including the titles "Cross-sub-concern impact mapping" and "Whitespace detection at sub-concern intersections")? It is used nowhere else in the catalog.
9. Personal data. "Private banking segment opportunity detection" builds prospect lists of individuals from business registers, property transactions and filings. Is this acceptable to present under Kyrgyz personal-data law, or should the card be limited to existing clients?
10. Two voices. Should the 24 Title Case cards and the 19 cycle cards be brought to the pattern of the rest (sentence-case title, one-sentence objective of about 25 words)? I did not rewrite them because they are correct and clear.
11. Tier 2 cap. Please have the capital team confirm whether a cap of Tier 2 relative to Tier 1 applies to the Bank and under which rule, so that "Tier 2 regulatory limit tracking" can cite it correctly.
