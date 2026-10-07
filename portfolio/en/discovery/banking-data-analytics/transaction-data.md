# Transaction data

Transaction data is the Bank's highest-volume, highest-velocity data domain — the continuous record of every payment, transfer, card purchase, trade, and account movement across the institution. Raw transaction records carry minimal semantic content; their analytical value is unlocked through enrichment — merchant category, counterparty identity, economic purpose, and customer-journey context — and through lineage tracking that enables reconciliation, audit, and AML pattern detection. AML/CFT transaction monitoring requirements, SWIFT message archiving standards, and the BCBS 239 data aggregation principles expect transaction data to be complete, timely, and traceable from source to downstream system. **The GenAI opportunity is to automate transaction enrichment and categorization at scale, compress reconciliation break investigation cycles, and surface behavioral patterns across the transaction stream** — transforming raw payment records into an analytics-ready layer within hours of settlement.

## Problems

### Payments & movement data {#payments-movement-data}

| Lens | Problem |
| --- | --- |
| Insights & analytics | Transaction volumes, payment-rail utilization, and settlement failure rates are each monitored within separate operations dashboards. Cross-rail patterns — a payment-rail capacity constraint correlating with a settlement-failure spike, or a transaction-value distribution shift indicating emerging merchant or counterparty behavior — are identified only through bespoke analytical work commissioned after an event. |
| Enablement | AML transaction monitoring alert investigation requires analysts to retrieve the full transaction history of a flagged customer across all payment rails, enrich each transaction with merchant category and counterparty identity, and reconstruct the transaction network before assessing the alert. The data-retrieval and enrichment step precedes the substantive compliance judgment. |
| Automation | Transaction enrichment rule application, reconciliation break classification, and settlement exception reporting follow defined logic applied to structured transaction data on each settlement cycle. Each process is repeatable, rule-driven, and high-volume — candidates for continuous AI-driven execution with operations team review at the exception level. |
| New business opportunities | An enriched transaction stream — with merchant category, counterparty identity, and economic purpose attached to each record within hours of settlement — provides the substrate for customer-facing spending insights, AML pattern detection, credit underwriting behavioral signals, and merchant analytics. Peers operating with batch-enriched transaction data delivered at T+1 or later cannot offer the same depth of near-real-time analytics. |

## Payment & transfer records {#payment-transfer-records}

The complete record of every payment instruction and fund transfer processed by the Bank — covering domestic and cross-border payments across domestic interbank payment systems, SWIFT, and card networks, interbank transfers, and internal account movements. Payment records are the primary source for AML transaction monitoring, sanctions screening, correspondent banking due diligence, and settlement reconciliation. Their completeness, timeliness, and traceability determine the Bank's compliance posture under AML/CFT monitoring requirements and the rules on suspicious transaction reporting.

### Payment Data Quality Self-Service

- URN: urn:financial-services:scenario:banking-data-analytics/transaction-data/payment-transfer-records/payment-data-quality-self-service
- Lens: Enablement
- Complexity: S
- Intent: The AI agent enables compliance and operations analysts to query the completeness and accuracy of payment records for a given date range, correspondent, or payment rail without submitting a data team request. The AI agent executes against approved read-only access to the payment records store; output is available within the same working session. AML/CFT compliance analysts apply the capability directly to sanctions-screening gap assessments and correspondent banking due diligence reviews.
- Problem to solve: Compliance and AML analysts who need to assess payment record completeness for a specific correspondent or date range submit a data request and wait for the data team to produce a query result. The wait is disproportionate to the complexity of the underlying query and slows sanctions-screening gap assessments and correspondent banking due diligence reviews. Compliance decisions are delayed by a data access bottleneck rather than analytical complexity.
- Solution: The AI agent accepts a natural-language query specifying a date range, payment rail, or correspondent bank and returns a completeness and accuracy assessment for the specified payment population — field coverage rates, missing mandatory fields, and records flagged for anomalous values. The compliance analyst uses the output to direct remediation or investigation without a data team handoff. Access is controlled through read-only permissions defined and maintained by the CDO.
- OKR: Compliance and AML analysts query payment record completeness and accuracy for specified correspondents, date ranges, and payment rails within a single working session under CDO-governed read-only access, without a data team request.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent handles ≥ 150 compliance and AML self-service queries per month within 12 months of go-live; capability covers all active payment rails and correspondent relationships. |
| Acceptance | ≥ 85% of query responses accepted by analysts as accurate without manual re-verification; field coverage rate calculations validated against payment records store in ≥ 90% of sampled queries. |
| Cycle | Payment data completeness assessment time reduced from multi-day data team request cycles to ≤ 30 minutes per analyst query within a single working session. |

### Payment Data Completeness Monitoring

- URN: urn:financial-services:scenario:banking-data-analytics/transaction-data/payment-transfer-records/payment-data-completeness-monitoring
- Lens: Automation
- Complexity: S
- Intent: The AI agent monitors the completeness of payment record fields required for AML transaction monitoring, sanctions screening, and correspondent banking due diligence on each settlement cycle — flagging payments with missing originator details, absent beneficiary information, or incomplete SWIFT message fields before they are processed by the monitoring systems. The payments operations team receives a same-session exception list for field completion before compliance system consumption.
- Problem to solve: AML transaction monitoring and sanctions screening rules rely on the completeness of originator and beneficiary fields in payment records — SWIFT field 50 (ordering customer), field 59 (beneficiary customer), and correspondent bank chain fields. Payments with missing or incomplete fields are processed by monitoring systems using partial data, degrading the accuracy of screening results and creating regulatory exposure under AML/CFT requirements. Completeness failures are identified in compliance system exception reports after processing rather than before consumption.
- Solution: The AI agent reads each incoming payment instruction before it is consumed by the AML monitoring and sanctions screening systems, validates the required fields against the completeness rules for each payment type (SWIFT, domestic interbank payment systems, card network), and flags incomplete records as same-session exceptions. The payments operations team receives the exception list with the missing field, the payment identifier, and the counterparty information available for manual completion. Payments that cannot be completed within the defined window are escalated to the compliance team for disposition.
- OKR: AML monitoring and sanctions screening systems receive complete, field-validated payment records, reducing screening accuracy failures from missing originator and beneficiary data.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent validates payment record completeness for ≥ 95% of settlement volume across SWIFT and domestic interbank payment rails for ≥ 48 weeks within 12 months; completeness rules approved by compliance within 45 days of go-live. |
| Acceptance | ≥ 90% of flagged completeness exceptions confirmed as genuine missing-field failures by the payments operations team; AML monitoring system exception rate from missing fields reduced by ≥ 60% within 3 months of go-live. |
| Cycle | Completeness validation completed before monitoring system consumption for ≥ 95% of payment volume; exception identification cycle shifted from post-processing compliance reports to pre-consumption same-session flags. |

### Correspondent Banking Due Diligence Data Package

- URN: urn:financial-services:scenario:banking-data-analytics/transaction-data/payment-transfer-records/correspondent-banking-due-diligence-data
- Lens: Insights
- Complexity: M
- Intent: The AI agent assembles transaction flow data, correspondent bank utilization analytics, and jurisdiction risk exposure for each correspondent banking relationship — supporting the annual correspondent due diligence review under AML/CFT requirements. The compliance team uses the data package to assess correspondent risk, identify unusual transaction flow patterns, and update the correspondent risk classification. The AI agent handles the data assembly step; the compliance team applies judgment to the risk assessment.
- Problem to solve: Annual correspondent banking due diligence requires the compliance team to assemble transaction flow analytics — volume and value by currency, payment type, and originator jurisdiction — for each correspondent relationship over the review period. The data assembly requires extracting transaction records from the payments system and the SWIFT archive, aggregating by the required dimensions, and cross-referencing against the correspondent's risk profile. The assembly step consumes compliance analyst time and is inconsistent across relationships, creating variability in due diligence depth.
- Solution: The AI agent reads the payments system and SWIFT message archive for each correspondent relationship, aggregates transaction flow data by currency, payment type, originator jurisdiction, and beneficiary jurisdiction over the review period, and identifies unusual flow patterns — jurisdiction concentrations inconsistent with the correspondent's stated business profile, payment type distributions that deviate from prior-year patterns. It produces a structured due diligence data package: flow summary table, unusual pattern flags, jurisdiction risk heat map, and a comparison to the prior review period. The compliance team reviews the package, applies risk assessment judgment, and updates the correspondent risk classification.
- OKR: The compliance team conducts correspondent banking due diligence reviews from a structured, data-grounded package for each relationship, with analyst capacity directed to risk assessment rather than data assembly.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent assembles due diligence packages for ≥ 90% of correspondent banking relationships in the annual review cycle for 2 consecutive annual review cycles; SWIFT archive and payments system integrations active within 60 days of go-live. |
| Acceptance | ≥ 85% of packages confirmed as complete by compliance analysts without additional manual data extraction; unusual flow flags confirmed as requiring investigation in ≥ 70% of cases. |
| Cycle | Due diligence data assembly time reduced from 3–5 analyst days per relationship to ≤ 1 day of package review; annual review cycle completable within 6 weeks with existing compliance headcount. |

## Transaction lineage & reconciliation {#transaction-lineage-reconciliation}

The documented path from source payment instruction through each processing step — enrichment, routing, settlement, and ledger posting — that enables reconciliation, audit, and regulatory tracing. In line with BCBS 239 Principle 3, transaction data should be traceable from source to aggregate report; AML investigation and sanctions compliance require the ability to reconstruct the full processing path for any transaction within a defined response window. Reconciliation operates on this lineage to match transaction records to ledger entries and identify breaks.

### End-of-Day Reconciliation Narrative

- URN: urn:financial-services:scenario:banking-data-analytics/transaction-data/transaction-lineage-reconciliation/reconciliation-break-investigation
- Lens: Automation
- Complexity: S
- Intent: The AI agent produces the end-of-day reconciliation summary — break count by type, resolution status, and unresolved break narrative — for operations management review and daily reconciliation close sign-off. The quality and completeness of the narrative are consistent regardless of individual analyst effort at end of shift. Operations management reviews the AI-generated narrative and signs off on the daily close.
- Problem to solve: The end-of-day reconciliation narrative is drafted manually by the operations team from reconciliation system outputs each evening. Assembling break counts by type, resolution actions, and outstanding break descriptions from separate system outputs adds time to the reconciliation close process. The completeness and consistency of the narrative depend on individual analyst effort under operational shift-end pressure.
- Solution: The AI agent reads the reconciliation system output at end of day, classifies breaks by type and resolution status, and generates the operations management narrative: break count by type, resolved versus outstanding, escalated items with root cause, and carry-forward summary. Operations management reviews the AI-generated narrative and signs off on the daily reconciliation close. Escalated items are flagged for next-day follow-up with root-cause context attached.
- OKR: Operations management reviews an AI-generated end-of-day reconciliation narrative — break count by type, resolution status, and unresolved break narrative — before daily close sign-off, with consistent quality regardless of individual analyst effort.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces the end-of-day reconciliation narrative for ≥ 95% of business days within 12 months of go-live; break classification by type and resolution status included in each output. |
| Acceptance | ≥ 90% of narratives accepted by operations management for daily close sign-off without material revision; break classification accuracy validated against reconciliation system outputs in ≥ 95% of outputs. |
| Cycle | Reconciliation narrative available for operations management review within 30 minutes of system reconciliation run completion, reducing close-of-shift narrative assembly time. |

### Settlement Reconciliation Break Classification

- URN: urn:financial-services:scenario:banking-data-analytics/transaction-data/transaction-lineage-reconciliation/settlement-reconciliation-break-classification
- Lens: Insights
- Complexity: S
- Intent: The AI agent classifies end-of-day settlement reconciliation breaks by root cause — timing difference, missing counterparty confirmation, system interface error, or genuine unmatched item — using transaction lineage data and the processing log. The settlement operations team receives a classified break list ranked by resolution urgency and approach, reducing the investigation time required for each break and enabling the team to focus manual effort on genuine unmatched items.
- Problem to solve: Settlement reconciliation breaks are investigated manually by the settlement operations team each day, joining the break list from the reconciliation system with the processing log to determine why each transaction did not match. Breaks arising from timing differences — a counterparty confirmation arriving after the reconciliation cut-off — require the same manual investigation step as breaks arising from system interface errors, which require IT escalation. The classification step is repetitive for high-volume break types but consumes investigation time that could be applied to complex or genuine unmatched items.
- Solution: The AI agent reads the EOD break list from the reconciliation system and the processing log for each unmatched item, and classifies each break by applying lineage-based rules: timing difference (counterparty confirmation status), missing confirmation (no confirmation received from counterparty within the expected window), interface error (processing log shows a system-side failure), or genuine unmatched (no lineage trace supports a match). The classified break list ranks items by resolution approach — auto-clearable on next-day confirmation receipt, IT escalation required, or manual investigation required. Settlement operations direct investigation resources to the genuine unmatched and IT escalation tiers.
- OKR: Settlement operations resolve reconciliation breaks more efficiently through a classified, prioritized break list, with auto-clearable breaks separated from items requiring manual investigation.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces classified break lists for ≥ 95% of EOD reconciliation cycles for ≥ 48 weeks within 12 months; processing log and reconciliation system integrations active from go-live. |
| Acceptance | ≥ 85% of break classifications confirmed as accurate by the settlement operations team; manual investigation time per break cycle reduced by ≥ 40% within 3 months of go-live. |
| Cycle | Break classification delivered within 30 minutes of EOD reconciliation output; investigation resource allocation shifted to genuine unmatched items from go-live. |

### AML Transaction Tracing Support

- URN: urn:financial-services:scenario:banking-data-analytics/transaction-data/transaction-lineage-reconciliation/aml-transaction-tracing-support
- Lens: Enablement
- Complexity: M
- Intent: The AI agent reconstructs the full processing path for a specified transaction or transaction set — from source payment instruction through enrichment, routing, settlement, and ledger posting — providing the AML investigations team with a complete evidence trail for STR preparation and regulatory inquiry responses. The AI agent assembles the lineage record from the processing log archive within the defined response window; the investigator reviews the trail and applies judgment to the STR narrative.
- Problem to solve: AML investigations require the investigator to reconstruct the full processing path for suspect transactions — which systems handled the instruction, when each step occurred, whether any screening or enrichment flags were set, and how the transaction reached the ledger. The reconstruction is performed manually by querying the processing log archive, the AML monitoring system, and the ledger posting records sequentially. For complex transactions — cross-border SWIFT messages with correspondent chain hops — the reconstruction can take a full investigation day, compressing the time available for case analysis.
- Solution: The AI agent accepts a transaction identifier or a set of transaction identifiers and queries the processing log archive, the enrichment pipeline output, the AML monitoring system records, and the ledger posting records to reconstruct the end-to-end processing path. The output is a structured lineage trail: each processing step with its timestamp, the system that handled it, any screening or enrichment flags set, and the final ledger posting. For SWIFT transactions, the correspondent chain is reconstructed from the message archive. The investigator uses the trail as the evidence base for the STR narrative and regulatory response, without performing the manual archive reconstruction.
- OKR: AML investigators receive a complete transaction lineage trail within hours of request, directing analyst capacity to case analysis and STR preparation rather than archive reconstruction.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent handles ≥ 85% of transaction lineage reconstruction requests from the AML investigations team within 12 months of go-live; processing log, enrichment, AML monitoring, and ledger sources integrated within 60 days of go-live. |
| Acceptance | ≥ 90% of lineage trails confirmed as complete by the AML investigator without additional manual archive queries; SWIFT correspondent chain reconstruction accuracy validated in ≥ 85% of tested cases. |
| Cycle | Transaction lineage reconstruction time reduced from a full investigation day to ≤ 2 hours of AI agent assembly and investigator review; STR preparation cycle shortened by the elimination of the manual reconstruction step. |

## Transaction enrichment & categorization {#transaction-enrichment-categorisation}

The process of adding semantic content to raw transaction records — attaching merchant category codes, counterparty identity, economic purpose classification, and customer-journey context to payment and transfer data. Enriched transactions are the analytical substrate for AML pattern detection, credit behavior scoring, customer-facing spending insights, and merchant analytics. Enrichment rule sets require maintenance as merchant naming conventions and payment-reference formats evolve; NLP-based enrichment extends coverage beyond static rule sets.

### Enrichment Coverage and Accuracy Drift Detection

- URN: urn:financial-services:scenario:banking-data-analytics/transaction-data/transaction-enrichment-categorisation/enrichment-rule-maintenance
- Lens: Enablement
- Complexity: S
- Intent: The AI agent monitors the enrichment pipeline's classification performance on a weekly basis, detecting coverage drift — an increasing proportion of unclassified transactions — and accuracy drift — a shift in the distribution of manual classification corrections — that indicates the enrichment rule set or NLP model requires updating. The analytics team uses the drift report to prioritize rule maintenance and model retraining, maintaining enrichment quality as merchant naming conventions and payment reference formats evolve.
- Problem to solve: Transaction enrichment quality degrades silently as the payment landscape evolves. New merchants with names outside the trained vocabulary, payment reference format changes adopted by major domestic banks, and new economic purpose categories introduced by product changes create coverage gaps that grow incrementally. The degradation is visible in the unclassified transaction rate but that metric is not monitored systematically; the analytics team discovers quality drift when a downstream consumer — the AML team, the credit underwriting team — reports unusual results in enrichment-dependent analytics.
- Solution: The AI agent reads the weekly enrichment pipeline output, tracks the unclassified transaction rate by merchant category and payment rail, and monitors the distribution of manual classification corrections applied by the training data team. Coverage drift — an unclassified rate rising above trend — and accuracy drift — a correction distribution shifting toward new merchant types or reference patterns — are identified and quantified. The drift report specifies the merchant category and payment rail affected, the magnitude of drift, and a suggested retraining trigger. The analytics team uses the report to schedule rule maintenance sprints and NLP model retraining cycles.
- OKR: Enrichment pipeline quality is maintained through weekly drift detection and structured maintenance cycles run by the analytics team, preventing silent coverage and accuracy degradation between manual reviews.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces weekly drift reports for ≥ 48 weeks within 12 months; coverage and accuracy drift metrics validated against ground-truth sampling within 45 days of go-live. |
| Acceptance | ≥ 80% of drift alerts confirmed as requiring rule maintenance or model retraining by the analytics team; enrichment coverage maintained at ≥ 90% throughout the first 12 months with drift-triggered maintenance. |
| Cycle | Enrichment drift detection cycle shifted from reactive downstream quality complaint discovery to weekly proactive monitoring; rule maintenance and retraining cycles initiated within 2 weeks of drift threshold crossing. |

### Customer Spending Category Insight Delivery

- URN: urn:financial-services:scenario:banking-data-analytics/transaction-data/transaction-enrichment-categorisation/spending-category-insight-delivery
- Lens: Insights
- Complexity: S
- Intent: The AI agent generates a monthly spending category insight summary for the retail and SME banking teams — showing transaction volume and value distribution by enriched spending category for each customer segment, with trend comparisons against prior periods. The insight summary enables product, marketing, and credit teams to identify shifts in customer spending patterns for product development, campaign targeting, and credit model input, drawing directly from the enriched transaction layer.
- Problem to solve: The enriched transaction layer is an analytics substrate for multiple downstream functions but its spending category distributions — how customers in each segment are actually spending — are not regularly surfaced to product, marketing, and credit teams as structured intelligence. Each team accesses the enriched transaction data independently through SQL queries or data requests; the resulting analyses are inconsistent in their time windows and segmentation approaches, making cross-team comparison unreliable. No shared monthly spending view is produced from the enrichment output.
- Solution: The AI agent reads the enriched transaction layer for the most recent month, aggregates transaction volume and value by spending category, payment rail, and customer segment, and produces a monthly spending category insight summary with time-series comparisons against the prior 12 months. It highlights the three largest category shifts per segment and flags categories where spending is diverging materially from the prior-year seasonal pattern. The retail and SME banking teams receive the summary as a shared baseline for product, marketing, and credit discussions.
- OKR: Product, marketing, and credit teams share a common monthly spending category view derived from the enriched transaction layer, enabling consistent cross-team analysis of customer spending behavior.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces monthly spending insight summaries for ≥ 12 consecutive months within the first year; all retail and SME customer segments covered from go-live. |
| Acceptance | ≥ 70% of surveyed product, marketing, and credit users confirm using the monthly summary as a primary spending behavior reference within 6 months; ad hoc spending data requests to the analytics team reduced by ≥ 40% within 6 months. |
| Cycle | Monthly spending summary available ≤ 3 business days after month close; ad hoc cross-team spending analysis cycle replaced by shared monthly baseline from first production cycle. |

### Transaction Enrichment Pipeline

- URN: urn:financial-services:scenario:banking-data-analytics/transaction-data/transaction-enrichment-categorisation/transaction-enrichment-pipeline
- Lens: Automation
- Complexity: M
- Intent: The AI agent enriches raw transaction records at settlement with merchant category codes, counterparty identity, economic purpose classification, and customer-journey context — using NLP-based classification on transaction reference strings, merchant name normalization, and counterparty identity resolution from the entity registry. The enriched transaction layer serves AML pattern detection, credit behavior scoring, customer-facing spending insights, and merchant analytics as a shared analytics substrate.
- Problem to solve: Raw payment and settlement records carry minimal semantic content — transaction reference strings, payment amounts, and account numbers — that is sufficient for settlement processing but not for analytics. Enriching transaction records with merchant categories, counterparty identity, and economic purpose classification currently relies on static rule sets keyed to known merchant name strings and reference patterns. Coverage gaps emerge as merchants change naming conventions, new payment reference formats are adopted, and new merchant types enter the portfolio. AML and credit analytics functions that depend on enrichment quality are degraded by uncategorized transactions.
- Solution: The AI agent reads each settlement transaction record, applies NLP classification to the merchant name and transaction reference string to infer merchant category and economic purpose, resolves the counterparty identity against the entity registry and existing customer golden records, and assigns a customer-journey context label where the transaction is part of a recognized product interaction sequence. Transactions classified with confidence below the defined threshold are queued for a secondary rule-based pass; transactions that fall below both thresholds are flagged for manual classification as training data. The enriched record is written to the analytics transaction layer within the defined latency window after settlement.
- OKR: The analytics transaction layer carries enriched merchant category, counterparty identity, and economic purpose labels for ≥ 90% of settled transactions, providing a reliable substrate for AML, credit, and customer analytics.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's enrichment pipeline is active for 100% of settlement volume across all payment rails for ≥ 48 weeks within 12 months; NLP model trained on ≥ 12 months of historical transaction data before go-live. |
| Acceptance | ≥ 90% enrichment coverage rate confirmed in monthly sampling reviews; enrichment accuracy validated at ≥ 85% correct classification in quarterly ground-truth sampling within 6 months of go-live. |
| Cycle | Enrichment latency: ≥ 95% of settled transactions enriched within 4 hours of settlement confirmation; enrichment coverage rate improved from static rule-set baseline to NLP-augmented target within 3 months of go-live. |

## Transaction analytics & patterns {#transaction-analytics-patterns}

Derived analytics from the enriched transaction stream — behavioral patterns, spending distributions, payment-flow networks, and anomaly detection — that serve AML, credit underwriting, product analytics, and customer intelligence. Transaction pattern analysis operates on the full transaction history across a customer or entity population; its depth and timeliness depend on the enrichment quality of the underlying transaction layer and the accessibility of the analytics environment to the teams that need to consume it.

### Product Analytics Usage Dashboard

- URN: urn:financial-services:scenario:banking-data-analytics/transaction-data/transaction-analytics-patterns/product-analytics-usage-dashboard
- Lens: Enablement
- Complexity: S
- Intent: The AI agent aggregates transaction pattern data by product type — deposit usage intensity, loan drawdown and repayment patterns, card spending category distribution, and digital channel engagement — and produces a monthly product analytics dashboard for the product management team. The dashboard provides the transaction-level evidence base for product performance assessment, feature prioritization, and pricing review, replacing ad hoc data requests to the analytics team.
- Problem to solve: Product managers rely on periodic data requests to the analytics team for transaction-level product usage insights — how customers are using features, which transaction categories dominate card spending for a given segment, how loan drawdown patterns vary by product type. The data request turnaround extends the product review cycle; the analytics produced are point-in-time snapshots rather than a continuous view. Product decisions that require understanding of usage evolution over time require multiple sequential data requests.
- Solution: The AI agent reads the enriched transaction stream and aggregates by product type, customer segment, and time dimension — deposit usage frequency and balance bands, loan utilization patterns and repayment behavior, card spending by MCC category, and digital channel transaction share. It produces a monthly product analytics dashboard with time-series views for each product and segment. The product management team uses the dashboard as a self-service analytics resource for product performance review and feature development prioritization, without requiring analytics team data requests for standard product usage questions.
- OKR: Product management holds a continuous, transaction-grounded view of product usage patterns by segment, enabling evidence-based product decisions without analytics team data requests for standard usage questions.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces monthly product analytics dashboards for ≥ 12 consecutive months within the first year; all product types and active customer segments covered from go-live. |
| Acceptance | ≥ 70% reduction in standard product usage data requests to the analytics team within 6 months of go-live; product managers confirm dashboard sufficient for ≥ 80% of regular product performance questions. |
| Cycle | Product usage analytics cycle shifted from ad hoc data request (days to weeks) to a monthly automated dashboard available ≤ 3 business days after month close. |

### Transaction Behavior Profile

- URN: urn:financial-services:scenario:banking-data-analytics/transaction-data/transaction-analytics-patterns/transaction-behaviour-profile
- Lens: Insights
- Complexity: M
- Intent: The AI agent generates a transaction behavior profile for a customer or segment — spending patterns, payment-rail preferences, and behavioral anomalies — structured for credit underwriting, AML, and product analytics use. For credit underwriting, the profile highlights income regularity, debt-service behavior, and sector exposure. For AML, it flags network anomalies, structuring patterns, and high-risk merchant categories.
- Problem to solve: Transaction behavior analysis for credit underwriting or AML investigation requires analysts to extract and aggregate transaction history across payment rails and merchant categories from the data warehouse. Analysts with direct SQL access spend hours on the extraction; those dependent on data team requests wait multiple days. The lag between analytical need and insight delays credit and compliance decisions that are time-sensitive.
- Solution: The AI agent reads the enriched transaction stream for the specified customer or segment, aggregates by spending category, payment rail, counterparty type, and time dimension, and produces a structured behavior profile. Credit and AML use cases receive purpose-specific profile sections with relevant indicators highlighted. The analyst receives the profile as structured output ready for downstream credit, compliance, or product decision use.
- OKR: Credit underwriting, AML, and product analytics functions receive structured transaction behavior profiles — spending patterns, payment-rail preferences, and behavioral anomalies — assembled by the AI agent from the enriched transaction stream for specified customers or segments.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces transaction behavior profiles for ≥ 95% of requests from credit, AML, and product analytics users within 12 months of go-live; credit and AML purpose-specific sections included in each applicable profile. |
| Acceptance | ≥ 85% of profiles accepted by analysts as suitable for direct use in credit, compliance, or product decisions without manual re-extraction; AML anomaly flag accuracy validated against investigation outcomes in ≥ 80% of sampled cases. |
| Cycle | Profile assembly time reduced from hours of manual SQL extraction or multi-day data team request cycles to ≤ 30 minutes per profile within a single working session. |

### AML Network Anomaly Detection

- URN: urn:financial-services:scenario:banking-data-analytics/transaction-data/transaction-analytics-patterns/aml-network-anomaly-detection
- Lens: Automation
- Complexity: M
- Intent: The AI agent analyzes the payment network graph — the pattern of fund flows between bank customers, counterparties, and third-party entities — to detect network-level AML anomalies that are invisible at the individual transaction level: layering chains, rapid pass-through patterns, and structuring networks operating across multiple accounts. The AML investigations team receives a weekly network anomaly report with the flagged entity clusters and the network pattern evidence supporting the alert.
- Problem to solve: AML transaction monitoring rules operate at the individual transaction or single-account level; they are designed to detect known typologies at the transaction level but are less effective against network-level patterns where the suspicious activity is distributed across multiple accounts and entities. Layering through a chain of accounts, structuring networks that operate through multiple individuals, and rapid-cycle pass-through patterns that reset at each hop are typologies that require network-level analysis. The AML investigations team identifies network patterns reactively — during investigations triggered by individual-account alerts — rather than proactively.
- Solution: The AI agent constructs the payment flow network from the enriched transaction record, treating each payment as a directed edge between the originator and beneficiary entities. It applies network analysis algorithms to detect structuring patterns (multiple entities making just-below-threshold transactions to a common recipient), layering chains (funds cycling through multiple accounts within a defined time window), and rapid pass-through patterns (accounts receiving and disbursing the majority of received funds within 24 hours). Detected network clusters are ranked by the strength of the anomaly signal and the total value flowing through the cluster. The AML investigations team receives the weekly network report with the supporting transaction evidence.
- OKR: The AML investigations team holds a weekly view of network-level anomaly patterns in the payment flow graph, enabling proactive investigation of typologies not detectable at the individual transaction level.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces weekly network anomaly reports for ≥ 48 weeks within 12 months; enriched transaction graph covering all payment rails active from go-live. |
| Acceptance | ≥ 40% of flagged network clusters confirmed as warranting AML investigation by the investigations team; STR filing rate from network-analysis-triggered investigations ≥ 25% within 6 months of go-live. |
| Cycle | Network anomaly detection cycle shifted from reactive investigation discovery to weekly proactive graph analysis; network-pattern STR filings initiated proactively rather than reactively within 6 months. |

## Card & merchant data {#card-merchant-data}

Transaction data specific to card-scheme processing — covering card authorization and settlement records, chargeback events, merchant category code assignments, and merchant performance data for acquiring businesses. Card data is processed under Visa and Mastercard scheme rules; data from the national card scheme adds a parallel data stream with distinct format conventions. Card transaction data feeds fraud detection, dispute processing, and merchant analytics; its enrichment quality directly affects the accuracy of customer spending categorization.

### Chargeback Root Cause Analysis

- URN: urn:financial-services:scenario:banking-data-analytics/transaction-data/card-merchant-data/chargeback-root-cause-analysis
- Lens: Automation
- Complexity: S
- Intent: The AI agent analyzes chargeback events by reason code, merchant category, card scheme, and channel to identify systematic root causes — merchant categories with elevated chargeback rates, processing errors driving non-fraud chargebacks, and scheme-specific dispute patterns — and produces a weekly root cause report for the card operations and merchant acquiring teams. The report supports the identification of operational and merchant-level issues driving chargeback costs before they breach scheme penalty thresholds.
- Problem to solve: Chargeback volumes are tracked in total and by reason code but the root cause analysis — identifying which merchant categories, processing steps, or card scheme interactions drive disproportionate chargeback rates — is performed manually for monthly management reporting. Merchant categories approaching Visa or Mastercard scheme chargeback penalty thresholds are identified at the monthly review, by which time the threshold may already be breached. Operational errors that could be corrected to reduce non-fraud chargebacks are not systematically identified.
- Solution: The AI agent reads chargeback event records, classifies each event by reason code, merchant category code, card scheme (Visa, Mastercard, the national card scheme), and channel, and calculates chargeback rates by each dimension against the transaction base. Merchant categories with chargeback rates above defined thresholds and those trending toward scheme penalty levels are flagged. Non-fraud reason codes with elevated rates in specific merchant categories are highlighted as potential operational error sources. The card operations and merchant acquiring teams receive the weekly root cause report with priority ranking by cost exposure.
- OKR: Card operations and merchant acquiring teams hold a weekly, root-cause-structured view of chargeback drivers, enabling operational corrections and merchant-level interventions before scheme penalty thresholds are breached.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces weekly chargeback root cause reports for ≥ 48 weeks within 12 months; all card scheme data sources integrated from go-live. |
| Acceptance | ≥ 80% of flagged merchant categories confirmed as requiring operational or merchant-level action by the card operations and merchant acquiring teams; scheme penalty threshold breaches reduced to zero within 6 months of go-live. |
| Cycle | Root cause analysis cycle shifted from monthly management reporting to a weekly structured report; scheme threshold breach identification lead time extended from monthly review to ≥ 3 weeks of forward warning. |

### Merchant MCC Assignment Quality Check

- URN: urn:financial-services:scenario:banking-data-analytics/transaction-data/card-merchant-data/merchant-mcc-assignment-quality
- Lens: Enablement
- Complexity: S
- Intent: The AI agent reviews merchant category code (MCC) assignments in the card acquiring portfolio each quarter against the merchant's actual business activity — using transaction descriptions, merchant name, and website category data — and identifies merchants whose MCC may be incorrectly assigned. Incorrect MCCs affect customer spending categorization accuracy, AML transaction monitoring rule accuracy, and interchange fee classification. The card acquiring team uses the review report to correct MCC assignments through the scheme re-registration process.
- Problem to solve: MCC assignments are made during merchant onboarding and reviewed only when a mis-classification is identified through a dispute or scheme audit. Merchants whose business activity has evolved since onboarding — an electronics retailer that has expanded into financial services, a travel agent now primarily selling insurance — carry stale MCCs that affect spending categorization in customer-facing analytics, AML monitoring rule accuracy, and interchange fee billing. The scope of MCC mis-classifications in the acquiring portfolio is not systematically known.
- Solution: The AI agent reads the acquiring merchant portfolio and cross-references each merchant's assigned MCC against the merchant's transaction description patterns, business name classification, and available website category data. Merchants where the MCC is inconsistent with the transaction description pattern — by statistical comparison to the distribution of transactions under the same MCC — are flagged as potential mis-classifications, ranked by transaction volume and AML rule impact. The card acquiring team reviews the flagged merchants and initiates the scheme MCC re-registration process for confirmed mis-classifications.
- OKR: MCC assignments in the acquiring portfolio reflect current merchant business activity, improving customer spending categorization accuracy, AML monitoring rule precision, and interchange fee billing integrity.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces quarterly MCC assignment quality reports covering 100% of the active acquiring merchant portfolio for ≥ 4 consecutive quarters within the first year; transaction description and MCC consistency rules validated within 60 days of go-live. |
| Acceptance | ≥ 70% of flagged merchants confirmed as mis-classified by the card acquiring team; MCC re-registration initiated for ≥ 90% of confirmed mis-classifications within 30 days of identification. |
| Cycle | MCC quality review cycle shifted from scheme-audit-triggered correction to quarterly proactive check; known MCC mis-classification rate in the acquiring portfolio reduced by ≥ 40% within 6 months. |

### Card Fraud Pattern Detection

- URN: urn:financial-services:scenario:banking-data-analytics/transaction-data/card-merchant-data/card-fraud-pattern-detection
- Lens: Insights
- Complexity: M
- Intent: The AI agent analyzes card authorization and settlement records to detect fraud patterns — unusual merchant category sequences, geographic velocity anomalies, and authorization-to-settlement timing outliers — across the card portfolio, generating a daily fraud signal report for the fraud operations team. The report distinguishes between card-present and card-not-present patterns and covers both Visa/Mastercard scheme data and national card scheme data. The fraud operations team uses the report to direct case investigation resources.
- Problem to solve: Card fraud detection operates through real-time transaction scoring at the point of authorization; portfolio-level pattern analysis — identifying emerging fraud typologies across the card book rather than at individual card level — is performed episodically by fraud analysts using data warehouse queries. Emerging fraud patterns that are not captured in the real-time scoring model accumulate in the portfolio before they are detected at the analyst review cycle. National card scheme data and international scheme data are analyzed separately, limiting cross-scheme pattern detection.
- Solution: The AI agent reads card authorization and settlement records across Visa, Mastercard, and national card scheme data, applies pattern detection across merchant category sequences, geographic velocity, and authorization-to-settlement timing, and produces a daily fraud signal report. The report identifies emerging typologies — patterns present in a growing proportion of disputed transactions — and ranks them by portfolio-level loss exposure. Card-present and card-not-present patterns are reported separately. The fraud operations team uses the report to update the real-time scoring model's feature set and to direct case investigation resources to the highest-risk merchant categories.
- OKR: The fraud operations team receives a daily portfolio-level fraud pattern signal covering all card scheme data, enabling emerging typology detection before the pattern reaches material loss levels.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces daily fraud pattern reports for ≥ 48 weeks within 12 months; all scheme data sources (Visa, Mastercard, the national card scheme) integrated from go-live. |
| Acceptance | ≥ 50% of flagged emerging patterns confirmed as genuine fraud typologies by the fraud operations team; real-time scoring model feature updates initiated for ≥ 80% of confirmed typologies within 2 weeks of pattern identification. |
| Cycle | Fraud typology detection cycle shifted from episodic analyst review to a daily automated pattern signal; emerging typology detection lead time extended from weeks to ≤ 5 business days of sustained pattern presence. |
