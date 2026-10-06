# 

source: html-alt/financial-services/en/risk-control/cyber-risk/index.html


[PAGE TEXT]
Threat intelligence & exposure
Threat intelligence is the structured collection and analysis of information about threat actors, attack techniques, and emerging vulnerabilities relevant to the bank's technology and product profile. FS-ISAC, SWIFT CSP, CERT-KZ, CERT-RU, and commercial threat intelligence feeds provide the raw signal; the CISO's team must filter, correlate with internal exposure, and act. Under DORA Article 13, banks must maintain threat intelligence capabilities proportionate to their ICT risk profile. Banking-sector-specific threat actors — state-sponsored groups targeting SWIFT connectivity, ransomware operators targeting core banking, credential-phishing campaigns targeting staff — require sector-specific intelligence sourcing and correlation.
Lens
Scenario
Intent
Complexity

### CARD 1 [Insights|M] Threat Intelligence Briefing
urn: urn:financial-services:scenario:risk-control/cyber-risk/threat-intelligence-exposure/threat-intelligence-briefing
intent: Agent aggregates external threat intelligence feeds, sector-specific advisories, and internal detection signals into a daily CISO briefing ranked by relevance to the bank's technology stack and product mix.
Problem to solve: The CISO and threat intelligence team receive hundreds of daily items from vendor feeds, CERT advisories, FS-ISAC, SWIFT CSP, and regulatory notifications. Relevance filtering and internal-exposure correlation are performed manually; material threats can remain in the queue for days before reaching the CISO's attention.
Solution: Agent ingests all threat intelligence sources, clusters threats by type, cross-references each cluster with the bank's technology stack and known vulnerabilities, ranks by relevance, and produces a daily prioritised briefing for the CISO. The team responds to prioritised signals rather than raw feed volume.
OKR objective: The CISO and threat intelligence team respond to a daily prioritised briefing — with threats ranked by relevance to the bank's technology stack and product mix — rather than manually filtering and correlating raw feed volume.
OKR KR [Adoption]: Agent threat intelligence aggregation and prioritisation covering all major feed sources (vendor feeds, CERT advisories, FS-ISAC, SWIFT CSP, regulatory notifications) within 6 months of go-live; daily prioritised briefing delivered to the CISO for ≥200 business days per year once live.
OKR KR [Acceptance]: ≥75% of top-ranked daily threats confirmed as material to the bank's environment by the threat intelligence team; critical threat-to-CISO attention latency reduced by ≥70% versus the prior manual filtering approach.
OKR KR [Cycle]: Daily prioritised briefing delivered before the start of business each morning, versus ≥2 days of latency from signal emergence to CISO attention under the prior manual queue approach.

### CARD 2 [Insights|M] Threat Actor Exposure Mapping
urn: urn:financial-services:scenario:risk-control/cyber-risk/threat-intelligence-exposure/threat-actor-exposure-mapping
intent: Agent maps active banking-sector threat actors to the bank's technology stack, identifying the specific systems and controls most relevant to each actor's known TTPs for the CISO's quarterly threat exposure review.
Problem to solve: Threat intelligence briefings describe threat actors and their techniques but do not map them to the bank's specific technology profile. The CISO and security architecture team perform this mapping manually for high-priority advisories; lower-priority actors and their relevance to specific systems are not systematically assessed.
Solution: Agent reads threat intelligence on active banking-sector actors, extracts their known TTPs using the MITRE ATT&CK framework, and maps each TTP to the bank's technology asset inventory. It identifies the systems most frequently targeted by each actor's techniques and delivers a quarterly threat-actor exposure map to the CISO.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 3 [Enablement|M] Threat Intelligence Control Gap Analysis
urn: urn:financial-services:scenario:risk-control/cyber-risk/threat-intelligence-exposure/threat-intel-control-gap-analysis
intent: Agent cross-references the bank's control framework against current threat actor TTPs, identifies controls that do not address observed attack techniques, and delivers a gap analysis to the CISO for security programme prioritisation.
Problem to solve: The bank's control framework is assessed in the annual risk and control self-assessment cycle. Emerging attack techniques that have appeared in threat intelligence since the last RCSA cycle may not be covered by current controls; the gap is not visible until the next scheduled assessment.
Solution: Agent reads current threat intelligence TTPs, maps each technique to the NIST CSF or CIS control framework, and cross-references against the bank's documented control inventory. It identifies TTP-to-control gaps and delivers the analysis to the CISO for prioritisation in the security programme roadmap.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
Incident detection & response
Cyber incident response is the structured process of detecting, containing, eradicating, and recovering from a security incident — governed by an Incident Response Plan (IRP) that defines roles, escalation paths, and regulatory notification obligations. Under DORA Article 19, major ICT incidents must be notified to the competent authority within 4 hours of classification, with a detailed incident report within 72 hours. Incident detection latency — the time between initial compromise and detection — is the primary driver of incident severity; mean time to detect (MTTD) and mean time to respond (MTTR) are the KPIs governing security operations effectiveness.
Lens
Scenario
Intent
Complexity

### CARD 4 [Automation|S] Cyber Incident Triage Pack
urn: urn:financial-services:scenario:risk-control/cyber-risk/incident-detection-response/cyber-incident-triage-pack
intent: Agent assembles the initial incident triage pack when a cyber alert is escalated — asset inventory context, historical alert pattern, DORA notification checklist, and stakeholder contact list — so the incident response team has an actionable dossier at the start of the response.
Problem to solve: When a cyber incident is escalated, the response team assembles asset context, prior alert history, DORA notification thresholds, and stakeholder contacts from multiple systems while simultaneously managing containment. The triage context assembly step delays initial response actions in a time-critical window.
Solution: Agent reads the alert from the SIEM, retrieves asset inventory context, surfaces the prior 90-day alert history for that asset, applies the DORA significance threshold check, and populates the incident triage template. The incident commander receives a pre-populated dossier and focuses on containment decisions from the first minute.
OKR objective: The incident commander begins containment decisions from the first minute with an agent-assembled triage dossier — covering asset context, alert history, DORA notification checklist, and stakeholder contacts — available at the point of escalation.
OKR KR [Adoption]: Agent triage pack assembled for ≥95% of escalated cyber incidents within 12 months of go-live; DORA significance threshold check applied automatically to every incident from go-live.
OKR KR [Acceptance]: ≥85% of agent-assembled triage packs rated as complete by incident commanders without requiring supplemental manual lookups during the initial response; DORA notification checklist accuracy validated at ≥95% in quarterly simulation exercises.
OKR KR [Cycle]: Triage pack delivered to the incident commander within 5 minutes of alert escalation, versus ≥30 minutes of manual assembly under the prior approach.

### CARD 5 [Automation|S] DORA Incident Notification Draft
urn: urn:financial-services:scenario:risk-control/cyber-risk/incident-detection-response/incident-dora-notification-draft
intent: Agent generates the DORA Article 19 initial notification draft — incident classification, affected systems, business impact estimate, and containment status — within the four-hour regulatory window from major ICT incident classification.
Problem to solve: DORA requires a major ICT incident notification to the competent authority within four hours of classification. Drafting the notification under time pressure, with incomplete information and simultaneous incident management activity, produces notifications that may omit required fields or misstate the incident classification.
Solution: Agent reads the incident triage record, applies the DORA major incident classification criteria, and generates the initial notification draft in the prescribed format — incident type, classification rationale, affected systems, estimated business impact, and containment actions taken. The incident commander reviews and submits within the four-hour window.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 6 [Insights|M] Cyber Incident Post-Mortem Pack
urn: urn:financial-services:scenario:risk-control/cyber-risk/incident-detection-response/incident-post-mortem-pack
intent: Agent assembles the post-incident review pack from the event timeline, containment and recovery logs, and communications records, and identifies control gaps and detection improvements for the CISO's lessons-learned review.
Problem to solve: Post-incident reviews are conducted after containment but the pack assembly — incident timeline reconstruction, control failure identification, detection gap analysis — consumes security team hours at a point when the team is managing residual remediation activity.
Solution: Agent reads SIEM event logs, containment action records, recovery timeline, and communications records. It reconstructs the incident timeline, identifies the initial access vector and detection point, maps the gap between compromise and detection, and flags control and detection improvements. The CISO reviews the pack and assigns remediation ownership in the lessons-learned session.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
Vulnerability & patch management
Vulnerability management is the programme of discovering, assessing, prioritizing, and remediating known security weaknesses in the bank's technology estate. Scanner tools generate thousands of findings per week; the CVSS scoring system provides a standardized severity measure. DORA Article 10 requires banks to maintain documented vulnerability management processes with defined remediation timeframes by severity. Banking regulators expect critical vulnerabilities on internet-facing systems to be remediated within 30 days; exploited vulnerabilities require emergency patching. Patch management coordinates the remediation workflow — testing compatibility, scheduling deployment, and tracking completion — across infrastructure, application, and endpoint layers.
Lens
Scenario
Intent
Complexity

### CARD 7 [Automation|S] Patch Compliance Status Report
urn: urn:financial-services:scenario:risk-control/cyber-risk/vulnerability-patch-management/patch-compliance-status-report
intent: Agent reads patch deployment status across all asset tiers, computes compliance rates against the DORA-required remediation timeframes by severity, and delivers a weekly patch compliance report to the CISO.
Problem to solve: DORA and CBR requirements set remediation timeframes for critical and high-severity vulnerabilities. Patch compliance status is tracked across infrastructure, application, and endpoint tiers in separate tools; producing a consolidated compliance view for the CISO requires manual aggregation from multiple sources.
Solution: Agent reads patch deployment status from infrastructure, application, and endpoint management tools, applies the severity-tiered remediation timeframe schedule, computes compliance rates by asset tier and severity level, and produces the weekly compliance report flagging assets overdue by tier. The CISO uses the report to direct remediation focus.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 8 [Automation|S] Vulnerability Exception Management Tracker
urn: urn:financial-services:scenario:risk-control/cyber-risk/vulnerability-patch-management/vulnerability-exception-management
intent: Agent tracks active vulnerability exceptions — cases where patching is deferred with documented business justification — monitors expiry dates, and generates the exception renewal or escalation queue for the CISO's review.
Problem to solve: Vulnerabilities that cannot be immediately patched require a documented exception with a compensating control and expiry date. With dozens of active exceptions across the estate, monitoring expiry dates and ensuring renewals are approved before exceptions lapse is a manual tracking task that creates the risk of unmanaged expired exceptions.
Solution: Agent reads the active exception register, monitors expiry dates, flags exceptions approaching expiry without a renewal submission, and generates the CISO's weekly exception review queue. Lapsed exceptions are escalated automatically to the vulnerability management lead.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 9 [Insights|M] Vulnerability Risk-Adjusted Prioritization
urn: urn:financial-services:scenario:risk-control/cyber-risk/vulnerability-patch-management/vulnerability-prioritization-narrative
intent: Agent cross-references scanner output with asset criticality and threat intelligence to produce a risk-adjusted remediation queue for the security operations team.
Problem to solve: Vulnerability scanners generate thousands of weekly findings. CVSS-based prioritization without asset criticality or current exploitation activity places high-CVSS findings on low-criticality assets ahead of lower-CVSS findings on core banking infrastructure where exploitation carries materially higher impact.
Solution: Agent reads scanner output, cross-references each finding with the asset criticality register and current threat intelligence on active exploitation, and produces a risk-adjusted prioritization ranking by critical-asset score, exploitability, and current threat actor relevance. The security operations team works the ranked queue.
OKR objective: The security operations team works a risk-adjusted vulnerability remediation queue — combining CVSS scores, asset criticality, and current threat actor exploitation activity — generated by the agent from scanner output and threat intelligence.
OKR KR [Adoption]: Agent risk-adjusted prioritisation applied to ≥95% of scanner-identified vulnerabilities within 6 months of go-live; asset criticality register and current threat intelligence integrated in every prioritisation run from go-live.
OKR KR [Acceptance]: ≥80% of agent-assigned priority rankings confirmed as appropriate by the security operations team lead on weekly review; critical-asset, high-exploitability vulnerabilities ranked in the top quartile in ≥90% of cases.
OKR KR [Cycle]: Risk-adjusted remediation queue updated within 4 hours of each scanner output publication, versus ≥24 hours of manual prioritisation under the prior CVSS-only approach.

[PAGE TEXT]
Cyber resilience & recovery
Digital operational resilience under DORA encompasses the bank's capacity to withstand, adapt, and recover from ICT-related disruption — tested through threat-led penetration testing (TLPT) and scenario-based tabletop exercises. Recovery capability is measured against defined Recovery Time Objectives and Recovery Point Objectives for critical ICT systems. Post-incident lessons-learned processes update the IRP, playbooks, and control environment. Under DORA Article 26, Tier 1 regulated entities must conduct TLPT at least every three years; tabletop exercises at higher frequency. NBKR and CBR digital resilience frameworks set equivalent requirements in the Central Asian and Russian supervisory context.
Lens
Scenario
Intent
Complexity

### CARD 10 [Enablement|M] Resilience Testing Scenario Design
urn: urn:financial-services:scenario:risk-control/cyber-risk/cyber-resilience-recovery/resilience-testing-scenario-design
intent: Agent designs tabletop exercise scenarios calibrated to the bank's specific threat profile and technology stack, incorporating current threat intelligence and lessons from prior incidents.
Problem to solve: Tabletop exercise scenarios are typically drawn from generic playbooks not calibrated to the bank's specific threat actor profile, technology stack, or prior incident history. Exercises test the team against scenarios that may not reflect the bank's actual threat landscape or DORA notification decision points.
Solution: Agent reads current threat intelligence on active threat actors targeting the banking sector, the bank's technology stack profile, and prior incident and near-miss records. It generates tabletop scenarios specific to the bank's profile — including realistic attack chains, DORA notification decision points, and lessons-learned integration. The CISO reviews and schedules the exercise.
OKR objective: The CISO schedules tabletop exercises built on agent-generated scenarios calibrated to the bank's specific threat actor profile, technology stack, and prior incident history, incorporating current threat intelligence and DORA notification decision points.
OKR KR [Adoption]: Agent-designed tabletop scenarios used for ≥2 exercises within 12 months of go-live; current threat intelligence applied and DORA notification decision points incorporated in every agent-designed scenario from go-live.
OKR KR [Acceptance]: ≥80% of agent-generated scenarios rated by the CISO as more relevant to the bank's actual threat profile than generic playbook scenarios; exercise participants confirm ≥75% of scenarios as realistic to the bank's environment in post-exercise surveys.
OKR KR [Cycle]: Tabletop scenario design document delivered within 5 business days of CISO brief, versus ≥3 weeks of manual scenario development from generic playbooks under the prior approach.

### CARD 11 [Automation|M] DORA TLPT Preparation Support
urn: urn:financial-services:scenario:risk-control/cyber-risk/cyber-resilience-recovery/dora-tlpt-preparation-support
intent: Agent assembles the DORA Article 26 TLPT preparation package — threat intelligence summary, technology scope map, and prior test findings — for the CISO and the appointed threat-led penetration testing provider.
Problem to solve: TLPT under DORA requires the bank to provide the testing provider with a structured threat profile, scope documentation, and prior test history before testing commences. Assembling this package from threat intelligence, asset inventory, and prior test records is a manual preparation step that delays the start of the testing engagement.
Solution: Agent reads current threat intelligence for the banking sector, the bank's technology asset inventory, and prior TLPT and penetration test findings. It assembles the TLPT preparation package in the DORA-prescribed format — threat actor profile, in-scope system inventory, prior finding history, and testing constraint summary. The CISO reviews and transmits to the testing provider.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 12 [Insights|M] Resilience & Recovery Metrics Dashboard
urn: urn:financial-services:scenario:risk-control/cyber-risk/cyber-resilience-recovery/resilience-recovery-metrics-dashboard
intent: Agent aggregates RTO/RPO test results, BCP exercise outcomes, and DORA incident recovery timelines into a quarterly resilience metrics dashboard for the CISO and Board Risk Committee.
Problem to solve: Resilience metrics — RTO and RPO achievement rates in testing, BCP exercise pass rates, DORA notification timeliness — are captured in separate test reports and incident records. The Board Risk Committee receives a narrative resilience summary without the underlying metric trends; deteriorating resilience performance is identified in individual test reports rather than as a portfolio signal.
Solution: Agent reads RTO/RPO test results, BCP exercise reports, and incident response timelines. It computes recovery metric trends by system criticality tier, flags systems where RTO/RPO targets were not met in the most recent test cycle, and assembles the quarterly resilience metrics dashboard for the CISO and Board Risk Committee.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
GenAI-enabled Banking and Financial Services Framework · v11i
