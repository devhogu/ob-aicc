# 

source: html-alt/financial-services/en/risk-control/risk-cycles/index.html


[PAGE TEXT]
Identification & assessment
RCSA cycle (risk & control self-assessment)
Annual RCSA with quarterly refresh — identification and scoring of inherent risks, assessment of control effectiveness, residual risk rating, and issue capture. Aligned to Basel operational risk standards and SR 11-7 model risk governance where models are in scope.
The risk and control self-assessment (RCSA) cycle is the bank's primary mechanism for identifying, assessing, and documenting material risks and the controls that mitigate them across the institution. Under Basel III operational risk standards and the three-lines-of-defence architecture, business lines and functions own the RCSA for their risk domains; the second line Risk function oversees methodology, challenges ratings, and produces the aggregated risk register. Under SR 11-7 (the Federal Reserve and OCC model risk management guidance), model risk is a specific RCSA risk type with its own validation and governance requirements; CIS supervisors maintain equivalent model governance expectations.
The cycle runs annually for a full RCSA refresh, with quarterly updates to reflect new risks identified through operational incidents, regulatory changes, and business strategy updates. NBKR, NBK/ARDFM, and CBR each require evidence of an active RCSA framework as part of operational risk supervisory review; the RCSA register and issue log are primary examination documents.
GenAI can assist the RCSA narrative — drafting risk descriptions, control assessments, and issue summaries from structured inputs — and flag RCSA ratings that are inconsistent with loss event history or benchmark peer assessments.
Analyze
The RCSA risk register and issue log are point-in-time documents updated at cycle boundaries. The CRO lacks a continuous view of residual risk trends — which risks are migrating upward between formal refresh cycles, which action plans are slipping — without manual extraction from the GRC system.
Optimize
RCSA rating calibration across business lines and the second line challenge process are constrained by the time available for manual review. Risks with above-tolerance residual ratings and overdue action plans receive less review time than their materiality warrants when the review burden across the full register is high.
Automate
RCSA risk description drafting, control effectiveness narrative production, issue summary writing, and quarterly refresh commentary are structured narrative tasks performed on a consistent framework for each risk item each cycle. GenAI can draft from structured inputs — risk type, loss event history, control design details — with risk officer review.
Enrich
RCSA ratings across business lines and the incident event database accumulate across annual cycles but are rarely mined for patterns that would improve the next cycle's risk identification step. Recurring themes — the same operational risk type appearing in three business lines, or a control failing repeatedly in the same way — are identified informally rather than through systematic cross-cycle analysis.
<button
class="flow-stages__stage"
type="button"
data-stage="identify"
data-flow-id="urn:financial-services:flow:risk-control/rcsa-cycle"
>
Identify
→
<button
class="flow-stages__stage"
type="button"
data-stage="assess"
data-flow-id="urn:financial-services:flow:risk-control/rcsa-cycle"
>
Assess
→
<button
class="flow-stages__stage"
type="button"
data-stage="score"
data-flow-id="urn:financial-services:flow:risk-control/rcsa-cycle"
>
Score
→
<button
class="flow-stages__stage"
type="button"
data-stage="document"
data-flow-id="urn:financial-services:flow:risk-control/rcsa-cycle"
>
Document
→
<button
class="flow-stages__stage"
type="button"
data-stage="refresh"
data-flow-id="urn:financial-services:flow:risk-control/rcsa-cycle"
>
Refresh
Lens
Scenario
Intent
Complexity

### CARD 1 [Enablement|S] RCSA Risk Identification Facilitation Pack
urn: urn:financial-services:scenario:flow/risk-control/rcsa-cycle/rcsa-risk-identification-facilitation
intent: Agent supports RCSA risk identification workshops by pre-populating the risk taxonomy with operational incidents, audit findings, and regulatory change signals relevant to each business line's scope.
Problem to solve: Risk identification workshops are facilitated manually from a generic taxonomy; risk items from operational incidents and regulatory observations accumulate between cycles without being consistently channelled into the RCSA identify stage.
Solution: Agent reads the loss event database, audit findings register, and regulatory change log and maps each item to the relevant RCSA risk taxonomy category and business line scope. Coordinators receive a pre-populated identification pack for each workshop, reducing facilitation time and improving coverage of emerging risk themes.
OKR objective: RCSA risk identification workshop coordinators use agent-generated pre-populated identification packs — mapping loss events, audit findings, and regulatory change signals to business line scope — as the starting point for each session.
OKR KR [Adoption]: Agent-generated identification packs used for ≥70% of risk identification workshops in the next annual RCSA cycle within 18 months of go-live; all three input sources (loss events, audit findings, regulatory changes) mapped per business line in every pack.
OKR KR [Acceptance]: ≥80% of identification packs rated as useful or better by coordinating risk officers; coverage of emerging risk themes in workshop outputs (assessed against prior-cycle gaps) improved by ≥20% versus workshops run from generic taxonomy alone.
OKR KR [Cycle]: Pre-populated identification pack delivered within 2 business days of business unit scope confirmation, enabling workshop preparation to complete within the same week.

### CARD 2 [Automation|S] RCSA Register Narrative Drafting
urn: urn:financial-services:scenario:flow/risk-control/rcsa-cycle/rcsa-narrative-drafting
intent: Agent drafts RCSA risk descriptions, control effectiveness narratives, and issue summaries from structured inputs — risk type, loss history, control design attributes — for risk officer review and GRC entry.
Problem to solve: RCSA register documentation is a manual data-entry exercise across dozens of risk items each cycle. Documentation quality is inconsistent across business lines, and supervisors have challenged the specificity of risk descriptions during NBKR and NBK/ARDFM operational risk examinations.
Solution: Agent reads structured risk attributes and loss event history for each RCSA item and produces a draft risk description, control effectiveness narrative, and issue summary per the bank's RCSA methodology. Risk officers review, edit, and submit to the GRC system, compressing documentation effort from days to hours.
OKR objective: Risk officers review and submit agent-drafted RCSA risk descriptions, control effectiveness narratives, and issue summaries to the GRC system rather than producing documentation through manual data entry.
OKR KR [Adoption]: Agent used to draft RCSA register documentation for ≥70% of risk items in the next full annual RCSA cycle within 18 months of go-live; all three documentation types (risk description, control effectiveness narrative, issue summary) produced per item from go-live.
OKR KR [Acceptance]: ≥80% of agent-drafted narratives accepted by risk officers with only minor amendment before GRC entry; supervisory examination challenges on RCSA documentation specificity reduced by ≥1 category severity in the next NBKR/NBK/ARDFM review.
OKR KR [Cycle]: Draft documentation for each RCSA item available within 1 business day of structured risk attribute input, compressing documentation effort from days to hours of risk officer review per cycle.

### CARD 3 [Insights|M] RCSA Cross-Cycle Risk Trend Signal
urn: urn:financial-services:scenario:flow/risk-control/rcsa-cycle/rcsa-cross-cycle-risk-trend-signal
intent: Agent mines the RCSA register across annual cycles to surface risk ratings trending upward between refresh periods, action plans approaching overdue status, and recurring operational risk themes across business lines.
Problem to solve: The RCSA register is a point-in-time document updated at cycle boundaries. The CRO has no continuous view of which residual risk ratings are drifting upward or which action plans are slipping without manual extraction from the GRC system.
Solution: Agent reads the structured RCSA register and issue log each quarter, computes rating trajectory per risk item against prior cycles, and produces a trend signal report flagging deteriorating residual ratings and overdue action plan status. The CRO receives a concise watchlist for the quarterly refresh governance agenda.
OKR objective: The CRO manages a quarterly RCSA watchlist of deteriorating residual risk ratings and overdue action plans, generated by agent analysis of RCSA register trajectory across prior cycles.
OKR KR [Adoption]: Agent RCSA cross-cycle analysis run quarterly within 6 months of go-live; trend signal report delivered to the CRO ahead of ≥4 consecutive quarterly refresh governance meetings in year 1.
OKR KR [Acceptance]: ≥75% of agent-flagged deteriorating residual ratings confirmed as warranting watchlist inclusion by the CRO; overdue action plan flags confirmed as accurate in ≥85% of instances on review.
OKR KR [Cycle]: Quarterly trend signal report produced within 3 business days of register data cut, replacing a manual extraction exercise with no defined production timeline between annual RCSA cycle boundaries.

### CARD 4 [Optimize|M] RCSA Rating Calibration Challenge Assist
urn: urn:financial-services:scenario:flow/risk-control/rcsa-cycle/rcsa-rating-calibration-challenge-assist
intent: Agent assists the second-line challenge process by flagging RCSA inherent risk and control effectiveness ratings that are inconsistent with the business line's own loss event history or with benchmark ratings for equivalent risks at peer banks.
Problem to solve: Second-line challenge of RCSA ratings is constrained by the volume of items under review each cycle. High-materiality risks with above-tolerance residuals receive insufficient challenge when the review burden spans the full register without systematic triage.
Solution: Agent reads each RCSA rating against the business line's three-year loss event history and cross-business-line comparables for the same risk taxonomy category, scoring calibration deviation. The second-line team receives a prioritised challenge list focused on outlier ratings and high-residual items, allocating review effort by materiality.
OKR objective: The second-line challenge team allocates review effort to outlier RCSA ratings and high-residual items identified by agent comparison of inherent risk and control effectiveness ratings against loss event history and cross-business-line benchmarks.
OKR KR [Adoption]: Agent calibration challenge analysis covering ≥80% of RCSA items in the next full annual cycle within 18 months of go-live; both loss event history and cross-business-line comparables applied as calibration benchmarks in every run.
OKR KR [Acceptance]: ≥70% of agent-prioritised challenge items confirmed as warranting second-line scrutiny by the reviewing team; challenge capacity redirected to high-materiality, high-residual items as a proportion of total review hours increased by ≥25% versus prior cycle.
OKR KR [Cycle]: Prioritised challenge list delivered within 3 business days of RCSA first-line submission cut-off, enabling structured second-line review to begin before the challenge window compresses.

### CARD 5 [New opps|M] RCSA Pattern Mining — Pre-Cycle Brief
urn: urn:financial-services:scenario:flow/risk-control/rcsa-cycle/rcsa-pattern-mining-next-cycle-brief
intent: Agent analyses accumulated RCSA ratings, issue log entries, and operational loss events across prior cycles to identify systemic patterns — recurring control failures, risk types appearing across business lines, and action plan completion rates by risk category — and produces a pre-cycle brief for the Risk Strategy team.
Problem to solve: RCSA ratings and issue histories accumulate across annual cycles but are rarely mined for systemic patterns. Recurring themes — the same operational risk type appearing across three business lines, or a control failing repeatedly in the same form — are identified informally rather than through structured cross-cycle analysis.
Solution: Agent runs a structured cross-cycle analysis of the RCSA register and issue log, clustering risk items by taxonomy, business line, and control type to surface systemic patterns and recurrent themes. The Risk Strategy team receives a pre-cycle brief that prioritises risk categories for deeper identification attention and calibration review in the upcoming annual cycle.
OKR objective: The Risk Strategy team enters the annual RCSA cycle with an agent-produced pre-cycle brief that identifies systemic patterns — recurring control failures, risk types appearing across business lines, and action plan completion rates — from accumulated cross-cycle RCSA data.
OKR KR [Adoption]: Agent pre-cycle brief produced ahead of ≥1 full annual RCSA cycle within 18 months of go-live; cross-cycle analysis spanning ≥3 prior annual cycles in every run from go-live.
OKR KR [Acceptance]: ≥70% of agent-identified systemic patterns rated as actionable by the Risk Strategy team; ≥1 structural change to risk identification priorities per annual RCSA cycle attributable to agent-surfaced cross-cycle pattern.
OKR KR [Cycle]: Pre-cycle brief delivered ≥4 weeks before the RCSA identification stage begins, enabling the Risk Strategy team to incorporate findings into workshop design rather than identifying patterns after facilitation is complete.

[PAGE TEXT]
Stress testing cycle (ICAAP, ILAAP, climate)
Annual integrated stress testing programme — ICAAP capital stress, ILAAP liquidity stress, and climate scenario analysis — covering base and adverse scenarios across credit, market, liquidity, and climate risk. Aligned to ICAAP/ILAAP supervisory expectations from NBKR/NBK/CBR and TCFD physical and transition scenario frameworks.
The stress testing cycle produces the bank's integrated assessment of resilience under adverse conditions across capital (ICAAP), liquidity (ILAAP), and climate risk (TCFD scenarios). Under NBKR, NBK/ARDFM, and CBR supervisory frameworks, banks must conduct annual stress tests and submit ICAAP/ILAAP equivalent documents demonstrating that the institution holds sufficient capital and liquidity buffers under defined stress conditions. Basel III Pillar 2 requirements and the BCBS supervisory review process underpin the CIS supervisory frameworks.
The climate stress testing element draws on TCFD scenario frameworks (Network for Greening the Financial System — NGFS scenarios) for transition risk and physical risk analysis. ISSB disclosure standards (IFRS S1/S2) are increasingly referenced by CIS supervisors for climate risk governance; the stress testing cycle feeds the bank's climate risk disclosures.
The cycle runs annually with a mid-year ICAAP refresh. Its primary bottleneck is cross-domain scenario aggregation — translating macro stress scenarios into risk-type-specific shocks, running each risk model independently, and aggregating the outputs into a coherent group capital adequacy or survival horizon statement. GenAI can compress the aggregation narrative and assist with scenario design documentation.
Analyze
Stress test results are produced and reviewed at the annual submission cycle. Continuous monitoring of the bank's resilience position — how the ICAAP trough CET1 or ILAAP survival horizon is shifting with the balance sheet between annual submissions — is absent from the standard management information set.
Optimize
Stress scenario design and cross-domain consistency checking are constrained by the serial production process. Exploring a wider scenario set — additional macro pathways, idiosyncratic bank-specific scenarios, TCFD climate variants — requires proportional additional production effort that the current cycle calendar cannot accommodate.
Automate
ICAAP/ILAAP narrative sections — stress scenario descriptions, risk-type-specific adequacy narratives, management action plan documentation, and supervisory query response packs — are structured writing tasks with substantial content reuse across cycles. Climate scenario description following NGFS pathway conventions follows a reproducible structure amenable to agent-assisted drafting.
Enrich
Prior supervisory dialog — questions raised by NBKR/NBK/CBR in prior SREP cycles, findings on methodology, management action plan credibility — represents an institutional knowledge base that rarely feeds systematically into the next cycle's scenario design or narrative framing. Each submission cycle re-learns the same supervisory preferences through fresh dialog.
<button
class="flow-stages__stage"
type="button"
data-stage="define"
data-flow-id="urn:financial-services:flow:risk-control/stress-testing-cycle"
>
Define scenarios
→
<button
class="flow-stages__stage"
type="button"
data-stage="run"
data-flow-id="urn:financial-services:flow:risk-control/stress-testing-cycle"
>
Run models
→
<button
class="flow-stages__stage"
type="button"
data-stage="aggregate"
data-flow-id="urn:financial-services:flow:risk-control/stress-testing-cycle"
>
Aggregate
→
<button
class="flow-stages__stage"
type="button"
data-stage="approve"
data-flow-id="urn:financial-services:flow:risk-control/stress-testing-cycle"
>
Approve
→
<button
class="flow-stages__stage"
type="button"
data-stage="submit"
data-flow-id="urn:financial-services:flow:risk-control/stress-testing-cycle"
>
Submit
Lens
Scenario
Intent
Complexity

### CARD 6 [Enablement|S] Stress Scenario Design Documentation Support
urn: urn:financial-services:scenario:flow/risk-control/stress-testing-cycle/stress-scenario-design-documentation-support
intent: Agent assists the Risk Strategy team in documenting macro stress scenarios to the standard required for ICAAP/ILAAP supervisory submission — narrative framing, NGFS pathway alignment for TCFD climate scenarios, and cross-risk-type shock consistency checks.
Problem to solve: Scenario design documentation requires translating calibrated macro assumptions into consistent cross-domain shocks at the standard NBKR/ NBK/CBR supervisors will scrutinise. Scenario assumptions coherent at the macro level are frequently inconsistent when translated into risk-type- specific shock inputs for credit, market, liquidity, and IRRBB models.
Solution: Agent reads the macro scenario parameter set and cross-references shock magnitudes against historical precedent, NGFS pathway benchmarks for climate scenarios, and internal model input ranges across domains. It flags cross-domain inconsistencies and produces a structured scenario documentation template populated with calibrated assumptions, leaving the Risk Strategy team to apply final professional judgment on scenario severity and narrative framing.
OKR objective: The Risk Strategy team applies final judgement on scenario severity and narrative framing to an agent-produced scenario documentation template — with macro assumptions calibrated, NGFS pathway alignment confirmed, and cross-domain shock inconsistencies flagged — structured to supervisory submission standards.
OKR KR [Adoption]: Agent used to produce scenario documentation templates for ≥80% of ICAAP/ILAAP stress scenarios within 18 months of go-live; cross-domain consistency checks applied across credit, market, liquidity, and IRRBB shock inputs in every run.
OKR KR [Acceptance]: ≥75% of agent-produced scenario documentation templates accepted by the Risk Strategy team without structural revision; cross-domain shock inconsistencies flagged by the agent reduced to ≤2 unresolved items per submission cycle.
OKR KR [Cycle]: Scenario documentation template delivered within 3 business days of macro parameter set receipt, versus ≥2 weeks of manual documentation under the prior approach.

### CARD 7 [Automation|S] ICAAP/ILAAP Narrative Section Drafting
urn: urn:financial-services:scenario:flow/risk-control/stress-testing-cycle/icaap-ilaap-narrative-section-drafting
intent: Agent drafts the narrative sections of the ICAAP/ILAAP document — stress scenario descriptions, risk-type adequacy narratives, and management action plan documentation — from structured model outputs and approved scenario parameters, for CRO and board review.
Problem to solve: ICAAP/ILAAP narrative drafting is performed manually under the board presentation deadline, consuming senior Capital and Risk team resource on a repeating structure. Narrative quality — the coherence of the management action plan and the plausibility of the trough-recovery trajectory — has been the primary focus of NBKR and NBK/ARDFM supervisory feedback on prior submissions.
Solution: Agent reads approved stress scenario parameters, model outputs by risk type, and management action plan commitments and produces draft ICAAP/ ILAAP narrative sections per the supervisory submission framework. Each section covers scenario rationale, stress impact by risk type, trough capital or liquidity position, and the management action plan response. The CRO reviews and applies judgment on the adequacy assessment conclusion before board submission.
OKR objective: The CRO reviews and applies judgement to agent-drafted ICAAP/ILAAP narrative sections — covering scenario rationale, stress impact, trough position, and management action plan — structured to the supervisory submission framework.
OKR KR [Adoption]: Agent used to draft narrative sections for ≥1 ICAAP and ≥1 ILAAP submission cycle within 18 months of go-live; all prescribed section types (scenario rationale, stress impact by risk type, trough, management actions) produced by the agent from go-live.
OKR KR [Acceptance]: ≥80% of agent-drafted sections accepted by the CRO without structural revision; supervisory feedback items attributed to narrative quality or section completeness reduced by ≥40% versus prior submission.
OKR KR [Cycle]: Narrative section drafts delivered within 3 business days of approved stress parameter and model output receipt, compressing the drafting phase from ≥2 weeks of manual effort.

### CARD 8 [Insights|M] Continuous Capital Resilience Monitoring
urn: urn:financial-services:scenario:flow/risk-control/stress-testing-cycle/continuous-capital-resilience-monitoring
intent: Agent tracks the bank's inferred ICAAP trough CET1 and ILAAP survival horizon between annual submissions by applying approved stress parameters to the current balance sheet, producing a continuous-form resilience indicator for the CRO and Capital Committee.
Problem to solve: Stress test results are reviewed at the annual ICAAP/ILAAP submission cycle. Continuous monitoring of the bank's resilience position — how the trough CET1 or ILAAP survival horizon is shifting with the balance sheet between formal submissions — is absent from the standard management information set.
Solution: Agent applies the prior year's approved adverse scenario shocks to the current month-end balance sheet and risk position, computing an indicative trough CET1 and survival horizon on a monthly basis. The Capital Committee receives a continuous-form resilience indicator that flags material deterioration in the inferred stress position warranting an off-cycle review.
OKR objective: The CRO and Capital Committee monitor a continuous-form ICAAP resilience indicator — reflecting the current balance sheet's inferred trough CET1 and ILAAP survival horizon — on a monthly basis between annual submissions.
OKR KR [Adoption]: Agent-computed monthly resilience indicator delivered to the Capital Committee for ≥10 consecutive months in year 1; covers both trough CET1 (ICAAP) and survival horizon (ILAAP) dimensions from go-live.
OKR KR [Acceptance]: ≥80% of monthly resilience indicators accepted by the CRO without recalculation; methodology consistency with approved annual ICAAP stress parameters confirmed by the Capital team in ≥90% of monthly runs.
OKR KR [Cycle]: Monthly resilience indicator produced within 3 business days of month-end balance sheet close, replacing a posture visible only at the annual ICAAP/ILAAP submission.

### CARD 9 [Optimize|M] Parallel Stress Scenario Set Expansion
urn: urn:financial-services:scenario:flow/risk-control/stress-testing-cycle/parallel-scenario-set-expansion
intent: Agent extends the stress testing programme beyond the minimum ICAAP/ILAAP scenario set by generating additional scenario variants — alternative macro pathways, bank-specific idiosyncratic scenarios, TCFD transition and physical risk combinations — within the approved scenario calibration methodology.
Problem to solve: Exploring a wider stress scenario set beyond the minimum regulatory submission requirement requires proportional additional production effort that the current serial cycle calendar cannot accommodate. Scenario coverage is constrained by production capacity rather than by scenario risk materiality.
Solution: Agent applies the approved scenario calibration methodology to additional scenario seeds — alternative macro trajectories, sector-specific shocks, TCFD pathway variants — producing parameterised scenario specifications ready for model execution. The Risk Strategy team reviews scenario plausibility, selects the extended set for parallel model runs, and integrates selective results into the ICAAP/ILAAP narrative to demonstrate scenario coverage breadth to supervisors.
OKR objective: The Risk Strategy team runs a wider stress scenario set — including TCFD transition and physical risk combinations and idiosyncratic scenarios — within the existing production cycle calendar, using agent-generated parameterised specifications ready for model execution.
OKR KR [Adoption]: Agent-generated additional scenario specifications produced for ≥4 scenario variants beyond the minimum ICAAP/ILAAP required set within 12 months of go-live; approved calibration methodology applied to all agent-generated variants from go-live.
OKR KR [Acceptance]: ≥70% of agent-generated scenario specifications accepted by the Risk Strategy team as plausible and within approved methodology bounds without material recalibration; ≥2 extended scenario results integrated into ICAAP/ILAAP narrative per submission cycle.
OKR KR [Cycle]: Parameterised scenario specification delivered within 3 business days of scenario seed input, versus ≥2 weeks of manual calibration effort per additional scenario under the prior serial approach.

### CARD 10 [New opps|M] Supervisory Dialogue Knowledge Base
urn: urn:financial-services:scenario:flow/risk-control/stress-testing-cycle/supervisory-dialogue-knowledge-base
intent: Agent structures accumulated supervisory dialogue from prior SREP cycles — ICAAP/ILAAP findings, methodology questions, and management action plan credibility challenges — into a searchable knowledge base that feeds into the next cycle's scenario design and narrative framing.
Problem to solve: Prior NBKR/NBK/CBR supervisory dialogue represents institutional knowledge that rarely feeds systematically into the next cycle. Each submission re-learns supervisory preferences through fresh dialogue rather than building on prior SREP experience.
Solution: Agent reads prior SREP correspondence, information request logs, and supervisory meeting records and structures them into a thematic findings database classified by submission section, risk domain, and finding type. The Risk Strategy team queries the database at scenario design and narrative drafting stages to anticipate supervisory focus areas, and the Capital team uses it to pre-empt information requests in the submission pack.
OKR objective: The Risk Strategy and Capital teams query an agent-structured thematic findings database — classified by submission section, risk domain, and finding type from prior SREP cycles — at scenario design and narrative drafting stages to anticipate supervisory focus areas.
OKR KR [Adoption]: Agent-structured supervisory dialogue knowledge base incorporating ≥3 prior SREP cycles deployed within 12 months of go-live; database actively queried by the Risk Strategy and Capital teams ahead of ≥1 full submission cycle per year.
OKR KR [Acceptance]: ≥70% of database-retrieved prior supervisory focus areas rated as relevant to the current submission cycle by the Risk Strategy team; information request pre-emption rate in supervisory submission improved by ≥20% versus prior cycle.
OKR KR [Cycle]: Knowledge base updated within 10 business days of each SREP interaction record becoming available, maintaining a current institutional record rather than accumulating unstructured correspondence.

[PAGE TEXT]
Governance & oversight
Limits & breach governance cycle
Continuous risk limit monitoring with a structured breach governance cycle — breach detection, root-cause investigation, escalation, and resolution — across financial and non-financial risk types. The cycle anchor is the time from breach detection to documented resolution or approved limit action.
The limits and breach governance cycle operates across all material risk types — credit concentration limits, market risk VaR and sensitivity limits, IRRBB NII-at-risk and EVE limits, liquidity LCR and NSFR floors, operational risk event thresholds, and model performance limits. Under Basel III Pillar 2 and the NBKR/NBK/CBR supervisory frameworks, the bank must maintain an approved risk appetite with quantified limits, demonstrate continuous monitoring, and evidence a structured escalation process for limit approaches and breaches.
The cycle runs continuously for limit monitoring and on a structured cadence — weekly for market and liquidity limits, monthly for credit and operational limits — for formal breach review. Breach governance is not solely a compliance function; the resolution outcome (limit reset, risk reduction, or management action) directly affects the bank's capital deployment and earnings capacity.
GenAI can support the cycle by flagging limit approach patterns before formal breach, drafting breach investigation narratives, and producing the committee-ready breach resolution summary.
Analyze
Limit utilisation across risk types is monitored within each domain but not in a consolidated cross-domain view. The CRO cannot see the full limit utilisation picture — which risk types are at high utilisation simultaneously, where concentration of near-limit positions creates systemic risk — without manual assembly from multiple risk reporting systems.
Optimize
Soft-breach threshold calibration and the timing of escalation relative to hard breach events are set by static rules rather than by dynamic position trajectory analysis. The escalation design does not distinguish between slow drift toward a limit and rapid directional moves, both of which have different intervention needs.
Automate
Breach investigation narrative drafting, limit utilisation report commentary, and breach resolution documentation are structured writing tasks that repeat for each breach on a consistent framework. The factual content — position history, driver attribution, approver chain — is drawn from risk reporting systems and approval records that an agent can traverse systematically.
Enrich
Breach histories across risk types — root causes, resolution outcomes, time-to-resolution — are held in individual breach files rather than in a structured repository. Pattern analysis across breach histories that could improve limit calibration and early-warning design is not routinely applied between formal limit review cycles.
<button
class="flow-stages__stage"
type="button"
data-stage="set"
data-flow-id="urn:financial-services:flow:risk-control/limits-breach-governance-cycle"
>
Set limits
→
<button
class="flow-stages__stage"
type="button"
data-stage="monitor"
data-flow-id="urn:financial-services:flow:risk-control/limits-breach-governance-cycle"
>
Monitor
→
<button
class="flow-stages__stage"
type="button"
data-stage="detect"
data-flow-id="urn:financial-services:flow:risk-control/limits-breach-governance-cycle"
>
Detect breaches
→
<button
class="flow-stages__stage"
type="button"
data-stage="investigate"
data-flow-id="urn:financial-services:flow:risk-control/limits-breach-governance-cycle"
>
Investigate
→
<button
class="flow-stages__stage"
type="button"
data-stage="resolve"
data-flow-id="urn:financial-services:flow:risk-control/limits-breach-governance-cycle"
>
Resolve
Lens
Scenario
Intent
Complexity

### CARD 11 [Enablement|S] Limit Governance Framework Calibration Support
urn: urn:financial-services:scenario:flow/risk-control/limits-breach-governance-cycle/limit-governance-framework-calibration-support
intent: Agent supports the annual limit calibration exercise by modelling graduated escalation structures — floor, warning, and hard limit tiers per risk type — and flagging where the current limit structure collapses tiers into a single board-level threshold.
Problem to solve: Inconsistent limit structures — where the board-level limit equals the business-line limit with no graduated escalation — are a recurring NBKR and NBK/ARDFM risk governance examination finding. Calibrating a coherent multi-tier structure across all material risk types requires consistent methodology the Risk Strategy team applies manually each year.
Solution: Agent reads the approved risk appetite framework and current limit register, identifies risk types where the limit structure lacks graduated escalation, and produces a draft calibration proposal with three-tier structures anchored to the bank's capital and liquidity constraints. The Risk Strategy team reviews proposals and submits the revised limit schedule for board approval.
OKR objective: The Risk Strategy team submits a revised multi-tier limit schedule for board approval, based on agent-modelled three-tier escalation structures calibrated to the bank's capital and liquidity constraints across all material risk types.
OKR KR [Adoption]: Agent-modelled calibration proposals covering ≥90% of material risk types delivered to the Risk Strategy team ahead of the next annual limit review cycle; all risk types lacking graduated escalation flagged with a draft three-tier structure from go-live.
OKR KR [Acceptance]: ≥75% of agent-generated calibration proposals accepted by the Risk Strategy team without material structural revision; NBKR/NBK/ARDFM examination findings on graduated escalation structure reduced by ≥1 category severity in the next review cycle.
OKR KR [Cycle]: Limit calibration proposals delivered within 5 business days of risk appetite framework data cut, enabling review and board submission within the annual RAF update window.

### CARD 12 [Automation|S] Breach Investigation Narrative Drafting
urn: urn:financial-services:scenario:flow/risk-control/limits-breach-governance-cycle/breach-investigation-narrative-drafting
intent: Agent drafts the breach investigation narrative — position history, root-cause attribution, approver chain, and resolution recommendation — for confirmed limit breaches, structured per the bank's breach governance framework.
Problem to solve: Breach investigation narrative drafting requires the risk team to assemble position history, driver attribution, and governance documentation from multiple risk systems under time pressure. Investigation quality and speed vary with the technical depth of the investigating risk officer, and documentation quality must withstand supervisory scrutiny.
Solution: Agent reads position time series, risk attribution outputs, and approval records for a confirmed breach and produces a structured investigation narrative covering root-cause classification (market move, business action, model recalibration, or limit inadequacy), approver chain, and recommended resolution. The risk officer reviews the draft, applies professional judgment on resolution recommendation, and submits to the breach resolution committee.
OKR objective: The risk team submits breach investigation narratives drafted from agent-assembled position history, root-cause attribution, and governance documentation within the breach governance framework's required window.
OKR KR [Adoption]: Agent used to draft breach investigation narratives for ≥90% of confirmed limit breaches within 12 months of go-live.
OKR KR [Acceptance]: ≥80% of agent-drafted narratives accepted by the risk officer with only minor amendment before submission to the breach resolution committee; supervisory challenge rate on investigation quality reduced by ≥30% year-on-year.
OKR KR [Cycle]: Breach investigation narrative draft available within 2 hours of breach confirmation, versus ≥1 business day under the prior manual approach.

### CARD 13 [Insights|M] Cross-Domain Limit Utilisation Dashboard
urn: urn:financial-services:scenario:flow/risk-control/limits-breach-governance-cycle/cross-domain-limit-utilisation-dashboard
intent: Agent assembles a consolidated cross-domain limit utilisation view — credit concentration, VaR and sensitivity, LCR/NSFR floors, IRRBB NII-at-risk, and operational KRI thresholds — in a single CRO-facing dashboard updated at each domain's monitoring cadence.
Problem to solve: Limit monitoring systems across risk domains operate independently with separate dashboards. The CRO cannot assess the full limit utilisation picture — which risk types are simultaneously at high utilisation, where cross-domain concentrations create systemic risk — without manual assembly from multiple reporting systems.
Solution: Agent reads utilisation outputs from each domain's monitoring system and assembles a cross-domain limit utilisation summary ranked by distance-to-limit, flagging domains approaching 80% of hard limits and any cross-domain correlations where simultaneous high utilisation across credit and market risk warrants a consolidated escalation. The CRO receives the consolidated view at each weekly risk management information run.
OKR objective: The CRO has a consolidated cross-domain limit utilisation view — ranked by distance-to-limit across credit, market, liquidity, IRRBB, and operational KRI thresholds — updated at each domain's monitoring cadence.
OKR KR [Adoption]: Agent-assembled consolidated dashboard in live production for ≥40 weekly management information runs within 12 months of go-live; all five limit domains (credit, VaR/sensitivity, LCR/NSFR, IRRBB NII-at-risk, operational KRI) covered from go-live.
OKR KR [Acceptance]: ≥85% of weekly consolidated dashboards accepted by the CRO as complete and accurate without manual supplementation; cross-domain correlation flags rated as actionable by the CRO in ≥65% of instances.
OKR KR [Cycle]: Consolidated dashboard available within 4 hours of the last domain's monitoring data publication, versus same-day manual assembly that could not be reliably completed before the CRO's weekly review.

### CARD 14 [Optimize|M] Dynamic Soft-Breach Threshold Calibration
urn: urn:financial-services:scenario:flow/risk-control/limits-breach-governance-cycle/dynamic-soft-breach-threshold-calibration
intent: Agent analyses position velocity and directional trajectory for each limit-monitored risk type, calibrating dynamic soft-breach warning thresholds that distinguish slow drift from rapid directional moves requiring earlier escalation.
Problem to solve: Soft-breach warning thresholds are set as a static percentage of the hard limit and do not distinguish between slow position drift and rapid directional moves. The first formal breach notification can be the hard breach rather than an early warning in fast-moving market conditions.
Solution: Agent monitors rolling position velocity for each limit-monitored risk type and recalibrates warning trigger points based on observed directional rate-of-change. Positions with high velocity receive an earlier warning signal relative to distance-to-limit than slow-moving positions, ensuring the escalation chain has time to intervene before a hard breach.
OKR objective: The risk management escalation chain receives earlier warning signals for fast-moving positions through agent-calibrated dynamic soft-breach thresholds that distinguish position velocity from slow drift.
OKR KR [Adoption]: Dynamic threshold calibration applied to ≥90% of limit-monitored risk types within 12 months of go-live; threshold recalibration running on at least a weekly cadence per risk type from go-live.
OKR KR [Acceptance]: ≥75% of dynamic soft-breach alerts rated as providing materially earlier warning than the prior static threshold by the risk officer reviewing the escalation; false-positive rate on dynamic alerts ≤15% as measured over rolling 90-day windows.
OKR KR [Cycle]: Threshold recalibration completed within 24 hours of each monitoring cycle, ensuring dynamic warnings reflect current position velocity rather than a trailing static threshold.

### CARD 15 [New opps|M] Breach Pattern — Limit Recalibration Brief
urn: urn:financial-services:scenario:flow/risk-control/limits-breach-governance-cycle/breach-pattern-limit-recalibration-brief
intent: Agent mines the breach history database across risk types to identify patterns — recurring root causes, resolution time by type, limits that breach repeatedly — and produces a limit recalibration recommendation brief for the annual risk appetite review.
Problem to solve: Breach histories across risk types are held in individual breach files rather than a structured repository. Pattern analysis that could improve limit calibration and early-warning design is not routinely applied between formal limit review cycles, meaning structurally misaligned limits recur as annual breach events.
Solution: Agent structures the breach history database by risk type, root cause, resolution outcome, and time-to-resolution, clustering recurring breach patterns that indicate limits set too tightly relative to normal business operations versus genuine risk appetite exceedance. The annual risk appetite review team receives a prioritised recalibration brief with proposed limit and threshold adjustments supported by breach frequency and resolution data.
OKR objective: The annual risk appetite review team receives an agent-produced limit recalibration brief that identifies structurally misaligned limits and recurring breach patterns across all risk types.
OKR KR [Adoption]: Agent-produced breach pattern and recalibration brief incorporated into the annual risk appetite review for ≥1 full cycle within 18 months of go-live; breach history database covering ≥3 years of records structured for analysis.
OKR KR [Acceptance]: ≥70% of recalibration candidates flagged by the agent accepted by risk discipline owners as warranting review; ≥1 material limit adjustment per annual RAF update attributable to agent-identified recurring breach pattern.
OKR KR [Cycle]: Breach pattern analysis and recalibration brief produced within 5 business days of data cut, replacing a manual exercise that was not routinely performed between formal review cycles.

[PAGE TEXT]
Risk reporting cycle (ERMC & board)
Monthly and quarterly risk reporting to the executive risk management committee and board — integrated risk picture, limit utilisation, emerging risks, and regulatory developments. The cycle anchor is the time from risk position data to a committee-ready risk pack.
The risk reporting cycle produces the bank's periodic risk management reports for the executive risk management committee (ERMC), the board risk committee (BRC), and the full board — the primary governance forums by which the institution's leadership monitors risk posture and holds the CRO accountable. Under NBKR, NBK/ARDFM, and CBR supervisory frameworks, the bank must demonstrate that board-level risk oversight is substantive and informed; the quality of risk reporting packs is assessed directly in supervisory governance examinations.
The cycle runs monthly for ERMC and quarterly for the board risk committee, with an annual integrated risk report to the full board. Each reporting event requires the Risk function to synthesise positions, limit utilisation, emerging risks, regulatory developments, and forward-looking risk indicators across all material risk domains into a single coherent management document.
GenAI can accelerate the aggregation and narrative drafting stages — assembling the cross-domain risk picture from standard inputs and producing committee-ready commentary — freeing the CRO and risk officers for the analytical and governance work that boards are convened to perform.
Analyze
The committee risk pack is produced at monthly and quarterly intervals. The CRO lacks a continuous-form view of the institution's aggregate risk posture between formal reporting cycles — which domains are in motion, which are stable — without triggering an ad hoc report assembly.
Optimize
Cross-domain risk coherence checking and the calibration of the pack's executive summary to committee members' analytical priorities are performed by the Risk Reporting team manually each cycle without a systematic framework for allocating editorial attention to the most material and actionable risk developments.
Automate
Risk pack narrative drafting — executive summary, domain commentaries, emerging risk sections, regulatory developments summary — follows a consistent structure each cycle with only the current-period risk content varying. GenAI can draft from structured risk data inputs with CRO editorial review, compressing the production window from days to hours.
Enrich
Risk committee discussions and management commitments accumulate in meeting minutes but are not systematically structured to feed forward into the next cycle's pack framing or the annual risk appetite review. The longitudinal record of risk committee governance — what was discussed, what actions were taken, whether management responses were effective — is thin and inaccessible.
<button
class="flow-stages__stage"
type="button"
data-stage="aggregate"
data-flow-id="urn:financial-services:flow:risk-control/risk-reporting-cycle"
>
Aggregate
→
<button
class="flow-stages__stage"
type="button"
data-stage="validate"
data-flow-id="urn:financial-services:flow:risk-control/risk-reporting-cycle"
>
Validate
→
<button
class="flow-stages__stage"
type="button"
data-stage="brief"
data-flow-id="urn:financial-services:flow:risk-control/risk-reporting-cycle"
>
Brief
→
<button
class="flow-stages__stage"
type="button"
data-stage="discuss"
data-flow-id="urn:financial-services:flow:risk-control/risk-reporting-cycle"
>
Discuss
→
<button
class="flow-stages__stage"
type="button"
data-stage="track"
data-flow-id="urn:financial-services:flow:risk-control/risk-reporting-cycle"
>
Track actions
Lens
Scenario
Intent
Complexity

### CARD 16 [Enablement|S] Risk Committee Pre-Read Structuring
urn: urn:financial-services:scenario:flow/risk-control/risk-reporting-cycle/risk-committee-pre-read-structuring
intent: Agent produces a structured committee pre-read from the draft risk pack — executive summary, key risk movements, limit governance status, and proposed discussion agenda — calibrated to the committee's time allocation and prior governance priorities.
Problem to solve: Risk pack narrative drafting consumes two to three analyst-days each cycle on a repeating structure where only the current-period content changes. Committee discussions are frequently dominated by data walkthrough rather than forward-looking governance discussion because the pack structure is not calibrated to direct committee attention toward the most actionable risk developments.
Solution: Agent reads the draft risk pack data inputs and produces the committee pre-read in a standard format: executive summary with three to five key risk movements, limit governance status by domain, and a proposed discussion agenda ranked by materiality and actionability. The CRO reviews the pre-read, adds forward-looking framing, and distributes to the committee two days before the meeting.
OKR objective: The CRO adds forward-looking framing to an agent-produced committee pre-read — with executive summary, key risk movements, limit governance status, and proposed discussion agenda — calibrated to committee time allocation and prior governance priorities.
OKR KR [Adoption]: Agent-produced pre-read used for ≥6 consecutive risk committee meetings within 12 months of go-live; all four standard components (executive summary, key movements, limit governance status, discussion agenda) produced in every run.
OKR KR [Acceptance]: ≥80% of agent-produced pre-reads accepted by the CRO with only minor framing edits before distribution; committee discussions rated as more forward-looking and less data-walkthrough-dominated in ≥75% of post-meeting CRO assessments.
OKR KR [Cycle]: Committee pre-read delivered to the CRO ≥3 business days before each committee meeting, allowing distribution 2 days before the meeting per governance standard.

### CARD 17 [Automation|S] Risk Pack Narrative Drafting
urn: urn:financial-services:scenario:flow/risk-control/risk-reporting-cycle/risk-pack-narrative-drafting
intent: Agent drafts the full risk pack narrative — executive summary, domain commentaries, emerging risk sections, and regulatory developments summary — from structured risk data inputs for CRO editorial review and committee submission.
Problem to solve: Risk pack narrative drafting follows a consistent structure each cycle with only the current-period risk content varying. Drafting consumes two to three senior analyst-days on a repeating structure, compressing the governance review window available to the CRO before the committee deadline.
Solution: Agent reads the consolidated risk data set — domain risk positions, limit utilisation, KRI movements, incident log, and regulatory change inputs — and produces a full draft risk pack narrative per the ERMC/board pack template. The CRO and senior risk officers review the draft, apply risk judgment and forward-looking commentary, and clear for committee distribution. Pack production time compresses from days to hours.
OKR objective: The CRO and senior risk officers apply risk judgement and forward-looking commentary to an agent-drafted full risk pack narrative — covering executive summary, domain commentaries, emerging risk sections, and regulatory developments — rather than authoring from consolidated data inputs.
OKR KR [Adoption]: Agent used to draft the full ERMC/board risk pack narrative for ≥6 consecutive committee cycles within 12 months of go-live; all prescribed pack sections produced by the agent in every run from go-live.
OKR KR [Acceptance]: ≥80% of agent-drafted sections accepted by CRO reviewers without structural revision; pack production cycle time reduced by ≥50% from data lock to committee-ready draft.
OKR KR [Cycle]: Full draft risk pack narrative available within 1 business day of consolidated data set lock, compressing the drafting phase from 2–3 senior analyst-days to ≤4 hours of CRO and senior officer editorial review.

### CARD 18 [Insights|M] Continuous Risk Posture View
urn: urn:financial-services:scenario:flow/risk-control/risk-reporting-cycle/continuous-risk-posture-view
intent: Agent maintains a continuous-form aggregate risk posture for the CRO by synthesising domain risk data as it is produced between formal ERMC and board reporting cycles, flagging material movements that warrant off-cycle attention.
Problem to solve: The CRO lacks a continuous-form view of the institution's aggregate risk posture between monthly ERMC and quarterly board reporting cycles. Material risk movements between cycles are identified through informal domain team channels rather than through a structured continuous signal.
Solution: Agent reads domain risk position outputs on the schedule each domain produces them — daily for market and liquidity, weekly for credit and KRIs, event-driven for operational and compliance — and maintains a rolling cross-domain risk posture summary. The CRO receives a daily digest of material movements above a configurable materiality threshold, with the full posture summary available on demand between formal pack cycles.
OKR objective: The CRO maintains a continuous-form aggregate risk posture — with material cross-domain movements flagged above a configurable threshold — available daily between formal ERMC and board reporting cycles.
OKR KR [Adoption]: Agent-maintained rolling risk posture summary in continuous operation for ≥10 consecutive months in year 1; daily digest delivered to the CRO on ≥200 business days per year once live.
OKR KR [Acceptance]: ≥80% of agent-flagged material risk movements rated as genuinely actionable by the CRO; ≤5% false-positive rate on materiality threshold triggers, validated by quarterly CRO review.
OKR KR [Cycle]: Material risk movement flag delivered to the CRO within 24 hours of the domain data update that triggered it, versus identification through informal channels with no defined latency under the prior approach.

### CARD 19 [Optimize|M] Cross-Domain Risk Coherence Check
urn: urn:financial-services:scenario:flow/risk-control/risk-reporting-cycle/cross-domain-risk-coherence-check
intent: Agent performs a systematic cross-domain coherence check on the consolidated risk data set before narrative drafting — reconciling shared metrics across risk sections, flagging movements inconsistent across domains, and prioritising editorial attention on the most material divergences.
Problem to solve: Cross-domain risk metric consistency — ensuring credit concentration figures reconcile to large-exposure figures in the regulatory reporting section — is checked manually by the Risk Reporting team. Inconsistencies that survive to draft are caught in CRO review, requiring last-minute corrections that compress the delivery window.
Solution: Agent reads the consolidated risk data set and applies a structured coherence rule set — cross-domain metric reconciliation points, prior- period comparison bounds, and BCBS 239 regulatory metric alignment checks — producing a pre-draft quality report that identifies inconsistencies and assigns materiality scores. The Risk Reporting team resolves flagged items before narrative drafting begins, reducing CRO review corrections and compressing the overall production cycle.
OKR objective: The Risk Reporting team resolves cross-domain data inconsistencies before narrative drafting begins, using an agent-generated pre-draft quality report ranked by materiality score.
OKR KR [Adoption]: Agent coherence check run on 100% of consolidated risk data sets before narrative drafting begins within 6 months of go-live; BCBS 239 reconciliation rule set applied in every run.
OKR KR [Acceptance]: ≥80% of flagged inconsistencies confirmed as genuine data errors by the Risk Reporting team; CRO review corrections attributed to cross-domain data inconsistencies reduced by ≥50% year-on-year.
OKR KR [Cycle]: Pre-draft quality report delivered within 2 hours of consolidated data set lock, allowing inconsistency resolution to complete before narrative drafting begins rather than surfacing in CRO review.

### CARD 20 [New opps|M] Risk Committee Governance Longitudinal Record
urn: urn:financial-services:scenario:flow/risk-control/risk-reporting-cycle/risk-committee-governance-longitudinal-record
intent: Agent structures the accumulated record of risk committee discussions, management commitments, and action completion outcomes into a searchable longitudinal governance record that feeds into annual risk appetite reviews and supervisory engagement preparation.
Problem to solve: Risk committee discussions and management commitments accumulate in meeting minutes with variable specificity. The longitudinal record of risk governance — what was discussed, what actions were taken, whether responses were effective — is inaccessible in its current form and does not feed systematically into risk appetite reviews or supervisory examination preparation.
Solution: Agent reads meeting minutes, action logs, and completion records across prior ERMC and board risk committee cycles and structures them into a governance database keyed by risk domain, action type, owner, and completion status. The CRO queries the database to prepare for annual risk appetite reviews and supervisory examinations, and the Risk Reporting team uses the longitudinal record to frame current-period developments in the context of prior governance decisions.
OKR objective: The CRO and Risk Reporting team query a structured longitudinal governance database — keyed by risk domain, action type, owner, and completion status — to prepare for annual risk appetite reviews and supervisory examinations.
OKR KR [Adoption]: Agent-structured governance database incorporating ≥3 prior years of ERMC and board risk committee records deployed within 12 months of go-live; database actively queried by the CRO for ≥2 annual risk appetite reviews or supervisory engagement preparations per year once live.
OKR KR [Acceptance]: ≥75% of CRO queries return relevant prior governance records rated as useful for preparation; supervisory engagement preparation time reduced by ≥30% versus prior approach, as assessed by CCO and CRO.
OKR KR [Cycle]: Database updated within 5 business days of each committee meeting with minutes and action log, maintaining a continuous record rather than a batch annual compilation.

[PAGE TEXT]
Model validation cycle (SR 11-7)
Annual model validation programme — inventory review, independent validation of material models, approval for continued use, performance monitoring, and planned retirement — aligned to SR 11-7 model risk management guidance and CIS supervisor equivalents.
The model validation cycle governs the bank's independent validation of material models across all risk and business domains — credit scoring and ECL models, market risk VaR models, ALM NII and EVE models, AML detection models, pricing models, and decision-support models. SR 11-7 (Federal Reserve / OCC supervisory guidance on model risk management, 2011) is the international benchmark for model risk governance; CIS supervisors increasingly reference SR 11-7 principles in their own model governance expectations, and NBKR and NBK/ARDFM have incorporated model risk into their operational risk supervisory frameworks.
Under SR 11-7, model validation is an independent function that tests model conceptual soundness, data integrity, and performance outcomes — and produces validation findings, approved use conditions, and restrictions. The model inventory, validation schedule, and remediation backlog are primary supervisory examination documents.
GenAI can support the cycle by assisting with validation report drafting, model performance monitoring commentary, and the structured synthesis of validation findings across the model inventory — maintaining consistency and coverage across a large model portfolio.
Analyze
Model performance across the production model inventory is monitored by individual domain teams on separate schedules and reported through separate channels. The CRO and Model Risk Committee lack a consolidated view of model performance health — which models are approaching performance thresholds, which have unresolved validation findings — without manual assembly from multiple model monitoring systems.
Optimize
Validation resource allocation to the prioritised model schedule is a manual planning exercise. When unexpected validation findings from a high-priority model consume more validation capacity than planned, the schedule for lower-priority models slips without a structured re-prioritisation that considers the relative risk of delaying each pending validation.
Automate
Validation report drafting — conceptual soundness summary, data integrity test results, backtesting analysis, and findings documentation — follows the SR 11-7 validation framework structure for each model type. Model performance monitoring commentary and the Model Risk Committee pack are structured, recurring production tasks that repeat for each model each cycle.
Enrich
Validation findings across the model inventory — recurring finding types, common model limitations by domain, and patterns in model performance deterioration — accumulate in individual validation reports rather than in a consolidated findings database. The Model Risk Committee does not have access to a thematic synthesis of validation findings that could prioritise systemic model risk issues above individual model-level management.
<button
class="flow-stages__stage"
type="button"
data-stage="inventory"
data-flow-id="urn:financial-services:flow:risk-control/model-validation-cycle"
>
Inventory
→
<button
class="flow-stages__stage"
type="button"
data-stage="validate"
data-flow-id="urn:financial-services:flow:risk-control/model-validation-cycle"
>
Validate
→
<button
class="flow-stages__stage"
type="button"
data-stage="approve"
data-flow-id="urn:financial-services:flow:risk-control/model-validation-cycle"
>
Approve
→
<button
class="flow-stages__stage"
type="button"
data-stage="monitor"
data-flow-id="urn:financial-services:flow:risk-control/model-validation-cycle"
>
Monitor performance
→
<button
class="flow-stages__stage"
type="button"
data-stage="retire"
data-flow-id="urn:financial-services:flow:risk-control/model-validation-cycle"
>
Retire
Lens
Scenario
Intent
Complexity

### CARD 21 [Enablement|S] Model Inventory Completeness Support
urn: urn:financial-services:scenario:flow/risk-control/model-validation-cycle/model-inventory-completeness-support
intent: Agent supports continuous model inventory maintenance by monitoring model deployment activity in production systems and flagging models that appear to have entered use, been materially changed, or been retired without a corresponding inventory update.
Problem to solve: New models and material model changes do not always trigger a model inventory update before entering production use. The inventory is discovered to be incomplete during annual review rather than maintained as a continuous registry, and inventory completeness is a recurring SR 11-7 examination finding from NBKR and NBK/ARDFM.
Solution: Agent monitors model deployment logs and system change records for production model activity and cross-references against the current model inventory, flagging instances where a model in production has no corresponding inventory entry or where a material change event has occurred without a version update. Model Risk Management receives a weekly inventory gap report for resolution, maintaining continuous inventory completeness between annual reviews.
OKR objective: Model Risk Management maintains continuous model inventory completeness by receiving a weekly agent-generated gap report of production models without a corresponding inventory entry or unversioned material changes.
OKR KR [Adoption]: Agent monitoring model deployment logs and cross-referencing against the inventory on a weekly basis within 6 months of go-live; gap report delivered to Model Risk Management for ≥45 consecutive weeks in year 1.
OKR KR [Acceptance]: ≥80% of agent-flagged inventory gaps confirmed as genuine gaps by Model Risk Management on review; SR 11-7 examination findings on model inventory completeness reduced to zero in the examination following go-live.
OKR KR [Cycle]: Weekly gap report delivered within 1 business day of monitoring cycle close, enabling inventory gaps to be resolved within the same week rather than discovered at annual review.

### CARD 22 [Automation|S] Validation Report Drafting
urn: urn:financial-services:scenario:flow/risk-control/model-validation-cycle/validation-report-drafting
intent: Agent drafts validation report sections — conceptual soundness summary, data integrity test results, outcome analysis narrative, findings documentation, and conditions for approved use — structured per the SR 11-7 validation framework for each model type.
Problem to solve: Validation report drafting is a structured production exercise that consumes Model Validation team capacity on a repeating framework for each model. Validation resource is the binding constraint on the cycle, and drafting effort consumed on report production reduces capacity for independent technical work on the validation backlog.
Solution: Agent reads validation test outputs, model documentation, and the prior validation report for each in-scope model and produces a structured draft validation report per SR 11-7 format — conceptual soundness, data integrity, outcome analysis, sensitivity testing, and findings sections. The Model Validation team reviews, applies independent technical judgment on findings classification and severity, and finalises the report for Model Risk Committee submission.
OKR objective: Model Validation team members apply independent technical judgment on findings classification and severity to agent-drafted validation reports — structured per SR 11-7 format across all prescribed sections — reducing report production effort on the validation cycle's binding constraint.
OKR KR [Adoption]: Agent used to draft validation report sections for ≥70% of in-scope model validations within 12 months of go-live; all SR 11-7 prescribed sections (conceptual soundness, data integrity, outcome analysis, sensitivity, findings) produced in every draft from go-live.
OKR KR [Acceptance]: ≥75% of agent-drafted report sections accepted by Model Validation team members without structural revision; validation cycle throughput (validations completed per quarter) increased by ≥20% versus pre-agent baseline.
OKR KR [Cycle]: Validation report draft delivered within 3 business days of test output and documentation receipt, compressing the drafting phase from ≥1 week of manual production and freeing validation capacity for independent technical work.

### CARD 23 [Insights|M] Model Portfolio Performance Health Dashboard
urn: urn:financial-services:scenario:flow/risk-control/model-validation-cycle/model-portfolio-performance-health-dashboard
intent: Agent consolidates model performance monitoring outputs from all domain teams into a unified model portfolio health dashboard for the Model Risk Committee — showing discriminatory power, calibration drift, stability, and validation finding status across the full model inventory.
Problem to solve: Model performance across the production model inventory is monitored by individual domain teams on separate schedules and reported through separate channels. The Model Risk Committee lacks a consolidated view of model performance health — which models are approaching performance thresholds and which have unresolved SR 11-7 validation findings — without manual assembly from multiple monitoring systems.
Solution: Agent reads performance monitoring outputs from each domain team and maps them to the model inventory, computing a health score per model across four dimensions: discriminatory power trend, calibration status, stability index, and open validation finding count. The Model Risk Committee receives a consolidated portfolio health dashboard at each quarterly meeting, with models approaching performance thresholds flagged for accelerated validation scheduling.
OKR objective: The Model Risk Committee reviews a consolidated model portfolio health dashboard — covering discriminatory power, calibration drift, stability, and validation finding status across the full inventory — at each quarterly meeting.
OKR KR [Adoption]: Agent-consolidated portfolio health dashboard used for ≥4 consecutive Model Risk Committee meetings within 18 months of go-live; all four health dimensions (discriminatory power, calibration, stability, open findings) covered for ≥90% of active models from go-live.
OKR KR [Acceptance]: ≥80% of health score assessments accepted by domain team model owners as accurate; models approaching performance thresholds flagged ≥1 quarter before threshold breach in ≥75% of cases on retrospective review.
OKR KR [Cycle]: Portfolio health dashboard produced within 3 business days of each quarterly domain monitoring data cut, versus ≥3 weeks of manual assembly from separate domain team reports under the prior approach.

### CARD 24 [Optimize|M] Validation Schedule Dynamic Re-Prioritisation
urn: urn:financial-services:scenario:flow/risk-control/model-validation-cycle/validation-schedule-dynamic-reprioritisation
intent: Agent supports dynamic re-prioritisation of the model validation schedule when unexpected findings from high-priority models consume excess validation capacity — computing revised schedule risk scores across pending validations based on model materiality, time since last validation, and current performance monitoring status.
Problem to solve: Validation resource allocation to the model schedule is a manual planning exercise. When high-priority model findings consume more capacity than planned, lower-priority model validations slip without structured re-prioritisation that considers the relative SR 11-7 risk of delaying each pending validation.
Solution: Agent reads the current validation schedule, capacity consumption to date, and performance monitoring signals for each pending model and computes a revised risk-weighted prioritisation score — combining model materiality, elapsed time since last validation, and current performance trend. Model Risk Management receives a recommended revised schedule when actual capacity consumption deviates from plan by more than a defined threshold, maintaining SR 11-7 compliance under capacity pressure.
OKR objective: Model Risk Management maintains SR 11-7 compliance under capacity pressure by applying agent-computed risk-weighted prioritisation scores to dynamically re-sequence pending validations when actual capacity consumption deviates from plan.
OKR KR [Adoption]: Agent re-prioritisation triggered and actioned for ≥80% of capacity deviation events above the defined threshold within 12 months of go-live; model materiality, elapsed time since last validation, and current performance trend applied in every re-prioritisation run.
OKR KR [Acceptance]: ≥75% of agent-recommended schedule revisions accepted by Model Risk Management without manual override; SR 11-7 compliance breaches attributable to unstructured capacity-driven schedule slippage reduced to zero following go-live.
OKR KR [Cycle]: Revised risk-weighted schedule delivered within 1 business day of capacity deviation threshold breach, enabling replanning before the original schedule has materially slipped.

### CARD 25 [New opps|M] Validation Findings Thematic Synthesis
urn: urn:financial-services:scenario:flow/risk-control/model-validation-cycle/validation-findings-thematic-synthesis
intent: Agent structures validation findings across the full model inventory into a thematic synthesis — recurring finding types, common limitations by model domain, and patterns in performance deterioration — for Model Risk Committee review and systemic model risk management.
Problem to solve: Validation findings accumulate in individual validation reports rather than a consolidated findings database. The Model Risk Committee lacks a thematic synthesis of findings that could prioritise systemic model risk issues above individual model-level management, limiting the bank's ability to address root causes of recurring model weaknesses across PD/LGD/EAD, AML, and pricing model classes.
Solution: Agent reads the structured findings sections from all completed validation reports and clusters findings by type, model domain, root cause, and severity — surfacing themes such as recurring data quality gaps, conceptual soundness issues prevalent in a model class, or calibration methodology weaknesses appearing across multiple PD/LGD/EAD models. The Model Risk Committee receives a thematic synthesis alongside individual model approval decisions, enabling systemic remediation to be prioritised alongside model-specific actions.
OKR objective: The Model Risk Committee reviews an agent-produced thematic synthesis of validation findings — clustering by type, model domain, root cause, and severity across the full inventory — alongside individual model approval decisions, enabling systemic remediation to be prioritised.
OKR KR [Adoption]: Agent thematic synthesis produced for ≥4 consecutive quarterly Model Risk Committee meetings within 18 months of go-live; all completed validation reports included in each synthesis run from go-live.
OKR KR [Acceptance]: ≥70% of agent-identified thematic finding clusters rated as actionable for systemic remediation by the Model Risk Committee; ≥1 thematic remediation workstream per annual cycle initiated from agent-surfaced finding patterns.
OKR KR [Cycle]: Thematic synthesis delivered within 2 business days of the quarterly validation report cut-off, enabling committee distribution alongside individual model approval packs rather than as a separate deferred exercise.

[PAGE TEXT]
GenAI-enabled Banking and Financial Services Framework · v11i
×
