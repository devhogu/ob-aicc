# Contact center

The contact center is the highest-volume assisted channel in a bank and carries the most complex regulatory obligations — consumer-protection requirements call for documented complaint handling, regulated disclosure at the point of service, and defined SLA obligations per transaction category. The contact center is also the point where digital channel failures surface: customers who cannot complete a task in a digital channel call a contact-center agent. **The opportunity for GenAI is to instrument every inbound interaction** — routing calls more accurately, assisting contact-center agents in real time, automating quality assurance across 100% of calls, and optimizing workforce schedules from demand forecasts — compressing average handle time, improving first-call resolution, and reducing the compliance exposure of manual QA sampling.

## Problems

### Inbound servicing {#inbound-servicing}

| Lens | Problem |
| --- | --- |
| Insights & analytics | IVR containment rate, first-call resolution, and average handle time are tracked in aggregate across the contact center. The contact-center operations team lacks a step-level view of where the IVR loses customers to transfer to a contact-center agent and which knowledge gaps are driving handle time above standard. Root-cause analysis is episodic and based on sampled call listening rather than systematic coverage. |
| Enablement | Contact-center agents handle a broad range of queries from product knowledge refreshed infrequently and a knowledge base that requires manual search during live calls. The time they spend searching reference materials while customers wait on hold is a direct driver of handle time and a constraint on first-call resolution. |
| Automation | Complaint triage and classification, QA scoring, and workforce scheduling are each performed manually on a sample or periodic basis. The structured, data-driven nature of each task — complaints arrive with classifiable attributes; calls generate scoreable transcripts; scheduling uses known demand forecasts — makes all three candidates for AI-driven automation. |
| New business opportunities | A contact center operating with GenAI-backed agent assist, real-time routing, and 100% call QA coverage creates a compounding performance loop: higher first-call resolution reduces repeat contacts, lower handle time increases capacity within the same headcount, and continuous QA coverage surfaces coaching priorities that improve contact-center agent performance faster than sampled review allows. |

## Inbound call routing & IVR {#inbound-call-routing-ivr}

The automated front-end of the contact center — the IVR system that routes callers to the appropriate skill group of contact-center agents or completes the call in self-service without their involvement. IVR design is a regulated function in retail banking: consumer-protection requirements commonly provide that customers can reach a human agent within a defined number of IVR steps and within a defined wait time. Containment rate — the proportion of calls resolved in the IVR without transfer to a contact-center agent — is the primary cost driver; each percentage point of containment improvement reduces the contact-center agent headcount requirement proportionally.

### IVR Script Update Automation

- URN: urn:financial-services:scenario:customer-channels/contact-center/inbound-call-routing-ivr/ivr-script-update-automation
- Lens: Automation
- Complexity: S
- Intent: The AI agent drafts IVR script updates for approved routing changes and new self-service tasks from the change specification, ready for the IVR operations team to review, test, and deploy. The draft covers menu prompt language, routing logic description, and the self-service task confirmation message, consistent with the Bank's IVR style guide and regulatory consumer-protection wording standards. No script change is released without IVR operations team review and test confirmation.
- Problem to solve: Each approved IVR routing change or new self-service task addition requires a script update: revised menu prompts, updated routing logic documentation, and new task confirmation messages. Script drafting from change specifications is a manual step that delays implementation of containment improvements identified in the monthly routing analysis. Under consumer-protection requirements, IVR menu language must meet defined standards for clarity and complaint-rights disclosure; manual drafting with variable author interpretation creates inconsistent compliance quality across updates.
- Solution: The AI agent reads the approved routing change or self-service task specification and generates menu prompt language, routing logic documentation, and task confirmation messages consistent with the Bank's IVR style guide and regulatory language requirements. The IVR operations team reviews the draft, tests in the staging environment, and confirms before release; the compliance team spot-checks regulatory disclosure language before deployment. Script preparation time and the gap between change approval and deployment are tracked against the pre-deployment manual baseline.
- OKR: A draft IVR script update for each approved routing change or new self-service task — menu prompt language, routing logic documentation, and task confirmation message, consistent with the IVR style guide and consumer-protection wording standards — is available to the IVR operations team for review, testing, and deployment.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent drafts the script update for ≥95% of approved routing changes and self-service task specifications within 1 working day of approval, for ≥12 consecutive months post go-live. |
| Acceptance | ≥85% of drafts confirmed by the IVR operations team without substantive rewrite; ≥95% of drafts sampled by the compliance team pass the regulatory disclosure language spot-check. |
| Cycle | Script preparation time reduced from several days of manual drafting per change to ≤1 day of review; gap between change approval and deployment tracked against the pre-deployment baseline. |

### IVR Containment & Routing Optimization

- URN: urn:financial-services:scenario:customer-channels/contact-center/inbound-call-routing-ivr/ivr-containment-routing-optimisation
- Lens: Insights
- Complexity: M
- Intent: The AI agent analyzes IVR session paths to identify containment failures — where customers exit to a contact-center agent — and quantifies the routing changes and self-service task enablement that would improve containment rate. The analysis clusters failure points by menu node, call reason, and customer segment to distinguish navigational complexity from genuinely unserviceable task types. The Head of Contact Center reviews a monthly ranked improvement backlog with estimated containment recovery value per change.
- Problem to solve: IVR containment rate is tracked in aggregate; the contact-center operations team cannot identify which menu paths fail to contain customers without discrete analytical effort per failure mode. Failure attribution between navigational complexity and unserviceable task types requires manual session log review that is not performed at operational cadence. Each percentage point of containment below target represents a direct headcount cost in the contact-center agent population.
- Solution: The AI agent reads IVR session logs, mapping each session path from entry to exit — containment or transfer to a contact-center agent — and clusters failure points by menu node, call reason, and customer segment. It estimates the containment recovery value of each routing adjustment or self-service task addition, producing a ranked improvement backlog. The Head of Contact Center reviews the monthly output and directs the IVR configuration backlog from an evidence-based priority list.
- OKR: A monthly ranked improvement backlog — with containment recovery value estimated per routing change or self-service task addition, and failure points clustered by menu node, call reason, and segment — is available to the Head of Contact Center for IVR configuration prioritization.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent delivers the IVR containment analysis and ranked backlog for ≥95% of scheduled monthly cycles for ≥12 consecutive months post go-live. |
| Acceptance | ≥75% of ranked improvement items confirmed as actionable by the Head of Contact Center on monthly review; IVR containment rate tracked as primary outcome metric. |
| Cycle | IVR containment failure attribution cycle reduced from ad hoc per-failure-mode manual session log review to monthly automated clustering and backlog delivery within 48 hours of period close. |

### IVR Caller Experience Intelligence

- URN: urn:financial-services:scenario:customer-channels/contact-center/inbound-call-routing-ivr/ivr-caller-experience-intelligence
- Lens: Enablement
- Complexity: M
- Intent: The AI agent analyzes IVR session recordings and post-call survey data to identify caller experience friction points — menu hesitation, incorrect option selection and correction, repeat entry, and abandonment before task completion — and assembles the evidence in a quarterly brief for the IVR design team. The output surfaces behavioral signals not visible in routing analytics, such as callers who navigate correctly but indicate confusion through repeated key presses or extended decision time. The IVR design team uses the brief to complement containment analytics with qualitative experience evidence in configuration improvement decisions.
- Problem to solve: IVR configuration improvement is directed primarily from quantitative containment and routing analytics; the customer experience quality of menu navigation — whether callers are confident in their route, confused by menu language, or making unforced errors — is not measured systematically. Experience friction that does not result in transfer to a contact-center agent is invisible to the current analytics model; callers who eventually self-serve but do so with difficulty are counted as containment successes. Behavioral signals from session recordings — hesitation time, key-correction frequency, repeat navigation — contain experience intelligence that quantitative metrics do not capture.
- Solution: The AI agent analyzes IVR session data for behavioral friction signals — menu hesitation duration, key-correction frequency, repeat option selection, and session abandonment before task completion — and correlates these with post-call survey sentiment where available. The quarterly caller experience brief ranks menu nodes by friction intensity and identifies the prompt language or option structure most associated with navigation errors. The IVR design team reviews the brief alongside the containment analytics output, using both evidence sets in configuration decisions; friction score improvement after redesign is tracked as the primary qualitative outcome metric.
- OKR: A quarterly caller experience brief — ranking IVR menu nodes by friction intensity and identifying the prompt language or option structure most associated with navigation errors — is available to the IVR design team alongside the containment analytics for configuration decisions.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent delivers the caller experience brief for ≥95% of scheduled quarterly cycles for ≥4 consecutive quarters post go-live. |
| Acceptance | ≥75% of ranked friction points confirmed as actionable by the IVR design team on quarterly review; friction score improvement after redesign tracked as primary outcome metric. |
| Cycle | Caller experience friction analysis moved from no systematic measurement to quarterly automated delivery within 1 week of period close. |

## Contact center quality assurance {#contact-center-quality-assurance}

The monitoring and scoring of contact-center agent interactions against a defined QA rubric — compliance disclosure adherence, tone and empathy, resolution accuracy, and escalation procedure. Under consumer-protection requirements, documented QA coverage is a supervisory expectation; the regulator assesses whether the Bank has adequate internal controls over the quality of customer-facing interactions. Manual listening covers 1–3% of call volume in most contact centers — insufficient for systematic compliance monitoring. QA findings drive coaching, script updates, and performance management.

### QA Coaching Brief Generation

- URN: urn:financial-services:scenario:customer-channels/contact-center/contact-center-quality-assurance/qa-coaching-brief-generation
- Lens: Automation
- Complexity: S
- Intent: The AI agent generates a structured coaching brief for each contact-center agent scheduled for QA review, drawn from that agent's scored call sample — identifying the specific interactions and rubric dimensions for discussion, and drafting improvement prompts aligned to the underperformance pattern. The QA manager reviews the brief before the coaching session; the brief replaces the manual session-preparation step. Coaching session preparation time and post-coaching QA score improvement rate are the primary metrics.
- Problem to solve: QA managers prepare for individual coaching sessions by manually reviewing scored call samples, identifying the interactions that best illustrate the contact-center agent's performance pattern, and constructing a discussion agenda. Preparation for a single coaching session can take 30–60 minutes when built from sampled call records; QA team capacity constrains the number of contact-center agents who can receive a structured coaching session per cycle. The session quality depends on the QA manager's time investment; compressed preparation produces generic feedback that does not address the individual agent's specific performance pattern.
- Solution: The AI agent reads the contact-center agent's QA score record for the period — call samples, rubric dimension scores, and trend against prior periods — and generates a coaching brief with the three to five interactions recommended for review, the rubric dimensions driving underperformance, and structured improvement prompts. The QA manager reviews the brief, makes any adjustments, and conducts the session; post-coaching QA score trajectory is tracked per agent. Coaching session preparation time and the proportion of coached contact-center agents showing QA score improvement within two cycles are the primary outcome metrics.
- OKR: A structured coaching brief for each contact-center agent scheduled for QA review — the three to five interactions recommended for discussion, the rubric dimensions driving underperformance, and drafted improvement prompts — is available to the QA manager before the coaching session.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent generates a coaching brief for ≥95% of scheduled QA coaching sessions for ≥12 consecutive months post go-live. |
| Acceptance | ≥80% of briefs used by the QA manager without substantive rework; ≥60% of coached contact-center agents show QA score improvement within two cycles. |
| Cycle | Coaching session preparation time reduced from 30–60 minutes of manual call sample review to ≤10 minutes of brief review per session. |

### Contact Center QA Intelligence

- URN: urn:financial-services:scenario:customer-channels/contact-center/contact-center-quality-assurance/contact-center-qa-intelligence
- Lens: Insights
- Complexity: M
- Intent: The AI agent scores 100% of inbound calls against the Bank's QA rubric — compliance disclosure adherence, resolution accuracy, tone calibration, and escalation procedure — and produces a weekly performance brief decomposed by contact-center agent, team, and call category. The brief identifies the contact-center agents and call types with the lowest QA scores, ranked by coaching priority, and surfaces the specific rubric dimensions driving underperformance. The contact-center QA manager reviews the brief and directs the coaching cycle from an evidence-based priority list rather than from a sampled subset.
- Problem to solve: Manual QA listening covers 1–3% of call volume, providing a statistically insufficient basis for systematic compliance monitoring or individual agent performance assessment. Under consumer-protection requirements, documented QA coverage is a supervisory expectation; 1–3% sampling does not constitute systematic internal control. The coaching cycle is directed by QA team capacity rather than by a current-state performance signal; contact-center agents with consistent disclosure misses may not be reviewed for weeks between manual sampling cycles.
- Solution: The AI agent processes call recordings against the Bank's QA rubric, scoring each interaction on compliance disclosure adherence, resolution accuracy, tone, and escalation procedure adherence. The weekly brief presents scores by contact-center agent and team, ranked by coaching priority, with the specific rubric dimensions driving underperformance highlighted for each low-scoring agent. The QA manager reviews the brief and directs coaching sessions to the highest-priority agents; QA coverage rate and disclosure adherence rate across 100% of calls are tracked as primary compliance outcomes.
- OKR: A weekly QA performance brief — built from scoring 100% of inbound calls against the Bank's QA rubric and ranking contact-center agents, teams, and call categories by coaching priority, with the rubric dimensions driving underperformance — is available to the contact-center QA manager to direct the coaching cycle.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent scores ≥98% of recorded inbound calls against the QA rubric and delivers the weekly brief for ≥95% of scheduled weeks for ≥48 consecutive weeks post go-live. |
| Acceptance | ≥85% of automated scores confirmed in QA team calibration sampling; ≥80% of coaching priorities accepted by the QA manager; disclosure adherence rate tracked as primary compliance metric. |
| Cycle | QA coverage raised from 1–3% of call volume by manual listening to 100% of calls, with coaching priorities refreshed weekly rather than across multi-week sampling cycles. |

### QA Script & Disclosure Gap Detection

- URN: urn:financial-services:scenario:customer-channels/contact-center/contact-center-quality-assurance/qa-script-gap-detection
- Lens: Enablement
- Complexity: M
- Intent: The AI agent analyzes QA-scored call transcripts to identify the product or regulatory disclosure categories with the highest miss rates across the contact-center agent population, and surfaces gaps in the current scripts and call guides that explain systematic underperformance. The output is a quarterly script improvement brief for the contact-center operations and compliance teams, ranking disclosure gap categories by miss rate and associating each gap with a specific script element or call guide deficiency. The script improvement brief reduces the coaching burden by addressing root causes at the script level rather than remediating individual agents.
- Problem to solve: QA coaching addresses individual agent performance; the underlying scripts and call guides that contact-center agents follow are reviewed on a scheduled basis rather than from a current-state miss rate signal. When a regulatory disclosure is consistently missed across multiple agents, the root cause is often a script gap or ambiguous call guide instruction rather than individual agent error; individual coaching does not resolve a systemic script deficiency. Under consumer-protection requirements, disclosure miss rates across the population represent a systemic control weakness; script-level remediation is the appropriate response, not individual coaching alone.
- Solution: The AI agent reads QA-scored call transcripts and aggregates miss rates by disclosure category across the contact-center agent population, computing the frequency of each miss type and identifying the call guide instruction or script element associated with each category. The quarterly brief ranks disclosure gap categories by miss rate and identifies the specific script or call guide element requiring revision for each high-miss category. The compliance and contact-center operations teams review the brief and revise scripts before the next QA cycle; population-level miss rate reduction after script revision is the primary outcome metric.
- OKR: A quarterly script improvement brief — ranking disclosure gap categories by miss rate across the contact-center agent population and identifying the script or call guide element requiring revision for each — is available to the contact-center operations and compliance teams before the next QA cycle.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent delivers the script improvement brief for ≥95% of scheduled quarterly cycles for ≥4 consecutive quarters post go-live. |
| Acceptance | ≥75% of identified script and call guide deficiencies confirmed as requiring revision by the compliance and contact-center operations teams; population-level miss rate after script revision tracked as primary outcome metric. |
| Cycle | Script gap identification moved from scheduled periodic script review to quarterly delivery from current miss-rate data within 1 week of period close. |

## Agent assist & guided resolution {#agent-assist-guided-resolution}

The in-call support layer for contact-center agents — knowledge-base articles, product terms, procedural guidance, and regulatory disclosure checklists — that they access during live interactions. Under consumer-protection requirements, contact-center agents must provide accurate disclosures on product terms, fees, and complaint rights during the service call. Failure to disclose is a supervisory risk. Average handle time is the primary contact-center cost KPI; knowledge search during live calls is the dominant driver of handle time above target.

### Agent Assist Effectiveness Intelligence

- URN: urn:financial-services:scenario:customer-channels/contact-center/agent-assist-guided-resolution/agent-assist-effectiveness-intelligence
- Lens: Insights
- Complexity: S
- Intent: The AI agent analyzes assist-log acceptance rates, knowledge-base miss events, and post-call QA outcomes to produce a weekly accuracy and coverage brief for the contact-center operations manager. The brief identifies knowledge-base gaps — query categories where contact-center agents override or reject assist recommendations — and ranks them by volume for the knowledge management team. The contact-center operations manager reviews the brief and directs knowledge-base remediation from the evidence-ranked backlog.
- Problem to solve: Real-time assist quality is monitored through periodic QA sampling; systematic drift in assist accuracy — emerging from product term updates, regulation changes, or new complaint categories — is not detected until it shows up in QA scores. Knowledge-base gaps generate overrides by contact-center agents and hold transfers at operational cadence but are not aggregated into a prioritized remediation backlog between knowledge management review cycles. The absence of a continuous assist effectiveness brief means the knowledge management team directs remediation effort from scheduled review rather than from current override signal.
- Solution: The AI agent reads assist log records — recommendation surfaced, the contact-center agent's action (accept / override / dismiss), and post-call QA outcome where available — and computes acceptance rates by query category, flagging categories with declining acceptance as potential accuracy drift signals. It identifies knowledge-base miss events — queries where no recommendation was surfaced — and ranks them by volume for remediation prioritization. The weekly brief is reviewed by the contact-center operations manager; knowledge management remediates the ranked backlog before the next quality review cycle.
- OKR: A weekly assist accuracy and coverage brief — acceptance rates by query category, categories with declining acceptance, and knowledge-base miss events ranked by volume — is available to the contact-center operations manager to direct knowledge-base remediation.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent delivers the assist effectiveness brief for ≥95% of scheduled weeks for ≥48 consecutive weeks post go-live. |
| Acceptance | ≥80% of ranked knowledge-base gaps confirmed as requiring remediation by the contact-center operations manager; ≥75% of the ranked backlog remediated by knowledge management before the next quality review cycle. |
| Cycle | Detection of assist accuracy drift reduced from periodic QA sampling and scheduled knowledge review to weekly delivery within 2 days of week close. |

### Post-Call Documentation Automation

- URN: urn:financial-services:scenario:customer-channels/contact-center/agent-assist-guided-resolution/post-call-documentation-automation
- Lens: Automation
- Complexity: S
- Intent: The AI agent generates a structured call summary and CRM update from the call transcript immediately after each interaction, ready for the handling agent's review and confirmation before submission. The summary covers call reason, resolution status, regulatory disclosures delivered, and any follow-up actions, in the format required by the Bank's CRM and compliance documentation standards. The handling agent's after-call work time is the primary operational metric; compliance disclosure documentation completeness is the primary regulatory metric.
- Problem to solve: After-call work — summarizing the interaction, updating CRM records, and documenting regulatory disclosures delivered — is the primary driver of contact-center agent time outside active call handling. Under consumer-protection requirements, accurate post-call documentation of disclosures and complaint flags is a supervisory obligation; documentation quality degrades under high call volume as agents compress after-call work to meet availability targets. After-call work time consumes a material share of total paid hours and is structurally resistant to reduction under the manual documentation model.
- Solution: The AI agent reads the call transcript and generates a structured summary covering call reason, outcome, regulatory disclosures confirmed, and follow-up actions, pre-populated in the Bank's CRM format. The handling agent reviews and confirms before the record is committed; any additions or corrections are captured in the audit trail. After-call work time per interaction and disclosure documentation completeness rate are tracked against pre-deployment baselines as primary outcome metrics.
- OKR: A structured call summary and pre-populated CRM update — call reason, resolution status, regulatory disclosures delivered, and follow-up actions — is available to the handling agent for review and confirmation immediately after each interaction.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent generates the call summary and CRM update for ≥95% of transcribed inbound calls within 30 seconds of call end, for ≥12 consecutive weeks post go-live. |
| Acceptance | ≥85% of summaries confirmed by the handling agent without substantive correction; disclosure documentation completeness rate ≥98% on QA sampling. |
| Cycle | After-call work time per interaction reduced by ≥40% against the pre-deployment baseline within 6 months of go-live. |

### Agent Real-Time Knowledge Assist

- URN: urn:financial-services:scenario:customer-channels/contact-center/agent-assist-guided-resolution/agent-real-time-knowledge-assist
- Lens: Enablement
- Complexity: M
- Intent: The AI agent listens to inbound calls and surfaces the relevant policy, product term, or procedural guidance to the handling agent in real time, reducing average handle time and compliance disclosure misses. The guidance appears in the agent desktop without requiring manual knowledge-base search, eliminating hold transfers for complex queries. Quality assurance reviews assist logs for accuracy drift on a defined cadence.
- Problem to solve: Contact-center agents handle queries on product terms, regulatory disclosures, and fee structures from memory and infrequently updated reference materials; complex queries require placing customers on hold to search the knowledge base, inflating average handle time (AHT). Mandatory consumer-protection disclosures are delivered from memory under call-volume pressure, creating compliance exposure. New hire ramp-up on product and policy knowledge is slow under the current search-and-recall model.
- Solution: The AI agent processes the live call transcript and surfaces the most relevant knowledge-base article, product term, or regulatory disclosure checklist in the agent desktop without requiring manual search. The handling agent reads the guidance and resolves the query without a hold transfer, reducing AHT and ensuring mandatory disclosures are presented in full. Quality assurance reviews assist logs periodically to detect accuracy drift and flag knowledge-base gaps for remediation.
- OKR: Accurate policy, product-term, and regulatory-disclosure guidance is available to the handling agent in the agent desktop on every inbound call — eliminating hold transfers for knowledge queries and reducing compliance disclosure misses.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent surfaces a knowledge-assist recommendation for ≥90% of inbound calls in which a policy, product-term, or regulatory-disclosure query is detected, across ≥12 consecutive weeks post go-live. |
| Acceptance | ≥80% of assist recommendations accepted by handling agents without manual override, as confirmed by QA review of sampled assist logs. |
| Cycle | Average handle time for knowledge-query call types reduced from the pre-deployment baseline by ≥15% within 6 months of go-live. |

## Workforce management {#workforce-management}

The planning, scheduling, and real-time management of contact-center agent capacity against call volume forecasts — the primary cost management lever for the contact center. Workforce management covers interval-level demand forecasting, shift scheduling against skill-group requirements, intraday reforecast and adjustment, and adherence monitoring. Consumer-protection requirements commonly set defined service levels — maximum wait time, answer rate targets — that must be maintained through staffing adequacy. Schedule efficiency is measured as the ratio of productive agent time to total paid hours.

### Contact Center Demand Forecast Intelligence

- URN: urn:financial-services:scenario:customer-channels/contact-center/workforce-management/contact-center-demand-forecast-intelligence
- Lens: Insights
- Complexity: M
- Intent: The AI agent forecasts inbound call volume at 30-minute interval resolution for the next 14 days by skill group, incorporating payroll calendar events, product rate changes, system maintenance windows, and prior-year seasonal patterns. The forecast brief identifies periods where current schedules will miss the service-level target and quantifies the staffing adjustment required to close the gap. The workforce management team reviews the brief and adjusts schedules before the impacted intervals are locked for the next planning cycle.
- Problem to solve: Contact-center demand forecasts are generated from rolling average call volumes with manual adjustments for known events; interval-level demand variability from payroll cycles, product changes, and seasonal peaks is not systematically captured at the granularity required for shift-level scheduling. Defined service levels — maximum wait time and answer rate targets, commonly set by consumer-protection requirements — must be maintained through staffing adequacy; schedules built on rolling averages routinely generate under-staffed and over-staffed intervals that are only visible in retrospect. The workforce management team cannot see which future intervals are at service-level risk without commissioning discrete forecast work per planning cycle.
- Solution: The AI agent reads historical call volume at 30-minute interval resolution by skill group, calendar inputs, and known event triggers, and generates a 14-day interval-level demand forecast with a confidence range per interval. It compares the forecast against current schedules and identifies intervals where scheduled capacity is below the service-level requirement, quantifying the staffing adjustment needed. The workforce management team reviews the brief and adjusts schedules before the planning cycle locks; service-level adherence rate and the proportion of intervals within staff target are the primary outcome metrics.
- OKR: A 14-day inbound call volume forecast at 30-minute interval resolution by skill group — identifying the intervals where current schedules will miss the service-level target and the staffing adjustment required to close the gap — is available to the workforce management team before schedules are locked.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent delivers the 14-day interval forecast brief for ≥95% of scheduled planning cycles for ≥48 consecutive weeks post go-live. |
| Acceptance | ≥80% of recommended staffing adjustments applied by the workforce management team before schedule lock; forecast within ±10% of actual volume for ≥85% of intervals. |
| Cycle | Identification of service-level risk moved from retrospective review of schedules built on rolling averages to 14 days of advance notice at interval level. |

### Intraday Staffing Reforecast

- URN: urn:financial-services:scenario:customer-channels/contact-center/workforce-management/intraday-staffing-reforecast
- Lens: Automation
- Complexity: M
- Intent: The AI agent monitors intraday call arrival against the forecast and, when actual volume deviates materially from the planned level, generates a reforecast for the remaining intervals and recommends the staffing adjustment — voluntary overtime, shift extension, or controlled diversion — for the contact-center supervisor's review and release. The supervisor confirms the adjustment; the decision and outcome are recorded for schedule accuracy improvement in future cycles. Service-level adherence during high-deviation days and reforecast response time are the primary outcome metrics.
- Problem to solve: Intraday demand deviations from forecast — a product outage driving call surge, or a quiet Friday with lower-than-forecast volume — require the contact-center supervisor to manually assess the deviation, determine whether it warrants a staffing adjustment, and identify the available response options. Manual intraday reforecast and adjustment takes 15–30 minutes per deviation event; in a high-volume deviation, service-level degradation accumulates during the assessment window. The cost of intraday staffing errors — under-staffing generating service-level breach, over-staffing generating idle paid hours — is material across the year but individual events are not systematically captured for forecast model improvement.
- Solution: The AI agent monitors actual call arrival at 15-minute intervals against the interval forecast, detects material deviations above a defined threshold, and generates a reforecast for the remaining shift with a recommended staffing adjustment and the available response options. The contact-center supervisor reviews and confirms the adjustment within a defined response window; the outcome is recorded for schedule accuracy diagnostics. Service-level adherence on deviation days and the time from deviation detection to supervisor confirmation are tracked against the pre-deployment manual baseline.
- OKR: A reforecast for the remaining intervals with a recommended staffing adjustment — voluntary overtime, shift extension, or controlled diversion — is available to the contact-center supervisor for review and release whenever intraday call arrival deviates materially from forecast.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent generates a reforecast and staffing recommendation for ≥95% of deviation events above the defined threshold within 15 minutes of detection, for ≥48 consecutive weeks post go-live. |
| Acceptance | ≥80% of recommended adjustments confirmed by the supervisor within the defined response window; service-level adherence on deviation days tracked as primary outcome metric. |
| Cycle | Time from deviation detection to supervisor confirmation reduced from 15–30 minutes of manual assessment to ≤5 minutes of review. |

### Schedule Efficiency Optimization

- URN: urn:financial-services:scenario:customer-channels/contact-center/workforce-management/schedule-efficiency-optimisation
- Lens: Optimize
- Complexity: M
- Intent: The AI agent optimizes the weekly schedule of contact-center agents across skill groups by minimizing idle paid hours while maintaining service-level compliance at each interval, within the constraints of contracted shift patterns and their availability preferences. The optimized schedule is presented to the workforce management team for review and release; the team retains authority to override any assignment before publication. Schedule efficiency — the ratio of productive agent time to total paid hours — and service-level adherence are the dual outcome metrics tracked against the prior manual-schedule baseline.
- Problem to solve: Contact-center schedules are built manually from demand forecasts and the availability of contact-center agents; the optimization is limited by the number of schedule permutations a workforce management planner can evaluate within the planning cycle. Idle paid hours — scheduled agents without sufficient call volume to fill their shift — are a direct cost that manual scheduling cannot minimize effectively across a large skill-group matrix. The workforce management team cannot systematically trade off idle hour cost against service-level risk across hundreds of agents and 30-minute intervals without automated optimization support.
- Solution: The AI agent reads the interval demand forecast, the contact-center agents' availability and contracted shift patterns, and skill-group assignments, and generates an optimized weekly schedule minimizing idle paid hours subject to the service-level constraint at each interval. The optimized schedule is presented to the workforce management team; any assignment can be overridden before publication. Schedule efficiency ratio and service-level adherence are tracked weekly against the prior manual-schedule baseline; efficiency gains are quantified in paid-hours terms for management reporting.
- OKR: An optimized weekly schedule across skill groups — minimizing idle paid hours while holding the service level at each interval, within contracted shift patterns and availability preferences — is available to the workforce management team for review and release.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent generates the optimized weekly schedule for ≥95% of scheduling cycles for ≥48 consecutive weeks post go-live. |
| Acceptance | ≥90% of shift assignments published by the workforce management team without override; schedule efficiency ratio improved by ≥5 percentage points against the prior manual-schedule baseline with service-level adherence maintained. |
| Cycle | Weekly schedule construction reduced from 1–2 days of manual planning to ≤2 hours of review and release. |

## Complaint & escalation handling {#complaint-escalation-handling}

The triage, classification, investigation, and resolution of customer complaints received through the contact center. Consumer-protection requirements commonly oblige banks to acknowledge complaints within defined timelines, classify them by product and regulatory category, and maintain a full audit trail from receipt to resolution. Regulatory reporting on complaint volumes and resolution rates is a periodic supervisory obligation. Manual triage introduces classification inconsistency and SLA risk when complaint volumes spike.

### Complaint Response Drafting

- URN: urn:financial-services:scenario:customer-channels/contact-center/complaint-escalation-handling/complaint-response-drafting
- Lens: Enablement
- Complexity: S
- Intent: The AI agent drafts the formal complaint response for the complaint handler's review from the case investigation record, covering the finding, regulatory obligations met, and resolution outcome in the tone and structure required by consumer-protection standards. The handler reviews, edits, and releases the draft; no response is dispatched without the handler's confirmation. Response drafting time and first-attempt acceptance rate by handlers are the primary efficiency metrics.
- Problem to solve: Complaint handlers draft formal response letters after completing investigation, drawing on the case record to construct a response that meets consumer-protection language requirements. Drafting from case notes is a time-intensive step that varies in quality across handlers; regulatory tone and disclosure requirements are not consistently applied, creating rework and supervisory risk. Response quality and completeness are subject to supervisory scrutiny; inconsistent drafting quality is a reviewable control weakness.
- Solution: The AI agent reads the investigation record — case classification, root cause finding, resolution outcome, and applicable regulatory disclosure requirements — and generates a formal response draft in the Bank's approved template. The complaint handler reviews, edits, and releases; edits are logged and used to identify template improvement opportunities on a quarterly review cycle. Average response drafting time and first-attempt acceptance rate — the proportion of drafts confirmed without substantive revision — are tracked against the pre-deployment baseline.
- OKR: A formal complaint response draft in the Bank's approved template — covering the finding, the regulatory obligations met, and the resolution outcome — is available to the complaint handler for review, editing, and release on completion of each investigation.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent drafts the formal response for ≥95% of complaints with a completed investigation record for ≥48 consecutive weeks post go-live. |
| Acceptance | ≥75% of drafts released by handlers without substantive revision (first-attempt acceptance rate); 100% of responses dispatched only after handler confirmation. |
| Cycle | Average response drafting time reduced from 30–45 minutes of manual drafting from case notes to ≤10 minutes of handler review and edit. |

### Complaint Triage & Classification

- URN: urn:financial-services:scenario:customer-channels/contact-center/complaint-escalation-handling/complaint-triage-classification
- Lens: Automation
- Complexity: M
- Intent: The AI agent classifies inbound complaints by product, theme, and regulatory obligation, assigns severity and SLA band, and drafts the initial root-cause assessment for the complaint handler's review. Classification covers all intake channels — phone, email, digital submission, and branch — in a consistent format that supports regulatory reporting at period end. The complaint handler reviews, edits, and confirms triage before the case progresses.
- Problem to solve: Inbound complaints arriving via multiple channels are manually triaged by the complaints team; classification by product type, regulatory reporting category, and SLA band is inconsistent across handlers. Under consumer-protection requirements, SLA compliance and audit trail completeness are supervisory obligations; manual triage creates SLA breach risk when complaint volumes spike. Cross-channel complaint patterns that warrant systemic investigation are not visible at triage cadence under the current manual model.
- Solution: The AI agent reads complaint content from each intake channel — transcribed calls, email text, digital submissions, and branch-logged complaints — and classifies by product, theme, and regulatory reporting obligation. It assigns severity and SLA band, drafts a root-cause assessment from the complaint narrative, and flags cases with regulatory escalation triggers for senior review. The complaint handler confirms the triage before the case progresses. Regulatory reporting extracts are generated from the classified complaint database at period end, with an unbroken audit trail from intake to resolution.
- OKR: Every inbound complaint from all intake channels is classified by product, theme, regulatory obligation, severity, and SLA band — with a draft root-cause assessment attached — at intake for the complaint handler's confirmation, maintaining SLA compliance and audit trail completeness under consumer-protection requirements.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent classifies ≥98% of inbound complaints at intake across all channels for ≥48 consecutive weeks post go-live. |
| Acceptance | ≥85% of triage classifications confirmed without material amendment by the complaint handler before case progression; SLA breach rate tracked as primary compliance metric. |
| Cycle | Triage classification time per complaint reduced from 15–30 minutes of manual handler review and categorization to ≤5 minutes of AI-assisted handler confirmation. |

### Complaint Pattern Intelligence

- URN: urn:financial-services:scenario:customer-channels/contact-center/complaint-escalation-handling/channel-complaint-pattern-intelligence
- Lens: Insights
- Complexity: M
- Intent: The AI agent analyzes classified complaint records to surface emerging product, process, and channel failure patterns at weekly cadence, providing the Head of Complaints with a current-state pattern brief before the patterns are visible in monthly regulatory reports. The brief ranks complaint themes by volume trend, flags themes with accelerating growth, and identifies the product and process root causes most associated with each pattern. The Head of Complaints and product owners review the brief and determine whether systemic investigation or process remediation is warranted.
- Problem to solve: Complaint classification data exists in the case management system, but cross-case pattern analysis is performed during the monthly regulatory reporting cycle rather than on the week's complaint intake. Emerging product failures or process defects that generate complaint spikes are identified from the monthly report — by which time the pattern has been accumulating for weeks. Under consumer-protection requirements, systemic complaint patterns require investigation and remediation documentation; early identification reduces the regulatory exposure window and the scale of remediation required.
- Solution: The AI agent reads the classified complaint database and computes theme volumes on a rolling 7-day window, comparing each theme's current rate against the prior four-week baseline to identify accelerating patterns. For themes showing material acceleration, it retrieves the case records and identifies the most common product and process root causes from the classification fields. The Head of Complaints reviews the weekly brief with product owners and determines which patterns warrant systemic investigation; time from pattern emergence to investigation initiation is the primary outcome metric.
- OKR: A weekly complaint pattern brief — ranking complaint themes by volume trend, flagging themes accelerating against the prior four-week baseline, and identifying the product and process root causes most associated with each — is available to the Head of Complaints and product owners before the patterns appear in monthly regulatory reports.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent delivers the complaint pattern brief for ≥95% of scheduled weeks for ≥48 consecutive weeks post go-live. |
| Acceptance | ≥70% of flagged accelerating themes confirmed by the Head of Complaints as warranting systemic investigation or process remediation. |
| Cycle | Time from pattern emergence to investigation initiation reduced from 4–6 weeks under the monthly reporting cycle to ≤7 days. |
