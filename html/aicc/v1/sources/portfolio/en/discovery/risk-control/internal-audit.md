# Internal audit

Internal audit is a bank's independent assurance function — the third line of defense that provides the board and Audit Committee with objective assurance over the adequacy and effectiveness of risk management and internal controls. In line with the IIA Standards, the audit function maintains a risk-based audit plan, conducts audits with independence and objectivity, and reports findings with sufficient clarity for the Audit Committee to take action. Supervisors assess the quality of the internal audit function in the supervisory review process; a downgraded supervisory rating for internal audit quality can carry capital implications. **The GenAI opportunity is to compress the audit cycle** — finding synthesis, remediation tracking, and audit planning — releasing specialist capacity from data assembly to substantive assurance work.

## Problems

### Audit planning & execution {#audit-planning-execution}

| Lens | Problem |
| --- | --- |
| Insights & analytics | Risk-based audit planning requires the Chief Audit Executive (CAE) to rank the audit universe — typically 80–150 auditable entities — by inherent risk, control effectiveness, audit coverage history, and regulatory change. Each dimension draws from different data sources: risk registers, prior audit results, regulatory examination findings, operational risk events, and business performance. Assembling the ranking from these sources is a multi-week exercise each planning cycle. |
| Enablement | Audit execution — workpaper preparation, control testing evidence assembly, and finding documentation — consumes the majority of the audit team's calendar per engagement. Pre-population of workpaper templates, automated evidence extraction from system logs, and structured finding documentation would reduce execution time per audit, enabling higher audit coverage with the same headcount. |
| Automation | Audit report drafting — the structured document that summarizes audit scope, findings, management responses, and recommended actions — follows a defined format per engagement type. The findings themselves are documented during execution; the report draft draws from completed workpapers and finding records. |
| New business opportunities | A risk-based audit plan that is updated continuously — as new operational risk events, regulatory findings, and control failures emerge — rather than annually or semi-annually gives the CAE a dynamic resource allocation signal. Audit capacity can be directed toward areas where risk is rising between planned engagements, improving assurance quality without proportional headcount investment. |

## Audit universe & risk ranking {#audit-universe-risk-ranking}

The audit universe is the complete population of auditable entities — business processes, legal entities, systems, and projects — across which the internal audit function allocates its annual assurance capacity. Risk-based audit planning, in line with the IIA Standards, ranks universe entities by inherent risk and control effectiveness to prioritize the highest-risk areas for audit coverage in each planning cycle. The ranking combines inputs from the risk register, prior audit findings, operational risk events, regulatory examination outcomes, and business performance. Entities not covered in a planning cycle carry a residual assurance gap; the CAE must document and disclose the gap to the Audit Committee.

### Audit Universe Risk Ranking

- URN: urn:financial-services:scenario:risk-control/internal-audit/audit-universe-risk-ranking/audit-universe-risk-ranking
- Lens: Enablement
- Complexity: M
- Intent: The AI agent reads the risk register, prior audit findings, RCSA outputs, and operational event data to produce a ranked audit universe, supporting the CAE's annual audit plan prioritization.
- Problem to solve: Annual audit plan prioritization requires the CAE and audit planning team to manually assess the risk profile of each audit universe entity drawing from the risk register, prior findings, RCSA outputs, and loss event data. With 80–150 audit universe entities, the assessment is necessarily judgmental and time-constrained.
- Solution: The AI agent reads the current risk register, prior audit findings by entity, RCSA risk ratings, loss event history, and regulatory interaction records. It applies a multi-factor risk ranking model and produces a ranked audit universe with the contributing factors visible per entity. The CAE reviews rankings, applies professional judgment, and constructs the annual plan from the AI-generated base.
- OKR: The CAE constructs the annual audit plan from an AI-generated risk-ranked audit universe that integrates risk register, prior findings, RCSA, and loss event data across all entities.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-generated ranked audit universe used as the base for annual plan construction in ≥1 full annual planning cycle within 18 months of go-live; ≥80% of audit universe entities covered by the ranking model. |
| Acceptance | ≥75% of AI-assigned risk rankings accepted by the CAE without material reordering; ranking model covers all four contributing data sources (risk register, prior findings, RCSA, loss events) for ≥90% of entities. |
| Cycle | Initial audit universe risk ranking produced within 5 business days of data refresh, versus ≥4 weeks of manual assessment under the prior approach. |

### Audit Coverage Gap Analysis

- URN: urn:financial-services:scenario:risk-control/internal-audit/audit-universe-risk-ranking/audit-coverage-gap-analysis
- Lens: Insights
- Complexity: M
- Intent: The AI agent compares the proposed annual audit plan against the risk-ranked universe, identifies coverage gaps where high-risk entities are scheduled infrequently, and delivers a gap analysis to the CAE before the Audit Committee plan approval.
- Problem to solve: The annual audit plan is constructed from the risk-ranked universe subject to available audit days. High-risk entities that fall below the resource threshold in a given year create an assurance gap; identifying these gaps and their cumulative effect across multi-year coverage cycles requires systematic analysis that is typically performed judgmentally.
- Solution: The AI agent reads the current-year audit plan, the risk-ranked universe, and the three-year rolling coverage history. It identifies high-risk entities with gaps in coverage frequency, computes the cumulative risk exposure represented by uncovered entities, and delivers the gap analysis to the CAE for Audit Committee disclosure.
- OKR: The CAE discloses assurance gaps to the Audit Committee from an AI-produced gap analysis that compares the proposed annual audit plan with the risk-ranked universe and the three-year coverage history, before the plan is approved.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's coverage gap analysis is produced for ≥1 annual audit plan approval cycle within 18 months of go-live; 100% of high-risk universe entities assessed against the three-year rolling coverage history. |
| Acceptance | ≥80% of AI-identified coverage gaps confirmed by the CAE as genuine; gap analysis used as the basis of the Audit Committee assurance gap disclosure without material rework. |
| Cycle | Gap analysis delivered within 3 business days of the draft annual plan, versus a judgmental assessment with no defined production timeline under the prior approach. |

### Mid-Year Audit Universe Re-Ranking

- URN: urn:financial-services:scenario:risk-control/internal-audit/audit-universe-risk-ranking/audit-plan-dynamic-reranking
- Lens: Insights
- Complexity: M
- Intent: The AI agent re-ranks the audit universe at mid-year using updated risk register, operational events, and regulatory interaction data, flagging for the CAE's consideration entities whose risk profile has materially changed since the plan was approved.
- Problem to solve: The annual audit plan is set at year-start based on the risk ranking at that date. Material risk developments during the year — a significant operational loss event, a regulatory examination finding, or a major process change — may increase the risk profile of entities not scheduled in the current plan, but the plan is not systematically reassessed mid-year.
- Solution: The AI agent re-reads the risk register, loss event register, and regulatory interaction records at mid-year and re-ranks the audit universe. It flags entities whose risk score has materially increased since plan approval and delivers the re-ranking to the CAE for discretionary plan adjustment or Audit Committee notification.
- OKR: The CAE adjusts the audit plan or notifies the Audit Committee from an AI-produced mid-year re-ranking of the audit universe that flags entities whose risk profile has materially increased since the plan was approved.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's mid-year re-ranking is produced in the first audit year after go-live; risk register, loss event register, and regulatory interaction records re-read for ≥90% of audit universe entities. |
| Acceptance | ≥70% of entities flagged as materially higher risk confirmed by the CAE as warranting consideration; every mid-year re-ranking followed by a documented CAE decision on plan adjustment or Audit Committee notification. |
| Cycle | Mid-year re-ranking delivered within 5 business days of the data refresh, versus no systematic reassessment of the plan between annual planning cycles. |

## Findings & thematic synthesis {#findings-thematic-synthesis}

Finding synthesis identifies the common root causes, recurring themes, and systemic patterns that run across individual audit findings — enabling the Audit Committee to direct remediation at root causes rather than individual findings. IIA Standards expect the CAE to provide thematic analysis, not merely per-engagement summaries; supervisors assess whether the audit function is providing value-adding assurance or mechanical finding-by-finding documentation. Cross-audit correlation — connecting audit findings with operational risk events, regulatory observations, and customer complaints sharing the same root cause — enhances the depth of assurance provided.

### Audit Findings Thematic Synthesis

- URN: urn:financial-services:scenario:risk-control/internal-audit/findings-thematic-synthesis/audit-findings-synthesis
- Lens: Insights
- Complexity: M
- Intent: The AI agent clusters findings across all engagements in the year, identifies repeat findings and systemic root causes, and generates the Audit Committee thematic synthesis pack.
- Problem to solve: The Audit Committee receives per-engagement summaries without a synthesized thematic picture. Cross-audit patterns — a common root cause across separate engagements, or a repeat finding from the prior year — surface only at the annual review.
- Solution: The AI agent reads all completed audit finding records, clusters by theme and root cause, identifies repeats against prior-year records, and generates the Audit Committee thematic synthesis. It flags clusters where systemic remediation is warranted; the CAE reviews before Audit Committee submission.
- OKR: The Audit Committee receives a thematic synthesis of all engagement findings — with repeat patterns and systemic root causes identified — rather than per-engagement summaries in isolation.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent is used to produce the Audit Committee thematic synthesis pack for ≥4 quarterly committee cycles in year 1, covering 100% of completed engagements within each cycle. |
| Acceptance | ≥80% of thematic clusters rated as decision-relevant by Audit Committee members; CAE accepts ≥85% of AI-generated synthesis packs without material structural revision. |
| Cycle | Synthesis pack preparation time reduced from ≥5 analyst-days of manual cross-engagement review to ≤1 day of CAE editorial review per cycle. |

### Repeat Finding Root Cause Drill-Down

- URN: urn:financial-services:scenario:risk-control/internal-audit/findings-thematic-synthesis/repeat-finding-root-cause-drill
- Lens: Enablement
- Complexity: M
- Intent: The AI agent identifies repeat findings across the rolling three-year audit history, drills into root cause patterns, and produces a structured repeat-finding analysis for the CAE to present to the Audit Committee as evidence of systemic control weakness.
- Problem to solve: IIA Standards require the CAE to identify and report on repeat findings. The identification of repeats across three years of audit records — matching findings by root cause rather than by entity or audit title — is performed manually in the annual thematic review and is constrained by the analyst's recall of prior engagements.
- Solution: The AI agent reads the three-year finding archive, applies semantic matching to identify findings with the same root cause across different engagements and entities, and produces the repeat-finding analysis with the finding chain per root cause. The CAE uses the output for the Audit Committee's systemic weakness discussion.
- OKR: The CAE presents the Audit Committee with an AI-produced repeat-finding analysis — findings matched by root cause across the rolling three-year audit history, with the finding chain per root cause — as evidence for the systemic control weakness discussion.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's repeat-finding analysis is produced for ≥1 annual thematic review within 18 months of go-live; 100% of findings in the three-year archive included in the semantic matching. |
| Acceptance | ≥80% of AI-identified repeat-finding chains confirmed by the CAE as sharing the same root cause; analysis presented to the Audit Committee without material rework. |
| Cycle | Repeat-finding analysis produced within 3 business days of the finding archive data cut, versus manual identification in the annual thematic review constrained by analyst recall of prior engagements. |

### Cross-Audit Risk Correlation Analysis

- URN: urn:financial-services:scenario:risk-control/internal-audit/findings-thematic-synthesis/cross-audit-risk-correlation
- Lens: Insights
- Complexity: M
- Intent: The AI agent cross-references audit findings with operational risk events and regulatory observations to identify shared root causes, providing the Audit Committee with an integrated cross-source view of systemic control weaknesses.
- Problem to solve: Audit findings, operational risk events, and regulatory observations are managed in separate functions. Root causes shared across all three sources — a common process failure that generates audit findings, operational losses, and regulatory observations simultaneously — are identified in the annual thematic review rather than on a rolling basis.
- Solution: The AI agent reads the audit finding register, operational risk event database, and regulatory observation tracker. It applies root-cause matching across all three populations, identifies shared root causes, and quantifies the combined finding, event, and observation count per root cause. The CAE confirms the shared root causes before the Audit Committee receives the integrated cross-source view in the quarterly synthesis pack.
- OKR: The Audit Committee receives, in each quarterly synthesis pack, an AI-produced integrated view of root causes shared across audit findings, operational risk events, and regulatory observations, with the combined count per root cause.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's root-cause correlation is included in ≥4 consecutive quarterly synthesis packs within 18 months of go-live; audit finding register, operational risk event database, and regulatory observation tracker all read in every run. |
| Acceptance | ≥75% of AI-identified shared root causes confirmed as valid by the CAE before submission; ≥1 systemic remediation action per year initiated from a shared root cause. |
| Cycle | Shared root causes identified within 5 business days of each quarterly data cut, versus identification only in the annual thematic review under the prior approach. |

## Audit execution & workpapers {#audit-execution-workpapers}

Audit execution covers the fieldwork phase of each engagement — planning the audit approach, executing test procedures, documenting evidence in workpapers, and drafting findings. IIA Standards require workpapers that document objectives, procedures, evidence, and conclusions for each test; the workpaper set is the primary quality-control artifact reviewed in internal quality assurance, external quality assessments, and supervisory examinations. For a program of 30–50 audits a year, execution documentation consumes the majority of the audit team's calendar. Pre-populating workpaper templates with prior-period content, system-generated control test data, and structured finding templates reduces per-engagement time without reducing assurance quality.

### Audit Finding Drafting Support

- URN: urn:financial-services:scenario:risk-control/internal-audit/audit-execution-workpapers/audit-finding-drafting-support
- Lens: Enablement
- Complexity: S
- Intent: The AI agent drafts audit findings in the IIA-compliant condition/criteria/cause/effect/recommendation structure from the auditor's fieldwork notes, reducing per-finding drafting time and improving consistency across the team.
- Problem to solve: Audit finding quality varies by auditor experience. Senior auditors spend material time editing junior drafts to meet IIA Standards and the Bank's quality requirements — a review bottleneck that extends the time from testing completion to report issuance.
- Solution: The AI agent reads the auditor's fieldwork notes and test evidence for each finding. It drafts the finding in the Bank's standard IIA-compliant format — condition, criteria, cause, effect, risk rating, and recommended management action — for the senior auditor to review, refine, and approve.
- OKR: Senior auditors review, refine, and approve audit findings drafted by the AI agent from fieldwork notes and test evidence in the Bank's standard format — condition, criteria, cause, effect, risk rating, and recommended management action — rather than editing junior drafts up to standard.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent is used to draft ≥80% of audit findings within 12 months of go-live; all six elements of the standard finding format populated in every draft. |
| Acceptance | ≥75% of AI-drafted findings approved by the senior auditor with only minor amendment; findings returned for structural non-compliance with the standard format reduced by ≥50% year-on-year. |
| Cycle | Finding draft available within 1 business day of fieldwork note submission, shortening the time from testing completion to report issuance. |

### Workpaper Quality Review Check

- URN: urn:financial-services:scenario:risk-control/internal-audit/audit-execution-workpapers/workpaper-quality-review
- Lens: Automation
- Complexity: S
- Intent: The AI agent reviews completed workpapers against the IIA Standards quality checklist before QA supervisor review, flagging documentation gaps and consistency issues for the auditor to resolve.
- Problem to solve: QA supervisor review identifies workpaper deficiencies after the auditor considers the file complete, creating rework cycles that delay report issuance. Common deficiencies — unsigned objectives, unticked test steps, missing evidence cross-references — could be caught by systematic checklist review before QA submission.
- Solution: The AI agent reads completed workpaper files and applies the IIA Standards and bank-policy quality checklist — objectives documented, procedures signed off, evidence cross-referenced, findings rated per the risk scale. It returns a flagged deficiency list to the auditor before QA submission, reducing the first-pass deficiency rate.
- OKR: Auditors resolve documentation gaps before QA submission using an AI-generated deficiency list that checks each completed workpaper file against the IIA Standards and bank-policy quality checklist.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's quality check runs on ≥90% of completed workpaper files before QA submission within 12 months of go-live; full quality checklist applied in every run. |
| Acceptance | ≥85% of AI-flagged deficiencies confirmed as genuine by the auditor or QA supervisor; first-pass deficiency rate at QA supervisor review reduced by ≥50% versus the pre-go-live baseline. |
| Cycle | Deficiency list returned within 1 business day of workpaper completion, removing the rework cycle that followed QA supervisor review and delayed report issuance. |

### Audit Workpaper Pre-Population

- URN: urn:financial-services:scenario:risk-control/internal-audit/audit-execution-workpapers/workpaper-pre-population
- Lens: Automation
- Complexity: M
- Intent: The AI agent pre-populates audit workpaper templates with prior-period test results, system-generated control test data, and relevant policy extracts ahead of each engagement, reducing per-engagement preparation time.
- Problem to solve: Each audit engagement requires the senior auditor to prepare workpaper templates before fieldwork begins — incorporating prior-period findings, control test criteria from the policy library, and relevant system data. For an annual program of 30–50 engagements, this preparation consumes audit team hours before testing begins.
- Solution: The AI agent reads the prior-period workpaper set, current control inventory, policy library, and system data feeds relevant to each engagement scope. It pre-populates the workpaper template with prior test results, control objectives, and available system-generated evidence, leaving the auditor to execute tests and document professional judgment sections.
- OKR: Auditors begin each engagement with workpaper templates pre-populated by the AI agent — prior test results, control objectives, policy extracts, and available system-generated evidence — and spend fieldwork time on executing tests and documenting professional judgment.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent is used to pre-populate workpaper templates for ≥80% of engagements in the annual audit program within 12 months of go-live; prior-period results, control objectives, and policy extracts populated in every template. |
| Acceptance | ≥80% of pre-populated workpapers accepted by the senior auditor as a usable starting point without material correction; accuracy of pre-populated content confirmed at ≥95% on QA review. |
| Cycle | Pre-populated workpaper set delivered ≥5 business days before fieldwork begins, versus manual template preparation by the senior auditor ahead of each engagement. |

## Remediation tracking {#remediation-tracking}

Remediation tracking monitors the progress of management actions against each open finding — covering audit findings, regulatory matters, and internal control gaps — from commitment through to evidence-based closure. Under IIA Standards, the audit function is responsible for following up on open findings to ensure management actions are completed on schedule; lapsed remediation without escalation is a quality finding in itself. The Audit Committee receives a remediation status pack each cycle; supervisors expect evidence that the audit function actively monitors remediation rather than passively recording it. With typically 150–200 open items at any time, manual tracking at item level consumes significant audit team capacity.

### Remediation Evidence Quality Check

- URN: urn:financial-services:scenario:risk-control/internal-audit/remediation-tracking/remediation-evidence-quality-check
- Lens: Automation
- Complexity: S
- Intent: The AI agent reviews management-submitted remediation evidence against the original finding's action description, flags submissions that do not address the finding, and returns a quality assessment to the audit manager before closure is approved.
- Problem to solve: Remediation closure requires the audit manager to review management-submitted evidence against the original finding. Evidence submissions that are incomplete or address a symptom rather than the root cause identified in the finding are identified in the closure review, creating a back-and-forth cycle that delays closure and consumes audit team capacity.
- Solution: The AI agent reads the original finding text, the agreed management action, and the submitted evidence. It assesses whether the evidence demonstrates the specific action committed to, flags gaps or misalignments, and returns a quality assessment to the audit manager before closure is formally approved.
- OKR: The audit manager approves remediation closure with an AI-produced quality assessment showing whether the submitted evidence demonstrates the agreed management action, with gaps and misalignments flagged.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's evidence assessment runs on ≥90% of remediation evidence submissions within 12 months of go-live; original finding text and agreed management action read in every assessment. |
| Acceptance | ≥80% of the AI agent's quality assessments confirmed by the audit manager's closure decision; submissions returned to management more than once before closure reduced by ≥40% year-on-year. |
| Cycle | Quality assessment returned to the audit manager within 1 business day of evidence submission, shortening the back-and-forth cycle that delays closure. |

### Remediation Tracking & Status Reporting

- URN: urn:financial-services:scenario:risk-control/internal-audit/remediation-tracking/remediation-tracking-status-reporting
- Lens: Automation
- Complexity: M
- Intent: The AI agent aggregates remediation status across all open findings, applies pattern detection to identify at-risk items and capacity stress, and generates the Audit Committee status pack.
- Problem to solve: Tracking 150–200 open remediation items across audit findings, regulatory matters, and control gaps — with status self-reported by owners — consumes substantial analyst hours per Audit Committee cycle in manual aggregation. At-risk items surface when owners report delay, typically close to the deadline.
- Solution: The AI agent reads remediation records from audit management systems, regulatory matter trackers, and control registers. It aggregates status, applies delay-pattern detection to identify structurally at-risk items, and generates the Audit Committee pack with capacity analysis and escalation recommendations. The CAE reviews and adds judgment before distribution.
- OKR: The CAE reviews and distributes an AI-generated Audit Committee status pack — aggregating 150–200 open remediation items with delay-pattern detection applied and at-risk items escalated — rather than producing the pack through manual status aggregation.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent is used to generate the Audit Committee remediation status pack for ≥4 consecutive committee cycles within 18 months of go-live; delay-pattern detection applied to 100% of open items in every run. |
| Acceptance | ≥80% of AI-generated status packs accepted by the CAE without material structural revision before distribution; at-risk items identified by delay-pattern detection confirmed as genuinely at risk in ≥75% of cases on review. |
| Cycle | Remediation status pack produced within 2 business days of data cut, versus ≥5 analyst-days of manual aggregation under the prior approach. |

### Remediation Systemic Delay Analysis

- URN: urn:financial-services:scenario:risk-control/internal-audit/remediation-tracking/remediation-systemic-delay-analysis
- Lens: Insights
- Complexity: M
- Intent: The AI agent analyzes the remediation history to identify business units, finding categories, and root causes with systematically longer remediation cycles, and delivers the analysis to the CAE for Audit Committee escalation.
- Problem to solve: Individual remediation delays are tracked and escalated per item. Patterns of delay — a specific business unit consistently missing remediation deadlines, or a category of finding that systematically takes longer to remediate than management commits — are visible only in aggregate analysis performed infrequently.
- Solution: The AI agent reads the full remediation history, computes actual vs committed remediation cycle by business unit, finding category, and root cause, and identifies statistically significant delay patterns. The CAE receives the analysis for Audit Committee presentation as part of the program quality section of the annual report.
- OKR: The CAE presents the Audit Committee with an AI-produced analysis of systemic remediation delay — actual versus committed remediation cycle by business unit, finding category, and root cause — in the program quality section of the annual report.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's delay analysis covering 100% of the remediation history is produced for ≥1 annual report cycle within 18 months of go-live; all three dimensions (business unit, finding category, root cause) analyzed in every run. |
| Acceptance | ≥75% of AI-identified delay patterns confirmed as valid by the CAE; ≥1 Audit Committee escalation or management action per year initiated from an identified pattern. |
| Cycle | Delay analysis produced within 5 business days of the remediation data cut, replacing an aggregate analysis performed infrequently under the prior approach. |
