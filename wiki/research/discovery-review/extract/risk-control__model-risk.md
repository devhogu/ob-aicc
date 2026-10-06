# 

source: html-alt/financial-services/en/risk-control/model-risk/index.html


[PAGE TEXT]
Model inventory & governance
The model inventory is the master register of every model in production use — covering the model's purpose, owner, development date, validation status, approval decision, and monitoring plan. SR 11-7 requires the inventory to be comprehensive and current; regulators expect to be able to walk from a business decision to the models informing it and from each model to its validation history. Shadow models — spreadsheet tools and vendor outputs that function as models but are not registered — are the most common inventory gap identified in regulatory model risk reviews. Maintaining a current, accurate inventory requires systematic reconciliation against technology and vendor records.
Lens
Scenario
Intent
Complexity

### CARD 1 [Automation|S] Model Inventory & Documentation Completeness Check
urn: urn:financial-services:scenario:risk-control/model-risk/model-inventory-governance/model-inventory-documentation-completeness
intent: Agent scans the model inventory against the MRM policy documentation standard, flags gaps per model, and generates the completeness report for the Chief Model Risk Officer.
Problem to solve: Model documentation completeness — development documentation, validation reports, approval records, and ongoing monitoring plans — is reviewed manually against the MRM policy standard. With 80–200 models in a typical bank's inventory, the completeness audit is a periodic exercise that misses interim gaps between review cycles.
Solution: Agent reads the model inventory and associated documentation repositories, applies the MRM policy schema as a completeness checklist, flags missing or stale documents per model, and produces a completeness report ranked by regulatory priority. The Chief Model Risk Officer reviews gaps and assigns owners for remediation.
OKR objective: The Chief Model Risk Officer manages model documentation completeness from an agent-generated completeness report — applying the MRM policy standard across the full inventory — rather than a periodic manual audit.
OKR KR [Adoption]: Agent completeness check run across 100% of model inventory entries at least quarterly within 6 months of go-live; MRM policy schema applied as the completeness checklist in every run from go-live.
OKR KR [Acceptance]: ≥85% of agent-flagged documentation gaps confirmed as genuine by the Chief Model Risk Officer on review; interim documentation gap rate between annual reviews reduced by ≥50% versus the prior periodic audit approach.
OKR KR [Cycle]: Full inventory completeness report delivered within 3 business days of inventory data cut, enabling gap remediation to begin within the same reporting month rather than at annual review.

### CARD 2 [Enablement|S] Model Inventory Annual Attestation Support
urn: urn:financial-services:scenario:risk-control/model-risk/model-inventory-governance/model-inventory-annual-attestation
intent: Agent pre-populates the annual model inventory attestation form for each model owner — summarising current status, validation history, monitoring plan, and outstanding findings — reducing the per-owner completion time and improving attestation response rates.
Problem to solve: Annual model inventory attestation requires each model owner to confirm and update their model's details. Low response rates and incomplete submissions are common; the model risk function spends significant time chasing owners and reconciling incomplete attestations before the inventory certification is complete.
Solution: Agent reads current inventory records for each model, pre-populates the attestation form with the current status, validation date, monitoring plan citation, and open finding count. Model owners receive a pre-populated form requiring only confirmation or update rather than a blank template, reducing the completion burden. The Chief Model Risk Officer reviews exceptions before certification.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 3 [Insights|M] Shadow Model Identification Scan
urn: urn:financial-services:scenario:risk-control/model-risk/model-inventory-governance/shadow-model-identification
intent: Agent scans business unit systems and shared drives for spreadsheet tools and vendor outputs that meet the SR 11-7 model definition, identifies items not registered in the model inventory, and delivers a shadow model candidates list to the Chief Model Risk Officer.
Problem to solve: Shadow models — spreadsheet tools and vendor outputs that function as models but are not registered in the inventory — are the most common inventory gap identified in regulatory model risk reviews. Identifying these requires systematic scanning of business unit systems; the current approach relies on business units self-reporting, which systematically underestimates the shadow model population.
Solution: Agent scans metadata from business unit shared drives and finance system exports, applies the SR 11-7 model definition criteria to identify files that function as quantitative tools producing outputs used in business decisions, and cross-references each candidate against the registered model inventory. The Chief Model Risk Officer reviews the candidate list and initiates inventory onboarding for confirmed shadow models.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
Model performance monitoring
Ongoing monitoring tracks each model's performance between validation cycles — measuring discrimination (Gini, KS, AUC for classification models), calibration (predicted vs actual default rates, ECL vs realized losses), and stability (PSI, CSI for input distribution shifts). SR 11-7 requires documented monitoring plans for every model, with defined escalation triggers when performance falls below acceptable bands. Performance deterioration that crosses a materiality threshold triggers an out-of-cycle validation. For credit risk models, performance deterioration coincides with macroeconomic cycle turns — precisely the moment when the model's outputs are most consequential for capital and provision planning.
Lens
Scenario
Intent
Complexity

### CARD 4 [Automation|M] Model Performance Monthly Dashboard
urn: urn:financial-services:scenario:risk-control/model-risk/model-performance-monitoring/model-performance-monthly-dashboard
intent: Agent assembles the monthly model performance dashboard from owner-submitted monitoring reports, applying consistent metric computation and flagging models that breach defined performance thresholds for the Chief Model Risk Officer.
Problem to solve: SR 11-7 requires documented performance monitoring for every model. Model owners submit monitoring outputs in varying formats; the model risk function must standardise metrics, compute aggregate performance indicators, and identify threshold breaches before each monthly Model Risk Committee cycle — a manual consolidation task across 80-200 models.
Solution: Agent reads monthly monitoring submissions from model owners, standardises performance metrics by model class (Gini/KS for credit, RMSE for continuous, backtesting exception counts for market risk), flags threshold breaches, and assembles the dashboard in the committee's standard format. The Chief Model Risk Officer reviews flagged models before the committee pack is distributed.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 5 [Insights|M] Model Performance Deterioration Alert
urn: urn:financial-services:scenario:risk-control/model-risk/model-performance-monitoring/model-performance-deterioration-alert
intent: Agent monitors performance metric trends across the model portfolio between monthly reporting cycles, flagging models where trajectory indicates an imminent threshold breach before it is surfaced in the next scheduled report.
Problem to solve: Performance deterioration is identified at the monthly monitoring cycle. A model declining steadily across three months may cross the threshold only in the fourth month; the model risk function has no signal of the developing deterioration during the intervening reporting windows.
Solution: Agent reads performance metric time series across the portfolio, applies trend analysis to identify models on a deteriorating trajectory, and flags models projected to breach performance thresholds within 90 days. The Chief Model Risk Officer receives the trend alert between monthly cycles, enabling proactive validation scheduling.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 6 [Insights|M] Model Performance vs Macro Correlation Analysis
urn: urn:financial-services:scenario:risk-control/model-risk/model-performance-monitoring/model-performance-vs-macro-correlation
intent: Agent cross-references credit model performance metrics with macroeconomic cycle indicators to identify models whose calibration is likely to deteriorate under the current macro outlook, informing the validation prioritisation schedule.
Problem to solve: Credit risk model performance deterioration correlates with macroeconomic cycle turns, but the model risk function's validation prioritisation does not systematically factor in macro signals. A model calibrated in a benign credit environment may perform adequately today while the macro environment deteriorating around it; the validation team discovers the misalignment when the performance metric breaches its threshold.
Solution: Agent reads macro indicators — GDP growth, credit spreads, unemployment — alongside monthly model performance metrics for PD, LGD, and ECL models, computes the historical correlation between macro cycle and model performance, and flags models whose performance is historically correlated with the current macro trajectory. The Chief Model Risk Officer uses the output to front-load validation of macro-sensitive models.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
Model validation
Model validation is the set of processes and activities intended to verify that models perform as expected and are appropriate for their intended use. Under SR 11-7, validation must be conducted by a function independent of model development and must include conceptual soundness review, outcome analysis, and ongoing monitoring. EBA model risk guidelines impose equivalent requirements for EU-regulated banks. Validation engagements produce formal reports with findings classified by severity; material findings must be remediated before the model can be approved for expanded use. The volume of models requiring annual or biennial validation often exceeds the capacity of the validation function.
Lens
Scenario
Intent
Complexity

### CARD 7 [Enablement|M] Model Development Specification Drafting
urn: urn:financial-services:scenario:risk-control/model-risk/model-validation/model-development-spec-drafting
intent: Agent drafts the model development specification — conceptual soundness rationale, data lineage, methodology alternatives considered, and back-test design — from the modeller's working notes and data exploration outputs.
Problem to solve: Model development specifications are drafted by quantitative analysts after the development work is complete, with documentation quality that is inconsistent across the team. Validators frequently return specifications for additional conceptual soundness explanation or data lineage detail, extending the validation cycle and delaying model deployment.
Solution: Agent reads the modeller's working notes, exploratory analysis outputs, and dataset documentation, and drafts the development specification in the bank's standard template — conceptual soundness argument, data lineage, methodology alternatives, benchmark comparison, and back-test design. The modeller reviews and fills expert judgement sections before submission to model validation.
OKR objective: Modellers submit development specifications drafted by the agent from working notes and data exploration outputs — covering conceptual soundness, data lineage, methodology alternatives, and back-test design — for expert review rather than producing documentation after development is complete.
OKR KR [Adoption]: Agent used to draft model development specifications for ≥70% of new model and material model change submissions within 12 months of go-live; all standard template sections produced by the agent in every run from go-live.
OKR KR [Acceptance]: ≥75% of agent-drafted specifications accepted by Model Validation without a first-pass return for additional documentation; validation cycle length reduced by ≥20% for agent-documented models versus manually documented peers.
OKR KR [Cycle]: Development specification draft delivered within 2 business days of modeller working note submission, versus ≥1 week of post-development manual documentation under the prior approach.

### CARD 8 [Insights|M] Model Validation Finding Synthesis
urn: urn:financial-services:scenario:risk-control/model-risk/model-validation/model-validation-finding-synthesis
intent: Agent reads completed validation reports across a calendar year, clusters findings by category and root cause, and identifies systemic weaknesses in the bank's model development practices for the Chief Model Risk Officer's annual model risk review.
Problem to solve: Validation findings are documented in individual reports reviewed by the Model Risk Committee on a model-by-model basis. Systemic weaknesses — documentation shortfalls common to models built by a specific team, or recurring conceptual soundness challenges in a model class — are visible in aggregate but not in the individual report review cycle.
Solution: Agent reads all validation reports completed in the year, extracts finding categories and root causes, clusters them by model family and development team, and identifies systemic patterns. The Chief Model Risk Officer uses the analysis in the annual model risk programme review and in targeted developer training planning.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 9 [Automation|M] Validation Pipeline Capacity Planning
urn: urn:financial-services:scenario:risk-control/model-risk/model-validation/validation-pipeline-capacity-planning
intent: Agent projects the validation pipeline demand for the next 12 months — based on scheduled revalidation dates, new model submissions, and model changes — and compares it against available validation capacity, flagging capacity gaps for the Chief Model Risk Officer.
Problem to solve: Validation pipeline management is performed by the model risk leadership team using the annual validation schedule. New model submissions and out-of-cycle revalidations are tracked individually; the aggregate pipeline demand against available validator headcount is not projected systematically, creating capacity surprises within the year.
Solution: Agent reads the scheduled revalidation calendar, new model submission pipeline from development teams, and planned model change notifications. It projects monthly validation demand against current validator capacity, identifies months where demand exceeds capacity, and delivers the 12-month capacity plan to the Chief Model Risk Officer for resource planning.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
Model risk reporting
Model risk reporting delivers the periodic view of the model risk environment to the Model Risk Committee, board risk committee, and regulatory supervisors. The report covers inventory status, validation pipeline, finding severity distribution, ongoing monitoring outcomes, and key model risk metrics (proportion of models with current validation, proportion with lapsed monitoring, material finding count by category). Under SR 11-7 and EBA guidelines, model risk must be treated as a distinct risk type with formal governance and reporting. Supervisors expect to see evidence of portfolio-level model risk management — not merely individual model approval records.
Lens
Scenario
Intent
Complexity

### CARD 10 [Insights|S] Model Risk Appetite Metric Watch
urn: urn:financial-services:scenario:risk-control/model-risk/model-risk-reporting/model-risk-appetite-metric-watch
intent: Agent monitors the bank's model risk appetite metrics — proportion of models with current validation, proportion with lapsed monitoring, material finding count — on a monthly basis and alerts the Chief Model Risk Officer when any metric approaches its appetite threshold.
Problem to solve: Model risk appetite metrics are reported to the Model Risk Committee on a quarterly basis. A metric approaching its appetite threshold during the inter-committee period is not signalled until the next quarterly pack is prepared, limiting the function's ability to take preventive action.
Solution: Agent reads the model inventory, validation pipeline, and monitoring status monthly, computes the risk appetite metrics, and delivers an automated alert when any metric is within 10 percentage points of its appetite threshold. The Chief Model Risk Officer receives the alert with the contributing models listed for prioritisation.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 11 [Insights|M] Model Risk Portfolio Reporting
urn: urn:financial-services:scenario:risk-control/model-risk/model-risk-reporting/model-risk-portfolio-reporting
intent: Agent clusters validation findings and performance metrics across the model portfolio, identifies systemic patterns and correlated deterioration, and assembles the Model Risk Committee pack.
Problem to solve: Validation findings arrive sequentially per model; the Model Risk Committee reviews each individually, and systemic weaknesses visible in aggregate — documentation gaps, shared data lineage issues, recurring ML conceptual soundness challenges — surface only when a validator notices the pattern. Per-model performance monitoring is produced by individual owners in varying formats; correlated deterioration across models is not visible until each report is reviewed separately.
Solution: Agent reads completed validation reports and performance data across the active portfolio, standardizes metrics by model class, clusters findings by category and model family, and identifies systemic patterns and correlated deterioration. It assembles the Model Risk Committee pack covering portfolio coverage, validation pipeline status, finding severity distribution, and monitoring outcomes. The Chief Model Risk Officer reviews and adds forward judgement before distribution.
OKR objective: The Model Risk Committee reviews an agent-assembled portfolio pack — with validation findings clustered by category, correlated performance deterioration identified, and systemic patterns flagged — alongside individual model approval decisions.
OKR KR [Adoption]: Agent used to assemble the Model Risk Committee portfolio pack for ≥4 consecutive quarterly meetings within 18 months of go-live; finding clustering and correlated deterioration detection applied to 100% of the active validation pipeline in every run.
OKR KR [Acceptance]: ≥75% of systemic patterns identified by the agent rated as actionable by the Chief Model Risk Officer; correlated deterioration patterns identified by the agent lead to ≥1 thematic remediation workstream per annual cycle.
OKR KR [Cycle]: Model Risk Committee pack assembly completed within 2 business days of final quarterly validation report receipt, versus ≥5 analyst-days of manual aggregation and formatting under the prior approach.

### CARD 12 [Automation|M] Model Risk Regulatory Reporting Pack
urn: urn:financial-services:scenario:risk-control/model-risk/model-risk-reporting/model-risk-regulatory-reporting-pack
intent: Agent assembles the SR 11-7 and EBA model risk reporting pack for the supervisory review process — inventory coverage, validation pipeline, material findings, and monitoring status — from the model risk management system for the Chief Model Risk Officer's review and submission.
Problem to solve: Supervisory model risk reporting requires assembling inventory metrics, validation pipeline status, and material finding counts in the prescribed format. The assembly draws on the model risk management system, validation report archive, and monitoring records; manual compilation across these sources consumes the model risk reporting function's time before each supervisory submission cycle.
Solution: Agent reads the model inventory, validation pipeline, and monitoring status records. It computes the prescribed metrics — proportion of models with current validation, proportion in monitoring, material finding count by severity — and assembles the supervisory reporting pack in the required format. The Chief Model Risk Officer reviews and submits.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
GenAI-enabled Banking and Financial Services Framework · v11i
