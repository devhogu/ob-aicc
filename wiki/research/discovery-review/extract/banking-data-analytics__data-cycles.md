# 

source: html-alt/financial-services/en/banking-data-analytics/data-cycles/index.html


[PAGE TEXT]
Stewardship & quality
Data quality assessment cycle (BCBS 239)
Monthly data quality assessment across critical data elements — profile, score, issue, remediate, and retest — aligned to BCBS 239 Principles 2 and 3 (accuracy and integrity, completeness) and the bank's approved data quality dimensions. The cycle anchor is the interval from quality assessment to confirmed remediation.
The data quality assessment cycle is the bank's primary mechanism for measuring, managing, and improving the quality of its critical data elements (CDEs) — the data items that are material to risk aggregation, regulatory reporting, and business decision-making. Under BCBS 239 (Basel Committee on Banking Supervision Principles for Effective Risk Data Aggregation and Risk Reporting, January 2013), banks must establish a data architecture and quality framework that ensures risk data is accurate, complete, timely, consistent, and aggregated on demand. NBKR, NBK/ARDFM, and CBR each reference BCBS 239 principles in their supervisory expectations for systemically important banks.
The cycle runs monthly for CDE quality scoring and quarterly for a comprehensive quality assessment that includes all data dimensions — completeness, accuracy, timeliness, consistency, validity, and uniqueness — across the full operational and risk data estate. Data quality issues identified in the cycle feed a remediation pipeline managed by data domain stewards in coordination with IT and source-system owners.
GenAI can accelerate the cycle by automating data profiling across large CDE populations, classifying quality issues from profiling output, and drafting remediation plans from structured issue records — enabling the data quality team to process a larger CDE inventory per cycle without proportional headcount growth.
Analyze
CDE quality dimension scores are measured monthly but tracked informally between cycles. The CDO lacks a continuous-form view of the data quality trajectory — which CDEs are improving, which are stable, which are deteriorating — and the connection between quality trends and downstream risk reporting impact is not routinely surfaced.
Optimize
Remediation resource allocation across the issue backlog is not systematically optimised against downstream regulatory reporting impact. Issues in less-visible data domains that affect BCBS 239 risk aggregation may be deprioritised relative to issues in high-profile business reporting systems, creating a compliance exposure that the standard prioritisation process does not detect.
Automate
Data profiling execution, quality score calculation, issue classification from profiling output, and remediation plan drafting from structured issue records are structured, rule-based tasks applied to large data volumes each cycle. BCBS 239 quality dimension checks follow prescribed definitions amenable to agent-driven assessment with steward review.
Enrich
Data quality issue histories — root causes, remediation actions, and time-to-resolution — are held in individual issue records rather than in a structured knowledge base. Systematic patterns in quality failures — the same ETL transformation consistently producing null values for a category of CDEs — are not detected across the issue history, preventing pro-active engineering fixes from being prioritised.
<button
class="flow-stages__stage"
type="button"
data-stage="profile"
data-flow-id="urn:financial-services:flow:banking-data-analytics/data-quality-assessment-cycle"
>
Profile
→
<button
class="flow-stages__stage"
type="button"
data-stage="score"
data-flow-id="urn:financial-services:flow:banking-data-analytics/data-quality-assessment-cycle"
>
Score
→
<button
class="flow-stages__stage"
type="button"
data-stage="issue"
data-flow-id="urn:financial-services:flow:banking-data-analytics/data-quality-assessment-cycle"
>
Issue
→
<button
class="flow-stages__stage"
type="button"
data-stage="remediate"
data-flow-id="urn:financial-services:flow:banking-data-analytics/data-quality-assessment-cycle"
>
Remediate
→
<button
class="flow-stages__stage"
type="button"
data-stage="retest"
data-flow-id="urn:financial-services:flow:banking-data-analytics/data-quality-assessment-cycle"
>
Retest
Lens
Scenario
Intent
Complexity

### CARD 1 [Automation|S] CDE Profiling and Scoring Automation
urn: urn:financial-services:scenario:flow/banking-data-analytics/data-quality-assessment-cycle/dq-profiling-and-scoring-automation
intent: Agent executes the monthly CDE profiling run and quality dimension scoring across the full CDE inventory, applying BCBS 239 quality dimension definitions to each element and producing a scored output for steward review. Coverage extends to the complete approved CDE inventory rather than the subset reachable within the engineering team's available cycle capacity. The data quality team reviews scored output and approves the cycle results.
Problem to solve: Profiling coverage is incomplete each cycle — approximately 60–70% of identified CDEs are profiled — because onboarding new data sources to the profiling framework requires engineering effort that competes with other priorities. Quality dimension scoring is applied inconsistently by domain stewards when automated scoring is not available, reducing comparability across domains.
Solution: Agent applies pre-configured profiling rules across all onboarded source systems each month — null checks, range validation, referential integrity, format consistency, and duplicate detection — and translates profiling outputs into quality dimension scores using the approved BCBS 239 definitions. The scored output is delivered to domain stewards for review within the assessment cycle. Coverage gaps in non-onboarded sources are flagged separately for engineering prioritisation.
OKR objective: Monthly CDE profiling and quality dimension scoring extends to 100% of the approved CDE inventory, with BCBS 239 dimension definitions applied consistently across all domains and scored output delivered for steward review within the assessment cycle.
OKR KR [Adoption]: Agent executes the full monthly profiling run covering 100% of onboarded CDEs for ≥ 12 consecutive months; coverage gap flags for non-onboarded sources delivered to engineering prioritisation queue each cycle.
OKR KR [Acceptance]: ≥ 90% of scored outputs accepted by domain stewards without recalculation; BCBS 239 dimension scoring consistency validated as uniform across domains in ≥ 85% of monthly cycles.
OKR KR [Cycle]: Profiling coverage expanded from approximately 60–70% of the CDE inventory to 100% of onboarded CDEs without additional engineering resource per cycle.

### CARD 2 [Enablement|S] DQ Remediation Plan Drafting
urn: urn:financial-services:scenario:flow/banking-data-analytics/data-quality-assessment-cycle/dq-remediation-plan-drafting
intent: For each prioritised data quality issue, agent generates a structured remediation plan from the issue record — root-cause hypothesis, recommended remediation action, responsible IT owner, and target retest date — enabling data stewards to initiate remediation without a manual drafting step. The steward reviews and confirms the plan before IT engagement. Drafting quality is calibrated against the bank's remediation framework and BCBS 239 root-cause classification.
Problem to solve: Root-cause investigation for data quality issues requires the data quality team to trace the issue through the ETL pipeline to the source system; where lineage documentation is incomplete, investigations can consume days before root cause is identified. Each investigation and remediation plan is drafted from scratch by the steward, consuming time that could be redirected to higher-judgment quality work.
Solution: Agent reads the issue record — affected CDE, quality dimension failure, profiling output — and traverses available lineage documentation to produce a root-cause hypothesis and a pre-populated remediation plan covering recommended action, responsible IT owner derived from the CDE ownership registry, and a retest date proposal. The steward reviews, adjusts if required, and submits the plan to IT. Where lineage documentation is insufficient for automated traversal, the agent flags the gap for steward investigation.
OKR objective: Data stewards initiate remediation for each prioritised quality issue from an agent-generated plan covering root-cause hypothesis, recommended action, responsible IT owner, and target retest date, calibrated to the bank's BCBS 239 root-cause classification framework.
OKR KR [Adoption]: Agent generates a remediation plan for ≥ 90% of prioritised issues within 1 business day of issue confirmation; lineage-gap flags raised for ≥ 95% of issues where lineage documentation is insufficient for automated traversal.
OKR KR [Acceptance]: ≥ 80% of agent-generated plans confirmed and submitted to IT by stewards without material amendment; root-cause hypotheses validated against IT findings in ≥ 75% of closed issues.
OKR KR [Cycle]: Steward time per remediation plan reduced from manual investigation and drafting (typically half to a full day) to ≤ 1 hour of review and confirmation per issue.

### CARD 3 [Insights|M] CDE Quality Trajectory Monitor
urn: urn:financial-services:scenario:flow/banking-data-analytics/data-quality-assessment-cycle/dq-continuous-posture-monitor
intent: Agent monitors CDE quality dimension scores on a continuous basis between formal monthly assessments, surfacing deteriorating dimensions and downstream risk reporting impact to the CDO before the next scoring cycle. The dashboard tracks completeness, accuracy, timeliness, and consistency trajectories per CDE domain and flags CDEs where quality is trending below threshold. The CDO uses the trajectory view to direct pre-emptive steward engagement.
Problem to solve: Quality dimension scores are produced monthly and tracked informally between cycles. The CDO has no continuous view of which CDEs are deteriorating and cannot connect quality trends to downstream regulatory reporting impact without commissioning a manual extraction exercise. Deterioration that begins between cycles is visible only after the next formal scoring run.
Solution: Agent reads profiling outputs and quality scores as they are produced and maintains a running trajectory per CDE and domain. Dimensions trending below threshold trigger an alert with a downstream impact assessment identifying which BCBS 239 risk aggregation outputs and regulatory submissions consume the affected CDE. The CDO reviews the trajectory dashboard on a weekly cadence rather than waiting for the monthly cycle.
OKR objective: The CDO holds a continuous quality trajectory view per CDE domain between formal monthly assessments, with deteriorating dimensions and their downstream BCBS 239 impact surfaced on a weekly basis.
OKR KR [Adoption]: Agent maintains the continuous trajectory dashboard covering 100% of registered CDEs; weekly threshold-breach alerts issued for ≥ 95% of qualifying deteriorations within 12 months of go-live.
OKR KR [Acceptance]: ≥ 80% of threshold-breach alerts rated as requiring pre-emptive steward engagement by the CDO; downstream BCBS 239 impact assessments validated as accurate by the risk reporting team in ≥ 85% of alerts.
OKR KR [Cycle]: CDE quality deterioration surfaced within 7 days of the threshold crossing, compared to identification at the next formal monthly scoring cycle.

### CARD 4 [Optimize|M] DQ Remediation Impact Prioritisation
urn: urn:financial-services:scenario:flow/banking-data-analytics/data-quality-assessment-cycle/dq-remediation-impact-prioritisation
intent: Agent scores each open data quality issue by its downstream impact on BCBS 239 risk aggregation and regulatory submission accuracy, re-ordering the remediation backlog by regulatory materiality rather than issue visibility. The data quality team directs remediation resources to issues with the highest compliance exposure first. The CDO uses the ranked backlog to justify remediation resource allocation to the data governance council.
Problem to solve: Remediation resource allocation across the issue backlog is not systematically aligned to downstream regulatory reporting impact. Issues in less-visible data domains that affect BCBS 239 risk aggregation may be deprioritised relative to issues in high-profile business reporting systems, accumulating compliance exposure that the standard prioritisation process does not detect.
Solution: Agent maps each open issue to the downstream reports, risk metrics, and regulatory submissions that consume the affected CDE, scores impact by regulatory materiality, and re-orders the remediation queue accordingly. Issues affecting BCBS 239 risk aggregation CDEs and time-sensitive regulatory submissions are surfaced at the top of the queue with a compliance exposure summary. The data quality team reviews the ranked queue at the start of each remediation sprint.
OKR objective: The data quality team's remediation resources are directed by a regulatory-materiality-ranked backlog, with BCBS 239 risk aggregation CDEs and time-sensitive regulatory submissions surfaced at the top of each sprint queue.
OKR KR [Adoption]: Agent re-orders the remediation queue by regulatory materiality for ≥ 95% of sprint cycles within 12 months of go-live; downstream impact mapping covers 100% of open issues against the data catalog.
OKR KR [Acceptance]: ≥ 85% of top-ranked issues confirmed as correctly prioritised by the data quality team at sprint start; compliance exposure summary accepted without material revision for ≥ 80% of BCBS 239 material flags.
OKR KR [Cycle]: Remediation queue ranking available to the team at the start of each sprint, replacing end-of- sprint manual prioritisation reviews.

### CARD 5 [New opps|M] DQ Failure Pattern Knowledge Base
urn: urn:financial-services:scenario:flow/banking-data-analytics/data-quality-assessment-cycle/dq-failure-pattern-knowledge-base
intent: Agent mines the accumulated issue history across closed remediation cycles to detect systemic failure patterns — recurring root causes, ETL transformation categories producing disproportionate quality failures, source systems with persistent accuracy gaps — and surfaces them as a prioritised engineering programme for the CDO and data engineering lead. The pattern analysis shifts investment from reactive per-cycle remediation toward pro-active pipeline quality improvement. Detection runs quarterly against the closed-issue register.
Problem to solve: Data quality issue histories are held in individual issue records rather than a structured knowledge base. Systematic patterns — the same ETL transformation consistently producing null values for a category of CDEs, a specific source system repeatedly failing timeliness standards — are not detected across the issue history, and engineering investment in pipeline quality improvement is not informed by cumulative failure evidence.
Solution: Agent reads the closed-issue register across all completed remediation cycles, clusters issues by root-cause category, ETL transformation type, and source system, and identifies patterns where the same root cause appears across multiple CDEs or cycles. It produces a quarterly pattern report ranking systemic failure categories by cumulative quality impact and recommending engineering remediation actions with estimated CDE coverage benefit. The CDO uses the report to direct a pipeline quality investment programme alongside the standard per-cycle remediation effort.
OKR objective: The CDO directs pipeline quality investment using a quarterly pattern analysis of closed remediation issues, identifying systemic ETL failure categories and source-system gaps ranked by cumulative quality impact.
OKR KR [Adoption]: Agent produces the quarterly pattern report for ≥ 4 consecutive quarters within the first 12 months; analysis covers 100% of closed issues in the remediation register across all CDE domains.
OKR KR [Acceptance]: ≥ 80% of identified systemic failure patterns confirmed as actionable engineering priorities by the CDO and data engineering lead; pipeline quality investment programme initiated within 30 days of the first pattern report.
OKR KR [Cycle]: Cross-cycle systemic pattern identification cycle reduced from ad hoc manual retrospectives to a structured quarterly report delivered within 5 business days of quarter close.

[PAGE TEXT]
Master & reference data stewardship cycle
Quarterly master data governance cycle — CDE ownership definition, golden record curation, reference data refresh, and cross-domain consistency validation. The cycle anchor is the interval from data definition change to validated golden record publication.
The master and reference data stewardship cycle governs the bank's authoritative records for customers, counterparties, products, accounts, instruments, and the reference and code tables that classify transaction and risk data across the enterprise. Master data management — the practice of maintaining a single, accurate, and authoritative record for each critical entity — is foundational to BCBS 239 risk data aggregation; without consistent customer, counterparty, and instrument identifiers, risk aggregation across sub-systems produces inconsistent exposure pictures.
The cycle runs quarterly for comprehensive master data quality review and governance decisions — new CDE definitions, ownership changes, deduplication initiatives, and reference data refresh — with a monthly monitoring cadence for golden record quality scores. FATF customer due diligence (CDD) requirements and NBKR/NBK/ARDFM KYC data standards impose specific accuracy and completeness obligations on customer master data that the stewardship cycle must satisfy.
GenAI can support the cycle by automating deduplication candidate identification, enriching incomplete master data records from available sources, and drafting data stewardship decisions from structured governance inputs.
Analyze
Master data quality — golden record completeness, deduplication coverage, cross-domain identifier consistency — is assessed quarterly. The CDO lacks a continuous view of master data estate health between formal stewardship cycles and cannot quantify the impact of outstanding deduplication backlogs on downstream risk aggregation accuracy.
Optimize
Deduplication candidate review prioritisation is not systematically aligned to the downstream regulatory and risk impact of specific master data CDEs. High-volume, low-impact customer match pairs consume review capacity that would be better directed at counterparty and instrument CDEs that affect BCBS 239 risk aggregation.
Automate
Deduplication candidate identification from statistical matching, reference data refresh from authoritative external sources, cross-domain consistency validation queries, and data stewardship decision documentation are structured, high-volume tasks amenable to agent-assisted execution with steward review.
Enrich
Master data governance decisions and their downstream quality impacts are documented in individual meeting records rather than in a structured governance knowledge base. Recurring disputes — the same cross-domain identifier inconsistency arising from the same source system interface limitation — are resolved from first principles each time rather than through a catalogued resolution pattern.
<button
class="flow-stages__stage"
type="button"
data-stage="define"
data-flow-id="urn:financial-services:flow:banking-data-analytics/master-reference-data-cycle"
>
Define
→
<button
class="flow-stages__stage"
type="button"
data-stage="govern"
data-flow-id="urn:financial-services:flow:banking-data-analytics/master-reference-data-cycle"
>
Govern
→
<button
class="flow-stages__stage"
type="button"
data-stage="curate"
data-flow-id="urn:financial-services:flow:banking-data-analytics/master-reference-data-cycle"
>
Curate
→
<button
class="flow-stages__stage"
type="button"
data-stage="validate"
data-flow-id="urn:financial-services:flow:banking-data-analytics/master-reference-data-cycle"
>
Validate
→
<button
class="flow-stages__stage"
type="button"
data-stage="publish"
data-flow-id="urn:financial-services:flow:banking-data-analytics/master-reference-data-cycle"
>
Publish
Lens
Scenario
Intent
Complexity

### CARD 6 [Automation|S] Golden Record Deduplication Assist
urn: urn:financial-services:scenario:flow/banking-data-analytics/master-reference-data-cycle/golden-record-deduplication-assist
intent: Agent applies probabilistic matching across name variants, Cyrillic-Latin transliterations, tax identifiers, and address fields to produce scored deduplication candidates for data steward review on a weekly cadence, compressing the time from the quarterly governance decision to an actionable candidate queue. The data steward reviews high-confidence candidates and resolves edge cases; the MDM hub golden record is updated following steward approval. Lower-confidence candidates are queued for judgment review rather than auto-merged.
Problem to solve: Customer master data accumulates duplicate and inconsistent records across core banking, CRM, and KYC systems as entities are onboarded across channels and products. Deduplication campaigns are periodic, leaving the golden record stale between cycles. CIS market characteristics — Cyrillic-Latin transliterations, alias conventions, and thin tax-identifier coverage — compound the deduplication workload beyond what campaign-based steward review can clear within standard cycle capacity.
Solution: Agent reads entity records from all source systems weekly and applies probabilistic matching across name variants, transliterations, tax identifiers, and address fields, producing a confidence-scored candidate list. High-confidence matches are presented to the steward as a batch-approval track; edge cases and lower-confidence matches are queued for individual judgment review. The MDM hub golden record is updated following steward approval, with the merge decision and confidence score recorded in the governance log.
OKR objective: The MDM hub golden record for customer and entity master data is maintained at production quality on a weekly cadence through agent-assisted probabilistic deduplication, with high-confidence candidates batched for steward approval and edge cases queued for judgment review.
OKR KR [Adoption]: Agent produces deduplication candidate lists for ≥ 95% of weekly cadence cycles within 12 months of go-live; matching covers name variants, Cyrillic-Latin transliterations, tax identifiers, and address fields across all source systems.
OKR KR [Acceptance]: ≥ 80% of high-confidence batch candidates approved by stewards without individual judgment review; post-merge golden record accuracy verified at ≥ 95% in quarterly data quality assessments.
OKR KR [Cycle]: Deduplication cycle shifted from periodic quarterly campaigns to a continuous weekly cadence; golden record staleness window reduced from up to 3 months to ≤ 7 days.

### CARD 7 [Enablement|S] Master Data Governance Decision Documentation
urn: urn:financial-services:scenario:flow/banking-data-analytics/master-reference-data-cycle/governance-decision-documentation
intent: Agent produces structured governance decision records from data governance forum inputs — capturing the decision scope, rationale, affected CDEs, ownership assignments, and implementation actions — and indexes each record in a queryable knowledge base accessible to stewards, IT, and the data governance council. The governance secretary reviews and approves each record before it is published. The knowledge base enables recurrent disputes to be resolved by reference to prior decisions rather than from first principles.
Problem to solve: Master data governance decisions and their downstream quality impacts are documented in individual meeting minutes rather than a structured governance knowledge base. Recurring cross-domain disputes — the same identifier inconsistency arising from the same source system interface limitation — are resolved from first principles each time because prior decisions are not retrievable in a usable form. Stewards and IT owners lack a reference standard for disputed CDE ownership and quality expectations.
Solution: Agent reads governance forum meeting notes and structured decision inputs, extracts each decision, and generates a formal decision record — scope, rationale, affected CDEs, ownership assignments, and required IT implementation actions. Records are indexed by CDE, domain, decision type, and date and published to the governance knowledge base. At each forum, the agent retrieves relevant prior decisions for recurring agenda items and surfaces them to the chair before the session opens, reducing re-litigation of settled issues.
OKR objective: Data governance forum decisions are captured in structured, queryable records indexed by CDE, domain, and decision type, enabling stewards and IT to resolve recurring disputes by reference to prior decisions rather than from first principles.
OKR KR [Adoption]: Agent generates governance decision records for ≥ 95% of actionable forum decisions within 2 business days of each session; prior decision retrieval deployed for ≥ 100% of governance forum recurring agenda items.
OKR KR [Acceptance]: ≥ 85% of decision records approved by the governance secretary without material amendment; re-litigation rate for settled issues reduced by ≥ 50% year-on-year as measured by governance forum minutes.
OKR KR [Cycle]: Decision documentation turnaround reduced from end-of-meeting minutes (typically 3–5 business days) to approved records available within 2 business days; prior decisions surfaced to chair before each session.

### CARD 8 [Insights|M] Master Data Estate Health Monitor
urn: urn:financial-services:scenario:flow/banking-data-analytics/master-reference-data-cycle/master-data-estate-health-monitor
intent: Agent monitors golden record quality scores, deduplication coverage rates, and cross-domain identifier consistency across the master data estate on a continuous basis between quarterly stewardship cycles, surfacing deterioration and outstanding backlog impact to the CDO. The monitor tracks customer, counterparty, and instrument CDEs by domain and quantifies the BCBS 239 risk aggregation exposure from deduplication backlogs and cross-system identifier mismatches. The CDO uses the output for quarterly data governance council reporting.
Problem to solve: Master data quality is assessed quarterly; between cycles, gaps accumulate as deduplication backlogs grow and cross-system identifier consistency deteriorates without systematic detection. The CDO cannot quantify the impact of outstanding deduplication backlogs on downstream risk aggregation accuracy without commissioning a manual assessment. Board reporting on data quality relies on manual aggregation from domain-level inputs with no common scoring baseline.
Solution: Agent reads golden record quality metrics, deduplication coverage counts, and cross-domain identifier consistency scores from the MDM hub and producing systems on a weekly cadence. It maintains a continuous master data health dashboard per CDE domain with trailing quality trend lines and a deduplication backlog estimate expressed as a share of the total entity population. The BCBS 239 impact section quantifies how outstanding backlogs affect counterparty and instrument exposure aggregation accuracy.
OKR objective: The CDO monitors golden record quality, deduplication coverage, and cross-domain identifier consistency on a continuous weekly basis, with BCBS 239 risk aggregation exposure from outstanding backlogs quantified and reported to the data governance council quarterly.
OKR KR [Adoption]: Agent maintains the continuous master data health dashboard covering customer, counterparty, and instrument CDE domains for ≥ 48 weeks within the first 12 months; BCBS 239 impact section included in each quarterly governance council report.
OKR KR [Acceptance]: ≥ 85% of dashboard quality scores validated against MDM hub outputs by the governance team at quarterly review; BCBS 239 deduplication backlog impact estimates accepted by the risk reporting team as directionally accurate in ≥ 80% of quarters.
OKR KR [Cycle]: Master data health assessment cycle reduced from quarterly manual aggregation to a continuous weekly dashboard; governance council reporting prepared from dashboard output in ≤ 1 business day.

### CARD 9 [Optimize|M] Deduplication Candidate Impact Prioritisation
urn: urn:financial-services:scenario:flow/banking-data-analytics/master-reference-data-cycle/deduplication-impact-prioritisation
intent: Agent ranks the deduplication candidate queue by downstream regulatory and risk impact of the affected entity type, directing data steward review capacity toward counterparty and instrument CDEs that affect BCBS 239 risk aggregation ahead of high-volume, lower-impact retail customer match pairs. The ranking integrates entity type, exposure materiality, and consuming report dependency to produce a steward review schedule aligned to BCBS 239 compliance obligations. The data governance lead uses the ranked schedule to allocate the steward team's review capacity.
Problem to solve: Deduplication candidate review prioritisation is not systematically aligned to the downstream regulatory and risk impact of specific master data CDEs. High-volume retail customer match pairs consume review capacity that would produce higher compliance value if directed at counterparty and instrument CDEs material to BCBS 239 risk aggregation. The curation backlog accumulates across cycles without differentiation by entity materiality.
Solution: Agent reads the deduplication candidate queue and maps each entity type and candidate pair to downstream risk and regulatory report dependencies sourced from the data catalog. It scores each pair by entity type materiality — counterparty and instrument CDEs used in BCBS 239 aggregation receive the highest weight — and produces a ranked steward review schedule. High-confidence retail pairs above a defined match threshold are separated into a batch-approval track, reserving the judgment queue for high-materiality, lower-confidence matches.
OKR objective: The data steward team's review capacity is directed toward counterparty and instrument CDE deduplication candidates with the highest BCBS 239 risk aggregation materiality, with high-volume retail pairs managed through a separate batch-approval track.
OKR KR [Adoption]: Agent produces a ranked steward review schedule for ≥ 95% of weekly deduplication candidate queues within 12 months of go-live; batch-approval track active for high-confidence retail pairs from go-live.
OKR KR [Acceptance]: ≥ 85% of materiality-based prioritisation rankings confirmed as correctly ordered by the data governance lead; BCBS 239 material CDE backlog cleared at a rate ≥ 50% faster than pre-agent baseline within 12 months.
OKR KR [Cycle]: Counterparty and instrument CDE deduplication queue clearance rate improved from quarterly campaign-based review to a continuous weekly steward cadence.

### CARD 10 [New opps|M] Reference Data Change Impact Map
urn: urn:financial-services:scenario:flow/banking-data-analytics/master-reference-data-cycle/reference-data-change-impact-map
intent: When a reference data or taxonomy change is approved in the governance cycle — a revised NBKR product code, an updated FIBO entity classification, a new CBR sector definition — agent traces the downstream impact across all consuming systems and reports before publication and produces a prioritised propagation plan ranked by submission deadline. The data governance team uses the plan to coordinate the propagation sprint before the next regulatory submission cycle. Each consuming system receives a data transformation note describing the mapping from the prior to the revised classification.
Problem to solve: Reference data taxonomy changes propagate inconsistently across systems when the governance team manually identifies affected downstream assets. Consuming systems filing against superseded classifications continue to do so until individually updated, creating a compliance exposure window. For NBKR and CBR submission cycles, the propagation lag is a regulatory filing risk that is managed reactively rather than through a pre-publication impact assessment.
Solution: Agent reads the approved reference data change and queries the enterprise data catalog for all downstream assets referencing the affected code or classification. It produces a system-by-system, report-by-report impact map with update priority ranked by submission deadline and regulatory materiality. For each consuming system, it drafts a data transformation note covering the field-level mapping from prior to revised classification. The data governance team uses the impact map and transformation notes to plan and sequence the propagation sprint before the next submission deadline.
OKR objective: When a reference data or taxonomy change is approved in the governance cycle, the data governance team receives a system-by-system, report-by-report impact map with a propagation plan ranked by submission deadline before publication, accompanied by a data transformation note for each consuming system.
OKR KR [Adoption]: Agent produces the impact map and transformation notes for ≥ 95% of approved reference data changes within 12 months of go-live; coverage extends to all consuming systems in the enterprise data catalog.
OKR KR [Acceptance]: ≥ 85% of impact maps accepted by the data governance team as complete and correctly prioritised without material additions; transformation notes validated as field-level accurate in ≥ 90% of consuming systems.
OKR KR [Cycle]: Impact map delivered within 3 business days of governance approval, enabling propagation sprint planning before the next regulatory submission deadline for ≥ 90% of approved changes.

[PAGE TEXT]
Lineage & control attestation cycle
Semi-annual data lineage mapping and control attestation cycle — documenting the end-to-end path from source to regulatory report field, testing transformation controls, and attesting lineage accuracy for BCBS 239 supervisory compliance. The cycle anchor is the interval from pipeline change to updated, attested lineage documentation.
The lineage and control attestation cycle documents the end-to-end data lineage for each critical data element — the traceable path from origination in a source system through every ETL transformation, aggregation step, and system boundary to the regulatory report field or risk metric where it is consumed. BCBS 239 Principle 6 (timeliness) and Principle 7 (adaptability) require that banks be able to generate accurate aggregated risk data on demand; effective lineage documentation is the enabler that makes on-demand aggregation possible and auditable.
The cycle runs semi-annually for full lineage review and attestation. Between cycles, lineage documentation is updated on a change-triggered basis — when a source system changes, when a pipeline is modified, or when a new regulatory reporting field is introduced. The attestation step requires the data governance team and data domain owners to sign off that documented lineage accurately reflects the production pipeline configuration.
GenAI can support the cycle by automatically traversing pipeline metadata to generate draft lineage documentation, comparing documented lineage against actual pipeline configurations to identify undocumented changes, and drafting attestation-ready lineage summaries for steward review.
Analyze
Lineage documentation currency — how many CDEs have lineage documentation that matches the current production configuration — is not measured continuously. The CDO cannot answer the BCBS 239 question of whether the institution''s risk data aggregation capability is audit-ready without commissioning a manual coverage assessment.
Optimize
Lineage mapping effort is allocated to CDEs that are in scope for the current attestation cycle, based on the prior cycle's scope definition. CDEs that have changed their production pipeline configuration between attestation cycles are not re-attested until the next full cycle, creating a window of unattested lineage change that accumulates without systematic detection.
Automate
Pipeline metadata traversal for lineage discovery, transformation logic documentation from ETL script parsing, control total comparison across pipeline boundaries, and attestation-ready lineage summary drafting are structured technical tasks that follow repeatable patterns amenable to agent-assisted execution with engineering and governance review.
Enrich
Prior attestation findings — lineage gaps, control test failures, and documentation deficiencies identified in previous cycles — are documented in attestation reports but not synthesised into a pattern analysis that would prioritise systematic pipeline quality improvements over individual cycle remediations.
<button
class="flow-stages__stage"
type="button"
data-stage="map"
data-flow-id="urn:financial-services:flow:banking-data-analytics/lineage-control-attestation-cycle"
>
Map
→
<button
class="flow-stages__stage"
type="button"
data-stage="document"
data-flow-id="urn:financial-services:flow:banking-data-analytics/lineage-control-attestation-cycle"
>
Document
→
<button
class="flow-stages__stage"
type="button"
data-stage="test"
data-flow-id="urn:financial-services:flow:banking-data-analytics/lineage-control-attestation-cycle"
>
Test controls
→
<button
class="flow-stages__stage"
type="button"
data-stage="attest"
data-flow-id="urn:financial-services:flow:banking-data-analytics/lineage-control-attestation-cycle"
>
Attest
→
<button
class="flow-stages__stage"
type="button"
data-stage="renew"
data-flow-id="urn:financial-services:flow:banking-data-analytics/lineage-control-attestation-cycle"
>
Renew
Lens
Scenario
Intent
Complexity

### CARD 11 [Optimize|S] Change-Triggered Lineage Update Prioritisation
urn: urn:financial-services:scenario:flow/banking-data-analytics/lineage-control-attestation-cycle/change-triggered-lineage-prioritisation
intent: Agent monitors the production deployment pipeline and flags each release that modifies a CDE lineage path, creating a prioritised lineage update queue ranked by the regulatory materiality of the affected CDEs. The data governance team processes update requests as they arise rather than absorbing a large undocumented change backlog at each semi-annual attestation. CDEs with the highest BCBS 239 materiality receive lineage update requests on the same sprint cycle as the pipeline change that affects them.
Problem to solve: Change-driven lineage updates depend on the data engineering team flagging pipeline changes to the data governance function. The change management process does not consistently trigger lineage update requirements; pipeline changes that alter CDE lineage paths are implemented without corresponding documentation updates, creating an accumulating divergence between documented and production lineage that the semi-annual attestation cycle must absorb in a compressed window.
Solution: Agent reads deployment release notes and pipeline change logs from the production change management system and identifies releases that modify ETL transformations, data source connections, or aggregation logic for any registered CDE. For each qualifying change, it creates a lineage update ticket ranked by the CDE's regulatory materiality and assigns it to the responsible data domain steward. The governance function has a continuously updated queue rather than a semi-annual backlog. Changes to BCBS 239 material CDEs produce update tickets on the same sprint cycle as the deployment.
OKR objective: Every production deployment that modifies a CDE lineage path generates a lineage update ticket within the same sprint cycle, ranked by the regulatory materiality of the affected CDE.
OKR KR [Adoption]: Agent monitors ≥ 95% of production deployments within 12 months of go-live; lineage update tickets raised for ≥ 90% of qualifying deployments within 2 business days of release.
OKR KR [Acceptance]: ≥ 85% of raised tickets accepted by data domain stewards as correctly scoped and prioritised without reclassification; BCBS 239 material CDE tickets closed within the same sprint cycle in ≥ 80% of cases.
OKR KR [Cycle]: Attestation-cycle lineage backlog from undocumented pipeline changes reduced by ≥ 70% year-on-year as measured against the prior semi-annual attestation volume.

### CARD 12 [Automation|S] Lineage Documentation Automation
urn: urn:financial-services:scenario:flow/banking-data-analytics/lineage-control-attestation-cycle/lineage-documentation-automation
intent: Agent traverses production ETL scripts and pipeline metadata to generate draft business-readable lineage documentation for each CDE — source system and field, each transformation step with a business-readable logic description, intermediate data stores, and consuming regulatory report fields — for data steward review and approval. The steward reviews the draft for accuracy and approves it for publication to the data catalog. Lineage documentation cycle time is compressed from weeks to days for each CDE in scope.
Problem to solve: Lineage documentation quality is constrained by the competing demands on data engineering time. Documentation written under production pressure uses technical descriptions not readable to business stakeholders or supervisors; the business-readable translation step is typically deferred to the attestation cycle and performed under deadline pressure. Pipeline metadata contains the information needed for accurate lineage documentation but it is not automatically surfaced in a business-readable form.
Solution: Agent reads ETL scripts, transformation configuration files, and data catalog metadata for the CDE in scope and generates a structured lineage record in business-readable form: source system and field, each transformation step with a plain-language description of the logic applied, intermediate staging tables, and the regulatory report field or risk metric where the CDE is consumed. Technical terms are translated using the approved data dictionary. The data steward reviews the draft lineage record for accuracy and approves it for publication to the data catalog.
OKR objective: Data stewards receive agent-generated business-readable draft lineage documentation for each CDE — from source field through every transformation step to consuming regulatory report field — for review and approval before publication to the data catalog.
OKR KR [Adoption]: Agent produces draft lineage records for ≥ 90% of CDEs queued for documentation within 12 months of go-live; coverage extends to all onboarded source systems and ETL pipeline configurations.
OKR KR [Acceptance]: ≥ 80% of draft lineage records approved by data stewards without material amendment; business- readable translation accuracy validated against approved data dictionary in ≥ 90% of records.
OKR KR [Cycle]: Lineage documentation cycle time per CDE reduced from weeks of manual technical translation to ≤ 3 business days from agent draft to steward approval.

### CARD 13 [Enablement|S] Lineage Attestation Pack Drafting
urn: urn:financial-services:scenario:flow/banking-data-analytics/lineage-control-attestation-cycle/attestation-pack-drafting
intent: Agent produces an attestation-ready lineage summary per CDE — source path, transformation steps in plain language, control test results, and a comparison of current documentation against the production configuration — enabling data domain owners to conduct a substantive attestation review rather than a formality sign-off. The data domain owner reviews the summary and attests to its accuracy; the agent does not attest on the owner's behalf. The governance team uses the signed attestation packs as the evidence base for BCBS 239 supervisory examination defense.
Problem to solve: Attestation by data domain owners requires owners to review lineage documentation that is often technically dense. Domain owners who are not data engineering specialists cannot meaningfully assess whether the documented transformation logic matches the production configuration without a readability translation step. Attestation becomes a formality rather than a substantive assurance step, reducing the governance value of the cycle for BCBS 239 supervisory purposes.
Solution: Agent reads the current lineage documentation for each CDE in the attestation scope, reformats it into a domain-owner-readable summary covering source path, key transformation logic in plain language, control test results from the current cycle, and a flag for any differences between the documented and production configuration identified by the currency monitor. The summary is delivered to the domain owner as a structured attestation pack. The domain owner reviews the summary, resolves any flagged differences, and signs the attestation record.
OKR objective: Data domain owners conduct substantive BCBS 239 attestation reviews using agent-generated attestation packs that present CDE lineage and control test results in business-readable form.
OKR KR [Adoption]: Agent-generated attestation packs cover 100% of CDEs in the attestation scope for ≥ 2 consecutive semi-annual cycles within 12 months of go-live; delivery completed ≥ 5 business days before the attestation sign-off deadline.
OKR KR [Acceptance]: ≥ 85% of agent-generated packs accepted by domain owners without material amendment; documented and production configuration divergence flags resolved by domain owners in ≥ 90% of cases before sign-off.
OKR KR [Cycle]: Per-CDE attestation pack preparation time reduced from days of manual documentation review to ≤ 2 hours of domain owner review per CDE.

### CARD 14 [Insights|M] Lineage Documentation Currency Dashboard
urn: urn:financial-services:scenario:flow/banking-data-analytics/lineage-control-attestation-cycle/lineage-currency-dashboard
intent: Agent compares documented lineage records in the data catalog against current production pipeline configurations on a continuous basis, quantifying the share of CDEs with lineage documentation that accurately reflects the production state. The currency dashboard gives the CDO a real-time BCBS 239 audit-readiness signal without commissioning a manual assessment exercise. CDEs with undocumented pipeline changes are ranked by regulatory materiality to prioritise the documentation backlog.
Problem to solve: Lineage documentation currency — the share of CDEs with lineage documentation matching the current production configuration — is not measured continuously. The CDO cannot answer the BCBS 239 audit-readiness question without commissioning a manual coverage assessment, and undocumented pipeline changes accumulate between attestation cycles without systematic detection.
Solution: Agent reads pipeline metadata from production ETL and data pipeline configurations and compares each pipeline segment against the current lineage documentation in the data catalog. CDEs where the production configuration differs from the documented lineage are flagged as stale, with the nature of the change and its downstream impact on regulatory reporting noted. The currency score — percentage of CDEs with current, accurate lineage documentation — is updated weekly and presented on the BCBS 239 readiness dashboard.
OKR objective: The CDO holds a continuous BCBS 239 audit-readiness signal expressed as the share of CDEs with lineage documentation accurately reflecting the current production pipeline configuration, updated weekly and ranked by regulatory materiality.
OKR KR [Adoption]: Agent updates the lineage currency score on a weekly cadence covering 100% of in-scope CDEs for ≥ 48 weeks within the first 12 months; stale documentation flags raised for ≥ 95% of qualifying pipeline-to-documentation divergences.
OKR KR [Acceptance]: ≥ 90% of stale documentation flags confirmed as genuine divergences by data governance team; lineage currency score validated against the semi-annual attestation findings in ≥ 95% of CDEs.
OKR KR [Cycle]: Audit-readiness assessment cycle reduced from a commissioned manual coverage assessment (typically weeks) to a weekly automated score available within 1 business day of the pipeline metadata read.

### CARD 15 [New opps|M] Attestation Findings Pattern Synthesis
urn: urn:financial-services:scenario:flow/banking-data-analytics/lineage-control-attestation-cycle/attestation-findings-pattern-synthesis
intent: Agent synthesises attestation findings across cycles — lineage gaps, control test failures, documentation deficiencies, and undocumented pipeline changes — into a pattern analysis that ranks systemic pipeline quality weaknesses by frequency and BCBS 239 materiality. The CDO and data engineering lead use the pattern analysis to direct a structured pipeline quality improvement programme alongside the standard per-cycle remediation effort. The analysis runs after each semi-annual attestation cycle closes.
Problem to solve: Prior attestation findings are documented in attestation reports but not synthesised into a cross-cycle pattern analysis. Lineage gaps, recurring control test failures, and documentation deficiencies identified in one cycle reappear in the next because they are addressed as individual findings rather than as symptoms of systemic pipeline quality weaknesses. The attestation cycle produces compliance evidence but does not generate a pro-active engineering improvement programme.
Solution: Agent reads attestation reports from the preceding cycles, classifies each finding by type — lineage gap, control test failure, documentation deficiency, undocumented change — and clusters findings by affected pipeline segment, ETL system, and CDE domain. It produces a pattern synthesis ranking systemic weaknesses by recurrence frequency and BCBS 239 materiality, with a recommended engineering remediation prioritisation. The CDO presents the pattern synthesis to the data engineering lead at the close of each attestation cycle as the basis for a pipeline quality investment plan.
OKR objective: The CDO and data engineering lead direct pipeline quality investment using a cross-cycle attestation findings pattern synthesis ranked by recurrence frequency and BCBS 239 materiality.
OKR KR [Adoption]: Agent produces a pattern synthesis after ≥ 2 consecutive semi-annual attestation cycle closings within the first 12 months, covering 100% of classified finding types across all in-scope pipeline segments and CDE domains.
OKR KR [Acceptance]: ≥ 80% of ranked systemic weaknesses rated decision-relevant by the CDO and data engineering lead without material reclassification; engineering remediation programme initiated within 30 days of each synthesis delivery.
OKR KR [Cycle]: Pattern synthesis delivered to the CDO within 5 business days of attestation cycle close, replacing a manual cross-cycle finding review that was not previously performed.

[PAGE TEXT]
Submission & disclosure
Regulatory data submission cycle
Monthly and quarterly regulatory data submissions to NBKR, NBK/ARDFM, and CBR — data aggregation, format validation, submission, post-submission reconciliation, and supervisory query resolution. Aligned to BCBS 239 data aggregation requirements and CIS regulatory submission standards.
The regulatory data submission cycle governs the bank's periodic data submissions to NBKR (Kyrgyz Republic), NBK/ARDFM (Kazakhstan), and CBR (Russia) — the prescribed datasets that underpin prudential supervision, financial stability monitoring, and statistical reporting. Each supervisor publishes its own submission forms, validation rules, and electronic submission protocols. For banking groups with operations across multiple CIS jurisdictions, the submission cycle runs in parallel across three regulatory perimeters with different calendars, formats, and data definitions.
BCBS 239 Principle 2 (data accuracy and integrity) requires that the bank be able to produce complete, accurate, and timely regulatory data for supervisors. The submission cycle is the operational expression of BCBS 239 compliance — the recurring test of whether the data architecture and quality framework are performing to standard. Supervisory data requests outside the standard submission calendar — ad hoc requests arising from supervisory investigation, on-site inspection, or financial stability analysis — must be fulfilled on demand from the same data infrastructure.
GenAI can support the cycle by automating data aggregation validation commentary, drafting explanatory notes for submission exceptions, and triage supervisory query response packs from the lineage documentation and data quality record.
Analyze
Submission performance — validation failure rates, exception volumes, query frequencies by supervisor — is tracked informally by the regulatory reporting team but not aggregated into a quality trend analysis across submissions and supervisors. The CDO cannot produce a BCBS 239 compliance scorecard without manual extraction from submission records.
Optimize
Validation exception resolution is performed sequentially by the reporting team against each supervisor's deadline. Cross-supervisor pattern analysis — identifying data quality issues that consistently generate exceptions across multiple supervisors because they originate in the same source system — is not applied within the standard submission cycle.
Automate
Regulatory submission aggregation commentary, validation exception explanatory notes, post-submission reconciliation difference commentary, and supervisory query response drafts are structured writing tasks with consistent frameworks. BCBS 239 lineage traversal for specific CDE data points follows a reproducible path from source to submitted value amenable to agent-assisted response generation.
Enrich
Supervisory query histories across NBKR, NBK/ARDFM, and CBR — which data points were challenged, which explanations were accepted, which methodology changes were requested — accumulate in individual query files rather than in a consolidated knowledge base. Each query cycle re-performs the investigation and drafting effort that prior cycle responses could have informed.
<button
class="flow-stages__stage"
type="button"
data-stage="aggregate"
data-flow-id="urn:financial-services:flow:banking-data-analytics/regulatory-data-submission-cycle"
>
Aggregate
→
<button
class="flow-stages__stage"
type="button"
data-stage="validate"
data-flow-id="urn:financial-services:flow:banking-data-analytics/regulatory-data-submission-cycle"
>
Validate
→
<button
class="flow-stages__stage"
type="button"
data-stage="submit"
data-flow-id="urn:financial-services:flow:banking-data-analytics/regulatory-data-submission-cycle"
>
Submit
→
<button
class="flow-stages__stage"
type="button"
data-stage="reconcile"
data-flow-id="urn:financial-services:flow:banking-data-analytics/regulatory-data-submission-cycle"
>
Reconcile
→
<button
class="flow-stages__stage"
type="button"
data-stage="resolve"
data-flow-id="urn:financial-services:flow:banking-data-analytics/regulatory-data-submission-cycle"
>
Resolve queries
Lens
Scenario
Intent
Complexity

### CARD 16 [Automation|S] Regulatory Submission Commentary Automation
urn: urn:financial-services:scenario:flow/banking-data-analytics/regulatory-data-submission-cycle/submission-commentary-automation
intent: Agent drafts the standard narrative components of the regulatory submission package — data aggregation methodology commentary, validation exception explanatory notes, and post-submission reconciliation difference commentary — from structured data inputs and prior-period reference text. The regulatory reporting team reviews and approves each component before submission or response. Drafting effort across three regulatory perimeters is compressed from days to hours per cycle.
Problem to solve: Regulatory submission aggregation commentary, validation exception explanatory notes, and post-submission reconciliation difference commentary are structured writing tasks performed manually each cycle. For three regulatory perimeters with different form structures and commentary requirements, the drafting effort accumulates to a material portion of the regulatory reporting team's cycle capacity, reducing time available for data quality investigation.
Solution: Agent reads the aggregated submission dataset, validation exception report, and prior-period commentary for each supervisor and produces draft narrative components aligned to each supervisor's prescribed format and the bank's standard methodology descriptions. Exception explanatory notes are generated from exception metadata and available root-cause classification. The regulatory reporting team reviews each draft, applies professional judgment on exceptions requiring methodological explanation, and approves before submission or response.
OKR objective: The regulatory reporting team reviews and approves agent-drafted narrative components — aggregation methodology commentary, validation exception explanatory notes, and post-submission reconciliation difference commentary — before each submission or supervisory response across all three regulatory perimeters.
OKR KR [Adoption]: Agent produces draft narrative components for ≥ 90% of submission cycles across NBKR, NBK/ARDFM, and CBR perimeters within 12 months of go-live; all prescribed commentary sections covered in each draft.
OKR KR [Acceptance]: ≥ 85% of draft components accepted by the regulatory reporting team without material methodological revision; exception explanatory notes rated as accurate in ≥ 90% of cases by the team lead.
OKR KR [Cycle]: Commentary drafting effort per submission cycle reduced from days of manual writing across three perimeters to ≤ 4 hours of team review and approval per cycle.

### CARD 17 [Enablement|S] Supervisory Query Response Assistant
urn: urn:financial-services:scenario:flow/banking-data-analytics/regulatory-data-submission-cycle/supervisory-query-response-assistant
intent: For each supervisory query from NBKR, NBK/ARDFM, or CBR, agent traverses lineage documentation, re-runs the relevant aggregation logic, and retrieves prior query responses on the same data point to produce a structured draft response pack for analyst review. The regulatory analyst reviews the draft, applies professional judgment, and signs off before transmission to the supervisor. Retrieval and drafting effort per query is compressed from days to hours.
Problem to solve: Supervisory queries require the data management team to retrieve lineage documentation, re-run aggregation logic for specific data points, and draft explanatory responses in the supervisor's preferred format. Where lineage documentation is incomplete or the aggregation logic has changed since the submission, query responses require additional investigation that delays the supervisory dialogue and consumes regulatory reporting team capacity during the next submission preparation window.
Solution: Agent reads the supervisory query text, identifies the CDE and submission data point referenced, and traverses the lineage record to reconstruct the source-to-submitted-value path. It re-runs the relevant aggregation logic for the data point in question and retrieves prior query-response records on the same topic from the query knowledge base. The draft response pack includes the lineage narrative, aggregation methodology summary, and any relevant prior explanation, structured in the supervisor's expected response format for analyst review and approval.
OKR objective: For each supervisory query from NBKR, NBK/ARDFM, or CBR, the regulatory analyst reviews an agent-assembled response pack — lineage narrative, aggregation methodology summary, and prior relevant explanations — and signs off before transmission to the supervisor.
OKR KR [Adoption]: Agent assembles the response pack for ≥ 90% of supervisory queries within 1 business day of query receipt for ≥ 12 months following go-live; lineage traversal, aggregation re-run, and prior query retrieval included in each pack.
OKR KR [Acceptance]: ≥ 85% of response packs accepted by analysts as a sufficient basis for sign-off without additional data retrieval; lineage narrative accuracy confirmed by data governance review in ≥ 90% of packs.
OKR KR [Cycle]: Per-query retrieval and drafting cycle reduced from days of manual investigation to ≤ 4 hours of analyst review and sign-off per query.

### CARD 18 [Insights|M] Regulatory Submission Quality Scorecard
urn: urn:financial-services:scenario:flow/banking-data-analytics/regulatory-data-submission-cycle/submission-quality-trend-scorecard
intent: Agent aggregates validation failure rates, exception volumes, post-submission reconciliation differences, and supervisory query frequencies across NBKR, NBK/ARDFM, and CBR submissions into a rolling quality scorecard for the CDO. The scorecard tracks BCBS 239 compliance trajectory by supervisor and submission form type. The CDO uses the scorecard as the primary evidence base for data governance council reporting and for directing data quality investment toward submission-critical CDEs.
Problem to solve: Submission performance across NBKR, NBK/ARDFM, and CBR is tracked informally by the regulatory reporting team but not aggregated into a quality trend analysis across submissions and supervisors. The CDO cannot produce a BCBS 239 compliance scorecard without manual extraction from submission records, and the connection between submission exceptions and upstream data quality failures is not routinely surfaced.
Solution: Agent reads validation exception reports, post-submission reconciliation outputs, and supervisory query logs from each submission cycle across all three regulatory perimeters. It produces a monthly quality scorecard segmented by supervisor, submission form, and data domain, with trending metrics for exception volume, reconciliation difference materiality, and query frequency. The scorecard links each exception category to the upstream CDE quality dimension failure driving it, enabling the CDO to direct remediation investment at the source.
OKR objective: The CDO holds a rolling BCBS 239 compliance scorecard tracking validation failure rates, exception volumes, and supervisory query frequencies by supervisor and form type across NBKR, NBK/ARDFM, and CBR, linked to upstream CDE quality dimension failures.
OKR KR [Adoption]: Agent produces the monthly quality scorecard covering all three regulatory perimeters for ≥ 12 consecutive months; each scorecard includes exception-to-CDE linkage for ≥ 90% of exception categories.
OKR KR [Acceptance]: ≥ 85% of CDE-to-exception linkages confirmed as accurate by the data quality team; scorecard used as primary evidence base for data governance council reporting in ≥ 10 of 12 monthly cycles.
OKR KR [Cycle]: BCBS 239 compliance scorecard produced within 5 business days of each monthly cycle close, replacing manual aggregation exercises that previously required 2–3 weeks per cycle.

### CARD 19 [Optimize|M] Cross-Supervisor Exception Pattern Analysis
urn: urn:financial-services:scenario:flow/banking-data-analytics/regulatory-data-submission-cycle/cross-supervisor-exception-pattern
intent: Agent analyses validation exception logs across NBKR, NBK/ARDFM, and CBR submission cycles to identify data quality failures that generate exceptions in multiple regulatory perimeters from the same source-system root cause. The analysis re-orders exception resolution effort from a per-supervisor queue to a cross-supervisor root-cause queue, enabling the data team to resolve a single source-system issue that clears exceptions across all three perimeters simultaneously. The CDO uses the output to direct pre-submission remediation effort.
Problem to solve: Validation exception resolution is performed sequentially against each supervisor's deadline. Cross-supervisor pattern analysis — identifying data quality issues that consistently generate exceptions across multiple supervisors because they originate in the same source system — is not applied within the standard submission cycle. The same root cause is investigated and corrected separately for each supervisor's form, multiplying remediation effort without improving underlying data quality.
Solution: Agent reads exception logs from the most recent submission cycles for each supervisor and clusters exceptions by the source-system CDE and data quality dimension they trace to. It identifies source-system root causes that generate exceptions across multiple regulatory perimeters and ranks them by aggregated exception volume across all three supervisors. The data quality team resolves the highest-ranked shared root causes before the next submission deadline, reducing total exception volume across all perimeters from a single remediation action.
OKR objective: The data team resolves regulatory submission exceptions from a cross-supervisor root-cause queue, directing remediation effort toward source-system issues that clear exceptions across NBKR, NBK/ARDFM, and CBR simultaneously.
OKR KR [Adoption]: Agent produces cross-supervisor exception pattern analysis before ≥ 90% of submission deadlines across all three regulatory perimeters; coverage extends to 100% of exception categories in each cycle.
OKR KR [Acceptance]: ≥ 80% of identified shared root causes confirmed as accurate by the data quality team; at least one cross-perimeter root cause resolved per cycle in ≥ 75% of submission periods.
OKR KR [Cycle]: Total cross-supervisor exception volume reduced by ≥ 20% year-on-year as shared root causes are systematically resolved; pattern analysis delivered ≥ 5 business days before each submission deadline.

### CARD 20 [New opps|M] Supervisory Query Knowledge Base
urn: urn:financial-services:scenario:flow/banking-data-analytics/regulatory-data-submission-cycle/supervisory-query-knowledge-base
intent: Agent consolidates supervisory query histories across NBKR, NBK/ARDFM, and CBR into a structured knowledge base, classifying each query by data point, challenge type, and resolution approach and surfacing recurrent patterns to the CDO and regulatory reporting team. The knowledge base is used to anticipate query categories in advance of submission, to accelerate response drafting by reference to prior accepted explanations, and to direct pre-submission data quality improvement at chronically challenged data points. The CDO uses the pattern analysis for BCBS 239 programme governance reporting.
Problem to solve: Supervisory query histories across the three regulatory perimeters accumulate in individual query files rather than a consolidated knowledge base. Each query cycle re-performs the investigation and drafting effort that prior cycle responses could have informed. Recurrent challenges on the same data points — indicative of a systematic data quality or methodology issue — are not identified as a pattern because query records are not aggregated and classified.
Solution: Agent reads all historical supervisory query and response records across NBKR, NBK/ARDFM, and CBR, classifies each query by CDE, data quality dimension, submission form, and resolution type, and builds a structured knowledge base accessible to the regulatory reporting team. The knowledge base surfaces recurrent query patterns ranked by frequency and identifies data points that have been challenged by multiple supervisors. Pre-submission briefings for the regulatory reporting team include the top recurring challenge categories for each upcoming submission deadline.
OKR objective: The regulatory reporting team applies a consolidated supervisory query knowledge base — classifying queries by CDE, challenge type, and resolution approach across NBKR, NBK/ARDFM, and CBR — to anticipate recurrent query categories and accelerate response drafting.
OKR KR [Adoption]: Agent ingests and classifies ≥ 95% of historical supervisory query records across all three perimeters by end of month 3; knowledge base refreshed for each new query cycle within 2 business days of response closure.
OKR KR [Acceptance]: ≥ 80% of recurrent query patterns confirmed as decision-relevant by the regulatory reporting team; pre-submission challenge category briefings used in ≥ 90% of upcoming submission preparation cycles within 12 months.
OKR KR [Cycle]: Per-query response drafting time reduced by ≥ 40% for recurrent challenge categories within 12 months, as prior accepted explanations are surfaced by the knowledge base before drafting begins.

[PAGE TEXT]
GenAI-enabled Banking and Financial Services Framework · v11i
×
