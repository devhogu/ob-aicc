# Finance & Treasury — review notes

Reviewer id: `finance-treasury`. Source: `html-alt/financial-services/en/finance-treasury/` (10 pages, 126 cards). Fix map: `fixmap/finance-treasury.jsonl` (159 entries: 74 drafted OKRs, 85 other fixes — 3 high, 47 medium, 35 low).

## Summary

1. All 10 pages and all 126 cards were read: the area page (5 cards), eight sub-area pages (12 cards each, 96 in total) and the Finance Cycles page (5 cycles, 25 cards, 25 stage dialogs). No card lacks a title, intent, problem or solution, and no sentence is truncated inside a card.
2. 74 of the 96 sub-area cards have an empty OKR; all 74 are drafted in the fix map. The 22 filled sub-area cards are at most one per section, and they are the broader, older cards; the empty ones are narrower cards beside them. This is why most sections contain a card that overlaps its two neighbours.
3. The extract does not contain three kinds of text that are on the pages: the page header intent, the "problems" rows of each page, and the 25 stage dialogs of the cycles page (they sit in a script block). I read them from the HTML. Other reviewers working from the extract alone will have missed the same text in their areas.
4. The cycles page is complete (all 25 OKRs filled) and its cycle logic mostly holds, but it carries the densest set of errors: a wrong BCBS 368 principle number (four places), an IRRBB card that still carries the text of its liquidity twin (ILAAP), BCBS 368 cited in the liquidity cycle, a broken phrase in a stage dialog, "≥100%" targets, and a budget cycle length that contradicts the FP&A page.
5. Fit for O!Bank is weakest on two pages. Regulatory financial reporting is built around COREP, FINREP, the EBA and XBRL (36 mentions of COREP in the area). Tax management never names the Kyrgyz Republic: it cites Kazakhstan and Russia only, and assumes a multi-jurisdiction "Group Tax" function with intra-group transfer pricing.
6. Labels generated from slugs are broken on every page: sub-group labels on the area page and the problems tab label on each sub-area page ("Irrbb balance sheet hedging", "Ftp rate scenario reasoning", "Basel corep finrep"). This is the same across the catalog.
7. The overview page shows "Finance & Treasury (101)". The area holds 126 cards. The difference is the 25 cards of the Finance Cycles page, which the overview neither counts nor links. See "Counts" below.
8. English is generally sound. Clarity problems are local (about a dozen sentences); there is little inflated prose. Role names drift between pages (Controller, Controllers team, Financial Controller, close manager; Group Tax, Tax Operations; model risk team, model risk committee).

## Counts: overview against the area

- Overview (`extract/_root.md`): Finance & Treasury (101); eight sub-areas at (12) each, which sum to 96.
- Actually present: 5 cards on the area page + 8 × 12 = 96 on sub-area pages + 25 on Finance Cycles = 126.
- Explanation: 101 = 96 + the 5 area-level cards. The overview total therefore includes five cards that are not listed anywhere in its own breakdown (a reader adding the eight numbers gets 96, not 101), and it excludes the 25 cycle cards. The overview page has no link to any cycles page.
- The same convention holds for every area: the nine overview totals sum to 941, the cycles pages hold 160 cards, and 941 + 160 = 1,101, the catalog total. So this is one catalog-wide decision, not an error particular to this area.
- Counts shown on the area page itself are all correct: each sub-area (12), each section (3), Finance Cycles (25), each cycle (5).

## How to read the fix map

- `current` and `proposed` are plain text; in the HTML source `&` is `&amp;` and `'` is `&#39;`.
- For a card field, `proposed` is the whole new field and `current` is the first 200 characters of the old one. The note says which phrase changed.
- For long page elements (cycle descriptions, problem rows, section intents), `locator` names the element; where `current` is a single sentence, replace that sentence inside the element.
- For a filled OKR, `proposed` is the whole OKR object; parts not mentioned in the note are unchanged.
- Label fixes: the same string also appears in the `aria-label` of the tab input. The `id` and `for` attributes are slugs and should stay as they are.
- The BCBS 368 principle number (entries 141, 143, 145, 146) is corrected from my knowledge of the standard, where Principle 4 concerns economic value and earnings measures and Principle 5 concerns behavioural and modelling assumptions. Please check one against the text of the standard before applying all four.

## Area-specific forms of the global patterns

- Regulators are named in several different forms: "NBKR, NBK/ARDFM, and CBR" (55 uses of NBK/ARDFM in the area), "NBKR/NBK/CBR" (12, cycles page only), "NBKR/NBK", "NBKR/CBR", "NBKR and CBR", "NBKR, NBK, and CBR", and the section title "NBKR / NBK / CBR prudential returns". NBK/ARDFM (Kazakhstan) is not on the list of measured patterns but is the same case as CBR and should be decided with it.
- Several OKR targets are built on three supervisors, so removing CBR and NBK changes the target and not only the wording: cycles cards "Regulatory Reporting Quality Trend Analytics" ("all three supervisor perimeters"), "Supervisory Query Response Knowledge Base", and capital card "ICAAP Narrative Drafting" ("across NBKR, NBK/ARDFM, or CBR perimeters as applicable").
- "AOCI" (8 uses, capital and ALM pages and the area problem row) is a US GAAP term; under IFRS the item is other comprehensive income or the fair value reserve.
- "the relevant jurisdiction" and "by jurisdiction" are used on the liquidity page (2) and the tax page (24) as if the bank operated in several.

## Page by page

### Area page — `finance-treasury/index.html`

On it: header intent; one problems tab with four rows; eight sub-area cards with 16 sub-group labels and 32 section links; the Finance Cycles card; 5 area-level scenario cards (all with OKRs).

- The only problems tab is "Planning balance sheet steering". The second group on the page, "Accounting, reporting & tax" (three sub-areas), has no problem rows at all. Areas such as Strategic Banking Portfolio have one tab per group.
- 14 of 16 sub-group labels are humanised slugs with lost punctuation and acronym case (entries 079–092). "Transfer pricing indirect taxes" is also wrong in content: the group holds transfer pricing and FATCA / CRS, and no indirect-tax section exists.
- Problem row "Enablement" uses "a Fed pivot" as its example (entry 077).
- Card "Continuous CFO Financial Posture": "until both appear" has no antecedent (entry 075).
- Card "CFO Ad-Hoc Financial Q&A" is rated S while resting on the same cross-function live view as the M card beside it (entry 076). It also overlaps the FP&A card "CFO Scenario Sandbox" almost entirely.
- The area page orders the sub-areas FP&A, ALM, Finance Cycles, Capital, Liquidity, Performance; the overview orders them FP&A, Capital, Liquidity, ALM, Performance. Low priority.

### FP&A — `fpa/index.html`

On it: header intent; one problems tab ("Planning forecasting"); 4 sections × 3 cards; 4 OKRs filled, 8 empty (drafted, entries 001–008).

- Section "CFO & ALCO Q&A support" describes on-demand Q&A only, while two of its three cards are an ALCO pre-meeting briefing pack and a post-ALCO decision log (entry 098).
- "Budget Assumption Quality Scan": the intent promises a peer-benchmark comparison the solution does not make (entry 095).
- "In-Period Variance Flash": intent says mid-month and "trading data", solution says day 20 and intra-month feeds (entry 096).
- "Post-ALCO Decision & Action Log": "transcribes ALCO meeting minutes" (entry 097).
- "CFO Scenario Sandbox" is rated S (entry 099).
- "Rolling Forecast & Budget Narrative" sits in the "Annual budget cycle" section although its title, problem and Cycle key result are about the rolling forecast; the "Rolling forecast" section is the next one.
- The section "Budget-to-actual variance attribution" and its card "Budget-to-Actual Variance Attribution" are repeated on the Performance measurement page (section "Budget-to-actual variance & attribution", card "Segment Performance Variance Attribution"): same decomposition, same day-one delivery, same problem.
- The problems tab covers planning and forecasting only; the second sub-group (variance and decision support) has no rows. The same holds on every sub-area page.

### ALM — `alm/index.html`

On it: header intent; one problems tab ("Irrbb balance sheet hedging"); 4 sections × 3 cards; 3 filled, 9 empty (drafted, entries 009–017).

- "Rate Scenario Sensitivity Decomposition": the problem says the ALCO pack has no driver decomposition, which contradicts the section intent and the card "ALCO Rate-Scenario Pack" (entry 104); the solution ranks scenarios by "capital-consuming", which is not what NII sensitivity is (entry 103).
- "IRRBB Limit Utilisation Dashboard" is a monthly report in every field but the title (entry 102).
- "FTP-Driven Product Pricing Signals" is in the "NII & EVE sensitivity" section; it belongs with "FTP curve governance". Its Cycle key result speaks of "the monthly FTP curve update", while the section says the curve is approved quarterly.
- "NII & EVE Driver Decomposition" and "Rate Scenario Sensitivity Decomposition" are close: one attributes the month-on-month change, the other splits each scenario. They are distinct, but a reader will need the difference stated.
- Fit: the page intent and the hedge card assume an IR derivative hedge portfolio.

### Capital management — `capital-management/index.html`

On it: header intent; one problems tab; 4 sections × 3 cards; 3 filled, 9 empty (drafted, entries 018–026).

- "ICAAP Prior-Submission Delta Analysis": "for CFO and regulator review before filing" (entry 107).
- "Supervisory Communications Drafting": the list of the bank's responses includes "ad hoc data requests" (entries 108, 109).
- "ICAAP Narrative Drafting": the Acceptance key result names a Compliance team that the card does not mention (entry 111).
- "Dividend Policy Scenario Modelling": "adds the board's qualitative context" (entry 110).
- "CET1 Capital Headroom & Forward Projection" delivers "a weekly ALCO capital update" although the section says ALCO receives the position monthly. Acceptable as a between-meetings update; no fix proposed.
- Fit: "AT1 & Tier 2 Market Window Assessment" (secondary spreads, peer issuance, syndicate banks) and the buyback wording assume an issuer active in international capital markets.

### Liquidity management — `liquidity-management/index.html`

On it: header intent; one problems tab; 4 sections × 3 cards; 3 filled, 9 empty (drafted, entries 027–035).

- "CFP Annual Review Narrative": the problem contradicts itself on reuse of the prior submission (entry 113).
- "HQLA Stress Scenario Adequacy Check": the intent claims NSFR and concentration-limit checks that the solution does not perform (entry 114); "ALCO risk committee" (entry 115).
- "LCR & NSFR Driver Trend Analysis": "ALCO liquidity desk" (entry 116).
- "LCR Buffer Optimisation Signal" is about HQLA composition and yield and would sit more naturally in "HQLA portfolio & investment management" than in "Daily LCR & NSFR monitoring".
- "CFP Annual Review Narrative" and "Contingency Funding Plan Stress Analysis" both "produce the CFP narrative".
- Fit: the whole page speaks in LCR, NSFR and HQLA Level 1 / Level 2 terms as binding rules, although the cycles page itself says NBKR maintains its own liquidity ratios. "Wholesale Funding Maturity Ladder" lists medium-term notes and covered bonds.

### Performance measurement — `performance-measurement/index.html`

On it: header intent; one problems tab; 4 sections × 3 cards; 3 filled, 9 empty (drafted, entries 036–044).

- Section "Lending portfolio attribution & CECL / IFRS 9": CECL is the US GAAP model and no card uses it (entries 093, 117, 118).
- Section "RAROC & EVA attribution by BU" and the page intent say Basel II Pillar 2 "must" drive RAROC use (entries 119, 120).
- "RAROC & EVA Attribution by BU": the problem complains that attribution is only quarterly; the solution is still quarterly (entry 121).
- "Provision Sensitivity Scenario Analysis": recipients differ between intent and solution (entry 122).
- "Lending Portfolio Performance Attribution" (filled) already contains what the two cards beside it do: vintage cohort default tracking and provision sensitivities.
- "Segment Performance Variance Attribution" duplicates the FP&A card (see FP&A). Its URN slug ends in "-daily" although the card is monthly; "RAROC Hurdle Monitoring" has the slug "raroc-limit-breach-early-warning". URNs are identifiers and I propose no change, but the mismatch shows the cards were renamed.

### Accounting & financial close — `accounting-financial-close/index.html`

On it: header intent; one problems tab; 4 sections × 3 cards; 1 filled, 11 empty (drafted, entries 045–055).

- The one filled card, "Month-End Close Management", is three scenarios in one (task monitoring, GL-to-sub-ledger matching, close narrative drafting). Each is also a separate card or section on the same page ("Close Exception Escalation", the reconciliation section, "Close Narrative Drafting"). Its M rating is low for that scope.
- "Close Exception Escalation": "the daily end-of-close-day status report" (entry 124).
- "Close Narrative Peer Benchmarking Context": metric list differs between intent and solution (entry 125).
- Lens spread: 7 Automation, 4 Insights, 1 Enablement; no Optimize or New opps card on the page.

### Regulatory financial reporting — `regulatory-financial-reporting/index.html`

On it: header intent; one problems tab ("Basel corep finrep"); 4 sections × 3 cards; 2 filled, 10 empty (drafted, entries 056–065).

- Fit, most serious on this page: the page intent names the EBA as a supervisor ("and internationally the EBA through COREP and FINREP frameworks"), all four problem rows are about COREP/FINREP, and the first section (3 cards) is COREP/FINREP validation with the EBA XBRL suite. These three cards only make sense for a bank that reports to an EBA-aligned supervisor. I drafted their OKRs in the cards' own terms so they are complete either way.
- The section intent for prudential returns cites "NBKR Form 700 series" and "CBR Form 0409300 series". The NBKR form name needs checking by the Bank's reporting team (the same name is used in the Banking Data & Analytics area).
- "COREP / FINREP Data Quality Validation": "≥100%" in the Adoption key result (entry 127).
- "Earnings Release Drafting" carries the lens Insights; it is a drafting card (entry 128).
- "Regulatory Submission Narrative & Investor Disclosure Drafting" (filled, L) joins two scenarios: regulatory narrative, and investor disclosures. The second half belongs to the next section and overlaps "Earnings Release Drafting". It uses "MD&A", a US filing term.
- "COREP & FINREP Movement Commentary" and "Prudential Return Movement Insights" are the same scenario (top five movements, attributed, drafted) for two return families.
- "Regulatory Narrative Movement Threshold Coverage" states that the regulators "prescribe movement explanation thresholds". That is a claim about NBKR practice that I cannot verify.
- Lens spread: 8 Automation, 4 Insights.

### Tax management — `tax-management/index.html`

On it: header intent; one problems tab; 4 sections × 3 cards; 3 filled, 9 empty (drafted, entries 066–074).

- Fit, most serious on this page: the Kyrgyz Republic is not named once. The page intent speaks of "national tax authorities in Kazakhstan, Russia, and other operating jurisdictions"; the transfer pricing section says "Kazakhstan and Russian transfer pricing regulations require local files"; the FATCA / CRS section says "Kazakhstan and Russia are both CRS signatory jurisdictions". "Group Tax" (32 uses), "by jurisdiction" and "each in-scope entity" assume a multi-country group. The three transfer pricing cards only make sense for a group with intra-group transactions above a statutory threshold.
- The page intent promises "VAT and indirect tax compliance" and "corporate income tax filings", and two of the four problem rows are about corporate income tax returns. No section or card covers either.
- "FATCA / CRS Reporting Quality Check" (filled) is the sum of the two cards beside it ("FATCA & CRS XML Submission Validation" and "FATCA & CRS Account Classification Review"). It alone names "Tax Operations"; the other eleven cards name "Group Tax".
- "≥100%" in the Adoption key result of the same card (entry 130).
- "Effective Tax Rate Reconciliation": the last sentence of the problem does not explain the lateness it describes (entry 131).
- The section "Tax position in investor & rating agency disclosure" assumes rating agency presentations and investor calls.

### Finance Cycles — `finance-cycles/index.html`

On it: header intent; 5 cycles in two groups; each cycle has a summary, a three-paragraph description, four problem rows (Analyze, Optimize, Automate, Enrich), five stages with a dialog each (title, intent, problem), and 5 cards. All 25 OKRs are filled.

Cycle logic, cycle by cycle:

- Budget & forecast (Set assumptions → Plan → Build → Approve → Track & reforecast). The stage order is sound. The description says the cycle "opens six to eight weeks before the financial year end"; the FP&A page says it runs three to four months, and the stages' own durations do not fit six to eight weeks (entry 134). Cards attach to Set assumptions, Build, Approve and Track; the Plan stage (reconciling business-line submissions) has no card here. The lens labels of the first two cards are swapped relative to the other four cycles (entries 135, 136). The summary says actuals are "tracked quarterly", while the FP&A and Performance pages work with monthly variance attribution.
- ALM & balance-sheet steering (Measure → Analyse → Decide → Execute hedges → Monitor). The order is sound and cadences agree (monthly run, weekly monitoring, daily signal card). "BCBS 368 Principle 4" should be Principle 5 in four places (entries 141, 143, 145, 146). The card "BCBS 368 Behavioural Assumption Backtesting" was written from its liquidity twin and still says ILAAP in the problem, solution and OKR (entries 146–148). The description never mentions FTP although one card is the FTP brief (entry 142). The same scenario is S here and M on the ALM page (entry 144). Measure and Execute hedges have no card.
- Liquidity steering (Forecast → Stress → Plan → Report → Adjust). The order is doubtful: "Plan" documents "the ALCO steering decision", but the ALCO pack that informs that decision is produced in "Report", the stage after it. Forecast → Stress → Report → Plan → Adjust would match the ALM cycle (measure, analyse, decide, execute, monitor). The "Automate" row cites BCBS 368, the interest-rate standard (entry 150). The card "Daily LCR/NSFR Submission Exception Commentary" and the "Report" stage describe a daily LCR and NSFR submission to the supervisor; the Liquidity management page describes the daily report as internal to the Treasurer. Plan has no card.
- Financial close (Cut-off → Reconcile → Adjust → Close → Report). The order is sound. The description lists "IAS 32/39" beside IFRS 9 (entry 152). The "Report" dialog has a broken phrase, "within the close-plus business day target" (entry 153). The close is said to run "7-12 business days"; the FP&A page says the first P&L view comes "three to five business days into the following month". This is the only cycle without one card per lens: two Automation, no New opps. The text assumes a group ("inter-entity mismatches", "consolidation perimeter", "multiple legal entities").
- Regulatory reporting (Aggregate → Validate → Submit → Reconcile → Audit & respond). The order is sound. Three OKRs narrow their card to COREP/FINREP or use "≥100%" (entries 155, 156, 159). "BCBS 239 prescribed format" does not exist; the standard is a set of principles (entries 157, 158). The description says the bank "must demonstrate BCBS 239 risk data aggregation capability", which is written for systemically important banks.

Across the page:

- Each cycle description is one `<p>` holding three paragraphs; with the current stylesheet it renders as a single block of about 200 words (entry 133). This is likely the same on every cycles page in the catalog.
- Lens vocabularies differ: cycle problem rows use Analyze / Optimize / Automate / Enrich; sub-area problem rows use Insights & analytics / Enablement / Automation / New business opportunities; cards use Insights / Automation / Enablement / Optimize / New opps. The row "Analyze" and the stage label "Analyse" stand on the same page.
- Most cycle cards restate a card from a sub-area page under another title. Pairs: "Intra-Month IRRBB Position Signal" and ALM "IRRBB Early Warning Signal"; "ALCO IRRBB Pack Narrative Drafting" and ALM "ALCO Rate-Scenario Pack"; "Budget Assumption Calibration Library" and FP&A "Rolling Forecast Driver Insights"; "Budget Board Pack Narrative Drafting" and "Rolling Reforecast Model Compression" and FP&A "Rolling Forecast & Budget Narrative"; "Daily LCR/NSFR Submission Exception Commentary" and Liquidity "Daily LCR / NSFR Monitoring & Commentary"; "Close Reconciliation Exception Triage" and Close "GL Reconciliation Break Triage"; "Close Critical-Path Re-Sequencing" and Close "Close Critical Path Monitoring"; "Management Accounts Commentary Production" and Performance "Management Accounts Narrative" and Close "Close Narrative Drafting"; "Regulatory Submission Pre-Dispatch Quality Gate" and Reporting "COREP & FINREP Submission Readiness Check".
- "Rolling Reforecast Model Compression" reads as shrinking a model (entry 138).

## Questions for the owner

1. Overview count. Should "Finance & Treasury (101)" become (126), or should the overview list "Finance Cycles (25)" as a line of its own? Today the total includes five area-level cards that the breakdown does not show and leaves out the 25 cycle cards. The answer applies to all areas.
2. COREP / FINREP. The Bank reports to NBKR, not to an EBA-aligned supervisor. Should the COREP/FINREP section (3 cards), the problems tab and the page intent be re-pointed to NBKR prudential returns, kept as an international reference and marked so, or removed?
3. NBKR return names. Is "NBKR Form 700 series" the right name for the Bank's prudential returns? Do NBKR rules prescribe movement-explanation thresholds, as one card asserts?
4. Tax page. What applies to O!Bank: which transfer pricing documentation duty under Kyrgyz tax law, which FATCA and CRS status, and is there a "Group Tax" function or a tax unit within Finance? Should VAT and corporate income tax filings, promised in the page intent, get sections, or be removed from the intent?
5. Liquidity vocabulary. Should the liquidity page and cycle keep LCR / NSFR / HQLA Level 1–2 as the working terms, or use NBKR's liquidity norms? Is there a daily liquidity submission to NBKR, as the cycles page says, or only an internal daily report?
6. Instruments the Bank may not use. Interest-rate swaps, FRAs and hedge accounting (ALM page and cycle), AT1 and Tier 2 issuance through syndicate banks and share buybacks (capital page), medium-term notes and covered bonds (liquidity page), rating agency packs and earnings releases (tax and reporting pages). Keep as generic banking scenarios, or mark or remove what does not apply?
7. Budget and the supervisor. The budget cycle says annual budget approval "is required by NBKR, NBK/ARDFM, and CBR supervisory frameworks" and that a budget narrative is filed "in the prescribed NBKR/NBK/CBR format". Is there such a submission?
8. Duplicates. For the overlapping cards listed above (the umbrella card in each section, the two variance sections, the cycle cards that restate sub-area cards), should they be merged, differentiated in wording, or linked?
9. Card placement. Move "Rolling Forecast & Budget Narrative" to the Rolling forecast section, "FTP-Driven Product Pricing Signals" to FTP curve governance, "LCR Buffer Optimisation Signal" to the HQLA section, and split "Regulatory Submission Narrative & Investor Disclosure Drafting" between its two sections? Moving a card changes its URN.
10. Two facts stated differently on different pages: is the FTP curve updated monthly or approved quarterly, and does the monthly close take 3–5 or 7–12 business days?
11. Liquidity cycle stage order: accept Forecast → Stress → Report → Plan → Adjust?
12. Lenses. What does "Enablement" mean for a card? It is used here for drafting and assembly cards that elsewhere are Automation. Should the financial close cycle have one card per lens like the other four cycles? Should the three lens vocabularies be made one?
13. Problems tabs. Each page shows problem rows for its first sub-group only, and the area page has none for "Accounting, reporting & tax". Is one tab per page intended, or are the second tabs missing?
14. Single entity or group. The close cycle and the tax page assume several legal entities and a consolidation perimeter. Does this match the Bank?
