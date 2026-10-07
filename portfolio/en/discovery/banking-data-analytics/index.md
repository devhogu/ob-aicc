# Banking Data & Analytics

Banking Data & Analytics is the institution's data foundation — the governed layer of master, customer, transaction, market, credit, risk, and regulatory data that every business function consumes. Aligned to DAMA-DMBOK data management principles, the BCBS 239 principles for risk data aggregation, and the FIBO financial industry ontology, this domain defines how the Bank acquires, governs, and serves authoritative data across the enterprise. Data quality dimensions — completeness, accuracy, timeliness, consistency, validity, and uniqueness — and critical data elements (CDEs) with documented lineage underpin every downstream decision. **The GenAI opportunity is to automate data-quality monitoring across CDEs, enrich data assets through NLP-driven cataloging and lineage mapping, and deliver self-service analytics to data consumers** — compressing the cycle from data-quality event to remediation and from data request to insight from days to hours.

## Problems

### Operational data {#operational-data}

| Lens | Problem |
| --- | --- |
| Insights & analytics | Master, customer, transaction, and market data are each monitored within their own domain reporting cycle. The CDO lacks a consolidated view of data-quality dimension scores — completeness, accuracy, timeliness — across the full operational data estate; degradation in a CDE surfaces only when a downstream analytics process fails or a regulatory submission is queried. Cross-domain quality patterns, such as customer master duplication amplifying transaction enrichment errors, are not detected systematically. |
| Enablement | Data consumers across risk, finance, and customer analytics teams assemble their own working datasets from source system extracts. The Bank's data catalog covers a fraction of the production data estate; undocumented fields, unknown lineage, and stale business definitions force analysts to reverse-engineer data semantics before substantive analysis can begin. |
| Automation | Golden-record deduplication, reference-data refresh cycles, transaction enrichment, and market-data quality checks are executed on fixed, manually triggered cycles. Each process follows a defined rule set applied to structured inputs — the pattern is repeatable and volume-intensive, making each a candidate for continuous AI-driven execution. |
| New business opportunities | A continuously governed operational data estate — golden records maintained in near-real time, enriched transactions feeding analytics within hours, market data quality alerts firing before downstream systems consume errors — creates an analytical infrastructure that enables faster product decisions, better credit underwriting, and richer customer analytics than peers operating on batch data cycles can achieve. |

## Overview

### Master & reference data {#master-reference-data}

- Group: Operational data

| Sub-group | Items |
| --- | --- |
| Customer & product master | golden-record-management, customer-master-data, product-account-master |
| Reference & lookup data | reference-code-tables, data-quality-mdm-governance, data-catalog-stewardship |

### Regulatory data {#regulatory-data}

- Group: Risk & regulatory data

| Sub-group | Items |
| --- | --- |
| Reporting datasets | regulatory-reporting-datasets, supervisory-data-submissions, regulatory-change-data-management |
| Lineage & BCBS 239 | data-lineage-bcbs239, data-residency-localization |

### Data Cycles {#data-cycles}

- Group: Data governance

| Section | List name | Flows |
| --- | --- | --- |
| Stewardship & quality | Stewardship & quality | data-quality-assessment-cycle, master-reference-data-cycle, lineage-control-attestation-cycle |
| Submission & disclosure | Submission & disclosure | regulatory-data-submission-cycle |

### Customer data {#customer-data}

- Group: Operational data

| Sub-group | Items |
| --- | --- |
| Customer 360 & identity | customer-identity-kyc-data, customer-360-profile, segmentation-behavioural-data |
| Consents & relationship history | consent-privacy-records, relationship-interaction-history |

### Transaction data {#transaction-data}

- Group: Operational data

| Sub-group | Items |
| --- | --- |
| Payments & movement data | payment-transfer-records, transaction-enrichment-categorisation, card-merchant-data |
| Transaction lineage & analytics | transaction-lineage-reconciliation, transaction-analytics-patterns |

### Market data {#market-data}

- Group: Operational data

| Sub-group | Items |
| --- | --- |
| Pricing & rates | pricing-rates-feeds, fx-benchmark-rates, curve-construction-interpolation |
| External feeds & indices | external-index-macro-data, market-data-quality-vendor |

### Credit & exposure data {#credit-exposure-data}

- Group: Risk & regulatory data

| Sub-group | Items |
| --- | --- |
| Loan-level exposure | loan-level-exposure-records, counterparty-group-exposure, credit-parameter-inputs |
| Collateral & provisions | collateral-security-data, ecl-provision-data |

### Risk & position data {#risk-position-data}

- Group: Risk & regulatory data

| Sub-group | Items |
| --- | --- |
| Risk metrics & sensitivities | trading-book-positions, risk-metrics-sensitivities, stress-scenario-data |
| Limits & liquidity data | limit-headroom-data, liquidity-funding-data |

## Scenarios

### Data Quality Remediation Workflow

- URN: urn:financial-services:scenario:banking-data-analytics/data-quality-remediation-workflow
- Lens: Automation
- Complexity: S
- Intent: The AI agent picks up CDE quality failures that the data quality platform logs across the enterprise data catalog, routes each failure to the responsible data steward with a pre-populated remediation ticket, and tracks resolution status for the data governance council. The data steward resolves the underlying data issue; the AI agent handles routing, tracking, and escalation on SLA breach. The governance council receives a weekly open-items summary by steward and domain.
- Problem to solve: CDE quality failures are detected by monitoring rules and logged in the data quality platform, but routing each failure to the responsible steward and tracking remediation to closure are manual steps. Failures accumulate unresolved when routing is delayed. The governance council has no automated view of open remediation items between its scheduled cycles.
- Solution: The AI agent reads open quality failures from the data quality platform, matches each failure to the responsible data steward from the CDE registry, and creates a pre-populated remediation ticket with failure context, affected downstream reports, and SLA deadline. The data steward resolves the underlying data issue; the AI agent tracks each ticket through to closure and escalates on SLA breach. The weekly open-items summary for the governance council is generated from the same tracking state.
- OKR: CDE quality failures are routed to responsible data stewards with pre-populated remediation tickets, tracked to closure with automated SLA escalation, and reported to the governance council on a weekly cadence.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent routes ≥ 95% of detected quality failures to the correct steward within 1 business day of detection; weekly open-items summary delivered to the governance council for ≥ 50 consecutive weeks within the first 12 months. |
| Acceptance | ≥ 90% of ticket routings confirmed as correctly assigned by receiving stewards; SLA escalations triggered accurately for ≥ 95% of breaches as validated at quarterly governance council review. |
| Cycle | Average time from quality failure detection to steward ticket receipt reduced from manual routing (typically days) to ≤ 1 business day per failure event. |

### Cross-Domain Data Quality Posture

- URN: urn:financial-services:scenario:banking-data-analytics/cross-domain-data-quality-posture
- Lens: Insights
- Complexity: S
- Intent: The AI agent synthesizes CDE quality health across all seven data domains — master reference, customer, transaction, market, credit-exposure, risk-position, and regulatory — into a single executive scorecard for the CDO and data governance council. Quality deterioration in one domain can propagate to downstream regulatory and risk processes before the CDO's attention is drawn to the cross-domain picture. The CDO uses the scorecard for governance reporting and remediation budget allocation.
- Problem to solve: CDE quality monitoring operates independently within each data domain; the CDO has no consolidated view across the full data estate. Board reporting on data quality relies on manual aggregation from domain-level reports with no common scoring baseline, and the aggregation is performed retrospectively rather than on a regular cadence. The absence of a cross-domain view delays the CDO's identification of systemic quality deterioration.
- Solution: The AI agent reads CDE quality metrics from all domain monitoring platforms — completeness, accuracy, timeliness, and consistency scores by domain — and produces a monthly cross-domain quality posture scorecard. It ranks domains by overall CDE health, surfaces the highest-severity degradations across the estate, and generates the board-level data quality narrative with trend analysis over the prior three cycles. The CDO presents the scorecard at the data governance council and uses it as the basis for remediation budget allocation.
- OKR: The CDO and data governance council hold a consolidated quality posture view across all seven data domains, updated every month, enabling remediation budget allocation and board reporting from a single scored source.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces the cross-domain quality scorecard for ≥ 12 consecutive monthly governance council cycles within the first year; all seven data domains included in each cycle. |
| Acceptance | ≥ 85% of highest-severity domain degradations flagged by the AI agent rated as requiring priority remediation by the CDO; board-level data quality narratives accepted without material revision in ≥ 80% of cycles. |
| Cycle | Cross-domain scorecard preparation time reduced from manual multi-domain aggregation (typically 1–2 weeks) to ≤ 1 business day per monthly cycle. |

### Cross-Functional Case Taxonomy

- URN: urn:financial-services:scenario:banking-data-analytics/unified-case-taxonomy-across-functions
- Lens: Insights
- Complexity: M
- Intent: The AI agent maps case labels from customer service, operations, risk, and complaints to a unified taxonomy using semantic analysis, enabling management to query cross-functional issue patterns without manual reconciliation exercises. The CDO and COO use the cross-functional dashboard for operational decision-making. The data governance team maintains the unified taxonomy as the canonical reference.
- Problem to solve: Each business function labels cases under its own taxonomy: an authorization failure registers as "Card Decline" in customer service, "Authorization Failure" in operations, "Fraud Investigation Required" in risk, and "Card Service Issue" in complaints. Cross-functional analysis of institution-wide issue patterns requires periodic manual reconciliation exercises. Management has no continuous view of case patterns across functions.
- Solution: The AI agent reads case data from customer service, operations, risk, and complaints systems and maps each label to the unified taxonomy using semantic analysis of label text and case descriptions. It produces a cross-functional dashboard showing issue frequency and resolution patterns by unified category. The data governance team maintains the taxonomy and validates the mappings each quarter; the dashboard is refreshed on a continuous basis as new cases are classified.
- OKR: The CDO and COO access a cross-functional case dashboard mapping customer service, operations, risk, and complaints labels to a unified taxonomy through AI-driven semantic analysis, enabling institution-wide issue pattern monitoring without manual reconciliation.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent maps case labels to the unified taxonomy on a continuous basis covering all four source functions from go-live; dashboard refreshed within 24 hours of new case classification for ≥ 95% of case volume within 12 months. |
| Acceptance | ≥ 85% of cross-functional taxonomy mappings confirmed as accurate by the data governance team at quarterly taxonomy validation; management cross-functional pattern queries satisfied without additional manual reconciliation in ≥ 80% of cases. |
| Cycle | Cross-functional issue pattern analysis cycle reduced from periodic manual reconciliation exercises (typically monthly or quarterly) to a continuous dashboard updated within 24 hours. |

### Data Mesh Domain API Registry

- URN: urn:financial-services:scenario:banking-data-analytics/data-mesh-domain-api-registry
- Lens: New opps
- Complexity: M
- Intent: The AI agent maintains a searchable registry of data product APIs published by domain teams, generating interface descriptions, usage guidance, and SLA summaries from API schema and usage telemetry. Data consumers across the Bank query the registry in natural language to identify the right data product for their use case. The CDO monitors domain data product maturity and adoption through the registry.
- Problem to solve: As domain teams publish data products through APIs, consumers have no reliable way to discover what products exist, what their schemas mean, or what quality commitments they carry. Discovery relies on peer networks and tribal knowledge, constraining adoption of domain data products beyond the originating team. The CDO has no consolidated view of data product maturity across the domain landscape.
- Solution: The AI agent reads API schema definitions, endpoint telemetry, and SLA logs published by domain teams and generates a human-readable registry entry per data product — available endpoints, field definitions, freshness guarantees, and historical SLA compliance. Consumers query the registry in natural language; the CDO uses it to assess domain data product adoption and maturity. Registry entries are refreshed as schema and telemetry data are updated, and the CDO's data governance team checks query results and SLA summaries.
- OKR: Data consumers across the Bank discover and assess domain data products through a searchable registry that the AI agent maintains from API schema and usage telemetry, with interface descriptions, usage guidance, and SLA summaries available in natural-language query form.

| Dimension | Key result |
| --- | --- |
| Adoption | Registry covers ≥ 90% of published domain data product APIs within 12 months; registry entries refreshed within 48 hours of schema or telemetry updates for ≥ 95% of products. |
| Acceptance | ≥ 80% of natural-language queries return the correct data product reference as assessed by the CDO's data governance team; SLA summaries validated against endpoint telemetry and SLA logs in ≥ 90% of entries. |
| Cycle | Data product discovery time for consumers reduced from peer-network queries (typically 1–3 days) to a same-session registry query with ≤ 5 minutes to actionable product reference. |

### Enterprise Data Self-Service

- URN: urn:financial-services:scenario:banking-data-analytics/enterprise-data-self-service
- Lens: Enablement
- Complexity: L
- Intent: The AI agent resolves natural-language questions from executive and analytical users against the Bank's data estate, spanning BI warehouse layers and operational system records. Each answer is sourced and reproducible, with metric definitions and data lineage attached to the response. The CDO governs scope, access controls, and the semantic layer that standardizes metric definitions across the estate.
- Problem to solve: Senior executives and analysts submit structured and ad hoc questions that require querying across multiple systems; each cycle returns days later as a report or one-off query output. Strategic decisions are taken on incomplete information when the data retrieval cycle outlasts the decision window. Data team capacity is consumed by retrieval work that does not require professional judgment.
- Solution: The AI agent accepts a natural-language question, selects the appropriate source — BI warehouse for standard metrics, operational system APIs for live positions and exposures — and executes the query under read-only access approved by the CDO. Multi-step questions are decomposed and resolved across systems in a single interaction. The response includes the query logic applied, metric definitions, and a data lineage reference for the requesting user to check.
- OKR: Executive and analytical users resolve natural-language questions against the Bank's data estate within the same working session, with each answer sourced, reproducible, and linked to metric definitions and data lineage under CDO-governed access controls.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent handles ≥ 200 executive and analyst queries per month within 12 months of go-live; BI warehouse and operational system API sources both active in production. |
| Acceptance | ≥ 85% of query responses accepted by requesting users as analytically accurate without manual re-derivation; metric definition and lineage references validated as correct in ≥ 90% of sampled responses. |
| Cycle | Time from question submission to response reduced from days (data team request cycle) to ≤ 30 minutes per query within a single working session. |
