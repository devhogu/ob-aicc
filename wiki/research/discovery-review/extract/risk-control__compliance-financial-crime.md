# 

source: html-alt/financial-services/en/risk-control/compliance-financial-crime/index.html


[PAGE TEXT]
AML transaction monitoring
Transaction monitoring is the automated surveillance of customer transactions against rule-based and behavioural typologies to detect money laundering and terrorist financing activity. Under FATF Recommendation 10 and NBKR/CBR AML implementing regulations, banks must implement risk-based transaction monitoring covering all transaction types. Monitoring systems generate alert queues that AML investigators must disposition within defined SLA windows; alert volumes peak in periods of high transaction activity. The ratio of true positives to total alerts — the alert precision rate — determines the analyst hours required per confirmed suspicious activity.
Lens
Scenario
Intent
Complexity

### CARD 1 [Insights|S] AML Alert Volume & Trend Analysis
urn: urn:financial-services:scenario:risk-control/compliance-financial-crime/aml-transaction-monitoring/aml-alert-volume-trend-analysis
intent: Agent tracks alert volume, disposition rates, and true-positive ratios by rule and customer segment on a weekly basis, surfacing rule performance trends for the AML programme manager.
Problem to solve: AML monitoring programme performance — alert volumes, true-positive rates, and analyst SLA adherence — is reviewed in periodic programme reviews rather than on a rolling basis. A rule generating increasing false-positive volume over four weeks is identified in the monthly review rather than as the signal develops.
Solution: Agent reads alert management system data, computes weekly volume and disposition metrics by rule and customer segment, and tracks trend in true-positive ratio and SLA adherence over a rolling eight-week window. The AML programme manager receives a weekly performance digest, enabling responsive rule tuning before the next formal programme review.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 2 [Automation|M] AML Investigation Pack & False-Positive Analytics
urn: urn:financial-services:scenario:risk-control/compliance-financial-crime/aml-transaction-monitoring/aml-investigation-pack-fp-analytics
intent: Agent auto-assembles the investigation pack when an AML alert is opened, and produces a periodic false-positive root-cause analysis to enable systematic rule tuning.
Problem to solve: Each AML alert requiring escalation needs a full investigation pack — KYC records, transaction detail, related-account links, prior alerts, sanctions results, and adverse media — before a supervisor can review. Alert false-positive rates of 90–98% consume analyst capacity, but rule tuning is constrained by the absence of systematic FP pattern analysis across the alert population.
Solution: Agent auto-assembles the investigation pack at alert-open time from all connected systems, so the supervisor receives a complete dossier at the point of review. On a monthly cadence, agent clusters 12 months of closed alerts by transaction context, customer profile, and rule parameter to identify the specific combinations driving disproportionate false-positive volume. The AML and model risk teams use the clustering output to calibrate rule parameters.
OKR objective: AML supervisors receive a complete investigation dossier at alert-open time, and the compliance team applies a systematic monthly false-positive root-cause analysis to calibrate rule parameters and reduce unnecessary analyst burden.
OKR KR [Adoption]: Agent used to auto-assemble investigation packs for ≥95% of AML alerts requiring supervisor review within 12 months of go-live; monthly FP clustering analysis run for ≥10 consecutive months in year 1.
OKR KR [Acceptance]: ≥80% of auto-assembled investigation packs accepted by supervisors as complete without manual supplementation; ≥70% of monthly FP clustering outputs actioned by the AML and model risk teams for rule recalibration.
OKR KR [Cycle]: Per-alert investigation pack assembly time reduced from manual assembly (≥30 minutes) to ≤2 minutes at alert open; monthly FP analysis cycle completed within 5 business days of month-end close.

### CARD 3 [Insights|M] AML Typology Library Update
urn: urn:financial-services:scenario:risk-control/compliance-financial-crime/aml-transaction-monitoring/aml-typology-library-update
intent: Agent reads FinCEN advisories, FATF typology reports, and sector-specific AML guidance, extracts new transaction patterns and red flags, and delivers a structured typology update to the AML model risk and financial crime teams for rule review.
Problem to solve: AML transaction monitoring rules are calibrated against a typology library that reflects money laundering techniques at the time of rule implementation. New typologies published by FATF, FinCEN, Rosfinmonitoring, and KFM are reviewed by the financial crime team when capacity permits; rule updates lag the publication of new patterns.
Solution: Agent monitors FATF typology reports, FinCEN advisories, Rosfinmonitoring guidance, and FS-ISAC financial crime publications. It extracts new transaction pattern descriptions and risk indicators, maps each to the existing rule library, and flags rules that do not cover the pattern. The AML model risk team receives a quarterly typology update report with a coverage gap analysis.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
Regulatory licensing & filings
Regulatory licensing and filing obligations span money transmitter licenses, banking licenses, product filings, and periodic regulatory submissions — each with jurisdiction-specific deadlines, capital and bond requirements, and form requirements. For US-based fintechs, 45-50 state money transmitter licenses each carry their own filing cadence, capital minimum, surety bond requirement, and examination schedule. CBR and NBKR filing obligations cover capital adequacy submissions, liquidity reports, AML statistical filings, and consumer protection disclosures — each on defined monthly, quarterly, or annual cycles.
Lens
Scenario
Intent
Complexity

### CARD 4 [Automation|S] Regulatory Filing Calendar & Tracker
urn: urn:financial-services:scenario:risk-control/compliance-financial-crime/regulatory-licensing-filings/regulatory-filing-calendar-tracker
intent: Agent maintains the consolidated regulatory filing calendar across all jurisdictions, tracks submission status against each deadline, and delivers a weekly completion status report to the CCO.
Problem to solve: Regulatory filing obligations span NBKR, CBR, and multiple state money transmitter licensing jurisdictions, each with distinct monthly, quarterly, and annual deadlines. The compliance team tracks filing completion in a manually updated spreadsheet; a missed deadline is identified only when the calendar is reviewed rather than when the risk of missing it first emerges.
Solution: Agent reads the regulatory filing calendar, monitors submission confirmation receipts against each deadline, flags filings at risk of missing the deadline three weeks in advance, and delivers a weekly status report to the CCO covering all open, at-risk, and completed filings.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 5 [Automation|M] License Renewal Pack Assembly
urn: urn:financial-services:scenario:risk-control/compliance-financial-crime/regulatory-licensing-filings/license-renewal-pack-assembly
intent: Agent assembles the license renewal submission pack from current financial statements, capital and surety bond certificates, and officer certification templates, reducing the per-jurisdiction preparation time for state money transmitter renewals.
Problem to solve: State money transmitter license renewals require assembling current financial statements, surety bond and capital documentation, officer certifications, and jurisdiction-specific form completions. For a bank with 40-50 active state licenses, the preparation cycle consumes weeks of compliance team effort each renewal season.
Solution: Agent reads the renewal requirements schedule, current financial statements, surety bond registry, and officer certification database. It pre-populates renewal forms with current data, assembles the supporting documentation pack per jurisdiction, and flags items requiring manual certification or notarisation. The compliance officer reviews each pack and files.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 6 [Insights|M] Regulatory Filing Gap & Obligation Analysis
urn: urn:financial-services:scenario:risk-control/compliance-financial-crime/regulatory-licensing-filings/regulatory-filing-gap-analysis
intent: Agent reads new regulatory guidance and jurisdiction updates, identifies filing obligations not yet captured in the compliance calendar, and delivers a gap analysis to the CCO for calendar update.
Problem to solve: Regulatory filing obligations evolve with new supervisory guidance, product approvals, and jurisdictional law changes. New obligations are identified through manual monitoring of regulatory publications; there is no systematic process to cross-reference new regulatory output against the existing filing calendar to detect gaps.
Solution: Agent monitors regulatory publication feeds from NBKR, CBR, and US state money transmitter regulators, extracts new filing obligations, cross-references each against the current compliance calendar, and identifies obligations not yet tracked. The CCO receives a quarterly gap analysis with each new obligation flagged and a draft calendar entry for review.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
SAR & case management
A Suspicious Activity Report (SAR) is the mandatory filing with the financial intelligence unit — FinCEN in the US, Rosfinmonitoring in Russia, KFM in Kazakhstan — when an AML investigation produces evidence of suspicious activity. Under FATF and domestic implementing regulations, SARs must be filed within 30 days of detecting suspicious activity; late or deficient filings carry supervisory penalties. SAR narrative quality — precision of the who/what/when/where/why/how framework — directly influences the financial intelligence unit's ability to act on the report and the bank's supervisory standing.
Lens
Scenario
Intent
Complexity

### CARD 7 [Automation|S] SAR Drafting Support
urn: urn:financial-services:scenario:risk-control/compliance-financial-crime/sar-case-management/sar-drafting-support
intent: Agent generates the SAR narrative from investigation notes in regulatory format, with cross-investigation links and prior-SAR cross-reference, for BSA officer review and filing.
Problem to solve: SAR drafting is a material per-case overhead for the drafter and BSA reviewer, executed under hard regulatory deadlines. Narrative quality varies by drafter; prior-SAR cross-reference and cross-investigation linking are performed inconsistently across the team.
Solution: Agent reads investigation notes and produces the SAR narrative in the prescribed regulatory format — covering the who, what, when, where, and how of the suspicious activity — with cross-SAR consistency, prior-SAR cross-reference, and compliance flags populated. The BSA officer reviews and files.
OKR objective: The BSA officer reviews and files a SAR narrative — in prescribed regulatory format with cross-investigation links and prior-SAR cross-reference — drafted by the agent from investigation notes under hard filing deadlines.
OKR KR [Adoption]: Agent used to generate SAR narrative drafts for ≥90% of SAR-eligible investigations within 12 months of go-live; cross-SAR consistency checks and prior-SAR cross-reference applied in every draft from go-live.
OKR KR [Acceptance]: ≥80% of agent-drafted SAR narratives accepted by BSA officers with only minor amendment before filing; regulatory filing completeness (who/what/when/where/how all populated) confirmed at ≥98% on quality audit.
OKR KR [Cycle]: SAR narrative draft delivered within 4 hours of investigation note submission, compressing the drafting phase and expanding BSA officer review time within the regulatory filing window.

### CARD 8 [Automation|S] SAR Filing Deadline Tracker
urn: urn:financial-services:scenario:risk-control/compliance-financial-crime/sar-case-management/sar-filing-deadline-tracker
intent: Agent tracks all open SAR investigations against the 30-day regulatory filing deadline, escalates cases approaching the deadline without a completed narrative, and generates the BSA officer's daily case queue with deadline proximity ranking.
Problem to solve: SAR investigations in progress across multiple analysts are tracked in the case management system but the BSA officer has no automated escalation when a case is approaching the 30-day regulatory deadline without a completed filing. Late filings are identified in the post-filing quality review rather than prevented.
Solution: Agent reads the open case register, computes days-remaining for each case against the investigation-open date, escalates cases where fewer than five days remain without a filed narrative, and generates the BSA officer's daily queue ranked by deadline proximity. The BSA officer uses the queue to direct analyst capacity to time-critical cases.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 9 [Insights|M] SAR Quality & Narrative Pattern Analysis
urn: urn:financial-services:scenario:risk-control/compliance-financial-crime/sar-case-management/sar-quality-and-pattern-analysis
intent: Agent reviews filed SAR narratives for completeness against the who/what/when/where/how framework, identifies recurring quality gaps by analyst and activity type, and delivers a quarterly quality analysis to the BSA officer.
Problem to solve: SAR narrative quality is assessed in individual BSA officer reviews before filing. Recurring quality gaps — incomplete activity descriptions, missing subject identification, inconsistent red flag articulation — are visible across the filing population but not tracked systematically, so coaching is reactive to individual filings rather than pattern-based.
Solution: Agent reads the rolling 90-day filed SAR population, applies the who/what/when/where/how completeness schema, computes quality scores by narrative section, and identifies recurring deficiency patterns by analyst and activity type. The BSA officer receives a quarterly quality analysis for use in targeted training and quality-programme calibration.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
Conduct & complaints
Conduct risk is the risk that the bank's actions or product design produce unfair customer outcomes — generating regulatory intervention under consumer protection frameworks (NBKR consumer protection rules, CBR Ordinance No. 3241-U, FCA PRIN principles, CFPB regulations). Customer complaint data is the primary signal for conduct risk; complaint theme analysis identifies systematic product or process failures before they reach regulatory attention. Complaint root-cause analytics drive product remediation, staff retraining, and disclosure improvement. Under CRD IV and FCA SYSC, conduct risk governance is a board-level responsibility with documented escalation paths.
Lens
Scenario
Intent
Complexity

### CARD 10 [Automation|S] Complaint Regulatory Escalation Tracker
urn: urn:financial-services:scenario:risk-control/compliance-financial-crime/conduct-complaints/complaint-regulatory-escalation-tracker
intent: Agent tracks complaints that meet regulatory escalation thresholds — FCA/CFPB reportable complaints, NBKR complaint registry submissions — and generates the escalation record and regulator submission pack for the compliance officer.
Problem to solve: Complaints meeting regulatory escalation criteria must be identified from the complaint queue and submitted to the regulator within defined timeframes. The threshold identification and submission preparation is performed manually per complaint; during high-volume periods the risk of a missed escalation deadline increases.
Solution: Agent reads the daily complaint queue, applies the jurisdiction-specific escalation criteria, flags complaints meeting the threshold, and generates the submission pack in the required format. The compliance officer reviews and files within the regulatory window.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 11 [Insights|M] Complaint Theme & Root-Cause Analytics
urn: urn:financial-services:scenario:risk-control/compliance-financial-crime/conduct-complaints/complaint-theme-root-cause-analytics
intent: Agent classifies complaints into granular themes, clusters by root cause, and tags conduct-risk signals for the Head of Compliance.
Problem to solve: Complaint teams categorize incoming complaints into broad buckets and handle each individually. Recurring themes, shared root causes across complaint types, and conduct-risk signals are visible only in periodic reviews rather than as they develop.
Solution: Agent processes complaints through thematic classification, clusters by root cause across category boundaries, and tags each cluster for conduct-risk signal strength. The Head of Compliance receives a monthly theme and root-cause pack with signals ranked by severity.
OKR objective: The Head of Compliance receives a monthly thematic classification of complaints with root-cause clusters and conduct-risk signal rankings, on a continuous basis rather than in periodic manual reviews.
OKR KR [Adoption]: Agent complaint classification and root-cause clustering running on 100% of incoming complaints within 6 months of go-live; monthly pack delivered to Head of Compliance for ≥10 consecutive months in year 1.
OKR KR [Acceptance]: ≥75% of agent-identified conduct-risk signal clusters rated as material by the Head of Compliance; ≤5% misclassification rate on thematic taxonomy validated by quarterly compliance team review.
OKR KR [Cycle]: Monthly thematic pack produced within 3 business days of month-end, versus ≥2 weeks of manual complaint review under the prior approach.

### CARD 12 [Insights|M] Conduct Risk Product Review Signal
urn: urn:financial-services:scenario:risk-control/compliance-financial-crime/conduct-complaints/conduct-risk-product-review-signal
intent: Agent correlates complaint theme clusters with product-level data — fee structures, disclosure documentation, and sales channel performance — to identify the product or process root cause for the Head of Compliance's quarterly conduct risk review.
Problem to solve: Complaint theme analysis identifies the topic of complaints but not the product-level root cause. Connecting a complaint cluster to a specific disclosure inadequacy, fee calculation error, or sales channel practice requires additional data joins that are performed manually when a theme becomes large enough to warrant investigation.
Solution: Agent reads complaint theme clusters, cross-references each cluster with product fee structures, disclosure documentation versions, and sales channel performance data. It identifies the most probable product or process root cause per cluster and presents the correlation analysis to the Head of Compliance ahead of the quarterly conduct risk review.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
Sanctions & PEP screening
Sanctions screening matches customers, transactions, and counterparties against sanctions lists — OFAC SDN, UN Security Council lists, EU Consolidated List, and domestic NBKR and CBR lists — and politically exposed person (PEP) registers. Under FATF Recommendation 6 and domestic sanctions-compliance regulations, screening must cover onboarding, periodic review, and real-time transaction screening. Screening generates false positives from name-matching algorithms; each potential match requires investigation and disposition. Screening list updates — following regulatory additions — must be implemented within defined timeframes.
Lens
Scenario
Intent
Complexity

### CARD 13 [Automation|S] Sanctions Hit Investigation Pack
urn: urn:financial-services:scenario:risk-control/compliance-financial-crime/sanctions-pep-screening/sanctions-hit-investigation-pack
intent: Agent assembles the investigation package for each sanctions screening match — customer profile, transaction context, name-match analysis, and disposition rationale template — for the compliance officer to review.
Problem to solve: Each sanctions screening potential match requires the compliance officer to investigate the hit — reviewing customer profile, transaction context, and the specific match reason — before disposition as true or false positive. Investigation context assembly is a per-hit overhead that peaks during sanctions list updates when volume spikes.
Solution: Agent assembles the per-hit investigation package: customer KYC profile, recent transaction context, the specific match field and confidence score, prior disposition history for this customer, and a disposition rationale template. The compliance officer completes disposition with the full context available from the outset.
OKR objective: Compliance officers complete sanctions screening match disposition with the full investigation package — KYC profile, transaction context, match analysis, prior disposition history, and rationale template — assembled by the agent at the point of hit review.
OKR KR [Adoption]: Agent used to assemble investigation packages for ≥95% of sanctions screening potential matches within 6 months of go-live; all six investigation package components populated in every run from go-live.
OKR KR [Acceptance]: ≥85% of agent-assembled packages accepted by compliance officers as complete without requiring supplemental manual lookups; package completeness confirmed at ≥95% on quarterly quality audits.
OKR KR [Cycle]: Investigation package available to the compliance officer within 5 minutes of hit assignment, versus ≥20 minutes of manual assembly per hit under the prior approach.

### CARD 14 [Insights|S] Sanctions List Update Impact Assessment
urn: urn:financial-services:scenario:risk-control/compliance-financial-crime/sanctions-pep-screening/sanctions-list-update-impact-assessment
intent: Agent reads new sanctions list updates from OFAC, EU, UN, and domestic regulators, identifies newly added names against the active customer and counterparty book, and delivers an impact assessment to the sanctions compliance officer within the implementation window.
Problem to solve: Sanctions list updates must be reflected in screening systems within defined timeframes. The impact assessment — which active customers or counterparties match the new additions — is performed manually or relies on the screening system batch run, which may not execute until the following business day.
Solution: Agent reads the new sanctions list update, extracts added names and entities, and applies name-matching logic against the active customer and counterparty registers. It delivers a same-day impact assessment flagging potential matches for the sanctions compliance officer to investigate and action before the system batch run.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 15 [Automation|M] PEP Periodic Review Pack
urn: urn:financial-services:scenario:risk-control/compliance-financial-crime/sanctions-pep-screening/pep-periodic-review-pack
intent: Agent assembles the enhanced due diligence review pack for PEP customers on the periodic review schedule — current PEP registry status, transaction behaviour analysis, adverse media, and prior review findings — for the compliance officer.
Problem to solve: PEP customers require enhanced due diligence on a defined periodic review cycle. Assembling the review pack — current PEP registry status, transaction behaviour, adverse media, and prior review summary — for each customer ahead of the review date is a manual preparation task for the compliance analyst.
Solution: Agent reads the PEP periodic review schedule, retrieves each customer's current registry classification, 12-month transaction behaviour, adverse media results, and prior review documentation. It assembles the review pack for each customer due in the cycle and presents it to the compliance officer for the review assessment.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
Regulatory examination management
Regulatory examinations — conducted by NBKR, NBK/ARDFM, CBR, FCA, OCC, Fed, or FDIC depending on jurisdiction — follow defined cycles with document request lists, management presentations, and findings issuance. For a mid-size bank, an examination cycle consumes 80-150 CCO and General Counsel hours plus 200-400 hours across business lines. The quality of examination preparation — document request response speed, anticipated focus area coverage, prior-commitment tracking — directly influences examination outcomes and supervisory ratings. Under the CAMELS or equivalent supervisory framework, a management rating downgrade affects capital requirements and regulatory flexibility.
Lens
Scenario
Intent
Complexity

### CARD 16 [Enablement|M] Regulatory Examination Readiness
urn: urn:financial-services:scenario:risk-control/compliance-financial-crime/regulatory-examination-management/regulatory-examination-readiness
intent: Agent tracks examination document request status, pre-assembles responses from institutional records, surfaces anticipated examiner focus areas, and maintains an internal policy corpus for staff queries throughout the examination cycle.
Problem to solve: A 100–200 item examiner document request consumes significant CCO and cross-business hours over several weeks per examination cycle. Anticipated examiner focus areas are informed by institutional memory; prior-examination commitments are tracked manually; compliance staff spend material time per query on search-and-verify with accuracy varying by experience.
Solution: Agent tracks document request completion, cross-references institutional records against each request, anticipates examiner focus areas from prior examination findings and recent regulatory guidance, and drafts response templates. A RAG corpus of internal policies and key regulatory texts answers staff queries with cited sources; ambiguous cases defer to General Counsel. The CCO reviews weekly status and directs resources to gaps.
OKR objective: The CCO manages the examination cycle with agent-maintained document request tracking, pre-assembled institutional responses, and a RAG corpus of internal policies that resolves staff queries with cited sources throughout the examination window.
OKR KR [Adoption]: Agent examination readiness system in active use for ≥1 full NBKR/NBK/ARDFM examination cycle within 18 months of go-live; RAG corpus covering ≥90% of current internal policies and key regulatory texts from go-live.
OKR KR [Acceptance]: ≥75% of agent pre-assembled document responses accepted by the CCO as complete without major supplementation; staff query resolution accuracy confirmed at ≥85% on quality audit of cited responses.
OKR KR [Cycle]: Document request response preparation cycle reduced by ≥40% in total elapsed days versus the prior examination cycle, as measured by time from examiner request to CCO-approved response.

### CARD 17 [Automation|M] Examination Document Request Response Assembly
urn: urn:financial-services:scenario:risk-control/compliance-financial-crime/regulatory-examination-management/examination-document-request-response
intent: Agent reads each item on the examiner document request list, retrieves the matching document from the institutional records repository, and assembles the submission package for the CCO's review, reducing the per-item manual retrieval cycle.
Problem to solve: A regulatory examination document request typically contains 80-150 items spanning policies, procedures, transaction samples, committee minutes, and prior remediation evidence. The compliance team assigns each item to a business line owner, who locates and returns the document; the retrieval and assembly process can span three to four weeks and consumes significant cross-business capacity.
Solution: Agent reads the document request list, matches each item against the institutional document repository using semantic search, and retrieves the most current version. It assembles the submission package per request item with source citations, flags items where no matching document is found, and presents the assembled package to the CCO for review before transmission to the examiner.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 18 [Insights|M] Examination Findings Pattern Analysis
urn: urn:financial-services:scenario:risk-control/compliance-financial-crime/regulatory-examination-management/examination-findings-pattern-analysis
intent: Agent clusters examination findings across multiple examination cycles by root cause, business line, and regulatory framework, identifying systemic patterns that the CCO can address proactively before the next examination.
Problem to solve: Examination findings are documented per examination and responded to individually. Systemic patterns — the same root cause generating findings across three successive examinations, or findings concentrated in a specific business line under a particular regulatory framework — are visible only in a cross-examination analysis that is not routinely produced.
Solution: Agent reads the examination finding archive across the rolling five-year period, applies root-cause clustering across finding descriptions, maps each cluster to business line and regulatory framework, and identifies systemic patterns with repeat incidence. The CCO receives the analysis before each new examination cycle, enabling targeted pre-examination remediation of demonstrated systemic weaknesses.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
GenAI-enabled Banking and Financial Services Framework · v11i
