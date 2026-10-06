# 

source: html-alt/financial-services/en/finance-treasury/tax-management/index.html


[PAGE TEXT]
Effective tax rate reconciliation
The quarterly ETR reconciliation explains the gap between the statutory tax rate and the rate actually charged in the income statement — decomposing the difference into permanent differences, deferred tax movements, tax credits, and jurisdiction-specific items. It is a required IFRS disclosure, reviewed by the external auditor and the audit committee each quarter, and the primary tool for assessing whether the tax charge is directionally consistent with prior periods and expectations.
Lens
Scenario
Intent
Complexity

### CARD 1 [Insights|S] ETR Trend & Driver Analysis
urn: urn:financial-services:scenario:finance-treasury/tax-management/etr-reconciliation/etr-trend-and-driver-analysis
intent: Agent analyses the bank's effective tax rate over the trailing eight quarters — decomposing the ETR into its permanent difference, deferred tax, and jurisdiction components — and identifies the factors driving ETR volatility for the CFO's and audit committee's earnings quality assessment.
Problem to solve: The quarterly ETR reconciliation reports the current-period ETR and its components but does not contextualise them within the trailing trend. Audit committee members and investors assess ETR volatility as an earnings quality signal, but the analytical framing of what is driving quarter-on-quarter ETR movements is produced informally rather than as a structured component of the ETR output.
Solution: Agent reads the ETR reconciliation outputs for the trailing eight quarters. It constructs a time-series decomposition — tracking the permanent difference, deferred tax movement, tax credit, and jurisdiction component of the ETR across each period — and identifies the factors responsible for quarter-on-quarter ETR change. The analysis is presented alongside the current-period ETR reconciliation as a trend annex for the audit committee and CFO. Group Tax reviews the decomposition before it is included in the audit committee pack.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 2 [Automation|M] Effective Tax Rate Reconciliation
urn: urn:financial-services:scenario:finance-treasury/tax-management/etr-reconciliation/effective-tax-rate-reconciliation
intent: Agent computes the quarterly ETR reconciliation from P&L and tax provision data, decomposes the rate movement against prior period and statutory rate, and surfaces items requiring discrete disclosure under IFRS.
Problem to solve: The quarterly ETR reconciliation requires the Group Tax function to cross-reference pre-tax income by jurisdiction, current and deferred tax entries, and permanent and temporary differences each cycle. Disclosure items requiring explicit mention in the IFRS notes surface late if the reconciliation is reviewed only after the audit committee meeting.
Solution: Agent reads the consolidated P&L by jurisdiction, current and deferred tax provision entries, and the statutory rate schedule per jurisdiction. It computes the ETR reconciliation, decomposes rate movement against prior quarter and statutory rate, flags items requiring discrete tax disclosure under IFRS, and delivers the reconciliation pack to Group Tax for review.
OKR objective: The quarterly ETR reconciliation — decomposed against prior period and statutory rate by jurisdiction, with IFRS discrete disclosure items flagged — is available for Group Tax review from P&L and tax provision data each quarter-end.
OKR KR [Adoption]: Agent-produced ETR reconciliation used for ≥4 quarterly close cycles within year 1; all material jurisdictions covered in each reconciliation.
OKR KR [Acceptance]: ≥90% of ETR reconciliation outputs accepted by Group Tax without material restatement; IFRS discrete disclosure items flagged by the agent confirmed as requiring disclosure in ≥85% of cases on Audit Committee review.
OKR KR [Cycle]: ETR reconciliation available for Group Tax review within 2 business days of quarter-end P&L close, vs. 5–7 days of manual cross-jurisdiction assembly in the prior process.

### CARD 3 [Automation|M] Deferred Tax Asset Recoverability Review
urn: urn:financial-services:scenario:finance-treasury/tax-management/etr-reconciliation/deferred-tax-asset-recoverability-review
intent: Agent assesses the recoverability of deferred tax assets against the approved three-year profit forecast each quarter, applies the IFRS-required probability threshold, and produces a DTA recoverability memo for the CFO and external auditor review.
Problem to solve: Deferred tax assets are recognised only when it is probable that sufficient taxable profits will be available to utilise them. Each quarter, Group Tax is required to assess DTA recoverability against the forward profit forecast and document the assessment for the external auditor. The documentation is produced manually and reviewed by the auditor as a substantive audit area each reporting cycle, with queries about the probability assessment methodology generating audit correspondence under tight deadlines.
Solution: Agent reads the current DTA balance by category, the approved three-year profit forecast from FP&A, and the tax rate assumptions for each jurisdiction. It applies the IFRS probability threshold framework — assessing which DTA categories are covered by the forecast horizon and which rely on projected reversals of temporary differences — and produces a structured recoverability memo covering each DTA category, the supporting profit evidence, and the IFRS assessment conclusion. Group Tax reviews and confirms the methodology; the auditor receives the memo at the start of the quarterly substantive review cycle.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
Transfer pricing local file documentation
OECD BEPS Action 13 local files document each material intra-group transaction for the relevant tax authority — entity description, controlled transaction analysis, arm's-length comparables, and conclusions on pricing compliance. Kazakhstan and Russian transfer pricing regulations require local files for transactions above statutory thresholds, with documentation available on request by the tax authority within a defined deadline.
Lens
Scenario
Intent
Complexity

### CARD 4 [Insights|S] Transfer Pricing Threshold Monitoring
urn: urn:financial-services:scenario:finance-treasury/tax-management/transfer-pricing-documentation/transfer-pricing-threshold-monitoring
intent: Agent monitors intra-group transaction volumes against the statutory documentation thresholds in Kazakhstan, Russia, and other operating jurisdictions, and alerts Group Tax when a transaction category approaches or crosses the threshold that triggers a local file obligation — enabling documentation preparation in advance of the fiscal year-end.
Problem to solve: Transfer pricing local file obligations are triggered when intra-group transaction volumes exceed statutory thresholds set by each jurisdiction's tax authority. Group Tax tracks these thresholds manually against the annual intercompany transaction schedule. Transactions that approach the threshold mid-year are identified at the annual review rather than when the documentation obligation first becomes probable, leaving insufficient time for thorough local file preparation before the fiscal year closes.
Solution: Agent reads the intercompany transaction register and the statutory documentation thresholds for each jurisdiction. It monitors the cumulative intra-group transaction volume for each controlled transaction category on a quarterly basis and issues an alert to Group Tax when any category reaches 75% of the applicable threshold. The alert includes the current volume, the threshold, the estimated quarter in which the threshold will be crossed at the current run rate, and the documentation requirements that will apply. Group Tax uses the alert to initiate local file scoping before the fiscal year closes.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 5 [Automation|M] Transfer Pricing Arm's-Length Benchmarking
urn: urn:financial-services:scenario:finance-treasury/tax-management/transfer-pricing-documentation/transfer-pricing-arm-length-benchmarking
intent: Agent assembles the arm's-length benchmarking analysis for each material controlled transaction category — identifying comparable transactions or companies, computing interquartile ranges, and confirming that the bank's pricing falls within the arm's-length range — for inclusion in the OECD BEPS Action 13 local file.
Problem to solve: The benchmarking analysis for each controlled transaction category in the transfer pricing local file is performed by Group Tax with external advisor support, using comparables databases. The analysis is treated as a standalone exercise each year rather than building on prior-year benchmarks, and external advisor fees for comparable search and analysis represent a significant portion of the transfer pricing compliance cost.
Solution: Agent reads the prior-year benchmarking analysis for each transaction category and the current-year controlled transaction pricing. It constructs the updated benchmarking analysis — refreshing the comparable set for any transaction category where the prior year's comparables have become less reliable, computing updated interquartile ranges, and confirming whether the bank's current pricing falls within the arm's-length range. Transactions outside the arm's-length range are flagged for Group Tax review and potential pricing adjustment. The output is formatted for direct inclusion in the local file documentation, with Group Tax providing the technical conclusions.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 6 [Automation|L] Transfer Pricing Local File Documentation
urn: urn:financial-services:scenario:finance-treasury/tax-management/transfer-pricing-documentation/transfer-pricing-documentation-assistant
intent: Agent drafts the annual transfer pricing local file for each in-scope entity from intra-group transaction data, benchmarking analysis, and prior-year documentation, reducing the external advisor dependency on routine documentation.
Problem to solve: OECD BEPS Action 13 and local transfer pricing regulations in Kazakhstan and Russia require annual local file documentation for each entity with above-threshold intra-group transactions. Drafting is primarily outsourced to external advisors at significant cost per entity; the Group Tax team manages the process and reviews drafts.
Solution: Agent reads intra-group transaction data by entity, the approved intercompany pricing policy, benchmarking databases where licensed, and the prior-year local file. It generates the local file structure — entity description, controlled transaction analysis, arm's-length benchmarking narrative, and conclusions — in the format required by the local tax authority. Group Tax reviews and signs off; external advisor involvement is limited to complex or novel transactions.
OKR objective: The annual transfer pricing local file for each in-scope entity — covering entity description, controlled transaction analysis, arm's-length benchmarking narrative, and conclusions in the format required by the local tax authority — is drafted from intra-group transaction data and prior-year documentation, reducing external advisor dependency on routine documentation.
OKR KR [Adoption]: Agent used to draft local file content for ≥80% of in-scope entities in ≥1 annual transfer pricing cycle within year 1.
OKR KR [Acceptance]: ≥80% of agent-drafted local file sections accepted by Group Tax without material rewrite; external advisor involvement limited to complex or novel transactions, representing ≤20% of in-scope entities by year 2.
OKR KR [Cycle]: Local file draft for standard entities available for Group Tax review within 3 weeks of intra-group transaction data close, vs. 6–10 weeks of external advisor production in the prior process.

[PAGE TEXT]
Tax position in investor & rating agency disclosure
Investors and rating agencies assess the bank's tax position as part of earnings quality review — examining ETR volatility, uncertain tax provisions under IFRIC 23, and the size of deferred tax assets relative to capital. Tax narrative in earnings releases, annual reports, and rating agency presentations requires technical accuracy and accessible explanation of complex tax positions.
Lens
Scenario
Intent
Complexity

### CARD 7 [Automation|S] Tax Narrative for Rating Agency Pack
urn: urn:financial-services:scenario:finance-treasury/tax-management/rating-agency-tax/tax-narrative-for-rating-agency-pack
intent: Agent drafts the tax section of the annual rating agency presentation — covering ETR trajectory, deferred tax asset quality, uncertain tax position (IFRIC 23) provisions, and tax jurisdiction concentration — from the current year's tax data and prior rating agency correspondence.
Problem to solve: Rating agency presentations include a tax section covering ETR, DTA quality, and uncertain tax positions. The section is drafted by Group Tax and the CFO's office from the year's tax data and the prior year's presentation as a style anchor. The drafting cycle begins after all other financial sections are assembled, compressing the review window for a section that receives significant analytical scrutiny from rating analysts.
Solution: Agent reads the current year ETR reconciliation, DTA balance and recoverability assessment, IFRIC 23 uncertain tax provision register, and the prior year's rating agency presentation tax section. It drafts the tax section covering ETR trajectory with drivers, DTA quality and recoverability, IFRIC 23 position summary, and jurisdiction concentration. Group Tax reviews the draft for technical accuracy; the CFO's office adds framing context for the rating agency audience. The draft is available for inclusion in the presentation pack at the same time as the financial sections.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 8 [Insights|S] Tax Position Earnings Quality Insights
urn: urn:financial-services:scenario:finance-treasury/tax-management/rating-agency-tax/tax-position-earnings-quality-insights
intent: Agent produces a quarterly tax position earnings quality summary — assessing ETR sustainability, DTA utilisation trajectory, and IFRIC 23 provision adequacy against the bank's forward profit forecast — structured for the CFO's and audit committee's earnings quality review.
Problem to solve: Rating agencies and investors assess the bank's tax position as part of their earnings quality review, but the bank's internal quarterly close process does not produce a systematic earnings quality view of the tax position. ETR volatility analysis, DTA utilisation pace, and IFRIC 23 provision adequacy are addressed separately in the ETR reconciliation and DTA assessment rather than synthesised into a single earnings quality assessment.
Solution: Agent reads the quarterly ETR reconciliation, DTA balance and prior-quarter utilisation, IFRIC 23 uncertain provision register, and the approved forward profit forecast. It produces a structured earnings quality summary covering three questions: whether the current ETR is sustainable given the mix of permanent differences and deferred items, whether the DTA utilisation pace is consistent with the forward forecast, and whether the IFRIC 23 provision is directionally adequate given open tax authority enquiries. Group Tax reviews the summary before it is included in the CFO and audit committee pack.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 9 [Enablement|S] Tax Disclosure Peer Benchmarking
urn: urn:financial-services:scenario:finance-treasury/tax-management/rating-agency-tax/tax-disclosure-peer-benchmarking
intent: Agent compares the bank's disclosed ETR, DTA-to-capital ratio, and IFRIC 23 provision level against peer bank disclosures from the most recent annual reports, and produces a benchmarking summary for Group Tax and IR to assess the bank's disclosure positioning.
Problem to solve: Investors and rating agencies benchmark the bank's tax position against peers. Group Tax and IR assess this benchmarking informally by reading peer annual reports, without a structured comparison of the key tax metrics. The absence of a systematic benchmarking review means that material deviations in the bank's tax metrics from the peer range — which may attract rating analyst scrutiny or investor questions — are not identified before the rating agency meeting or investor call.
Solution: Agent reads the bank's current disclosed ETR, DTA balance as a percentage of Tier 1 capital, and IFRIC 23 uncertain provision level. It reads the equivalent disclosures from the most recent annual reports of a defined peer set and computes the peer range for each metric. The benchmarking summary presents the bank's position relative to the peer range, with any metric outside the peer band flagged for Group Tax and IR discussion. Group Tax and the CFO's office use the summary to prepare responses to expected rating analyst and investor questions on the bank's tax position.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
FATCA / CRS reporting compliance
Annual FATCA (US Foreign Account Tax Compliance Act) and CRS (OECD Common Reporting Standard) reporting requires the bank to identify reportable account holders, validate their tax residency and classification, and submit XML-formatted account data to the local tax authority for onward exchange with partner jurisdictions. Kazakhstan and Russia are both CRS signatory jurisdictions; FATCA obligations apply to any bank with US-connected customers or correspondent relationships.
Lens
Scenario
Intent
Complexity

### CARD 10 [Automation|S] FATCA & CRS XML Submission Validation
urn: urn:financial-services:scenario:finance-treasury/tax-management/fatca-crs-reporting/fatca-crs-xml-submission-validation
intent: Before the annual FATCA and CRS XML files are submitted to the local tax authority, agent validates the file structure, TIN format compliance, account balance population, and completeness against the reportable account population — producing a pre-submission validation report for Group Tax sign-off.
Problem to solve: FATCA and CRS XML submissions are generated from the bank's reporting system and submitted to the local tax authority without a comprehensive pre-submission validation. Submission errors — malformed XML, missing TINs for reportable accounts, account balances that differ from the authoritative source — are identified by the tax authority's processing system after submission and require corrective re-submissions with regulatory scrutiny.
Solution: Agent reads the generated XML file and validates it against the FATCA and CRS XML schema and the bank's authoritative reportable account population. It checks XML schema compliance, TIN format validity by jurisdiction, account balance consistency with the financial system, and completeness against the expected reportable account count. The pre-submission validation report presents each check as pass or fail, with failed items identified to the responsible data owner for correction before submission. Group Tax signs off the validation report before the file is dispatched to the tax authority.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 11 [Automation|M] FATCA / CRS Reporting Quality Check
urn: urn:financial-services:scenario:finance-treasury/tax-management/fatca-crs-reporting/fatca-crs-reporting-quality-check
intent: Agent validates FATCA and CRS account population, classification, and XML report data against schema rules and prior-year benchmarks before the annual submission window.
Problem to solve: Annual FATCA and CRS submissions require the bank to validate account classification, due diligence completeness, and XML schema compliance across thousands of reportable accounts. Data quality issues discovered after submission trigger amended returns and heightened regulator scrutiny.
Solution: Agent reads the account population extract, due diligence records, and classification decisions. It validates each record against FATCA/CRS classification rules, checks XML schema compliance, and compares the reportable population to the prior year with materiality-ranked exceptions. Tax Operations receives a structured exception report with remediation guidance before the submission window closes.
OKR objective: FATCA and CRS account population, classification, and XML report data are validated against schema rules and prior-year benchmarks before the annual submission window, with a structured exception report and remediation guidance delivered to Tax Operations.
OKR KR [Adoption]: Agent-produced FATCA/CRS quality validation used for ≥100% of annual submission cycles within year 1; all material account classifications and XML schema requirements covered.
OKR KR [Acceptance]: ≥90% of flagged exception items remediated by Tax Operations before the submission window closes; post-submission amended return rate attributable to classification or schema errors reduced by ≥50% vs. pre-deployment baseline.
OKR KR [Cycle]: FATCA/CRS exception report available to Tax Operations within 5 business days of account population extract, vs. 2–3 weeks of manual review in the prior process.

### CARD 12 [Insights|M] FATCA & CRS Account Classification Review
urn: urn:financial-services:scenario:finance-treasury/tax-management/fatca-crs-reporting/fatca-crs-account-classification-review
intent: Agent analyses the bank's FATCA and CRS reportable account population for classification consistency — identifying accounts where the tax residency, entity type, or reportable status classification is inconsistent with the information held in the customer data system or with OECD CRS guidance.
Problem to solve: FATCA and CRS account classifications are assigned during onboarding and updated through periodic review. Classification inconsistencies — accounts classified as non-reportable where the customer data indicates US indicia, or entity accounts where the controlling person classification conflicts with the KYC documentation — accumulate between review cycles and create regulatory exposure in the annual reporting submission.
Solution: Agent reads the FATCA/CRS classification file and the corresponding customer data records — tax identification numbers, declared tax residencies, entity legal form, and controlling person records. It applies the FATCA IGA and OECD CRS consistency rules, flags accounts where the classification is inconsistent with the customer data or where the classification cannot be traced to a completed self-certification, and produces a ranked exception list for Group Tax and Compliance review. The teams resolve each exception before the annual XML submission is prepared.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
GenAI-enabled Banking and Financial Services Framework · v11i
