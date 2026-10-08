# Tax management

Tax management covers the Bank's current and deferred tax position under IFRS, corporate income tax filings with the tax authority, transfer pricing documentation for intra-group transactions, VAT and indirect tax compliance, and FATCA/CRS reporting obligations. The Group Tax function is accountable to the CFO and operates under applicable tax law (that of each jurisdiction, where the Bank operates in more than one jurisdiction), OECD BEPS Action Plan commitments adopted locally, and international information-exchange frameworks. **The GenAI opportunity is automated compliance documentation — ETR reconciliation, transfer pricing local files, and FATCA/CRS data quality validation — reducing reliance on external advisors for routine documentation and freeing Group Tax for judgment-intensive positions.**

## Problems

### Tax position & filings {#tax-position-filings}

| Lens | Problem |
| --- | --- |
| Insights & analytics | The effective tax rate (ETR) reconciliation — comparing the actual tax charge to the charge that would result from applying the statutory rate to pre-tax income — surfaces deferred tax movements, permanent differences, and jurisdiction-specific items that affect the income statement. The reconciliation is produced quarterly and reviewed by the audit committee, but the items driving ETR movement are often not identified until the reconciliation is assembled, leaving insufficient time for disclosure review. |
| Enablement | Tax teams at banks with multi-jurisdiction operations manage corporate income tax filings across several distinct tax regimes — each with its own tax calendar, deductibility rules, and filing format. The compliance calendar is dense, with quarterly estimated payments, annual return deadlines, and ad hoc transfer pricing inquiries from local tax authorities arriving concurrently with the financial close cycle. |
| Automation | Corporate income tax returns for each jurisdiction are prepared manually from the IFRS trial balance, adjusted for local tax deductibility rules, and filed in the jurisdiction-specific format. Deferred tax calculations are computed separately from the tax provision entries and reconciled to the balance sheet each period. The mechanical computation work is substantial and repeatable. |
| New business opportunities | A Group Tax function with automated ETR reconciliation and tax provision computation can respond faster to tax authority inquiries and close tax positions earlier in the audit cycle. Faster tax certainty reduces provisioning requirements for uncertain tax positions under IFRIC 23, with direct balance sheet impact. |

## Effective tax rate reconciliation {#etr-reconciliation}

The quarterly ETR reconciliation explains the gap between the statutory tax rate and the rate actually charged in the income statement — decomposing the difference into permanent differences, deferred tax movements, tax credits, and jurisdiction-specific items. It is a required IFRS disclosure, reviewed by the external auditor and the audit committee each quarter, and the primary tool for assessing whether the tax charge is directionally consistent with prior periods and expectations.

### ETR Trend & Driver Analysis

- URN: urn:financial-services:scenario:finance-treasury/tax-management/etr-reconciliation/etr-trend-and-driver-analysis
- Lens: Insights
- Complexity: S
- Intent: The AI agent analyzes the Bank's effective tax rate over the trailing eight quarters — decomposing the ETR into its permanent difference, deferred tax, tax credit, and jurisdiction components — and identifies the factors driving ETR volatility for the CFO's and audit committee's earnings quality assessment.
- Problem to solve: The quarterly ETR reconciliation reports the current-period ETR and its components but does not contextualize them within the trailing trend. Audit committee members and investors assess ETR volatility as an earnings quality signal, but the analytical framing of what is driving quarter-on-quarter ETR movements is produced informally rather than as a structured component of the ETR output.
- Solution: The AI agent reads the ETR reconciliation outputs for the trailing eight quarters. It constructs a time-series decomposition — tracking the permanent difference, deferred tax movement, tax credit, and jurisdiction component of the ETR across each period — and identifies the factors responsible for quarter-on-quarter ETR change. The analysis is presented alongside the current-period ETR reconciliation as a trend annex for the audit committee and CFO. Group Tax reviews the decomposition before it is included in the audit committee pack.
- OKR: The CFO and audit committee receive, alongside each quarterly ETR reconciliation, a trend annex that decomposes the ETR over the trailing eight quarters into permanent difference, deferred tax, tax credit, and jurisdiction components and identifies the drivers of quarter-on-quarter change.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced ETR trend annex included in ≥4 quarterly audit committee packs within year 1. |
| Acceptance | ≥85% of trend annexes approved by Group Tax without material restatement; component series reconcile to the quarterly ETR reconciliations in ≥98% of reviewed quarters. |
| Cycle | Trend annex available with the current-period ETR reconciliation, vs. informal framing of quarter-on-quarter ETR movements in the prior process. |

### Effective Tax Rate Reconciliation

- URN: urn:financial-services:scenario:finance-treasury/tax-management/etr-reconciliation/effective-tax-rate-reconciliation
- Lens: Automation
- Complexity: M
- Intent: The AI agent computes the quarterly ETR reconciliation from P&L and tax provision data, decomposes the rate movement against prior period and statutory rate, and surfaces items requiring discrete disclosure under IFRS.
- Problem to solve: The quarterly ETR reconciliation requires the Group Tax function to cross-reference pre-tax income by jurisdiction, current and deferred tax entries, and permanent and temporary differences each cycle. Disclosure items requiring explicit mention in the IFRS notes surface late, because they are identified only when the reconciliation is assembled shortly before the audit committee meeting.
- Solution: The AI agent reads the consolidated P&L by jurisdiction, current and deferred tax provision entries, and the statutory rate schedule per jurisdiction. It computes the ETR reconciliation, decomposes rate movement against prior quarter and statutory rate, flags items requiring discrete tax disclosure under IFRS, and delivers the reconciliation pack to Group Tax for review.
- OKR: The quarterly ETR reconciliation — decomposed against prior period and statutory rate by jurisdiction, with IFRS discrete disclosure items flagged — is available for Group Tax review from P&L and tax provision data each quarter-end.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced ETR reconciliation used for ≥4 quarterly close cycles within year 1; all material jurisdictions covered in each reconciliation. |
| Acceptance | ≥90% of ETR reconciliation outputs accepted by Group Tax without material restatement; IFRS discrete disclosure items flagged by the AI agent confirmed as requiring disclosure in ≥85% of cases on audit committee review. |
| Cycle | ETR reconciliation available for Group Tax review within 2 business days of quarter-end P&L close, vs. 5–7 days of manual cross-jurisdiction assembly in the prior process. |

### Deferred Tax Asset Recoverability Review

- URN: urn:financial-services:scenario:finance-treasury/tax-management/etr-reconciliation/deferred-tax-asset-recoverability-review
- Lens: Automation
- Complexity: M
- Intent: The AI agent assesses the recoverability of deferred tax assets against the approved three-year profit forecast each quarter, applies the IFRS-required probability threshold, and produces a DTA recoverability memo for the CFO and external auditor review.
- Problem to solve: Deferred tax assets are recognized only when it is probable that sufficient taxable profits will be available to utilize them. Each quarter, Group Tax is required to assess DTA recoverability against the forward profit forecast and document the assessment for the external auditor. The documentation is produced manually and reviewed by the auditor as a substantive audit area each reporting cycle, with queries about the probability assessment methodology generating audit correspondence under tight deadlines.
- Solution: The AI agent reads the current DTA balance by category, the approved three-year profit forecast from FP&A, and the tax rate assumptions for each jurisdiction. It applies the IFRS probability threshold framework — assessing which DTA categories are covered by the forecast horizon and which rely on projected reversals of temporary differences — and produces a structured recoverability memo covering each DTA category, the supporting profit evidence, and the IFRS assessment conclusion. Group Tax reviews and confirms the methodology; the auditor receives the memo at the start of the quarterly substantive review cycle.
- OKR: Group Tax receives each quarter a structured DTA recoverability memo — each DTA category, the supporting profit evidence from the approved three-year forecast, and the IFRS assessment conclusion — ready for the CFO and for the external auditor at the start of the substantive review cycle.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced DTA recoverability memo used for ≥4 quarterly reporting cycles within year 1; all DTA categories covered. |
| Acceptance | ≥85% of memos confirmed by Group Tax without material change to the assessment conclusion; auditor queries on the probability assessment methodology reduced by ≥40% vs. the pre-deployment baseline. |
| Cycle | Memo available at the start of the quarterly substantive review cycle, vs. manual documentation with audit correspondence under tight deadlines in the prior process. |

## Transfer pricing local file documentation {#transfer-pricing-documentation}

OECD BEPS Action 13 local files document each material intra-group transaction for the relevant tax authority — entity description, controlled transaction analysis, arm's-length comparables, and conclusions on pricing compliance. Transfer pricing regulations commonly require local files for transactions above statutory thresholds, with documentation available on request by the tax authority within a defined deadline.

### Transfer Pricing Threshold Monitoring

- URN: urn:financial-services:scenario:finance-treasury/tax-management/transfer-pricing-documentation/transfer-pricing-threshold-monitoring
- Lens: Insights
- Complexity: S
- Intent: The AI agent monitors intra-group transaction volumes against the statutory documentation thresholds of each jurisdiction in which the Bank operates, and alerts Group Tax when a transaction category approaches or crosses the threshold that triggers a local file obligation — enabling documentation preparation in advance of the fiscal year-end.
- Problem to solve: Transfer pricing local file obligations are triggered when intra-group transaction volumes exceed statutory thresholds set by each jurisdiction's tax authority. Group Tax tracks these thresholds manually against the annual intercompany transaction schedule. Transactions that approach the threshold mid-year are identified at the annual review rather than when the documentation obligation first becomes probable, leaving insufficient time for thorough local file preparation before the fiscal year closes.
- Solution: The AI agent reads the intercompany transaction register and the statutory documentation thresholds for each jurisdiction. It monitors the cumulative intra-group transaction volume for each controlled transaction category on a quarterly basis and issues an alert to Group Tax when any category reaches 75% of the applicable threshold. The alert includes the current volume, the threshold, the estimated quarter in which the threshold will be crossed at the current run rate, and the documentation requirements that will apply. Group Tax uses the alert to initiate local file scoping before the fiscal year closes.
- OKR: Group Tax receives an alert when the cumulative volume of any controlled transaction category reaches 75% of the applicable statutory documentation threshold — with the current volume, the estimated quarter of crossing, and the documentation requirements that will apply.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-run threshold monitoring completed for ≥4 quarters within year 1; all controlled transaction categories and jurisdictions in the intercompany transaction register covered. |
| Acceptance | ≥85% of alerts confirmed by Group Tax as accurate; local file scoping initiated before the fiscal year closes for 100% of categories that cross a threshold. |
| Cycle | Threshold approach flagged in the quarter it arises, vs. identified at the annual review in the prior process. |

### Transfer Pricing Arm's-Length Benchmarking

- URN: urn:financial-services:scenario:finance-treasury/tax-management/transfer-pricing-documentation/transfer-pricing-arm-length-benchmarking
- Lens: Automation
- Complexity: M
- Intent: The AI agent assembles the arm's-length benchmarking analysis for each material controlled transaction category — identifying comparable transactions or companies, computing interquartile ranges, and confirming whether the Bank's pricing falls within the arm's-length range — for inclusion in the OECD BEPS Action 13 local file.
- Problem to solve: The benchmarking analysis for each controlled transaction category in the transfer pricing local file is performed by Group Tax with external advisor support, using comparables databases. The analysis is treated as a standalone exercise each year rather than building on prior-year benchmarks, and external advisor fees for comparable search and analysis represent a significant portion of the transfer pricing compliance cost.
- Solution: The AI agent reads the prior-year benchmarking analysis for each transaction category and the current-year controlled transaction pricing. It constructs the updated benchmarking analysis — refreshing the comparable set for any transaction category where the prior year's comparables have become less reliable, computing updated interquartile ranges, and confirming whether the Bank's current pricing falls within the arm's-length range. Transactions outside the arm's-length range are flagged for Group Tax review and potential pricing adjustment. The output is formatted for direct inclusion in the local file documentation, with Group Tax providing the technical conclusions.
- OKR: Group Tax receives an updated arm's-length benchmarking analysis for each material controlled transaction category — refreshed comparables, updated interquartile ranges, and the position of the Bank's pricing within the range — formatted for inclusion in the local file.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced benchmarking analysis used for ≥80% of material controlled transaction categories in ≥1 annual transfer pricing cycle within year 1. |
| Acceptance | ≥80% of benchmarking analyses accepted by Group Tax without a new external comparable search; transactions flagged outside the arm's-length range confirmed in ≥90% of cases. |
| Cycle | Updated benchmarking available within 2 weeks of the current-year pricing data, vs. a standalone annual exercise with external advisor support in the prior process. |

### Transfer Pricing Local File Documentation

- URN: urn:financial-services:scenario:finance-treasury/tax-management/transfer-pricing-documentation/transfer-pricing-documentation-assistant
- Lens: Automation
- Complexity: L
- Intent: The AI agent drafts the annual transfer pricing local file for each in-scope entity from intra-group transaction data, benchmarking analysis, and prior-year documentation, reducing the external advisor dependency on routine documentation.
- Problem to solve: Under OECD BEPS Action 13 and local transfer pricing regulations, annual local file documentation is required for each entity with above-threshold intra-group transactions. Drafting is primarily outsourced to external advisors at significant cost per entity; Group Tax manages the process and reviews drafts.
- Solution: The AI agent reads intra-group transaction data by entity, the approved intercompany pricing policy, benchmarking databases where licensed, and the prior-year local file. It generates the local file structure — entity description, controlled transaction analysis, arm's-length benchmarking narrative, and conclusions — in the format required by the local tax authority. Group Tax reviews and signs off; external advisor involvement is limited to complex or novel transactions.
- OKR: The annual transfer pricing local file for each in-scope entity — covering entity description, controlled transaction analysis, arm's-length benchmarking narrative, and conclusions in the format required by the local tax authority — is drafted from intra-group transaction data and prior-year documentation, reducing external advisor dependency on routine documentation.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-drafted local file content used for ≥80% of in-scope entities in ≥1 annual transfer pricing cycle within year 1. |
| Acceptance | ≥80% of AI-drafted local file sections accepted by Group Tax without material rewrite; external advisor involvement limited to complex or novel transactions, representing ≤20% of in-scope entities by year 2. |
| Cycle | Local file draft for standard entities available for Group Tax review within 3 weeks of intra-group transaction data close, vs. 6–10 weeks of external advisor production in the prior process. |

## Tax position in investor & rating agency disclosure {#rating-agency-tax}

Investors and rating agencies assess the Bank's tax position as part of earnings quality review — examining ETR volatility, uncertain tax provisions under IFRIC 23, and the size of deferred tax assets relative to capital. Tax narrative in earnings releases, annual reports, and rating agency presentations requires technical accuracy and accessible explanation of complex tax positions.

### Tax Narrative for Rating Agency Pack

- URN: urn:financial-services:scenario:finance-treasury/tax-management/rating-agency-tax/tax-narrative-for-rating-agency-pack
- Lens: Automation
- Complexity: S
- Intent: The AI agent drafts the tax section of the annual rating agency presentation — covering ETR trajectory, deferred tax asset quality, uncertain tax position (IFRIC 23) provisions, and tax jurisdiction concentration — from the current year's tax data and prior rating agency correspondence.
- Problem to solve: Rating agency presentations include a tax section covering ETR, DTA quality, and uncertain tax positions. The section is drafted by Group Tax and the CFO's office from the year's tax data and the prior year's presentation as a style anchor. The drafting cycle begins after all other financial sections are assembled, compressing the review window for a section that receives significant analytical scrutiny from rating analysts.
- Solution: The AI agent reads the current year ETR reconciliation, DTA balance and recoverability assessment, IFRIC 23 uncertain tax provision register, and the prior year's rating agency presentation tax section. It drafts the tax section covering ETR trajectory with drivers, DTA quality and recoverability, IFRIC 23 position summary, and jurisdiction concentration. Group Tax reviews the draft for technical accuracy; the CFO's office adds framing context for the rating agency audience. The draft is available for inclusion in the presentation pack at the same time as the financial sections.
- OKR: Group Tax and the CFO's office receive a draft of the tax section of the annual rating agency presentation — ETR trajectory with drivers, DTA quality and recoverability, IFRIC 23 position summary, and jurisdiction concentration — at the same time as the financial sections.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-drafted tax section used for ≥1 annual rating agency presentation within year 1; all four topics covered. |
| Acceptance | ≥85% of the drafted section accepted by Group Tax for technical accuracy without material rewrite; figures reconcile to the ETR reconciliation, DTA recoverability assessment, and IFRIC 23 register in ≥98% of reviewed entries. |
| Cycle | Tax section draft available with the financial sections, vs. drafting started after all other sections are assembled in the prior process. |

### Tax Position Earnings Quality Insights

- URN: urn:financial-services:scenario:finance-treasury/tax-management/rating-agency-tax/tax-position-earnings-quality-insights
- Lens: Insights
- Complexity: S
- Intent: The AI agent produces a quarterly tax position earnings quality summary — assessing ETR sustainability, DTA utilization trajectory, and IFRIC 23 provision adequacy against the Bank's forward profit forecast — structured for the CFO's and audit committee's earnings quality review.
- Problem to solve: Rating agencies and investors assess the Bank's tax position as part of their earnings quality review, but the Bank's internal quarterly close process does not produce a systematic earnings quality view of the tax position. ETR volatility analysis, DTA utilization pace, and IFRIC 23 provision adequacy are addressed separately in the ETR reconciliation and DTA assessment rather than synthesized into a single earnings quality assessment.
- Solution: The AI agent reads the quarterly ETR reconciliation, DTA balance and prior-quarter utilization, IFRIC 23 uncertain provision register, and the approved forward profit forecast. It produces a structured earnings quality summary covering three questions: whether the current ETR is sustainable given the mix of permanent differences and deferred items, whether the DTA utilization pace is consistent with the forward forecast, and whether the IFRIC 23 provision is directionally adequate given open tax authority inquiries. Group Tax reviews the summary before it is included in the CFO and audit committee pack.
- OKR: The CFO and audit committee receive a quarterly earnings quality summary of the tax position — ETR sustainability, DTA utilization pace against the forward profit forecast, and IFRIC 23 provision adequacy — reviewed by Group Tax.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced earnings quality summary included in ≥4 quarterly CFO and audit committee packs within year 1; all three questions addressed in each summary. |
| Acceptance | ≥85% of summaries approved by Group Tax without material change to the assessment; inputs reconcile to the ETR reconciliation, DTA balance, and IFRIC 23 register in ≥98% of reviewed quarters. |
| Cycle | Synthesized earnings quality view of the tax position available each quarter, vs. separate ETR and DTA outputs with no single assessment in the prior process. |

### Tax Disclosure Peer Benchmarking

- URN: urn:financial-services:scenario:finance-treasury/tax-management/rating-agency-tax/tax-disclosure-peer-benchmarking
- Lens: Enablement
- Complexity: S
- Intent: The AI agent compares the Bank's disclosed ETR, DTA-to-capital ratio, and IFRIC 23 provision level against peer bank disclosures from the most recent annual reports, and produces a benchmarking summary for Group Tax and IR to assess the Bank's disclosure positioning.
- Problem to solve: Investors and rating agencies benchmark the Bank's tax position against peers. Group Tax and IR assess this benchmarking informally by reading peer annual reports, without a structured comparison of the key tax metrics. The absence of a systematic benchmarking review means that material deviations in the Bank's tax metrics from the peer range — which may attract rating analyst scrutiny or investor questions — are not identified before the rating agency meeting or investor call.
- Solution: The AI agent reads the Bank's current disclosed ETR, DTA balance as a percentage of Tier 1 capital, and IFRIC 23 uncertain provision level. It reads the equivalent disclosures from the most recent annual reports of a defined peer set and computes the peer range for each metric. The benchmarking summary presents the Bank's position relative to the peer range, with any metric outside the peer band flagged for Group Tax and IR discussion. Group Tax and the CFO's office use the summary to prepare responses to expected rating analyst and investor questions on the Bank's tax position.
- OKR: Group Tax and IR receive a benchmarking summary that places the Bank's disclosed ETR, DTA-to-Tier 1 capital ratio, and IFRIC 23 provision level against the range of a defined peer set, with any metric outside the peer band flagged for discussion.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced benchmarking summary prepared for ≥1 annual reporting cycle within year 1; all three metrics and the full defined peer set covered. |
| Acceptance | ≥85% of peer figures confirmed against the published annual reports on Group Tax review; ≥75% of out-of-band flags used by Group Tax and the CFO's office to prepare responses to rating analyst and investor questions. |
| Cycle | Benchmarking summary available before the rating agency meeting or investor call, vs. informal reading of peer annual reports in the prior process. |

## FATCA / CRS reporting compliance {#fatca-crs-reporting}

Annual FATCA (US Foreign Account Tax Compliance Act) and CRS (OECD Common Reporting Standard) reporting requires the Bank to identify reportable account holders, validate their tax residency and classification, and submit XML-formatted account data to the local tax authority for onward exchange with partner jurisdictions. CRS applies in jurisdictions that have adopted the standard; FATCA obligations apply to any bank with US-connected customers or correspondent relationships.

### FATCA & CRS XML Submission Validation

- URN: urn:financial-services:scenario:finance-treasury/tax-management/fatca-crs-reporting/fatca-crs-xml-submission-validation
- Lens: Automation
- Complexity: S
- Intent: Before the annual FATCA and CRS XML files are submitted to the local tax authority, the AI agent validates the file structure, TIN format compliance, account balance population, and completeness against the reportable account population — producing a pre-submission validation report for Group Tax sign-off.
- Problem to solve: FATCA and CRS XML submissions are generated from the Bank's reporting system and submitted to the local tax authority without a comprehensive pre-submission validation. Submission errors — malformed XML, missing TINs for reportable accounts, account balances that differ from the authoritative source — are identified by the tax authority's processing system after submission and require corrective re-submissions with regulatory scrutiny.
- Solution: The AI agent reads the generated XML file and validates it against the FATCA and CRS XML schema and the Bank's authoritative reportable account population. It checks XML schema compliance, TIN format validity by jurisdiction, account balance consistency with the financial system, and completeness against the expected reportable account count. The pre-submission validation report presents each check as pass or fail, with failed items identified to the responsible data owner for correction before submission. Group Tax signs off the validation report before the file is dispatched to the tax authority.
- OKR: Group Tax receives, before the annual FATCA and CRS XML files are dispatched, a pre-submission validation report with pass/fail results for XML schema compliance, TIN format validity, account balance consistency, and completeness against the reportable account population.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced validation report used for 100% of annual FATCA and CRS XML submissions within year 1; all four check categories covered. |
| Acceptance | ≥95% of failed items corrected by the responsible data owner before submission; no corrective re-submission required for an error covered by the checks. |
| Cycle | Validation report available within 1 business day of XML file generation, vs. errors identified by the tax authority's processing system after submission in the prior process. |

### FATCA / CRS Reporting Quality Check

- URN: urn:financial-services:scenario:finance-treasury/tax-management/fatca-crs-reporting/fatca-crs-reporting-quality-check
- Lens: Automation
- Complexity: M
- Intent: The AI agent validates FATCA and CRS account population, classification, and XML report data against schema rules and prior-year benchmarks before the annual submission window.
- Problem to solve: Annual FATCA and CRS submissions require the Bank to validate account classification, due diligence completeness, and XML schema compliance across thousands of reportable accounts. Data quality issues discovered after submission trigger amended returns and heightened regulator scrutiny.
- Solution: The AI agent reads the account population extract, due diligence records, and classification decisions. It validates each record against FATCA/CRS classification rules, checks XML schema compliance, and compares the reportable population to the prior year with materiality-ranked exceptions. Tax Operations receives a structured exception report with remediation guidance and remediates the flagged items before the submission window closes.
- OKR: FATCA and CRS account population, classification, and XML report data are validated against schema rules and prior-year benchmarks before the annual submission window, with a structured exception report and remediation guidance delivered to Tax Operations.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced FATCA/CRS quality validation used for 100% of annual submission cycles within year 1; all material account classifications and XML schema requirements covered. |
| Acceptance | ≥90% of flagged exception items remediated by Tax Operations before the submission window closes; post-submission amended return rate attributable to classification or schema errors reduced by ≥50% vs. pre-deployment baseline. |
| Cycle | FATCA/CRS exception report available to Tax Operations within 5 business days of account population extract, vs. 2–3 weeks of manual review in the prior process. |

### FATCA & CRS Account Classification Review

- URN: urn:financial-services:scenario:finance-treasury/tax-management/fatca-crs-reporting/fatca-crs-account-classification-review
- Lens: Insights
- Complexity: M
- Intent: The AI agent analyzes the Bank's FATCA and CRS reportable account population for classification consistency — identifying accounts where the tax residency, entity type, or reportable status classification is inconsistent with the information held in the customer data system or with OECD CRS guidance.
- Problem to solve: FATCA and CRS account classifications are assigned during onboarding and updated through periodic review. Classification inconsistencies — accounts classified as non-reportable where the customer data indicates US indicia, or entity accounts where the controlling person classification conflicts with the KYC documentation — accumulate between review cycles and create regulatory exposure in the annual reporting submission.
- Solution: The AI agent reads the FATCA/CRS classification file and the corresponding customer data records — tax identification numbers, declared tax residencies, entity legal form, and controlling person records. It applies the FATCA IGA and OECD CRS consistency rules, flags accounts where the classification is inconsistent with the customer data or where the classification cannot be traced to a completed self-certification, and produces a ranked exception list for Group Tax and Compliance review. The teams resolve each exception before the annual XML submission is prepared.
- OKR: Group Tax and Compliance receive a ranked exception list of accounts whose FATCA or CRS classification is inconsistent with the customer data or cannot be traced to a completed self-certification, and resolve each exception before the annual XML submission is prepared.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced classification review run on the full FATCA/CRS classification file for ≥1 annual reporting cycle within year 1. |
| Acceptance | ≥80% of flagged accounts confirmed by Group Tax and Compliance as genuine inconsistencies; 100% of confirmed exceptions resolved before the XML submission is prepared. |
| Cycle | Classification exceptions identified ≥4 weeks before the annual submission window, vs. inconsistencies accumulating between periodic review cycles in the prior process. |
