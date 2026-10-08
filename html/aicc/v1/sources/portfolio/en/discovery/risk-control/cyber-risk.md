# Cyber risk

Cyber risk is the risk of financial loss, operational disruption, or reputational damage arising from the compromise of a bank's technology assets or data. Operational-resilience and cybersecurity requirements, such as the Digital Operational Resilience Act (DORA), expect banks to maintain documented threat intelligence capabilities, vulnerability management programs, incident response plans, and digital operational resilience frameworks. The SWIFT Customer Security Program (CSP) adds a baseline of mandatory controls for correspondent banking participants. **The GenAI opportunity is to instrument cyber risk posture continuously** — processing threat intelligence volumes, vulnerability data, and incident signals that exceed manual review capacity — enabling the CISO to maintain awareness of the current threat landscape and respond at speed.

## Problems

### Threat & vulnerability exposure {#threat-exposure-detection}

| Lens | Problem |
| --- | --- |
| Insights & analytics | The CISO and threat intelligence team consume threat feeds from multiple vendor sources, CERT advisories, FS-ISAC bulletins, SWIFT CSP updates, and regulatory cyber notifications — hundreds of daily items. Relevance filtering against the Bank's specific technology stack and product mix is done manually; internal-exposure correlation — connecting an external CVE exploitation report to the Bank's own vulnerability scanner output — requires analyst judgment that is not systematic. |
| Enablement | Vulnerability prioritization requires the security operations team to apply CVSS scores to thousands of weekly scanner findings, without systematic cross-referencing of asset criticality, current threat actor exploitation activity, or banking-sector-specific exposure patterns. High-CVSS findings on non-critical assets consume remediation capacity ahead of medium-CVSS findings on core banking infrastructure. |
| Automation | Cyber risk reporting for the board and Risk Committee — threat landscape summary, vulnerability remediation status, security control effectiveness metrics — is assembled manually from multiple source systems on a quarterly cycle. The narrative format is consistent; the inputs are structured. |
| New business opportunities | A continuously instrumented cyber risk posture — daily threat briefings relevant to the Bank's specific exposure, risk-adjusted vulnerability queues updated as threat actor activity evolves — enables the CISO to allocate remediation resources based on current risk rather than the periodic vulnerability scan schedule. That posture quality is directly observable to the regulator in operational-resilience supervisory reviews. |

## Threat intelligence & exposure {#threat-intelligence-exposure}

Threat intelligence is the structured collection and analysis of information about threat actors, attack techniques, and emerging vulnerabilities relevant to the Bank's technology and product profile. FS-ISAC, SWIFT CSP, the national CERT, and commercial threat intelligence feeds provide the raw signal; the CISO's team must filter, correlate with internal exposure, and act. Operational-resilience requirements commonly expect banks to maintain threat intelligence capabilities proportionate to their ICT risk profile. Banking-sector-specific threat actors — state-sponsored groups targeting SWIFT connectivity, ransomware operators targeting core banking, credential-phishing campaigns targeting staff — require sector-specific intelligence sourcing and correlation.

### Threat Intelligence Briefing

- URN: urn:financial-services:scenario:risk-control/cyber-risk/threat-intelligence-exposure/threat-intelligence-briefing
- Lens: Insights
- Complexity: M
- Intent: The AI agent aggregates external threat intelligence feeds, sector-specific advisories, and internal detection signals into a daily CISO briefing ranked by relevance to the Bank's technology stack and product mix.
- Problem to solve: The CISO and threat intelligence team receive hundreds of daily items from vendor feeds, CERT advisories, FS-ISAC, SWIFT CSP, and regulatory notifications. Relevance filtering and internal-exposure correlation are performed manually; material threats can remain in the queue for days before reaching the CISO's attention.
- Solution: The AI agent ingests all threat intelligence sources, clusters threats by type, cross-references each cluster with the Bank's technology stack and known vulnerabilities, ranks by relevance, and produces a daily prioritized briefing for the CISO. The threat intelligence team confirms the top-ranked threats and responds to prioritized signals rather than raw feed volume.
- OKR: The CISO and threat intelligence team respond to a daily prioritized briefing — with threats ranked by relevance to the Bank's technology stack and product mix — rather than manually filtering and correlating raw feed volume.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's threat intelligence aggregation and prioritization covers all major feed sources (vendor feeds, CERT advisories, FS-ISAC, SWIFT CSP, regulatory notifications) within 6 months of go-live; daily prioritized briefing delivered to the CISO for ≥200 business days per year once live. |
| Acceptance | ≥75% of top-ranked daily threats confirmed as material to the Bank's environment by the threat intelligence team; critical threat-to-CISO attention latency reduced by ≥70% versus the prior manual filtering approach. |
| Cycle | Daily prioritized briefing delivered before the start of business each morning, versus ≥2 days of latency from signal emergence to CISO attention under the prior manual queue approach. |

### Threat Actor Exposure Mapping

- URN: urn:financial-services:scenario:risk-control/cyber-risk/threat-intelligence-exposure/threat-actor-exposure-mapping
- Lens: Insights
- Complexity: M
- Intent: The AI agent maps active banking-sector threat actors to the Bank's technology stack, identifying the specific systems and controls most relevant to each actor's known TTPs for the CISO's quarterly threat exposure review.
- Problem to solve: Threat intelligence briefings describe threat actors and their techniques but do not map them to the Bank's specific technology profile. The CISO and security architecture team perform this mapping manually for high-priority advisories; lower-priority actors and their relevance to specific systems are not systematically assessed.
- Solution: The AI agent reads threat intelligence on active banking-sector actors, extracts their known TTPs using the MITRE ATT&CK framework, and maps each TTP to the Bank's technology asset inventory. It identifies the systems most frequently targeted by each actor's techniques and delivers a quarterly threat-actor exposure map to the CISO; the security architecture team reviews the mappings.
- OKR: The CISO receives a quarterly threat-actor exposure map — the known TTPs of active banking-sector threat actors mapped to the Bank's technology asset inventory — identifying the systems most frequently targeted by each actor's techniques.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's exposure map is produced for ≥4 consecutive quarterly threat exposure reviews within 18 months of go-live; TTPs extracted using the MITRE ATT&CK framework and mapped to the full technology asset inventory in every run. |
| Acceptance | ≥75% of the AI agent's TTP-to-system mappings confirmed as accurate by the security architecture team on review; ≥80% of quarterly maps used by the CISO in the threat exposure review without supplementary manual mapping. |
| Cycle | Quarterly exposure map delivered within 5 business days of the review cycle start, versus manual mapping performed only for high-priority advisories under the prior approach. |

### Threat Intelligence Control Gap Analysis

- URN: urn:financial-services:scenario:risk-control/cyber-risk/threat-intelligence-exposure/threat-intel-control-gap-analysis
- Lens: Enablement
- Complexity: M
- Intent: The AI agent cross-references the Bank's control framework against current threat actor TTPs, identifies controls that do not address observed attack techniques, and delivers a gap analysis to the CISO for security program prioritization.
- Problem to solve: The Bank's control framework is assessed in the annual risk and control self-assessment (RCSA) cycle. Emerging attack techniques that have appeared in threat intelligence since the last RCSA cycle may not be covered by current controls; the gap is not visible until the next scheduled assessment.
- Solution: The AI agent reads current threat intelligence TTPs, maps each technique to the NIST CSF or CIS control framework, and cross-references against the Bank's documented control inventory. It identifies TTP-to-control gaps and delivers the analysis to the CISO for prioritization in the security program roadmap.
- OKR: The CISO prioritizes the security program roadmap from the AI agent's gap analysis identifying current threat actor TTPs that the Bank's documented control inventory does not address, without waiting for the next annual assessment cycle.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's gap analysis runs against 100% of the documented control inventory at least quarterly within 6 months of go-live; each current TTP mapped to the NIST CSF or CIS control framework in every run. |
| Acceptance | ≥70% of AI-identified TTP-to-control gaps confirmed as genuine by the CISO on review; ≥75% of confirmed gaps entered into the security program roadmap within one quarter. |
| Cycle | Gap analysis delivered within 5 business days of each quarterly run, versus gaps becoming visible only at the next annual risk and control self-assessment cycle. |

## Incident detection & response {#incident-detection-response}

Cyber incident response is the structured process of detecting, containing, eradicating, and recovering from a security incident — governed by an Incident Response Plan (IRP) that defines roles, escalation paths, and regulatory notification obligations. Incident-reporting requirements, such as DORA, commonly provide that a major ICT incident is notified to the regulator within 4 hours of classification, with a detailed incident report within 72 hours. Incident detection latency — the time between initial compromise and detection — is the primary driver of incident severity; mean time to detect (MTTD) and mean time to respond (MTTR) are the KPIs governing security operations effectiveness.

### Cyber Incident Triage Pack

- URN: urn:financial-services:scenario:risk-control/cyber-risk/incident-detection-response/cyber-incident-triage-pack
- Lens: Automation
- Complexity: S
- Intent: The AI agent assembles the initial incident triage pack when a cyber alert is escalated — asset inventory context, historical alert pattern, regulatory notification checklist, and stakeholder contact list — so the incident response team has an actionable dossier at the start of the response.
- Problem to solve: When a cyber incident is escalated, the response team assembles asset context, prior alert history, regulatory notification thresholds, and stakeholder contacts from multiple systems while simultaneously managing containment. The triage context assembly step delays initial response actions in a time-critical window.
- Solution: The AI agent reads the alert from the SIEM, retrieves asset inventory context, surfaces the prior 90-day alert history for that asset, applies the regulatory notification threshold check, and populates the incident triage template. The incident commander receives a pre-populated dossier and focuses on containment decisions from the first minute.
- OKR: The incident commander begins containment decisions from the first minute with an AI-assembled triage dossier — covering asset context, alert history, regulatory notification checklist, and stakeholder contacts — available at the point of escalation.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's triage pack is assembled for ≥95% of escalated cyber incidents within 12 months of go-live; regulatory notification threshold check applied automatically to every incident from go-live. |
| Acceptance | ≥85% of AI-assembled triage packs rated as complete by incident commanders without requiring supplemental manual lookups during the initial response; regulatory notification checklist accuracy validated at ≥95% in quarterly simulation exercises. |
| Cycle | Triage pack delivered to the incident commander within 5 minutes of alert escalation, versus ≥30 minutes of manual assembly under the prior approach. |

### Major ICT Incident Notification Draft

- URN: urn:financial-services:scenario:risk-control/cyber-risk/incident-detection-response/incident-dora-notification-draft
- Lens: Automation
- Complexity: S
- Intent: The AI agent generates the initial notification draft for a major ICT incident — incident classification, affected systems, business impact estimate, and containment status — within the regulatory notification window, commonly four hours from incident classification.
- Problem to solve: Incident-reporting requirements, such as DORA, commonly require a major ICT incident to be notified to the regulator within four hours of classification. Drafting the notification under time pressure, with incomplete information and simultaneous incident management activity, produces notifications that may omit required fields or misstate the incident classification.
- Solution: The AI agent reads the incident triage record, applies the major incident classification criteria, and generates the initial notification draft in the prescribed format — incident type, classification rationale, affected systems, estimated business impact, and containment actions taken. The incident commander reviews and submits within the four-hour window.
- OKR: The incident commander reviews and submits the initial major ICT incident notification — incident type, classification rationale, affected systems, estimated business impact, and containment actions — from an AI-generated draft within the four-hour notification window.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent is used to generate the initial notification draft for 100% of incidents classified as major ICT incidents within 6 months of go-live; major incident classification criteria applied in every draft. |
| Acceptance | ≥90% of AI-generated drafts submitted by the incident commander with only factual updates; required-field omissions in submitted notifications reduced to zero. |
| Cycle | Notification draft available to the incident commander within 30 minutes of major incident classification, leaving ≥3 hours of the four-hour window for review, versus drafting under time pressure during incident management. |

### Cyber Incident Post-Mortem Pack

- URN: urn:financial-services:scenario:risk-control/cyber-risk/incident-detection-response/incident-post-mortem-pack
- Lens: Insights
- Complexity: M
- Intent: The AI agent assembles the post-incident review pack from the event timeline, containment and recovery logs, and communications records, and identifies control gaps and detection improvements for the CISO's lessons-learned review.
- Problem to solve: Post-incident reviews are conducted after containment but the pack assembly — incident timeline reconstruction, control failure identification, detection gap analysis — consumes security team hours at a point when the team is managing residual remediation activity.
- Solution: The AI agent reads SIEM event logs, containment action records, recovery timeline, and communications records. It reconstructs the incident timeline, identifies the initial access vector and detection point, maps the gap between compromise and detection, and flags control and detection improvements. The CISO reviews the pack and assigns remediation ownership in the lessons-learned session.
- OKR: The CISO runs the lessons-learned session from an AI-assembled post-incident review pack — reconstructed timeline, initial access vector, detection point, compromise-to-detection gap, and flagged control and detection improvements — and assigns remediation ownership.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent is used to assemble the post-incident review pack for ≥90% of cyber incidents subject to post-incident review within 12 months of go-live; SIEM event logs, containment action records, recovery timeline, and communications records read in every run. |
| Acceptance | ≥80% of AI-assembled packs accepted by the CISO without timeline rework; ≥75% of AI-flagged control and detection improvements assigned a remediation owner in the lessons-learned session. |
| Cycle | Post-incident review pack delivered within 3 business days of incident containment, versus ≥2 weeks of security team assembly alongside residual remediation under the prior approach. |

## Vulnerability & patch management {#vulnerability-patch-management}

Vulnerability management is the program of discovering, assessing, prioritizing, and remediating known security weaknesses in the Bank's technology estate. Scanner tools generate thousands of findings per week; the CVSS scoring system provides a standardized severity measure. Operational-resilience requirements commonly call for documented vulnerability management processes with defined remediation timeframes by severity. Supervisors commonly expect critical vulnerabilities on internet-facing systems to be remediated within 30 days; exploited vulnerabilities require emergency patching. Patch management coordinates the remediation workflow — testing compatibility, scheduling deployment, and tracking completion — across infrastructure, application, and endpoint layers.

### Patch Compliance Status Report

- URN: urn:financial-services:scenario:risk-control/cyber-risk/vulnerability-patch-management/patch-compliance-status-report
- Lens: Automation
- Complexity: S
- Intent: The AI agent reads patch deployment status across all asset tiers, computes compliance rates against the required remediation timeframes by severity, and delivers a weekly patch compliance report to the CISO.
- Problem to solve: Supervisory requirements set remediation timeframes for critical and high-severity vulnerabilities. Patch compliance status is tracked across infrastructure, application, and endpoint tiers in separate tools; producing a consolidated compliance view for the CISO requires manual aggregation from multiple sources.
- Solution: The AI agent reads patch deployment status from infrastructure, application, and endpoint management tools, applies the severity-tiered remediation timeframe schedule, computes compliance rates by asset tier and severity level, and produces the weekly compliance report flagging assets overdue by tier. The CISO uses the report to direct remediation focus.
- OKR: The CISO directs remediation focus from a weekly patch compliance report — compliance rates against the severity-tiered remediation timeframes by asset tier, with overdue assets flagged — consolidated by the AI agent across infrastructure, application, and endpoint tools.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent is used to produce the weekly patch compliance report for ≥48 weeks within 12 months of go-live; infrastructure, application, and endpoint management tools all read in every run from go-live. |
| Acceptance | ≥90% of weekly reports accepted by the CISO without manual reconciliation against source tools; overdue asset flags confirmed accurate in ≥95% of cases on monthly quality checks. |
| Cycle | Weekly compliance report delivered within 4 hours of the weekly data cut, versus ≥1 business day of manual aggregation from multiple tools under the prior approach. |

### Vulnerability Exception Management Tracker

- URN: urn:financial-services:scenario:risk-control/cyber-risk/vulnerability-patch-management/vulnerability-exception-management
- Lens: Automation
- Complexity: S
- Intent: The AI agent tracks active vulnerability exceptions — cases where patching is deferred with documented business justification — monitors expiry dates, and generates the exception renewal or escalation queue for the CISO's review.
- Problem to solve: Vulnerabilities that cannot be immediately patched require a documented exception with a compensating control and expiry date. With dozens of active exceptions across the estate, monitoring expiry dates and ensuring renewals are approved before exceptions lapse is a manual tracking task that creates the risk of unmanaged expired exceptions.
- Solution: The AI agent reads the active exception register, monitors expiry dates, flags exceptions approaching expiry without a renewal submission, and generates the CISO's weekly exception review queue. Lapsed exceptions are escalated automatically to the vulnerability management lead.
- OKR: The CISO reviews a weekly AI-generated exception queue — active vulnerability exceptions approaching expiry without a renewal submission — and lapsed exceptions are escalated automatically to the vulnerability management lead, so no exception expires unmanaged.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent tracks 100% of the active exception register within 3 months of go-live; weekly exception review queue generated for the CISO for ≥48 weeks in year 1. |
| Acceptance | ≥95% of AI-flagged exceptions confirmed by the CISO as correctly due for renewal or escalation; exceptions lapsing without an approved renewal or escalation reduced to zero. |
| Cycle | Exceptions flagged ≥2 weeks before expiry and lapsed exceptions escalated within 1 business day, versus manual expiry tracking across dozens of exceptions under the prior approach. |

### Vulnerability Risk-Adjusted Prioritization

- URN: urn:financial-services:scenario:risk-control/cyber-risk/vulnerability-patch-management/vulnerability-prioritization-narrative
- Lens: Insights
- Complexity: M
- Intent: The AI agent cross-references scanner output with asset criticality and threat intelligence to produce a risk-adjusted remediation queue for the security operations team.
- Problem to solve: Vulnerability scanners generate thousands of weekly findings. CVSS-based prioritization without asset criticality or current exploitation activity places high-CVSS findings on low-criticality assets ahead of lower-CVSS findings on core banking infrastructure where exploitation carries materially higher impact.
- Solution: The AI agent reads scanner output, cross-references each finding with the asset criticality register and current threat intelligence on active exploitation, and produces a risk-adjusted prioritization ranking by critical-asset score, exploitability, and current threat actor relevance. The security operations team works the ranked queue; the team lead reviews the rankings weekly.
- OKR: The security operations team works a risk-adjusted vulnerability remediation queue — combining CVSS scores, asset criticality, and current threat actor exploitation activity — generated by the AI agent from scanner output and threat intelligence.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's risk-adjusted prioritization is applied to ≥95% of scanner-identified vulnerabilities within 6 months of go-live; asset criticality register and current threat intelligence integrated in every prioritization run from go-live. |
| Acceptance | ≥80% of AI-assigned priority rankings confirmed as appropriate by the security operations team lead on weekly review; critical-asset, high-exploitability vulnerabilities ranked in the top quartile in ≥90% of cases. |
| Cycle | Risk-adjusted remediation queue updated within 4 hours of each scanner output publication, versus ≥24 hours of manual prioritization under the prior CVSS-only approach. |

## Cyber resilience & recovery {#cyber-resilience-recovery}

Digital operational resilience is the Bank's capacity to withstand, adapt to, and recover from ICT-related disruption — tested through threat-led penetration testing (TLPT) and scenario-based tabletop exercises. Recovery capability is measured against defined Recovery Time Objectives and Recovery Point Objectives for critical ICT systems. Post-incident lessons-learned processes update the IRP, playbooks, and control environment. Where TLPT is required of a bank, as for significant institutions under frameworks such as DORA, it is commonly conducted at least every three years, with tabletop exercises at higher frequency.

### Resilience Testing Scenario Design

- URN: urn:financial-services:scenario:risk-control/cyber-risk/cyber-resilience-recovery/resilience-testing-scenario-design
- Lens: Enablement
- Complexity: M
- Intent: The AI agent designs tabletop exercise scenarios calibrated to the Bank's specific threat profile and technology stack, incorporating current threat intelligence and lessons from prior incidents.
- Problem to solve: Tabletop exercise scenarios are typically drawn from generic playbooks not calibrated to the Bank's specific threat actor profile, technology stack, or prior incident history. Exercises test the team against scenarios that may not reflect the Bank's actual threat landscape or regulatory notification decision points.
- Solution: The AI agent reads current threat intelligence on active threat actors targeting the banking sector, the Bank's technology stack profile, and prior incident and near-miss records. It generates tabletop scenarios specific to the Bank's profile — including realistic attack chains, regulatory notification decision points, and lessons-learned integration. The CISO reviews and schedules the exercise.
- OKR: The CISO schedules tabletop exercises built on AI-generated scenarios calibrated to the Bank's specific threat actor profile, technology stack, and prior incident history, incorporating current threat intelligence and regulatory notification decision points.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-designed tabletop scenarios used for ≥2 exercises within 12 months of go-live; current threat intelligence applied and regulatory notification decision points incorporated in every AI-designed scenario from go-live. |
| Acceptance | ≥80% of AI-generated scenarios rated by the CISO as more relevant to the Bank's actual threat profile than generic playbook scenarios; exercise participants confirm ≥75% of scenarios as realistic to the Bank's environment in post-exercise surveys. |
| Cycle | Tabletop scenario design document delivered within 5 business days of CISO brief, versus ≥3 weeks of manual scenario development from generic playbooks under the prior approach. |

### TLPT Preparation Support

- URN: urn:financial-services:scenario:risk-control/cyber-risk/cyber-resilience-recovery/dora-tlpt-preparation-support
- Lens: Automation
- Complexity: M
- Intent: Where the Bank conducts threat-led penetration testing (TLPT), the AI agent assembles the TLPT preparation package — threat intelligence summary, technology scope map, and prior test findings — for the CISO and the appointed testing provider.
- Problem to solve: TLPT requires the Bank to provide the testing provider with a structured threat profile, scope documentation, and prior test history before testing commences. Assembling this package from threat intelligence, asset inventory, and prior test records is a manual preparation step that delays the start of the testing engagement.
- Solution: The AI agent reads current threat intelligence for the banking sector, the Bank's technology asset inventory, and prior TLPT and penetration test findings. It assembles the TLPT preparation package in the prescribed format — threat actor profile, in-scope system inventory, prior finding history, and testing constraint summary. The CISO reviews the package and transmits it to the testing provider.
- OKR: The CISO reviews and transmits to the appointed testing provider an AI-assembled TLPT preparation package — threat actor profile, in-scope system inventory, prior finding history, and testing constraint summary — in the prescribed format.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent is used to assemble the preparation package for 100% of TLPT engagements within 12 months of go-live; current threat intelligence, technology asset inventory, and prior TLPT and penetration test findings read in every run. |
| Acceptance | ≥80% of package sections accepted by the CISO without structural revision; the testing provider's requests for additional scoping information reduced by ≥50% versus the prior engagement. |
| Cycle | Preparation package delivered within 5 business days of engagement confirmation, versus ≥3 weeks of manual assembly delaying the start of testing under the prior approach. |

### Resilience & Recovery Metrics Dashboard

- URN: urn:financial-services:scenario:risk-control/cyber-risk/cyber-resilience-recovery/resilience-recovery-metrics-dashboard
- Lens: Insights
- Complexity: M
- Intent: The AI agent aggregates RTO/RPO test results, BCP exercise outcomes, and incident recovery timelines into a quarterly resilience metrics dashboard for the CISO and Board Risk Committee.
- Problem to solve: Resilience metrics — RTO and RPO achievement rates in testing, BCP exercise pass rates, regulatory notification timeliness — are captured in separate test reports and incident records. The Board Risk Committee receives a narrative resilience summary without the underlying metric trends; deteriorating resilience performance is identified in individual test reports rather than as a portfolio signal.
- Solution: The AI agent reads RTO/RPO test results, BCP exercise reports, and incident response timelines. It computes recovery metric trends by system criticality tier, flags systems where RTO/RPO targets were not met in the most recent test cycle, and assembles the quarterly resilience metrics dashboard for the CISO and Board Risk Committee.
- OKR: The CISO and Board Risk Committee receive a quarterly resilience metrics dashboard — RTO/RPO achievement trends by system criticality tier, BCP exercise outcomes, and incident recovery timelines — with systems that missed targets in the latest test cycle flagged.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's resilience dashboard is assembled for ≥4 consecutive quarterly Board Risk Committee meetings within 18 months of go-live; RTO/RPO test results, BCP exercise reports, and incident response timelines read in every run. |
| Acceptance | ≥85% of dashboards accepted by the CISO without manual metric recomputation; systems flagged for missed RTO/RPO targets confirmed accurate against test reports in ≥95% of cases. |
| Cycle | Quarterly dashboard delivered within 5 business days of quarter-end, versus a narrative resilience summary without underlying metric trends under the prior approach. |
