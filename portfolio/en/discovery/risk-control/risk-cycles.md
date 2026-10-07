# Risk Cycles

The recurring risk and control cycles — RCSA, stress testing, limits and breach governance, risk reporting, and model validation.

## Identification & assessment {#identification-assessment}

### RCSA cycle (risk & control self-assessment) {#rcsa-cycle}

- URN: urn:financial-services:flow:risk-control/rcsa-cycle
- Summary: Annual RCSA with quarterly refresh — identification and scoring of inherent risks, assessment of control effectiveness, residual risk rating, and issue capture. Aligned to the Basel operational risk standards and, where models are in scope, to model-risk guidance.

The risk and control self-assessment (RCSA) cycle is the Bank's primary mechanism for identifying, assessing, and documenting material risks and the controls that mitigate them across the institution. In line with the Basel III operational risk standards and the three-lines-of-defense model, business lines and functions own the RCSA for their risk domains; the second-line Risk function oversees methodology, challenges ratings, and produces the aggregated risk register. Under model-risk guidance, model risk is a specific RCSA risk type with its own validation and governance requirements. The cycle runs annually for a full RCSA refresh, with quarterly updates to reflect new risks identified through operational incidents, regulatory changes, and business strategy updates. Supervisors expect evidence of an active RCSA framework as part of operational risk supervisory review; the RCSA register and issue log are primary examination documents. GenAI can assist the RCSA narrative — drafting risk descriptions, control assessments, and issue summaries from structured inputs — and flag RCSA ratings that are inconsistent with loss event history or with ratings for equivalent risks in other business lines.

| Lens | Problem |
| --- | --- |
| Analyze | The RCSA risk register and issue log are point-in-time documents updated at cycle boundaries. The CRO lacks a continuous view of residual risk trends — which risks are migrating upward between formal refresh cycles, which action plans are slipping — without manual extraction from the GRC system. |
| Optimize | RCSA rating calibration across business lines and the second-line challenge process are constrained by the time available for manual review. Risks with above-tolerance residual ratings and overdue action plans receive less review time than their materiality warrants when the review burden across the full register is high. |
| Automate | RCSA risk description drafting, control effectiveness narrative production, issue summary writing, and quarterly refresh commentary are structured narrative tasks performed on a consistent framework for each risk item each cycle. GenAI can draft from structured inputs — risk type, loss event history, control design details — with risk officer review. |
| Enrich | RCSA ratings across business lines and the incident event database accumulate across annual cycles but are rarely mined for patterns that would improve the next cycle's risk identification step. Recurring themes — the same operational risk type appearing in three business lines, or a control failing repeatedly in the same way — are identified informally rather than through systematic cross-cycle analysis. |

| Key | Stage | Title | Description | Problem to solve |
| --- | --- | --- | --- | --- |
| identify | Identify | Risk identification across business lines and functions | Identifies material risks within the RCSA scope — operational, conduct, regulatory, model, strategic, and reputational — through structured workshops, top-down risk taxonomy mapping, and bottom-up input from business line and function risk owners. The stage that populates the risk universe for the assessment cycle. | Risk identification workshops are conducted by the second-line Risk function in coordination with business line risk coordinators. Workshop facilitation and output synthesis consume two to four weeks per major business line. Risk items identified through informal channels — operational incidents, regulatory observations, audit findings — are not consistently captured in the RCSA between annual refresh cycles. |
| assess | Assess | Inherent risk scoring and control effectiveness assessment | Scores each identified risk on inherent likelihood and impact and assesses the design and operating effectiveness of the controls that mitigate it — the two inputs from which the residual rating is derived in the next stage. The analytical core of the RCSA cycle. | Inherent risk and control effectiveness scores are self-assessed by business line risk coordinators using the Bank's rating methodology. Calibration consistency — whether the same risk would receive the same inherent score from two different coordinators — is a persistent quality concern. The second-line challenge process catches the most obvious outliers but does not have the capacity to review every rating with equal rigor. |
| score | Score | Residual risk scoring and tolerance classification | Derives the residual risk rating from the inherent risk score and control effectiveness assessment, classifies residuals against the Bank's risk appetite and tolerance thresholds, and identifies risks rated above tolerance for escalation and action. The classification stage that drives the issue and remediation pipeline. | Residual risk ratings above tolerance require an approved action plan. Action plan quality is variable — some plans address root cause with quantified targets and clear owners; others are generic with rolling target dates. The second-line Risk function reviews action plans but is stretched across multiple risk domains and business lines simultaneously. |
| document | Document | RCSA register update and issue log maintenance | Updates the RCSA register with the cycle's assessment outputs — risk descriptions, ratings, control assessments, issue details, and action plans — and maintains the issue log with current status for each open action. The documentation stage that produces the primary RCSA artifact for supervisory examination. | RCSA register documentation is a manual data-entry exercise performed by risk coordinators into the GRC system. Documentation quality — the specificity of risk descriptions, the precision of control effectiveness narratives — is inconsistent across business lines. The quality of RCSA risk descriptions is a common point of supervisory challenge in operational risk examinations. |
| refresh | Refresh | Quarterly RCSA refresh to reflect emerging risks and control changes | Updates the RCSA register each quarter to reflect new risks from operational incidents, regulatory developments, business strategy changes, and audit findings — and revises action plan status for open issues. The maintenance stage that keeps the RCSA current between annual full cycles. | Quarterly RCSA refreshes require risk coordinators to revisit the full register, assess whether any ratings should be updated, and document the rationale for any changes. The refresh cycle competes with operational and project work, and coordinators under capacity pressure tend to confirm existing ratings rather than conducting a substantive review of whether the risk landscape has changed. |

#### RCSA Risk Identification Facilitation Pack

- URN: urn:financial-services:scenario:flow/risk-control/rcsa-cycle/rcsa-risk-identification-facilitation
- Lens: Enablement
- Complexity: S
- Intent: The AI agent supports RCSA risk identification workshops by pre-populating the risk taxonomy with operational incidents, audit findings, and regulatory change signals relevant to each business line's scope.
- Problem to solve: Risk identification workshops are facilitated manually from a generic taxonomy; risk items from operational incidents and regulatory observations accumulate between cycles without being consistently channeled into the RCSA identify stage.
- Solution: The AI agent reads the loss event database, audit findings register, and regulatory change log and maps each item to the relevant RCSA risk taxonomy category and business line scope. Workshop coordinators receive a pre-populated identification pack as the starting point for each workshop, reducing facilitation time and improving coverage of emerging risk themes.
- OKR: RCSA risk identification workshop coordinators use AI-generated pre-populated identification packs — mapping loss events, audit findings, and regulatory change signals to business line scope — as the starting point for each session.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-generated identification packs used for ≥70% of risk identification workshops in the next annual RCSA cycle within 18 months of go-live; all three input sources (loss events, audit findings, regulatory changes) mapped per business line in every pack. |
| Acceptance | ≥80% of identification packs rated as useful or better by workshop coordinators; coverage of emerging risk themes in workshop outputs (assessed against prior-cycle gaps) improved by ≥20% versus workshops run from generic taxonomy alone. |
| Cycle | Pre-populated identification pack delivered within 2 business days of business unit scope confirmation, enabling workshop preparation to complete within the same week. |

#### RCSA Register Narrative Drafting

- URN: urn:financial-services:scenario:flow/risk-control/rcsa-cycle/rcsa-narrative-drafting
- Lens: Automation
- Complexity: S
- Intent: The AI agent drafts RCSA risk descriptions, control effectiveness narratives, and issue summaries from structured inputs — risk type, loss history, control design attributes — for risk officer review and GRC entry.
- Problem to solve: RCSA register documentation is a manual data-entry exercise across dozens of risk items each cycle. Documentation quality is inconsistent across business lines, and the specificity of risk descriptions is a common point of supervisory challenge in operational risk examinations.
- Solution: The AI agent reads structured risk attributes and loss event history for each RCSA item and produces a draft risk description, control effectiveness narrative, and issue summary per the Bank's RCSA methodology. Risk officers review, edit, and submit to the GRC system, compressing documentation effort from days to hours.
- OKR: Risk officers review and submit AI-drafted RCSA risk descriptions, control effectiveness narratives, and issue summaries to the GRC system rather than producing documentation through manual data entry.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent is used to draft RCSA register documentation for ≥70% of risk items in the next full annual RCSA cycle within 18 months of go-live; all three documentation types (risk description, control effectiveness narrative, issue summary) produced per item from go-live. |
| Acceptance | ≥80% of AI-drafted narratives accepted by risk officers with only minor amendment before GRC entry; risk description specificity rated as adequate for ≥90% of items sampled in second-line quality review. |
| Cycle | Draft documentation for each RCSA item available within 1 business day of structured risk attribute input, compressing documentation effort from days to hours of risk officer review per cycle. |

#### RCSA Cross-Cycle Risk Trend Signal

- URN: urn:financial-services:scenario:flow/risk-control/rcsa-cycle/rcsa-cross-cycle-risk-trend-signal
- Lens: Insights
- Complexity: M
- Intent: The AI agent mines the RCSA register across annual cycles to surface risk ratings trending upward between refresh periods, action plans approaching overdue status, and recurring operational risk themes across business lines.
- Problem to solve: The RCSA register is a point-in-time document updated at cycle boundaries. The CRO has no continuous view of which residual risk ratings are drifting upward or which action plans are slipping without manual extraction from the GRC system.
- Solution: The AI agent reads the structured RCSA register and issue log each quarter, computes rating trajectory per risk item against prior cycles, and produces a trend signal report flagging deteriorating residual ratings and overdue action plan status. The CRO receives a concise watchlist and confirms the items for the quarterly refresh governance agenda.
- OKR: The CRO manages a quarterly RCSA watchlist of deteriorating residual risk ratings and overdue action plans, generated by the AI agent's analysis of RCSA register trajectory across prior cycles.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's RCSA cross-cycle analysis runs quarterly within 6 months of go-live; trend signal report delivered to the CRO ahead of ≥4 consecutive quarterly refresh governance meetings in year 1. |
| Acceptance | ≥75% of AI-flagged deteriorating residual ratings confirmed as warranting watchlist inclusion by the CRO; overdue action plan flags confirmed as accurate in ≥85% of instances on review. |
| Cycle | Quarterly trend signal report produced within 3 business days of register data cut, replacing a manual extraction exercise with no defined production timeline between annual RCSA cycle boundaries. |

#### RCSA Rating Calibration Challenge Assist

- URN: urn:financial-services:scenario:flow/risk-control/rcsa-cycle/rcsa-rating-calibration-challenge-assist
- Lens: Optimize
- Complexity: M
- Intent: The AI agent assists the second-line challenge process by flagging RCSA inherent risk and control effectiveness ratings that are inconsistent with the business line's own loss event history or with ratings for equivalent risks in other business lines.
- Problem to solve: Second-line challenge of RCSA ratings is constrained by the volume of items under review each cycle. High-materiality risks with above-tolerance residuals receive insufficient challenge when the review burden spans the full register without systematic triage.
- Solution: The AI agent reads each RCSA rating against the business line's three-year loss event history and cross-business-line comparables for the same risk taxonomy category, scoring calibration deviation. The second-line challenge team receives a prioritized challenge list focused on outlier ratings and high-residual items, allocating review effort by materiality.
- OKR: The second-line challenge team allocates review effort to outlier RCSA ratings and high-residual items identified by the AI agent's comparison of inherent risk and control effectiveness ratings against loss event history and cross-business-line benchmarks.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's calibration challenge analysis covers ≥80% of RCSA items in the next full annual cycle within 18 months of go-live; both loss event history and cross-business-line comparables applied as calibration benchmarks in every run. |
| Acceptance | ≥70% of AI-prioritized challenge items confirmed by the second-line challenge team as warranting scrutiny; challenge capacity redirected to high-materiality, high-residual items as a proportion of total review hours increased by ≥25% versus prior cycle. |
| Cycle | Prioritized challenge list delivered within 3 business days of RCSA first-line submission cut-off, enabling structured second-line review to begin before the challenge window compresses. |

#### RCSA Pattern Mining — Pre-Cycle Brief

- URN: urn:financial-services:scenario:flow/risk-control/rcsa-cycle/rcsa-pattern-mining-next-cycle-brief
- Lens: New opps
- Complexity: M
- Intent: The AI agent analyzes accumulated RCSA ratings, issue log entries, and operational loss events across prior cycles to identify systemic patterns — recurring control failures, risk types appearing across business lines, and action plan completion rates by risk category — and produces a pre-cycle brief for the Risk Strategy team.
- Problem to solve: RCSA ratings and issue histories accumulate across annual cycles but are rarely mined for systemic patterns. Recurring themes — the same operational risk type appearing across three business lines, or a control failing repeatedly in the same form — are identified informally rather than through structured cross-cycle analysis.
- Solution: The AI agent runs a structured cross-cycle analysis of the RCSA register and issue log, clustering risk items by taxonomy, business line, and control type to surface systemic patterns and recurrent themes. The Risk Strategy team receives a pre-cycle brief that prioritizes risk categories for deeper identification attention and calibration review in the upcoming annual cycle.
- OKR: The Risk Strategy team enters the annual RCSA cycle with an AI-produced pre-cycle brief that identifies systemic patterns — recurring control failures, risk types appearing across business lines, and action plan completion rates — from accumulated cross-cycle RCSA data.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's pre-cycle brief produced ahead of ≥1 full annual RCSA cycle within 18 months of go-live; cross-cycle analysis spanning ≥3 prior annual cycles in every run from go-live. |
| Acceptance | ≥70% of AI-identified systemic patterns rated as actionable by the Risk Strategy team; ≥1 structural change to risk identification priorities per annual RCSA cycle attributable to an AI-surfaced cross-cycle pattern. |
| Cycle | Pre-cycle brief delivered ≥4 weeks before the RCSA identification stage begins, enabling the Risk Strategy team to incorporate findings into workshop design rather than identifying patterns after facilitation is complete. |

### Stress testing cycle (ICAAP, ILAAP, climate) {#stress-testing-cycle}

- URN: urn:financial-services:flow:risk-control/stress-testing-cycle
- Summary: Annual integrated stress testing program — ICAAP capital stress, ILAAP liquidity stress, and climate scenario analysis — covering base and adverse scenarios across credit, market, liquidity, and climate risk. Aligned to supervisory expectations for ICAAP/ILAAP and to NGFS physical and transition scenarios, in line with the TCFD recommendations.

The stress testing cycle produces the Bank's integrated assessment of resilience under adverse conditions across capital (ICAAP), liquidity (ILAAP), and climate risk (NGFS scenarios). Supervisory frameworks commonly require banks to conduct annual stress tests and submit ICAAP/ILAAP documents demonstrating that the institution holds sufficient capital and liquidity buffers under defined stress conditions, in line with Basel III Pillar 2 and the BCBS supervisory review process. The climate stress testing element draws on the scenarios of the Network for Greening the Financial System (NGFS) for transition risk and physical risk analysis, in line with the TCFD recommendations. ISSB disclosure standards (IFRS S1/S2) are increasingly referenced by supervisors for climate risk governance; the stress testing cycle feeds the Bank's climate risk disclosures. The cycle runs annually with a mid-year ICAAP refresh. Its primary bottleneck is cross-domain scenario aggregation — translating macro stress scenarios into risk-type-specific shocks, running each risk model independently, and aggregating the outputs into a coherent group capital adequacy or survival horizon statement. GenAI can compress the aggregation narrative and assist with scenario design documentation.

| Lens | Problem |
| --- | --- |
| Analyze | Stress test results are produced and reviewed at the annual submission cycle. Continuous monitoring of the Bank's resilience position — how the ICAAP trough CET1 or ILAAP survival horizon is shifting with the balance sheet between annual submissions — is absent from the standard management information set. |
| Optimize | Stress scenario design and cross-domain consistency checking are constrained by the serial production process. Exploring a wider scenario set — additional macro pathways, idiosyncratic bank-specific scenarios, climate scenario variants — requires proportional additional production effort that the current cycle calendar cannot accommodate. |
| Automate | ICAAP/ILAAP narrative sections — stress scenario descriptions, risk-type-specific adequacy narratives, management action plan documentation, and supervisory query response packs — are structured writing tasks with substantial content reuse across cycles. Climate scenario description following NGFS pathway conventions follows a reproducible structure amenable to AI-assisted drafting. |
| Enrich | Prior supervisory dialogue — questions raised by the regulator in prior supervisory review cycles, findings on methodology, management action plan credibility — represents an institutional knowledge base that rarely feeds systematically into the next cycle's scenario design or narrative framing. Each submission cycle re-learns the same supervisory preferences through fresh dialogue. |

| Key | Stage | Title | Description | Problem to solve |
| --- | --- | --- | --- | --- |
| define | Define scenarios | Macro and idiosyncratic stress scenario design and calibration | Defines the stress scenarios for the cycle — base, adverse, and severely adverse macro scenarios, idiosyncratic scenarios relevant to the Bank's risk profile, and climate scenarios drawn from NGFS pathways. Calibrates scenario severity relative to prior submissions and supervisory benchmarks. | Scenario design requires the Risk Strategy team to align macro scenario assumptions with the Bank's capital projection model, the ALM IRRBB model, and the credit risk ECL framework simultaneously. Scenario assumptions that are coherent at the macro level are often inconsistent when translated into risk-type-specific shocks — a GDP shock that implies credit migration at an implausible rate, or a rate shock that is inconsistent with the liquidity stress assumptions. |
| run | Run models | Stress scenario execution across credit, market, liquidity, and climate risk models | Executes the approved stress scenarios across all material risk models — ECL and credit migration under adverse macro, NII and EVE under IRRBB stress, LCR and survival horizon under combined liquidity stress, and transition/physical risk exposure under NGFS climate scenarios. Produces raw stress output by risk type and scenario. | Each risk domain runs its stress models independently on different systems and at different points in the production calendar. Input data synchronization across domains — ensuring that the credit stress model and the liquidity stress model share the same balance-sheet starting point — is manual and error-prone. Scenario run timing differences mean that some domains produce outputs two to three weeks after others, creating a sequential rather than parallel stress production process. |
| aggregate | Aggregate | Cross-domain stress output aggregation and capital/liquidity impact calculation | Aggregates stress outputs across credit, market, liquidity, and climate risk domains into a group capital impact — trough CET1 ratio under each scenario — and a group liquidity impact — minimum survival horizon under each scenario. The cross-domain synthesis that produces the core ICAAP/ILAAP result. | Cross-domain aggregation requires reconciling independently produced stress outputs into a consistent capital and liquidity impact statement. Domain model differences in scope, timing, and output format require manual transformation before aggregation. The aggregated output is assembled by a small Capital and Treasury team under the submission deadline, and the quality of cross-domain consistency checking is constrained by the time available. |
| approve | Approve | Board and executive approval of stress results and capital/liquidity adequacy assessment | Presents the integrated stress results to the executive committee and board for approval of the capital and liquidity adequacy assessment — including the management action plan that describes the Bank's response under each adverse scenario. The governance gate that authorizes the supervisory submission. | Board presentation of stress results requires a narrative that converts technical risk outputs into a business-comprehensible capital adequacy story. The translation from stress model outputs to the adequacy assessment narrative is performed manually by the Capital and Risk teams under the board presentation deadline. Stress narrative quality — the coherence of the management action plan, the plausibility of the trough-recovery trajectory — is a common focus of supervisory feedback on ICAAP/ILAAP submissions. |
| submit | Submit | ICAAP/ILAAP submission to supervisors and dialogue management | Submits the ICAAP/ILAAP document to the regulator within the supervisory calendar, and manages the subsequent supervisory dialogue — information requests, methodology clarifications, and communication of the supervisory review outcome. The cycle closes when the supervisor's capital or liquidity add-on determination is communicated. | Supervisory information requests after ICAAP/ILAAP submission require the Capital team to re-assemble model inputs and lineage documentation for specific stress outputs. The institutional knowledge of which model produced which output and under which assumption is concentrated in a small technical team; responses to supervisory queries are slow when that team is simultaneously preparing the next cycle or managing other supervisory engagements. |

#### Stress Scenario Design Documentation Support

- URN: urn:financial-services:scenario:flow/risk-control/stress-testing-cycle/stress-scenario-design-documentation-support
- Lens: Enablement
- Complexity: S
- Intent: The AI agent assists the Risk Strategy team in documenting macro stress scenarios to the standard required for ICAAP/ILAAP supervisory submission — narrative framing, NGFS pathway alignment for climate scenarios, and cross-risk-type shock consistency checks.
- Problem to solve: Scenario design documentation requires translating calibrated macro assumptions into consistent cross-domain shocks at the standard supervisors will scrutinize. Scenario assumptions coherent at the macro level are frequently inconsistent when translated into risk-type-specific shock inputs for credit, market, liquidity, and IRRBB models.
- Solution: The AI agent reads the macro scenario parameter set and cross-references shock magnitudes against historical precedent, NGFS pathway benchmarks for climate scenarios, and internal model input ranges across domains. It flags cross-domain inconsistencies and produces a structured scenario documentation template populated with calibrated assumptions, leaving the Risk Strategy team to apply final professional judgment on scenario severity and narrative framing.
- OKR: The Risk Strategy team applies final judgment on scenario severity and narrative framing to an AI-produced scenario documentation template — with macro assumptions calibrated, NGFS pathway alignment confirmed, and cross-domain shock inconsistencies flagged — structured to supervisory submission standards.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent is used to produce scenario documentation templates for ≥80% of ICAAP/ILAAP stress scenarios within 18 months of go-live; cross-domain consistency checks applied across credit, market, liquidity, and IRRBB shock inputs in every run. |
| Acceptance | ≥75% of AI-produced scenario documentation templates accepted by the Risk Strategy team without structural revision; cross-domain shock inconsistencies flagged by the AI agent reduced to ≤2 unresolved items per submission cycle. |
| Cycle | Scenario documentation template delivered within 3 business days of macro parameter set receipt, versus ≥2 weeks of manual documentation under the prior approach. |

#### ICAAP/ILAAP Narrative Section Drafting

- URN: urn:financial-services:scenario:flow/risk-control/stress-testing-cycle/icaap-ilaap-narrative-section-drafting
- Lens: Automation
- Complexity: S
- Intent: The AI agent drafts the narrative sections of the ICAAP/ILAAP document — stress scenario descriptions, risk-type adequacy narratives, and management action plan documentation — from structured model outputs and approved scenario parameters, for CRO and board review.
- Problem to solve: ICAAP/ILAAP narrative drafting is performed manually under the board presentation deadline, consuming senior Capital and Risk team resource on a repeating structure. Narrative quality — the coherence of the management action plan and the plausibility of the trough-recovery trajectory — is a common focus of supervisory feedback on ICAAP/ILAAP submissions.
- Solution: The AI agent reads approved stress scenario parameters, model outputs by risk type, and management action plan commitments and produces draft ICAAP/ILAAP narrative sections per the supervisory submission framework. Each section covers scenario rationale, stress impact by risk type, trough capital or liquidity position, and the management action plan response. The CRO reviews and applies judgment on the adequacy assessment conclusion before board submission.
- OKR: The CRO reviews and applies judgment to AI-drafted ICAAP/ILAAP narrative sections — covering scenario rationale, stress impact, trough position, and management action plan — structured to the supervisory submission framework.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent is used to draft narrative sections for ≥1 ICAAP and ≥1 ILAAP submission cycle within 18 months of go-live; all prescribed section types (scenario rationale, stress impact by risk type, trough, management actions) produced by the AI agent from go-live. |
| Acceptance | ≥80% of AI-drafted sections accepted by the CRO without structural revision; supervisory feedback items attributed to narrative quality or section completeness reduced by ≥40% versus prior submission. |
| Cycle | Narrative section drafts delivered within 3 business days of approved stress parameter and model output receipt, compressing the drafting phase from ≥2 weeks of manual effort. |

#### Monthly Capital & Liquidity Resilience Indicator

- URN: urn:financial-services:scenario:flow/risk-control/stress-testing-cycle/continuous-capital-resilience-monitoring
- Lens: Insights
- Complexity: M
- Intent: The AI agent tracks the Bank's inferred ICAAP trough CET1 and ILAAP survival horizon between annual submissions by applying approved stress parameters to the current balance sheet, producing a monthly resilience indicator for the CRO and Capital Committee.
- Problem to solve: Stress test results are reviewed at the annual ICAAP/ILAAP submission cycle. Continuous monitoring of the Bank's resilience position — how the trough CET1 or ILAAP survival horizon is shifting with the balance sheet between formal submissions — is absent from the standard management information set.
- Solution: The AI agent applies the prior year's approved adverse scenario shocks to the current month-end balance sheet and risk position, computing an indicative trough CET1 and survival horizon on a monthly basis. The Capital team confirms each run against the approved stress parameters, and the CRO and Capital Committee receive a monthly resilience indicator that flags material deterioration in the inferred stress position warranting an off-cycle review.
- OKR: The CRO and Capital Committee monitor a monthly resilience indicator — reflecting the current balance sheet's inferred ICAAP trough CET1 and ILAAP survival horizon — between annual submissions.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-computed monthly resilience indicator delivered to the Capital Committee for ≥10 consecutive months in year 1; covers both trough CET1 (ICAAP) and survival horizon (ILAAP) dimensions from go-live. |
| Acceptance | ≥80% of monthly resilience indicators accepted by the CRO without recalculation; methodology consistency with approved annual ICAAP stress parameters confirmed by the Capital team in ≥90% of monthly runs. |
| Cycle | Monthly resilience indicator produced within 3 business days of month-end balance sheet close, replacing a posture visible only at the annual ICAAP/ILAAP submission. |

#### Parallel Stress Scenario Set Expansion

- URN: urn:financial-services:scenario:flow/risk-control/stress-testing-cycle/parallel-scenario-set-expansion
- Lens: Optimize
- Complexity: M
- Intent: The AI agent extends the stress testing program beyond the minimum ICAAP/ILAAP scenario set by generating additional scenario variants — alternative macro pathways, bank-specific idiosyncratic scenarios, TCFD transition and physical risk combinations — within the approved scenario calibration methodology.
- Problem to solve: Exploring a wider stress scenario set beyond the minimum regulatory submission requirement requires proportional additional production effort that the current serial cycle calendar cannot accommodate. Scenario coverage is constrained by production capacity rather than by scenario risk materiality.
- Solution: The AI agent applies the approved scenario calibration methodology to additional scenario seeds — alternative macro trajectories, sector-specific shocks, NGFS pathway variants — producing parameterized scenario specifications ready for model execution. The Risk Strategy team reviews scenario plausibility, selects the extended set for parallel model runs, and integrates selected results into the ICAAP/ILAAP narrative to demonstrate scenario coverage breadth to supervisors.
- OKR: The Risk Strategy team runs a wider stress scenario set — including TCFD transition and physical risk combinations and idiosyncratic scenarios — within the existing production cycle calendar, using AI-generated parameterized specifications ready for model execution.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-generated additional scenario specifications produced for ≥4 scenario variants beyond the minimum ICAAP/ILAAP required set within 12 months of go-live; approved calibration methodology applied to all AI-generated variants from go-live. |
| Acceptance | ≥70% of AI-generated scenario specifications accepted by the Risk Strategy team as plausible and within approved methodology bounds without material recalibration; ≥2 extended scenario results integrated into the ICAAP/ILAAP narrative per submission cycle. |
| Cycle | Parameterized scenario specification delivered within 3 business days of scenario seed input, versus ≥2 weeks of manual calibration effort per additional scenario under the prior serial approach. |

#### Supervisory Dialogue Knowledge Base

- URN: urn:financial-services:scenario:flow/risk-control/stress-testing-cycle/supervisory-dialogue-knowledge-base
- Lens: New opps
- Complexity: M
- Intent: The AI agent structures accumulated supervisory dialogue from prior supervisory review cycles — ICAAP/ILAAP findings, methodology questions, and management action plan credibility challenges — into a searchable knowledge base that feeds into the next cycle's scenario design and narrative framing.
- Problem to solve: Prior supervisory dialogue represents institutional knowledge that rarely feeds systematically into the next cycle. Each submission re-learns supervisory preferences through fresh dialogue rather than building on experience from prior supervisory review cycles.
- Solution: The AI agent reads prior supervisory review correspondence, information request logs, and supervisory meeting records and structures them into a thematic findings database classified by submission section, risk domain, and finding type. The Risk Strategy team queries the database at scenario design and narrative drafting stages to anticipate supervisory focus areas, and the Capital team uses it to preempt information requests in the submission pack.
- OKR: The Risk Strategy and Capital teams query an AI-structured thematic findings database — classified by submission section, risk domain, and finding type from prior supervisory review cycles — at scenario design and narrative drafting stages to anticipate supervisory focus areas.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-structured supervisory dialogue knowledge base incorporating ≥3 prior supervisory review cycles deployed within 12 months of go-live; database actively queried by the Risk Strategy and Capital teams ahead of ≥1 full submission cycle per year. |
| Acceptance | ≥70% of database-retrieved prior supervisory focus areas rated as relevant to the current submission cycle by the Risk Strategy team; information request preemption rate in supervisory submission improved by ≥20% versus prior cycle. |
| Cycle | Knowledge base updated within 10 business days of each supervisory review interaction record becoming available, maintaining a current institutional record rather than accumulating unstructured correspondence. |

## Governance & oversight {#governance-oversight}

### Limits & breach governance cycle {#limits-breach-governance-cycle}

- URN: urn:financial-services:flow:risk-control/limits-breach-governance-cycle
- Summary: Continuous risk limit monitoring with a structured breach governance cycle — breach detection, root-cause investigation, escalation, and resolution — across financial and non-financial risk types. The cycle anchor is the time from breach detection to documented resolution or approved limit action.

The limits and breach governance cycle operates across all material risk types — credit concentration limits, market risk VaR and sensitivity limits, IRRBB NII-at-risk and EVE limits, liquidity LCR and NSFR floors, operational risk event thresholds, and model performance limits. Under Basel III Pillar 2 and supervisory requirements, a bank is expected to maintain an approved risk appetite with quantified limits, demonstrate continuous monitoring, and evidence a structured escalation process for limit approaches and breaches. The cycle runs continuously for limit monitoring and on a structured cadence — weekly for market and liquidity limits, monthly for credit and operational limits — for formal breach review. Breach governance is not solely a compliance function; the resolution outcome (limit reset, risk reduction, or management action) directly affects the Bank's capital deployment and earnings capacity. GenAI can support the cycle by flagging limit approach patterns before formal breach, drafting breach investigation narratives, and producing the committee-ready breach resolution summary.

| Lens | Problem |
| --- | --- |
| Analyze | Limit utilization across risk types is monitored within each domain but not in a consolidated cross-domain view. The CRO cannot see the full limit utilization picture — which risk types are at high utilization simultaneously, where concentration of near-limit positions creates systemic risk — without manual assembly from multiple risk reporting systems. |
| Optimize | Soft-breach threshold calibration and the timing of escalation relative to hard breach events are set by static rules rather than by dynamic position trajectory analysis. The escalation design does not distinguish between slow drift toward a limit and rapid directional moves, both of which have different intervention needs. |
| Automate | Breach investigation narrative drafting, limit utilization report commentary, and breach resolution documentation are structured writing tasks that repeat for each breach on a consistent framework. The factual content — position history, driver attribution, approver chain — is drawn from risk reporting systems and approval records that an AI agent can traverse systematically. |
| Enrich | Breach histories across risk types — root causes, resolution outcomes, time-to-resolution — are held in individual breach files rather than in a structured repository. Pattern analysis across breach histories that could improve limit calibration and early-warning design is not routinely applied between formal limit review cycles. |

| Key | Stage | Title | Description | Problem to solve |
| --- | --- | --- | --- | --- |
| set | Set limits | Risk appetite limit setting and calibration across risk types | Establishes quantified risk limits for each material risk type — calibrated to the Bank's risk appetite, capital and liquidity constraints, and regulatory minimums — and documents the limit structure in the approved risk appetite framework. Reviewed annually and updated when risk appetite or regulatory requirements change. | Limit calibration requires the Risk Strategy team to translate qualitative risk appetite statements into quantified thresholds that are consistent across risk types and binding at the relevant management level. Inconsistent limit structures — where the board-level limit is the same as the business-line limit, providing no graduated escalation — are a common supervisory observation in risk governance examinations. |
| monitor | Monitor | Continuous automated limit monitoring and utilization reporting | Monitors risk positions continuously against approved limits — VaR and sensitivity positions daily, credit concentration and LCR positions daily, operational risk KRIs weekly — and produces limit utilization reports for each risk committee's information set. The continuous surveillance stage. | Limit monitoring systems across risk domains operate independently and report through separate dashboards. A cross-domain risk concentration — a single large counterparty approaching credit concentration limits while simultaneously contributing to counterparty risk in the trading book — is not surfaced by individual-domain monitoring. The CRO lacks a consolidated limit utilization view across all risk types without manual assembly. |
| detect | Detect breaches | Breach detection, classification, and initial escalation | Detects limit breaches — including hard breaches above approved limits and soft breaches of pre-defined warning thresholds — classifies them by risk type, severity, and duration, and initiates the escalation chain defined in the risk appetite framework. The detection stage that triggers the formal breach governance process. | Soft-breach detection — positions that approach but have not yet exceeded limits — relies on warning threshold rules set at a fixed percentage of the hard limit. Static warning thresholds do not capture rapid directional moves where the position is within tolerance one day and above the hard limit the next. The first formal breach notification can therefore be the hard breach rather than an early warning. |
| investigate | Investigate | Root-cause investigation of confirmed breaches | Investigates confirmed breaches to determine root cause — market move, business-line action, model recalibration, or limit inadequacy — and documents the investigation findings for the breach resolution committee. The analytical stage that shapes the resolution action. | Breach investigation requires the risk team to attribute the position movement to its drivers across a multi-dimensional position space. For market risk VaR breaches, decomposing the move across asset class, desk, and risk factor contributions is a quantitative exercise that the risk team undertakes manually from position reports and attribution tools. Investigation quality and speed vary with the technical depth of the investigating risk officer. |
| resolve | Resolve | Breach resolution — risk reduction, limit reset, or management action | Resolves the breach through an approved action — position reduction to bring within limit, temporary limit override with risk committee approval, or permanent limit reset with board approval where the limit is structurally misaligned to risk appetite. Documents the resolution and updates the limit register. | Breach resolution governance requires documentation of the resolution action, the approver chain, and the post-resolution position. Documentation quality is variable; resolutions that rely on management override rather than position reduction require clear rationale documentation that will withstand supervisory scrutiny during risk governance examinations. |

#### Limit Governance Framework Calibration Support

- URN: urn:financial-services:scenario:flow/risk-control/limits-breach-governance-cycle/limit-governance-framework-calibration-support
- Lens: Enablement
- Complexity: S
- Intent: The AI agent supports the annual limit calibration exercise by modeling graduated escalation structures — warning threshold, management limit, and board-level hard limit per risk type — and flagging where the current limit structure collapses tiers into a single board-level threshold.
- Problem to solve: Inconsistent limit structures — where the board-level limit equals the business-line limit with no graduated escalation — are a common supervisory observation in risk governance examinations. Calibrating a coherent multi-tier structure across all material risk types requires consistent methodology the Risk Strategy team applies manually each year.
- Solution: The AI agent reads the approved risk appetite framework and current limit register, identifies risk types where the limit structure lacks graduated escalation, and produces a draft calibration proposal with three-tier structures anchored to the Bank's capital and liquidity constraints. The Risk Strategy team reviews proposals and submits the revised limit schedule for board approval.
- OKR: The Risk Strategy team submits a revised multi-tier limit schedule for board approval, based on AI-modeled three-tier escalation structures calibrated to the Bank's capital and liquidity constraints across all material risk types.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-modeled calibration proposals covering ≥90% of material risk types delivered to the Risk Strategy team ahead of the next annual limit review cycle; all risk types lacking graduated escalation flagged with a draft three-tier structure from go-live. |
| Acceptance | ≥75% of AI-generated calibration proposals accepted by the Risk Strategy team without material structural revision; 100% of material risk types carrying a graduated three-tier structure in the limit schedule approved by the board. |
| Cycle | Limit calibration proposals delivered within 5 business days of the risk appetite framework (RAF) data cut, enabling review and board submission within the annual RAF update window. |

#### Breach Investigation Narrative Drafting

- URN: urn:financial-services:scenario:flow/risk-control/limits-breach-governance-cycle/breach-investigation-narrative-drafting
- Lens: Automation
- Complexity: S
- Intent: The AI agent drafts the breach investigation narrative — position history, root-cause attribution, approver chain, and resolution recommendation — for confirmed limit breaches, structured per the Bank's breach governance framework.
- Problem to solve: Breach investigation narrative drafting requires the risk team to assemble position history, driver attribution, and governance documentation from multiple risk systems under time pressure. Investigation quality and speed vary with the technical depth of the investigating risk officer, and documentation quality must withstand supervisory scrutiny.
- Solution: The AI agent reads position time series, risk attribution outputs, and approval records for a confirmed breach and produces a structured investigation narrative covering root-cause classification (market move, business action, model recalibration, or limit inadequacy), approver chain, and recommended resolution. The risk officer reviews the draft, applies professional judgment on resolution recommendation, and submits to the breach resolution committee.
- OKR: The risk team submits breach investigation narratives drafted from AI-assembled position history, root-cause attribution, and governance documentation within the breach governance framework's required window.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent is used to draft breach investigation narratives for ≥90% of confirmed limit breaches within 12 months of go-live. |
| Acceptance | ≥80% of AI-drafted narratives accepted by the risk officer with only minor amendment before submission to the breach resolution committee; supervisory challenge rate on investigation quality reduced by ≥30% year-on-year. |
| Cycle | Breach investigation narrative draft available within 2 hours of breach confirmation, versus ≥1 business day under the prior manual approach. |

#### Cross-Domain Limit Utilization Dashboard

- URN: urn:financial-services:scenario:flow/risk-control/limits-breach-governance-cycle/cross-domain-limit-utilisation-dashboard
- Lens: Insights
- Complexity: M
- Intent: The AI agent assembles a consolidated cross-domain limit utilization view — credit concentration, VaR and sensitivity, LCR/NSFR floors, IRRBB NII-at-risk, and operational KRI thresholds — in a single CRO-facing dashboard updated at each domain's monitoring cadence.
- Problem to solve: Limit monitoring systems across risk domains operate independently with separate dashboards. The CRO cannot assess the full limit utilization picture — which risk types are simultaneously at high utilization, where cross-domain concentrations create systemic risk — without manual assembly from multiple reporting systems.
- Solution: The AI agent reads utilization outputs from each domain's monitoring system and assembles a cross-domain limit utilization summary ranked by distance-to-limit, flagging domains approaching 80% of hard limits and any cross-domain correlations where simultaneous high utilization across credit and market risk warrants a consolidated escalation. The view refreshes at each domain's monitoring cadence, and the CRO reviews the consolidated position at each weekly risk management information run.
- OKR: The CRO has a consolidated cross-domain limit utilization view — ranked by distance-to-limit across credit, market, liquidity, IRRBB, and operational KRI thresholds — updated at each domain's monitoring cadence.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-assembled consolidated dashboard in live production for ≥40 weekly management information runs within 12 months of go-live; all five limit domains (credit, VaR/sensitivity, LCR/NSFR, IRRBB NII-at-risk, operational KRI) covered from go-live. |
| Acceptance | ≥85% of weekly consolidated dashboards accepted by the CRO as complete and accurate without manual supplementation; cross-domain correlation flags rated as actionable by the CRO in ≥65% of instances. |
| Cycle | Consolidated dashboard available within 4 hours of the last domain's monitoring data publication, versus same-day manual assembly that could not be reliably completed before the CRO's weekly review. |

#### Dynamic Soft-Breach Threshold Calibration

- URN: urn:financial-services:scenario:flow/risk-control/limits-breach-governance-cycle/dynamic-soft-breach-threshold-calibration
- Lens: Optimize
- Complexity: M
- Intent: The AI agent analyzes position velocity and directional trajectory for each limit-monitored risk type, calibrating dynamic soft-breach warning thresholds that distinguish slow drift from rapid directional moves requiring earlier escalation.
- Problem to solve: Soft-breach warning thresholds are set as a static percentage of the hard limit and do not distinguish between slow position drift and rapid directional moves. The first formal breach notification can be the hard breach rather than an early warning in fast-moving market conditions.
- Solution: The AI agent monitors rolling position velocity for each limit-monitored risk type and recalibrates warning trigger points, within bounds approved by the Risk Strategy team, based on observed directional rate-of-change. Positions with high velocity receive an earlier warning signal relative to distance-to-limit than slow-moving positions; a risk officer reviews each alert, so the escalation chain has time to intervene before a hard breach.
- OKR: The risk management escalation chain receives earlier warning signals for fast-moving positions through AI-calibrated dynamic soft-breach thresholds that distinguish rapid directional moves from slow drift.

| Dimension | Key result |
| --- | --- |
| Adoption | Dynamic threshold calibration applied to ≥90% of limit-monitored risk types within 12 months of go-live; threshold recalibration running at each risk type's monitoring cadence — daily for market and liquidity limits — from go-live. |
| Acceptance | ≥75% of dynamic soft-breach alerts rated as providing materially earlier warning than the prior static threshold by the risk officer reviewing the escalation; false-positive rate on dynamic alerts ≤15% as measured over rolling 90-day windows. |
| Cycle | Threshold recalibration completed within 24 hours of each monitoring cycle, ensuring dynamic warnings reflect current position velocity rather than a trailing static threshold. |

#### Breach Pattern — Limit Recalibration Brief

- URN: urn:financial-services:scenario:flow/risk-control/limits-breach-governance-cycle/breach-pattern-limit-recalibration-brief
- Lens: New opps
- Complexity: M
- Intent: The AI agent mines the breach history database across risk types to identify patterns — recurring root causes, resolution time by type, limits that breach repeatedly — and produces a limit recalibration recommendation brief for the annual risk appetite review.
- Problem to solve: Breach histories across risk types are held in individual breach files rather than a structured repository. Pattern analysis that could improve limit calibration and early-warning design is not routinely applied between formal limit review cycles, meaning structurally misaligned limits recur as annual breach events.
- Solution: The AI agent structures the breach history database by risk type, root cause, resolution outcome, and time-to-resolution, clustering recurring breach patterns that indicate limits set too tightly relative to normal business operations versus genuine risk appetite exceedance. The annual risk appetite review team receives a prioritized recalibration brief with proposed limit and threshold adjustments supported by breach frequency and resolution data, and risk discipline owners decide which candidates warrant review.
- OKR: The annual risk appetite review team receives an AI-produced limit recalibration brief that identifies structurally misaligned limits and recurring breach patterns across all risk types.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced breach pattern and recalibration brief incorporated into the annual risk appetite review for ≥1 full cycle within 18 months of go-live; breach history database covering ≥3 years of records structured for analysis. |
| Acceptance | ≥70% of recalibration candidates flagged by the AI agent accepted by risk discipline owners as warranting review; ≥1 material limit adjustment per annual risk appetite review attributable to an AI-identified recurring breach pattern. |
| Cycle | Breach pattern analysis and recalibration brief produced within 5 business days of data cut, replacing a manual exercise that was not routinely performed between formal review cycles. |

### Risk reporting cycle (ERMC & board) {#risk-reporting-cycle}

- URN: urn:financial-services:flow:risk-control/risk-reporting-cycle
- Summary: Monthly and quarterly risk reporting to the executive risk management committee and board — integrated risk picture, limit utilization, emerging risks, and regulatory developments. The cycle anchor is the time from risk position data to a committee-ready risk pack.

The risk reporting cycle produces the Bank's periodic risk management reports for the executive risk management committee (ERMC), the board risk committee (BRC), and the full board — the primary governance forums by which the institution's leadership monitors risk posture and holds the CRO accountable. Supervisors expect a bank to demonstrate that board-level risk oversight is substantive and informed; the quality of risk reporting packs is assessed directly in supervisory governance examinations. The cycle runs monthly for the ERMC and quarterly for the board risk committee, with an annual integrated risk report to the full board. Each reporting event requires the Risk function to synthesize positions, limit utilization, emerging risks, regulatory developments, and forward-looking risk indicators across all material risk domains into a single coherent management document. GenAI can accelerate the aggregation and narrative drafting stages — assembling the cross-domain risk picture from standard inputs and producing committee-ready commentary — freeing the CRO and risk officers for the analytical and governance work that boards are convened to perform.

| Lens | Problem |
| --- | --- |
| Analyze | The committee risk pack is produced at monthly and quarterly intervals. The CRO lacks a continuous view of the institution's aggregate risk posture between formal reporting cycles — which domains are in motion, which are stable — without triggering an ad hoc report assembly. |
| Optimize | Cross-domain risk coherence checking and the calibration of the pack's executive summary to committee members' analytical priorities are performed by the Risk Reporting team manually each cycle without a systematic framework for allocating editorial attention to the most material and actionable risk developments. |
| Automate | Risk pack narrative drafting — executive summary, domain commentaries, emerging risk sections, regulatory developments summary — follows a consistent structure each cycle with only the current-period risk content varying. GenAI can draft from structured risk data inputs with CRO editorial review, compressing the production window from days to hours. |
| Enrich | Risk committee discussions and management commitments accumulate in meeting minutes but are not systematically structured to feed forward into the next cycle's pack framing or the annual risk appetite review. The longitudinal record of risk committee governance — what was discussed, what actions were taken, whether management responses were effective — is thin and inaccessible. |

| Key | Stage | Title | Description | Problem to solve |
| --- | --- | --- | --- | --- |
| aggregate | Aggregate | Cross-domain risk data aggregation for the reporting cycle | Collects risk position data, limit utilization reports, incident and loss event records, and emerging risk signals from each risk domain team — credit, market, liquidity, operational, compliance, model, cyber, and climate — and assembles the cross-domain risk data set for the reporting cycle. The data assembly stage. | Risk data for the ERMC pack is collected from domain risk teams on varying schedules, each submitting their contribution in their own format. The Risk Reporting team reconciles and consolidates contributions manually — aligning metrics to common definitions, resolving cross-domain inconsistencies, and filling gaps where domain submissions arrive late. The consolidation consumes the majority of the production window. |
| validate | Validate | Cross-domain consistency checking and prior-period comparison | Validates the consolidated risk picture for internal consistency — cross-domain coherence, reconciliation to prior-period positions, and alignment of risk metrics to management accounts figures — before narrative drafting begins. The quality assurance stage. | Cross-domain risk metric consistency — ensuring that the credit concentration figure in the credit risk section reconciles to the large-exposure figure in the regulatory reporting section — is checked manually by the Risk Reporting team. Inconsistencies that survive to the draft report are caught by the CRO review and require last-minute corrections that compress the delivery window. |
| brief | Brief | Executive and board risk pack narrative drafting and assembly | Produces the committee risk pack — executive summary, domain risk heat maps, limit utilization dashboards, emerging risk narratives, and regulatory developments summary — in a format calibrated for the committee's time allocation and analytical depth. The production stage. | Risk pack narrative drafting — the executive summary, domain highlight commentaries, and emerging risk narratives — is performed by a small senior risk team manually each cycle. The same structural framework is applied each period; only the current-period content changes. Drafting consumes two to three analyst-days on a repeating structure that lends itself to AI-assisted production. |
| discuss | Discuss | Committee review and risk governance discussion | Presents the risk pack to the ERMC or board risk committee for substantive governance discussion — material risk movements, limit governance status, management actions on emerging risks, and regulatory developments. The governance event the reporting cycle is built around. | Committee discussions on risk packs are frequently dominated by data walkthrough rather than forward-looking governance discussion. Committees spend a disproportionate fraction of their time confirming factual accuracy and understanding metric movements rather than discussing management actions, strategic risk implications, and the adequacy of the risk management response. |
| track | Track actions | Post-committee action tracking and management response monitoring | Captures committee actions and management commitments from the risk pack discussion, tracks completion against agreed timelines, and updates the open-action register for the next cycle's committee pack. The follow-through stage that converts committee decisions into operational mandates. | Committee actions from risk discussions are captured in meeting minutes with variable specificity. The link between the action as minuted, the responsible owner, and the completion criterion is not always explicit enough to determine whether the action has been completed at the next reporting cycle. Management commitments made to the regulator during supervisory engagement are similarly tracked with insufficient rigor. |

#### Risk Committee Pre-Read Structuring

- URN: urn:financial-services:scenario:flow/risk-control/risk-reporting-cycle/risk-committee-pre-read-structuring
- Lens: Enablement
- Complexity: S
- Intent: The AI agent produces a structured committee pre-read from the draft risk pack — executive summary, key risk movements, limit governance status, and proposed discussion agenda — calibrated to the committee's time allocation and prior governance priorities.
- Problem to solve: Committee discussions are frequently dominated by data walkthrough rather than forward-looking governance discussion because the pack structure is not calibrated to direct committee attention toward the most actionable risk developments. Members spend a disproportionate share of meeting time confirming figures and understanding metric movements rather than discussing management actions and the adequacy of the risk management response.
- Solution: The AI agent reads the draft risk pack data inputs and produces the committee pre-read in a standard format: executive summary with three to five key risk movements, limit governance status by domain, and a proposed discussion agenda ranked by materiality and actionability. The CRO reviews the pre-read, adds forward-looking framing, and distributes to the committee two days before the meeting.
- OKR: The CRO adds forward-looking framing to an AI-produced committee pre-read — with executive summary, key risk movements, limit governance status, and proposed discussion agenda — calibrated to committee time allocation and prior governance priorities.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced pre-read used for ≥6 consecutive risk committee meetings within 12 months of go-live; all four standard components (executive summary, key movements, limit governance status, discussion agenda) produced in every run. |
| Acceptance | ≥80% of AI-produced pre-reads accepted by the CRO with only minor framing edits before distribution; committee discussions rated as more forward-looking and less data-walkthrough-dominated in ≥75% of post-meeting CRO assessments. |
| Cycle | Committee pre-read delivered to the CRO ≥3 business days before each committee meeting, allowing distribution 2 days before the meeting per governance standard. |

#### Risk Pack Narrative Drafting

- URN: urn:financial-services:scenario:flow/risk-control/risk-reporting-cycle/risk-pack-narrative-drafting
- Lens: Automation
- Complexity: S
- Intent: The AI agent drafts the full risk pack narrative — executive summary, domain commentaries, emerging risk sections, and regulatory developments summary — from structured risk data inputs for CRO editorial review and committee submission.
- Problem to solve: Risk pack narrative drafting follows a consistent structure each cycle with only the current-period risk content varying. Drafting consumes two to three senior analyst-days on a repeating structure, compressing the governance review window available to the CRO before the committee deadline.
- Solution: The AI agent reads the consolidated risk data set — domain risk positions, limit utilization, KRI movements, incident log, and regulatory change inputs — and produces a full draft risk pack narrative per the ERMC/board pack template. The CRO and senior risk officers review the draft, apply risk judgment and forward-looking commentary, and clear for committee distribution. Pack production time compresses from days to hours.
- OKR: The CRO and senior risk officers apply risk judgment and forward-looking commentary to an AI-drafted full risk pack narrative — covering executive summary, domain commentaries, emerging risk sections, and regulatory developments — rather than authoring from consolidated data inputs.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent is used to draft the full ERMC/board risk pack narrative for ≥6 consecutive committee cycles within 12 months of go-live; all prescribed pack sections produced by the AI agent in every run from go-live. |
| Acceptance | ≥80% of AI-drafted sections accepted by the CRO and senior risk officers without structural revision; pack production cycle time reduced by ≥50% from data lock to committee-ready draft. |
| Cycle | Full draft risk pack narrative available within 1 business day of consolidated data set lock, compressing the drafting phase from 2–3 senior analyst-days to ≤4 hours of CRO and senior officer editorial review. |

#### Continuous Risk Posture View

- URN: urn:financial-services:scenario:flow/risk-control/risk-reporting-cycle/continuous-risk-posture-view
- Lens: Insights
- Complexity: M
- Intent: The AI agent maintains a continuous view of aggregate risk posture for the CRO by synthesizing domain risk data as it is produced between formal ERMC and board reporting cycles, flagging material movements that warrant off-cycle attention.
- Problem to solve: The CRO lacks a continuous view of the institution's aggregate risk posture between monthly ERMC and quarterly board reporting cycles. Material risk movements between cycles are identified through informal domain team channels rather than through a structured continuous signal.
- Solution: The AI agent reads domain risk position outputs on the schedule each domain produces them — daily for market and liquidity, weekly for credit and KRIs, event-driven for operational and compliance — and maintains a rolling cross-domain risk posture summary. The CRO receives a daily digest of material movements above a configurable materiality threshold, with the full posture summary available on demand between formal pack cycles.
- OKR: The CRO has a continuous view of aggregate risk posture — with material cross-domain movements flagged above a configurable threshold — available daily between formal ERMC and board reporting cycles.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-maintained rolling risk posture summary in continuous operation for ≥10 consecutive months in year 1; daily digest delivered to the CRO on ≥200 business days per year once live. |
| Acceptance | ≥80% of AI-flagged material risk movements rated as genuinely actionable by the CRO; ≤5% false-positive rate on materiality threshold triggers, validated by quarterly CRO review. |
| Cycle | Material risk movement flag delivered to the CRO within 24 hours of the domain data update that triggered it, versus identification through informal channels with no defined latency under the prior approach. |

#### Cross-Domain Risk Coherence Check

- URN: urn:financial-services:scenario:flow/risk-control/risk-reporting-cycle/cross-domain-risk-coherence-check
- Lens: Optimize
- Complexity: M
- Intent: The AI agent performs a systematic cross-domain coherence check on the consolidated risk data set before narrative drafting — reconciling shared metrics across risk sections, flagging movements inconsistent across domains, and prioritizing editorial attention on the most material divergences.
- Problem to solve: Cross-domain risk metric consistency — ensuring credit concentration figures reconcile to large-exposure figures in the regulatory reporting section — is checked manually by the Risk Reporting team. Inconsistencies that survive to draft are caught in CRO review, requiring last-minute corrections that compress the delivery window.
- Solution: The AI agent reads the consolidated risk data set and applies a structured coherence rule set — cross-domain metric reconciliation points, prior-period comparison bounds, and regulatory metric alignment checks in line with the BCBS 239 principles — producing a pre-draft quality report that identifies inconsistencies and assigns materiality scores. The Risk Reporting team resolves flagged items before narrative drafting begins, reducing CRO review corrections and compressing the overall production cycle.
- OKR: The Risk Reporting team resolves cross-domain data inconsistencies before narrative drafting begins, using an AI-generated pre-draft quality report ranked by materiality score.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's coherence check run on 100% of consolidated risk data sets before narrative drafting begins within 6 months of go-live; reconciliation rule set aligned with the BCBS 239 principles applied in every run. |
| Acceptance | ≥80% of flagged inconsistencies confirmed as genuine data errors by the Risk Reporting team; CRO review corrections attributed to cross-domain data inconsistencies reduced by ≥50% year-on-year. |
| Cycle | Pre-draft quality report delivered within 2 hours of consolidated data set lock, allowing inconsistency resolution to complete before narrative drafting begins rather than surfacing in CRO review. |

#### Risk Committee Governance Longitudinal Record

- URN: urn:financial-services:scenario:flow/risk-control/risk-reporting-cycle/risk-committee-governance-longitudinal-record
- Lens: New opps
- Complexity: M
- Intent: The AI agent structures the accumulated record of risk committee discussions, management commitments, and action completion outcomes into a searchable longitudinal governance record that feeds into annual risk appetite reviews and supervisory engagement preparation.
- Problem to solve: Risk committee discussions and management commitments accumulate in meeting minutes with variable specificity. The longitudinal record of risk governance — what was discussed, what actions were taken, whether responses were effective — is inaccessible in its current form and does not feed systematically into risk appetite reviews or supervisory examination preparation.
- Solution: The AI agent reads meeting minutes, action logs, and completion records across prior ERMC and board risk committee cycles and structures them into a governance database keyed by risk domain, action type, owner, and completion status. The CRO queries the database to prepare for annual risk appetite reviews and supervisory examinations, and the Risk Reporting team uses the longitudinal record to frame current-period developments in the context of prior governance decisions.
- OKR: The CRO and Risk Reporting team query a structured longitudinal governance database — keyed by risk domain, action type, owner, and completion status — to prepare for annual risk appetite reviews and supervisory examinations.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-structured governance database incorporating ≥3 prior years of ERMC and board risk committee records deployed within 12 months of go-live; database queried by the CRO ahead of the annual risk appetite review and ≥1 supervisory engagement per year once live. |
| Acceptance | ≥75% of CRO queries return relevant prior governance records rated as useful for preparation; supervisory engagement preparation time reduced by ≥30% versus prior approach, as assessed by the CRO. |
| Cycle | Database updated within 5 business days of each committee meeting with minutes and action log, maintaining a continuous record rather than a batch annual compilation. |

### Model validation cycle (model risk management) {#model-validation-cycle}

- URN: urn:financial-services:flow:risk-control/model-validation-cycle
- Summary: Annual model validation program — inventory review, independent validation of material models, approval for continued use, performance monitoring, and planned retirement — aligned to supervisory model-risk guidance such as SR 11-7.

The model validation cycle governs the Bank's independent validation of material models across all risk and business domains — credit scoring and ECL models, market risk VaR models, ALM NII and EVE models, AML detection models, pricing models, and decision-support models. Supervisory model-risk guidance, such as SR 11-7, serves as an international benchmark for model risk governance; supervisors increasingly reference its principles in their own model governance expectations and often treat model risk within their operational risk frameworks. Under such guidance, model validation is an independent function that tests model conceptual soundness, data integrity, and performance outcomes — and produces validation findings, approved use conditions, and restrictions. The model inventory, validation schedule, and remediation backlog are primary supervisory examination documents. GenAI can support the cycle by assisting with validation report drafting, model performance monitoring commentary, and the structured synthesis of validation findings across the model inventory — maintaining consistency and coverage across a large model portfolio.

| Lens | Problem |
| --- | --- |
| Analyze | Model performance across the production model inventory is monitored by individual domain teams on separate schedules and reported through separate channels. The CRO and Model Risk Committee lack a consolidated view of model performance health — which models are approaching performance thresholds, which have unresolved validation findings — without manual assembly from multiple model monitoring systems. |
| Optimize | Validation resource allocation to the prioritized model schedule is a manual planning exercise. When unexpected validation findings from a high-priority model consume more validation capacity than planned, the schedule for lower-priority models slips without a structured re-prioritization that considers the relative risk of delaying each pending validation. |
| Automate | Validation report drafting — conceptual soundness summary, data integrity test results, backtesting analysis, and findings documentation — follows the validation framework structure for each model type. Model performance monitoring commentary and the Model Risk Committee pack are structured, recurring production tasks that repeat for each model each cycle. |
| Enrich | Validation findings across the model inventory — recurring finding types, common model limitations by domain, and patterns in model performance deterioration — accumulate in individual validation reports rather than in a consolidated findings database. The Model Risk Committee does not have access to a thematic synthesis of validation findings that could prioritize systemic model risk issues above individual model-level management. |

| Key | Stage | Title | Description | Problem to solve |
| --- | --- | --- | --- | --- |
| inventory | Inventory | Model inventory review and validation schedule prioritization | Reviews the model inventory — all material models in production use across the Bank — updates the inventory for new models, retired models, and material changes to existing models, and produces the annual validation schedule prioritized by model materiality and time since last validation. The planning stage that governs the full validation cycle. | Model inventory maintenance is a joint responsibility between Model Risk Management, model development teams, and business owners. New models and material model changes do not always trigger an inventory update before they enter production use; the inventory is discovered to be incomplete during annual review rather than maintained as a continuous registry. Inventory completeness is a commonly cited model risk governance deficiency in supervisory examinations. |
| validate | Validate | Independent technical validation of models per model-risk guidance | Conducts independent validation of each in-scope model — conceptual soundness review, data integrity testing, outcome analysis and backtesting, sensitivity testing, and documentation adequacy assessment — and documents findings, limitations, and conditions for approved use. The technical core of the validation process. | Model validation resource is the binding constraint on the validation cycle. The Model Validation team has capacity to validate a defined number of models per year; the model inventory growth rate — from new credit scoring models, updated AML detection models, and expanded pricing models — consistently exceeds the team's validation capacity, creating a validation backlog that exposes the Bank to supervisory findings on unvalidated models in production use. |
| approve | Approve | Model approval, restriction, or decommission decision | Reviews validation findings with the Model Risk Committee and produces an approval decision for each validated model — full approval for continued use, conditional approval with restrictions, or model decommission recommendation — aligned to the model-risk governance framework for approval authority and escalation. | Model Risk Committee approval discussions require members to engage substantively with technical validation findings across a diverse model portfolio — credit, market, liquidity, AML, pricing. Committee time is frequently consumed by factual clarification of technical findings rather than by governance decisions on model use conditions and remediation priorities. |
| monitor | Monitor performance | Ongoing model performance monitoring and drift detection | Monitors production model performance continuously against pre-defined performance thresholds — discriminatory power, calibration, stability, and output distribution — flagging models that have drifted beyond acceptable performance bounds between formal validation cycles. The continuous oversight stage between annual validations. | Model performance monitoring reports are produced by model development teams rather than by the independent Model Validation team, creating a self-monitoring structure that model-risk guidance treats as a governance gap. Performance thresholds are set at model approval but are not always recalibrated when the business environment changes materially — a credit scoring model calibrated in a benign credit environment will show performance metrics that are technically within threshold even as its discriminatory power deteriorates against the current portfolio. |
| retire | Retire | Model retirement planning and decommission execution | Plans and executes the retirement of models that are no longer fit for use — superseded by replacement models, performing below threshold, or identified as materially limited in validation — following the model retirement procedure with appropriate management and IT system decommission steps. | Model retirement is the least governed stage of the model lifecycle. Models recommended for decommission by validation findings remain in production use because the business owner has not commissioned a replacement, or because the IT system decommission has not been prioritized. Model-risk guidance expects models not in continued approved use to be restricted or decommissioned; a backlog of models in this state is a common examination finding. |

#### Model Inventory Completeness Support

- URN: urn:financial-services:scenario:flow/risk-control/model-validation-cycle/model-inventory-completeness-support
- Lens: Enablement
- Complexity: S
- Intent: The AI agent supports continuous model inventory maintenance by monitoring model deployment activity in production systems and flagging models that appear to have entered use, been materially changed, or been retired without a corresponding inventory update.
- Problem to solve: New models and material model changes do not always trigger a model inventory update before entering production use. The inventory is discovered to be incomplete during annual review rather than maintained as a continuous registry, and inventory completeness is a common model risk governance finding in supervisory examinations.
- Solution: The AI agent monitors model deployment logs and system change records for production model activity and cross-references against the current model inventory, flagging instances where a model in production has no corresponding inventory entry or where a material change event has occurred without a version update. Model Risk Management receives a weekly inventory gap report for resolution, maintaining continuous inventory completeness between annual reviews.
- OKR: Model Risk Management maintains continuous model inventory completeness by receiving a weekly AI-generated gap report of production models without a corresponding inventory entry or unversioned material changes.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent monitors model deployment logs and cross-references them against the inventory on a weekly basis within 6 months of go-live; gap report delivered to Model Risk Management for ≥45 consecutive weeks in year 1. |
| Acceptance | ≥80% of AI-flagged inventory gaps confirmed as genuine gaps by Model Risk Management on review; no model inventory completeness findings raised in the first internal audit or supervisory review following go-live. |
| Cycle | Weekly gap report delivered within 1 business day of monitoring cycle close, enabling inventory gaps to be resolved within the same week rather than discovered at annual review. |

#### Validation Report Drafting

- URN: urn:financial-services:scenario:flow/risk-control/model-validation-cycle/validation-report-drafting
- Lens: Automation
- Complexity: S
- Intent: The AI agent drafts validation report sections — conceptual soundness summary, data integrity test results, outcome analysis narrative, sensitivity testing, findings documentation, and conditions for approved use — structured per the validation framework set by model-risk guidance for each model type.
- Problem to solve: Validation report drafting is a structured production exercise that consumes Model Validation team capacity on a repeating framework for each model. Validation resource is the binding constraint on the cycle, and drafting effort consumed on report production reduces capacity for independent technical work on the validation backlog.
- Solution: The AI agent reads validation test outputs, model documentation, and the prior validation report for each in-scope model and produces a structured draft validation report in the validation framework format — conceptual soundness, data integrity, outcome analysis, sensitivity testing, and findings sections. The Model Validation team reviews, applies independent technical judgment on findings classification and severity, and finalizes the report for Model Risk Committee submission.
- OKR: Model Validation team members apply independent technical judgment on findings classification and severity to AI-drafted validation reports — structured in the validation framework format across all prescribed sections — reducing report production effort on the validation cycle's binding constraint.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent is used to draft validation report sections for ≥70% of in-scope model validations within 12 months of go-live; all prescribed sections (conceptual soundness, data integrity, outcome analysis, sensitivity, findings) produced in every draft from go-live. |
| Acceptance | ≥75% of AI-drafted report sections accepted by Model Validation team members without structural revision; validation cycle throughput (validations completed per quarter) increased by ≥20% versus the pre-deployment baseline. |
| Cycle | Validation report draft delivered within 3 business days of test output and documentation receipt, compressing the drafting phase from ≥1 week of manual production and freeing validation capacity for independent technical work. |

#### Model Portfolio Performance Health Dashboard

- URN: urn:financial-services:scenario:flow/risk-control/model-validation-cycle/model-portfolio-performance-health-dashboard
- Lens: Insights
- Complexity: M
- Intent: The AI agent consolidates model performance monitoring outputs from all domain teams into a unified model portfolio health dashboard for the Model Risk Committee — showing discriminatory power, calibration drift, stability, and validation finding status across the full model inventory.
- Problem to solve: Model performance across the production model inventory is monitored by individual domain teams on separate schedules and reported through separate channels. The Model Risk Committee lacks a consolidated view of model performance health — which models are approaching performance thresholds and which have unresolved validation findings — without manual assembly from multiple monitoring systems.
- Solution: The AI agent reads performance monitoring outputs from each domain team and maps them to the model inventory, computing a health score per model across four dimensions: discriminatory power trend, calibration status, stability index, and open validation finding count. Domain team model owners confirm the scores, and the Model Risk Committee receives a consolidated portfolio health dashboard at each quarterly meeting, with models approaching performance thresholds flagged for accelerated validation scheduling.
- OKR: The Model Risk Committee reviews a consolidated model portfolio health dashboard — covering discriminatory power, calibration drift, stability, and validation finding status across the full inventory — at each quarterly meeting.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-consolidated portfolio health dashboard used for ≥4 consecutive Model Risk Committee meetings within 18 months of go-live; all four health dimensions (discriminatory power, calibration, stability, open findings) covered for ≥90% of active models from go-live. |
| Acceptance | ≥80% of health score assessments accepted by domain team model owners as accurate; models approaching performance thresholds flagged ≥1 quarter before threshold breach in ≥75% of cases on retrospective review. |
| Cycle | Portfolio health dashboard produced within 3 business days of each quarterly domain monitoring data cut, versus ≥3 weeks of manual assembly from separate domain team reports under the prior approach. |

#### Validation Schedule Dynamic Re-Prioritization

- URN: urn:financial-services:scenario:flow/risk-control/model-validation-cycle/validation-schedule-dynamic-reprioritisation
- Lens: Optimize
- Complexity: M
- Intent: The AI agent supports dynamic re-prioritization of the model validation schedule when unexpected findings from high-priority models consume excess validation capacity — computing revised schedule risk scores across pending validations based on model materiality, time since last validation, and current performance monitoring status.
- Problem to solve: Validation resource allocation to the model schedule is a manual planning exercise. When high-priority model findings consume more capacity than planned, lower-priority model validations slip without structured re-prioritization that considers the relative model risk of delaying each pending validation.
- Solution: The AI agent reads the current validation schedule, capacity consumption to date, and performance monitoring signals for each pending model and computes a revised risk-weighted prioritization score — combining model materiality, elapsed time since last validation, and current performance trend. Model Risk Management receives a recommended revised schedule when actual capacity consumption deviates from plan by more than a defined threshold and decides whether to adopt it, maintaining compliance with model-risk guidance under capacity pressure.
- OKR: Model Risk Management maintains compliance with model-risk guidance under capacity pressure by applying AI-computed risk-weighted prioritization scores to dynamically re-sequence pending validations when actual capacity consumption deviates from plan.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's re-prioritization triggered and actioned for ≥80% of capacity deviation events above the defined threshold within 12 months of go-live; model materiality, elapsed time since last validation, and current performance trend applied in every re-prioritization run. |
| Acceptance | ≥75% of AI-recommended schedule revisions accepted by Model Risk Management without manual override; breaches of model-risk guidance attributable to unstructured capacity-driven schedule slippage reduced to zero following go-live. |
| Cycle | Revised risk-weighted schedule delivered within 1 business day of capacity deviation threshold breach, enabling replanning before the original schedule has materially slipped. |

#### Validation Findings Thematic Synthesis

- URN: urn:financial-services:scenario:flow/risk-control/model-validation-cycle/validation-findings-thematic-synthesis
- Lens: New opps
- Complexity: M
- Intent: The AI agent structures validation findings across the full model inventory into a thematic synthesis — recurring finding types, common limitations by model domain, and patterns in performance deterioration — for Model Risk Committee review and systemic model risk management.
- Problem to solve: Validation findings accumulate in individual validation reports rather than a consolidated findings database. The Model Risk Committee lacks a thematic synthesis of findings that could prioritize systemic model risk issues above individual model-level management, limiting the Bank's ability to address root causes of recurring model weaknesses across PD/LGD/EAD, AML, and pricing model classes.
- Solution: The AI agent reads the structured findings sections from all completed validation reports and clusters findings by type, model domain, root cause, and severity — surfacing themes such as recurring data quality gaps, conceptual soundness issues prevalent in a model class, or calibration methodology weaknesses appearing across multiple PD/LGD/EAD models. The Model Risk Committee receives a thematic synthesis alongside individual model approval decisions, enabling systemic remediation to be prioritized alongside model-specific actions.
- OKR: The Model Risk Committee reviews an AI-produced thematic synthesis of validation findings — clustering by type, model domain, root cause, and severity across the full inventory — alongside individual model approval decisions, enabling systemic remediation to be prioritized.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's thematic synthesis produced for ≥4 consecutive quarterly Model Risk Committee meetings within 18 months of go-live; all completed validation reports included in each synthesis run from go-live. |
| Acceptance | ≥70% of AI-identified thematic finding clusters rated as actionable for systemic remediation by the Model Risk Committee; ≥1 thematic remediation workstream per annual cycle initiated from AI-surfaced finding patterns. |
| Cycle | Thematic synthesis delivered within 2 business days of the quarterly validation report cut-off, enabling committee distribution alongside individual model approval packs rather than as a separate deferred exercise. |
