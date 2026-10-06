# Risk & Control, second half — review notes (risk-control-2)

Scope: five pages under `html-alt/financial-services/en/risk-control/` — `compliance-financial-crime`, `internal-audit`, `climate-esg-risk`, `strategic-reputational-risk`, `risk-cycles`. Fix map: `wiki/research/discovery-review/fixmap/risk-control-2.jsonl` (122 entries, ids `risk-control-2-001` … `-122`).

## Summary

- Read in full: 5 pages, 80 scenario cards, 18 level-3 sections, 5 cycles with their 25 stage dialogs, 16 problem rows on the four ordinary pages and 20 lens rows on the cycles page. The extract does not contain the page header intents, the problem tables of the four ordinary pages, or the stage dialogs of the cycles page; I read those from the source HTML.
- Completeness: 40 of the 80 cards have an empty OKR (compliance 13 of 18, internal audit 9 of 12, climate 8 of 13, strategic 10 of 12, cycles 0 of 25). All 40 are drafted in the fix map. No card is missing an intent, problem or solution; no section is empty; the counts shown on the area page (18, 12, 13, 12, 25) match the pages.
- The compliance page is the weakest for fit. Its licensing section and one card are written for US fintech state money transmitter licences, the SAR section names the US, Russian and Kazakh financial intelligence units but not the Kyrgyz one and gives the US 30-day filing deadline as a FATF rule, and the reviewer role is the "BSA officer" (US Bank Secrecy Act).
- The cycles page is complete and the cycle logic mostly holds, but several cards and stage dialogs state as fact that NBKR and the Kazakh regulator (NBK/ARDFM) have raised findings against the bank ("a recurring … examination finding", "has been the primary focus of NBKR and NBK/ARDFM supervisory feedback on prior submissions"). That is invented supervisory history and should not be published as written.
- Broken content is rare: one problem pasted from the neighbouring card (cycles), one problem sentence that says the opposite of what it means (strategic), one KR that counts six components where the card has five (compliance), four stray-space artifacts (cycles), and the slug-style tab labels ("Aml sanctions financial crime").
- Structure, same on all four ordinary pages: only one problems tab is rendered, named after the first of the page's two groups, and its four rows cover only that group; the sections are shown in an order that alternates between the two groups.
- Overlap is common: on each ordinary page two or three cards are a subset of a neighbour, and five cycle cards repeat cards on the area page or on the model-risk and operational-risk pages. These need an owner decision and are listed under Questions; I fixed only the overlaps that have an obvious one-line cure.
- Fix map totals: 40 OKR drafts; 82 other entries — 8 high, 43 medium, 31 low.

Reading note for the fix round: `current` is the rendered text (whitespace collapsed). Several source paragraphs contain line breaks, so match on normalised whitespace. For long paragraphs `current` is the first 200 characters and `proposed` is the whole replacement paragraph; entries 109 and 110 replace one sentence inside a multi-paragraph intent and say so in the locator. Stage dialog fixes (099–101, 114–116) point at the `FLOW_STAGES` JSON in the page script, not at markup.

## Page: Compliance & financial crime

What is on it: page intent; one problems tab ("Aml sanctions financial crime") with 4 rows; 6 sections of 3 cards each = 18 cards (Automation 9, Insights 8, Enablement 1; S 7, M 11). OKR filled on 5 cards, empty on 13. Entries 001–036.

Findings, most serious first:

1. "License Renewal Pack Assembly" only makes sense in the US: state money transmitter licences, surety bonds, "a bank with 40-50 active state licenses". The section intent above it says "For US-based fintechs, 45-50 state money transmitter licenses…". Two more cards in the section name "state money transmitter" jurisdictions. Proposed: reframe the card to the bank's own licences, permits and approvals and rewrite the section intent (001–004, 013, 014). Whether to keep the card at all is Q1.
2. The SAR section defines the filing as going to "FinCEN in the US, Rosfinmonitoring in Russia, KFM in Kazakhstan" and says "Under FATF … SARs must be filed within 30 days". The 30 days is the US rule; FATF says "promptly"; the Kyrgyz deadline is set by domestic law and is, as far as I know, much shorter. "SAR Filing Deadline Tracker" is built entirely on the 30-day window ("fewer than five days remain") and counts from the investigation-open date rather than from detection. Proposed: deadline-neutral wording and the Kyrgyz FIU named (005–008). The FIU name and the statutory deadline must be checked by Compliance (Q2).
3. "Sanctions Hit Investigation Pack": the Adoption KR says "all six investigation package components"; the solution and the objective list five (009).
4. "BSA officer" is the reviewer in three cards and their OKRs (12 occurrences). It is a US statutory role. Proposed page-wide replacement with "AML/CFT compliance officer" (018); the exact O!Bank title is Q2. My OKR drafts for these cards use "BSA officer" so that they match the cards until the rename is applied.
5. "AML Typology Library Update" takes its typologies from FinCEN, Rosfinmonitoring, KFM and FS-ISAC (a cyber-threat body, not an AML source). Proposed: FATF, the EAG (the regional FATF-style body the Kyrgyz Republic belongs to) and the national FIU; recipient aligned between intent and solution (010–012).
6. "Complaint Regulatory Escalation Tracker" defines its thresholds as "FCA/CFPB reportable complaints, NBKR complaint registry submissions"; the Conduct & complaints section rests board responsibility on "CRD IV and FCA SYSC" and cites a CBR ordinance, FCA PRIN and CFPB (015, 016).
7. "Examination Document Request Response Assembly" says a request "typically contains 80-150 items"; its neighbour says "100–200 item"; 80–150 is the section's figure for CCO hours (017). The same card is one of the four functions already inside "Regulatory Examination Readiness" (Q6); that card bundles four capabilities and is rated M like its single-capability neighbours (022, proposed L).
8. The only problems tab reads "Aml sanctions financial crime" (019). The page's second group — licensing, conduct, examinations — has no problem rows (Q8). Section order alternates between the two groups (023).
9. Small: "Regulatory Filing Calendar & Tracker" flags every filing three weeks ahead, which would flag monthly filings permanently (020); the filled OKR of the investigation-pack card says manual assembly takes "≥30 minutes" where the page's problem row says 15–25 (021).

Not fixed, for information: the page intent promises KYC/CDD and alert triage, and the "Insights" row describes mule-network detection; no card covers them. The page has a "New business opportunities" row and no New opps card. The sanctions section speaks of "domestic NBKR and CBR lists"; the Kyrgyz sanctions list is, as far as I know, kept by the FIU rather than by NBKR. Scale figures (50–2,000 alerts a day, 100–200 item examination requests) are those of a much larger bank.

## Page: Internal audit

What is on it: page intent; one problems tab ("Audit planning execution") with 4 rows; 4 sections of 3 cards = 12 cards (Insights 6, Enablement 3, Automation 3; S 3, M 9). OKR filled on 3, empty on 9. Entries 037–053.

This is the cleanest of the five pages; it has no jurisdiction problem beyond the global ones. Findings:

1. "Workpaper Quality Review Check" is tagged Insights; it runs a checklist and returns a deficiency list. The same pattern two sections down ("Remediation Evidence Quality Check") is Automation (037).
2. "Cross-Audit Risk Correlation Analysis" promises "an integrated three-lines view". The three things it joins are data sources (audit findings, operational risk events, regulatory observations), not the three lines of defence (038–040).
3. The "Audit execution & workpapers" section says workpapers are "reviewed by the Audit Committee and supervisors"; the Audit Committee does not review workpapers. Same paragraph: "For a 30-50 audit programme" (041).
4. "Audit Plan Dynamic Re-Ranking" re-ranks once, at mid-year. The page's "New business opportunities" row asks for a plan "updated continuously … rather than annually or semi-annually", which is exactly what the card does not do. I proposed only the honest title (042); the cadence is Q4.
5. The "Automation" problem row is about audit report drafting; no card drafts the audit report (the nearest drafts individual findings). Q4.
6. Tab label and section order as on the other pages (043, 044); the second group (findings synthesis, remediation) has no problem rows (Q8).

Not fixed: "Audit Findings Thematic Synthesis" already identifies repeat findings, and "Repeat Finding Root Cause Drill-Down" does the same over three years (Q6). The filled OKR of "Audit Universe Risk Ranking" counts four data sources where the solution reads five. Scale (80–150 auditable entities, 30–50 audits a year, 150–200 open items) is illustrative.

## Page: Climate & ESG risk

What is on it: page intent; one problems tab ("Physical transition risk") with 4 rows; 4 sections with 3, 4, 3 and 3 cards = 13 cards (Automation 5, Insights 5, Enablement 2, New opps 1; S 3, M 6, L 4). OKR filled on 5, empty on 8. Entries 054–071.

Findings:

1. The whole page assumes a European regulatory setting and a large-bank toolkit: IRB model parameters (5 mentions; as far as I know NBKR banks work on the standardised approach), EU taxonomy and green asset ratio (5), green bond allocation capacity, a project finance portfolio, third-party ESG ratings for borrowers, EBA guidelines (8). TCFD is named 28 times as the standing framework although the task force was wound up in 2023 and ISSB carries the standard now. I did not rewrite this card by card; it is Q5.
2. "TCFD Pillar 3 disclosure requirements" in the Physical risk section does not exist as such (054). The page intent says TCFD disclosure "is mandatory for regulated banks in most jurisdictions" and the disclosure section says it is increasingly mandatory "in NBKR and CBR frameworks"; both overstate (055, 056).
3. Overlaps with a simple cure: "Physical Risk Portfolio Assessment" ends by producing "the physical risk narrative for ICAAP", which is the next card's output (057); "Transition Risk & Carbon Exposure Analysis" recomputes the financed emissions that "Financed Emissions Calculation" computes (058).
4. Overlaps that need a decision (Q6): "Transition Risk Sector Stress Analysis" is the Disorderly-scenario slice of "Transition Risk & Carbon Exposure Analysis"; "Physical Risk Collateral Heat Map" and "Physical Risk Portfolio Assessment" both geocode the collateral register and overlay the same hazard layers; "ESG Disclosure Draft" repeats the commitment cross-reference of "TCFD Prior Commitment Tracking".
5. Small: "NGFS ordered transition scenarios" in the Enablement row (059); title "ESG Disclosure Draft" for a TCFD/ISSB draft (060); "reconciles financed emissions" with nothing to reconcile against (061); tab label and section order (062, 063).

Not fixed: team names drift between "sustainability team", "climate risk team" and, once, "ESG teams" (in a filled card and its OKR). Wildfire is listed among the hazards throughout; for the Kyrgyz Republic the relevant hazards are more likely flood and mudflow, drought and glacier loss — a point for Q5.

## Page: Strategic & reputational risk

What is on it: page intent; one problems tab ("Strategic decision risk") with 4 rows; 4 sections of 3 cards = 12 cards (Insights 6, Automation 3, Enablement 2, New opps 1; S 3, M 9). OKR filled on 2, empty on 10. Entries 072–093.

Findings:

1. "ESG Rating Agency Signal Monitor": the problem ends "a rating downgrade or controversy flag may be identified in the sustainability team's routine review before investor enquiries arrive" — that is the good outcome, not the problem. Rewritten to say the signal does not reach IR and the CRO in time (072). The card also assumes the bank is rated by MSCI, Sustainalytics and ISS and is held under "ESG-benchmarked institutional investor mandates" (Q7).
2. The page intent promises "a structured weekly picture"; nothing on the page is weekly (daily, monthly, quarterly, semi-annual) (073).
3. The "Insights" row gives "CBR digital ruble adoption impacts" as a strategic risk scenario; for the Bank the equivalent is the NBKR digital som (074, to be confirmed).
4. "Executive Mention & Media Monitor": the problem is that an adverse mention circulates for hours; the solution is a daily brief. Proposed an intraday alert for high-severity signals (076, 077), which also separates the card from "Reputational Signal Monitoring" — that card already monitors executive mentions and sends a daily brief to the same person (Q6).
5. "Strategic-Decision Risk Analysis" is tagged New opps; it drafts a CRO risk opinion (075, proposed Enablement). The two other cards of the section are parts of it: the risk appetite alignment check and the regulatory constraint mapping are two of its four opinion dimensions (Q6).
6. "Peer Earnings & Strategy Signal Digest" reads "10-K" filings and investor day transcripts, and its solution never says who receives the digest (078). Whether peers in the Kyrgyz market publish such material is Q7.
7. Crisis section intent: "post-crisis response executes the prepared materials" should be the response during the crisis, and the last sentence compares a time with itself (079, 080).
8. Lens drift between look-alike monitoring cards: publications-to-briefing is Insights in one card and Automation in the next (081). Tab label and section order (082, 083).

Not fixed: the "Strategic-decision risk analysis" section intent says the analysis "quantifies … the range of outcomes under competitive, regulatory, and macroeconomic scenarios"; none of its three cards does scenario quantification.

## Page: Risk Cycles

What is on it: a one-sentence page intent; 2 categories; 5 cycles (RCSA; stress testing; limits & breach governance; risk reporting; model validation), each with a summary intent, a full intent of 3–4 paragraphs, 4 lens rows (Analyze, Optimize, Automate, Enrich), 5 stages with a dialog each (title, intent, problem), and 5 cards (one per lens: Enablement, Automation, Insights, Optimize, New opps). 25 cards, all with OKR. Entries 094–122.

Cycle logic, cycle by cycle:

- RCSA (Identify → Assess → Score → Document → Refresh; annual with quarterly refresh). Coherent. Assess "produces an initial residual risk rating" and Score "derives the residual risk rating" — one output claimed twice (114). The Score dialog's problem is about action plan quality, which no stage owns. Cards attach to Identify (facilitation pack, pre-cycle brief), Assess (calibration challenge), Document (narrative drafting) and Refresh (trend signal); Score has no card. "RCSA Rating Calibration Challenge Assist" promises a peer-bank benchmark in the intent and delivers a cross-business-line one in the solution and OKR (105).
- Stress testing (Define scenarios → Run models → Aggregate → Approve → Submit; annual with mid-year ICAAP refresh). Coherent. The Aggregate dialog aggregates "credit, market, liquidity, and operational risk" although the Run stage runs credit, market, liquidity and climate (115). The text treats NGFS scenarios as "TCFD scenario frameworks" (109, 110) and the cards switch between "TCFD scenarios" and "NGFS pathways". "Continuous Capital Resilience Monitoring" is a monthly indicator and also covers liquidity (117, 118).
- Limits & breach governance (Set limits → Monitor → Detect breaches → Investigate → Resolve; continuous monitoring, weekly and monthly formal review). Coherent. No card serves Resolve, although the cycle intent promises "the committee-ready breach resolution summary". The dashboard card is "updated at each domain's monitoring cadence" in the intent and weekly in the solution (106). "Dynamic Soft-Breach Threshold Calibration" lets the agent move escalation thresholds with no approved band and no reviewer, and its Adoption KR accepts weekly recalibration for a problem defined as day-to-day (107, 108). "Floor, warning, and hard limit tiers" — a floor is not an escalation tier (119).
- Risk reporting (Aggregate → Validate → Brief → Discuss → Track actions; monthly ERMC, quarterly board risk committee, annual full board). The Discuss dialog says it "closes the reporting cycle" and is followed by a fifth stage (116). No card serves Aggregate, which the dialog calls the stage that "consumes the majority of the production window". The first sentence of the problem of "Risk Committee Pre-Read Structuring" belongs to the next card (094, high).
- Model validation (Inventory → Validate → Approve → Monitor performance → Retire; annual). Coherent. No card serves Retire, described as "the least governed stage". The Monitor dialog says monitoring by model developers is a governance gap; the dashboard card consolidates exactly those developer reports.

Findings across the page, most serious first:

1. Invented supervisory history. Four cards and three stage dialogs say NBKR and NBK/ARDFM have challenged or repeatedly found fault with the bank's RCSA descriptions, ICAAP narrative, limit structure and model inventory; three filled OKRs then target "examination findings reduced by ≥1 category severity" or "reduced to zero". Reworded to general supervisory patterns and to measures the bank controls (095–104).
2. Jurisdiction, special cases beyond the global list: the Kazakh regulator is named as a supervisor of the bank 23 times on this page (15 as "NBK/ARDFM", 8 as "NBK" in "NBKR/NBK/CBR") and 3 times on the compliance page; SR 11-7, a US supervisory letter, is the stated standard of the model validation cycle (25 mentions, including the cycle title and "SR 11-7 examination finding from NBKR"); SREP, an EU process, 8 times. Counts include the stage dialogs. Not rewritten one by one — Q3.
3. Wrong-card text, 094 above.
4. Logic and consistency items listed per cycle above (105–110, 114–119), plus: an Adoption KR that asks for "≥2 annual risk appetite reviews … per year" and names the CCO, who is not in the card (120); intent of "Validation Report Drafting" omits sensitivity testing that the solution and OKR include (121); page intent lists the cycles in another order (122).
5. Four stray spaces from source line breaks: "NBKR/ NBK/CBR", "risk-type- specific", "ICAAP/ ILAAP", "prior- period" (111–113).

Not fixed: "continuous-form" (7 times on this page) is not an English term; I changed it only where the thing described is monthly. Every cycle has the same complexity pattern S, S, M, M, M by lens, which looks templated rather than assessed (for example, monitoring deployment logs across all production systems is S). Lens names in the cycle tables (Analyze, Automate, Enrich) differ from the card lenses (Insights, Automation, New opps), and the Enablement card of each cycle has no row (Q9). "Dialog" and "dialogue" alternate inside the stress testing cycle (global spelling pattern).

## Questions for the owner

Q1. Compliance, "License Renewal Pack Assembly": keep the card reframed to the bank's own licences, permits and approvals (001–003, OKR draft 027), or drop it? As far as I know an NBKR banking licence is not renewed periodically, so the reframed card needs a real recurring obligation behind it (for example approvals of officers, payment-system or card-scheme attestations, correspondent-bank questionnaires).

Q2. Compliance terminology: what is the Bank's title for the officer who signs suspicious transaction reports (replacing "BSA officer", 018)? Should the catalog keep "SAR" or use the Kyrgyz term (suspicious transaction report)? Please have Compliance confirm the name of the FIU and the statutory filing deadline used in 005–008.

Q3. Supervisors and standards beyond the "CBR" pattern, to be decided once: (a) NBK/ARDFM (Kazakhstan) named as the bank's supervisor — 26 occurrences on my pages; (b) SR 11-7 as the governing model-risk standard, including the cycle title "Model validation cycle (SR 11-7)" — 25; (c) SREP, FinCEN, OFAC, FCA, CFPB, OCC, FDIC, EBA as cited authorities. And please confirm that statements about what NBKR has found in examinations of the bank are to be removed everywhere, as proposed in 095–104.

Q4. Internal audit: should "Audit Plan Dynamic Re-Ranking" stay a mid-year exercise (then the title in 042 applies) or become quarterly and event-driven, as the "New business opportunities" row describes? Should a card for audit report drafting be added to answer the "Automation" row, or the row be rewritten to the cards that exist?

Q5. Climate page: is it to be re-based on what applies to the Bank — NBKR expectations, the national green taxonomy, ISSB rather than TCFD naming, internal PD/LGD from IFRS 9 rather than IRB, hazards relevant to the Kyrgyz Republic — or kept as a forward-looking international reference? The answer decides a few dozen phrases on the page and whether "Green Finance Pipeline Screening" (green bond allocation) stays.

Q6. Overlapping cards — merge, or keep both with a sharper boundary? Compliance: "Regulatory Examination Readiness" contains "Examination Document Request Response Assembly". Internal audit: "Audit Findings Thematic Synthesis" and "Repeat Finding Root Cause Drill-Down". Climate: "Transition Risk & Carbon Exposure Analysis" and "Transition Risk Sector Stress Analysis"; "Physical Risk Collateral Heat Map" and "Physical Risk Portfolio Assessment". Strategic: "Strategic-Decision Risk Analysis" contains the two other cards of its section; "Reputational Signal Monitoring" contains "Executive Mention & Media Monitor". Cycles against other pages: "ICAAP/ILAAP Narrative Section Drafting" [S] and the area-page "ICAAP/ILAAP Narrative Assembly" [M]; "Breach Pattern — Limit Recalibration Brief" and the area-page "RAF Threshold Calibration Synthesis"; "Validation Findings Thematic Synthesis" [New opps] and model-risk "Model Validation Finding Synthesis" [Insights]; "Model Portfolio Performance Health Dashboard" and model-risk "Model Performance Monthly Dashboard"; "RCSA Risk Identification Facilitation Pack" and operational-risk "RCSA Facilitation Support".

Q7. Strategic page: do the scenarios that presuppose a capital-market setting stay — ESG ratings of the bank by MSCI, Sustainalytics and ISS with ESG-benchmarked investor mandates; peer earnings releases, investor days and 10-K filings? If they stay, should the sources be re-based on what exists locally (published financial statements, stock exchange disclosures, NBKR statistics)?

Q8. Problems tables on the ordinary pages (I count 39 of the catalog's 66 level-2 pages with exactly one tab, so this is probably catalog-wide): each page shows one tab named after its first group and four rows that cover only that group. Should rows be written for the second group of each page ("Conduct regulatory adherence", "Findings remediation", "Esg exposure disclosure", "Reputational signal response"), or should the single tab simply carry the page name? The tab labels I corrected (019, 043, 062, 082) and the same slug-style group labels on the area page ("Var sensitivity", "Pl attribution backtest") come from the same source. Is the alternating section order (023, 044, 063, 083) intended?

Q9. Cycles page, by design or not: lens names in the cycle tables differ from the card lenses and the Enablement card has no row; three stages have no card (Resolve, Retire, and Aggregate in the reporting cycle); complexity is S, S, M, M, M in every cycle. If other cycle pages follow the same template this should be decided once.

Q10. Roles and committees are generic throughout — ERMC, board risk committee, EXCO, Capital Committee, Model Risk Committee, breach resolution committee, CAE, CCO, Chief Strategy Officer, Head of Investor Relations, Risk Strategy team, and "Model Risk Management" here against "Chief Model Risk Officer" on the model-risk page. Should they be mapped to O!Bank's actual bodies and titles, or left generic? The OKR drafts name the roles exactly as the cards do.
