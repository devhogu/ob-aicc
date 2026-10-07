# Model risk

Model risk is the potential for adverse consequences from decisions based on models that are incorrect or misused. Under model-risk guidance such as SR 11-7, every model in use is inventoried, validated by an independent function, and monitored for performance on a continuous basis. The model inventory spans credit risk (PD, LGD, EAD, IFRS 9 staging), market risk (VaR, Greeks), liquidity stress, AML transaction monitoring, fraud scoring, and increasingly, machine learning models. **The GenAI opportunity is to automate the governance overhead** — inventory reconciliation, validation finding synthesis, and performance monitoring — while enabling the model risk function to cover more models per cycle with the same headcount.

## Problems

### Model lifecycle & validation {#model-lifecycle-validation}

| Lens | Problem |
| --- | --- |
| Insights & analytics | Model validation findings across the portfolio arrive sequentially — one validation report per model — and the Model Risk Committee reviews each individually. Systemic weaknesses visible only in aggregate — a consistent documentation gap across retail PD models, a shared data lineage issue in IFRS 9 staging models, a recurring conceptual soundness challenge in machine learning models — surface only when a validator notices the pattern across several reports. |
| Enablement | Model inventory maintenance — reconciling the inventory register against production deployments to identify shadow models and stale validation records — requires analysts to cross-reference the model inventory against technology deployment records, data science code repositories, and vendor contract registers. The exercise reveals gaps; addressing them requires the model risk team to initiate validation and remediation workflows across the originating business units. |
| Automation | Model Risk Committee packs — inventory status, validation pipeline, finding severity distribution, and annual validation coverage — are assembled manually from model risk management system exports each cycle. The format is consistent; the data is structured. |
| New business opportunities | A model risk function with systematic inventory reconciliation and portfolio-level finding synthesis can demonstrate compliance with model-risk guidance to supervisors with evidence that goes beyond the individual model validation report. That portfolio governance maturity is increasingly assessed in regulatory model risk reviews; gaps — particularly shadow models and lapsed validations — carry capital implications and enforcement risk. |

## Model inventory & governance {#model-inventory-governance}

The model inventory is the master register of every model in production use — covering the model's purpose, owner, development date, validation status, approval decision, and monitoring plan. Model-risk guidance expects the inventory to be comprehensive and current; supervisors expect to be able to walk from a business decision to the models informing it and from each model to its validation history. Shadow models — spreadsheet tools and vendor outputs that function as models but are not registered — are the most common inventory gap identified in regulatory model risk reviews. Maintaining a current, accurate inventory requires systematic reconciliation against technology and vendor records.

### Model Inventory & Documentation Completeness Check

- URN: urn:financial-services:scenario:risk-control/model-risk/model-inventory-governance/model-inventory-documentation-completeness
- Lens: Automation
- Complexity: S
- Intent: The AI agent scans the model inventory against the MRM policy documentation standard, flags gaps per model, and generates the completeness report for the Chief Model Risk Officer.
- Problem to solve: Model documentation completeness — development documentation, validation reports, approval records, and ongoing monitoring plans — is reviewed manually against the MRM policy standard. With 80–200 models in a typical bank's inventory, the completeness audit is a periodic exercise that misses interim gaps between review cycles.
- Solution: The AI agent reads the model inventory and associated documentation repositories, applies the MRM policy schema as a completeness checklist, flags missing or stale documents per model, and produces a completeness report ranked by regulatory priority. The Chief Model Risk Officer reviews gaps and assigns owners for remediation.
- OKR: The Chief Model Risk Officer manages model documentation completeness from an AI-generated completeness report — applying the MRM policy standard across the full inventory — rather than a periodic manual audit.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's completeness check runs across 100% of model inventory entries at least quarterly within 6 months of go-live; MRM policy schema applied as the completeness checklist in every run from go-live. |
| Acceptance | ≥85% of AI-flagged documentation gaps confirmed as genuine by the Chief Model Risk Officer on review; interim documentation gap rate between annual reviews reduced by ≥50% versus the prior periodic audit approach. |
| Cycle | Full inventory completeness report delivered within 3 business days of inventory data cut, enabling gap remediation to begin within the same reporting month rather than at annual review. |

### Model Inventory Annual Attestation Support

- URN: urn:financial-services:scenario:risk-control/model-risk/model-inventory-governance/model-inventory-annual-attestation
- Lens: Enablement
- Complexity: S
- Intent: The AI agent pre-populates the annual model inventory attestation form for each model owner — summarizing current status, validation history, monitoring plan, and outstanding findings — reducing the per-owner completion time and improving attestation response rates.
- Problem to solve: Annual model inventory attestation requires each model owner to confirm and update their model's details. Low response rates and incomplete submissions are common; the model risk function spends significant time chasing owners and reconciling incomplete attestations before the inventory certification is complete.
- Solution: The AI agent reads current inventory records for each model and pre-populates the attestation form with the current status, validation date, monitoring plan citation, and open finding count. Model owners receive a pre-populated form requiring only confirmation or update rather than a blank template, reducing the completion burden. The Chief Model Risk Officer reviews exceptions before certification.
- OKR: Model owners confirm or update a pre-populated annual attestation form — current status, validation date, monitoring plan citation, and open finding count — and the Chief Model Risk Officer reviews only exceptions before inventory certification.

| Dimension | Key result |
| --- | --- |
| Adoption | Attestation forms pre-populated by the AI agent issued for 100% of inventoried models in the next annual attestation cycle within 12 months of go-live; all four form sections populated from current inventory records in every form. |
| Acceptance | ≥90% of model owners return the attestation complete on first submission; ≥85% of pre-populated fields confirmed by model owners without correction. |
| Cycle | Annual inventory certification completed within 4 weeks of attestation launch, versus ≥8 weeks of chasing owners and reconciling incomplete attestations under the prior approach. |

### Shadow Model Identification Scan

- URN: urn:financial-services:scenario:risk-control/model-risk/model-inventory-governance/shadow-model-identification
- Lens: Insights
- Complexity: L
- Intent: The AI agent scans business unit systems and shared drives for spreadsheet tools and vendor outputs that meet the model definition in model-risk guidance, identifies items not registered in the model inventory, and delivers a shadow model candidates list to the Chief Model Risk Officer.
- Problem to solve: Shadow models — spreadsheet tools and vendor outputs that function as models but are not registered in the inventory — are the most common inventory gap identified in regulatory model risk reviews. Identifying these requires systematic scanning of business unit systems; the current approach relies on business units self-reporting, which systematically underestimates the shadow model population.
- Solution: The AI agent scans metadata from business unit shared drives and finance system exports, applies the model definition criteria from model-risk guidance to identify files that function as quantitative tools producing outputs used in business decisions, and cross-references each candidate against the registered model inventory. The Chief Model Risk Officer reviews the candidate list and initiates inventory onboarding for confirmed shadow models.
- OKR: The Chief Model Risk Officer receives a shadow model candidates list — spreadsheet tools and vendor outputs that meet the model definition but are not registered in the inventory — from a systematic scan rather than business unit self-reporting.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's scan covers shared drive metadata and finance system exports for 100% of business units at least twice a year within 12 months of go-live; every candidate cross-referenced against the registered model inventory. |
| Acceptance | ≥60% of AI-identified candidates confirmed as shadow models by the Chief Model Risk Officer on review; inventory onboarding initiated for 100% of confirmed shadow models within one quarter. |
| Cycle | Candidates list delivered within 10 business days of scan start, versus identification through business unit self-reporting that systematically underestimates the shadow model population. |

## Model performance monitoring {#model-performance-monitoring}

Ongoing monitoring tracks each model's performance between validation cycles — measuring discrimination (Gini, KS, AUC for classification models), calibration (predicted vs actual default rates, ECL vs realized losses), and stability (PSI, CSI for input distribution shifts). Model-risk guidance expects documented monitoring plans for every model, with defined escalation triggers when performance falls below acceptable bands. Performance deterioration that crosses a materiality threshold triggers an out-of-cycle validation. For credit risk models, performance deterioration often coincides with macroeconomic cycle turns — precisely the moment when the model's outputs are most consequential for capital and provision planning.

### Model Performance Monthly Dashboard

- URN: urn:financial-services:scenario:risk-control/model-risk/model-performance-monitoring/model-performance-monthly-dashboard
- Lens: Automation
- Complexity: M
- Intent: The AI agent assembles the monthly model performance dashboard from owner-submitted monitoring reports, applying consistent metric computation and flagging models that breach defined performance thresholds for the Chief Model Risk Officer.
- Problem to solve: Model-risk guidance expects documented performance monitoring for every model. Model owners submit monitoring outputs in varying formats; the model risk function must standardize metrics, compute aggregate performance indicators, and identify threshold breaches before each monthly reporting cycle — a manual consolidation task across 80–200 models.
- Solution: The AI agent reads monthly monitoring submissions from model owners, standardizes performance metrics by model class (Gini/KS for credit, RMSE for continuous, backtesting exception counts for market risk), flags threshold breaches, and assembles the dashboard in the committee's standard format. The Chief Model Risk Officer reviews flagged models before the committee pack is distributed.
- OKR: The Chief Model Risk Officer reviews flagged models on an AI-assembled monthly performance dashboard — owner-submitted monitoring results standardized by model class, with threshold breaches flagged — before the committee pack is distributed.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent is used to assemble the monthly performance dashboard for ≥11 of 12 monthly cycles within 12 months of go-live; monitoring submissions for 100% of models standardized by model class in every run. |
| Acceptance | ≥90% of AI-flagged threshold breaches confirmed by the Chief Model Risk Officer on review; ≥85% of dashboards distributed in the committee pack without manual recomputation of metrics. |
| Cycle | Dashboard assembled within 2 business days of the model owner submission deadline, versus ≥5 analyst-days of manual consolidation across the model inventory under the prior approach. |

### Model Performance Deterioration Alert

- URN: urn:financial-services:scenario:risk-control/model-risk/model-performance-monitoring/model-performance-deterioration-alert
- Lens: Insights
- Complexity: M
- Intent: The AI agent monitors performance metric trends across the model portfolio between monthly reporting cycles, flagging models whose trajectory indicates an imminent threshold breach before it is surfaced in the next scheduled report.
- Problem to solve: Performance deterioration is identified at the monthly monitoring cycle. A model declining steadily across three months may cross the threshold only in the fourth month; the model risk function has no signal of the developing deterioration during the intervening reporting windows.
- Solution: The AI agent reads performance metric time series across the portfolio, applies trend analysis to identify models on a deteriorating trajectory, and flags models projected to breach performance thresholds within 90 days. The Chief Model Risk Officer receives the trend alert between monthly cycles, enabling proactive validation scheduling.
- OKR: The Chief Model Risk Officer receives a trend alert for every model projected to breach a performance threshold within 90 days, enabling validation to be scheduled before the breach appears in the monthly report.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's trend analysis runs on performance metric time series for 100% of monitored models within 6 months of go-live; projected-breach alerts issued between monthly reporting cycles from go-live. |
| Acceptance | ≥70% of models flagged by the AI agent confirmed by the Chief Model Risk Officer as on a deteriorating trajectory; ≥75% of threshold breaches in the year preceded by one of the AI agent's trend alerts. |
| Cycle | Trend alert delivered up to 90 days before the projected threshold breach, versus identification in the monthly report in which the breach occurs under the prior approach. |

### Model Performance vs Macro Correlation Analysis

- URN: urn:financial-services:scenario:risk-control/model-risk/model-performance-monitoring/model-performance-vs-macro-correlation
- Lens: Insights
- Complexity: M
- Intent: The AI agent cross-references credit model performance metrics with macroeconomic cycle indicators to identify models whose calibration is likely to deteriorate under the current macro outlook, informing the validation prioritization schedule.
- Problem to solve: Credit risk model performance deterioration correlates with macroeconomic cycle turns, but the model risk function's validation prioritization does not systematically factor in macro signals. A model calibrated in a benign credit environment may perform adequately today while the macro environment deteriorates around it; the validation team discovers the misalignment when the performance metric breaches its threshold.
- Solution: The AI agent reads macro indicators — GDP growth, credit spreads, unemployment — alongside monthly model performance metrics for PD, LGD, and ECL models, computes the historical correlation between macro cycle and model performance, and flags models whose performance is historically correlated with the current macro trajectory. The Chief Model Risk Officer uses the output to front-load validation of macro-sensitive models.
- OKR: The Chief Model Risk Officer front-loads validation of macro-sensitive credit models using the AI agent's analysis, which correlates PD, LGD, and ECL model performance with macroeconomic indicators and flags the models exposed to the current macro trajectory.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's macro correlation analysis runs for 100% of PD, LGD, and ECL models at least quarterly within 12 months of go-live; GDP growth, credit spreads, and unemployment indicators read in every run. |
| Acceptance | ≥70% of models flagged as macro-sensitive accepted by the Chief Model Risk Officer for reprioritization in the validation schedule; ≥1 validation per year brought forward on a flag from the AI agent. |
| Cycle | Analysis delivered within 5 business days of each quarterly macro indicator release, versus discovery of the misalignment only when a performance metric breaches its threshold under the prior approach. |

## Model validation {#model-validation}

Model validation is the set of processes and activities intended to verify that models perform as expected and are appropriate for their intended use. Under model-risk guidance, validation is conducted by a function independent of model development and includes conceptual soundness review, outcome analysis, and ongoing monitoring. Validation engagements produce formal reports with findings classified by severity; material findings must be remediated before the model can be approved for expanded use. The volume of models requiring annual or biennial validation often exceeds the capacity of the validation function.

### Model Development Specification Drafting

- URN: urn:financial-services:scenario:risk-control/model-risk/model-validation/model-development-spec-drafting
- Lens: Enablement
- Complexity: M
- Intent: The AI agent drafts the model development specification — conceptual soundness rationale, data lineage, methodology alternatives considered, and back-test design — from the modeler's working notes and data exploration outputs.
- Problem to solve: Model development specifications are drafted by quantitative analysts after the development work is complete, with documentation quality that is inconsistent across the team. Validators frequently return specifications for additional conceptual soundness explanation or data lineage detail, extending the validation cycle and delaying model deployment.
- Solution: The AI agent reads the modeler's working notes, exploratory analysis outputs, and dataset documentation, and drafts the development specification in the Bank's standard template — conceptual soundness argument, data lineage, methodology alternatives, benchmark comparison, and back-test design. The modeler reviews and fills expert judgment sections before submission to model validation.
- OKR: Modelers submit development specifications drafted by the AI agent from working notes and data exploration outputs — covering conceptual soundness, data lineage, methodology alternatives, and back-test design — for expert review rather than producing documentation after development is complete.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent is used to draft model development specifications for ≥70% of new model and material model change submissions within 12 months of go-live; all standard template sections produced by the AI agent in every run from go-live. |
| Acceptance | ≥75% of AI-drafted specifications accepted by model validation without a first-pass return for additional documentation; validation cycle length reduced by ≥20% for AI-documented models versus manually documented peers. |
| Cycle | Development specification draft delivered within 2 business days of modeler working note submission, versus ≥1 week of post-development manual documentation under the prior approach. |

### Model Validation Finding Synthesis

- URN: urn:financial-services:scenario:risk-control/model-risk/model-validation/model-validation-finding-synthesis
- Lens: Insights
- Complexity: M
- Intent: The AI agent reads completed validation reports across a calendar year, clusters findings by category and root cause, and identifies systemic weaknesses in the Bank's model development practices for the Chief Model Risk Officer's annual model risk review.
- Problem to solve: Validation findings are documented in individual reports reviewed by the Model Risk Committee on a model-by-model basis. Systemic weaknesses — documentation shortfalls common to models built by a specific team, or recurring conceptual soundness challenges in a model class — are visible in aggregate but not in the individual report review cycle.
- Solution: The AI agent reads all validation reports completed in the year, extracts finding categories and root causes, clusters them by model family and development team, and identifies systemic patterns. The Chief Model Risk Officer uses the analysis in the annual model risk program review and in targeted developer training planning.
- OKR: The Chief Model Risk Officer bases the annual model risk program review and developer training plan on the AI agent's synthesis of the year's validation findings, clustered by category, root cause, model family, and development team.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's synthesis, covering 100% of validation reports completed in the calendar year, is produced for ≥1 annual model risk review within 18 months of go-live; finding categories and root causes extracted from every report. |
| Acceptance | ≥75% of systemic weaknesses identified by the AI agent rated as actionable by the Chief Model Risk Officer; ≥2 targeted remediation or developer training actions per annual review initiated from the synthesis. |
| Cycle | Annual synthesis delivered within 5 business days of the year's final validation report, versus systemic weaknesses surfacing only when a validator notices the pattern across individual reports. |

### Validation Pipeline Capacity Planning

- URN: urn:financial-services:scenario:risk-control/model-risk/model-validation/validation-pipeline-capacity-planning
- Lens: Automation
- Complexity: M
- Intent: The AI agent projects the validation pipeline demand for the next 12 months — based on scheduled revalidation dates, new model submissions, and model changes — and compares it against available validation capacity, flagging capacity gaps for the Chief Model Risk Officer.
- Problem to solve: Validation pipeline management is performed by the model risk leadership team using the annual validation schedule. New model submissions and out-of-cycle revalidations are tracked individually; the aggregate pipeline demand against available validator headcount is not projected systematically, creating capacity surprises within the year.
- Solution: The AI agent reads the scheduled revalidation calendar, new model submission pipeline from development teams, and planned model change notifications. It projects monthly validation demand against current validator capacity, identifies months where demand exceeds capacity, and delivers the 12-month capacity plan to the Chief Model Risk Officer for resource planning.
- OKR: The Chief Model Risk Officer plans validation resources from an AI-produced 12-month capacity plan that projects monthly validation demand — scheduled revalidations, new model submissions, and model changes — against available validator capacity.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's capacity plan is refreshed at least quarterly within 6 months of go-live; revalidation calendar, new model submission pipeline, and planned model change notifications read in every run. |
| Acceptance | ≥80% of capacity gaps flagged by the AI agent confirmed by the Chief Model Risk Officer; projected monthly validation demand within ±20% of actual demand in ≥75% of months. |
| Cycle | Capacity gaps identified ≥3 months before the month in which demand exceeds capacity, versus capacity surprises arising within the year under the annual validation schedule. |

## Model risk reporting {#model-risk-reporting}

Model risk reporting delivers the periodic view of the model risk environment to the Model Risk Committee, Board Risk Committee, and regulatory supervisors. The report covers inventory status, validation pipeline, finding severity distribution, ongoing monitoring outcomes, and key model risk metrics (proportion of models with current validation, proportion with lapsed monitoring, material finding count by category). Model-risk guidance treats model risk as a distinct risk type with formal governance and reporting. Supervisors expect to see evidence of portfolio-level model risk management — not merely individual model approval records.

### Model Risk Appetite Metric Watch

- URN: urn:financial-services:scenario:risk-control/model-risk/model-risk-reporting/model-risk-appetite-metric-watch
- Lens: Insights
- Complexity: S
- Intent: The AI agent monitors the Bank's model risk appetite metrics — proportion of models with current validation, proportion with lapsed monitoring, material finding count — on a monthly basis and alerts the Chief Model Risk Officer when any metric approaches its appetite threshold.
- Problem to solve: Model risk appetite metrics are reported to the Model Risk Committee on a quarterly basis. A metric approaching its appetite threshold during the inter-committee period is not signaled until the next quarterly pack is prepared, limiting the function's ability to take preventive action.
- Solution: The AI agent reads the model inventory, validation pipeline, and monitoring status monthly, computes the risk appetite metrics, and delivers an automated alert when any metric is within 10 percentage points of its appetite threshold. The Chief Model Risk Officer receives the alert with the contributing models listed for prioritization.
- OKR: The Chief Model Risk Officer is alerted when any model risk appetite metric — proportion of models with current validation, proportion with lapsed monitoring, material finding count — comes within 10 percentage points of its threshold, with the contributing models listed for prioritization.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent computes all model risk appetite metrics monthly within 3 months of go-live; monthly watch run for ≥10 consecutive months in year 1. |
| Acceptance | ≥85% of the AI agent's alerts confirmed by the Chief Model Risk Officer as accurate against inventory and monitoring records; preventive action initiated on ≥75% of alerts before the next Model Risk Committee pack. |
| Cycle | Alert delivered within 3 business days of month-end, versus first visibility in the next quarterly Model Risk Committee pack under the prior approach. |

### Model Risk Portfolio Reporting

- URN: urn:financial-services:scenario:risk-control/model-risk/model-risk-reporting/model-risk-portfolio-reporting
- Lens: Insights
- Complexity: M
- Intent: The AI agent clusters validation findings and performance metrics across the model portfolio, identifies systemic patterns and correlated deterioration, and assembles the Model Risk Committee pack.
- Problem to solve: Validation findings arrive sequentially per model; the Model Risk Committee reviews each individually, and systemic weaknesses visible in aggregate — documentation gaps, shared data lineage issues, recurring ML conceptual soundness challenges — surface only when a validator notices the pattern. Per-model performance monitoring is produced by individual owners in varying formats; correlated deterioration across models is not visible until each report is reviewed separately.
- Solution: The AI agent reads completed validation reports and performance data across the active portfolio, standardizes metrics by model class, clusters findings by category and model family, and identifies systemic patterns and correlated deterioration. It assembles the Model Risk Committee pack covering portfolio coverage, validation pipeline status, finding severity distribution, and monitoring outcomes. The Chief Model Risk Officer reviews and adds forward judgment before distribution.
- OKR: The Model Risk Committee reviews an AI-assembled portfolio pack — with validation findings clustered by category, correlated performance deterioration identified, and systemic patterns flagged — alongside individual model approval decisions.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent is used to assemble the Model Risk Committee portfolio pack for ≥4 consecutive quarterly meetings within 18 months of go-live; finding clustering and correlated deterioration detection applied to 100% of the active validation pipeline in every run. |
| Acceptance | ≥75% of systemic patterns identified by the AI agent rated as actionable by the Chief Model Risk Officer; correlated deterioration patterns identified by the AI agent lead to ≥1 thematic remediation workstream per annual cycle. |
| Cycle | Model Risk Committee pack assembly completed within 2 business days of final quarterly validation report receipt, versus ≥5 analyst-days of manual aggregation and formatting under the prior approach. |

### Model Risk Regulatory Reporting Pack

- URN: urn:financial-services:scenario:risk-control/model-risk/model-risk-reporting/model-risk-regulatory-reporting-pack
- Lens: Automation
- Complexity: M
- Intent: The AI agent assembles the model risk reporting pack for the supervisory review process — inventory coverage, validation pipeline, material findings, and monitoring status — from the model risk management system for the Chief Model Risk Officer's review and submission.
- Problem to solve: Supervisory model risk reporting requires assembling inventory metrics, validation pipeline status, and material finding counts in the prescribed format. The assembly draws on the model risk management system, validation report archive, and monitoring records; manual compilation across these sources consumes the model risk reporting function's time before each supervisory submission cycle.
- Solution: The AI agent reads the model inventory, validation pipeline, and monitoring status records. It computes the prescribed metrics — proportion of models with current validation, proportion with lapsed monitoring, material finding count by severity — and assembles the supervisory reporting pack in the required format. The Chief Model Risk Officer reviews and submits.
- OKR: The Chief Model Risk Officer reviews and submits a supervisory model risk reporting pack — inventory coverage, validation pipeline, material findings by severity, and monitoring status — assembled by the AI agent from the model risk management system in the required format.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent is used to assemble the supervisory reporting pack for 100% of supervisory submission cycles within 12 months of go-live; all prescribed metrics computed from inventory, validation pipeline, and monitoring records in every run. |
| Acceptance | ≥85% of AI-assembled packs submitted by the Chief Model Risk Officer without material amendment; prescribed metrics reconciled to the model inventory in 100% of packs on quality review. |
| Cycle | Reporting pack assembled within 2 business days of the reporting date data cut, versus ≥5 analyst-days of manual compilation across three sources before each submission cycle under the prior approach. |

## AI governance {#ai-governance}

AI governance covers the rules on the Bank's own use of AI: which AI systems are in use, how risky each one is, how each is overseen in operation, and what happens when one fails. Rules on AI, such as the EU Artificial Intelligence Act, commonly classify systems by risk, treat credit assessment of individuals as high risk, and expect human oversight, logging, incident reporting and transparency to customers. Much of this AI is bought, and the Bank answers for it as for its own.

### AI Register Reconciliation & Risk Tier Classification

- URN: urn:financial-services:scenario:risk-control/model-risk/ai-governance/ai-register-risk-tier-classification
- Lens: Automation
- Complexity: M
- Intent: The AI agent keeps the Bank's AI register complete and classified. It reconciles the register against AI platform usage logs, procurement records and vendor release notes to find AI systems not yet listed, proposes a risk tier for each entry from its data, influence on decisions, customer reach and autonomy, and flags systems in categories that rules on AI treat as high risk. The Chief Model Risk Officer confirms each tier.
- Problem to solve: AI enters a bank through many doors: models built in-house, bought software that gains AI features in a routine upgrade, generative AI services used by teams, and AI agents with rights over systems. The AI register is kept by hand from self-reported entries and lags behind actual use, and a risk tier is set once and rarely revisited when the data, the decision or the autonomy changes. A system in a high-risk category, such as credit assessment of individuals, can then run under the controls of a lower tier.
- Solution: The AI agent reads the AI register, AI platform usage logs, procurement and contract records, and vendor release notes, and lists AI use that is not registered. For each entry it records the attributes that set the risk tier — data class, influence on decisions, customer reach and degree of autonomy — proposes the tier with its rationale, and flags high-risk categories and the documentation the tier requires but the entry lacks. The Chief Model Risk Officer confirms or changes each tier, and system owners complete the missing entries.
- OKR: The Chief Model Risk Officer confirms the risk tier of every AI system from an AI-proposed classification with its rationale, and works from an AI register reconciled against actual use rather than self-reported entries.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's reconciliation and classification cover 100% of AI register entries at least quarterly within 6 months of go-live; usage logs, procurement records and vendor release notes read in every run. |
| Acceptance | ≥80% of AI-proposed risk tiers confirmed by the Chief Model Risk Officer without change; ≥70% of unregistered AI uses flagged by the AI agent confirmed as genuine and entered in the register within one quarter. |
| Cycle | Reconciled and classified register delivered within 5 business days of each quarterly data cut, versus a register updated only when owners self-report a new or changed AI system under the prior approach. |

### Human Oversight Evidence Review

- URN: urn:financial-services:scenario:risk-control/model-risk/ai-governance/human-oversight-evidence-review
- Lens: Insights
- Complexity: L
- Intent: The AI agent reads the decision logs of AI-assisted processes and produces a quarterly oversight evidence report for each AI system: how often reviewers accept, correct or override the AI output, how long reviews take, which cases affecting individuals lack a recorded human decision, and where the logs miss what record-keeping requires. The report goes to each system owner and to the Chief Model Risk Officer.
- Problem to solve: Rules on AI and the requirements of each risk tier expect a person to review AI output, a person to decide each case that affects an individual, and logs that prove both. In practice oversight is asserted in a design document rather than measured in operation. A reviewer who accepts nearly every output within seconds provides little oversight, and logs often lack the reviewer, the model version or the final decision. The gap surfaces at an audit, a complaint or an incident, when the evidence can no longer be rebuilt.
- Solution: The AI agent reads the decision logs of each AI system whose risk tier requires human review and computes, by system and reviewer team, acceptance, correction and override rates, review times, and cases affecting individuals without a recorded human decision. It checks each log against the record-keeping fields the tier requires — input, output, model version, reviewer, decision and time — and flags patterns that suggest review in name only. The system owner explains or remedies each flag, and the Chief Model Risk Officer reviews the report.
- OKR: Each AI system owner and the Chief Model Risk Officer receive quarterly evidence, measured from decision logs, that human oversight works as designed, with record-keeping gaps and review-in-name-only patterns flagged for remedy.

| Dimension | Key result |
| --- | --- |
| Adoption | The oversight evidence report is produced quarterly for 100% of AI systems whose risk tier requires human review within 12 months of go-live; the decision logs of every such system read in each run. |
| Acceptance | ≥75% of the AI agent's flags confirmed by system owners as genuine oversight or logging gaps; remedy agreed for 100% of confirmed gaps before the next quarterly report. |
| Cycle | Oversight evidence available within 10 business days of quarter-end, versus evidence rebuilt by hand only when an audit, a complaint or an incident calls for it under the prior approach. |

### AI Incident Detection & Notification Draft

- URN: urn:financial-services:scenario:risk-control/model-risk/ai-governance/ai-incident-detection-notification-draft
- Lens: Automation
- Complexity: L
- Intent: The AI agent watches the monitoring alerts, logs and complaints linked to the Bank's AI systems for signs of an AI incident — harmful or biased output, drift beyond alert levels, an AI agent acting beyond its permissions, data leaking through a prompt. It opens a record in the Bank's incident process marked as AI-related and drafts the incident report and, where needed, the notification to the regulator for the compliance officer's decision.
- Problem to solve: AI incidents rarely announce themselves. A model that drifts, a chat assistant that quotes wrong product terms, or an AI agent that acts outside its permissions shows up as scattered signals: a monitoring alert, a rise in overrides, a few complaints. Incident teams classify these as ordinary IT or service events and miss the AI aspect, while the time limits for reporting serious incidents, which rules on AI commonly set in days, are already running. The lessons then never reach the risk tier or the controls of the AI system.
- Solution: The AI agent reads monitoring alerts, override and correction rates, AI agent action logs and customer complaints for each registered AI system, links related signals to the system and its risk tier, and opens an incident record marked as AI-related with the evidence attached. For an incident that may be serious, it drafts the incident report and the regulator notification in the required structure. The incident manager classifies the incident, the compliance officer decides whether the regulator is notified, and the Chief Model Risk Officer reassesses the risk tier.
- OKR: The incident manager and the compliance officer receive AI incidents identified from linked monitoring, log and complaint signals, with the incident report and regulator notification drafted for decision within the reporting time limit.

| Dimension | Key result |
| --- | --- |
| Adoption | Detection covers 100% of registered AI systems with monitoring in place within 9 months of go-live; every incident linked to an AI system recorded as AI-related from go-live. |
| Acceptance | ≥70% of AI incidents opened by the AI agent confirmed by the incident manager; ≥85% of AI-drafted regulator notifications used by the compliance officer without material amendment. |
| Cycle | AI incident record opened within 4 hours of the first linked signal and draft notification ready within 1 business day of classification as serious, versus recognition of the AI aspect only at post-incident review under the prior approach. |

### Third-Party AI Due Diligence

- URN: urn:financial-services:scenario:risk-control/model-risk/ai-governance/third-party-ai-due-diligence
- Lens: Enablement
- Complexity: M
- Intent: The AI agent prepares the AI section of the third-party risk assessment for each provider of AI or of software with AI features: where data is processed and kept, whether the provider may train on the Bank's data, which model is in use and how changes are notified, what testing evidence exists, and the fallback and exit terms. The third-party risk manager and the information security and data protection reviewers decide.
- Problem to solve: Most AI in a bank arrives from providers: credit scoring engines, fraud tools, chat assistants, and standard software that adds AI features in an upgrade. A bank answers for that AI as for its own, yet vendor questionnaires seldom ask the questions that matter for AI, and contracts, model documentation and data-processing terms are long and differ by provider. Reviewers miss a clause that permits training on customer data, a model change made without notice, or the absence of a workable fallback when the service fails.
- Solution: The AI agent reads the provider's contract, data-processing terms, model documentation, security attestations and questionnaire answers, and fills the AI section of the assessment, citing the clause or page behind each answer and flagging gaps against the Bank's provider requirements: data location, training on Bank data, notice of model changes, testing evidence, access to logs, fallback and exit. It drafts follow-up questions for the provider. The reviewers verify the cited answers, and the third-party risk manager records whether the provider is approved.
- OKR: The third-party risk manager and the information security and data protection reviewers decide on each AI provider from an AI-prepared assessment that cites the contract or document behind every answer and flags each gap.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-prepared assessments used for 100% of new AI providers and for every reassessment, change of terms or change of model within 9 months of go-live. |
| Acceptance | ≥85% of the AI agent's cited answers confirmed by reviewers against the source document; ≥75% of flagged gaps confirmed as genuine and raised with the provider. |
| Cycle | AI section of the assessment ready within 3 business days of receipt of the provider's documents, versus 2–3 weeks of manual review of contracts and questionnaires under the prior approach. |

### Customer AI Disclosure & Decision Explanation

- URN: urn:financial-services:scenario:risk-control/model-risk/ai-governance/customer-ai-disclosure-explanation
- Lens: New opps
- Complexity: M
- Intent: The AI agent gives customers clear notice when they deal with AI and a plain-language explanation when AI informed a decision about them. It checks that every chat assistant, AI-drafted message and AI-assisted decision notice carries the disclosure its risk tier requires, and on request drafts an explanation of the main factors behind a decision, with the route to human review, for the complaint handler to check and send.
- Problem to solve: Rules on AI and on consumer protection commonly expect customers to know when they interact with AI or receive AI-generated content, and to receive an explanation of a decision in which AI played a significant part, with a way to contest it. Disclosures are added channel by channel and drift as scripts and templates change. When a customer asks why a loan was declined or a limit was cut, staff cannot read the model's factors, so the answer is generic and the complaint escalates.
- Solution: The AI agent checks chat assistant scripts, message templates and decision notices against the disclosure that the risk tier of each AI system requires, and lists the gaps for the product owner to correct. When a customer asks about a decision, it reads the decision record and the main factors the model recorded, and drafts a plain-language explanation with the route to human review. The complaint handler checks the draft against the case and sends it, and passes each contest to a person who can change the decision.
- OKR: Customers are told in every channel when they deal with the Bank's AI, and customers who ask about an AI-informed decision receive a plain-language explanation and the route to human review, checked and sent by the complaint handler.

| Dimension | Key result |
| --- | --- |
| Adoption | The disclosure check covers 100% of customer-facing AI channels and templates at least monthly within 6 months of go-live; AI-drafted explanations used for ≥90% of customer requests about AI-informed decisions. |
| Acceptance | ≥85% of AI-drafted explanations sent by the complaint handler without material amendment; ≥90% of disclosure gaps flagged by the AI agent corrected by the product owner within one month. |
| Cycle | Explanation sent within 2 business days of the customer's request, versus a generic reply followed by escalation through the complaints process under the prior approach. |
