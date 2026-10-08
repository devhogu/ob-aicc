# Credit & exposure data

Credit & exposure data is the risk data layer that aggregates every on- and off-balance-sheet commitment the Bank has made to borrowers, counterparties, and connected-party groups — covering loan-level records, counterparty and group exposure aggregations, collateral and security data, the PD/LGD/EAD credit parameter inputs that drive capital where the Bank uses internal-ratings (IRB) models, and the ECL and provision data required for IFRS 9 reporting. Large-exposure requirements, in line with Basel III, call for credit and exposure data to be aggregated across all product types within a defined supervisory response window. BCBS 239 Principle 4 (completeness) sets the expectation that no material exposure is excluded from the aggregate. **The GenAI opportunity is to automate large-exposure aggregation on a weekly cadence, monitor collateral valuations against LTV covenants continuously, and generate ECL provision narratives without manual assembly** — sustaining a current view of credit risk data between monthly reporting cycles.

## Problems

### Loan-level exposure {#loan-level-exposure}

| Lens | Problem |
| --- | --- |
| Insights & analytics | Large-exposure monitoring — the aggregation of on- and off-balance-sheet exposures to each counterparty and connected-party group across all product types — is performed monthly from separate system exports. Between cycles, exposure movements relative to regulatory thresholds are visible only to the teams monitoring individual product books; a cumulative approach to the limit by a group of connected counterparties may not be detected until the monthly aggregate runs. |
| Enablement | Credit review preparation for the watchlist and large-exposure committees requires assembling the current exposure picture — loans, commitments, derivatives, and trade finance — for each counterparty from separate product systems. The data-assembly step precedes the substantive credit analysis; for counterparties with complex product relationships, the assembly consumes the majority of preparation time. |
| Automation | Large-exposure aggregation, ECL staging flow computation, and PD/LGD/EAD model output compilation each follow defined logic applied to structured credit and position data on monthly or quarterly cycles. The aggregation logic is prescribed by the regulatory framework and is repeatable; the execution is manual and time-intensive. |
| New business opportunities | A continuously aggregated large-exposure view — updated weekly from live product positions — gives the Chief Credit Officer visibility into concentration headroom and group exposure utilization that monthly reporting cannot provide. Credit appetite deployment decisions for new transactions can be assessed against current exposure before committee approval. |

## Loan-level exposure records {#loan-level-exposure-records}

The granular record for each loan or credit facility — covering outstanding balance, committed amount, drawn and undrawn portions, facility terms, maturity, collateral linkage, and risk classification. Loan-level records are the atomic unit from which portfolio analytics, concentration metrics, and regulatory reporting are derived. Their completeness and accuracy determine the reliability of every aggregate produced from the credit book; missing or misclassified records propagate into IFRS 9 staging, large-exposure calculations, and capital computation.

### Loan Book Data Quality Scan

- URN: urn:financial-services:scenario:banking-data-analytics/credit-exposure-data/loan-level-exposure-records/loan-book-data-quality-scan
- Lens: Automation
- Complexity: S
- Intent: The AI agent runs a daily data quality scan across loan-level records in core banking — checking completeness of mandatory fields, consistency of drawn and committed amounts, validity of risk classification codes, and linkage to the collateral registry and customer golden record. The credit operations team receives a prioritized exception list by field type and facility size. Exceptions affecting IFRS 9 staging or large-exposure aggregation are flagged at elevated priority for same-day remediation.
- Problem to solve: Loan-level record quality is validated manually at month-end as part of the ECL and regulatory reporting close. Between month-end cycles, new disbursements, drawdowns, and re-pricing events may introduce incomplete or inconsistent records that are not detected until the next validation run. Missing risk classification codes, mismatched drawn and committed amounts, and absent collateral linkages propagate silently into portfolio analytics, IFRS 9 staging, and large-exposure aggregation until the month-end check.
- Solution: The AI agent reads all active loan and credit facility records from core banking and applies a quality rule set covering mandatory field completeness, amount consistency, risk classification code validity, and collateral and customer golden record linkage. Records failing any rule are categorized by failure type and ranked by outstanding balance and downstream impact — IFRS 9 staging impact, large-exposure aggregation impact, or regulatory reporting impact. The credit operations team receives the exception list each morning with remediation priority and SLA by exception category, confirms the exceptions, and remediates them.
- OKR: Loan-level data quality exceptions are identified daily for the credit operations team and remediated before they propagate into IFRS 9 staging, large-exposure aggregation, or regulatory reporting.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces daily loan book quality scans covering 100% of active facilities for ≥ 48 weeks within 12 months; quality rule set approved by credit risk and data governance within 60 days of go-live. |
| Acceptance | ≥ 85% of exceptions confirmed as genuine data quality failures by credit operations; high-priority exceptions remediated within the same-day SLA in ≥ 80% of cases within 3 months of go-live. |
| Cycle | Loan book quality validation cycle shifted from monthly manual review to a daily automated scan; exceptions affecting IFRS 9 or large-exposure aggregation cleared before the next downstream calculation run in ≥ 90% of cases. |

### Loan Classification Consistency Check

- URN: urn:financial-services:scenario:banking-data-analytics/credit-exposure-data/loan-level-exposure-records/loan-classification-consistency-check
- Lens: Insights
- Complexity: S
- Intent: The AI agent identifies loan facilities where the risk classification assigned in core banking is inconsistent with the IFRS 9 stage, the PD band, or the days-past-due status of the underlying account. The credit risk team uses the inconsistency report to investigate potential classification errors and update records before the next ECL and capital calculation cycle. Systematic classification patterns that diverge from model-implied grades are flagged for model validation review.
- Problem to solve: Risk classifications are assigned to loan facilities in core banking by credit officers and updated through the periodic review process. IFRS 9 staging and PD bands — IRB PD bands where the Bank uses internal-ratings models — are generated separately by the model engine. Where a facility carries a risk grade that is materially inconsistent with its model-implied PD or its IFRS 9 stage, the inconsistency may reflect a genuine credit judgment or a classification error. Without a systematic cross-check, classification errors are identified only when they surface in the Pillar 3 disclosure review or the external audit.
- Solution: The AI agent reads risk classifications from core banking and cross-references each facility against its IFRS 9 stage, model-implied PD band, and days-past-due status. Facilities where the assigned grade is more than one notch above the model-implied grade, or where the IFRS 9 stage does not align with the PD-implied staging outcome, are flagged in a monthly inconsistency report. The report distinguishes between potentially genuine overrides — larger facilities with documented credit officer justification — and unexplained divergences for investigation. The credit risk team investigates the unexplained divergences and corrects records before the next ECL and capital calculation cycle; systematic divergence patterns across a portfolio segment are flagged for the model validation team.
- OKR: Loan risk classification inconsistencies are identified for the credit risk team before each ECL and capital calculation cycle, with genuine overrides distinguished from unexplained divergences requiring investigation.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces monthly classification consistency reports covering 100% of active facilities for ≥ 12 consecutive months; cross-reference logic validated by credit risk and model validation within 60 days of go-live. |
| Acceptance | ≥ 80% of flagged inconsistencies confirmed as requiring investigation or correction by the credit risk team; model validation team reviews systematic divergence flags for ≥ 90% of flagged portfolio segments within the quarter. |
| Cycle | Classification inconsistency detection cycle shifted from ad hoc audit identification to a monthly structured cross-check; inconsistencies corrected before ECL and capital runs in ≥ 85% of cases within 6 months. |

### Portfolio Concentration Analytics

- URN: urn:financial-services:scenario:banking-data-analytics/credit-exposure-data/loan-level-exposure-records/portfolio-concentration-analytics
- Lens: Enablement
- Complexity: M
- Intent: The AI agent aggregates loan-level records by sector, geography, product type, collateral type, and risk grade band to produce a monthly portfolio concentration report for the Risk Committee and the credit portfolio team. The report identifies concentration build-up against board-approved appetite limits and generates a narrative summary of the three largest concentration movements since the prior month. The credit portfolio team uses the report for portfolio steering and appetite limit breach monitoring.
- Problem to solve: Portfolio concentration analysis requires aggregating the full loan book by multiple dimensions — sector, geography, product type, risk grade — and measuring each concentration against the board-approved limit framework. The aggregation is performed monthly by the credit analytics team using SQL extracts from core banking and credit systems. The resulting concentration table is distributed to the Risk Committee but without a narrative identifying which concentrations are growing fastest or approaching limits. Portfolio steering decisions are based on the concentration table without a structured signal about emerging risks.
- Solution: The AI agent reads the current loan book from core banking, aggregates by sector, geography, product type, collateral type, and risk grade band, and calculates utilization ratios against board-approved concentration limits. It produces the concentration table and a narrative summary identifying the three largest concentration movements month-on-month, any concentration approaching within 10% of an appetite limit, and the sector and geography mix of new disbursements in the period. The credit portfolio team reviews and approves the report before it goes to the Risk Committee, and receives an accompanying alert for concentrations approaching appetite limits.
- OKR: The Risk Committee and credit portfolio team receive a structured monthly concentration report with narrative signals on emerging build-up, supporting proactive portfolio steering before appetite limits are reached.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces monthly concentration reports covering 100% of the loan book for ≥ 12 consecutive months; concentration limit framework ingested and applied from go-live. |
| Acceptance | ≥ 85% of narrative summaries accepted by the credit portfolio team as accurate without material amendments; concentration limit alerts confirmed as requiring action in ≥ 80% of cases within 3 months. |
| Cycle | Concentration report assembly time reduced from 2–3 analyst days to ≤ half a day of review and approval per month; narrative commentary delivered alongside the concentration table from the first production cycle. |

## Collateral & security data {#collateral-security-data}

The records of collateral pledged against each secured credit facility — property valuations and legal registrations, financial security market values, inventory and receivables pledges, and personal guarantees — linked to the corresponding loan record. Collateral data drives LTV covenant monitoring, credit-impairment assessment, and LGD parameter calibration. How current a valuation is depends on the collateral type: financial securities update at market prices daily; commercial real estate updates through formal appraisals annually. The gap between formal valuation cycles and current market conditions creates LTV uncertainty that continuous monitoring tools can estimate but not fully resolve.

### Collateral Valuation Monitoring

- URN: urn:financial-services:scenario:banking-data-analytics/credit-exposure-data/collateral-security-data/collateral-valuation-monitoring
- Lens: Insights
- Complexity: S
- Intent: The AI agent monitors collateral valuations against loan exposures, flagging LTV covenant approaches and breaches before the next scheduled review cycle. The credit risk team receives a collateral-monitoring report ranked by severity of coverage deterioration. Interim market-index adjustments are applied to property and securities valuations between formal appraisals to maintain a current LTV view.
- Problem to solve: Collateral valuations — real estate, securities, and inventory — are updated on cycles ranging from monthly to annually depending on asset class. Between updates, market movements can erode collateral cover against the outstanding loan balance without the credit risk team's awareness. Collateral shortfalls are identified at the next formal valuation unless interim monitoring is in place.
- Solution: The AI agent reads current collateral valuations, applies market index adjustments for property and securities between formal appraisals, and computes current LTV for each secured exposure. It flags exposures where the adjusted LTV has crossed or is approaching covenant thresholds and generates a collateral-monitoring report for the credit risk team ranked by severity of coverage deterioration. The credit officer uses the report to prioritize collateral review and remediation actions.
- OKR: The credit risk team monitors current LTV positions every business day between formal appraisal cycles, with interim market-index adjustments applied to property and securities collateral and covenant-threshold alerts routed by severity.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent applies market-index LTV adjustments to ≥ 95% of secured exposures on a daily cadence; collateral-monitoring report delivered to the credit risk team each business day within year 1. |
| Acceptance | ≥ 85% of LTV covenant-approach alerts rated as actionable by credit officers; index-adjusted LTV values validated against formal appraisal outcomes within ± 5% for ≥ 90% of exposures at the next formal revaluation. |
| Cycle | Collateral coverage deterioration identified within 1 business day of the triggering market movement, compared to identification at the next scheduled formal appraisal. |

### Collateral Registry Completeness Check

- URN: urn:financial-services:scenario:banking-data-analytics/credit-exposure-data/collateral-security-data/collateral-registry-completeness-check
- Lens: Automation
- Complexity: S
- Intent: The AI agent scans the collateral registry daily against the loan book to identify secured facilities where collateral linkage is missing, valuations are overdue for refresh, or legal registration records are absent. The credit operations team receives a prioritized gap list by collateral type and facility size. Each gap carries an SLA for remediation based on the proximity of the next LTV covenant test or ECL assessment date.
- Problem to solve: Collateral records are maintained across the collateral registry and core banking systems; completeness checks are performed manually at quarter-end ahead of ECL and LTV reporting cycles. Between cycles, newly disbursed secured facilities may carry incomplete collateral linkage, overdue valuations, or missing legal registration data. These gaps surface as last-minute remediation items during the reporting close, compressing the time available for credit quality assessment.
- Solution: The AI agent reads the secured loan population from core banking and cross-references each facility against the collateral registry — checking collateral linkage, last-valuation date against required refresh frequency by collateral type, and legal registration status. Facilities with gaps are ranked by outstanding balance and proximity to the next LTV or ECL assessment. The credit operations team receives a daily prioritized work list with gap type, SLA, and responsible owner, and confirms and closes each gap.
- OKR: The collateral registry carries complete, current records for every secured facility, with gaps identified for the credit operations team and remediated before the next LTV covenant test or ECL assessment date.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces daily collateral completeness reports covering 100% of the secured loan population for ≥ 48 weeks within the first 12 months; gap detection active across all collateral types from go-live. |
| Acceptance | ≥ 85% of flagged gaps confirmed as requiring remediation by the credit operations team; false-positive rate on gap flags ≤ 10% within 3 months of go-live. |
| Cycle | Collateral completeness check cycle reduced from quarterly manual review to a daily automated scan; remediation backlog at quarter-end reduced to ≤ 5% of the secured portfolio within 6 months. |

### Collateral LTV Covenant Watch

- URN: urn:financial-services:scenario:banking-data-analytics/credit-exposure-data/collateral-security-data/collateral-ltv-covenant-watch
- Lens: Enablement
- Complexity: M
- Intent: The AI agent monitors LTV ratios on commercial real estate and financial security collateral on a continuous basis, flagging facilities approaching covenant breach thresholds and generating a pre-breach notice for the relationship manager (RM). For financial securities, the AI agent applies current market prices daily; for commercial real estate, it estimates the current value between formal appraisal cycles using index adjustments. The RM uses the notice to initiate borrower dialogue before a formal covenant event is triggered.
- Problem to solve: LTV covenant monitoring for real estate collateral relies on annual formal appraisals; between cycles the Bank carries LTV uncertainty as property market conditions move. Financial securities collateral updates daily from market prices but LTV monitoring against covenant thresholds is a manual step performed by credit analysts. Facilities approaching breach thresholds are identified reactively — at the point of breach rather than in advance — limiting the Bank's ability to manage the credit event proactively.
- Solution: The AI agent retrieves outstanding balances from core banking and current collateral values — market price for financial securities, index-adjusted estimate for commercial real estate — and calculates the current LTV for each secured facility. Facilities within a defined proximity band of the covenant threshold are flagged in a daily watch list ranked by headroom remaining. For each flagged facility, the AI agent drafts a pre-breach notice summarizing the current LTV, the covenant threshold, and the estimated market movement required to trigger a formal event. The RM reviews and initiates borrower dialogue as appropriate.
- OKR: Relationship managers receive early warning of LTV covenant proximity on all secured facilities, enabling proactive borrower engagement before formal covenant breach events materialize.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces daily LTV watch lists covering 100% of LTV-covenanted facilities for ≥ 48 weeks within 12 months; index-adjusted commercial real estate (CRE) estimation methodology approved by credit risk within 90 days of go-live. |
| Acceptance | ≥ 80% of pre-breach notices acted on by RMs within the defined response window; RM confirmation that index-adjusted LTV estimates are directionally reliable in ≥ 85% of cases reviewed. |
| Cycle | LTV monitoring cadence for CRE collateral shifted from annual formal appraisal review to a continuous index-adjusted daily watch; pre-breach notice issued ≥ 30 days before formal covenant event in ≥ 90% of breach cases within 6 months. |

## Counterparty & group exposure {#counterparty-group-exposure}

The aggregated credit exposure to a single counterparty or connected group of counterparties — consolidating on-balance-sheet loans and commitments, off-balance-sheet contingent liabilities, derivative mark-to-market exposure, and trade finance obligations — measured against single-name and group limits. Large-exposure limits commonly cap a single counterparty or connected group at 25% of Tier 1 capital; positions approaching this threshold typically trigger enhanced monitoring and supervisory notification. Aggregation across product types and entity hierarchies is the primary data challenge.

### Large-Exposure Limit Utilization Report

- URN: urn:financial-services:scenario:banking-data-analytics/credit-exposure-data/counterparty-group-exposure/large-exposure-limit-utilisation-report
- Lens: Enablement
- Complexity: S
- Intent: The AI agent generates the monthly large-exposure limit utilization report for the Risk Committee and the supervisory submission, covering all single-name and group exposures above 10% of Tier 1 capital with utilization ratios, headroom, and trend commentary. The risk officer reviews the draft report and adds qualitative context; the AI agent handles data assembly and the utilization narrative. The report is formatted to the regulator's large-exposure reporting template.
- Problem to solve: The large-exposure limit utilization report is assembled manually each month by the credit risk team, aggregating exposure data across product types and formatting the utilization table and narrative for the Risk Committee pack and the supervisory submission. The assembly step — pulling current exposures, calculating utilization ratios, and drafting the trend commentary — consumes two to three analyst days each cycle and is compressed when the Risk Committee pack deadline follows the month-end data close by fewer than five business days.
- Solution: The AI agent reads the consolidated counterparty and group exposure statement, retrieves the current Tier 1 capital figure from the capital reporting system, calculates utilization ratios against single-name and group limits, and identifies exposures above the 10% reporting threshold. It drafts the utilization table and a trend commentary section noting month-on-month movements above a defined threshold. The risk officer reviews the draft, adds qualitative context, and approves for Risk Committee submission and regulatory filing.
- OKR: The Risk Committee and the regulator receive a complete, formatted large-exposure utilization report on each monthly cycle with analyst capacity directed to qualitative review rather than data assembly.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-assembled large-exposure reports delivered for ≥ 12 consecutive monthly cycles within the first year; the regulator's template formatting applied from go-live. |
| Acceptance | ≥ 85% of report drafts accepted by the risk officer without material data amendments; utilization calculations validated against manual checks in ≥ 95% of cases in the first quarter. |
| Cycle | Report assembly time reduced from 2–3 analyst days to ≤ half a day of review and approval per cycle within 3 months of go-live. |

### Counterparty Group Exposure Aggregation

- URN: urn:financial-services:scenario:banking-data-analytics/credit-exposure-data/counterparty-group-exposure/counterparty-group-aggregation
- Lens: Automation
- Complexity: M
- Intent: The AI agent aggregates on-balance-sheet loans and commitments, off-balance-sheet contingent liabilities, derivative MTM exposure, and trade finance obligations for each counterparty and connected group on a weekly cadence, producing a consolidated exposure statement measured against single-name and group limits under large-exposure requirements. The credit risk team uses the statement to monitor the large-exposure limit, commonly 25% of Tier 1 capital, and to prepare the supervisory notification when positions approach it.
- Problem to solve: Aggregating total counterparty exposure across product types — loans, derivatives, letters of credit, guarantees — requires joining records from core banking, treasury, trade finance, and the derivatives ledger. The aggregation is performed manually by the credit risk team ahead of each monthly reporting cycle. Connected-party group hierarchies are maintained separately in the entity management system; mapping each counterparty to its group and consolidating group-level exposure is an additional manual step. Positions approaching the 25% limit are identified at the monthly cycle rather than on a continuous basis.
- Solution: The AI agent reads exposure records from core banking, the derivatives ledger, trade finance, and the off-balance-sheet commitment register, resolves each counterparty to its connected group using the entity hierarchy, and produces a consolidated exposure statement by counterparty and group. Positions crossing 20% of Tier 1 capital (the early-warning threshold) are flagged with a pre-notification brief for the credit risk officer. The credit risk team validates the weekly statement, which is formatted for the Risk Committee pack and for supervisory notification under large-exposure requirements.
- OKR: The credit risk team holds a current, product-complete view of single-name and group exposures measured against large-exposure limits, with pre-notification briefs generated before the supervisory threshold is reached.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces weekly consolidated exposure statements covering all product types for ≥ 48 weeks within 12 months; connected-group hierarchy ingested from the entity management system and applied from go-live. |
| Acceptance | ≥ 90% of exposure aggregations validated by the credit risk team as complete and accurate against manual cross-checks in the first quarter; pre-notification briefs issued for 100% of positions crossing the 20% early-warning threshold. |
| Cycle | Exposure aggregation cycle reduced from monthly manual consolidation to a weekly automated run; large-exposure monitoring posture shifted from reactive monthly identification to continuous weekly tracking within 3 months of go-live. |

### Connected-Party Group Mapping

- URN: urn:financial-services:scenario:banking-data-analytics/credit-exposure-data/counterparty-group-exposure/connected-party-group-mapping
- Lens: Insights
- Complexity: M
- Intent: The AI agent analyzes ownership and control data from the entity registry and beneficial ownership records, applying FIBO entity relationship structures, to identify connected-party groups that are not captured in the current manual hierarchy. The credit risk team uses the AI-generated group map to update the entity hierarchy before the next large-exposure aggregation cycle. Groups with incomplete or stale ownership data are flagged for CDE refresh.
- Problem to solve: Connected-party group hierarchies rely on ownership and control data maintained in the entity registry; groups are defined manually when relationships are identified during KYC or credit review. Groups where ownership structures are opaque, where control is exercised through nominees or intermediate holding companies, or where group membership has changed since the last review are not reliably captured. Large-exposure rules commonly require connected groups to be aggregated even where direct ownership falls below formal thresholds if control is exercised in other ways.
- Solution: The AI agent reads entity ownership, control, and beneficial ownership records from the KYC system and entity registry, applies FIBO entity relationship structures to identify indirect ownership chains and control relationships, and generates a proposed group map for entities where the current hierarchy is absent or where ownership data has changed since the last review. The credit risk team reviews and approves proposed group assignments before they are applied to the exposure aggregation. Entities where beneficial ownership data is missing or expired are flagged for CDE refresh.
- OKR: The connected-party group hierarchy is kept current and accurate through monthly analysis of ownership and control records, with new and updated group relationships identified for the credit risk team before each large-exposure aggregation cycle.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces group mapping proposals on a monthly cadence covering all entities with ownership changes or absent hierarchy entries for ≥ 12 consecutive months; FIBO relationship model applied from go-live. |
| Acceptance | ≥ 80% of proposed group assignments confirmed as correct by the credit risk team on first review; beneficial ownership data gap flags actioned in ≥ 85% of cases within one KYC refresh cycle. |
| Cycle | Connected-party group hierarchy review cycle reduced from ad hoc manual updates to a monthly structured pass; ownership changes reflected in the proposed group map within one monthly cycle of the registry or KYC update. |

## ECL & provision data {#ecl-provision-data}

The expected credit loss calculation and provision balance under IFRS 9 — produced quarterly from PD, LGD, EAD, and forward-looking macroeconomic adjustment factors, staged by SICR trigger assessment (Stage 1, 2, and 3). ECL provision data drives the Bank's impairment charge, regulatory capital deductions, and Pillar 3 disclosures. The quarterly provision narrative — explaining stage movements, macro overlay assumptions, and variance to the prior quarter — is consumed by the Audit Committee, external auditors, and supervisory authorities. Its production requires cross-referencing model outputs, staging flow data, and prior disclosures across finance and credit risk teams.

### Macro Overlay Sensitivity Brief

- URN: urn:financial-services:scenario:banking-data-analytics/credit-exposure-data/ecl-provision-data/macro-overlay-sensitivity-brief
- Lens: Enablement
- Complexity: S
- Intent: The AI agent produces a sensitivity brief quantifying the ECL provision impact of varying the macro overlay assumptions — GDP growth, unemployment, and commodity price inputs — across the base, downside, and severe downside scenarios. The brief enables the Audit Committee and finance leadership to assess provision sensitivity before approving the quarterly overlay assumptions. The credit risk team uses the brief to support the overlay calibration decision and to document the basis for the selected assumptions.
- Problem to solve: IFRS 9 forward-looking macro adjustments require a bank to apply probability-weighted macro scenarios to ECL calculations. The overlay calibration decision — selecting the scenario weights and input values — is reviewed by the Audit Committee and finance leadership each quarter. The provision sensitivity to different overlay assumptions is calculated manually by the credit risk team for the scenarios under consideration; the calculation scope is limited by the time available within the quarterly close window.
- Solution: The AI agent reads the approved scenario framework, retrieves the macro input ranges for GDP, unemployment, and commodity price under each scenario weight, and runs a parametric sensitivity calculation showing provision movement per unit change in each macro input. It produces a structured sensitivity brief: a scenario sensitivity table by portfolio segment, a commentary on the scenarios driving the largest provision swing, and a comparison to the prior quarter's overlay assumptions and their outturn. The credit risk team uses the brief in the overlay calibration discussion and as supporting documentation for the selected assumptions.
- OKR: The Audit Committee and finance leadership make the quarterly macro overlay calibration decision with access to a structured sensitivity brief covering the full scenario range, with the calculation delivered within the close window.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent delivers the macro overlay sensitivity brief for ≥ 4 consecutive quarterly ECL cycles within the first year; sensitivity calculation methodology reviewed and approved by model risk within 60 days. |
| Acceptance | ≥ 85% of sensitivity briefs used by the credit risk team in the overlay calibration discussion without material supplementary calculations; Audit Committee confirms sensitivity brief addresses scenario questions in ≥ 3 of 4 cycles. |
| Cycle | Macro sensitivity calculation time within the quarterly close reduced from 1–2 days of manual calculation to ≤ 4 hours of automated run and review. |

### ECL Provision Narrative

- URN: urn:financial-services:scenario:banking-data-analytics/credit-exposure-data/ecl-provision-data/exposure-aggregation-narrative
- Lens: Automation
- Complexity: M
- Intent: The AI agent assembles the quarterly IFRS 9 ECL provision narrative — stage movements, macro overlay rationale, and variance to prior quarter — for finance controller and CRO review. The narrative is generated in the prescribed format from model outputs, staging flow data, and prior disclosures. The finance controller and CRO review and sign off before disclosure.
- Problem to solve: The quarterly IFRS 9 ECL narrative requires cross-referencing model outputs, staging flow data, macro overlay assumptions, and prior disclosures. Inconsistencies between the model output view and the prior-quarter disclosure framing are identified late in the drafting process. The narrative drafting consumes substantial analyst hours per cycle before sign-off.
- Solution: The AI agent reads current ECL model outputs, staging flow data, macro overlay assumptions, and prior quarter disclosures. It generates the IFRS 9 provision narrative in the prescribed format — stage movement explanation, macro overlay rationale, and variance analysis relative to the prior quarter. The finance controller and CRO review the AI-generated narrative and sign off before disclosure.
- OKR: The finance controller and CRO review an AI-assembled quarterly IFRS 9 ECL provision narrative — covering stage movements, macro overlay rationale, and variance to prior quarter — in the prescribed disclosure format before sign-off.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces the IFRS 9 provision narrative for 100% of quarterly disclosure cycles within 12 months of go-live; stage movement, macro overlay, and variance sections included in each output. |
| Acceptance | ≥ 85% of narratives accepted by the finance controller and CRO without material amendment to the quantitative sections; macro overlay rationale rated as accurately described in ≥ 90% of cycles. |
| Cycle | Narrative drafting time reduced from substantial analyst hours per cycle to ≤ 4 hours of finance controller and CRO review per quarterly cycle. |

### ECL Stage Movement Analysis

- URN: urn:financial-services:scenario:banking-data-analytics/credit-exposure-data/ecl-provision-data/ecl-stage-movement-analysis
- Lens: Insights
- Complexity: M
- Intent: The AI agent analyzes quarterly IFRS 9 stage flow data — the population and balance movements between Stage 1, Stage 2, and Stage 3 — and produces a structured stage movement commentary for the Audit Committee and external auditors. The commentary explains the SICR triggers driving Stage 2 inflows, the cures and write-offs driving Stage 3 outflows, and the net provision impact of each flow. The credit risk team reviews the draft commentary and adds forward-looking context before Audit Committee submission.
- Problem to solve: The quarterly ECL provision narrative requires a detailed analysis of stage movements — which facilities moved between IFRS 9 stages, what SICR triggers drove Stage 2 inflows, and what the provision impact was by portfolio segment. Assembling the stage flow analysis from the ECL model output and provision system requires the credit risk and finance teams to join staging, PD, and balance data across multiple systems. The narrative drafting step follows the data assembly and consumes senior risk officer time that could be directed to analytical interpretation.
- Solution: The AI agent reads the quarterly staging flow data from the ECL system — opening and closing stage populations, transfers by direction and SICR trigger type, and provision balance movements — and produces a structured stage movement commentary: a flow table by portfolio segment, a SICR trigger attribution section, and a provision impact summary. The credit risk team reviews the draft, adds forward-looking context on portfolio quality trends, and approves for Audit Committee and external auditor submission.
- OKR: The Audit Committee and external auditors receive a structured, data-grounded stage movement commentary on each quarterly ECL cycle, with analyst capacity directed to interpretation and forward-looking assessment.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces stage movement commentary for ≥ 4 consecutive quarterly ECL cycles within the first year; SICR trigger attribution logic validated by credit risk within 60 days of go-live. |
| Acceptance | ≥ 80% of draft commentaries accepted by credit risk as factually complete without data amendments; Audit Committee feedback confirms commentary addresses stage movement questions in ≥ 3 of 4 quarterly cycles. |
| Cycle | Stage movement data assembly and commentary drafting cycle reduced from 3–4 analyst days to ≤ 1 day of review and approval per quarter. |

## Credit parameter inputs (PD/LGD/EAD) {#credit-parameter-inputs}

The probability of default (PD), loss given default (LGD), and exposure at default (EAD) estimates — produced by IRB models where the Bank uses internal ratings — that are consumed by regulatory capital computation (RWA), IFRS 9 ECL staging, and risk-adjusted pricing. Under the Basel III Pillar 1 IRB framework and supervisory model approval requirements, PD/LGD/EAD parameters are generated from approved models, monitored for performance against approved benchmarks, and recalibrated when performance deteriorates below supervisory thresholds. The parameters are regenerated monthly and consumed by capital, credit risk, and finance teams.

### Credit Parameter Review Brief

- URN: urn:financial-services:scenario:banking-data-analytics/credit-exposure-data/credit-parameter-inputs/credit-parameter-review-brief
- Lens: Enablement
- Complexity: S
- Intent: Where the Bank uses internal-ratings (IRB) models, the AI agent assembles the quarterly PD/LGD/EAD model performance review pack — actual versus predicted default rates, back-test results, and recalibration triggers — for the model validation committee. The pack is assembled in the format required by applicable model governance requirements. The model validation officer reviews the AI-assembled pack and adds professional judgment on recalibration decisions before committee submission.
- Problem to solve: The quarterly IRB model performance review requires the model risk team to extract back-test outputs, compare predicted PD/LGD/EAD against observed outcomes, and assess whether performance thresholds defined in the model approval require recalibration. The assembly of the review pack from multiple model output systems is a manual data consolidation exercise that consumes model validation team capacity before each committee cycle. Deadline pressure limits the depth of validation analysis.
- Solution: The AI agent reads back-test results, predicted versus observed default and loss rates, and model performance thresholds from the model risk system. It assembles the review pack in the prescribed format — per-model performance summary, threshold breach flags, and recalibration recommendation triggers under applicable model governance requirements. The model validation officer reviews the AI-assembled pack and adds professional judgment on recalibration decisions before committee submission.
- OKR: The model validation committee receives an AI-assembled PD/LGD/EAD performance review pack in the prescribed supervisory format, enabling the model validation officer to concentrate review capacity on recalibration judgment rather than data assembly.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent assembles the quarterly model performance review pack for 100% of in-scope IRB models across all four quarters within the first 12 months; delivery completed ≥ 5 business days before each committee cycle. |
| Acceptance | ≥ 85% of AI-assembled packs accepted by the model validation officer without material amendment to the quantitative sections; recalibration trigger flags validated as accurate in ≥ 90% of cases. |
| Cycle | Review pack assembly time reduced from days of manual data consolidation to ≤ 4 hours of model validation officer review per quarterly cycle. |

### PD/LGD/EAD Output Quality Gate

- URN: urn:financial-services:scenario:banking-data-analytics/credit-exposure-data/credit-parameter-inputs/pd-lgd-ead-output-quality-gate
- Lens: Automation
- Complexity: S
- Intent: The AI agent validates each monthly PD, LGD, and EAD parameter run against a defined set of quality rules — population completeness, parameter distribution plausibility, and cross-system consistency with prior-month values — before the outputs are consumed by IFRS 9 staging and, where the Bank uses internal-ratings (IRB) models, by capital computation. Validation failures are routed to the model operations team with a failure description and the downstream impact if the parameter run proceeds uncorrected.
- Problem to solve: PD, LGD, and EAD parameters are regenerated monthly; each run is consumed directly by RWA capital computation and IFRS 9 ECL staging. Quality validation before consumption is a manual review step performed by the model operations team, checking that the population is complete, that parameter distributions fall within expected ranges, and that month-on-month movements are within acceptable bounds. The review is time-constrained within the month-end close window; anomalous parameter outputs that pass the manual review propagate into capital and ECL calculations.
- Solution: The AI agent reads the completed PD, LGD, and EAD parameter run and applies a defined quality rule set: population count against prior month and expected portfolio size, distribution percentile checks against approved benchmark bands, and month-on-month movement flags for parameters exceeding a defined threshold. Failures are routed to the model operations team as a structured quality report — failure type, affected segment or model, and the capital and ECL impact of proceeding with the flagged output. The parameter run is cleared for downstream consumption only after the team resolves or accepts each flagged item.
- OKR: PD, LGD, and EAD parameter runs pass a structured quality gate before downstream consumption, with anomalies identified and resolved within the month-end close window.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent applies the quality gate to 100% of monthly parameter runs for ≥ 12 consecutive months within the first year; quality rule set approved by model risk within 60 days of go-live. |
| Acceptance | ≥ 90% of quality failures confirmed as genuine anomalies requiring resolution by the model operations team; false-positive rate on quality flags ≤ 8% within 3 months of go-live. |
| Cycle | Manual quality review step replaced by automated gate for ≥ 95% of parameter runs within 6 months; gate output delivered within 2 hours of parameter run completion, ahead of the downstream consumption window. |

### IRB Model Performance Monitor

- URN: urn:financial-services:scenario:banking-data-analytics/credit-exposure-data/credit-parameter-inputs/irb-model-performance-monitor
- Lens: Insights
- Complexity: M
- Intent: Where the Bank uses internal-ratings (IRB) models, the AI agent monitors PD, LGD, and EAD model performance against approved benchmarks on a monthly cadence, producing a model performance dashboard for the model risk and credit risk teams. The dashboard flags models where discriminatory power, calibration, or stability metrics have deteriorated below supervisory thresholds, triggering the model review process under supervisory model approval requirements. The model risk team uses the dashboard as the primary input to the quarterly model review agenda.
- Problem to solve: IRB model performance monitoring requires the model risk team to calculate Gini coefficients, Brier scores, PSI, and calibration metrics for each approved PD, LGD, and EAD model against the approved performance benchmarks. The calculation is performed quarterly using validation cohort data; deterioration in model performance between quarterly reviews is not detected until the next scheduled run. Supervisory model approval frameworks expect timely identification and escalation of performance breaches.
- Solution: The AI agent reads the monthly PD, LGD, and EAD outputs for each approved model, retrieves the corresponding validation cohort outcomes, and calculates discriminatory power (Gini, AUC), calibration (mean predicted vs actual default rate), and stability (PSI) metrics. Models where any metric crosses the threshold defined in the approved model documentation are flagged with a model review trigger. The monthly dashboard is structured for the model risk team, which confirms each review trigger, and is formatted for inclusion in the quarterly model review agenda submitted to the regulator under model approval reporting requirements.
- OKR: Model performance deterioration across the IRB parameter set is identified for the model risk team at a monthly cadence, with review triggers generated before the quarterly regulatory model review cycle.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces monthly model performance dashboards covering 100% of approved PD, LGD, and EAD models for ≥ 12 consecutive months within the first year; metric calculations aligned to approved model documentation thresholds from go-live. |
| Acceptance | ≥ 85% of performance breach flags confirmed as requiring model review by the model risk team; metric calculations validated against manual quarterly calculations in ≥ 95% of cases in the first two quarters. |
| Cycle | Performance monitoring cadence shifted from quarterly manual calculation to a monthly automated run; breach detection lead time extended from zero (detected at quarterly review) to up to 2 months before the next scheduled review cycle. |
