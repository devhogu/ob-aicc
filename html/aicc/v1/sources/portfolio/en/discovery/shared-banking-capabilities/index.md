# Shared Banking Capabilities

Shared Banking Capabilities are the cross-cutting engines that multiple value chains draw from — credit decisioning, transaction processing, pricing and profitability, financial crime controls, collections, customer onboarding, servicing, and advisory content that no single business line owns exclusively. They operate under direct supervisory requirements and international standards such as the FATF Recommendations: capability failures surface immediately in regulatory findings rather than business metrics. **The opportunity for GenAI is to compress the latency and analyst burden across every shared engine** — from KYC document review and AML alert triage through scorecard-driven credit decisions and frontline case resolution — releasing capacity from rule-based assembly work to judgment-intensive exception handling.

## Problems

### Operational capabilities {#operational-capabilities}

| Lens | Problem |
| --- | --- |
| Insights & analytics | Credit portfolio quality, transaction exception patterns, pricing-model performance, financial crime alert distributions, and collections waterfall effectiveness are each reported separately by the teams that own them. Senior management lacks a consolidated view of shared-capability health — how decisioning models are performing, where exception backlogs are building, which fraud typologies are rising — between formal reporting cycles. |
| Enablement | Credit underwriters, transaction investigators, AML analysts, collections officers, and pricing teams each rely on separate specialist knowledge bases and senior colleagues to handle exceptions and edge cases. The collective judgment bottleneck — a small group of experienced practitioners who resolve what automated rules cannot — limits throughput across every operational capability simultaneously. |
| Automation | Across credit decisioning, transaction processing, financial crime, pricing, and collections, the highest-volume work involves structured inputs, defined decision rules, and prescribed output formats: application scoring, alert triage, exception categorization, STR drafting, payment reconciliation. Each domain has large automation surface area that current manual workflows leave untouched. |
| New business opportunities | Banks that operate shared capabilities at lower unit cost and higher throughput — faster credit decisions, lower payment exception rates, compressed AML cycle times — create capacity headroom to take on more volume without proportional cost growth. GenAI-backed capability efficiency converts fixed operational infrastructure into a scalable competitive asset. |

## Overview

### Credit decisioning {#credit-decisioning}

- Group: Operational capabilities

| Sub-group | Items |
| --- | --- |
| Limit & line management | scorecard-model-performance, underwriter-review-override |
| Limit line management | annual-credit-review, covenant-monitoring |

### Customer servicing {#customer-servicing}

- Group: Customer-facing capabilities

| Sub-group | Items |
| --- | --- |
| Inquiry & case handling | frontline-policy-copilot, interaction-summarization, service-intake-routing, support-ticket-pattern-mining |
| Complaints & conduct | complaint-response-drafting, complaint-pattern-conduct-analytics |

### Capability Cycles {#capability-cycles}

- Group: Capability governance

| Section | List name | Flows |
| --- | --- | --- |
| Performance & improvement | Performance & improvement | capability-kpi-sla-review-cycle, continuous-improvement-cycle |
| Investment & sourcing | Investment & sourcing | capability-investment-cycle, vendor-sourcing-review-cycle |

### Customer onboarding {#customer-onboarding}

- Group: Customer-facing capabilities

| Sub-group | Items |
| --- | --- |
| Identity verification | kyc-document-extraction, cdd-risk-classification, sanctions-pep-screening |
| Activation & cross-sell | account-setup-activation, early-cross-sell-signals |

### Transaction processing & settlement {#transaction-processing}

- Group: Operational capabilities

| Sub-group | Items |
| --- | --- |
| Payment processing | payment-exception-pattern-analytics, investigation-triage-support |
| Settlement & reconciliation | nostro-reconciliation, case-dossier-builder-payments |
| Payments modernization | payments-modernization |

### Pricing & profitability {#pricing-profitability}

- Group: Operational capabilities

| Sub-group | Items |
| --- | --- |
| Pricing models & FTP | pricing-experiment-analytics, ftp-raroc-pricing-signal |
| Profitability attribution | segment-profitability-deep-dive, profitability-pack-production |

### Financial crime {#financial-crime}

- Group: Operational capabilities

| Sub-group | Items |
| --- | --- |
| Fraud & sanctions detection | transaction-monitoring-alert-triage, false-positive-rule-tuning |
| AML investigations & STR | aml-investigation-pack, sar-drafting |

### Collections & recoveries {#collections-recoveries}

- Group: Operational capabilities

| Sub-group | Items |
| --- | --- |
| Early-stage delinquency | delinquency-segmentation, promise-to-pay-management, early-warning-escalation |
| Recovery operations | legal-referral-triage, portfolio-write-off-sale |

### Advisory & research {#advisory-research}

- Group: Customer-facing capabilities

| Sub-group | Items |
| --- | --- |
| Investment research | earnings-call-synthesis, issuer-sector-research-drafting |
| Advisory content production | client-suitability-assessment, portfolio-review-narratives |

## Scenarios

### Shared Capability Health Dashboard

- URN: urn:financial-services:scenario:shared-banking-capabilities/shared-capability-health-dashboard
- Lens: Insights
- Complexity: M
- Intent: The AI agent assembles an integrated operational health view across credit decisioning, transaction exceptions, AML alert queue, and collections delinquency on a weekly cadence for COO review. The composite narrative covers decisioning approval rates and override ratios, payment exception volume and age, AML alert queue depth and disposition rates, and delinquency roll rates and contact effectiveness. The COO reviews the AI-generated summary; capability leads provide forward-looking commentary.
- Problem to solve: Operational capability teams report separately — credit decisioning through the Risk Committee, payment exceptions through Operations, AML through Compliance, and collections through the Collections Director. The COO has no composite view of shared-capability throughput and backlog status between formal reporting cycles. Emerging pressures — rising exception rates, growing AML queues, scorecard drift — reach the COO only after accumulation into a supervisory or P&L event.
- Solution: The AI agent reads throughput and exception feeds from each operational capability system on a weekly cadence and assembles a composite dashboard narrative. Each capability section covers approval or processing rates, backlog depth and age, and emerging quality signals relative to prior periods. The COO reviews the AI-generated summary; capability leads add forward-looking commentary where the operational signal warrants escalation.
- OKR: An integrated operational health view across credit decisioning, payment exceptions, AML alert queue, and collections delinquency is available to the COO each week, with composite throughput and backlog status covering all four capability domains.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced shared capability health dashboard delivered for ≥48 of 52 weeks in year 1; all four capability domains covered in each weekly summary. |
| Acceptance | ≥85% of weekly dashboard summaries accepted by the COO as accurate without requiring supplementary capability team reports; composite operational signals validated against capability system records in ≥90% of reviewed weeks. |
| Cycle | Weekly dashboard summary available each Monday morning, vs. composite visibility only at formal quarterly reporting cycles in the prior process. |

### Cross-Capability Operations Readiness Brief

- URN: urn:financial-services:scenario:shared-banking-capabilities/cross-capability-operations-readiness-brief
- Lens: Enablement
- Complexity: M
- Intent: The AI agent synthesizes operational posture, risk indicators, and open regulatory actions across all shared banking capabilities into a structured readiness brief for COO and CRO review before board operations committee sessions, supervisory meetings, or investor operational due diligence. Each section covers the capability's throughput status, open risk items ranked by severity, and the forward-looking action summary. The COO and CRO enter each review from a cross-capability synthesis rather than a stack of individual team reports.
- Problem to solve: Before each board operations committee, supervisory dialogue, or investor review, the COO and CRO assemble a posture summary manually from eight separate capability teams, each producing its own status update independently. Synthesis into a coherent cross-capability operational narrative falls to the COO or a small team of senior analysts; the assembled brief captures static positions from the prior week rather than the current state across decisioning, payments, AML, onboarding, collections, servicing, pricing, and advisory operations. The manual assembly cycle creates a fixed preparation overhead before every governance or external engagement, compressing the time available for substance review and forward-looking judgment.
- Solution: The AI agent reads current-state operational metrics, open regulatory findings, and risk indicators from each shared capability system and assembles a structured readiness brief with a section per capability. Each section covers throughput status, open risk items ranked by severity, and the forward-looking action summary drawn from the capability team's latest inputs. The COO and CRO review the brief, annotate for context and forward judgment, and enter the meeting from a synthesized cross-capability view; manual assembly time is eliminated from the governance preparation cycle.
- OKR: A structured cross-capability readiness brief — covering throughput status, open risk items, and forward-looking action summaries for each shared banking capability — is available for COO and CRO review before board operations committee sessions, supervisory meetings, and investor operational due diligence.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced readiness brief used for ≥90% of board operations committee sessions, supervisory meetings, and investor operational due diligence events within year 1. |
| Acceptance | ≥85% of readiness briefs accepted by the COO and CRO as accurate and complete without requiring supplementary team reports; capability data accuracy confirmed against operational system records in ≥95% of reviewed briefs. |
| Cycle | Governance preparation time for the COO and CRO reduced from 1–2 days of manual multi-team assembly to ≤2 hours of brief review and annotation. |

### Cross-Capability Demand Signal

- URN: urn:financial-services:scenario:shared-banking-capabilities/cross-capability-demand-signal
- Lens: New opps
- Complexity: M
- Intent: The AI agent reads customer-journey signals across onboarding conversion, servicing contact drivers, complaint classifications, and advisory information requests on a monthly cadence, identifies co-movement patterns that point to common product or process upstream causes, and surfaces a ranked investment-gap list to the COO and product owners. Upstream causes generating correlated demand spikes across multiple capabilities are identified from the combined signal before they reach complaint-level volume or a formal review cycle. The ranked gap list provides the first cross-capability investment prioritization input for the COO and product owners from a shared evidence base.
- Problem to solve: Servicing contacts, onboarding friction, complaint patterns, and advisory requests accumulate in separate operational systems; a product change or process gap that generates downstream demand across multiple capabilities simultaneously is not visible as a single signal until it reaches complaint-level volume or a formal review cycle. The combined cross-capability signal — which would identify the upstream cause and quantify its demand footprint across onboarding, servicing, complaints, and advisory teams — is not assembled under current reporting practice. Product and process investment decisions are made without a ranked evidence base showing which upstream gaps generate the largest aggregate demand burden across the shared capability layer.
- Solution: The AI agent reads servicing contact classifications, onboarding drop-off points, complaint root-cause families, and advisory request patterns across the shared capability layer on a monthly cadence. It identifies co-movement across capability streams — product changes, regulatory updates, and seasonal patterns generating correlated demand spikes — and ranks upstream causes by total demand footprint. The COO and product owners receive a monthly ranked investment-gap list with capability-specific evidence for each identified gap; product and channel investment is directed toward the highest-burden upstream causes rather than within individual capability silos.
- OKR: A monthly ranked investment-gap list — identifying upstream product and process causes generating correlated demand spikes across onboarding, servicing, complaints, and advisory capabilities — is available to the COO and product owners from a shared cross-capability evidence base.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced cross-capability demand signal delivered for ≥10 of 12 monthly cycles in year 1; all four capability signal streams (onboarding, servicing, complaints, advisory) covered in each cycle. |
| Acceptance | ≥70% of upstream causes identified in the AI-produced ranked list confirmed as investment-relevant by the COO; cross-capability co-movement patterns validated against individual capability system records in ≥85% of reviewed months. |
| Cycle | Monthly cross-capability demand signal available within 5 business days of the month-end data close, vs. no systematic cross-capability signal in the prior process. |

### Regulatory Examination Pack Assembly

- URN: urn:financial-services:scenario:shared-banking-capabilities/regulatory-examination-pack-assembly
- Lens: Automation
- Complexity: L
- Intent: The AI agent assembles supervisory examination packs spanning shared capabilities — KYC, AML, credit decisioning, and payment investigations — from current policy, procedure, and data evidence, ready for Compliance review before regulator submission. It flags evidence gaps, inconsistencies between policy and practice narratives, and AML typology coverage gaps for Compliance to resolve before the pack is submitted. Assembly time compresses materially; Compliance effort concentrates on supervisory judgment and gap remediation.
- Problem to solve: Supervisory examinations request evidence packs across shared capabilities: KYC and CDD files, AML alert disposition records, credit decisioning audit trails, and payment investigation logs. Each examination requires Compliance teams to assemble evidence across capability owners manually over two to four weeks, pulling specialist time from ongoing operations and creating concentrated peak demand before each examination date. Evidence consistency across capability domains — between policy documents and system data, between AML typology coverage and actual alert dispositions — is verified under time pressure rather than on a maintained basis.
- Solution: The AI agent reads structured evidence from KYC, AML, credit, and payment systems and assembles the examination pack in the prescribed supervisory format. It flags evidence gaps, inconsistencies between policy and practice narratives, and AML typology coverage gaps, delivering a pre-reviewed pack for Compliance sign-off before regulator submission. Compliance effort concentrates on supervisory judgment, gap remediation, and forward-looking examination narrative rather than on evidence assembly.
- OKR: Supervisory examination packs spanning KYC, AML, credit decisioning, and payment investigations are assembled from current policy, procedure, and data evidence with evidence gaps and policy-to-practice inconsistencies flagged, ready for Compliance review before regulator submission.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced examination packs used for ≥90% of supervisory examinations within year 1. |
| Acceptance | ≥85% of examination packs accepted by Compliance for regulator submission without requiring material supplementary assembly; evidence gap rate (missing required component) ≤5% on Compliance review. |
| Cycle | Examination pack available for Compliance review within 5 business days of examination request, vs. 2–4 weeks of manual assembly in the prior process. |
