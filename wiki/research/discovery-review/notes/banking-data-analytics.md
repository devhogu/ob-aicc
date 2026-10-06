# Banking Data & Analytics — review notes

Reviewer id: `banking-data-analytics`. Source: `html-alt/financial-services/en/banking-data-analytics/` (9 pages, 134 cards). Fix map: `fixmap/banking-data-analytics.jsonl` (124 entries: 29 high, 57 medium, 38 low).

## Summary

- All 134 cards are complete: every card has an intent, a problem, a solution and a full OKR. No section is empty and every count shown on the area page matches the cards under it.
- The OKRs measure their own cards: I found no OKR that belongs to another scenario. In 12 cards one line of the OKR drifts from the card (wrong source, wrong cadence, a scope the card does not have, an objective that contradicts the key results), 4 cards have the impossible target "≥ 100%", and 5 have broken hyphens. The fix map has 33 OKR entries in all, the rest being jurisdiction and wording.
- The serious problem of this area is its origin: it was written for a banking group in Kazakhstan and Russia. It cites Kazakh and Russian law as the Bank's own (in 14 fields), Kazakh and Russian exchanges, currencies, benchmarks, card schemes and statistics agencies, and three supervisors. This goes beyond the known "CBR next to NBKR" pattern and is concentrated here (for example 11 of the catalog's 12 "KZ and RU markets", all 11 "KASE", all 12 "MOEX", all 11 "Law No. 94-V").
- Some of these are wrong in any country: KASE and MOEX are named as payment rails (they are stock exchanges), KazPost as a card scheme (it is a postal operator), and COREP/FINREP as part of the submission set (EU frameworks).
- Three places attribute specific forms and limits to the NBKR that look like Kazakh references relabelled ("NBKR Form 700", "NBKR Regulation No. 9 … 25% of Tier 1 capital", "NBKR AML/CFT Regulation No. 2"). I could not verify them and did not rewrite them; see Questions.
- BCBS 239 principles are numbered or named wrongly in six places, and inconsistently with the one place that is right.
- There are nine pairs or triples of near-duplicate cards, inside pages and between the sub-area pages and the cycles page. They need an owner decision and are listed under Questions.
- The extract for this area does not contain the page header intents, the "problems" rows or the stage dialogs of the cycles page. I read those from the source HTML.
- English is clean overall. Sound problems are few: five broken hyphens, one doubled apostrophe, one broken sentence, "continuous-form view", "ungapped".

## Counts on the overview page

The overview shows "Banking Data & Analytics (114)". The area actually holds 134 cards.

- The seven sub-area counts on the overview are all correct: 18 + 15 + 15 + 15 + 15 + 15 + 16 = 109.
- 114 = 109 sub-area cards + 5 cards that sit directly on the area page ("Data Quality Remediation Workflow" and four others). So the area total does not equal the sum of the lines printed under it; the reader cannot see where the extra 5 come from.
- The 20 cards of the Data Cycles page are not counted, and the Data Cycles page is not listed or linked on the overview at all. It is reachable only from the area page, where it is shown as "Data Cycles (20)".
- This is the rule for every area, not a slip here: in all eight areas with sub-pages the overview total equals sub-area cards plus area-page cards, without cycles. Whether cycles should be counted and listed is a single decision for the whole catalog (Question 8).

## Special case: the Kazakhstan and Russia corpus

What the fix map already corrects (safe without a decision): "KZ and RU markets" wording (8 fields), Kazakh and Russian personal data laws in the customer data page (6 fields, replaced by the Law of the Kyrgyz Republic on Personal Information), stock exchanges named as payment rails (3), KazPost and Mir as card schemes (7, replaced by Elcart), Russian and Kazakh statistics agencies (3), "three regulators / three perimeters" (2 cards).

What is left for one decision (not in the fix map, counts are occurrences in this area):

| Now in the text | Where | Count | Suggested direction |
|---|---|---|---|
| NBK/ARDFM, ARDFM (Kazakh supervisor) | regulatory data 15, data cycles 19, master data 1 | 35 | Same decision as the global CBR pattern; add ARDFM and NBK to it (202 occurrences in the catalog) |
| KASE, MOEX as price sources | market data | 17 | Name the Bank's real sources (Kyrgyz Stock Exchange, NBKR, vendors) or drop the names |
| KZT, RUB yield curves | market data, curve section and its 3 cards | 18 | KGS and USD, if the Bank builds curves at all |
| TONIA, MOSPRIME | market data, FX section and 2 cards | 8 | Benchmarks the Bank actually uses |
| Law No. 94-V, Federal Law No. 242-FZ (data localisation) | regulatory data, residency section and its 3 cards, page intent | 11 | See Question 3 |
| "NBKR (Kyrgyz Republic), NBK/ARDFM (Kazakhstan), and CBR (Russia) … banking groups with operations across multiple CIS jurisdictions" | data cycles, submission cycle | whole cycle | See Question 6 |

## Area page (`index.html`)

On it: header intent, one "problems" tab (Operational data, 4 rows), links to 8 pages in 14 sub-groups, 5 area-level cards (Automation S, Insights S, Insights M, New opps M, Enablement L).

- 13 of the 14 sub-group labels are raw slugs with the "&" or hyphen lost: "Lineage bcbs239", "Customer 360 identity", "Loan level exposure", "Pricing rates" and so on. This is catalog-wide (customer-channels has "Rm productivity", risk-control "Aml sanctions financial crime"); only strategic-portfolio has proper labels. The fix map gives the 13 corrected labels for this area and the same labels for the problems tabs of six sub-pages.
- Three sub-groups do not contain what their label says: "Transaction enrichment lineage" has no enrichment section (it is in the other group), "Collateral risk inputs" has no risk inputs (PD/LGD/EAD is in the other group), "Position limit data" has no positions (trading book positions is in the other group). The proposed labels describe the real content. Two more are loose fits: data quality governance and the data catalog sit under "Reference lookup data", and data residency sits under "Lineage bcbs239".
- The tiles are in a different order from the overview (master data, regulatory data, cycles, customer, transaction, market, credit, risk), so the group names "Operational data" and "Risk & regulatory data" repeat instead of forming two blocks.
- The problems panel has one tab, "Operational data". The other two groups (Risk & regulatory data, Data governance) have no problem rows. Same on every sub-page: one tab, named after the first sub-group only. This is the same on all 39 sub-area pages of the catalog.
- Card "Data Quality Remediation Workflow" is the same scenario as "CDE Remediation Workflow Routing" on the master data page, with different targets (routing within 1 business day here, within 1 hour there). Question 7.
- Card "Data Mesh Domain API Registry": Acceptance KR validates SLA summaries "against vendor telemetry"; the card has no vendor (fixed).
- Card "Data Quality Remediation Workflow": Cycle KR starts from "manual aggregation cycles"; the card is about routing (fixed).

## Master & reference data (6 sections, 18 cards)

- Jurisdiction: "KZ and RU markets" in the problems row, the golden record section and card "MDM Golden Record Deduplication"; card "Entity Hierarchy Validation" checks the hierarchy against "Kazakhstan and Russian business registries" (all fixed).
- "BCBS 239 Principle 2 (data accuracy and integrity)" in the governance section and in "Customer Master CDE Quality Monitor": accuracy and integrity is Principle 3 (fixed).
- "Entity Hierarchy Validation" treats FIBO as an external source of facts next to the company registry. FIBO is an ontology; it classifies relationships and cannot confirm them (fixed in intent, solution and KR).
- "Customer Master Onboarding Quality Check": "the onboarding agent" is a person, in a catalog where "Agent" is the AI (fixed); Acceptance KR is ungrammatical (fixed); S looks light for an inline check in every onboarding channel (proposed M).
- "CDE Governance Health Monitor": last sentence of the problem is copied from the area card on data quality scores and does not fit governance coverage (fixed). Its URN still says `data-quality-dimension-dashboard` (Question 9).
- "Catalog Lineage Completeness Check": "each ungapped asset" (fixed). The card overlaps with two lineage cards on the regulatory page and one on the cycles page (Question 7).
- "Reference Taxonomy Change Propagation": "field- level" (fixed).
- Small: team named two ways in "Account Master Product Linkage Integrity"; "within ≤ 2 weeks" (both fixed).
- The six sections alternate between the two sub-groups on the page, so the page order does not follow the area page.

## Customer data (5 sections, 15 cards)

- The page intent and the whole "Consent & privacy records" section (intent and all three cards) rest on Kazakhstan's Law No. 94-V and Russian federal law; the page intent cites 149-FZ and the section 152-FZ for the same thing. Replaced by the Law of the Kyrgyz Republic on Personal Information in six fields; the citation needs Legal confirmation.
- "KYC Risk Reclassification Trigger": the intent says the pack is "for the scheduled review" while the card exists to trigger an out-of-cycle one (fixed).
- "KYC Refresh Candidate Pack" has lens New opps; it is a dossier for an analyst, Enablement (fixed). Its intent also ends with "characteristic of KZ and RU market institutions — the model shifts…" (fixed).
- "NBKR AML/CFT Regulation No. 2 and CBR Regulation No. 375-P" is cited in the KYC section and three cards (Question 2).
- "Churn Propensity Signal": a calibrated churn model on the whole customer base is rated S (proposed M). It and "Cross-Sell Signal from 360 Profile" overlap in subject with the Customer & Market Intelligence area (Retention & churn, Wallet share); I did not compare card by card.
- "RM Relationship Brief Assembly" carries the URN `customer-360-profile-assembly`, which reads as the neighbouring card "Customer 360 On-Demand Assembly" (Question 9).

## Transaction data (5 sections, 15 cards)

- "Payment & transfer records" section and "Payment Data Completeness Monitoring" name KASE and MOEX as payment rails ("domestic KASE, MOEX", "SWIFT, KASE, and MOEX payment rails"). They are stock exchanges. Fixed with "domestic interbank payment systems".
- "Card & merchant data" section, "Chargeback Root Cause Analysis" and "Card Fraud Pattern Detection" name "KazPost, Mir" as local card schemes and count "four scheme data sources". Replaced with Elcart; please confirm the schemes the Bank processes (Question 1).
- "Enrichment Rule Maintenance and Drift Detection": the agent detects drift and does not maintain rules; title adjusted.
- "End-of-Day Reconciliation Narrative" and "Settlement Reconciliation Break Classification" both classify the same end-of-day breaks, one into a narrative for management, one into a work list for operations. Two outputs of one job (Question 7). The first still has the URN `reconciliation-break-investigation`.
- "AML Network Anomaly Detection" and "Chargeback Root Cause Analysis" are analysis cards with lens Automation. I left them: each section has three cards with three different lenses, and changing one breaks that spread.
- Small: a percentage "of product, marketing, and credit teams"; two annual review cycles "within the first 18 months" (both fixed).

## Market data (5 sections, 15 cards)

- This page is the most tied to Kazakhstan and Russia: KASE and MOEX as primary exchanges, Rosstat and the Statistics Committee of Kazakhstan, TONIA and MOSPRIME, KZT and RUB curves. "Macro Data Publication Tracker" lists "the NBK, the CBR" and never mentions the NBKR; "Macro Indicator Consistency Check" compares estimates "for Russia" and "for Kazakhstan". The statistics sources are fixed; exchanges, curves and benchmarks wait for Question 1.
- The page also assumes a trading bank: real-time feeds, inter-dealer brokers, volatility surfaces, VaR engine, margin calls, "a significant expense line for trading banks" (Question 4).
- "FX & benchmark rates" section: the administrators "(CBR, NBKR, ICE, EMMI)" do not match the benchmarks in the same sentence; SOFR is administered by the Federal Reserve Bank of New York (fixed).
- "IFRS 9 Macro Input Version Control": the agent "assesses whether a restatement is required"; that decision belongs to credit risk and finance (fixed).
- "Market Data Feed Quality Monitor" and "Vendor SLA Performance Dashboard" both produce a monthly SLA report per vendor from feed quality metrics, and "FX Rate Coverage Completeness Report" produces a third monthly aggregate for the same vendor reviews. The first card also borrows its examples ("a CBR rate published outside the expected window…") from "Benchmark Rate Anomaly Detection" (Question 7).
- Four cards are pre-consumption gates of the same kind (end-of-day prices, benchmark rates, feeds, curve inputs) with lenses Automation, Automation, Optimize and Enablement. Not wrong, but the lens does not follow from what the card does.
- "Yield Curve Construction Commentary" and "Interpolation Methodology Review Brief" both document the interpolation rationale every day.

## Credit & exposure data (5 sections, 15 cards)

- "Collateral Valuation Monitoring": the objective says "intraday market-index adjustments"; the card describes interim adjustments between appraisals, applied daily (fixed).
- "≥ 100%" in "ECL Provision Narrative" and "Credit Parameter Review Brief" (fixed).
- "Collateral Valuation Monitoring" and "Collateral LTV Covenant Watch" are one scenario with two recipients (credit risk team, relationship manager): same index-adjusted LTV, same covenant thresholds. One is Insights S, the other Enablement M (Question 7).
- The "Counterparty & group exposure" section and its three cards state "Under NBKR Regulation No. 9, a single counterparty or connected group may not represent more than 25% of Tier 1 capital", a 10% reporting threshold and a mandatory supervisory notification. These read like the Basel large-exposure standard (Question 2).
- The "Credit parameter inputs" section and its three cards assume IRB models approved by the supervisor, RWA from PD/LGD/EAD, Pillar 3, and a "quarterly model review agenda submitted to NBKR under model approval reporting requirements" (Question 4).
- "Connected-Party Group Mapping": FIBO listed as a data source in the intent (fixed); second half of the Cycle KR has no measure (fixed). It overlaps with "Entity Hierarchy Validation" (master data) and "Beneficial Ownership Structure Analysis" (customer data).
- "ECL Provision Narrative" (URN `exposure-aggregation-narrative`) contains the stage movement explanation that "ECL Stage Movement Analysis" produces separately.

## Risk & position data (5 sections, 15 cards)

- "≥ 100%" in "Stress Scenario Result Narrative" (fixed).
- "Limit Utilisation Trend Monitor": daily monitoring, weekly alert, and a promise of 5 business days of warning. A weekly alert can arrive after the breach; changed to a daily alert in intent, solution and KR.
- "Limit Hierarchy Coverage Check": the objective covers "the trading book and credit portfolio"; the card never mentions the credit portfolio (fixed).
- "Stress Scenario Result Narrative" and "Stress Result Board Summary" are near-duplicates: both a stress result narrative for the Risk Committee, with capital and liquidity impact, prior-cycle comparison and CRO review (Question 7). The first has the URN `risk-position-commentary`.
- Page intent promises "market, liquidity, and operational risk exposures"; there is nothing on operational risk. It ends with "without compressing analyst capacity", which says the opposite of what is meant (both fixed).
- "Limit Breach Escalation Draft" calls the window "regulatory" three times; the section and the problem say it is set by the bank's own framework (fixed).
- "Risk Metric Sense-Check": "false- positive", "end- of-day" (fixed).
- "Liquidity Posture Narrative" (URN `dynamic-operational-dashboards-alert-narratives`): intent omits intraday liquidity and promises an early-warning signal the solution does not produce (fixed).
- The page assumes trading desks, derivatives, Greeks, the Internal Models Approach and FRTB (Question 4). "LCR and NSFR are reported monthly" under "NBKR liquidity regulation and CBR Instruction No. 139" needs the same verification as Question 2.

## Regulatory data (5 sections, 16 cards)

- "Supervisory data submissions" has four cards where every other section in the area has three. The fourth, "Supervisory submission portfolio health", is from another hand: title in sentence case, "continuous-form view" twice, "COREP/FINREP" in the problem, "≥80%" without a space, one-line key results (all fixed). It overlaps with "Submission Deadline Management".
- "Regulatory Change Data Impact Assessment" and "Regulatory Change Data Gap Assessment" are the same card twice: both read the new form specification, map each field to the data catalog, list the gaps and hand the result to the programme. They differ in lens (Enablement, Automation) and in the target (5 business days, 3 business days). The first has the URN `regulatory-reporting-pack-assembly` (Question 7).
- "Data residency & localization controls": the section and its three cards exist because of Kazakhstan's Law No. 94-V and Russia's Federal Law No. 242-FZ ("personal data of KZ or RU citizens"). The scenario only makes sense under those laws as written (Question 3).
- "NBKR Form 700 (prudential returns), CBR Form 0409 (credit risk reporting), ARDFM capital adequacy returns" in the datasets section and two cards (Question 2). "Three regulators" and "all three regulatory perimeters" in two cards (fixed, to apply with the global regulator decision).
- "BCBS 239 Lineage Mapping" produces the map "for supervisory submission … in the format required"; no supervisor prescribes such a submission, and the section itself calls lineage examination evidence (fixed).
- Lineage section: "Principles 2 and 3 (data accuracy and completeness)" (fixed). The section says lineage documentation is "a supervisory examination requirement" for "systemically important banks under NBKR and CBR supervision" (Question 5).
- "Regulatory Dataset Lineage Record": the Acceptance KR holds a time target (≤ 1 hour) that contradicts the Cycle KR (≤ 1 business day) (fixed).
- "BCBS 239 Lineage Gap Detection": "each ungapped CDE" (fixed).

## Data Cycles (4 cycles, 20 cards)

What is on it: two groups, "Stewardship & quality" (three cycles) and "Submission & disclosure" (one cycle; nothing on disclosure). Each cycle has a summary line, a three-paragraph description, four problem rows (Analyze, Optimize, Automate, Enrich), five stages with a dialog each (title, intent, problem), and five cards, one per lens. The cards are attached to the cycle, not to a stage.

Cycle logic:

- Data quality assessment (monthly; Profile → Score → Issue → Remediate → Retest). Steps and anchor are coherent. No card serves Retest, although its dialog states a clear problem (retests are scheduled by hand and slip without escalation). "Issue" as a stage name reads as a verb; the dialog means issue identification and triage. Card "CDE Quality Trajectory Monitor" monitors "continuously between monthly assessments" by reading scores that the cycle produces monthly; it needs interim runs (fixed). Card "CDE Profiling and Scoring Automation" promises the full approved CDE inventory in the intent and objective, and "100% of onboarded CDEs" in the solution and KRs; the stated problem (60–70% coverage because onboarding needs engineering) is not solved by the card (fixed to the honest scope).
- Master & reference data stewardship (quarterly, monthly monitoring; Define → Govern → Curate → Validate → Publish). Coherent. The summary line lists four activities that are not the five stages ("reference data refresh" is not a stage). No card serves Define. The description promises "enriching incomplete master data records" and the Automate row "reference data refresh from authoritative external sources"; no card does either. The "Enrich" problem (decisions kept in minutes, not in a knowledge base) is answered by the Enablement card, while the New opps card is an impact map; in the other three cycles New opps is the knowledge-base card (lens swap proposed).
- Lineage & control attestation (semi-annual, change-triggered updates between; Map → Document → Test controls → Attest → Renew). Coherent. No card serves Test controls, although the summary, the Automate row and the stage dialog all name control testing, and the attestation pack card consumes "control test results" that nothing produces. Principles numbered wrongly (fixed).
- Regulatory data submission (monthly and quarterly; Aggregate → Validate → Submit → Reconcile → Resolve queries). Coherent as steps. The summary has no cycle anchor, unlike the other three (added). No card serves Submit (the dialog names portal outages, signature renewals and format mismatches). The cycle is written for a group reporting to three supervisors in three countries; card "Cross-Supervisor Exception Pattern Analysis" has no meaning with one supervisor (Question 6).

Other findings:

- "≥ 100%" in "Master Data Governance Decision Documentation" (fixed). Broken sentence "…and triage supervisory query response packs" (fixed). "institution''s" with a doubled apostrophe (fixed). "end-of- sprint", "business- readable" (fixed).
- "BCBS 239 quality dimension definitions" and "BCBS 239 root-cause classification" in the first two cards: BCBS 239 contains neither (fixed).
- "Golden Record Deduplication Assist" is the same card as "MDM Golden Record Deduplication" on the master data page (same problem text and solution) but rated S there M (aligned to M). "Reference Data Change Impact Map" is the same as "Reference Taxonomy Change Propagation" (New opps M here, Optimize S there) (Question 7).
- "Lineage Documentation Currency Dashboard" promises a "real-time" signal and updates weekly (fixed). "Attestation Findings Pattern Synthesis" replaces a review "that was not previously performed" (fixed). "Lineage Attestation Pack Drafting" refers to "the currency monitor" (fixed).
- The problem rows here are named Analyze, Optimize, Automate, Enrich; on the sub-area pages they are Insights & analytics, Enablement, Automation, New business opportunities; the cards use a third set (Insights, Automation, Enablement, Optimize, New opps). No page has a problem row for every lens its cards carry. Catalog-wide.

## Patterns in this area not worth single fixes

- Nine Acceptance KRs pair "≥ N% confirmed" with a false-positive ceiling that is not its complement (for example "≥ 85% confirmed … false-positive rate ≤ 12%"). Two targets for one measure; harmless, but one of them is redundant.
- Several Acceptance KRs carry a time target and several Cycle KRs carry no before → after, only the new cadence. I fixed only the ones that contradict the card.
- Eight cards have a URN that no longer matches the title (listed in Question 9).

## Questions for the owner

1. Jurisdiction. This area was written for Kazakhstan and Russia. The fix map replaces what has an obvious Kyrgyz equivalent. Please confirm three replacements (Law of the Kyrgyz Republic on Personal Information, No. 58 of 14 April 2008; Elcart as the national card scheme; "domestic interbank payment systems" for the NBKR-operated rails) and decide the rest of the table above: which exchanges, currencies, curves and benchmarks the market data page should name. Should NBK and ARDFM join the global CBR decision?
2. Three NBKR references look like Kazakh or Basel references under an NBKR label and need Compliance and Risk to supply the real ones: "NBKR Form 700 (prudential returns)" (Form 700 is, as far as I know, a National Bank of Kazakhstan form); "NBKR Regulation No. 9 … 25% of Tier 1 capital", the 10% reporting threshold and the mandatory notification; "NBKR AML/CFT Regulation No. 2"; also "LCR and NSFR are reported monthly" under NBKR liquidity regulation. What are the correct instruments and figures?
3. Data residency section (3 cards). It is built on Kazakh and Russian localisation law. Does the Bank want it reframed on Kyrgyz rules for cross-border transfer of personal data and NBKR requirements on where bank data is held, or removed?
4. Scale. The market data, risk & position and credit parameter content assumes a trading bank on advanced approaches: derivatives desks, Greeks, VaR by desk, Internal Models Approach, FRTB, IRB capital models, Pillar 3, volatility surfaces, inter-dealer brokers. Keep as a general banking catalogue, or cut to what O!Bank runs (FX position, securities portfolio, IFRS 9 models, standardised capital)?
5. BCBS 239 is cited 107 times in this area, mostly as a binding requirement ("supervisory examination requirement", "BCBS 239 findings", "systemically important banks under NBKR … supervision"). Is it binding on the Bank, or a reference standard? The wording should follow.
6. The regulatory data submission cycle describes "banking groups with operations across multiple CIS jurisdictions" and three supervisors. Rewrite it for one supervisor? If yes, should "Cross-Supervisor Exception Pattern Analysis" become a cross-form analysis (one root cause producing exceptions in several returns) or be dropped?
7. Near-duplicate cards: keep both, differentiate, or merge? (a) "Regulatory Change Data Impact Assessment" / "Regulatory Change Data Gap Assessment"; (b) "Stress Scenario Result Narrative" / "Stress Result Board Summary"; (c) "Collateral Valuation Monitoring" / "Collateral LTV Covenant Watch"; (d) "Market Data Feed Quality Monitor" / "Vendor SLA Performance Dashboard"; (e) "Data Quality Remediation Workflow" (area page) / "CDE Remediation Workflow Routing"; (f) "MDM Golden Record Deduplication" / "Golden Record Deduplication Assist" (cycles); (g) "Reference Taxonomy Change Propagation" / "Reference Data Change Impact Map" (cycles); (h) lineage gaps: "Catalog Lineage Completeness Check" / "BCBS 239 Lineage Gap Detection" / "Lineage Documentation Currency Dashboard" (cycles); (i) "End-of-Day Reconciliation Narrative" / "Settlement Reconciliation Break Classification". Are the repeats between sub-area pages and the cycles page intended?
8. Overview count: show 114 (as now, without the 20 cycle cards and with 5 area-page cards that no line explains) or 134, and should Data Cycles be listed on the overview? One rule for all areas.
9. Eight URNs no longer match their card titles. Rename the URNs, or are they referenced elsewhere and must stay? `…/data-quality-mdm-governance/data-quality-dimension-dashboard` (CDE Governance Health Monitor); `…/relationship-interaction-history/customer-360-profile-assembly` (RM Relationship Brief Assembly); `…/transaction-lineage-reconciliation/reconciliation-break-investigation` (End-of-Day Reconciliation Narrative); `…/ecl-provision-data/exposure-aggregation-narrative` (ECL Provision Narrative); `…/liquidity-funding-data/dynamic-operational-dashboards-alert-narratives` (Liquidity Posture Narrative); `…/stress-scenario-data/risk-position-commentary` (Stress Scenario Result Narrative); `…/regulatory-change-data-management/regulatory-reporting-pack-assembly` (Regulatory Change Data Impact Assessment); `…/data-quality-assessment-cycle/dq-continuous-posture-monitor` (CDE Quality Trajectory Monitor).
10. Four cycle stages have no card: Retest, Define, Test controls, Submit. Add a card for each, or accept the gaps?
11. Problem rows: every page shows one tab, for its first sub-group only, and no page has a row for every lens. Is one tab intended? Which of the three lens vocabularies is the standard?
12. Sub-group labels: I repaired 13 labels and renamed three to match their content. Would you rather move the sections (enrichment, PD/LGD/EAD inputs, trading book positions) into the groups whose names promise them?
