# Strategic Initiatives & Transformation — review notes

Reviewer id: `strategic-initiatives`. Source: `html-alt/financial-services/en/strategic-initiatives/` (8 pages). Fix map: `fixmap/strategic-initiatives.jsonl` (89 entries: 7 high, 39 medium, 43 low).

## Summary

- Read 8 pages and all 130 cards: the area page (8 cards), six sub-area pages (105 cards in 35 sections of 3), and Change Cycles (17 cards in 5 cycles). The extract does not carry the page header intents or the 25 stage dialogs of Change Cycles; I read those from the source HTML.
- The area is complete in the mechanical sense: every card has intent, problem, solution and a full OKR; every section has an intent and exactly 3 cards; every count printed on the area page matches the cards present.
- Content is broken in seven places a reader will notice: a problem cut off mid-word, a bullet list pasted into one paragraph, a group label reading "Target dd", the NBKR attributed to Kazakhstan, and three intents that still contain an authoring note ("L complexity is retained because …").
- OKRs: all 130 are filled and each objective, Adoption KR and Acceptance KR measures its own card, with two exceptions (an objective borrowed from a Change Cycles card; an objective that is a bare metric). The weak spot is the Cycle KR: in about 50 cards it is an outcome rate rather than a before → after of time or cadence. I rewrote the 17 where the measure is unmeasurable, not attributable to the card, or a repeat of Adoption, and left 30 for an owner decision (listed under each page).
- The area was written for a Kazakhstan or regional bank. On Change Cycles the regulators are ARDFM (18 mentions) and NBK (17); the NBKR appears twice. This is a second jurisdiction pattern next to the CBR one already known: catalog-wide ARDFM 202 and NBK 310 mentions, 38 and 23 of them here.
- Three area-level cards are US/UK texts (CFPB, OCC, FRB, FCA, PRA, MRA/MRIA, Section 39, Skilled Person, Consumer Duty). These regulators appear almost nowhere else in the catalog, so I proposed neutral wording here instead of leaving them to the global decision.
- Overlap is heavy. One pair of cards is a plain duplicate (Innovation portfolio cards 7 and 8), four pairs within pages are near-duplicates, and 9 of the 17 Change Cycles cards restate a sub-area card, sometimes with a different cadence.
- Overview count: the overview says 113; the area holds 130 cards. The difference is the 17 Change Cycles cards, which the overview neither counts nor lists (details below).

## Overview count versus cards present

| Where | Shown | Cards present | Match |
|---|---|---|---|
| Overview: Strategic Initiatives & Transformation | 113 | 130 in the area | no |
| Overview and area page: M&A | 18 | 18 | yes |
| Overview and area page: Strategic partnerships | 15 | 15 | yes |
| Overview and area page: Ecosystem & platform strategy | 18 | 18 | yes |
| Overview and area page: Major transformation programs | 18 | 18 | yes |
| Overview and area page: Innovation portfolio | 18 | 18 | yes |
| Overview and area page: ESG commitments | 18 | 18 | yes |
| Area page only: Change Cycles | 17 | 17 (4 + 3 + 3 + 3 + 4) | yes |
| Area page: 35 section counts "(3)" | 3 each | 3 each | yes |
| Area page: own scenario cards | not counted anywhere | 8 | — |

113 = 105 cards on the six sub-area pages + 8 cards on the area page itself. The 17 Change Cycles cards are left out, and Change Cycles is not listed under the area on the overview at all. So a reader who adds the tiles on the area page gets 122, a reader who counts every card gets 130, and the overview says 113. The same rule holds for every other area (checked against `extract/_stats.json`: overview figure = sub-area cards + area-level cards, cycles page excluded), so this is a rule of the generator, not an error in this area. No fix-map entry: the choice between counting the cycles (130) and labelling the figure is the owner's (question 1).

## Area page — `strategic-initiatives/index.html`

On it: page intent, two tabs of problem rows (External growth, Internal transformation; four lenses each), seven tiles with section counts, 8 scenario cards (4 Insights, 3 Automation, 1 Enablement; 6 M, 2 L).

1. Card 4 "Regulatory Change Impact Assessment": the problem ends mid-word ("implementation plans are drafted fr..."); the solution is a six-item list pasted into one paragraph, so it reads as a run-on. Both rewritten (high).
2. Group label "Target dd" on the M&A tile is a broken slug (high). Six more labels lost their "&" ("Integration realization", "Industrialization scale", "Commitments disclosure" …) (low).
3. Cards 4, 5 and 7 are written for US and UK supervision: CFPB rule, OCC guidance, "small-business cards"; MRAs, MRIAs, Section 39 letters, Skilled Person reports; OCC, FRB, EBA, FCA, PRA, CFPB; Consumer Duty, IRB. The scenarios themselves hold for any supervised bank, so I proposed neutral wording (medium, fit).
4. Card 8 "M&A target screening & due-diligence synthesis": the body covers only diligence synthesis; title corrected (medium).
5. Card 6 "Earnings Call Q&A Prep": the solution is slide shorthand ("CEO + CFO use ~90 min vs 4 hours"), and the objective is a bare metric with a slip ("10 of 12 anticipated questions"). Both rewritten (medium). Whether the Bank holds quarterly analyst calls is question 6.
6. Card 3 "Stage-gate decision pack assembly" carries the Insights lens though it assembles a pack, and shares its title with Change Cycles card 12. Lens changed, both titles prefixed.
7. Cards 4–7 (regulatory change, supervisory response, earnings call, remediation tracking) sit on a page about M&A, partnerships, programmes, innovation and ESG; the page intent does not cover them (question 5).
8. Naming: this page writes "Steerco" (14 times) and "programme"; the sub-area pages write "steering committee" and "program". Two of the eight titles are in title case, six in sentence case (fixed, low).
9. The problem rows name four lenses; the cards use a fifth, Optimize (12 cards in the area), which has no problem row. Probably catalog-wide.
10. Scale claims left as they are: "30–50 initiative business cases per annual cycle", "20–100 workstream status reports per cycle".

## M&A — `ma/index.html`

On it: page intent, 6 sections × 3 cards = 18 (6 Insights, 5 Enablement, 4 Automation, 2 Optimize, 1 New opps; 3 S, 12 M, 3 L).

1. Section order on the page is Target screening, Integration planning, Due diligence, Synergy capture, Valuation, Post-merger reporting — integration planning before due diligence. The two groups are interleaved; this happens on every sub-area page of the catalog (medium, one entry per page).
2. "Target screening" section intent: "local M&A frameworks (NBK/ARDFM antitrust thresholds, CBR notification requirements)" — no NBKR, and antitrust thresholds are attributed to the Kazakh financial regulators.
3. Card 6 "Integration Workforce Readiness Brief": the Cycle KR measured key-person departures; rewritten (medium).
4. Small OKR repairs: card 4 ("≥100%", "post-close integration events" for a plan drafted before close), card 11 ("≥8 weeks earlier per quarter"), card 13 ("staleness complaints eliminated").
5. Card 15 "Valuation Scenario Sandbox" cites COREP, an EU reporting framework (catalog-wide: 39 mentions; left to the global decision).
6. Cycle KRs that are outcome rates, left for question 2: cards 5, 10, 14.
7. Lens doubts (question 3): card 8 Data Room Ingestion Brief and card 17 Board Integration Status Pack are Enablement but automate assembly; card 11 Synergy Realization Tracker is Optimize but reports; card 14 Deal Structure Regulatory Impact Assessment is New opps but is an assessment.
8. "CSO", "IC" and "DD" are never spelled out on the page.

## Major transformation programs — `major-transformation-programs/index.html`

On it: page intent, 6 sections × 3 cards = 18 (6 Insights, 6 Automation, 4 Enablement, 1 Optimize, 1 New opps; 5 S, 13 M).

1. Page intent: programmes "consume hundreds of millions in capital" — wrong scale for the Bank; reworded (medium).
2. Card 15 "Steering Governance Pack Drafting": the OKR objective lists "RAG status, financial burn, milestone achievement" — the content of Change Cycles card 9, not of this card; rewritten (medium). The card itself is nearly the same scenario as area card 3 and Change Cycles card 9, and overlaps card 13 (pre-read synthesis).
3. Card 3 "Resource Demand Forecast": the Cycle KR measured the cost premium of an emergency hire, which a forecast does not change; card 12 "Business Case Refresh": the Cycle KR counted programmes that "would have" been restructured; card 18: the Cycle KR was a go-live adoption rate. All three rewritten (medium).
4. Cards 16 "Change Readiness Assessment" and 18 "Change Readiness Continuous Signal Brief" read the same inputs and flag the same gaps; they differ only in timing (before go-live; fortnightly). Card 16 carries New opps on the strength of one closing sentence.
5. Section order interleaved (entry). Section "Steering governance" cites "NBKR operational resilience guidelines" (question 4).
6. Small OKR repairs: card 1 ("≥100%", garbled second clause), card 5 ("active program portfolios"), card 16 ("≥100%").
7. Cycle KRs that are outcome rates, left for question 2: cards 2, 4, 6, 8, 9.

## Strategic partnerships — `strategic-partnerships/index.html`

On it: page intent, 5 sections × 3 cards = 15 (5 Insights, 4 Automation, 3 Enablement, 2 Optimize, 1 New opps; 6 S, 9 M).

1. Card 13 "Regulatory Compliance Review Automation" carries the New opps lens against its own title; lens changed to Automation and complexity raised from S to M.
2. Section "Regulatory & compliance review" cites "NBKR Resolution No. 40" and "NBKR personal data regulations" as binding sources. A numbered resolution is either right or invented; it has to be checked before it stays (question 4).
3. Cards 6 and 12: the Cycle KR repeats adoption; rewritten (medium). Card 9: garbled Cycle KR and an Adoption KR that starts later than the brief is used (low).
4. Cards 1 and 2 overlap: the landscape brief (card 2) already pre-screens regulatory eligibility, which is the whole of card 1.
5. Page intent writes "NBKR/ARDFM open-banking and fintech licensing frameworks" — a hybrid of two countries' regulators. Three roles own partnerships on one page: "partnership governance lead", "business development lead" and "BD team".
6. Section order interleaved (entry): KPI tracking comes before deal structuring.
7. Cycle KRs that are outcome rates, left for question 2: cards 1, 3, 8, 11.

## Ecosystem & platform strategy — `ecosystem-platform-strategy/index.html`

On it: page intent, 6 sections × 3 cards = 18 (6 Insights, 5 Automation, 4 Enablement, 3 Optimize; 2 S, 13 M, 3 L).

1. Section "Ecosystem mapping" says "open-banking frameworks in Kazakhstan (NBKR), Kyrgyzstan, and Russia (CBR)" — the NBKR is placed in Kazakhstan (high). Card 2 speaks of "the KZ market" as the home market (medium).
2. Card 8 "Platform Role Options Analysis": the intent ends with an authoring note, "L complexity is retained because …" (high).
3. Cards 1 "Ecosystem Landscape Brief" (weekly) and 2 "Ecosystem Topology Shift Brief" (monthly) watch the same signals for the same reader (CSO) and answer the same problem.
4. Six Cycle KRs rewritten (cards 3, 7, 11, 13, 15, and 8 for wording): they counted decisions, extra committee reviews or revenue, or described "adopting a framework".
5. The whole page assumes a bank that runs a developer platform with take-rates, API product lines and BigTech competitors, under "NBKR and CBR open-banking API standards" (22 mentions each). Nothing on the page says where the Bank actually stands in its ecosystem (question 7).
6. Section order interleaved (entry). No Change Cycles cycle exists for this sub-area (five cycles for six sub-areas).
7. Lens doubts (question 3): cards 2, 7 and 14 are Automation but are monitoring or benchmark briefs.
8. Cycle KRs that are outcome rates, left for question 2: cards 5, 6, 9, 12, 14, 16, 18.

## Innovation portfolio — `innovation-portfolio/index.html`

On it: page intent, 6 sections × 3 cards = 18 (6 Insights, 6 Automation, 4 Optimize, 2 Enablement; 9 S, 9 M).

1. Cards 7 "Hypothesis Design Review" (Enablement) and 8 "Hypothesis Design Quality Review" (Insights) are the same scenario: the agent checks each experiment hypothesis against a quality rubric before the experiment runs. The section then has no card on MVP design itself (question 8).
2. Two cards are in each other's section: card 9 "MVP Test Results Interpretation Brief" matches the "Experiment analytics" section intent word for word but sits under "MVP design & hypothesis testing"; card 13 "Experiment Sample Design Optimisation Brief" is test design but sits under "Experiment analytics". Swap proposed (medium; urns carry the old section slugs).
3. Card 15 "Experiment Results Portfolio Synthesis": the Cycle KR rewards a higher hypothesis confirmation rate — a perverse target; card 12: "alignment improves by ≥20%" has no base. Both rewritten.
4. Card 1 "Stage-Gate Review Synthesis" and Change Cycles card 12 are one scenario with the same numbers (1–2 weeks → 2 business days); card 14 "Experiment Analytics Knowledge Accumulation" and Change Cycles card 13 likewise.
5. "CIO" is used for Chief Innovation Officer (card 11); readers will take it for Chief Information Officer. The gate body is called "innovation board", "investment committee" and "gate committee" on one page.
6. Card 14 Adoption KR assumes "≥100 experiments" in 12 months — scale. Page intent speaks of "banks operating in KG/KZ/RU markets".
7. Section order interleaved (entry): Scaling decision comes before MVP design.
8. Cycle KRs that are outcome rates, left for question 2: cards 3, 4, 5, 10, 13, 14, 18.

## ESG commitments — `esg-commitments/index.html`

On it: page intent, 6 sections × 3 cards = 18 (6 Insights, 6 Automation, 3 Enablement, 2 Optimize, 1 New opps; 3 S, 11 M, 4 L).

1. Cards 5 "Transition Plan Scenario Analysis" and 9 "Financed Emissions Attribution": each intent contains an authoring note, "L complexity is retained — …" (high).
2. Card 17 "Regulatory ESG Filing Automation" carries New opps against its own title; changed to Automation.
3. Card 6 "Transition Plan Portfolio Pathway Brief": the solution applies "IEA and PCAF pathway benchmarks" (PCAF is an accounting standard, not a pathway); the intent promises "real-time visibility" from a quarterly brief; rated L next to comparable M cards. Three entries.
4. Card 16 "Filing Calendar Brief": the Acceptance KR names no reviewer and Adoption counts "jurisdictions"; card 3: the Cycle KR ignores the card's own 4–6 weeks → 1 week. Cards 4, 6 and 15 Cycle KRs rewritten.
5. Cards 11 "ESG Target Trajectory Monitoring" (quarterly) and 14 "Sustainability Target Gap Brief" (monthly) are the same scenario in two sections. "Real-time" is used for monthly and quarterly briefs throughout the page.
6. The page states regulatory facts that need checking: "NBKR has issued green taxonomy guidelines", "NBKR and CBR have signaled alignment to TCFD expectations for systemically important financial institutions", mandatory "green taxonomy alignment reports" to the NBKR and "climate risk assessment submissions" to the CBR (question 4). The section "Regulatory ESG filings" and its three cards depend on those filings existing.
7. "TCFD report" is treated as the current annual vehicle (43 mentions in the area); the TCFD was wound up in 2023 and its work passed to the ISSB. "CSO" on this page reads as Chief Sustainability Officer, on the other pages as Chief Strategy Officer; it is never spelled out (58 uses in the area).
8. Overlap with Risk & Control: `risk-control/climate-esg-risk` has its own "TCFD/ISSB disclosure" section and a "Financed Emissions Calculation" card next to card 9 here.
9. Section order interleaved (entry). Lens doubts (question 3): cards 1 and 13 are Enablement but draft documents; cards 2 and 15 are Automation but are benchmark briefs.
10. Cycle KRs that are outcome rates, left for question 2: cards 2, 7, 8, 14.

## Change Cycles — `change-cycles/index.html`

On it: page intent, 5 cycles (M&A deal cycle 4 cards, Partnership lifecycle 3, Program governance cycle 3, Innovation stage-gate cycle 3, ESG reporting cycle 4 = 17; 10 Insights, 7 Automation; 9 S, 7 M, 1 L). Each cycle has a short and a long intent, four problem rows, and five stage dialogs (25 in all, each with title, intent and problem; all filled).

1. The page is written for Kazakhstan. "Board and regulator approval (ARDFM in Kazakhstan, NBK for financial groups, CBR in Russia as applicable)"; "Domestically, ARDFM, NBK, and CBR each publish …"; filings "to ARDFM/NBK/CBR". The NBKR is missing from: the M&A long intent and its Approve stage; cards 2, 5, 15 and 16 with their OKRs; the ESG long intent, its Enrich row and its Disclose stage. Card 5's OKR also adds "ARDFM and NBK regulatory eligibility screening", which the card's solution does not contain.
2. Nine cards restate a sub-area card, some with a different cadence: card 1 = M&A card 3; card 3 (quarterly) = M&A cards 11 and 12 (weekly); card 4 = M&A card 9 and area card 8; card 5 (quarterly) = Partnerships card 2 (weekly); card 6 = Partnerships card 10; card 9 = Programs cards 13 and 15; card 12 = Innovation card 1; card 13 = Innovation card 14; card 17 = ESG cards 1 and 13 (question 8).
3. The problem rows use the lens names Analyze, Optimize, Automate, Enrich; the cards use Insights and Automation only. No card answers an Optimize or Enrich row. Probably the same on every cycles page.
4. Six cards write "≥100%" (cards 2, 3, 10, 11, 16, 17) — fixed to "100%". Catalog-wide there are 55; a single global replace would cover them.
5. Stage dialog "Scale": "the binary scaling decision (proceed, pause, or exit)" (low). Program governance long intent: programmes "consume capital at eight-figure levels" (low, fit).
6. ESG reporting long intent cites EU CSRD for "banks with European subsidiaries or European investor bases" and "CIS-market banks" (11 uses of "CIS" on the page) — generic, not about the Bank.
7. Several stages have no card attached, for example Close in the M&A cycle, Negotiate, Charter, Industrialize and Disclose. Not a defect by itself; noted for completeness.

## Questions for the owner

1. Overview count. The overview shows 113 for this area; the area has 130 cards because the 17 Change Cycles cards are not counted and Change Cycles is not listed on the overview. The rule is the same for all eight areas with a cycles page. Count the cycles in (130 here) and list them, or keep the figure and say what it covers?
2. Cycle key results. The brief defines Cycle as the before → after of time or cadence. Thirty cards here still use an outcome rate instead ("cost overruns reduced by ≥40%", "conversion rate improves by ≥20%"); they are listed per page above. Rewrite all of them to time or cadence, or accept outcome rates where the card gives no timing?
3. Lens. By the area page's own lens rows, about 15 cards carry a lens that does not match what they do (document drafting under Enablement, benchmark briefs under Automation, trackers under Optimize, and "New opps" assigned once per page on the strength of a closing sentence). I fixed only the three that contradict their own title or twin. Is one lens per section slot intended, or should the lens follow the card's function?
4. Regulatory facts stated as binding. Please confirm or strike: "NBKR Resolution No. 40" (partnership notification); "NBKR green taxonomy guidelines" and mandatory green taxonomy alignment reports to the NBKR; "NBKR operational resilience guidelines" for programme steering; NBKR alignment to TCFD for systemically important institutions; "NBKR open-banking API standards"; "NBKR personal data regulations"; "NBK/ARDFM antitrust thresholds". If the ESG filings do not exist, the section "Regulatory ESG filings" (3 cards) has no basis.
5. Kazakhstan regulators. ARDFM and NBK appear 202 and 310 times in the catalog (38 and 23 here) and are not on the list of global patterns. Should they be decided together with the CBR references? On Change Cycles the NBKR is absent from nine places where the regulator list is given.
6. Area-level cards 4–7 (regulatory change impact, supervisory response drafting, earnings call Q&A, regulatory remediation tracking). Do they belong in this area, or in Risk & Control and Finance? Does the Bank hold quarterly earnings calls with analysts, or should card 6 be recast for its actual investor reporting?
7. Fit of two sub-areas. Ecosystem & platform strategy assumes a bank choosing a platform role and running a developer marketplace; M&A assumes a serial acquirer with a watch list and several live integrations. Keep them as generic catalog content, or anchor them to the Bank's actual position?
8. Duplicates. Innovation cards 7 and 8 are one scenario: delete one, or replace it with a card on MVP design? Near-duplicates within pages: Ecosystem 1 and 2, ESG 11 and 14, Programs 16 and 18, Partnerships 1 and 2. And should Change Cycles cards that restate a sub-area card be kept, merged, or aligned on cadence (weekly on the sub-area page, quarterly on the cycle)?
9. Abbreviations. "CSO" is used 58 times and never spelled out, as Chief Strategy Officer on most pages and Chief Sustainability Officer on the ESG page; "CIO" stands for Chief Innovation Officer. Which roles exist at the Bank, and should the first use on each page be spelled out?
10. Section order. On all six sub-area pages (and across the catalog) sections alternate between the two groups, so M&A runs screening → integration planning → due diligence. I proposed the area-page order per page; should this be fixed once in the generator instead?
