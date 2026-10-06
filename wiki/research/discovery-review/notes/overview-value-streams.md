# Notes: Discovery Catalog overview and Operational Value Streams

Reviewer id: `overview-value-streams`. Sources read: `html-alt/financial-services/en/index.html` (overview map), `html-alt/financial-services/en/value-streams/index.html` (11 streams, 56 stage dialogs, 55 cards), `INTRO` in `portal/tools/neighbours.py`, and the generated landing page `html/aicc/en/discovery/index.html`. Fix map: `fixmap/overview-value-streams.jsonl`, 97 entries (18 high, 36 medium, 43 low).

## Summary

- The overview map is complete and every one of its 78 links resolves (58 sub-area boxes, 9 area boxes, 11 value-stream anchors). All 58 sub-area counts and all 11 stream counts are right. All 8 area totals are wrong for a reader: the heading number matches neither the boxes shown under it nor the number of cards in the area.
- The cause is one omission: each area has a "cycles" page (Steering Cycles, Risk Cycles and so on, 160 cards in total) that has a box on the area page but no box on the overview. The map therefore shows 941 scenarios of 1,101, and 8 pages cannot be reached from it.
- The value-streams page is the best-kept page I read: no empty field, 55 OKRs all filled, 56 stage dialogs all with title, intent and problem, and stage order is sound in all 11 streams.
- Its weak points are precision, not completeness: two factual errors about regulators (Kazakhstan's central bank named "NBK/NBKR"; the Kyrgyz financial intelligence unit named "NBKR FIU"), key results that contradict the solution (real time against daily or monthly; "≥100%"), one wrong committee (ALCO for control-effectiveness), and one pair of cards that claim the same task.
- Cards are not tied to stages. A reader opens a stage dialog, reads its "Problem to solve", and cannot tell which card answers it. By my mapping 11 of the 56 stages state a problem that no card answers.
- Each stream has exactly one card per lens (5 lenses × 11 streams). The symmetry forces the label: about ten cards carry a lens that does not describe them, mostly "New opps" on internal reporting or analytics.
- Kazakhstan's regulators are cited throughout this page (NBK 19 times and ARDFM 5 times here; 310 and 202 occurrences catalog-wide). This pattern is not in the brief's list of global patterns and should be decided together with CBR.
- The landing introduction (two sentences) says what the catalog covers but not how big it is, how to read a card, or what status the content has. A replacement is proposed below.

## Page 1. Overview map (`en/index.html`)

### What is on it

Title "GenAI-enabled Banking and Financial Services Framework", one intent paragraph (replaced by `INTRO` in the integrated portal), nine area boxes, two "peer framework" boxes, footer "… · v11i".

| Area box (eyebrow) | Groups and boxes | Count shown | Boxes add up to | Cards on area page | Cycles page (not on map) | Real total |
| --- | --- | --- | --- | --- | --- | --- |
| Strategic Banking Portfolio (Operating state) | Market & business posture: 4; Capital & risk posture: 2 | 116 | 102 | 14 | Steering Cycles 19 | 135 |
| Strategic Initiatives & Transformation (Change state) | External growth: 3; Internal transformation: 3 | 113 | 105 | 8 | Change Cycles 17 | 130 |
| Operational Value Streams (Primary value chain) | Customer-facing value streams: 6; Cross-cutting flows: 5 | 55 | 55 | 0 | none | 55 |
| Customer & Market Intelligence (Analytics) | Customer insights: 5; Market position: 2 | 111 | 105 | 6 | Intelligence Cycles 17 | 128 |
| Customer & Channels (Operations) | Assisted channels: 3; Self-service & partner: 3 | 80 | 75 | 5 | Channel Cycles 17 | 97 |
| Risk & Control (Control) | Non-financial risks: 6; Financial risks: 3; Independent assurance: 1 | 139 | 134 | 5 | Risk Cycles 25 | 164 |
| Shared Banking Capabilities (Operating engines) | Operational capabilities: 5; Customer-facing capabilities: 3 | 112 | 108 | 4 | Capability Cycles 20 | 132 |
| Finance & Treasury (Financial control) | Planning & balance-sheet steering: 5; Accounting, reporting & tax: 3 | 101 | 96 | 5 | Finance Cycles 25 | 126 |
| Banking Data & Analytics (Foundation) | Operational data: 4; Risk & regulatory data: 3 | 114 | 109 | 5 | Data Cycles 20 | 134 |
| Total | 58 sub-area boxes + 11 streams | 941 | 889 | 52 | 160 | 1,101 |

All 58 sub-area counts match the number of `scenario-card` elements on the linked page, and each box label matches the `h1` of the page it opens. All 11 stream counts (5 each) match. Every link and every `#anchor` exists.

### Findings, most serious first

1. Area totals do not add up (fix map 001–008, high). "Strategic Banking Portfolio (116)" stands over six boxes that sum to 102. The 116 is the six sub-areas plus the 14 cards that sit on the area page itself; it leaves out the 19 cards of Steering Cycles. The same rule gives every other area total. A reader can verify none of these numbers from the page. The fix map proposes the real totals (135, 130, 128, 97, 164, 132, 126, 134). Whatever rule is chosen, the page needs one line that states it (included in the proposed introduction).
2. Eight pages are missing from the map (009–016, high). The cycles pages exist, carry 160 cards, and appear on the area pages under group labels such as "Strategic governance" and "Risk governance". They have no box on the overview. The fix map adds one sub-group per area with the label and link text the area page already uses. Side note for the area reviewers: those group labels are inconsistent among themselves ("Strategic governance", "Change cycles", "Analytics cycles", "Channel governance", "Risk governance", "Capability governance", "Finance governance", "Data governance").
3. Treasury & Funding sits under "Customer-facing value streams" (017–018, medium). The streams page describes it as the bank's own balance-sheet funding. The fix map renames the group on both pages; the alternative is to move the stream to "Cross-cutting flows".
4. "(deferred)" on the two peer-framework boxes (019–020, medium). It is status wording of the source project. A portal reader does not know what was deferred. The Enterprise Services box also lists "accounting", which the map already has under Finance & Treasury.
5. "ALM" means two things on one page (021, low): asset-liability management in Finance & Treasury and application lifecycle management in the IT peer box. The same line has a raw `&` in the HTML.
6. Eyebrows that do not say what the layer is (022–024, low): "Operating state" and "Change state" for the two strategy boxes, "Operations" for channels. "Control" (Risk & Control) and "Financial control" (Finance & Treasury) are close enough to confuse, and "Financial Control & Performance Cycle" is also a value stream; I left these alone.
7. The same subject appears in several boxes with nothing on the map to tell them apart. Financial crime: "Compliance & financial crime" (Risk & Control, 18), "Financial crime" (Shared Banking Capabilities, 12) and "Compliance & Financial Crime Cycle" (value stream, 5). Internal audit: sub-area and stream. Liquidity: "Liquidity management", "Liquidity risk", "Treasury & Funding". Churn and lifetime value: two Customer & Market Intelligence boxes and the Customer Lifecycle stream. Capital: "Capital allocation" and "Capital management". This is a matrix by design (what the bank does, what it measures, who controls it), but the page never says so. The proposed introduction adds one sentence; relabelling the boxes is a question for the owner.
8. "Banking Data & Analytics" has seven data boxes and no analytics box; "Analytics" is also the eyebrow of Customer & Market Intelligence. Noted, no fix.
9. The source page intent names four uses of GenAI where the cards have five lenses (025, low). It only shows in the stand-alone build.
10. As a map of a bank the grouping is sound: strategy on top, value streams and functions in the middle, shared capabilities and finance below, data as the foundation. What a Kyrgyz retail and SME bank would look for and not find as a box: remittances and money-transfer systems, cards and merchant acquiring including QR payments, and trade finance. What it would find and may not have: wealth management with an investment committee, and wholesale paper issuance. See questions 4 and 5.

## Page 2. Operational Value Streams (`en/value-streams/index.html`)

### What is on it

Page intent; a page-level table of four problems (Waste, Variability, Overload, Quality at source); two groups, "Customer-facing value streams" (6) and "Cross-cutting flows" (5). Each stream has a summary line, a description paragraph, a four-row problems table (Analyze, Optimize, Automate, Enrich), a row of clickable stages (56 in total; each opens a dialog with label, title, intent and "Problem to solve"), and 5 cards, one per lens. Complexity: 12 S, 41 M, 2 L. No empty field anywhere; 165 key results present.

### Findings that apply to the whole page

1. Cards are not placed on stages. The page shows stages, then cards, with no link between them, although most card problems are copied word for word from a stage dialog or a lens row. The tables below give my mapping. Stages whose dialog states a problem that no card answers: Fund (Deposits), Servicing (Lending), Plan and Implement (Wealth), Underwrite (Bancassurance), Execute (Treasury), Acquire and Serve (Customer Lifecycle), Monitor (Risk), Execute and Measure (Financial Control). Partly answered: Funding (Lending), Settle (FX), Exit (Customer Lifecycle), Report (Internal Audit). Question 3.
2. Three lens vocabularies. Cards use Insights, Automation, Enablement, Optimize, New opps. The problems tables on this page and on the cycles pages (47 tables catalog-wide) use Analyze, Optimize, Automate, Enrich. Area and sub-area pages (48 tables) use Insights & analytics, Automation, Enablement, New business opportunities. On this page "Enrich" feeds the New opps card in seven streams, the Enablement card in three, and the Optimize card in one (Bancassurance, which is simply mislabelled: fix map 049–050). Outside my area, `customer-market-intelligence/index.html` shows raw slugs ("insights", "new-opps") as row labels. Question 2.
3. One card per lens forces the label. Cards whose lens does not describe them: "Rating agency and counterparty posture brief" (New opps; it is drafting, Automation), "Cross-segment lending learning transfer", "Cross-domain aggregate risk event view", "Continuous AML program health monitoring", "Cross-entity audit control learning propagation", "IFRS 9 provision intelligence and planning integration", "Customer lifetime value intelligence" (all New opps; all are internal Insights), "Customer churn signal aggregation and scoring" (Enablement; Insights), "Audit finding remediation tracking enablement" (Enablement; Automation), "Budget and reforecast consolidation optimisation" (Optimize; it tracks submissions, Insights). Only "Corporate client FX rate intelligence service" is a new customer offering. I did not put lens changes in the fix map because each one breaks the five-lens symmetry of its stream. Question 2.
4. Regulators of other countries, a pattern beyond the brief's list. The page cites NBK (National Bank of Kazakhstan) and ARDFM (Kazakhstan's financial market regulator) next to NBKR 24 times (NBK 19, ARDFM 5): in the descriptions of Deposits, Treasury, FX, Risk, Compliance, Internal Audit and Financial Control; the stage dialogs FX Capture, FX Reconcile, Risk Report, Compliance Report, Financial Control Report; and the cards "FX purpose-code classification enablement" and "Nostro reconciliation and currency-control notification automation" (intent, problem, solution and OKR). The FX and Compliance descriptions present the bank as operating "in CIS markets — Kazakhstan, Kyrgyzstan, and Russia". Catalog-wide: NBK 310 occurrences, ARDFM 202, Kazakhstan 47. Two of these are plain errors and are in the fix map as high: "Kazakhstan (NBK/NBKR)" (059) and "NBKR FIU" (080).
5. Scenarios that lean on another jurisdiction. "FX purpose-code classification enablement" and "Nostro reconciliation and currency-control notification automation" are built on currency-control notifications of the Kazakh and Russian kind; they survive in a reduced form (payment-purpose classification and cross-border reporting to NBKR) if the Bank has such a duty. "ALCO pack and regulatory liquidity return automation" assumes LCR and NSFR returns to NBKR. Question 5.
6. "Real time" in the intent against a slower promise in the key results: five cards (039, 073, 084, 097 and the "continuous" of 062). "≥100%" in three key results (055, 063, 091); catalog-wide the string occurs 55 times on 19 pages, so it is a global pattern. Question 8.
7. The same text is read up to three times: lens row, stage dialog, card problem. By design; no fix. Where the copy brought a clause the card does not address, the fix map trims it (041, 056, 068).
8. Overlap with area pages. Nearly every card here has a sibling elsewhere that describes the same scenario in other words, for example "Payment exception pattern analytics" (identical title in Shared Banking Capabilities › Transaction processing), "Rating agency and counterparty posture brief" (Strategic Banking Portfolio, "Rating-agency relationship briefings"), "Intraday liquidity position copilot" (Risk & Control › Liquidity risk, "Intraday Liquidity Position Watch"; Banking Data › Risk & position data, "Intraday Liquidity Monitor"), "Financial crime investigation pack and SAR draft automation" (Shared Banking Capabilities › Financial crime, "AML Alert Investigation Pack"), "Audit finding remediation tracking enablement" (Risk & Control › Internal audit, "Remediation Tracking & Status Reporting"), "Financial close narrative and management pack automation" (Finance & Treasury › Accounting & financial close, "Close Narrative Drafting"). No URN is duplicated. Question 7.
9. "Cycle anchor" (029, low) is an undefined term used once per stream. "ALCO" is named as a recipient of management accounts five times in the Financial Control stream (description, Report stage intent and problem, and the solution and objective of "Financial close narrative and management pack automation"); the body that receives them at the Bank should be named instead. Question 6. Role titles from other markets: MLRO, Chief Audit Executive, Chief Accounting Officer, business unit CFOs, MD&A.
10. Naming: the page calls its eleven items "value streams", "flows" and "cycles" in turn, and the area-level cycles pages use "cycle" for something else.

### Per stream

Stage order was checked in every stream and is logical in all eleven. "Stage" in the tables is my reading of where the card acts; the page does not state it.

**Deposits & Transaction Banking** — Account opening → Fund → Transact → Service → Retain.

| Card | Lens, size | Stage |
| --- | --- | --- |
| Dispute resolution automation | Automation, S | Service |
| KYC adaptive document sequencing | Enablement, S | Account opening |
| Payment exception pattern analytics | Insights, M | Transact |
| STP routing and queue optimisation | Optimize, M | Service |
| Transaction behaviour intelligence for product and pricing | New opps, M | Retain |

Findings: the "STP routing" card routes dispute and investigation cases, not payments; title, intent and objective corrected (031–033). End-to-end dispute resolution is rated S beside M neighbours (034). Fund has no card. The description cites "NBK account-status reporting".

**Lending** — Application → Underwriting → Decision → Documentation → Funding → Servicing.

| Card | Lens, size | Stage |
| --- | --- | --- |
| Credit document collection and notification automation | Automation, S | Application, Documentation, Funding |
| Lending origination queue intelligence | Insights, M | all origination stages |
| Underwriting capacity and routing optimisation | Optimize, M | Application, Underwriting, Decision |
| Credit decision copilot for underwriters | Enablement, M | Underwriting, Decision |
| Cross-segment lending learning transfer | New opps, M | feedback into policy; no stage |

Findings: the Acceptance key result of the document-collection card measures approval before delivery of notifications that the solution sends automatically (038). The learning-transfer problem speaks of servicing feedback that the solution does not provide (041). Two grammar slips in stage dialogs (035, 036). Servicing has no card; the "Enrich" row's second problem (multi-week setup for new lending products) has no card either.

**Wealth Management** — Discover → Plan → Construct → Implement → Monitor → Review.

| Card | Lens, size | Stage |
| --- | --- | --- |
| Client review pack and IC pre-read automation | Automation, S | Review, Construct |
| Advisory discovery and suitability capture enablement | Enablement, S | Discover |
| Wealth portfolio drift and mandate-breach monitoring | Insights, M | Monitor |
| RM time allocation and book-capacity optimisation | Optimize, M | Review |
| Wealth prospect and competitive intelligence enrichment | New opps, M | before Discover; no stage |

Findings: the prospect card reuses client histories and "comparable client profiles" for sales preparation without saying they are anonymised (048). Summary says "institutional clients", everything else says high-net-worth (042). Drift card names two different recipients and has a garbled Cycle line (046, 047). Plan and Implement have no card. The whole stream assumes custodians, managed mandates and an investment committee: question 4.

**Bancassurance (insurance distribution)** — Identify trigger → Position offer → Underwrite → Sell & onboard → Retain.

| Card | Lens, size | Stage |
| --- | --- | --- |
| Insurance positioning and disclosure enablement for frontline staff | Enablement, S | Position offer |
| Bancassurance policy onboarding automation | Automation, S | Sell & onboard |
| Bancassurance conversion and trigger analytics | Insights, M | all stages |
| Insurance offer sequencing and propensity optimisation | Optimize, M | Identify trigger |
| Policy lapse early-warning and retention | New opps, M | Retain |

Findings: the "Optimize" and "Enrich" problem rows are swapped (049, 050). The onboarding automation crosses into the insurer's platform and the payment system and is rated S (052). Underwrite has no card.

**Treasury & Funding** — Forecast → Plan funding → Execute → Monitor → Report & narrate.

| Card | Lens, size | Stage |
| --- | --- | --- |
| Rating agency and counterparty posture brief | New opps, S | Report & narrate |
| Treasury cash forecast accuracy attribution | Insights, M | Forecast |
| Funding mix scenario optimisation | Optimize, M | Plan funding |
| ALCO pack and regulatory liquidity return automation | Automation, M | Report & narrate |
| Intraday liquidity position copilot | Enablement, M | Monitor |

Findings: broken bracket naming the regulators in the description (054). The rating-agency OKR has "≥100%" and a Cycle line that cannot be read (055). The forecast card's problem is the whole Analyze row although the card treats forecast error only (056). The ALCO-pack agent "calculates LCR and NSFR ratios"; it should take them from the controlled calculation (057). Refresh interval is 15 minutes in one key result and 10 in the next (058). Execute has no card. The stream is not customer-facing (017, 018).

**FX & Cross-border** — Capture order → Price & quote → Execute → Settle → Reconcile.

| Card | Lens, size | Stage |
| --- | --- | --- |
| FX purpose-code classification enablement | Enablement, S | Capture order |
| FX corridor exception and settlement failure analytics | Insights, M | Settle |
| FX correspondent routing table optimisation | Optimize, M | Execute |
| Nostro reconciliation and currency-control notification automation | Automation, M | Reconcile |
| Corporate client FX rate intelligence service | New opps, M | Price & quote |

Findings: "Kazakhstan (NBK/NBKR)" (059, high). Routing card is "continuous" in the intent, monthly in the solution, and "a continuous monthly cadence" in the key result (062, 063). Analytics card refreshes daily but promises 4 hours (061). Two solutions omit a task their intent promises (064, 065). Settlement status tracking, the problem of the Settle dialog, is only analysed, not solved.

**Customer Lifecycle** — Acquire → Onboard → Serve → Grow → Retain → Exit.

| Card | Lens, size | Stage |
| --- | --- | --- |
| Customer lifecycle cross-stage journey analytics | Insights, M | all stages |
| Onboarding and cross-sell sequencing optimisation | Optimize, M | Onboard, Grow |
| Lifecycle stage agent execution | Automation, M | Onboard, Grow, Exit |
| Customer churn signal aggregation and scoring | Enablement, M | Retain |
| Customer lifetime value intelligence | New opps, M | Grow, Retain |

Findings: the summary lists five of the six stages (066, 067). "Lifecycle stage agent execution" is an unreadable title and the widest automation on the page at M (070, 071). The sequencing card's Cycle line is an outcome target, not a time (069). The churn card's Cycle line cannot be parsed (072). Lifetime value is "real time" in the intent and monthly in the solution (073). Acquire and Serve have no card; the Exit dialog's problem (exit reasons not classified) has none. "Competitor inquiry" as a churn signal is never explained.

**Risk Management Cycle** — Identify → Assess → Mitigate → Monitor → Report.

| Card | Lens, size | Stage |
| --- | --- | --- |
| Emerging risk signal synthesis | Insights, M | Identify |
| Risk control effectiveness and mitigation prioritisation | Optimize, M | Mitigate |
| Risk narrative and regulatory reporting automation | Automation, M | Report |
| Stress test and risk assessment decision enrichment | Enablement, M | Assess |
| Cross-domain aggregate risk event view | New opps, L | Assess |

Findings: the mitigation card sends its output to "each ALCO cycle" in the solution and all four OKR lines; the forum is the risk committee (075, 076). Its intent says the reranking replaces the annual risk appetite review (074). Monitor (delay between a limit breach and the owner hearing of it) has no card.

**Compliance & Financial Crime Cycle** — Detect → Investigate → Action → Report.

| Card | Lens, size | Stage |
| --- | --- | --- |
| Financial crime typology enrichment copilot | Enablement, S | Investigate |
| AML alert throughput and false-positive analytics | Insights, M | Detect |
| Financial crime case triage and assignment optimisation | Optimize, M | Investigate |
| Financial crime investigation pack and SAR draft automation | Automation, M | Investigate, Action |
| Continuous AML program health monitoring | New opps, M | Report |

Findings: the Report dialog names "NBKR FIU" as the Kyrgyz financial intelligence unit (080, high). Filing with the FIU is in both the Action and the Report stage, and the Action intent ends in a sentence that does not parse (079). The report is called SAR, STR, "SAR/STR" and "STR/SAR" (081). The health-monitoring card is "real time" against daily (084) and repeats most metrics of the throughput card one level up; it is the same view for a different reader. "Action" is the only stage label that is not a verb (078).

**Internal Audit Cycle** — Plan → Execute → Report → Remediate.

| Card | Lens, size | Stage |
| --- | --- | --- |
| Audit fieldwork documentation and evidence automation | Automation, S | Execute |
| Audit finding remediation tracking enablement | Enablement, S | Remediate |
| Audit finding pattern intelligence | Insights, M | Report |
| Risk-ranked dynamic audit planning | Optimize, M | Plan |
| Cross-entity audit control learning propagation | New opps, M | after Report; no stage |

Findings: the fieldwork card also chases remediation status, which is the entire next card (086–089). Two key results have the audit committee accepting or reviewing drafts within days; that is the Chief Audit Executive's part (090, 091). "Cross-entity" means business lines of one bank (092–094). The head of audit is "audit director" in one dialog and "Chief Audit Executive" in the cards (085).

**Financial Control & Performance Cycle** — Plan → Execute → Measure → Report → Adjust.

| Card | Lens, size | Stage |
| --- | --- | --- |
| Financial variance attribution analytics | Insights, M | Report |
| Budget and reforecast consolidation optimisation | Optimize, M | Plan |
| Financial close narrative and management pack automation | Automation, M | Report |
| Reforecast cross-unit forward signal enrichment | Enablement, M | Adjust |
| IFRS 9 provision intelligence and planning integration | New opps, L | Adjust |

Findings: "Measure" is the financial close and should say so (095). ALCO as recipient of management accounts, five places (question 6). IFRS 9 card is "real time" against 48 hours (097). One 60-word intent sentence (096). Execute and Measure, the stages where the dialogs put most of the close-period pain, have no card. The stream assumes intercompany eliminations and business unit CFOs.

## Introduction on the Discovery landing page

Current text (`INTRO['en']`): "Banking services, journeys and operating capabilities where AI may add value. Explore the map and assess each opportunity in its intended context."

Judgement against the three things a first-time reader needs:

- What the catalog is: partly. It names "services, journeys and operating capabilities" but the map also covers strategy, risk, finance and data, which is more than half of the cards. It gives no size and does not say that the unit is a scenario card.
- How to read a card: not at all. Lens, complexity and OKR are not mentioned here or anywhere else in the catalog; there is no legend. The five lens names and the S–XL scale are shown as bare badges.
- What status the content has: not at all. "Assess each opportunity in its intended context" hints at it but does not say that the content comes from a general banking framework, is not validated for the Bank, carries illustrative targets, and commits nobody. The neighbouring Portfolio section already says "An indicative benefit or complexity estimate is a starting assumption"; Discovery should say the same about itself.

On the page as generated: the section name and the page title are the same words one above the other ("Discovery Catalog", "Discovery Catalog"), and the value-stream box is rendered twice (List and Stages) by the comparison code that is marked temporary. Neither is content.

Proposed introduction (English; numbers should be generated at build time, not typed):

> The Discovery Catalog is a map of a bank and, for each part of the map, a list of scenarios in which AI could help. It holds 1,101 scenarios in nine areas, from strategy at the top through value streams, customer, risk, finance and shared capabilities to data at the foundation. Use it to find and compare opportunities; nothing in it has been selected or approved.
>
> **How to read the map.** A box is a part of the bank; the number after it is the number of scenarios inside. The same subject can appear in more than one box because the map looks at the bank three ways: what it does (value streams and capabilities), what it measures and steers (strategy, finance, intelligence), and how it is controlled (risk and audit).
>
> **How to read a scenario card.** The lens says what kind of help it is: Insights gives people a view or analysis they lack today; Automation has an AI agent carry out a repeatable task while people review the result; Enablement supports a person at the moment of work with guidance or a prepared draft; Optimize retunes routing, sequencing or allocation from observed results; New opps opens a service or capability the bank does not have. Complexity (S, M, L, XL) is a first, relative estimate of the effort to implement. The card then states the problem and the solution. The OKR says how success would be judged: one objective and three key results — Adoption (how consistently the scenario is used), Acceptance (how often the named reviewer accepts its output) and Cycle (the time or cadence before and after).
>
> **Status of this content.** The scenarios come from a general banking framework and have not yet been validated for O!Bank. Some refer to regulators, products and roles of other markets, some cards are incomplete, and all target figures are illustrative. A scenario becomes an initiative only after assessment under the selection approach in Portfolio.

If the slot must stay one paragraph: "A map of a bank with 1,101 scenarios in which AI could help, grouped in nine areas. Each card gives the kind of help (lens), a first estimate of effort (S to XL), the problem, the solution, and how success would be measured (OKR). The content is a general reference not yet validated for O!Bank: targets are illustrative, and selection happens in Portfolio."

The definition of complexity in the proposal is my reading; the catalog defines the scale nowhere (question 11). The Russian `INTRO` needs the same change.

## Questions for the owner

1. Count rule. Should an area total include its cycles page, and should the eight cycles pages have boxes on the overview? The fix map assumes yes to both (totals 135, 130, 128, 97, 164, 132, 126, 134; map total 1,101). If the cycles pages are meant to stay off the map, the totals should be reduced to the sum of the boxes plus a stated number of area-level scenarios, and the introduction should say that 160 scenarios live one level down.
2. Lens vocabulary. One set of lens names for cards and problem tables, or three as now? And on the value-streams page: keep exactly one card per lens per stream, or relabel the ten or so cards whose lens does not fit (list in finding 3 of page 2)?
3. Stages and cards. Should each value-stream card name the stage it serves (mapping proposed above), and should the 11 stages with a stated problem and no card get a scenario or stay as acknowledged gaps?
4. Which streams apply to the Bank. Does the Bank run wealth management with managed mandates and an investment committee, bancassurance, wholesale paper issuance, rated debt, a payment factory? Should remittances and money-transfer systems, cards and acquiring (QR), and trade finance be on the map?
5. Regulators. Decide NBK and ARDFM (Kazakhstan) together with CBR. Please confirm three facts used or questioned in the fix map: the official English name of the Kyrgyz financial intelligence unit (I used "State Financial Intelligence Service of the Kyrgyz Republic"); whether NBKR requires LCR and NSFR returns; whether the Bank files currency-control notifications of the kind the two FX cards describe.
6. Committees and roles. Which body receives management accounts at the Bank (the stream says ALCO five times)? Which titles replace MLRO, Chief Audit Executive, Chief Accounting Officer and "business unit CFOs"?
7. Overlap. Value-stream cards repeat scenarios that area pages also hold, in different words. Keep both and cross-link, or reduce the stream cards to pointers?
8. "≥100%". 55 occurrences on 19 pages. Replace with "100%" everywhere?
9. "Cycle anchor" (drop, or define once on the page?) and the group "Customer-facing value streams" (rename, or move Treasury & Funding to the cross-cutting group?).
10. Peer frameworks. Should the two "(deferred)" boxes appear in the AICC portal at all, and with what wording?
11. Complexity. What does S, M, L, XL measure (effort, risk, number of systems), and against what reference? The three complexity changes in the fix map (034, 052, 071) are judgements by comparison with neighbours.
12. STR or SAR as the single name of the report in the Compliance stream?
