# 

source: html-alt/financial-services/en/risk-control/operational-risk/index.html


[PAGE TEXT]
Loss events & near-misses
Operational loss events are the realized losses from operational risk failures — recorded in the operational risk management system with event type, business line, amount, and root cause. Near-misses are events that could have produced a loss but did not — equally informative for risk management but recorded less systematically. Under Basel III Advanced Measurement Approach and EBA operational risk guidelines, internal loss data must meet minimum quality standards and cover at least five years of history. Loss data aggregated across the portfolio is the primary input to advanced capital modelling; thematic patterns in recent events inform RCSA updates.
Lens
Scenario
Intent
Complexity

### CARD 1 [Automation|S] Operational Loss Event Data Quality Check
urn: urn:financial-services:scenario:risk-control/operational-risk/loss-events-near-misses/operational-loss-event-data-quality
intent: Agent reviews newly entered loss events against the Basel II data quality standards — completeness, business line mapping, event type classification, and recovery recording — and returns a quality flag to the operational risk officer before the event is accepted into the AMA database.
Problem to solve: Advanced Measurement Approach capital models require loss event data meeting minimum quality standards for date, amount, business line, event type, and recovery recording. Quality issues in submitted loss events are identified in the quarterly data quality review rather than at the point of entry, requiring retrospective corrections that are time-consuming and may affect capital calculations.
Solution: Agent reads newly submitted loss event records and applies the Basel II data quality schema — all required fields populated, business line mapped to the regulatory taxonomy, event type classification consistent with the description, and gross loss and recovery separately recorded. It returns a quality flag with specific field-level issues to the operational risk officer for correction before acceptance.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 2 [Insights|M] Operational Loss Event Pattern Analysis
urn: urn:financial-services:scenario:risk-control/operational-risk/loss-events-near-misses/operational-loss-event-pattern-analysis
intent: Agent clusters loss events and near-misses by root cause, business line, and Basel II event category, surfacing systemic patterns for the Operational Risk Committee.
Problem to solve: Loss events and near-misses are recorded individually in the operational risk system. Patterns across events — a common process failure across three business lines, or a near-miss cluster preceding a material loss — are visible only when the operational risk analyst manually reviews the full population ahead of the quarterly committee.
Solution: Agent reads the loss event and near-miss register, clusters entries by root cause, business line, and Basel II event category, and applies pattern detection across time and entity dimensions. The Operational Risk Committee receives a monthly pattern digest with systemic-risk flags, supplementing the per-event log.
OKR objective: The Operational Risk Committee receives a monthly pattern digest — clustering loss events and near-misses by root cause, business line, and Basel II event category — enabling systemic risk flags to be actioned between quarterly formal reviews.
OKR KR [Adoption]: Agent pattern analysis running on the full loss event and near-miss register monthly within 6 months of go-live; monthly digest delivered to the Operational Risk Committee for ≥10 consecutive months in year 1.
OKR KR [Acceptance]: ≥70% of agent-surfaced systemic-risk flags rated as material by the Operational Risk Committee; root-cause clusters identified by the agent lead to ≥2 remediation actions per annual cycle.
OKR KR [Cycle]: Monthly pattern digest produced within 3 business days of month-end data cut, versus ≥2 weeks of manual pre-committee analysis under the prior approach.

### CARD 3 [Insights|M] Near-Miss Capture Programme Analysis
urn: urn:financial-services:scenario:risk-control/operational-risk/loss-events-near-misses/near-miss-capture-programme-analysis
intent: Agent analyses the near-miss register relative to the loss event population to assess the adequacy of the near-miss capture programme, identifying operational risk categories and business units with near-miss rates inconsistent with their loss event history.
Problem to solve: Near-miss reporting rates vary significantly across business units and risk categories. Business units with high loss event frequency but low near-miss reporting indicate an under-reporting culture; the operational risk function cannot distinguish genuine low near-miss environments from reporting reluctance without systematic cross-referencing.
Solution: Agent reads the near-miss register and loss event database, computes near-miss-to-loss ratios by business unit and Basel II event category, and identifies units with near-miss rates inconsistent with their loss event population. The operational risk function receives the analysis for targeted near-miss reporting culture improvement.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
Third-party & TPRM
Third-party risk management (TPRM) covers the governance and ongoing monitoring of risks arising from vendors, outsourcing partners, and ICT providers — including sub-outsourcing chains and intra-group dependencies. DORA Article 28 requires regulated institutions to maintain a register of all ICT third-party providers with defined information requirements per vendor; NBKR Regulation No. 12 sets equivalent requirements for outsourcing. Critical vendor identification, contract due diligence, ongoing performance monitoring, and exit planning are the core TPRM disciplines. With 50-300 ICT providers, maintaining a current, accurate register is a significant operational undertaking.
Lens
Scenario
Intent
Complexity

### CARD 4 [Automation|S] TPRM Exit Plan Currency Check
urn: urn:financial-services:scenario:risk-control/operational-risk/third-party-tprm/tprm-exit-plan-currency-check
intent: Agent reviews exit plan documentation for critical ICT vendors against the current contract terms and operational dependency profile, flags plans where the documented exit approach is inconsistent with the current environment, and delivers the review findings to the TPRM lead.
Problem to solve: DORA requires documented exit plans for critical ICT providers. Exit plans are prepared at contract execution and may not reflect changes in operational dependencies — new integrations, expanded scope, changed alternative provider market — that affect the feasibility of the documented exit approach.
Solution: Agent reads the exit plan documents for critical ICT vendors, compares the documented exit steps against current contract terms, service scope, and integration inventory, and flags exit plans where the documented approach is inconsistent with the current operating model. The TPRM lead receives a review report with specific plan sections requiring update.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 5 [Automation|M] DORA Third-Party Register Extraction
urn: urn:financial-services:scenario:risk-control/operational-risk/third-party-tprm/dora-third-party-register-extraction
intent: Agent extracts DORA-required structured fields from ICT vendor contracts and populates the third-party register with cited sources, replacing manual contract reading for each provider.
Problem to solve: DORA requires a register entry per ICT provider covering service scope, data types, sub-outsourcing chain, processing locations, exit clauses, and SLAs. Each entry requires reading a 20–100 page contract; with 50–300 providers, manual extraction across the register refresh cycle is a material TPRM overhead.
Solution: Agent reads ICT contracts and extracts DORA-required fields using schema-driven document extraction, providing citations for each extracted field. The risk team reviews agent-extracted entries and resolves ambiguous fields, reducing per-vendor effort from several hours to a focused review.
OKR objective: The TPRM team maintains the DORA ICT third-party register with agent-extracted structured fields cited to source contracts, replacing per-vendor manual document reading.
OKR KR [Adoption]: Agent-extracted register entries used for ≥80% of ICT providers in the next register refresh cycle within 18 months of go-live; all DORA-required fields extracted per vendor from go-live.
OKR KR [Acceptance]: ≥80% of agent-extracted register fields accepted by the risk team without amendment after focused review; citation accuracy (extracted field matches cited contract clause) confirmed at ≥90% on quality audit.
OKR KR [Cycle]: Per-vendor register extraction completed within 30 minutes of contract ingestion, versus ≥3 hours of manual reading under the prior approach, reducing total register refresh cycle duration by ≥60%.

### CARD 6 [Insights|M] ICT Vendor Performance Monitoring
urn: urn:financial-services:scenario:risk-control/operational-risk/third-party-tprm/ict-vendor-performance-monitoring
intent: Agent aggregates SLA performance data, incident records, and financial health signals for critical ICT vendors, producing a monthly vendor risk dashboard for the TPRM lead and CRO.
Problem to solve: Critical ICT vendor performance is monitored through SLA reports submitted by vendors themselves and reviewed by vendor relationship managers. Cross-vendor signals — a vendor with declining SLA performance and deteriorating financial health simultaneously — are not visible in the per-vendor review cycle; the risk is identified reactively when a vendor event triggers a review.
Solution: Agent reads SLA performance data, incident records, and vendor financial health indicators — credit ratings, payment behaviour, public financial disclosures — for all critical ICT vendors. It computes a risk score per vendor combining performance and financial health dimensions, identifies vendors with deteriorating combined profiles, and delivers the monthly dashboard to the TPRM lead and CRO.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
RCSA & KRI monitoring
The Risk and Control Self-Assessment (RCSA) is the structured framework through which each business unit identifies its key operational risks, assesses inherent risk severity, and evaluates the effectiveness of controls in place. Key Risk Indicators (KRIs) are quantitative measures that signal changes in the operational risk environment — transaction error rates, system downtime, staff turnover, control failure rates — tracked against thresholds defined in the Risk Appetite Statement. NBKR and CBR operational risk guidelines require documented RCSA processes and KRI frameworks. The RCSA cycle typically runs annually; KRI reporting runs monthly to the operational risk committee.
Lens
Scenario
Intent
Complexity

### CARD 7 [Automation|S] KRI Threshold Breach Alert & Pack
urn: urn:financial-services:scenario:risk-control/operational-risk/rcsa-kri-monitoring/kri-threshold-breach-alert
intent: Agent monitors KRI values against amber and red thresholds on each reporting cycle, generates a breach alert pack with the KRI value, trend, related RCSA risk entry, and response protocol reference, and delivers it to the operational risk officer and relevant business unit head.
Problem to solve: KRI threshold breaches require the operational risk officer to investigate the root cause and initiate the defined response protocol. The investigation pack — current KRI value and trend, linked RCSA risk entry, and response protocol — is assembled manually at breach, delaying the start of the response.
Solution: Agent reads the monthly KRI reporting data, compares each indicator to its amber and red thresholds, and generates the breach alert pack for each breached indicator. The operational risk officer and business unit head receive the pack with the triggering value, six-month trend, linked RCSA entry, and response protocol reference at the time of breach.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 8 [Enablement|M] RCSA Facilitation Support
urn: urn:financial-services:scenario:risk-control/operational-risk/rcsa-kri-monitoring/rcsa-facilitation-support
intent: Agent prepares business-unit-level RCSA working materials — pre-populated risk registers, control inventory, and prior-period KRI trends — enabling operational risk officers to run more RCSA sessions per cycle.
Problem to solve: RCSA facilitation requires operational risk officers to prepare risk and control inventories for each business unit before the assessment session. With 30–50 business units per cycle, drawing from prior RCSAs, audit findings, and loss event data consumes a material share of the function's capacity before facilitation begins.
Solution: Agent reads prior RCSA records, recent loss events, audit findings, and KRI trends for each business unit and generates a pre-populated RCSA working document. The operational risk officer uses it as the starting point for the facilitated session, reducing preparation time and increasing session coverage per cycle.
OKR objective: Operational risk officers run more RCSA sessions per cycle using agent-generated pre-populated working materials — incorporating prior RCSA records, control inventory, and KRI trends — for each business unit.
OKR KR [Adoption]: Agent-generated RCSA working materials used as the starting point for ≥70% of business unit facilitated sessions in the next full annual RCSA cycle within 18 months of go-live; all three data sources (prior RCSA, loss events, audit findings, KRI trends) integrated per business unit from go-live.
OKR KR [Acceptance]: ≥80% of agent-generated working documents rated as useful or better by facilitating risk officers; RCSA sessions conducted per operational risk officer per cycle increased by ≥20% versus the prior preparation-constrained rate.
OKR KR [Cycle]: Pre-populated RCSA working document delivered within 2 business days of business unit scoping confirmation, versus ≥1 week of manual preparation under the prior approach.

### CARD 9 [Insights|M] KRI and RCSA Alignment Review
urn: urn:financial-services:scenario:risk-control/operational-risk/rcsa-kri-monitoring/kri-rcsa-alignment-review
intent: Agent cross-references the KRI register against the RCSA risk register to identify risks with no monitoring KRI and KRIs with no RCSA linkage, and delivers a coverage gap analysis to the operational risk committee.
Problem to solve: RCSA risks and KRIs are maintained in separate registers and aligned manually in the annual RCSA cycle. Risks added to the RCSA between annual cycles may not have corresponding KRIs; KRIs configured for legacy risks may no longer correspond to current RCSA entries. The misalignment accumulates between annual review cycles.
Solution: Agent reads the current RCSA risk register and KRI register, applies linkage matching by risk category and description, and identifies RCSA risks with no covering KRI and KRIs with no corresponding RCSA risk. The operational risk committee receives the coverage gap analysis in the quarterly review pack.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
Business continuity & DR
Business continuity management (BCM) and disaster recovery (DR) define the bank's capacity to maintain critical business functions and restore IT systems following a disruption event. Under DORA Article 11 and NBKR operational resilience guidelines, banks must maintain tested BCM and DR plans, define Recovery Time Objectives (RTOs) and Recovery Point Objectives (RPOs) for critical systems, and test these against defined scenarios at least annually. Post-incident review documentation — capturing root cause, recovery timeline, and lessons learned — is a regulatory expectation after any major disruption. BCP and DR plans require annual refresh to reflect changes in the operating environment.
Lens
Scenario
Intent
Complexity

### CARD 10 [Automation|M] Post-Incident Review & BCP Update
urn: urn:financial-services:scenario:risk-control/operational-risk/business-continuity-dr/post-incident-review-bcp-update
intent: Agent assembles post-incident review documentation from recovery logs and communications records, and flags BCP sections requiring update based on incident root cause and recovery timeline.
Problem to solve: Post-incident review documentation — root cause, recovery timeline, lessons learned — must be produced following every major operational disruption. Assembling from system logs, incident communications, and recovery records is a substantial effort at a point when the team is simultaneously managing remediation.
Solution: Agent reads the incident timeline from monitoring systems, recovery logs, and communications records. It generates the post-incident review document in regulatory format — root cause narrative, recovery timeline mapped to RTO/RPO, and lessons learned — and flags BCP sections affected by the root cause. The BCM team reviews and signs off before submission.
OKR objective: The BCM team submits post-incident review documentation in regulatory format — with root cause, recovery timeline mapped to RTO/RPO, lessons learned, and BCP update flags — assembled by the agent from recovery logs and communications records.
OKR KR [Adoption]: Agent used to assemble post-incident review documentation for ≥90% of major operational disruptions within 12 months of go-live; BCP update flags applied automatically to every review from go-live.
OKR KR [Acceptance]: ≥80% of agent-assembled post-incident review documents accepted by the BCM team without structural revision before submission; BCP sections flagged by agent confirmed as requiring update in ≥75% of flagged instances on review.
OKR KR [Cycle]: Post-incident review draft delivered within 2 business days of incident closure, versus ≥1 week of manual assembly under the prior approach.

### CARD 11 [Enablement|M] BCP Annual Refresh Support
urn: urn:financial-services:scenario:risk-control/operational-risk/business-continuity-dr/bcp-annual-refresh-support
intent: Agent reads the current BCP documents and compares them against the current operating environment — system changes, organisational changes, vendor changes — flagging sections requiring update before the BCM team's annual review.
Problem to solve: Annual BCP refresh requires the BCM team to review each plan section for continued accuracy. With 10-30 BCP documents covering critical business functions, identifying sections affected by changes in systems, organisation, or third-party dependencies consumes the BCM team's cycle capacity before substantive review begins.
Solution: Agent reads the current BCP documents, compares recovery procedures and contact lists against the current system inventory, organisation chart, and vendor register, and flags sections where changes in the operating environment require plan update. The BCM team focuses the review on flagged sections rather than performing a full line-by-line review of unchanged content.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 12 [Insights|M] RTO/RPO Test Results Analysis
urn: urn:financial-services:scenario:risk-control/operational-risk/business-continuity-dr/rto-rpo-test-results-analysis
intent: Agent analyses RTO and RPO test results across all critical systems over the rolling 24-month test history, identifies systems with deteriorating recovery performance, and delivers the analysis to the BCM lead and CISO for remediation prioritisation.
Problem to solve: RTO and RPO test results are documented per test exercise and reviewed in the post-exercise report. Trend in recovery performance across multiple test cycles — a system meeting its RTO consistently but with increasing recovery time trend — is not visible in the per-exercise review.
Solution: Agent reads 24 months of RTO and RPO test results by system, computes recovery time trend and achievement rate per system, and identifies systems where performance is deteriorating or where the test-to-target gap is widening. The BCM lead and CISO receive the analysis for inclusion in the DR programme remediation roadmap.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
GenAI-enabled Banking and Financial Services Framework · v11i
