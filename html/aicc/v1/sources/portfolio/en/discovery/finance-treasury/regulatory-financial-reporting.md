# Regulatory financial reporting

Regulatory financial reporting is the Bank's obligation to submit accurate, complete, and timely financial data to the prudential supervisor — in the regulator's own return forms or in a standardized template framework such as COREP and FINREP. Returns cover capital adequacy (Basel III/IV Pillar 1), credit risk, market risk, operational risk, and IFRS-based financial statements across monthly, quarterly, and annual cycles. Errors in regulatory returns trigger supervisory scrutiny and can lead to enforcement action. **The GenAI opportunity is automated data quality validation and narrative drafting — reducing the manual effort in each submission cycle and creating space for regulatory teams to focus on judgment rather than assembly.**

## Problems

### Basel & supervisory reporting {#basel-corep-finrep}

| Lens | Problem |
| --- | --- |
| Insights & analytics | Capital adequacy returns in a template framework such as COREP contain hundreds of data cells with embedded validation rules and cross-template consistency requirements. Regulatory Reporting teams identify data quality failures by running the regulator's XBRL validation suite — a process that surfaces failures late in the submission timeline, compressing the remediation window before the regulatory deadline. |
| Enablement | Regulatory Reporting managers spend significant time translating between the regulatory data model (the supervisory reporting templates) and the Bank's internal financial data — mapping GL accounts to template cells, reconciling to management accounts, and documenting the data lineage. The mapping maintenance burden grows with each regulatory update and each internal system change. |
| Automation | Explanatory notes, movement commentary, and management narrative accompanying supervisory submissions are drafted manually each cycle from quantitative template data and prior-period submissions. Each narrative section is structurally predictable — the regulatory format is prescribed — and the inputs are drawn from a known set of financial data. |
| New business opportunities | Banks that build regulatory reporting automation — validated data feeds, template pre-population, and narrative generation — create a capability that scales without proportional headcount growth as regulatory requirements increase. Supervisors have generally increased reporting granularity and frequency in recent years; the trend continues. |

## Supervisory template data quality validation {#corep-finrep-validation}

Where the regulator prescribes a standardized template framework such as COREP and FINREP, submissions contain hundreds of data cells with embedded validation rules — intra-template arithmetic checks, cross-template consistency requirements, and regulatory threshold comparisons. Each return must pass the regulator's full XBRL validation suite before submission. Data quality failures discovered late in the cycle require emergency remediation that risks missing the submission deadline.

### Supervisory Template Movement Commentary

- URN: urn:financial-services:scenario:finance-treasury/regulatory-financial-reporting/corep-finrep-validation/corep-finrep-movement-commentary
- Lens: Insights
- Complexity: S
- Intent: The AI agent analyzes the period-on-period movements in material cells of the supervisory reporting templates (such as COREP and FINREP), identifies the top five movements by absolute value, and drafts attributive commentary for each — enabling the regulatory reporting team to include a pre-validated narrative addendum with the submission.
- Problem to solve: Supervisory template submissions are accompanied by management commentary on material movements, drafted by the regulatory reporting team after validation is complete. The drafting cycle begins once the data is validated, compressing the remaining submission window and producing commentary that is reactive rather than analytical.
- Solution: The AI agent reads the current and prior-period template data immediately after the validation run completes. It identifies the top five template cells with the largest absolute period-on-period movement, cross-references each movement against the corresponding GL and risk system data to identify the driver, and drafts a commentary paragraph per movement in the regulatory reporting team's house format. The team reviews each paragraph for accuracy and regulatory tone before inclusion in the submission package.
- OKR: The regulatory reporting team receives, immediately after each validation run, drafted commentary on the five largest period-on-period movements in supervisory reporting template cells, each attributed to its GL or risk system driver, for inclusion in the submission package.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-drafted movement commentary used for ≥4 quarterly template submission cycles within year 1; top five movements covered in each cycle. |
| Acceptance | ≥85% of commentary paragraphs accepted by the regulatory reporting team without material rewrite; driver attribution confirmed against GL and risk system data in ≥95% of reviewed paragraphs. |
| Cycle | Commentary drafts available within 2 hours of the validation run, vs. drafting started only after validation with a compressed submission window in the prior process. |

### Supervisory Template Submission Readiness Check

- URN: urn:financial-services:scenario:finance-treasury/regulatory-financial-reporting/corep-finrep-validation/corep-finrep-submission-readiness-check
- Lens: Automation
- Complexity: S
- Intent: On the day before the submission deadline for supervisory reporting templates (such as COREP or FINREP), the AI agent runs a final submission readiness check — confirming that all templates are populated, the XBRL validation suite has passed, the management commentary is attached, and the prior-period comparison is consistent — and presents a readiness certificate to the regulatory reporting lead.
- Problem to solve: Last-minute template submission issues — missing template sections, XBRL validation failures from a late data correction, or commentary that refers to a prior draft rather than the final data — are identified by the regulatory reporting lead through a manual pre-submission checklist. The checklist is not consistently executed under time pressure, and submission-day issues may require emergency remediation within a narrow window before the deadline.
- Solution: The AI agent runs a structured submission readiness check on the day before the deadline: confirms template completeness, reruns the XBRL validation suite against the final data file, checks that the management commentary is attached and references the correct reporting period, and confirms that the prior-period comparison figures are consistent with the prior approved submission. Results are presented to the regulatory reporting lead as a readiness certificate with a pass/fail status per check. Any failed checks are presented with the specific issue and the responsible team for remediation.
- OKR: The regulatory reporting lead receives, on the day before each template submission deadline, a readiness certificate with pass/fail status for template completeness, XBRL validation, commentary attachment, and prior-period comparison consistency.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced readiness check run for 100% of template submission cycles within year 1; all four check categories covered. |
| Acceptance | ≥90% of failed checks remediated by the responsible team before the deadline; no submission-day emergency remediation required for an issue covered by the check. |
| Cycle | Readiness certificate available one business day before the deadline, vs. a manual checklist inconsistently executed under time pressure in the prior process. |

### Supervisory Template Data Quality Validation

- URN: urn:financial-services:scenario:finance-treasury/regulatory-financial-reporting/corep-finrep-validation/corep-finrep-data-quality-check
- Lens: Automation
- Complexity: M
- Intent: The AI agent validates the data in supervisory reporting templates (such as COREP and FINREP) against the regulator's validation rules, cross-template consistency requirements, and prior-quarter benchmarks, delivering a prioritized exception report before the submission deadline.
- Problem to solve: Supervisory template submissions contain hundreds of data cells with embedded validation rules and cross-template consistency requirements. Data quality failures identified late in the cycle compress the remediation window before the submission deadline and risk regulatory scrutiny.
- Solution: The AI agent ingests the populated templates, runs all prescribed XBRL validation rules, checks cross-template consistency, and compares each material cell movement to the prior quarter with a materiality-ranked exception list. Finance receives the structured data quality report with prioritized remediation items with sufficient lead time to remediate them before the submission deadline.
- OKR: Supervisory reporting template data is validated against the regulator's validation rules, cross-template consistency requirements, and prior-quarter benchmarks before the submission deadline, with a prioritized exception report delivered to Finance with sufficient remediation lead time.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced data quality validation used for 100% of quarterly template submission cycles within year 1. |
| Acceptance | ≥90% of validation exception reports result in Finance remediating all flagged items before submission; post-submission supervisory query rate on data quality grounds reduced by ≥40% vs. the pre-deployment baseline. |
| Cycle | Prioritized exception report available within 1 business day of template population, vs. 2–4 days of manual validation in the prior process. |

## Local prudential returns {#local-prudential-returns}

Local prudential returns — the regulator's own return series and capital adequacy tables — are submitted monthly, quarterly, and annually to the regulator. Each return requires data extraction from the GL and risk systems, mapping to the prescribed template format, and narrative explanation of significant movements. Return accuracy is subject to regulatory examination during on-site inspections.

### Prudential Return Movement Insights

- URN: urn:financial-services:scenario:finance-treasury/regulatory-financial-reporting/local-prudential-returns/prudential-return-movement-insights
- Lens: Insights
- Complexity: S
- Intent: The AI agent compares the current-period prudential return to the prior submission and identifies the five largest cell-level movements, attributing each to its GL or risk system driver — providing the regulatory reporting team with a pre-drafted narrative explanation for each material movement before the submission narrative deadline.
- Problem to solve: The regulator requires narrative explanation of material movements in prudential returns. The regulatory reporting team identifies the material movements manually after the template is populated and drafts explanatory narrative under submission deadline pressure, without a systematic cross-reference to the underlying driver in the GL or risk systems.
- Solution: The AI agent reads the populated current-period template and the prior approved submission. It identifies the five largest cell-level movements by absolute value, maps each to the corresponding GL account or risk system driver, and drafts an attributive explanation in the regulatory house style for each movement. The regulatory reporting team reviews each explanation for accuracy and regulatory tone, confirms the driver attribution, and includes the approved explanations in the submission narrative. The draft is available as soon as the current-period template is validated.
- OKR: The regulatory reporting team receives, as soon as the current-period prudential return template is validated, a drafted explanation of each of the five largest cell-level movements, attributed to its GL account or risk system driver.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-drafted movement explanations used for ≥90% of prudential return submissions in year 1; five largest movements covered in each return. |
| Acceptance | ≥85% of explanations approved by the regulatory reporting team without material rewrite; driver attribution confirmed in ≥95% of reviewed explanations. |
| Cycle | Draft explanations available on the day the template is validated, vs. manual identification and drafting under submission deadline pressure in the prior process. |

### Prudential Return Submission Calendar

- URN: urn:financial-services:scenario:finance-treasury/regulatory-financial-reporting/local-prudential-returns/prudential-return-submission-calendar
- Lens: Automation
- Complexity: S
- Intent: The AI agent maintains an integrated submission calendar for all prudential returns — with submission deadlines, internal data-ready dates, and sign-off milestones — and issues a weekly preparation status report to the regulatory reporting lead throughout each submission cycle.
- Problem to solve: Prudential return submission calendars span monthly, quarterly, and annual cycles across multiple return series. The regulatory reporting team tracks submission deadlines in a manual calendar that does not integrate with the internal data-ready milestones or the GL close schedule — creating periodic deadline-proximity surprises when the data-ready date for a quarterly return is discovered to conflict with the GL close window.
- Solution: The AI agent maintains a structured submission calendar integrating each return's regulatory deadline, the internal data-ready milestone required, the GL close date dependency, and the sign-off milestone schedule. Each week it issues a preparation status report to the regulatory reporting lead — showing returns due within the next 30 days, current data-readiness status against each, and any milestone that is behind schedule. Deadline-proximity alerts are issued when a data-ready milestone is tracking late against the submission deadline. The regulatory reporting lead confirms the calendar at the start of each quarter.
- OKR: The regulatory reporting lead receives a weekly preparation status report from an integrated submission calendar — returns due within the next 30 days, data-readiness against each, and milestones behind schedule — covering every prudential return.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced weekly status report delivered for ≥48 of 52 weeks in year 1; all monthly, quarterly, and annual return series included in the calendar. |
| Acceptance | ≥85% of deadline-proximity alerts confirmed by the regulatory reporting lead as requiring action; calendar confirmed by the lead at the start of each quarter without material correction. |
| Cycle | Data-ready and GL close conflicts flagged up to 30 days ahead, vs. deadline-proximity surprises from a manual calendar in the prior process. |

### Prudential Return Data Extraction & Validation

- URN: urn:financial-services:scenario:finance-treasury/regulatory-financial-reporting/local-prudential-returns/prudential-return-data-extraction-validation
- Lens: Automation
- Complexity: M
- Intent: The AI agent extracts data from the GL and risk systems into the regulator's prescribed prudential return template formats, applies the Bank's regulatory mapping rules, and validates the extracted data against intra-template arithmetic and cross-template consistency checks before the regulatory reporting team's review.
- Problem to solve: Prudential return preparation requires data to be extracted from the GL and risk systems and mapped to prescribed regulatory template formats — a manual process that is repeated each monthly, quarterly, and annual cycle and accounts for the majority of the regulatory reporting team's production time. Data mapping errors are identified through validation checks run by the team after extraction, adding a remediation loop to an already compressed submission timeline.
- Solution: The AI agent reads the GL and risk system data extracts and applies the Bank's regulatory mapping rules for the relevant return. It populates the prescribed template cells, runs the embedded intra-template arithmetic checks and cross-template consistency validations, and presents the populated template and a structured exception list to the regulatory reporting team. The team reviews the exceptions, corrects source data errors at the GL or risk system level, and confirms the final template before submission. The AI agent re-runs the validation after each correction cycle.
- OKR: The regulatory reporting team receives each prudential return populated from GL and risk system extracts under the Bank's regulatory mapping rules, with a structured exception list from the intra-template arithmetic and cross-template consistency checks.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-populated templates used for ≥90% of monthly, quarterly, and annual prudential return cycles in year 1. |
| Acceptance | ≥90% of populated cells accepted by the regulatory reporting team without manual re-mapping; ≥85% of listed exceptions confirmed as genuine source data or mapping errors. |
| Cycle | Populated template and exception list available within 1 business day of the GL and risk system extracts, vs. manual extraction and mapping that takes the majority of the team's production time in the prior process. |

## Regulatory submission narrative {#regulatory-narrative}

Supervisory reporting templates and local prudential returns require explanatory narrative alongside quantitative templates — management commentary on significant movements, notes on methodology changes, and explanations of items exceeding supervisory movement thresholds. Narrative quality and consistency across submission cycles affect the Bank's relationship with the regulator.

### Regulatory Narrative Consistency Tracking

- URN: urn:financial-services:scenario:finance-treasury/regulatory-financial-reporting/regulatory-narrative/regulatory-narrative-consistency-tracking
- Lens: Insights
- Complexity: S
- Intent: The AI agent cross-references the narrative in the current regulatory submission against prior approved submissions to flag any statement that contradicts or materially departs from an established position — enabling the regulatory reporting team to address potential consistency concerns before filing.
- Problem to solve: Regulatory submission narratives are reviewed for quality within the current submission but not systematically cross-referenced against prior submissions for consistency. Statements that contradict a prior-period explanation — a methodology description that conflicts with last year's ICAAP narrative, or a threshold explanation that differs from the prior capital adequacy return commentary — are identified by the regulator during inspection rather than by the Bank before filing.
- Solution: The AI agent reads the draft narrative for the current submission and the approved narratives from the prior four submission cycles. It identifies passages in the current draft where the stated methodology, threshold, or explanation differs from the corresponding passage in a prior submission, and presents each divergence to the regulatory reporting team with the prior-period text alongside. The team reviews each divergence and confirms whether it reflects an intentional methodology change — which should be explicitly disclosed — or an unintended inconsistency for correction.
- OKR: The regulatory reporting team receives, before filing, every passage in the draft submission narrative whose stated methodology, threshold, or explanation departs from the approved narratives of the prior four submission cycles, with the prior-period text alongside.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced consistency review run on ≥90% of regulatory submission narratives in year 1. |
| Acceptance | ≥80% of presented divergences confirmed by the team as either an intentional change to disclose or an inconsistency to correct; no contradiction with a prior submission first identified by the regulator during inspection. |
| Cycle | Divergence list available within 1 business day of the draft narrative, vs. no systematic cross-reference to prior submissions in the prior process. |

### Regulatory Narrative Movement Threshold Coverage

- URN: urn:financial-services:scenario:finance-treasury/regulatory-financial-reporting/regulatory-narrative/regulatory-narrative-movement-threshold-flags
- Lens: Automation
- Complexity: S
- Intent: The AI agent identifies every template cell that exceeds the regulator's stated movement explanation threshold for the current submission period, confirms that a narrative explanation exists for each, and flags any threshold-breaching movement that is not covered in the draft narrative.
- Problem to solve: The regulator prescribes movement explanation thresholds — cells where the period-on-period change exceeds a defined percentage or absolute amount require narrative explanation in the submission commentary. Identifying all threshold-breaching movements and confirming narrative coverage is performed manually by the regulatory reporting team, and under submission deadline pressure some threshold-breaching items may lack explanation — a finding that emerges in the regulator's validation review rather than before filing.
- Solution: The AI agent reads the current-period template data and the regulator's published movement explanation thresholds. It identifies every cell where the period-on-period movement exceeds the threshold and cross-references each against the draft narrative to confirm that an explanation exists. Threshold-breaching cells without narrative coverage are presented to the regulatory reporting team in a gap list with the movement amount, the threshold, and the relevant template row reference. The team drafts explanations for each uncovered item before submission.
- OKR: The regulatory reporting team receives, before submission, a gap list of every template cell whose period-on-period movement exceeds the regulator's explanation threshold and is not covered in the draft narrative, with the movement amount, the threshold, and the template row reference.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced threshold coverage check run on ≥95% of submissions subject to movement explanation thresholds in year 1. |
| Acceptance | 100% of gap-list items given an explanation by the team before submission; ≥95% of threshold breaches identified by the AI agent confirmed against the template data. |
| Cycle | Gap list available within 2 hours of the draft narrative, vs. manual identification with gaps emerging in the regulator's validation review in the prior process. |

### Regulatory Submission Narrative & Investor Disclosure Drafting

- URN: urn:financial-services:scenario:finance-treasury/regulatory-financial-reporting/regulatory-narrative/regulatory-narrative-investor-disclosure-drafting
- Lens: Automation
- Complexity: L
- Intent: The AI agent drafts the narrative sections accompanying prudential returns and produces the full text of the Bank's investor-facing disclosures — quarterly earnings releases, annual MD&A, and investor letters — from closed financial data and prior submissions.
- Problem to solve: Local prudential returns require explanatory narrative — movement commentary, one-time item notes, and deviation explanations — while annual and quarterly investor disclosures require 40–120 pages of MD&A and earnings commentary. Both workflows share the same source data but are produced by different teams with inconsistent output quality across cycles; cross-period consistency and disclosure completeness are checked manually.
- Solution: The AI agent reads the current-period quantitative data, prior submissions, movement thresholds defined in supervisory guidance, and prior investor disclosures as style anchors. For regulatory returns, it drafts explanatory narrative in the prescribed supervisory format. For investor disclosures, it generates MD&A and earnings release text with cross-period consistency checking, disclosure compliance review against applicable IFRS and securities regulation, and forward-looking statement flagging. Finance and IR review and apply judgment on tone and commitment framing.
- OKR: Narrative sections accompanying prudential returns and full investor-facing disclosures — quarterly earnings releases, annual MD&A, and investor letters — are drafted from closed financial data and prior submissions with cross-period consistency verified and forward-looking statements flagged.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-drafted regulatory narrative and investor disclosure sections used for ≥4 quarterly and ≥1 annual reporting cycles within year 1. |
| Acceptance | ≥80% of AI-drafted sections accepted by Finance and IR without material structural rewrite; IFRS and securities regulation compliance review confirms required disclosure elements present in ≥97% of reviewed disclosures. |
| Cycle | Full draft of regulatory narrative and investor disclosure available for Finance and IR review within 5 business days of data close, vs. 2–3 weeks of manual production in the prior process. |

## Investor disclosure & statutory accounts {#investor-disclosure}

Annual IFRS financial statements, quarterly earnings releases, and investor letters are the Bank's public financial disclosure — filed with the regulator where required and published for investors. Each document requires cross-period consistency, numerical reconciliation across sections, and disclosure compliance review against applicable IFRS and securities regulation requirements.

### Investor Disclosure Numerical Consistency Check

- URN: urn:financial-services:scenario:finance-treasury/regulatory-financial-reporting/investor-disclosure/investor-disclosure-numerical-consistency
- Lens: Automation
- Complexity: S
- Intent: Before the annual IFRS financial statements or quarterly earnings release is published, the AI agent verifies numerical consistency across all document sections — cross-footing tables, reconciling figures that appear in multiple sections, and confirming period comparatives against prior published documents.
- Problem to solve: Annual IFRS financial statements and quarterly earnings releases contain hundreds of numerical figures that must be consistent across sections — balance sheet totals that reconcile across the primary statements, ratios that are consistent with their component numerators and denominators, and comparative figures that match the prior period's published disclosure. Manual consistency review by the disclosure team catches most errors but operates under time pressure near publication and treats each document as a standalone review without systematic cross-referencing to prior publications.
- Solution: The AI agent reads the draft financial statements or earnings release and applies a structured consistency check: cross-footing all table totals, verifying that figures appearing in multiple sections match, recomputing all stated ratios from their disclosed components, and comparing all comparative period figures against the prior approved publication. Exceptions — inconsistencies, rounding errors, and unexplained differences from prior publications — are presented in a numbered exception list to the disclosure team before publication. The team confirms each exception as intentional or directs a correction.
- OKR: The disclosure team receives, before the annual IFRS financial statements or a quarterly earnings release is published, a numbered exception list from cross-footing table totals, matching figures that appear in multiple sections, recomputing stated ratios, and checking comparatives against prior publications.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced consistency check run on ≥4 quarterly earnings releases and ≥1 set of annual IFRS financial statements within year 1. |
| Acceptance | ≥85% of listed exceptions confirmed by the disclosure team as either intentional or requiring correction; no numerical inconsistency identified after publication. |
| Cycle | Exception list available within 2 hours of each draft, vs. manual review under time pressure near publication in the prior process. |

### Earnings Release Drafting

- URN: urn:financial-services:scenario:finance-treasury/regulatory-financial-reporting/investor-disclosure/earnings-release-drafting
- Lens: Automation
- Complexity: M
- Intent: The AI agent drafts the quarterly earnings release from the closed management accounts, the capital and liquidity position, and the three most recent prior releases as style anchors — giving the CFO and IR team a complete draft on the day reporting closes, with all material movements attributed.
- Problem to solve: Quarterly earnings releases are drafted by the CFO's office and the IR team from multiple source documents, with the drafting cycle beginning after all source documents are finalized. The process takes three to five days, and early drafts circulated for review frequently require structural revision as the CFO's framing develops — extending the cycle further and creating version control risk across a large review group.
- Solution: The AI agent reads the closed management accounts, capital and liquidity reports, and the three most recent approved earnings releases as style and structural anchors. It generates a draft covering the standard release sections — financial highlights, segment performance, capital and liquidity, outlook, and financial tables — with attributed commentary for each material movement. The CFO and IR team receive the draft on the day reporting closes, review for strategic framing and forward guidance, and edit; the AI agent produces a revised draft from each round of edits. The numerical consistency check is run against the final draft before publication.
- OKR: The CFO and IR team receive a complete draft of the quarterly earnings release — financial highlights, segment performance, capital and liquidity, outlook, and financial tables, with each material movement attributed — on the day reporting closes.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-drafted earnings release used for ≥4 quarterly reporting cycles within year 1; all standard release sections covered. |
| Acceptance | ≥80% of drafts accepted by the CFO and IR team without material structural revision; figures reconcile to the closed management accounts and capital and liquidity reports in ≥98% of reviewed drafts. |
| Cycle | Complete draft available on the day reporting closes, vs. three to five days of drafting after source documents are finalized in the prior process. |

### IFRS Disclosure Compliance Review

- URN: urn:financial-services:scenario:finance-treasury/regulatory-financial-reporting/investor-disclosure/ifrs-disclosure-compliance-review
- Lens: Automation
- Complexity: M
- Intent: The AI agent reviews the draft annual IFRS financial statements against the applicable disclosure requirements — IFRS 7, IFRS 9, IFRS 13, and IAS 1 — and produces a compliance gap list identifying required disclosures that are absent or incomplete in the draft.
- Problem to solve: Annual IFRS financial statements carry extensive disclosure requirements under IFRS 7 (financial instruments), IFRS 9 (impairment), IFRS 13 (fair value), and IAS 1 (presentation). The disclosure compliance review is conducted manually by the external auditors and by the Bank's technical accounting team, with gaps identified in the audit review process rather than before the draft is submitted for audit. Late-stage gap identification adds to the audit timetable.
- Solution: The AI agent reads the draft IFRS financial statements and a structured disclosure checklist derived from the applicable IFRS standards. It maps each required disclosure element to the corresponding section of the draft, identifies elements that are absent or incomplete, and produces a numbered compliance gap list with the IFRS reference, the disclosure requirement, and the location in the draft where the disclosure is expected. The technical accounting team reviews the gap list before the draft is submitted to the auditors, reducing audit-stage queries on disclosure completeness.
- OKR: The technical accounting team receives, before the draft annual IFRS financial statements are submitted to the auditors, a numbered compliance gap list of required IFRS 7, IFRS 9, IFRS 13, and IAS 1 disclosures that are absent or incomplete.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced disclosure compliance review run on ≥1 set of annual IFRS financial statements within year 1; all four standards in the disclosure checklist covered. |
| Acceptance | ≥85% of listed gaps confirmed by the technical accounting team as genuine; audit-stage queries on disclosure completeness reduced by ≥50% vs. the prior year. |
| Cycle | Gap list available within 2 business days of the draft statements, vs. gaps identified during the audit review in the prior process. |
