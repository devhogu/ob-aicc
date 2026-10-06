# Risk & Control, first half — review notes (`risk-control-1`)

Scope: the area page `risk-control/index.html` and six sub-area pages — credit risk, market risk, liquidity risk, operational risk, model risk, cyber risk — under `html-alt/financial-services/en/risk-control/`. Seven pages, 84 scenario cards. Fix map: `fixmap/risk-control-1.jsonl`, 130 entries (58 drafted OKRs, 72 other fixes: 7 high, 23 medium, 42 low).

## Summary

1. 58 of the 79 cards on the six sub-area pages have an empty OKR (credit 15 of 19, market 10 of 12, liquidity 8 of 12, operational 8 of 12, model 9 of 12, cyber 8 of 12). All 58 are drafted in the fix map. The five cards on the area page are filled.
2. Apart from the OKRs the cards are complete: every card has a title, intent, problem and solution, every section has an intent and three or four cards, and no card or URN is duplicated. The text is fluent and specific; I found one broken sentence and no placeholders other than the known `service.eyebrow`.
3. The counts on the overview page and the area page all match the cards present. The area total of 139 leaves out the 25 cards of the Risk Cycles page; see the reconciliation below.
4. The plain-text extract does not contain the page header intents (missing on all 76 pages of the catalog) or the "Problems" rows (missing on 48 pages). I read both from the source HTML for my seven pages. Reviewers who worked from the extract alone have not seen them.
5. Six content errors a reader would notice (seven high-severity entries): a contradiction about the large-exposure threshold (credit), a daily NSFR where the page says monthly (liquidity), the Kazakh tenge as the Bank's currency (market), a key result that contradicts itself (credit), "all three data sources" followed by four (operational), and one broken sentence (model).
6. The group labels on the area page and the "Problems" tab labels are generated from URL slugs and read as broken English ("Aml sanctions financial crime", "Var sensitivity", "Pl attribution backtest", "Loss events kris", "Esg exposure disclosure"). This is catalog-wide, not in the brief's list of global patterns. The 23 labels in my scope are in the fix map.
7. Fit for O!Bank is the weakest side of this half. The pages describe a bank with IRB credit models, an Internal Models Approach trading book with several desks and options, AMA operational risk capital, and EU (DORA, EBA) and US (SR 11-7) rules cited as binding. The model risk page does not mention the NBKR at all. About 15 cards only make sense under those regimes; they are listed below for an owner decision.
8. Lens use is not consistent: the same kind of card (breach pack, watch or alert, calibration review, daily narrative) carries different lenses on different pages, and no card on the six sub-area pages uses "Optimize" or "New opps" although every page has a "New business opportunities" problem row.

## Counts on the overview page compared with the cards present (whole Risk & Control area)

| Where | Shown | Cards present | Match |
|---|---|---|---|
| Overview: Risk & Control | 139 | 164 on all twelve risk-control pages | differs by 25 |
| Overview: ten sub-areas (12, 18, 12, 12, 12, 13, 19, 12, 12, 12) | sum 134 | 134 | yes, each one |
| Area page, cards under "Scenarios" (no count shown) | — | 5 | — |
| Area page: Risk Cycles | 25 (5 cycles × 5) | 25 | yes |
| Area page: 44 section counts of the ten sub-areas | 42 × "(3)", 2 × "(4)" | same | yes, each one |

The difference has two parts and both are rule, not error.

- 139 = 134 cards on the ten sub-area pages + 5 area-level cards on the Risk & Control page itself. A reader who adds up the ten numbers printed under the heading gets 134, not 139, because the five area-level cards are counted in the total but listed nowhere on the overview.
- The 25 cards of the Risk Cycles page are not in the 139 and Risk Cycles is not listed or linked under Risk & Control on the overview. The area page does show it ("Risk Cycles (25)", eyebrow "Risk governance").

The same rule holds in every area: overview total = sub-area pages + area-level cards, cycles page left out. Across the catalog the overview totals sum to 941 while 1,101 cards exist; the missing 160 are the eight cycles pages. One thing that can mislead: the overview lists "Risk Management Cycle (5)" under Operational Value Streams. That is a section of the value-streams page, not the Risk Cycles page, and the two names are close.

Per-page actual counts, for the record: area page 5; credit risk 19; compliance & financial crime 18; market risk 12; liquidity risk 12; operational risk 12; cyber risk 12; model risk 12; strategic & reputational risk 12; climate & ESG risk 13; internal audit 12; risk cycles 25.

## Area page — `risk-control/index.html`

On it: page intent; one "Problems" tab ("Non-financial risks", four rows); eleven sub-area cards with 20 group labels and 49 section links (44 sections, 5 cycles); five area-level scenario cards (one per lens; four M, one L), all with OKRs.

Findings, most serious first.

- Problem rows exist only for "Non-financial risks". Financial risks (credit, market, liquidity) is the first group on the page and has no rows; neither do Independent assurance and Risk governance. Other areas with two groups have two tabs (Strategic Banking Portfolio, Customer & Market Intelligence). I drafted the four "Financial risks" rows from the credit, market and liquidity pages (fixes 002–005). Adding a tab is a structure change, so see Questions.
- 18 of the 20 group labels are slug-derived (fixes 006–023). Two of them also describe the wrong content: "Control testing tprm" sits over third-party risk and business continuity, and there is no control-testing section anywhere; "Pl attribution backtest" also holds limits utilisation.
- The page intent cites "NBK/ARDFM", the Kazakhstan regulators, beside NBKR and CBR (fix 001; same on the credit risk page, fix 027).
- "ICAAP/ILAAP Narrative Assembly": "ICAA" is used without expansion in a key result (fix 025). Complexity M looks low next to "CRO Risk Synthesis" (L): fourteen to twenty contributors, seven disciplines, two regulatory documents (fix 024, low).
- "RAF Threshold Calibration Synthesis": the Cycle key result is hard to parse (fix 026).
- "Regulatory Capital Efficiency Signal Detection" depends on IRB eligibility, a choice between standardised and internal-model market risk, and "SMA calibration". It only makes sense for a bank with those permissions; see Questions. Its lens is "New opps" although it optimises capital; left as is, because "New opps" is used loosely across the catalog.
- "CRO Risk Synthesis" bundles three different things — stress-test narrative, emerging-risk signals, and pre-drafted crisis narratives — into one Board Risk Committee pack. The text is consistent with itself; no fix proposed.
- Card order on the area page (credit, compliance, risk cycles, market, liquidity, operational, cyber, model, strategic, climate, internal audit) mixes the groups that the overview keeps apart (non-financial, financial, independent assurance). "Risk Cycles" is capitalised differently from the other sub-area names. Both are for the owner; no fix proposed.

## Credit risk — `risk-control/credit-risk/index.html`

On it: page intent; one "Problems" tab ("Counterparty exposure", four rows); six sections; 19 cards (8 Insights, 7 Automation, 4 Enablement; 16 M, 3 S); 4 OKRs filled, 15 empty.

- 15 empty OKRs, all drafted (fixes 030, 032, 033, 035, 037–040, 042, 043, 045, 047, 052–054).
- Contradiction on the large-exposure threshold. The first section says an exposure above 10% of Tier 1 "triggers enhanced reporting"; the second says notification is required above 25%; the card "Counterparty Exposure Breach Investigation Pack" treats crossing 10% as a breach with mandatory supervisory notification. The proposed intent names the limit without a figure (fix 029, high). The same card is called an "investigation pack" in title and intent and a "notification pack" in problem and solution (fix 031). Which percentages the NBKR actually sets is a question for the owner.
- "Basel III Art. 395" is a wrong reference; Article 395 is in the EU Capital Requirements Regulation (fix 028).
- "Credit Early-Warning Signal Enrichment": the Acceptance key result contradicts itself — at least 70% of flags material, and at most 20% immaterial (fix 050, high). Its lens is Enablement although it is a monitoring and alerting card (fix 049, low). "Manager cycle" in the solution is unclear (fix 051).
- "Vintage Cohort Performance Report": the intent promises prepayment speeds, the solution delivers migration paths (fix 044).
- "Watchlist Dossier Assembly": the intent lists exposure data as the fourth component; problem, solution and OKR say prior committee minutes (fix 048).
- "BCBS 239 requires … real-time concentration monitoring" overstates the standard (fix 034). "PD-point-in-time estimates" (fix 041).
- "Watchlist Covenant Breach Tracker" is rated S while the simpler "Watchlist Dossier Assembly" beside it is M (fix 046, low).
- The three cards of "PD/LGD/EAD model outputs" and the section intent assume approved IRB models ("NBKR and CBR IRB approval frameworks"). "IRB Model Performance Signal Watch" covers the same ground as two cards on the model risk page ("Model Performance Monthly Dashboard", "Model Performance Deterioration Alert") for the credit models only. See Questions.
- "NBKR Regulation No. 16" is cited for watchlist management; I could not verify the number. "Special Mention" is a US classification term.
- The "Problems" rows describe the whole page, not the "Counterparty exposure" group named on the tab. The "New business opportunities" row has no card with that lens.
- Sections appear on the page in an order that alternates between the two groups shown on the area page (analytics, concentration, PD/LGD/EAD, vintage, watchlist, ECL). Same on the other five pages; probably the layout, noted only.

## Market risk — `risk-control/market-risk/index.html`

On it: page intent; one "Problems" tab ("Var sensitivity", four rows); four sections; 12 cards (6 Automation, 4 Insights, 2 Enablement; 9 M, 3 S); 2 OKRs filled, 10 empty.

- 10 empty OKRs, all drafted (fixes 059–063, 065, 067, 070, 071, 073).
- The Enablement problem row asks "what if the KZT depreciates 15%". KZT is the Kazakh tenge (fix 056, high).
- The whole page assumes a trading book with several desks, options books reported by Greeks, and capital under the Internal Models Approach with Basel backtesting and stressed VaR. The page intent mentions IRRBB and FX but no section or card covers the banking book or the open FX position. If the Bank has no such trading book, at least five cards have no object: "VaR Model Backtesting Pack", "Stressed VaR Scenario Narrative", "Backtesting Exception Documentation Pack", "Greeks Daily Position Report", "Sensitivity Risk-Factor Concentration Analysis". See Questions.
- Two cards overlap. "VaR Model Backtesting Pack" (section VaR & expected shortfall) and "Backtesting Exception Documentation Pack" (section P&L attribution & backtesting) both keep the rolling 250-day exception count, both apply the traffic-light classification, and both draft the supervisory notification. The first also sits in the wrong section. I drafted distinct OKRs (monthly report against per-exception pack) and left the texts alone; see Questions.
- Three problem rows have no card that answers them: overnight anomaly detection on VaR (Insights), on-demand what-if stress runs (Enablement), and continuous limit headroom for the desks (New business opportunities).
- "VaR & Expected Shortfall Narrative" has the Insights lens, but it drafts a daily commentary in a standard format; the page's own Automation row names "the daily VaR narrative" (fix 058).
- "Sensitivity Limit Breach Escalation Pack": the problem says the desk head is notified, intent and solution say the trader (fixes 066, 069); "delays the start of the escalation window" (fix 068).
- "Limits Framework Calibration Review Support" names no reviewer or recipient; the OKR draft refers to "the annual limits review". Lens Enablement, while the same kind of card is Optimize on the area page and in Strategic Portfolio (fix 072, low).
- Small: "in the banking book" twice in the page intent (fix 055); two names for the validation team (fix 064); tab label (fix 057).

## Liquidity risk — `risk-control/liquidity-risk/index.html`

On it: page intent; one "Problems" tab ("Funding adequacy runoff", four rows); four sections; 12 cards (7 Insights, 4 Automation, 1 Enablement; 9 M, 3 S); 4 OKRs filled, 8 empty.

- 8 empty OKRs, all drafted (fixes 080–082, 084–087, 089).
- "LCR/NSFR Daily Ratio Narrative" describes daily NSFR ratios and a daily NSFR narrative. The page intent, the section intent above the card, and the next card all say the NSFR is monthly (fixes 077 and 079, high; 078 adjusts the existing OKR to match). The section sentence "Both ratios are calculated daily (LCR) and monthly (NSFR)" is itself awkward (fix 076).
- ILAAP cadence does not hold together across the page: the page intent says quarterly ILAAP updates are mandated; "Survival Horizon Scenario Refresh" says the ILAAP figure "may be six to twelve months old"; "ILAAP Behavioural Assumption Drift Monitor" speaks of an annual ILAAP review. The likely meaning is an annual submission with quarterly reviews, but that is a statement about the supervisory regime, so no fix proposed.
- Three cards in "Intraday liquidity monitoring" watch the same thing: late inflows from settlement counterparties. "Intraday Liquidity Position Watch" already "flags counterparty inflow delays above threshold", which is all that "Settlement Counterparty Behaviour Monitor" does. In "Funding runoff & concentration", "Funding Runoff & Concentration Watch" (weekly) and "ILAAP Behavioural Assumption Drift Monitor" (monthly) both compare deposit runoff with ILAAP assumptions. See Questions.
- "Wholesale Funding Maturity Cliff Watch": the problem says the cliff is visible two weeks ahead, the solution alerts three weeks ahead, and the horizon is 90 days (fix 088).
- "CFP Trigger Monitoring": after an alert at 20% distance "the Head of Treasury initiates the CFP pre-activation protocol", as if automatically (fix 083).
- "Intraday Peak Usage Trend Analysis" produces a "BCBS 248 intraday liquidity report" for submission; the section cites "BCBS 248 and CBR intraday liquidity guidelines" with no NBKR. Whether the LCR, NSFR, ILAAP and intraday reporting apply to the Bank in this form is for the owner.
- "broker deposit share" in the Insights problem row is a US notion.
- Small: missing article in the page intent (fix 074); tab label (fix 075).

## Operational risk — `risk-control/operational-risk/index.html`

On it: page intent; one "Problems" tab ("Loss events kris", four rows); four sections; 12 cards (5 Automation, 5 Insights, 2 Enablement; 9 M, 3 S); 4 OKRs filled, 8 empty.

- 8 empty OKRs, all drafted (fixes 093–096, 098, 101, 103, 104).
- "RCSA Facilitation Support", Adoption key result: "all three data sources" followed by four (fix 099, high).
- "Under Basel III Advanced Measurement Approach" is wrong as written: the AMA is a Basel II approach, the cards in the same section say "Basel II", and the area page speaks of "SMA calibration" (fix 092 corrects the reference only). Whether the page should describe AMA capital modelling at all is for the owner; "Operational Loss Event Data Quality Check" is built on "the AMA database".
- DORA is cited ten times as the governing rule (Articles 11 and 28). "DORA Third-Party Register Extraction" (filled) and "TPRM Exit Plan Currency Check" exist because of it. "NBKR Regulation No. 12" is cited for outsourcing; I could not verify the number.
- Three cards state no cadence: "Near-Miss Capture Programme Analysis", "TPRM Exit Plan Currency Check", "RTO/RPO Test Results Analysis". The OKR drafts set an illustrative one and say so in the note.
- "RTO/RPO Test Results Analysis" overlaps with "Resilience & Recovery Metrics Dashboard" on the cyber page: both compute RTO/RPO test trends by system for the CISO.
- Committee cadence: the Operational Risk Committee is quarterly in the problem rows and in two cards, but receives KRI reporting and a pattern digest monthly. Not a contradiction, but it reads loosely. Its name is lower-case in three places (fixes 097, 100, 102).
- "OpRisk Director" appears once; nowhere else is the role abbreviated or named (fix 090).
- Tab label (fix 091).

## Model risk — `risk-control/model-risk/index.html`

On it: page intent; one "Problems" tab ("Model lifecycle validation", four rows); four sections; 12 cards (6 Insights, 4 Automation, 2 Enablement; 9 M, 3 S); 3 OKRs filled, 9 empty.

- 9 empty OKRs, all drafted (fixes 106, 108, 110, 112, 113, 115, 116, 118, 119).
- Broken sentence in "Model Performance vs Macro Correlation Analysis": "while the macro environment deteriorating around it" (fix 114, high).
- The page rests entirely on SR 11-7 (US Federal Reserve and OCC; ten mentions) and EBA guidelines "for EU-regulated banks". The NBKR is not mentioned once. "Model Risk Regulatory Reporting Pack" assembles "the SR 11-7 and EBA model risk reporting pack for the supervisory review process", a submission that neither applies to the Bank nor is prescribed by SR 11-7. The role "Chief Model Risk Officer" appears in eleven of twelve cards, and the page assumes "80–200 models". See Questions.
- "Model Performance Monthly Dashboard" speaks of a monthly Model Risk Committee cycle; the other cards make the committee quarterly (fix 111).
- "Model Validation Finding Synthesis" (annual, for the Chief Model Risk Officer) and "Model Risk Portfolio Reporting" (quarterly committee pack, filled) both cluster validation findings by category and model family to find systemic patterns. The Risk Cycles page has a third one, "Validation Findings Thematic Synthesis".
- The "Model validation" section has no card that helps perform a validation, although the section intent says validation volume "often exceeds the capacity of the validation function". Its three cards draft the developer's specification, synthesise past findings, and plan capacity. "Model Development Specification Drafting" is a first-line development task filed under validation.
- "Shadow Model Identification Scan" is rated M, the same as report assembly, although it scans shared drives across all business units (fix 107, low). Three cards state no cadence; the OKR drafts set an illustrative one.
- Small: "coincides" stated as a rule (fix 109); "board risk committee" lower-case (fix 117); two names for one metric (fix 120); tab label (fix 105).

## Cyber risk — `risk-control/cyber-risk/index.html`

On it: page intent; one "Problems" tab ("Threat exposure detection", four rows); four sections; 12 cards (5 Insights, 5 Automation, 2 Enablement; 8 M, 4 S); 4 OKRs filled, 8 empty.

- 8 empty OKRs, all drafted (fixes 123–130).
- DORA is cited 29 times on this page and is the stated reason for three cards: "DORA Incident Notification Draft" (Article 19, four-hour window), "DORA TLPT Preparation Support" (Article 26), and the DORA checklist in "Cyber Incident Triage Pack" (filled). "Patch Compliance Status Report" measures against "DORA-required remediation timeframes" and its problem cites "DORA and CBR requirements" with no NBKR. The page intent cites "CBR Regulation No. 683-P". The last section ends "in the Central Asian and Russian supervisory context". See Questions.
- Threat sources named are "CERT-KZ, CERT-RU" — the Kazakh and Russian national CERTs (fix 122 proposes CERT-KG; the owner should confirm the name of the source the Bank uses).
- "Threat Intelligence Control Gap Analysis" states no cadence; the OKR draft sets an illustrative one.
- "Resilience & Recovery Metrics Dashboard" overlaps with "RTO/RPO Test Results Analysis" on the operational risk page.
- The section "Incident detection & response" has no card on detection; all three cards start after an alert is escalated.
- Tab label (fix 121).

## Special cases of the global patterns in this half

- Regulators other than NBKR and CBR are cited as binding and are not in the brief's list: DORA (EU) 40 times, SR 11-7 (US) 12 times, EBA 5 times, NBK/ARDFM (Kazakhstan) twice, BCBS 248 five times.
- CBR appears without NBKR in three places: intraday liquidity guidelines (liquidity), remediation timeframes (cyber, "Patch Compliance Status Report"), and "CBR Regulation No. 683-P" (cyber page intent).
- Regulation numbers attributed to the NBKR that I could not verify: "NBKR Regulation No. 16" (watchlist), "NBKR Regulation No. 12" (outsourcing). Thresholds attributed to the NBKR: 10% and 25% of Tier 1 for large exposures, LCR and NSFR minima of 100%, a 30-day survival horizon.
- Spelling is mixed inside single pages (market risk: "utilization" in the section and one card, "utilisation" in two cards). The OKR drafts follow the spelling of the card they belong to.
- A recurring small pattern, not fixed one by one: a dropped article before "trend" ("Trend in migration rates … is not directly visible", "to identify trend in peak usage", "with increasing recovery time trend").

## Questions for the owner

1. Overview counts. Should the area total include the cycles page (164 for Risk & Control) or keep the current rule (139), and should Risk Cycles be listed on the overview? Today the ten printed numbers add up to 134, the total says 139, and 164 cards exist.
2. Extract coverage. The page header intents (76 pages) and the "Problems" rows (48 pages) are not in the extract. Should the other reviewers' areas be re-read for these two fields before the fix round?
3. "Problems" tabs. On the area page only "Non-financial risks" has rows; on each sub-area page there is one tab named after the first of two groups while its rows describe the whole page. Options: (a) add the missing tabs — the four "Financial risks" rows are drafted, fixes 002–005, and Independent assurance would need four more; (b) keep one tab per page and rename it to the page. Which?
4. Group labels. May the slug-derived labels be replaced with written labels (fixes 006–023 and the tab labels)? Where the label did not describe its sections I proposed a new name rather than only restoring the ampersand ("Portfolio concentration & provisions", "P&L attribution & limits", "Third parties & continuity", "Threat & vulnerability exposure", "Model monitoring & reporting"). The other reviewer's pages carry the same tab labels.
5. Regulatory basis of this half. Which of these apply to the Bank, or should be kept as reference practice and worded that way: IRB models and an "IRB approval framework"; the Internal Models Approach for market risk with Basel backtesting and stressed VaR; AMA or SMA for operational risk capital; LCR, NSFR, ILAAP and BCBS 248 intraday reporting; DORA; SR 11-7 and EBA model risk guidelines. The answer decides the wording of the section intents on all six pages and the fate of the cards in question 6.
6. Cards that only make sense under another regime. Keep, re-base on NBKR and internal policy, or drop: "Regulatory Capital Efficiency Signal Detection" (area); "PD/LGD/EAD Monthly Output Narrative", "IRB Model Performance Signal Watch", "RWA & Capital Attribution Pack" (credit — could be re-based on the IFRS 9 models); "VaR Model Backtesting Pack", "Stressed VaR Scenario Narrative", "Backtesting Exception Documentation Pack", "Greeks Daily Position Report", "Sensitivity Risk-Factor Concentration Analysis" (market); "Intraday Peak Usage Trend Analysis" (liquidity); "Operational Loss Event Data Quality Check", "DORA Third-Party Register Extraction" (operational); "Model Risk Regulatory Reporting Pack" (model); "DORA Incident Notification Draft", "DORA TLPT Preparation Support" (cyber). I drafted OKRs for all of them as they stand.
7. Large-exposure thresholds. Which single-borrower and large-exposure limits should the credit risk page cite for the NBKR? The page now gives 10% and 25% of Tier 1.
8. NBKR references. Are "NBKR Regulation No. 16" (watchlist and classification) and "NBKR Regulation No. 12" (outsourcing) the right instruments? Is CERT-KG the right name for the national CERT feed (fix 122)?
9. Market risk scope. Does the Bank run a multi-desk trading book with options? If not, should the page be re-centred on the open FX position and IRRBB, which the page intent mentions and no card covers?
10. Roles. Does the Bank have, or want named in the catalog, a Chief Model Risk Officer, Chief Credit Officer, Market Risk Officer, Head of Treasury, CISO, TPRM lead and BCM lead? The OKR drafts use the roles the cards name.
11. Lens rule. What decides the lens? The same pattern carries different lenses: trigger-driven packs (Enablement in "Risk Appetite Breach Investigation Pack" and "Counterparty Exposure Breach Investigation Pack"; Automation in "Sensitivity Limit Breach Escalation Pack", "KRI Threshold Breach Alert & Pack", "Cyber Incident Triage Pack"); watches and alerts (Automation in "CFP Trigger Monitoring", "Settlement Counterparty Behaviour Monitor", "Wholesale Funding Maturity Cliff Watch"; Insights in "Intraday Liquidity Position Watch", "Model Risk Appetite Metric Watch"); calibration reviews (Optimize, Insights, Enablement). I proposed four lens changes where the evidence is on the page (fixes 036, 049, 058, 072); three of them wait on this answer.
12. Missing lenses. No card on the six sub-area pages has the "Optimize" or "New opps" lens, yet each page has a "New business opportunities" problem row, and on the market risk page three problem rows have no answering card. Add cards, or reword the rows?
13. Overlapping cards. Merge or sharpen: "VaR Model Backtesting Pack" and "Backtesting Exception Documentation Pack" (and move the first to the backtesting section); "Settlement Counterparty Behaviour Monitor" and "Intraday Liquidity Position Watch"; "Funding Runoff & Concentration Watch" and "ILAAP Behavioural Assumption Drift Monitor"; "Model Validation Finding Synthesis", "Model Risk Portfolio Reporting" and the Risk Cycles card "Validation Findings Thematic Synthesis"; "RTO/RPO Test Results Analysis" (operational) and "Resilience & Recovery Metrics Dashboard" (cyber); "IRB Model Performance Signal Watch" (credit) and the two performance cards on the model risk page.
14. Model validation section. Should it have a card that supports the validation work itself, and should "Model Development Specification Drafting" stay there?
15. Cadences. Nine cards state no cadence ("Counterparty Exposure Aggregation", "Concentration Limit Calibration Review", "Near-Miss Capture Programme Analysis", "TPRM Exit Plan Currency Check", "RTO/RPO Test Results Analysis", "Shadow Model Identification Scan", "Model Performance vs Macro Correlation Analysis", "Validation Pipeline Capacity Planning", "Threat Intelligence Control Gap Analysis"). The OKR drafts set illustrative ones and flag this in the note. Confirm or give the intended cadence.
16. ILAAP cadence. Annual submission with quarterly reviews? The liquidity page says three different things.
