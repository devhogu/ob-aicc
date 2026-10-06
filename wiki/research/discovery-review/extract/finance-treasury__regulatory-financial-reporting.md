# 

source: html-alt/financial-services/en/finance-treasury/regulatory-financial-reporting/index.html


[PAGE TEXT]
COREP & FINREP data quality validation
COREP and FINREP submissions to EBA-aligned regulators contain hundreds of data cells with embedded validation rules — intra-template arithmetic checks, cross-template consistency requirements, and regulatory threshold comparisons. Each return must pass the full EBA XBRL validation suite before submission. Data quality failures discovered late in the cycle require emergency remediation that risks missing the submission deadline.
Lens
Scenario
Intent
Complexity

### CARD 1 [Insights|S] COREP & FINREP Movement Commentary
urn: urn:financial-services:scenario:finance-treasury/regulatory-financial-reporting/corep-finrep-validation/corep-finrep-movement-commentary
intent: Agent analyses the period-on-period movements in material COREP and FINREP template cells, identifies the top five movements by absolute value, and drafts attributive commentary for each — enabling the regulatory reporting team to include a pre-validated narrative addendum with the submission.
Problem to solve: COREP and FINREP submissions are accompanied by management commentary on material movements, drafted by the regulatory reporting team after validation is complete. The drafting cycle begins once the data is validated, compressing the remaining submission window and producing commentary that is reactive rather than analytical.
Solution: Agent reads the current and prior-period COREP and FINREP template data immediately after the validation run completes. It identifies the top five template cells with the largest absolute period-on-period movement, cross-references each movement against the corresponding GL and risk system data to identify the driver, and drafts a commentary paragraph per movement in the regulatory team's house format. The team reviews each paragraph for accuracy and regulatory tone before inclusion in the submission package.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 2 [Automation|S] COREP & FINREP Submission Readiness Check
urn: urn:financial-services:scenario:finance-treasury/regulatory-financial-reporting/corep-finrep-validation/corep-finrep-submission-readiness-check
intent: On the day before the COREP or FINREP submission deadline, agent runs a final submission readiness check — confirming that all templates are populated, the XBRL validation suite has passed, the management commentary is attached, and the prior-period comparison is consistent — and presents a readiness certificate to the regulatory reporting lead.
Problem to solve: Last-minute COREP and FINREP submission issues — missing template sections, XBRL validation failures from a late data correction, or commentary that refers to a prior draft rather than the final data — are identified by the regulatory reporting lead through a manual pre-submission checklist. The checklist is not consistently executed under time pressure, and submission-day issues may require emergency remediation within a narrow window before the deadline.
Solution: Agent runs a structured submission readiness check on the day before the deadline: confirms template completeness, reruns the XBRL validation suite against the final data file, checks that the management commentary is attached and references the correct reporting period, and confirms that the prior-period comparison figures are consistent with the prior approved submission. Results are presented to the regulatory reporting lead as a readiness certificate with a pass/fail status per check. Any failed checks are presented with the specific issue and the responsible team for remediation.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 3 [Automation|M] COREP / FINREP Data Quality Validation
urn: urn:financial-services:scenario:finance-treasury/regulatory-financial-reporting/corep-finrep-validation/corep-finrep-data-quality-check
intent: Agent validates COREP and FINREP template data against EBA validation rules, cross-template consistency requirements, and prior-quarter benchmarks, delivering a prioritised exception report before the submission deadline.
Problem to solve: COREP and FINREP submissions contain hundreds of data cells with embedded EBA validation rules and cross-template consistency requirements. Data quality failures identified late in the cycle compress the remediation window before the submission deadline and risk regulatory scrutiny.
Solution: Agent ingests the populated COREP and FINREP templates, runs all prescribed EBA XBRL validation rules, checks cross-template consistency, and compares each material cell movement to the prior quarter with a materiality-ranked exception list. Finance receives the structured data quality report with prioritised remediation items with sufficient lead time before the submission deadline.
OKR objective: COREP and FINREP template data is validated against EBA validation rules, cross-template consistency requirements, and prior-quarter benchmarks before the submission deadline, with a prioritised exception report delivered to Finance with sufficient remediation lead time.
OKR KR [Adoption]: Agent-produced data quality validation used for ≥100% of quarterly COREP/FINREP submission cycles within year 1.
OKR KR [Acceptance]: ≥90% of validation exception reports result in Finance remediating all flagged items before submission; post-submission supervisory query rate on data quality grounds reduced by ≥40% vs. the pre-deployment baseline.
OKR KR [Cycle]: Prioritised exception report available within 1 business day of template population, vs. 2–4 days of manual validation in the prior process.

[PAGE TEXT]
NBKR / NBK / CBR prudential returns
Local prudential returns — NBKR Form 700 series, NBK/ARDFM capital adequacy tables, and CBR Form 0409300 series — are submitted monthly, quarterly, and annually to the respective national regulator. Each return requires data extraction from the GL and risk systems, mapping to the prescribed template format, and narrative explanation of significant movements. Return accuracy is subject to regulatory examination during on-site inspections.
Lens
Scenario
Intent
Complexity

### CARD 4 [Insights|S] Prudential Return Movement Insights
urn: urn:financial-services:scenario:finance-treasury/regulatory-financial-reporting/local-prudential-returns/prudential-return-movement-insights
intent: Agent compares the current-period prudential return to the prior submission and identifies the five largest cell-level movements, attributing each to its GL or risk system driver — providing the regulatory reporting team with a pre-drafted narrative explanation for each material movement before the submission narrative deadline.
Problem to solve: NBKR, NBK/ARDFM, and CBR require narrative explanation of material movements in prudential returns. The regulatory reporting team identifies the material movements manually after the template is populated and drafts explanatory narrative under submission deadline pressure, without a systematic cross-reference to the underlying driver in the GL or risk systems.
Solution: Agent reads the populated current-period template and the prior approved submission. It identifies the five largest cell-level movements by absolute value, maps each to the corresponding GL account or risk system driver, and drafts an attributive explanation in the regulatory house style for each movement. The regulatory reporting team reviews each explanation for accuracy and regulatory tone, confirms the driver attribution, and includes the approved explanations in the submission narrative. The draft is available as soon as the current-period template is validated.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 5 [Automation|S] Prudential Return Submission Calendar
urn: urn:financial-services:scenario:finance-treasury/regulatory-financial-reporting/local-prudential-returns/prudential-return-submission-calendar
intent: Agent maintains an integrated submission calendar for all NBKR, NBK/ARDFM, and CBR prudential returns — with submission deadlines, internal data-ready dates, and sign-off milestones — and issues a weekly preparation status report to the regulatory reporting lead throughout each submission cycle.
Problem to solve: NBKR, NBK/ARDFM, and CBR submission calendars span monthly, quarterly, and annual cycles across multiple return series. The regulatory reporting team tracks submission deadlines in a manual calendar that does not integrate with the internal data-ready milestones or the GL close schedule — creating periodic deadline-proximity surprises when the data-ready date for a quarterly return is discovered to conflict with the GL close window.
Solution: Agent maintains a structured submission calendar integrating each return's regulatory deadline, the internal data-ready milestone required, the GL close date dependency, and the sign-off milestone schedule. Each week it issues a preparation status report to the regulatory reporting lead — showing returns due within the next 30 days, current data-readiness status against each, and any milestone that is behind schedule. Deadline-proximity alerts are issued when a data-ready milestone is tracking late against the submission deadline. The regulatory reporting lead confirms the calendar at the start of each quarter.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 6 [Automation|M] Prudential Return Data Extraction & Validation
urn: urn:financial-services:scenario:finance-treasury/regulatory-financial-reporting/local-prudential-returns/prudential-return-data-extraction-validation
intent: Agent extracts data from the GL and risk systems into the prescribed NBKR Form 700, NBK/ARDFM capital adequacy, or CBR 0409300 template formats, applies the bank's regulatory mapping rules, and validates the extracted data against intra-template arithmetic and cross-template consistency checks before the regulatory reporting team's review.
Problem to solve: Prudential return preparation requires data to be extracted from the GL and risk systems and mapped to prescribed regulatory template formats — a manual process that is repeated each monthly, quarterly, and annual cycle and accounts for the majority of the regulatory reporting team's production time. Data mapping errors are identified through validation checks run by the team after extraction, adding a remediation loop to an already compressed submission timeline.
Solution: Agent reads the GL and risk system data extracts and applies the bank's regulatory mapping rules for the relevant return. It populates the prescribed template cells, runs the embedded intra-template arithmetic checks and cross-template consistency validations, and presents the populated template and a structured exception list to the regulatory reporting team. The team reviews the exceptions, corrects source data errors at the GL or risk system level, and confirms the final template before submission. Agent re-runs the validation after each correction cycle.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
Regulatory submission narrative
COREP, FINREP, and local prudential returns require explanatory narrative alongside quantitative templates — management commentary on significant movements, notes on methodology changes, and explanations of items exceeding supervisory movement thresholds. Narrative quality and consistency across submission cycles affects the supervisory relationship with NBKR, NBK/ARDFM, and CBR.
Lens
Scenario
Intent
Complexity

### CARD 7 [Insights|S] Regulatory Narrative Consistency Tracking
urn: urn:financial-services:scenario:finance-treasury/regulatory-financial-reporting/regulatory-narrative/regulatory-narrative-consistency-tracking
intent: Agent cross-references the narrative in the current regulatory submission against prior approved submissions to flag any statement that contradicts or materially departs from an established position — enabling the regulatory reporting team to address potential consistency concerns before filing.
Problem to solve: Regulatory submission narratives are reviewed for quality within the current submission but not systematically cross-referenced against prior submissions for consistency. Statements that contradict a prior-period explanation — a methodology description that conflicts with last year's ICAAP narrative, or a threshold explanation that differs from the prior COREP commentary — are identified by the regulator during inspection rather than by the bank before filing.
Solution: Agent reads the draft narrative for the current submission and the approved narratives from the prior four submission cycles. It identifies passages in the current draft where the stated methodology, threshold, or explanation differs from the corresponding passage in a prior submission, and presents each divergence to the regulatory reporting team with the prior-period text alongside. The team reviews each divergence and confirms whether it reflects an intentional methodology change — which should be explicitly disclosed — or an unintended inconsistency for correction.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 8 [Automation|S] Regulatory Narrative Movement Threshold Coverage
urn: urn:financial-services:scenario:finance-treasury/regulatory-financial-reporting/regulatory-narrative/regulatory-narrative-movement-threshold-flags
intent: Agent identifies every template cell that exceeds the regulator's stated movement explanation threshold for the current submission period, confirms that a narrative explanation exists for each, and flags any threshold-breaching movement that is not covered in the draft narrative.
Problem to solve: NBKR, NBK/ARDFM, and CBR prescribe movement explanation thresholds — cells where the period-on-period change exceeds a defined percentage or absolute amount require narrative explanation in the submission commentary. Identifying all threshold-breaching movements and confirming narrative coverage is performed manually by the regulatory reporting team, and under submission deadline pressure some threshold-breaching items may lack explanation — a finding that emerges in the regulator's validation review rather than before filing.
Solution: Agent reads the current-period template data and the regulator's published movement explanation thresholds. It identifies every cell where the period-on-period movement exceeds the threshold and cross-references each against the draft narrative to confirm that an explanation exists. Threshold-breaching cells without narrative coverage are presented to the team in a gap list with the movement amount, the threshold, and the relevant template row reference. The team drafts explanations for each uncovered item before submission.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 9 [Automation|L] Regulatory Submission Narrative & Investor Disclosure Drafting
urn: urn:financial-services:scenario:finance-treasury/regulatory-financial-reporting/regulatory-narrative/regulatory-narrative-investor-disclosure-drafting
intent: Agent drafts the narrative sections accompanying NBKR, NBK/ARDFM, and CBR prudential returns and produces the full text of the bank's investor-facing disclosures — quarterly earnings releases, annual MD&A, and investor letters — from closed financial data and prior submissions.
Problem to solve: Local prudential returns require explanatory narrative — movement commentary, one-time item notes, and deviation explanations — while annual and quarterly investor disclosures require 40–120 pages of MD&A and earnings commentary. Both workflows share the same source data but are produced by different teams with inconsistent output quality across cycles; cross-period consistency and disclosure completeness are checked manually.
Solution: Agent reads the current-period quantitative data, prior submissions, movement thresholds defined in supervisory guidance, and prior investor disclosures as style anchors. For regulatory returns, it drafts explanatory narrative in the prescribed supervisory format. For investor disclosures, it generates MD&A and earnings release text with cross-period consistency checking, disclosure compliance review against applicable IFRS and securities regulation, and forward-looking statement flagging. Finance and IR review and apply judgment on tone and commitment framing.
OKR objective: Narrative sections accompanying NBKR, NBK/ARDFM, and CBR prudential returns and full investor-facing disclosures — quarterly earnings releases, annual MD&A, and investor letters — are drafted from closed financial data and prior submissions with cross-period consistency verified and forward-looking statements flagged.
OKR KR [Adoption]: Agent used to draft regulatory narrative and investor disclosure sections for ≥4 quarterly and ≥1 annual reporting cycles within year 1.
OKR KR [Acceptance]: ≥80% of agent-drafted sections accepted by Finance and IR without material structural rewrite; IFRS and securities regulation compliance review confirms required disclosure elements present in ≥97% of reviewed disclosures.
OKR KR [Cycle]: Full draft of regulatory narrative and investor disclosure available for Finance and IR review within 5 business days of data close, vs. 2–3 weeks of manual production in the prior process.

[PAGE TEXT]
Investor disclosure & statutory accounts
Annual IFRS financial statements, quarterly earnings releases, and investor letters are the bank's public financial disclosure — filed with the regulator in some jurisdictions and published for investors in all. Each document requires cross-period consistency, numerical reconciliation across sections, and disclosure compliance review against applicable IFRS and securities regulation requirements.
Lens
Scenario
Intent
Complexity

### CARD 10 [Automation|S] Investor Disclosure Numerical Consistency Check
urn: urn:financial-services:scenario:finance-treasury/regulatory-financial-reporting/investor-disclosure/investor-disclosure-numerical-consistency
intent: Before the annual IFRS financial statements or quarterly earnings release is published, agent verifies numerical consistency across all document sections — cross-footing tables, reconciling figures that appear in multiple sections, and confirming period comparatives against prior published documents.
Problem to solve: Annual IFRS financial statements and quarterly earnings releases contain hundreds of numerical figures that must be consistent across sections — balance sheet totals that reconcile across the primary statements, ratios that are consistent with their component numerators and denominators, and comparative figures that match the prior period's published disclosure. Manual consistency review by the disclosure team catches most errors but operates under time pressure near publication and treats each document as a standalone review without systematic cross-referencing to prior publications.
Solution: Agent reads the draft financial statements or earnings release and applies a structured consistency check: cross-footing all table totals, verifying that figures appearing in multiple sections match, recomputing all stated ratios from their disclosed components, and comparing all comparative period figures against the prior approved publication. Exceptions — inconsistencies, rounding errors, and unexplained differences from prior publications — are presented in a numbered exception list to the disclosure team before publication. The team confirms each exception as intentional or directs a correction.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 11 [Insights|M] Earnings Release Drafting
urn: urn:financial-services:scenario:finance-treasury/regulatory-financial-reporting/investor-disclosure/earnings-release-drafting
intent: Agent drafts the quarterly earnings release from the closed management accounts, the capital and liquidity position, and the three most recent prior releases as style anchors — giving the CFO and IR team a complete draft on the day reporting closes, with all material movements attributed.
Problem to solve: Quarterly earnings releases are drafted by the CFO's office and the IR team from multiple source documents, with the drafting cycle beginning after all source documents are finalised. The process takes three to five days, and early drafts circulated for review frequently require structural revision as the CFO's framing develops — extending the cycle further and creating version control risk across a large review group.
Solution: Agent reads the closed management accounts, capital and liquidity reports, and the three most recent approved earnings releases as style and structural anchors. It generates a draft covering the standard release sections — financial highlights, segment performance, capital and liquidity, outlook, and financial tables — with attributed commentary for each material movement. The CFO and IR team receive the draft on the day reporting closes, review for strategic framing and forward guidance, and edit; the agent produces a revised draft from each round of edits. The consistency check is run against the final draft before publication.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 12 [Automation|M] IFRS Disclosure Compliance Review
urn: urn:financial-services:scenario:finance-treasury/regulatory-financial-reporting/investor-disclosure/ifrs-disclosure-compliance-review
intent: Agent reviews the draft annual IFRS financial statements against the applicable disclosure requirements — IFRS 7, IFRS 9, IFRS 13, and IAS 1 — and produces a compliance gap list identifying required disclosures that are absent or incomplete in the draft.
Problem to solve: Annual IFRS financial statements carry extensive disclosure requirements under IFRS 7 (financial instruments), IFRS 9 (impairment), IFRS 13 (fair value), and IAS 1 (presentation). The disclosure compliance review is conducted manually by the external auditors and by the bank's technical accounting team, with gaps identified in the audit review process rather than before the draft is submitted for audit. Late-stage gap identification adds to the audit timetable.
Solution: Agent reads the draft IFRS financial statements and a structured disclosure checklist derived from the applicable IFRS standards. It maps each required disclosure element to the corresponding section of the draft, identifies elements that are absent or incomplete, and produces a numbered compliance gap list with the IFRS reference, the disclosure requirement, and the location in the draft where the disclosure is expected. The technical accounting team reviews the gap list before the draft is submitted to the auditors, reducing audit-stage queries on disclosure completeness.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
GenAI-enabled Banking and Financial Services Framework · v11i
