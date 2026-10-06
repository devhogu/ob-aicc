# 

source: html-alt/financial-services/en/risk-control/internal-audit/index.html


[PAGE TEXT]
Audit universe & risk ranking
The audit universe is the complete population of auditable entities — business processes, legal entities, systems, and projects — across which the internal audit function allocates its annual assurance capacity. Risk-based audit planning, required by IIA Standards, ranks universe entities by inherent risk and control effectiveness to prioritise the highest-risk areas for audit coverage in each planning cycle. The ranking combines inputs from the risk register, prior audit findings, operational risk events, regulatory examination outcomes, and business performance. Entities not covered in a planning cycle carry a residual assurance gap; the CAE must document and disclose the gap to the Audit Committee.
Lens
Scenario
Intent
Complexity

### CARD 1 [Enablement|M] Audit Universe Risk Ranking
urn: urn:financial-services:scenario:risk-control/internal-audit/audit-universe-risk-ranking/audit-universe-risk-ranking
intent: Agent reads the risk register, prior audit findings, RCSA outputs, and operational event data to produce a ranked audit universe, supporting the CAE's annual audit plan prioritization.
Problem to solve: Annual audit plan prioritization requires the CAE and audit planning team to manually assess the risk profile of each audit universe entity drawing from the risk register, prior findings, RCSA outputs, and loss event data. With 80–150 audit universe entities, the assessment is necessarily judgemental and time-constrained.
Solution: Agent reads the current risk register, prior audit findings by entity, RCSA risk ratings, loss event history, and regulatory interaction records. It applies a multi-factor risk ranking model and produces a ranked audit universe with the contributing factors visible per entity. The CAE reviews rankings, applies professional judgement, and constructs the annual plan from the agent-generated base.
OKR objective: The CAE constructs the annual audit plan from an agent-generated risk-ranked audit universe that integrates risk register, prior findings, RCSA, and loss event data across all entities.
OKR KR [Adoption]: Agent-generated ranked audit universe used as the base for annual plan construction in ≥1 full annual planning cycle within 18 months of go-live; ≥80% of audit universe entities covered by the ranking model.
OKR KR [Acceptance]: ≥75% of agent-assigned risk rankings accepted by the CAE without material reordering; ranking model covers all four contributing data sources (risk register, prior findings, RCSA, loss events) for ≥90% of entities.
OKR KR [Cycle]: Initial audit universe risk ranking produced within 5 business days of data refresh, versus ≥4 weeks of manual assessment under the prior approach.

### CARD 2 [Insights|M] Audit Coverage Gap Analysis
urn: urn:financial-services:scenario:risk-control/internal-audit/audit-universe-risk-ranking/audit-coverage-gap-analysis
intent: Agent compares the proposed annual audit plan against the risk-ranked universe, identifies coverage gaps where high-risk entities are scheduled infrequently, and delivers a gap analysis to the CAE before the Audit Committee plan approval.
Problem to solve: The annual audit plan is constructed from the risk-ranked universe subject to available audit days. High-risk entities that fall below the resource threshold in a given year create an assurance gap; identifying these gaps and their cumulative effect across multi-year coverage cycles requires systematic analysis that is typically performed judgementally.
Solution: Agent reads the current-year audit plan, the risk-ranked universe, and the three-year rolling coverage history. It identifies high-risk entities with gaps in coverage frequency, computes the cumulative risk exposure represented by uncovered entities, and delivers the gap analysis to the CAE for Audit Committee disclosure.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 3 [Insights|M] Audit Plan Dynamic Re-Ranking
urn: urn:financial-services:scenario:risk-control/internal-audit/audit-universe-risk-ranking/audit-plan-dynamic-reranking
intent: Agent re-ranks the audit universe at mid-year using updated risk register, operational events, and regulatory interaction data, flagging entities whose risk profile has materially changed since the plan was approved for CAE consideration.
Problem to solve: The annual audit plan is set at year-start based on the risk ranking at that date. Material risk developments during the year — a significant operational loss event, a regulatory examination finding, or a major process change — may increase the risk profile of entities not scheduled in the current plan, but the plan is not systematically reassessed mid-year.
Solution: Agent re-reads the risk register, loss event register, and regulatory interaction records at mid-year and re-ranks the audit universe. It flags entities whose risk score has materially increased since plan approval and delivers the re-ranking to the CAE for discretionary plan adjustment or Audit Committee notification.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
Findings & thematic synthesis
Finding synthesis identifies the common root causes, recurring themes, and systemic patterns that run across individual audit findings — enabling the Audit Committee to direct remediation at root causes rather than individual findings. IIA Standards expect the CAE to provide thematic analysis, not merely per-engagement summaries; supervisors assess whether the audit function is providing value-adding assurance or mechanical finding-by-finding documentation. Cross-audit correlation — connecting audit findings with operational risk events, regulatory observations, and customer complaints sharing the same root cause — enhances the depth of assurance provided.
Lens
Scenario
Intent
Complexity

### CARD 4 [Insights|M] Audit Findings Thematic Synthesis
urn: urn:financial-services:scenario:risk-control/internal-audit/findings-thematic-synthesis/audit-findings-synthesis
intent: Agent clusters findings across all engagements in the year, identifies repeat findings and systemic root causes, and generates the Audit Committee thematic synthesis pack.
Problem to solve: The Audit Committee receives per-engagement summaries without a synthesised thematic picture. Cross-audit patterns — a common root cause across separate engagements, or a repeat finding from the prior year — surface only at the annual review.
Solution: Agent reads all completed audit finding records, clusters by theme and root cause, identifies repeats against prior-year records, and generates the Audit Committee thematic synthesis. It flags clusters where systemic remediation is warranted; the CAE reviews before Audit Committee submission.
OKR objective: The Audit Committee receives a thematic synthesis of all engagement findings — with repeat patterns and systemic root causes identified — rather than per-engagement summaries in isolation.
OKR KR [Adoption]: Agent used to produce the Audit Committee thematic synthesis pack for ≥4 quarterly committee cycles in year 1, covering 100% of completed engagements within each cycle.
OKR KR [Acceptance]: ≥80% of thematic clusters rated as decision-relevant by Audit Committee members; CAE accepts ≥85% of agent-generated synthesis packs without material structural revision.
OKR KR [Cycle]: Synthesis pack preparation time reduced from ≥5 analyst-days of manual cross-engagement review to ≤1 day of CAE editorial review per cycle.

### CARD 5 [Enablement|M] Repeat Finding Root Cause Drill-Down
urn: urn:financial-services:scenario:risk-control/internal-audit/findings-thematic-synthesis/repeat-finding-root-cause-drill
intent: Agent identifies repeat findings across the rolling three-year audit history, drills into root cause patterns, and produces a structured repeat-finding analysis for the CAE to present to the Audit Committee as evidence of systemic control weakness.
Problem to solve: IIA Standards require the CAE to identify and report on repeat findings. The identification of repeats across three years of audit records — matching findings by root cause rather than by entity or audit title — is performed manually in the annual thematic review and is constrained by the analyst's recall of prior engagements.
Solution: Agent reads the three-year finding archive, applies semantic matching to identify findings with the same root cause across different engagements and entities, and produces the repeat-finding analysis with the finding chain per root cause. The CAE uses the output for the Audit Committee's systemic weakness discussion.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 6 [Insights|M] Cross-Audit Risk Correlation Analysis
urn: urn:financial-services:scenario:risk-control/internal-audit/findings-thematic-synthesis/cross-audit-risk-correlation
intent: Agent cross-references audit findings with operational risk events and regulatory observations to identify shared root causes, providing the Audit Committee with an integrated three-lines view of systemic control weaknesses.
Problem to solve: Audit findings, operational risk events, and regulatory observations are managed in separate functions. Root causes shared across all three lines — a common process failure that generates audit findings, operational losses, and regulatory observations simultaneously — are identified in the annual thematic review rather than on a rolling basis.
Solution: Agent reads the audit finding register, operational risk event database, and regulatory observation tracker. It applies root-cause matching across all three populations, identifies shared root causes, and quantifies the combined finding, event, and observation count per root cause. The Audit Committee receives the integrated three-lines view in the quarterly synthesis pack.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
Audit execution & workpapers
Audit execution covers the fieldwork phase of each engagement — planning the audit approach, executing test procedures, documenting evidence in workpapers, and drafting findings. IIA Standards require workpapers that document objectives, procedures, evidence, and conclusions for each test; the workpaper set is the primary quality-control artifact reviewed by the Audit Committee and supervisors. For a 30-50 audit programme, execution documentation consumes the majority of the audit team's calendar. Pre-populating workpaper templates with prior-period content, system-generated control test data, and structured finding templates reduces per-engagement time without reducing assurance quality.
Lens
Scenario
Intent
Complexity

### CARD 7 [Enablement|S] Audit Finding Drafting Support
urn: urn:financial-services:scenario:risk-control/internal-audit/audit-execution-workpapers/audit-finding-drafting-support
intent: Agent drafts audit findings in the IIA-compliant condition/criteria/cause/effect/recommendation structure from the auditor's fieldwork notes, reducing per-finding drafting time and improving consistency across the team.
Problem to solve: Audit finding quality varies by auditor experience. Senior auditors spend material time editing junior drafts to meet IIA Standards and the bank's quality requirements — a review bottleneck that extends the time from testing completion to report issuance.
Solution: Agent reads the auditor's fieldwork notes and test evidence for each finding. It drafts the finding in the bank's standard IIA-compliant format — condition, criteria, cause, effect, risk rating, and recommended management action — for the senior auditor to review, refine, and approve.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 8 [Insights|S] Workpaper Quality Review Check
urn: urn:financial-services:scenario:risk-control/internal-audit/audit-execution-workpapers/workpaper-quality-review
intent: Agent reviews completed workpapers against the IIA Standards quality checklist before QA supervisor review, flagging documentation gaps and consistency issues for the auditor to resolve.
Problem to solve: QA supervisor review identifies workpaper deficiencies after the auditor considers the file complete, creating rework cycles that delay report issuance. Common deficiencies — unsigned objectives, unticked test steps, missing evidence cross-references — could be caught by systematic checklist review before QA submission.
Solution: Agent reads completed workpaper files and applies the IIA Standards and bank-policy quality checklist — objectives documented, procedures signed off, evidence cross-referenced, findings rated per the risk scale. It returns a flagged deficiency list to the auditor before QA submission, reducing the first-pass deficiency rate.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 9 [Automation|M] Audit Workpaper Pre-Population
urn: urn:financial-services:scenario:risk-control/internal-audit/audit-execution-workpapers/workpaper-pre-population
intent: Agent pre-populates audit workpaper templates with prior-period test results, system-generated control test data, and relevant policy extracts ahead of each engagement, reducing per-engagement preparation time.
Problem to solve: Each audit engagement requires the senior auditor to prepare workpaper templates before fieldwork begins — incorporating prior-period findings, control test criteria from the policy library, and relevant system data. For a 30-50 engagement annual programme, this preparation consumes audit team hours before testing begins.
Solution: Agent reads the prior-period workpaper set, current control inventory, policy library, and system data feeds relevant to each engagement scope. It pre-populates the workpaper template with prior test results, control objectives, and available system-generated evidence, leaving the auditor to execute tests and document professional judgement sections.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
Remediation tracking
Remediation tracking monitors the progress of management actions against each open finding — covering audit findings, regulatory matters, and internal control gaps — from commitment through to evidence-based closure. Under IIA Standards, the audit function is responsible for following up on open findings to ensure management actions are completed on schedule; lapsed remediation without escalation is a quality finding in itself. The Audit Committee receives a remediation status pack each cycle; supervisors expect evidence that the audit function actively monitors remediation rather than passively recording it. With 150-200 open items at any time, manual tracking at item level consumes significant audit team capacity.
Lens
Scenario
Intent
Complexity

### CARD 10 [Automation|S] Remediation Evidence Quality Check
urn: urn:financial-services:scenario:risk-control/internal-audit/remediation-tracking/remediation-evidence-quality-check
intent: Agent reviews management-submitted remediation evidence against the original finding's action description, flags submissions that do not address the finding, and returns a quality assessment to the audit manager before closure is approved.
Problem to solve: Remediation closure requires the audit manager to review management-submitted evidence against the original finding. Evidence submissions that are incomplete or address a symptom rather than the root cause identified in the finding are identified in the closure review, creating a back-and-forth cycle that delays closure and consumes audit team capacity.
Solution: Agent reads the original finding text, the agreed management action, and the submitted evidence. It assesses whether the evidence demonstrates the specific action committed to, flags gaps or misalignments, and returns a quality assessment to the audit manager before closure is formally approved.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 11 [Automation|M] Remediation Tracking & Status Reporting
urn: urn:financial-services:scenario:risk-control/internal-audit/remediation-tracking/remediation-tracking-status-reporting
intent: Agent aggregates remediation status across all open findings, applies pattern detection to identify at-risk items and capacity stress, and generates the Audit Committee status pack.
Problem to solve: Tracking 150–200 open remediation items across audit findings, regulatory matters, and control gaps — with status self-reported by owners — consumes substantial analyst hours per Audit Committee cycle in manual aggregation. At-risk items surface when owners report delay, typically close to the deadline.
Solution: Agent reads remediation records from audit management systems, regulatory matter trackers, and control registers. It aggregates status, applies delay-pattern detection to identify structurally at-risk items, and generates the Audit Committee pack with capacity analysis and escalation recommendations. The CAE reviews and adds judgement before distribution.
OKR objective: The CAE reviews and distributes an agent-generated Audit Committee status pack — aggregating 150–200 open remediation items with delay-pattern detection applied and at-risk items escalated — rather than producing the pack through manual status aggregation.
OKR KR [Adoption]: Agent used to generate the Audit Committee remediation status pack for ≥4 consecutive committee cycles within 18 months of go-live; delay-pattern detection applied to 100% of open items in every run.
OKR KR [Acceptance]: ≥80% of agent-generated status packs accepted by the CAE without material structural revision before distribution; at-risk items identified by delay-pattern detection confirmed as genuinely at risk in ≥75% of cases on review.
OKR KR [Cycle]: Remediation status pack produced within 2 business days of data cut, versus ≥5 analyst-days of manual aggregation under the prior approach.

### CARD 12 [Insights|M] Remediation Systemic Delay Analysis
urn: urn:financial-services:scenario:risk-control/internal-audit/remediation-tracking/remediation-systemic-delay-analysis
intent: Agent analyses the remediation history to identify business units, finding categories, and root causes with systematically longer remediation cycles, and delivers the analysis to the CAE for Audit Committee escalation.
Problem to solve: Individual remediation delays are tracked and escalated per item. Patterns of delay — a specific business unit consistently missing remediation deadlines, or a category of finding that systematically takes longer to remediate than management commits — are visible only in aggregate analysis performed infrequently.
Solution: Agent reads the full remediation history, computes actual vs committed remediation cycle by business unit, finding category, and root cause, and identifies statistically significant delay patterns. The CAE receives the analysis for Audit Committee presentation as part of the programme quality section of the annual report.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
GenAI-enabled Banking and Financial Services Framework · v11i
