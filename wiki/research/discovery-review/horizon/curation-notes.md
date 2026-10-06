# Regulatory Horizon: curation notes

Curated on 6 October 2026 from `candidates.md`, the original card text (tag `discovery-fix-start`) and the current catalog. The result is `portal/sections/discovery/horizon.json`: 12 themes, 138 links, 136 distinct cards. A card was taken when the regime, or a rule of its type, is a reason the work exists, or when the card produces what such a rule asks of a bank (evidence, a register, a report, a control, a test). Where the catalog holds near-duplicate cards in different domains, one representative was taken. Two cards sit in two themes: Shadow Model Identification Scan (HZ-001, HZ-003) and Payment Data Completeness Monitoring (HZ-010, HZ-012). Every urn was checked against `html-alt/financial-services/en`.

## HZ-001 AI governance: 5

- Included Credit decision copilot for underwriters (the only listed candidate): it raises decision explainability and keeps the underwriter as the reviewer, which is the human-oversight duty such rules set for credit decisions.
- Added Credit Origination Analytics (not listed): its segment-level approval-rate comparisons were introduced in the original text to catch disparate impact, which is bias monitoring of a credit-scoring system.
- Added KYC extraction quality analytics (weak in model risk): it tracks accuracy of an extraction model by document type and customer segment, which matches post-deployment accuracy monitoring.
- Added Transaction monitoring alert disposition feedback loop (not listed): it recalibrates an alert-scoring model from outcomes and leaves a calibration record for model governance.
- Shared Shadow Model Identification Scan with HZ-003: an inventory of AI systems in use is the first thing such rules ask for, and this scan finds unregistered models.
- Excluded Adverse Action Notification Drafting from this theme and placed it in HZ-011; the driver is consumer-credit notice rules, not AI rules.
- The theme stays thin; the scenarios being drafted for it should fill the gap.

## HZ-002 Operational and cyber resilience: 16

- Excluded ATM Fraud Pattern Detection and ATM Skimming Regulatory Incident Reporter (both strong): the original text cites domestic anti-fraud incident rules, not ICT resilience regimes; the incident is card fraud, not an ICT disruption.
- Excluded ATM Incident Response Automation and ATM Cash Load Optimization (weak): outage reporting under network availability standards is a passing driver.
- Included Cyber Incident Post-Mortem Pack (weak): post-incident review with lessons learned is a standing requirement of such regimes.
- Added Post-Incident Review & BCP Update, RTO/RPO Test Results Analysis and BCP Annual Refresh Support (not listed): they produce the continuity plans, recovery tests and post-incident reviews these regimes require; BCP Annual Refresh Support is the most generic of the three.
- Added ICT Vendor Performance Monitoring (not listed): ongoing monitoring of critical ICT providers.
- Added Vendor Contract Regulatory Adequacy Review (weak in HZ-005; original text cited EBA outsourcing guidelines), Vendor Onboarding Regulatory Notification Timeline Planning and Sourcing Concentration Risk Analysis at Renewal (not listed): contract clauses, prior notice to the supervisor and concentration risk are core third-party asks.
- Included TPRM Exit Plan Currency Check (weak): its original text was written around the DORA exit-plan requirement.
- Excluded Regulatory & Industry Horizon Scanning and Crisis Scenario Narrative Framework (weak): passing mentions only.

## HZ-003 Model risk management: 16

- Excluded Loan Classification Consistency Check and Macro Indicator Consistency Check (strong): both serve expected-loss and capital inputs; the first went to HZ-008, the second was left out.
- Included IRB Model Performance Signal Watch and Model Performance Monthly Dashboard (weak): the original texts tie them to the documented performance monitoring that the guidance requires.
- Included Model Risk Appetite Metric Watch (weak): borderline; it watches the appetite metrics the guidance expects a board to set.
- Added Model recalibration brief drafting (weak in HZ-006): it documents recalibration for model risk committee approval, which is a model-governance step rather than a capital one.
- Excluded Model Validation Finding Synthesis (weak): it overlaps Validation Findings Thematic Synthesis, which was kept.
- Excluded P&L Attribution Pattern Analysis, Write-off cohort recovery retrospective and Credit Origination Analytics (weak): the first is trading-book model testing, the second a recovery calibration, the third went to HZ-001.
- Excluded KYC extraction quality analytics (weak) from this theme; placed in HZ-001.

## HZ-004 Open banking and partner APIs: 9

- Included Partner SLA Breach Alert Automation: the original text ties availability failures affecting third-party access to reporting timelines.
- Included API Third-Party Integration Performance Brief (listed under HZ-005): interface performance and consent-transaction metrics are open-banking asks; placed here only.
- Included Partner Ecosystem Quality Monitoring Brief (weak in HZ-005): borderline; it monitors provider consent handling, for which the platform operator is accountable.
- Included Regulatory Compliance Review Automation (strong in HZ-004 and HZ-005): it checks partnership arrangements against open-banking, personal-data and AML duties; placed here only.
- Excluded API Catalog Expansion Opportunities (strong): the work is product monetization; the regulatory feasibility check is secondary.
- Excluded Partner Network Portfolio Intelligence, Partnership landscape and fit brief, Ecosystem Landscape Brief and Partnership Term Sheet Drafting (strong): commercial or market intelligence with a passing reference to open-banking rules.
- Excluded ESG Score Trend Monitoring (strong): its text has no open-banking content.
- Excluded API Integration Portfolio Prioritization Brief (weak): borderline; it ranks integrations by commercial return with obligations only flagged.
- Excluded Platform Role Options Stress Test Brief, Platform Role Peer Positioning Brief, Partnership Exclusivity & Scope Risk Brief, Partnership Ongoing Compliance Monitoring Brief, Partner Contract Renewal Automation, Partner Network Expansion Intelligence and Innovation regulatory horizon scan (weak): strategy or generic regulatory tracking.

## HZ-005 Personal data and consent: 7

- Excluded Low-Adoption Customer Outreach Automation, Digital Engagement Personalization and Personalization Effectiveness Intelligence (strong): consent scope is a constraint on commercial work, not its purpose; Consent Scope Enforcement Automation, which exists for that control, was kept.
- Left the three open-banking cards (API Governance Risk Intelligence, Open Banking API Compliance Monitoring, Third-Party Provider Onboarding Automation), API Third-Party Integration Performance Brief and Regulatory Compliance Review Automation in HZ-004 only, to keep one theme per card.
- Excluded Vendor Contract Regulatory Adequacy Review (weak): placed in HZ-002.

## HZ-006 Capital and liquidity reforms: 22 of 93 candidates

- Selection rule: one card for each artifact or control the reforms ask for (internal capital and liquidity assessments, capital ratios and instrument limits, risk-weighted assets, large exposures, trading-book boundary and backtesting, liquidity returns, liquidity coverage and stable funding ratios, high-quality liquid assets, behavioral assumptions, contingency funding, interest rate risk in the banking book, intraday liquidity).
- Took ICAAP/ILAAP Narrative Assembly as the one narrative card; excluded the near-duplicates ICAAP Narrative Drafting, ICAAP/ILAAP Narrative Section Drafting, ICAAP narrative drafting from stress outputs, ICAAP narrative drafting, Liquidity Stress Scenario Narrative and ICAAP capital adequacy insights pack.
- Took Daily LCR/NSFR Submission Exception Commentary and ALCO pack and regulatory liquidity return automation for liquidity returns; excluded the commentary near-duplicates LCR/NSFR Driver Commentary, Daily LCR / NSFR Monitoring & Commentary, LCR/NSFR Daily Ratio Narrative, LCR & NSFR Driver Trend Analysis, Liquidity Posture Narrative and Continuous Liquidity Position Monitoring.
- Took ILAAP Behavioral Assumption Continuous Backtesting; excluded ILAAP Behavioral Assumption Drift Monitor and Funding Runoff & Concentration Watch as overlapping.
- Took ALCO IRRBB Pack Narrative Drafting, BCBS 368 Behavioral Assumption Backtesting and IRRBB Supervisory Assessment Preparation; excluded IRRBB Limit Utilization Report (borderline, covered by the ALCO pack card), IRRBB Early Warning Signal and Intra-Month IRRBB Position Signal (internal early warning).
- Took Supervisory Dialogue Knowledge Base for the supervisory review; excluded Supervisory Communications Drafting and Supervisor information request response packs as overlapping.
- Included Tier 2 regulatory limit tracking, Trading Book Boundary Monitoring and Counterparty Exposure Breach Notification Pack (weak): each exists because of a specific Basel limit or boundary rule; excluded Tier 2 instrument adequacy monitor and Tier 2 refinancing scenario pack as overlapping or decision support.
- Included VaR Model Backtesting Pack; excluded Backtesting Exception Documentation Pack as overlapping.
- Added Intraday Peak Usage Trend Analysis (not listed; current text still names BCBS 248): it produces the intraday liquidity report that standard asks for.
- Excluded optimization and steering cards where the ratio is a constraint rather than the driver: LCR Buffer Optimization Signal, HQLA Portfolio Yield & Duration Dashboard, HQLA Reinvestment Decision Support, Funding Strategy Scenario Analysis, Funding mix scenario optimization, Regulatory Capital Efficiency Signal Detection, RAROC hurdle breach alert, Profitability pack assembly automation, Dividend Policy Scenario Modeling and Rating agency and counterparty posture brief.
- Excluded the climate stress cards (Physical Risk Collateral Heat Map, Physical Risk Stress Scenario Narrative, Transition Risk Sector Stress Analysis) from this theme; Physical Risk Portfolio Assessment and Transition Risk & Carbon Exposure Analysis went to HZ-009.
- Excluded Valuation Scenario Sandbox, Competitive Position Benchmark, Finance Production Calendar Sequencing, ALCO Pre-Meeting Briefing Pack and Cross-Domain Limit Utilization Dashboard (strong): the reform is mentioned as context.
- Excluded the remaining weak candidates (submission calendars, stress summaries, risk appetite tools, scorecard and override analytics, horizon scans): passing mentions.

## HZ-007 Risk data and supervisory reporting: 15

- Excluded IFRS 9 Macro Input Version Control (strong): placed in HZ-008, its primary driver.
- Excluded Supervisory Template Movement Commentary (strong): borderline; templated regimes do not require commentary, and the validation and readiness cards carry the theme.
- Excluded the near-duplicates Catalog Lineage Completeness Check, Change-Triggered Lineage Update Prioritization, CDE Quality Trajectory Monitor and Attestation Findings Pattern Synthesis (strong): the kept lineage, profiling and attestation cards cover the same asks.
- Included BCBS 239 Data Lineage Documentation Maintenance alongside BCBS 239 Lineage Mapping: borderline overlap; the first maintains lineage per reported cell in the reporting cycle, the second builds the lineage map.
- Included Regulatory Validation Exception Triage and Cross-Domain Risk Coherence Check: borderline; the first handles taxonomy changes in templated reporting, the second applies the accuracy and consistency principles to risk reports.
- Excluded DQ Remediation Plan Drafting, Deduplication Candidate Impact Prioritization and Master Data Estate Health Monitor (strong): data operations that support, rather than evidence, the principles.
- Excluded Supervisory Submission Portfolio Health, Finance Production Calendar Sequencing and Valuation Scenario Sandbox (strong): passing mentions.
- Excluded all weak candidates; Supervisory Submission Quality Gate overlaps Regulatory Submission Pre-Dispatch Quality Gate.

## HZ-008 Expected credit loss: 12

- Took one card per artifact; excluded near-duplicates ECL Provision Narrative (banking-data-analytics copy), IFRS 9 ECL Provision Commentary Drafting, Stage Migration Analysis Drafting and Macro Overlay Sensitivity Brief.
- Included Loan Classification Consistency Check (listed for HZ-003 and HZ-008): it reconciles risk classification with the expected-loss stage.
- Included Vintage Cohort Default Tracking: borderline; it signals when the provisioning model needs recalibration.
- Excluded PD/LGD/EAD Output Quality Gate (strong): borderline; it is a general parameter check that also serves capital.
- Excluded Collateral Registry Completeness Check, Loan Book Data Quality Scan, Macro Data Publication Tracker and Macro Indicator Consistency Check (strong): data operations with expected loss as one consumer.
- Excluded Write-off timing scenario analysis and Portfolio sale bid analysis (strong): collections decisions that cite impairment evidence in passing.
- Excluded Lending Portfolio Performance Attribution and IFRS 9 provision intelligence and planning integration (strong): performance and planning uses of provision data.
- Excluded all weak candidates.

## HZ-009 Climate and sustainability disclosure: 12

- Took TCFD & ISSB Disclosure Draft as the disclosure drafting card; excluded TCFD Report Drafting as a near-duplicate.
- Took Financed Emissions Calculation; excluded Financed Emissions Attribution as overlapping and Scope 3 Counterparty Data Collection Brief as data operations.
- Included TCFD Prior Commitment Tracking: borderline; disclosure standards ask for progress against stated targets.
- Included Green Finance Pipeline Screening: borderline; taxonomy screening feeds taxonomy-alignment reporting.
- Added Physical Risk Portfolio Assessment and Transition Plan Portfolio Pathway Brief (not listed for this theme): physical-risk exposure and transition-plan progress are disclosure metrics.
- Excluded Regulatory ESG Filing Calendar Brief (strong): overlaps Regulatory ESG disclosure standard monitoring.
- Excluded TCFD Peer Disclosure Benchmarking Brief and ESG Priority Progress Report (strong): benchmarking and management reporting.
- Excluded Parallel Stress Scenario Set Expansion (strong): a stress-testing card with a passing climate variant.
- Excluded Transition Risk Sector Stress Analysis: supervisory climate stress testing, covered by Transition Risk & Carbon Exposure Analysis.
- Excluded the remaining weak candidates.

## HZ-010 AML/CFT standards: 10

- Added Payment Data Completeness Monitoring (not listed; shared with HZ-012): it checks originator and beneficiary fields, which is what the travel rule asks.
- Added Correspondent Banking Due Diligence Data Package (not listed): correspondent due diligence is a specific FATF requirement.
- Included CDD classification consistency analytics and AML alert disposition quality analytics (weak): the original texts tie them to the risk-based approach and to documentation of the basis for decisions.
- Took AML Typology Library Update as the typology card; excluded Financial crime typology enrichment copilot and AML typology update enrichment (strong) as overlapping.
- Excluded Connected-Party Group Mapping (strong): beneficial-ownership data used for credit large-exposure grouping, not AML.
- Excluded KYC Refresh Candidate Pack (weak): borderline; ongoing due diligence is already covered by KYC Risk Reclassification Trigger.
- Excluded Sanctions false-positive triage and Transaction monitoring alert pre-investigation pack (weak): efficiency tools that cite the review obligation in passing.
- Excluded Entity Hierarchy Validation (weak): a master-data control driven by large-exposure rules.

## HZ-011 Consumer protection and conduct: 9

- Took Complaint response letter drafting; excluded Complaint Response Drafting (strong) as a near-duplicate in the contact-center domain.
- Included Adverse Action Notification Drafting: decline notices with reasons and appeal rights are a consumer-credit conduct requirement.
- Added Client Suitability Documentation (not listed): it produces the suitability record that investor-protection rules require, alongside the listed suitability enablement card.
- Included QA Script & Disclosure Gap Detection (weak): it targets disclosures customers miss, which is the consumer-understanding outcome.
- Excluded Contact Center QA Intelligence and Complaint Escalation Pattern Monitor (weak): borderline; overlap with the kept disclosure and early-warning cards.
- Excluded Portfolio drift advisory signal, Suitability refresh trigger monitoring and Suitability assessment gap analytics: borderline; suitability is represented by two cards.
- Excluded IVR Script Update Automation and Market Entry Regulatory Constraint Mapping (strong): passing mentions.
- Excluded Support ticket cluster root-cause synthesis (weak): borderline; overlaps Complaint root-cause attribution brief.
- Excluded the remaining weak candidates (ATM alerts, knowledge assist, documentation, forecasting, scheduling, frontline copilot, remediation tracking, regulatory change tracker): passing mentions.

## HZ-012 Payments modernization: 5

- Included both listed weak candidates, Intraday Liquidity Position Watch and Settlement Counterparty Behavior Monitor: round-the-clock and instant settlement turns intraday liquidity into a continuous task.
- Added Intraday Liquidity Monitor and Intraday liquidity position copilot (not listed): real-time liquidity views built from payment system feeds.
- Shared Payment Data Completeness Monitoring with HZ-010: structured party data is the core of the ISO 20022 migration.
- Excluded FX correspondent routing table optimization, Straight-through processing gap signal and Payment failure root-cause attribution: they touch format rejections and network rule changes, but no card names a payments-modernization rule; the scenarios being drafted for this theme should fill the gap.
- Excluded Intraday Peak Usage Trend Analysis from this theme: placed in HZ-006 under the intraday liquidity standard.
