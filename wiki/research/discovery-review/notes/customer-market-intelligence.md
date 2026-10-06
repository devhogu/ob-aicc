# Customer & Market Intelligence: review notes

Reviewer id `customer-market-intelligence`. Source `html-alt/financial-services/en/customer-market-intelligence/` (9 pages, 128 cards). Fix map: `fixmap/customer-market-intelligence.jsonl` (169 entries: 86 OKR drafts and 83 other fixes — 11 high, 36 medium, 36 low).

## Summary

- All 9 pages and all 128 cards were read: the area page (6 cards), seven sub-area pages (105 cards) and the Intelligence Cycles page (17 cards, 4 cycles, 20 stage dialogs). No card lacks a title, intent, problem or solution; no template token or truncated sentence appears in card text.
- 86 of the 105 sub-area cards have an empty OKR (segmentation 15, voice of customer 12, retention 11, lifetime value 13, wallet share 10, market share 13, brand 12). All 86 are drafted in the fix map. The area page and the cycles page are fully filled.
- The filled OKRs are not reliable as they stand: six of them state a "before" that contradicts the card's own problem (for example "from monthly batch recalculation" where the problem says quarterly), and five on the cycles page measure a recipient or an output the card does not name.
- Three regulatory references are wrong, not merely foreign: CBR Ordinance No. 3854-U is cited three times as a complaint-handling rule (it is the Russian cooling-off rule for voluntary insurance, as far as I can tell — please verify), and "OECD CRS" (the tax-information exchange standard) is cited as a basis for LTV assumptions, in a sentence that also confuses lifetime value with loan-to-value.
- The Kyrgyz regulator is nearly absent from this area. NBK (Kazakhstan) is cited 43 times, CBR 37 times, NBKR 15 times; the Voice of customer and Brand & reputation pages cite NBK and CBR twelve times each and NBKR never. The word "Kyrgyz" does not occur; the market is framed as "KG, KZ and RU" or "CIS".
- The area carries a great deal of repetition. In most sections the Automation card and an Insights card describe the same output twice, and one pair on the Brand page is the same scenario under two titles. I count about ten pairs within pages and six more between the sub-area pages and the cycles page. These need an owner decision and are listed under Questions.
- Lens and complexity look assigned by template: 34 of the 35 sections are S/S/M or S/M/M (the other is S/S/S), the only L in the area is on the area page, and there is no XL. Lens split: Insights 62, Automation 37, Enablement 18, Optimize 6, New opps 5.
- Several cards keep vocabulary from a subscription business or from the United Kingdom ("billing", "per pound spent", "offshore teams", "support-ticket spike"). The concrete cases are in the fix map.

## Counts on the overview compared with the cards present

- The overview (`_root.md`) shows "Customer & Market Intelligence (111)". The area holds 128 cards. The difference is exactly the 17 cards of the Intelligence Cycles page: 111 = 105 sub-area cards + 6 area-level cards.
- This is a rule, not a slip. In all eight areas the overview total equals sub-area cards plus area-level cards and leaves the cycles page out (banking data 114 of 134, customer channels 80 of 97, finance 101 of 126, risk 139 of 164, shared capabilities 112 of 132, initiatives 113 of 130, portfolio 116 of 135). The overview also does not list the cycles pages at all, so a reader of the overview cannot tell they exist.
- Every other count is correct: the seven sub-area counts (18, 15, 15, 15, 12, 15, 15), every section count (3 each), and the cycles counts on the area page (17; 4, 5, 4, 4) match the cards present.
- No fix-map entry: whether the total should become 128, or the cycles should be listed separately, is an owner decision (Question 1).

## Things the extract did not show

- The page header intent of every page and the eight "problems" rows of the area page are missing from the extract files for this area. I read them from the HTML. The page intents are sound; findings on them are below.
- The 20 stage dialogs of the cycles page are held in a script object (`FLOW_STAGES`) and appear in the extract only as button markup. I read them from the HTML: each has a title, intent and problem; none is broken.

## Special cases of the global patterns, and catalog-wide patterns not on the brief's list

- Regulators: beyond CBR next to NBKR, this area has a third regulator, NBK with its agency ARDFM (Kazakhstan), and 30 fields that cite NBK or CBR with no NBKR beside them. A blanket replacement of "CBR" will not reach them.
- Spelling: the section title "Save-program design" is American while its own cards say "Save-Programme"; the cycles page is American in its page text and British in its cards.
- Group labels on the area page are generated from slugs, so acronyms and punctuation are lost: "Clv measurement", "Clv driven decisions", "Synthesis action", "Reputation defense build". The same defect is on other area pages ("Aml investigations sar", "Basel corep finrep", "Var sensitivity", "Pl attribution backtest"). Entries 001–004 fix the four labels here.
- Section order: on all seven sub-area pages the sections alternate between the two groups shown on the area page (first of group one, first of group two, second of group one, and so on), and the group names are not shown on the page. The four other areas I sampled do the same, so this is generator behaviour. No entries.
- The "problems" block (four rows by lens under the page header) is absent from all seven sub-area pages here. It is present on every sub-area page of five areas and absent in three (this one, strategic portfolio, strategic initiatives). Question 4.
- Row labels: the cycles page labels its problem rows Analyze, Optimize, Automate, Enrich, which are not the five card lenses; the area page labels them with raw slugs ("insights", "new-opps").

## Page by page

### Area page — `customer-market-intelligence/index.html`

On it: header intent, two problem tabs with four rows each, eight sub-area tiles with counts, 6 area-level cards (all OKRs filled; Insights 5, Optimize 1; S 4, M 1, L 1).

- "Repeat-Contact & Poor-Outcome Correlation Analysis": the first sentence of the problem is broken (no main clause); the solution is written as an instruction ("Take 12 months of customer interactions…") with "AI" as actor; the OKR objective is an imperative with no recipient. Entries 012–014.
- "Customer Contact Root-Cause Intelligence": the objective promises a weekly cadence while Adoption measures only monthly review, and it is also an imperative. Entries 006–007.
- "Peer-bank competitive intelligence": the problem cites Call Report, FFIEC and EBA disclosures. The whole card rests on peer earnings calls and Pillar 3 reports. Entry 011 removes the United States and EU filings; whether the premise holds for the Bank's peers is Question 3.
- "Voice-of-customer / NPS verbatim synthesis": "Banks collect thousands…" and "offshore teams" describe another scale. Entry 009.
- Four group labels broken by slug rendering. Entries 001–004.
- Four of the six titles are in sentence case, the rest of the area in title case. Entries 005, 008, 010, 015.
- The two contact-analysis cards read as contact-centre analytics and overlap "Multi-Contact Chain Detection" on the Retention page. The "new-opps" problem rows state opportunities, not problems; I take that as intended.

### Customer segmentation — 18 cards, 6 sections, 15 empty OKRs

- Two of the three filled OKRs contradict their cards: "Segment Migration Tracker" says it replaces monthly recalculation where the problem says quarterly; "Cohort Migration Report" gives a 5–7 day baseline where the problem says one to two analyst days. Entries 029, 030.
- "Segment migration tracking" section: an OECD "fair-lending monitoring" requirement is asserted, and it is about risk tiers, not segments. Entry 016.
- "Transaction Pattern Anomaly Flag": the last sentence of the problem does not parse. Entry 020.
- Near-duplicates: "Needs-Cluster Inference" and "Needs Segment Transaction Inference" open with the same sentence and build the same clusters from the same data; "Behavioural Segment Refresh" (fortnightly) and "Segment Migration Tracker" (weekly) both recalculate segment membership, and the cycles page adds a third ("Segment Stability Continuous Monitor"). Question 2.
- Misplaced: "High-Value Attrition Early Warning" is an at-risk identification card and belongs with Retention & churn. Question 6.
- Lens: three cards carry a lens that does not match what they do. Entries 018, 032, 034. Smaller wording fixes: 025, 037.
- Fit: "KZ and KG banking markets", "CIS banking markets", "NBK/ARDFM consumer-credit regulations" in section intents (global pattern).

### Voice of customer — 15 cards, 5 sections, 12 empty OKRs

- Wrong reference, three times (page intent, "Complaint data" section, "Regulatory Exposure Theme Scoring" solution): CBR Ordinance No. 3854-U as a complaint-handling rule, next to a Kazakhstan standard whose agency is misnamed. The scoring card is calibrated on these two documents, so the scenario as written works only in another jurisdiction. Entries 040, 042, 055 put neutral wording; the right NBKR instrument is Question 3.
- "NPS & CSAT surveys" section claims that NPS trend is a supervisory-monitored indicator under CBR and NBK frameworks. I know of no such rule. Entry 041.
- "CSAT Post-Interaction Monitor": "daily" and "real-time" in one sentence. Entry 045.
- "Cross-Channel VoC Synthesis": "four separate channel reports" after five sources are listed. Entry 049.
- Near-duplicates: "Complaint Theme Extraction" and "Complaint Driver Insights" are both a weekly thematic classification of complaint text for ops prioritisation. Question 2.
- Three cards in the area fill the regulatory complaint report ("Complaint Theme Extraction", "Complaint Volume Trend Dashboard", and "Conduct Signal Regulator Report Preparation" on the Brand page). All assume a periodic complaint-report template required by the regulator. Question 3.
- NBKR is not named once on this page.

### Retention & churn — 15 cards, 5 sections, 11 empty OKRs

- "At-Risk Scoring and Triage": the OKR baseline is "monthly batch scoring", while the problem says there is no systematic scoring, only relationship-manager judgement and occasional studies. Entry 069. (The cycles page does assume a monthly scoring run, so the two pages disagree about today's state.)
- "Cohort Retention and Cross-Sell Window Analysis" is a cross-sell timing card: nothing in it analyses retention, and it sits in "Churn cohort analysis". Entry 061 corrects the title, entry 062 the "continuous" in its OKR; moving it to Wallet share is Question 6.
- "Save-Programme Efficacy Report": the solution gives the report to CX leadership, the OKR to the retention lead. Entry 071.
- "Intervention efficacy tracking" section cites "OECD consumer-finance guidelines". Entry 059.
- Near-duplicates: "Save-Offer Effectiveness Insights", "Save-Programme Efficacy Report" and "Intervention ROI by Cohort" all analyse the same save-programme outcomes; "Save-Programme Cohort Brief" has an almost word-for-word twin on the cycles page ("Retention Cohort Profiling Brief"). Question 2.
- Vocabulary from a subscription business in the "At-risk customer identification" section ("usage decline, support-ticket spike, payment failure"). Not rewritten; mentioned for the global round.
- Small fixes: 065, 068.

### Customer lifetime value — 15 cards, 5 sections, 13 empty OKRs

- "CAC / LTV / payback" section: "Under OECD CRS and regional regulatory expectations for consumer credit, LTV assumptions underpin pricing and provisioning." OECD CRS is about tax information, and pricing and provisioning depend on loan-to-value, not lifetime value. Entry 077 removes the sentence.
- Sterling: "per pound spent" twice and "CLV-preserved-per-pound". Entries 078, 092, 095.
- "Unit Economics Channel Dashboard": costs are said to be missing "in the denominator" of CAC; they are the numerator. Entry 081.
- The page is the most repetitive of the area. "CAC/LTV Payback Monitor", "Unit Economics Channel Dashboard" and "Channel LTV/CAC Ranking" are three quarterly CAC/LTV/payback views by channel; "Cohort CLV Vintage Monitor" and "Cohort CLV Trajectory Report" are the same quarterly trajectory against projection; "Segment CLV Automated Refresh" and "Segment CLV Comparison Report" are the same quarterly segment CLV, and their problems disagree on whether the calculation is quarterly or annual today (entry 098 removes the contradiction). Question 2.
- "Segment CLV ROI Attribution" computes no ROI; it attributes CLV movement to drivers. Entry 102.
- Lens and complexity: two optimisers are not under Optimize (087, 094); the multi-touch attribution model is rated S beside M neighbours (084).
- "Billing" data and systems, three places. Entries 089, 097, 099.
- CLV and LTV are used for the same thing throughout; I left this, since "CAC/LTV" is the usual pair.

### Wallet share — 12 cards, 4 sections, 10 empty OKRs

- "Salary-Switch Risk Alert": the intent lists a missed salary credit as an early signal, while the problem calls the first missed credit the point of loss. Entries 106, 107.
- "Competitor-held share estimation" section: two different source lists in two sentences, one of them "declined-competitor-offer data", which no bank holds. Entry 103.
- The page intent states as fact that "the bank holds less than 40% of their total financial wallet", and the first section that primary-bank customers have "three to five times the revenue potential". Question 5.
- This sub-area has four sections where the others have five or six; the "Share growth" group has one. The misplaced cross-sell card from Retention would fit here.
- Small fix: 110.

### Market share & competitive positioning — 15 cards, 5 sections, 13 empty OKRs

- "Product Market-Share Monitor": OKR baseline of 3–5 days against a problem that says two to three analyst days. Entry 119.
- Two section intents describe only Kazakhstan and Russia ("In Kazakhstan, NBK publishes…; in Russia, CBR quarterly reports…", "In KZ and RU markets…"). Entries 117, 118.
- "Segment Share Competitive Gap Analysis" measures the gap to the strategic target, not to competitors. Entry 130.
- "Regulatory Filing Intelligence Monitor": the solution swaps "enforcement actions" for unpublished "regulatory correspondence" (entry 132). The card assumes public regulator databases of licence applications and transaction notifications. Question 3.
- Near-duplicates: "Segment Share Monitoring Report" and "Segment Share Estimation Model". Question 2.
- "Competitor Move Intelligence Brief" relies on earnings transcripts and analyst notes. Question 3.
- Small fixes: 126, 128.

### Brand & reputation — 15 cards, 5 sections, 12 empty OKRs

- "Reputational Risk Composite Automation" and "Reputation Risk Composite Signal" are one scenario twice: the same four signals, the same weekly score for the CRO, the same quarterly board section. This is the clearest duplicate in the area. Question 2. The filled one also says "from monthly manual aggregation" where its problem says quarterly, and its title drops the "-al". Entries 145, 144.
- "NPS & Brand Equity Board Report" and "NPS & Brand Equity Dashboard" overlap: the dashboard card says the board section is sourced from it. Question 2.
- First section repeats the claim that NPS is a supervisory indicator under CBR guidance. Entry 137.
- Social channels: the section and "Social and Media Brand Monitor" name Telegram, VKontakte, Instagram and Twitter/X as the channels to monitor. Question 3.
- NBKR is not named once on this page; "Product Complaint Concentration Analysis" rests on an NBK and ARDFM supervisory metric.
- Small fixes: 138, 142, 152.

### Intelligence Cycles — 17 cards, 4 cycles, all OKRs filled

- "Segment Stability Continuous Monitor": continuous in the intent, weekly in the solution, daily in the OKR; the alert goes to segment heads in the intent and OKR and to the data science team in the solution. Entry 159.
- "Segmentation Governance Pack Drafting": the problem is the four-to-six-week committee cycle, which drafting does not shorten. Entry 157.
- "Retention Cohort Profiling Brief": "≥48 consecutive cycles" with a monthly scoring run is four years; carried over from the weekly twin. Entry 160.
- "Retention Offer A/B Optimisation": baseline of "quarterly manual A/B result aggregation" where the problem says there is no structured A/B testing. Entry 161.
- OKRs that name a role or output absent from the card: "Brand Signal Continuous Aggregation" (digest for communications leadership instead of feed for the brand analytics team), "Brand Materiality Alert Calibration" (does not measure the calibration), "Competitive Signal Continuous Scan", "Competitive Coverage Gap Audit", "Brand Commercial Impact Model". Entries 162, 164, 165, 166, 169.
- "Competitive Coverage Gap Audit": the example list is copied from the Brand sentiment cycle. Entry 163.
- "Brand Response Protocol Assistant": the problem says no protocol exists, the solution classifies against one. Entries 167, 168.
- Each cycle repeats sub-area cards under new names: continuous brand aggregation and "Social and Media Brand Monitor"; materiality alert and "Sentiment Crisis Threshold Alert"; response protocol assistant and "Crisis Response Brief Generator"; continuous scan and "Competitor Move Intelligence Brief"; real-time churn detection and "At-Risk Scoring and Triage". This may be by design of the cycle view. Question 2.
- Small fixes: 155, 156, 158.

## About the 86 OKR drafts

- Each draft follows the filled cards of this area: an objective naming the output and who receives it, Adoption as share of scheduled cycles over a run of weeks, months or quarters, Acceptance as share confirmed by the reviewer the card names, Cycle as before and after. Lengths match the catalog (median objective 219 characters against 220).
- Cadences, roles and baselines are taken from the card. Where a card gives no baseline time, the Cycle result says "moved from not produced to…" and does not invent a duration.
- Six cards state no cadence (Fraud Propensity Tier Overlay, Early-Warning Signal Calibration, Channel-Vintage CLV Comparison, Propensity Model Cross-Sell Insights, Product Combination Retention Analysis, Underserved Region Opportunity Brief). Their drafts say "scheduled cycles" or give an illustrative frequency; the owner may want to set the cadence in the card first.
- Two cards name no reviewer (Value-Tier Classification, Channel-Vintage CLV Comparison); their Acceptance results use the team that receives the output.
- Drafts for cards listed as duplicates are written for each card as it stands. If two cards are merged, one draft falls away.

## Questions for the owner

1. Overview total: should "Customer & Market Intelligence (111)" count the 17 cycle cards (128), or should the overview list the cycles page separately? The rule is the same in all eight areas.
2. Repeated scenarios: merge, or keep and make the difference explicit? Within pages: Reputational Risk Composite Automation / Reputation Risk Composite Signal; CAC/LTV Payback Monitor / Unit Economics Channel Dashboard / Channel LTV/CAC Ranking; Cohort CLV Vintage Monitor / Cohort CLV Trajectory Report; Segment CLV Automated Refresh / Segment CLV Comparison Report; Needs-Cluster Inference / Needs Segment Transaction Inference; Behavioural Segment Refresh / Segment Migration Tracker; Complaint Theme Extraction / Complaint Driver Insights; Segment Share Monitoring Report / Segment Share Estimation Model; NPS & Brand Equity Board Report / NPS & Brand Equity Dashboard; Save-Offer Effectiveness Insights / Save-Programme Efficacy Report. Between the sub-area pages and the cycles page: the five pairs named under Intelligence Cycles, and Save-Programme Cohort Brief / Retention Cohort Profiling Brief.
3. Scenarios that lean on another jurisdiction — keep, adapt, or drop? (a) Peer earnings calls, Pillar 3 reports, earnings transcripts and analyst notes as sources about peer banks (Peer-bank competitive intelligence; Competitor Move Intelligence Brief). (b) Public regulator databases of licence applications and transaction notifications (Regulatory Filing Intelligence Monitor). (c) A periodic complaint-report template required by the regulator (Complaint Volume Trend Dashboard; Conduct Signal Regulator Report Preparation), and the rule a complaint theme is scored against (Regulatory Exposure Theme Scoring): which NBKR instrument should be named? I put neutral wording and did not cite one. (d) Social channels: are VKontakte and Twitter/X relevant for the Bank, and should Kyrgyz-language processing be stated?
4. The "problems" rows are missing on all seven sub-area pages (present in five other areas). Should they be drafted — four rows for each of seven pages?
5. Figures stated as fact in descriptive text ("less than 40% of their total financial wallet", "three to five times the revenue potential", "40% lower LTV", "four to six weeks", "90% of the feedback received"): keep, mark as illustrative, or remove?
6. Misplaced cards: move "Cohort Retention and Cross-Sell Window Analysis" to Wallet share / Cross-sell opportunity identification, and "High-Value Attrition Early Warning" to Retention & churn / At-risk customer identification? A move changes the card's URN.
7. Roles and segments: the cards assume a CCO, CMO, Head of CX, CRO, board secretary, segment heads, a retention team, a save-programme team and a pricing committee, and the segments retail mass, emerging affluent, SME micro and SME core. Should these be mapped to the Bank's own roles and segments, or left as catalog vocabulary?
8. Complexity: is S/M meant relative to the section? As it stands, per-customer predictive models (Competitor Share Inference Model, Segment Share Estimation Model, At-Risk Scoring and Triage, Next-Best-Offer Prioritisation) are M, while the comparable area-level "Customer health score" is L.
9. Group labels and section order come from the generator (slug-derived labels; alternating section order with no group names on the page). Fix in the generator for the whole catalog, or in content? Entries 001–004 assume the labels can be set in this area's page.
