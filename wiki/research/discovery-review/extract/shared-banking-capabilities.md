# 

source: html-alt/financial-services/en/shared-banking-capabilities/index.html


[PAGE TEXT]
Operational capabilities
Credit decisioning (12)
Application underwriting
Scorecard & model performance (3)
·
Underwriter review & override (3)
Limit line management
Annual credit review (3)
·
Covenant monitoring (3)
Customer-facing capabilities
Customer servicing (18)
Inquiry case handling
Frontline policy & next-step copilot (3)
·
Customer interaction summarization & follow-up extraction (3)
·
Service intake & structured case skeleton (3)
·
Support ticket pattern mining (3)
Complaints conduct
Complaint response drafting & QA (3)
·
Complaint pattern & conduct analytics (3)
Capability governance
Capability Cycles (20)
Performance & improvement
Capability KPI & SLA review cycle (5)
Continuous improvement cycle (5)
Investment & sourcing
Capability investment cycle (5)
Vendor & sourcing review cycle (5)
Customer-facing capabilities
Customer onboarding (15)
Identity verification
KYC document extraction (3)
·
CDD risk classification (3)
·
Sanctions & PEP screening (3)
Activation cross sell
Account setup & activation (3)
·
Early cross-sell signals (3)
Operational capabilities
Transaction processing & settlement (12)
Payment processing
Payment failure & exception pattern analytics (3)
·
Investigation triage & next-step support (3)
Settlement reconciliation
Nostro reconciliation (3)
·
Case dossier builder (3)
Operational capabilities
Pricing & profitability (12)
Pricing models ftp
Pricing experiment analytics (3)
·
FTP & RAROC pricing signal (3)
Profitability attribution
Segment profitability deep-dive (3)
·
Profitability pack production (3)
Operational capabilities
Financial crime (12)
Fraud sanctions detection
Transaction monitoring alert triage (3)
·
False-positive root-cause analysis & rule tuning (3)
Aml investigations sar
AML alert investigation pack (3)
·
SAR drafting (3)
Operational capabilities
Collections & recoveries (15)
Early stage delinquency
Delinquency segmentation & contact strategy (3)
·
Promise-to-pay arrangement documentation (3)
·
Early warning & escalation signals (3)
Recovery operations
Legal referral triage (3)
·
Portfolio write-off & sale analysis (3)
Customer-facing capabilities
Advisory & research (12)
Investment research
Earnings call synthesis (3)
·
Issuer & sector research note drafting (3)
Advisory content production
Client suitability assessment (3)
·
Portfolio review narratives (3)
Scenarios
Lens
Scenario
Intent
Complexity

### CARD 1 [Insights|M] Shared Capability Health Dashboard
urn: urn:financial-services:scenario:shared-banking-capabilities/shared-capability-health-dashboard
intent: Agent assembles an integrated operational health view across credit decisioning, transaction exceptions, AML alert queue, and collections delinquency on a weekly cadence for COO review. The composite narrative covers decisioning approval rates and override ratios, payment exception volume and age, AML alert queue depth and disposition rates, and delinquency roll rates and contact effectiveness. COO reviews the agent-generated summary; capability leads provide forward-looking commentary.
Problem to solve: Operational capability teams report separately — credit decisioning through the Risk Committee, payment exceptions through Operations, AML through Compliance, and collections through the Collections Director. The COO has no composite view of shared-capability throughput and backlog status between formal reporting cycles. Emerging pressures — rising exception rates, growing AML queues, scorecard drift — reach the COO only after accumulation into a supervisory or P&L event.
Solution: Agent reads throughput and exception feeds from each operational capability system on a weekly cadence and assembles a composite dashboard narrative. Each capability section covers approval or processing rates, backlog depth and age, and emerging quality signals relative to prior periods. COO reviews the agent-generated summary; capability leads add forward-looking commentary where the operational signal warrants escalation.
OKR objective: An integrated operational health view across credit decisioning, payment exceptions, AML alert queue, and collections delinquency is available to the COO each week, with composite throughput and backlog status covering all four capability domains.
OKR KR [Adoption]: Agent-produced shared capability health dashboard delivered for ≥48 of 52 weeks in year 1; all four capability domains covered in each weekly summary.
OKR KR [Acceptance]: ≥85% of weekly dashboard summaries accepted by the COO as accurate without requiring supplementary capability team reports; composite operational signals validated against capability system records in ≥90% of reviewed weeks.
OKR KR [Cycle]: Weekly dashboard summary available each Monday morning, vs. composite visibility only at formal quarterly reporting cycles in the prior process.

### CARD 2 [Enablement|M] Cross-Capability Operations Readiness Brief
urn: urn:financial-services:scenario:shared-banking-capabilities/cross-capability-operations-readiness-brief
intent: Agent synthesises operational posture, risk indicators, and open regulatory actions across all shared banking capabilities into a structured readiness brief for COO and CRO review before board operations committee sessions, supervisory meetings, or investor operational due diligence. Each section covers the capability's throughput status, open risk items ranked by severity, and the forward-looking action summary. COO and CRO enter each review from a cross-capability synthesis rather than a stack of individual team reports.
Problem to solve: Before each board operations committee, supervisory dialogue, or investor review, the COO and CRO assemble a posture summary manually from eight separate capability teams, each producing its own status update independently. Synthesis into a coherent cross-capability operational narrative falls to the COO or a small team of senior analysts; the assembled brief captures static positions from the prior week rather than the current-state across decisioning, payments, AML, onboarding, collections, servicing, pricing, and advisory operations. The manual assembly cycle creates a fixed preparation overhead before every governance or external engagement, compressing the time available for substance review and forward-looking judgment.
Solution: Agent reads current-state operational metrics, open regulatory findings, and risk indicators from each shared capability system and assembles a structured readiness brief with a section per capability. Each section covers throughput status, open risk items ranked by severity, and the forward-looking action summary drawn from the capability team's latest inputs. COO and CRO review the brief, annotate for context and forward judgment, and enter the meeting from a synthesised cross-capability view; manual assembly time is eliminated from the governance preparation cycle.
OKR objective: A structured cross-capability readiness brief — covering throughput status, open risk items, and forward-looking action summaries for each shared banking capability — is available for COO and CRO review before board operations committee sessions, supervisory meetings, and investor operational due diligence.
OKR KR [Adoption]: Agent-produced readiness brief used for ≥90% of board operations committee sessions, supervisory meetings, and investor operational due diligence events within year 1.
OKR KR [Acceptance]: ≥85% of readiness briefs accepted by the COO and CRO as accurate and complete without requiring supplementary team reports; capability data accuracy confirmed against operational system records in ≥95% of reviewed briefs.
OKR KR [Cycle]: Governance preparation time for the COO and CRO reduced from 1–2 days of manual multi-team assembly to ≤2 hours of brief review and annotation.

### CARD 3 [New opps|M] Cross-Capability Demand Signal
urn: urn:financial-services:scenario:shared-banking-capabilities/cross-capability-demand-signal
intent: Agent reads customer-journey signals across onboarding conversion, servicing contact drivers, complaint classifications, and advisory information requests on a monthly cadence, identifies co-movement patterns that point to common product or process upstream causes, and surfaces a ranked investment-gap list to the COO and product teams. Upstream causes generating correlated demand spikes across multiple capabilities are identified from the combined signal before they reach complaint-level volume or a formal review cycle. The ranked gap list provides the first cross-capability investment prioritisation input for the COO and product owners from a shared evidence base.
Problem to solve: Servicing contacts, onboarding friction, complaint patterns, and advisory requests accumulate in separate operational systems; a product change or process gap that generates downstream demand across multiple capabilities simultaneously is not visible as a single signal until it reaches complaint-level volume or a formal review cycle. The combined cross-capability signal — which would identify the upstream cause and quantify its demand footprint across onboarding, servicing, complaints, and advisory teams — is not assembled under current reporting practice. Product and process investment decisions are made without a ranked evidence base showing which upstream gaps generate the largest aggregate demand burden across the shared capability layer.
Solution: Agent reads servicing contact classifications, onboarding drop-off points, complaint root-cause families, and advisory request patterns across the shared capability layer on a monthly cadence. It identifies co-movement across capability streams — product changes, regulatory updates, and seasonal patterns generating correlated demand spikes — and ranks upstream causes by total demand footprint. The COO and product owners receive a monthly ranked investment-gap list with capability-specific evidence for each identified gap; product and channel investment is directed toward the highest-burden upstream causes rather than within individual capability silos.
OKR objective: A monthly ranked investment-gap list — identifying upstream product and process causes generating correlated demand spikes across onboarding, servicing, complaints, and advisory capabilities — is available to the COO and product teams from a shared cross-capability evidence base.
OKR KR [Adoption]: Agent-produced cross-capability demand signal delivered for ≥10 of 12 monthly cycles in year 1; all four capability signal streams (onboarding, servicing, complaints, advisory) covered in each cycle.
OKR KR [Acceptance]: ≥70% of upstream causes identified in the agent-produced ranked list confirmed as investment-relevant by the COO; cross-capability co-movement patterns validated against individual capability system records in ≥85% of reviewed months.
OKR KR [Cycle]: Monthly cross-capability demand signal available within 5 business days of the month-end data close, vs. no systematic cross-capability signal in the prior process.

### CARD 4 [Automation|L] Regulatory Examination Pack Assembly
urn: urn:financial-services:scenario:shared-banking-capabilities/regulatory-examination-pack-assembly
intent: Agent assembles supervisory examination packs spanning shared capabilities — KYC, AML, credit decisioning, and payment investigations — from current policy, procedure, and data evidence, ready for Compliance review before regulator submission. It flags evidence gaps, inconsistencies between policy and practice narratives, and AML typology coverage gaps for Compliance resolution before regulator submission. Assembly time compresses materially; Compliance effort concentrates on supervisory judgment and gap remediation.
Problem to solve: NBKR, NBK/ARDFM, and CBR supervisory examinations request evidence packs across shared capabilities: KYC and CDD files, AML alert disposition records, credit decisioning audit trails, and payment investigation logs. Each examination requires Compliance teams to assemble evidence across capability owners manually over two to four weeks, pulling specialist time from ongoing operations and creating concentrated peak demand before each examination date. Evidence consistency across capability domains — between policy documents and system data, between AML typology coverage and actual alert dispositions — is verified under time pressure rather than on a maintained basis.
Solution: Agent reads structured evidence from KYC, AML, credit, and payment systems and assembles the examination pack in the prescribed supervisory format. It flags evidence gaps, inconsistencies between policy and practice narratives, and AML typology coverage gaps, delivering a pre-reviewed pack for Compliance sign-off before regulator submission. Compliance effort concentrates on supervisory judgment, gap remediation, and forward-looking examination narrative rather than on evidence assembly.
OKR objective: Supervisory examination packs spanning KYC, AML, credit decisioning, and payment investigations are assembled from current policy, procedure, and data evidence with evidence gaps and policy-to-practice inconsistencies flagged, ready for Compliance review before regulator submission.
OKR KR [Adoption]: Agent-produced examination packs used for ≥90% of NBKR, NBK/ARDFM, and CBR supervisory examinations within year 1.
OKR KR [Acceptance]: ≥85% of examination packs accepted by Compliance for regulator submission without requiring material supplementary assembly; evidence gap rate (missing required component) ≤5% on Compliance review.
OKR KR [Cycle]: Examination pack available for Compliance review within 5 business days of examination request, vs. 2–4 weeks of manual assembly in the prior process.

[PAGE TEXT]
GenAI-enabled Banking and Financial Services Framework · v11i
