# 

source: html-alt/financial-services/en/banking-data-analytics/index.html


[PAGE TEXT]
Operational data
Master & reference data (18)
Customer product master
Golden record management (3)
·
Customer master data (3)
·
Product & account master (3)
Reference lookup data
Reference & code tables (3)
·
Data quality & MDM governance (3)
·
Data catalog & stewardship (3)
Risk & regulatory data
Regulatory data (16)
Reporting datasets
Regulatory reporting datasets (3)
·
Supervisory data submissions (4)
·
Regulatory change data management (3)
Lineage bcbs239
Data lineage & BCBS 239 compliance (3)
·
Data residency & localization controls (3)
Data governance
Data Cycles (20)
Stewardship & quality
Data quality assessment cycle (BCBS 239) (5)
Master & reference data stewardship cycle (5)
Lineage & control attestation cycle (5)
Submission & disclosure
Regulatory data submission cycle (5)
Operational data
Customer data (15)
Customer 360 identity
Customer identity & KYC data (3)
·
Customer 360 profile (3)
·
Segmentation & behavioural data (3)
Consents relationship history
Consent & privacy records (3)
·
Relationship & interaction history (3)
Operational data
Transaction data (15)
Payments movement data
Payment & transfer records (3)
·
Transaction enrichment & categorisation (3)
·
Card & merchant data (3)
Transaction enrichment lineage
Transaction lineage & reconciliation (3)
·
Transaction analytics & patterns (3)
Operational data
Market data (15)
Pricing rates
Pricing & rates feeds (3)
·
FX & benchmark rates (3)
·
Curve construction & interpolation (3)
External feeds indices
External index & macro data (3)
·
Market data quality & vendor management (3)
Risk & regulatory data
Credit & exposure data (15)
Loan level exposure
Loan-level exposure records (3)
·
Counterparty & group exposure (3)
·
Credit parameter inputs (PD/LGD/EAD) (3)
Collateral risk inputs
Collateral & security data (3)
·
ECL & provision data (3)
Risk & regulatory data
Risk & position data (15)
Risk metrics sensitivities
Trading book positions (3)
·
Risk metrics & sensitivities (3)
·
Stress & scenario data (3)
Position limit data
Limit & headroom data (3)
·
Liquidity & funding data (3)
Scenarios
Lens
Scenario
Intent
Complexity

### CARD 1 [Automation|S] Data Quality Remediation Workflow
urn: urn:financial-services:scenario:banking-data-analytics/data-quality-remediation-workflow
intent: Agent detects CDE quality failures across the enterprise data catalog, routes each failure to the responsible data steward with a pre-populated remediation ticket, and tracks resolution status for the data governance council. The data steward resolves the underlying data issue; the agent handles routing, tracking, and escalation on SLA breach. Governance council receives a weekly open-items summary by steward and domain.
Problem to solve: CDE quality failures are detected by monitoring rules and logged in the data quality platform, but routing each failure to the responsible steward and tracking remediation to closure are manual steps. Failures accumulate unresolved when routing is delayed. The governance council has no automated view of open remediation items between its scheduled cycles.
Solution: Agent reads open quality failures from the data quality platform, matches each failure to the responsible steward from the CDE registry, and creates a pre-populated remediation ticket with failure context, affected downstream reports, and SLA deadline. It tracks each ticket through to closure and escalates on SLA breach. The weekly open-items summary for the governance council is generated from the same tracking state.
OKR objective: CDE quality failures are routed to responsible data stewards with pre-populated remediation tickets, tracked to closure with automated SLA escalation, and reported to the governance council on a weekly cadence.
OKR KR [Adoption]: Agent routes ≥ 95% of detected quality failures to the correct steward within 1 business day of detection; weekly open-items summary delivered to the governance council for ≥ 50 consecutive weeks within the first 12 months.
OKR KR [Acceptance]: ≥ 90% of ticket routings confirmed as correctly assigned by receiving stewards; SLA escalations triggered accurately for ≥ 95% of breaches as validated at quarterly governance council review.
OKR KR [Cycle]: Average time from quality failure detection to steward ticket receipt reduced from manual aggregation cycles (typically days) to ≤ 1 business day per failure event.

### CARD 2 [Insights|S] Cross-Domain Data Quality Posture
urn: urn:financial-services:scenario:banking-data-analytics/cross-domain-data-quality-posture
intent: Agent synthesises CDE quality health across all seven data domains — master reference, customer, transaction, market, credit-exposure, risk-position, and regulatory — into a single executive scorecard for the CDO and data governance council. Quality deterioration in one domain can propagate to downstream regulatory and risk processes before the CDO's attention is drawn to the cross-domain picture. The CDO uses the scorecard for governance reporting and remediation budget allocation.
Problem to solve: CDE quality monitoring operates independently within each data domain; the CDO has no consolidated view across the full data estate. Board reporting on data quality relies on manual aggregation from domain-level reports with no common scoring baseline, and the aggregation is performed retrospectively rather than on a continuous cadence. The absence of a cross-domain view delays the CDO's identification of systemic quality deterioration.
Solution: Agent reads CDE quality metrics from all domain monitoring platforms — completeness, accuracy, timeliness, and consistency scores by domain — and produces a cross-domain quality posture scorecard. It ranks domains by overall CDE health, surfaces the highest-severity degradations across the estate, and generates the board-level data quality narrative with trend analysis over the prior three cycles. The CDO presents the scorecard at the data governance council and uses it as the basis for remediation budget allocation.
OKR objective: The CDO and data governance council hold a consolidated, continuously updated quality posture view across all seven data domains, enabling remediation budget allocation and board reporting from a single scored source.
OKR KR [Adoption]: Agent produces the cross-domain quality scorecard for ≥ 12 consecutive monthly governance council cycles within the first year; all seven data domains included in each cycle.
OKR KR [Acceptance]: ≥ 85% of highest-severity domain degradations flagged by the agent rated as requiring priority remediation by the CDO; board-level data quality narratives accepted without material revision in ≥ 80% of cycles.
OKR KR [Cycle]: Cross-domain scorecard preparation time reduced from manual multi-domain aggregation (typically 1–2 weeks) to ≤ 1 business day per monthly cycle.

### CARD 3 [Insights|M] Cross-Functional Case Taxonomy
urn: urn:financial-services:scenario:banking-data-analytics/unified-case-taxonomy-across-functions
intent: Agent maps case labels from customer service, operations, risk, and complaints to a unified taxonomy using semantic analysis, enabling management to query cross-functional issue patterns without manual reconciliation exercises. The CDO and COO use the cross-functional dashboard for operational decision-making. The data governance team maintains the unified taxonomy as the canonical reference.
Problem to solve: Each business function labels cases under its own taxonomy: an authorisation failure registers as "Card Decline" in customer service, "Authorization Failure" in operations, "Fraud Investigation Required" in risk, and "Card Service Issue" in complaints. Cross-functional analysis of institution-wide issue patterns requires periodic manual reconciliation exercises. Management has no continuous view of case patterns across functions.
Solution: Agent reads case data from customer service, operations, risk, and complaints systems and maps each label to the unified taxonomy using semantic analysis of label text and case descriptions. It produces a cross-functional dashboard showing issue frequency and resolution patterns by unified category. The governance team maintains the taxonomy; the dashboard is refreshed on a continuous basis as new cases are classified.
OKR objective: The CDO and COO access a cross-functional case dashboard mapping customer service, operations, risk, and complaints labels to a unified taxonomy through agent-driven semantic analysis, enabling institution-wide issue pattern monitoring without manual reconciliation.
OKR KR [Adoption]: Agent maps case labels to the unified taxonomy on a continuous basis covering all four source functions from go-live; dashboard refreshed within 24 hours of new case classification for ≥ 95% of case volume within 12 months.
OKR KR [Acceptance]: ≥ 85% of cross-functional taxonomy mappings confirmed as accurate by the data governance team at quarterly taxonomy validation; management cross-functional pattern queries satisfied without additional manual reconciliation in ≥ 80% of cases.
OKR KR [Cycle]: Cross-functional issue pattern analysis cycle reduced from periodic manual reconciliation exercises (typically monthly or quarterly) to a continuous dashboard updated within 24 hours.

### CARD 4 [New opps|M] Data Mesh Domain API Registry
urn: urn:financial-services:scenario:banking-data-analytics/data-mesh-domain-api-registry
intent: Agent maintains a searchable registry of data product APIs published by domain teams, generating interface descriptions, usage guidance, and SLA summaries from API schema and usage telemetry. Data consumers across the bank query the registry in natural language to identify the right data product for their use case. The CDO monitors domain data product maturity and adoption through the registry.
Problem to solve: As domain teams publish data products through APIs, consumers have no reliable way to discover what products exist, what their schemas mean, or what quality commitments they carry. Discovery relies on peer networks and tribal knowledge, constraining adoption of domain data products beyond the originating team. The CDO has no consolidated view of data product maturity across the domain landscape.
Solution: Agent reads API schema definitions, endpoint telemetry, and SLA logs published by domain teams and generates a human-readable registry entry per data product — available endpoints, field definitions, freshness guarantees, and historical SLA compliance. Consumers query the registry in natural language; the CDO uses it to assess domain data product adoption and maturity. Registry entries are refreshed as schema and telemetry data are updated.
OKR objective: Data consumers across the bank discover and assess domain data products through a searchable registry maintained by agent from API schema and usage telemetry, with interface descriptions, usage guidance, and SLA summaries available in natural-language query form.
OKR KR [Adoption]: Registry covers ≥ 90% of published domain data product APIs within 12 months; registry entries refreshed within 48 hours of schema or telemetry updates for ≥ 95% of products.
OKR KR [Acceptance]: ≥ 80% of natural-language queries return the correct data product reference as assessed by the CDO data governance team; SLA summaries validated against vendor telemetry in ≥ 90% of entries.
OKR KR [Cycle]: Data product discovery time for consumers reduced from peer-network queries (typically 1–3 days) to a same-session registry query with ≤ 5 minutes to actionable product reference.

### CARD 5 [Enablement|L] Enterprise Data Self-Service
urn: urn:financial-services:scenario:banking-data-analytics/enterprise-data-self-service
intent: Agent resolves natural-language questions from executive and analytical users against the bank's data estate, spanning BI warehouse layers and operational system records. Each answer is sourced and reproducible, with metric definitions and data lineage attached to the response. The CDO governs scope, access controls, and the semantic layer that standardises metric definitions across the estate.
Problem to solve: Senior executives and analysts submit structured and ad hoc questions that require querying across multiple systems; each cycle returns days later as a report or one-off query output. Strategic decisions are taken on incomplete information when the data retrieval cycle outlasts the decision window. Data team capacity is consumed by retrieval work that does not require professional judgment.
Solution: Agent accepts a natural-language question, selects the appropriate source — BI warehouse for standard metrics, operational system APIs for live positions and exposures — and executes the query under approved read-only access. Multi-step questions are decomposed and resolved across systems in a single interaction. The response includes the query logic applied, metric definitions, and a data lineage reference.
OKR objective: Executive and analytical users resolve natural-language questions against the bank's data estate within the same working session, with each answer sourced, reproducible, and linked to metric definitions and data lineage under CDO-governed access controls.
OKR KR [Adoption]: Agent handles ≥ 200 executive and analyst queries per month within 12 months of go-live; BI warehouse and operational system API sources both active in production.
OKR KR [Acceptance]: ≥ 85% of query responses accepted by requesting users as analytically accurate without manual re-derivation; metric definition and lineage references validated as correct in ≥ 90% of sampled responses.
OKR KR [Cycle]: Time from question submission to response reduced from days (data team request cycle) to ≤ 30 minutes per query within a single working session.

[PAGE TEXT]
GenAI-enabled Banking and Financial Services Framework · v11i
