# Risk appetite

Risk appetite is the board's formal declaration of the maximum risk the institution will accept in pursuit of its strategic objectives — expressed in the Risk Appetite Statement (RAS), cascaded into BU-level tolerance levels, and bounded by the Bank's risk capacity. Under supervisory requirements, the RAS is typically a board-ratified document with annual review cycles and quarterly performance tracking. **The opportunity for GenAI is continuous instrumentation of risk-budget consumption and scenario-driven recalibration of tolerance levels** — turning a quarterly reporting exercise into a monthly or more frequent operating signal. The cycle from appetite declaration to limit utilization to performance attribution compresses from months to days.

## Problems

### Risk appetite {#risk-appetite}

| Lens | Problem |
| --- | --- |
| Insights & analytics | RAS performance, limit utilization, tolerance breaches, and risk capacity are reported weekly, monthly, or quarterly by separate risk desks. The CRO lacks a single current view across all dimensions, and appetite drift that develops between board meetings stays invisible until the next report. |
| Enablement | Stress-testing RAS metrics, recalibrating tolerance levels, and RAROC sensitivity modeling are bottlenecked on senior modelers and the finance team. The risk team and BU heads wait days to weeks for a what-if, so decisions are taken without one. |
| Automation | The annual RAS board narrative, limit-breach documentation and escalation, stress-test results narratives, recovery scenario packs, and the quarterly risk-adjusted performance pack are produced manually to fixed formats. Quality varies by author, and packs often arrive after the meetings they are meant to inform. |
| New business opportunities | Limits and tolerance levels are recalibrated judgmentally once a year, and some stay unchanged for years regardless of portfolio evolution. With back-tested calibration and a current view of the gap between risk capacity and appetite, the Bank can release unused risk budget to business lines without narrowing its safety margin. |

## Risk appetite statement (RAS) {#risk-appetite-statement-ras}

The Risk Appetite Statement (RAS) is the board-ratified document that formally declares the maximum level and types of risk the institution will accept in pursuit of its strategic objectives — expressed across credit, market, liquidity, operational, compliance, and reputational risk dimensions with qualitative positions and quantitative thresholds. Under supervisory expectations, the RAS typically undergoes annual board review with intra-year updates triggered by material changes to the risk profile or operating environment.

### RAS Board Narrative Pack

- URN: urn:financial-services:scenario:strategic-portfolio/risk-appetite/risk-appetite-statement-ras/ras-board-narrative-pack
- Lens: Automation
- Complexity: S
- Intent: The annual RAS board narrative — risk philosophy, prior-year appetite performance, and proposed changes — is assembled by an AI agent from current risk data and prior board commentary and delivered to the CRO for editing and sign-off.
- Problem to solve: Annual RAS review requires the CRO to collate prior board minutes, current risk metrics, and regulatory context into a board-pack narrative. The drafting exercise spans two to three weeks of senior time with no structured assembly support.
- Solution: The AI agent ingests prior board minutes, current risk-metric feeds, and regulator communications, then generates the RAS narrative in the prescribed board-pack format. The CRO edits for forward judgment and signs off.
- OKR: The annual RAS board narrative — risk philosophy, prior-year appetite performance, and proposed changes — is assembled by an AI agent from current risk-metric feeds, prior board minutes, and regulator communications in the prescribed board-pack format, giving the CRO an editing and forward-judgment task rather than a 2–3 week drafting exercise.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent drafts the RAS board narrative for 100% of annual RAS review cycles; all three required dimensions (risk philosophy, prior-year performance, proposed changes) populated in each draft. |
| Acceptance | ≥80% of AI-produced RAS narratives accepted by the CRO as the working board submission basis without full redraft; regulatory context accuracy confirmed in ≥90% of reviewed narratives. |
| Cycle | Annual RAS narrative drafting cycle reduced from 2–3 weeks of senior time to ≤3 business days of CRO editing and forward-judgment sign-off. |

### RAS performance continuous insights

- URN: urn:financial-services:scenario:strategic-portfolio/risk-appetite/risk-appetite-statement-ras/ras-performance-continuous-insights
- Lens: Insights
- Complexity: S
- Intent: The RAS defines the board's risk appetite across quantitative and qualitative dimensions; tracking actual performance against RAS metrics in continuous form is the operating discipline that makes the RAS actionable rather than a point-in-time declaration. The AI agent maintains a RAS performance dashboard, refreshed monthly, showing distance to each appetite metric and trend direction.
- Problem to solve: RAS performance is reported quarterly to the board risk committee; between board meetings, the executive committee lacks a current read of risk budget consumption relative to the board-set appetite. Material appetite drift that develops intra-quarter is invisible until the next board report.
- Solution: The AI agent integrates RAS metric data — credit metrics, liquidity ratios, operational loss, capital ratios — on a monthly basis, producing a RAS performance dashboard with traffic-light status per metric and trend signals. Metrics moving into amber or red territory generate an automated alert to the CRO. The CRO team reviews each dashboard for accuracy and completeness.
- OKR: RAS performance against all board-set appetite metrics is visible to the executive committee on a monthly basis, with automated alerts reaching the CRO when any metric moves into amber or red territory.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces monthly RAS performance dashboards for ≥10 consecutive months in the first year. |
| Acceptance | ≥85% of dashboards accepted by the CRO team as accurate and complete without material data additions; executive committee adopts dashboard as primary intra-quarter RAS tracking tool. |
| Cycle | RAS performance visibility cycle compressed from quarterly board report to a monthly read. |

### RAS on-demand stress impact tool

- URN: urn:financial-services:scenario:strategic-portfolio/risk-appetite/risk-appetite-statement-ras/ras-scenario-stress-impact-enablement
- Lens: Enablement
- Complexity: M
- Intent: The RAS must be stress-tested to ensure that appetite levels remain appropriate under adverse macro conditions. The AI agent enables the risk team to run on-demand stress scenarios against RAS metrics, estimating the impact of defined macro shocks on credit, capital, and liquidity appetite metrics between annual RAS reviews.
- Problem to solve: RAS stress testing is conducted once annually as part of the ICAAP and RAS review process; the risk team lacks a self-service tool for testing scenario impacts intra-year when macro conditions shift materially. Appetite levels that may be inappropriate under new conditions persist until the annual review.
- Solution: The AI agent provides a self-service RAS stress tool for the risk team, accepting macro scenario parameters and returning the projected impact on each RAS metric with a traffic-light status assessment. Outputs feed directly into the risk committee agenda when material appetite breaches are projected.
- OKR: The risk team can stress-test RAS metrics against any macro scenario on demand, enabling intra-year appetite recalibration proposals when conditions warrant.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's stress tool is used for ≥6 distinct scenario analyses in the 12 months following deployment. |
| Acceptance | ≥75% of stress outputs accepted by the risk committee as analytically sound without requiring external validation. |
| Cycle | RAS stress scenario production time reduced from ≥2 weeks of manual modeling to ≤2 business days. |

## Limits framework {#limits-framework}

The limits framework translates the board-approved Risk Appetite Statement into quantitative ceilings and floors at the business line, portfolio, counterparty, and risk-factor level — covering credit concentration limits, market risk sensitivities, liquidity thresholds, and operational risk event tolerance. Limits are cascaded from the RAS through the risk committee to business lines, with escalation protocols triggered by limit utilization approaching defined warning and hard-breach thresholds.

### Limits framework utilization insights

- URN: urn:financial-services:scenario:strategic-portfolio/risk-appetite/limits-framework/limits-framework-utilisation-insights
- Lens: Insights
- Complexity: S
- Intent: The limits framework governs maximum exposure by risk type, counterparty, sector, and geography. Continuous monitoring of limit utilization — including trend toward limits, not just point-in-time headroom — is essential for the risk management function to anticipate breaches rather than react to them. The AI agent synthesizes limit utilization across all material risk dimensions into a daily dashboard for the CRO.
- Problem to solve: Limit utilization is reported weekly or monthly depending on the risk type; intra-period trend information is not aggregated, and the CRO lacks a single current view across all limit dimensions. Approaching-limit alerts are issued by individual risk desks without coordination, creating noise without hierarchy.
- Solution: The AI agent integrates utilization data across credit, market, liquidity, and operational risk limits on a daily basis, producing a ranked utilization dashboard with trend velocity signals. Limits approaching 80% utilization are elevated to the CRO with a narrative context note. Risk desk owners validate each alert.
- OKR: The CRO has a daily view of limit utilization across all material risk dimensions, with approaching-limit alerts ranked by urgency.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces daily utilization dashboards for ≥95% of business days within six months of deployment. |
| Acceptance | ≥90% of approaching-limit alerts validated by risk desk owners as timely and accurately calculated; the CRO adopts the dashboard as the primary limits monitoring tool. |
| Cycle | CRO limits visibility cycle compressed from weekly/monthly reports to a daily read. |

### Limits breach remediation workflow

- URN: urn:financial-services:scenario:strategic-portfolio/risk-appetite/limits-framework/limits-breach-remediation-workflow
- Lens: Automation
- Complexity: M
- Intent: When a limit is breached, the Bank is required to document the event, escalate to the appropriate governance body, and implement a remediation plan within defined timeframes. The AI agent automates the breach documentation, escalation routing, and remediation tracking workflow, ensuring consistent treatment across all limit types and business lines.
- Problem to solve: Limit breach remediation is managed inconsistently across risk desks; documentation quality varies, escalation routing is manual, and remediation progress is tracked in separate spreadsheets. Supervisory examinations commonly find gaps in breach documentation and follow-through.
- Solution: The AI agent detects limit breaches from the utilization feed, automatically generates a breach record with context (limit type, utilization %, trigger event), routes it to the appropriate governance tier, and tracks remediation status through to closure. Overdue remediations escalate automatically. The risk governance function checks each record.
- OKR: All limit breaches are documented, escalated, and tracked to closure through a standardized automated workflow, eliminating manual process gaps.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent manages the end-to-end breach workflow for ≥95% of documented limit breaches within six months of deployment. |
| Acceptance | ≥90% of breach records accepted by the risk governance function as complete and correctly routed without manual correction; supervisory examination findings on breach documentation reduced to zero. |
| Cycle | Breach documentation and escalation time reduced from ≥24 hours to ≤2 hours from detection. |

### Limits framework calibration scenario

- URN: urn:financial-services:scenario:strategic-portfolio/risk-appetite/limits-framework/limits-framework-optimisation-scenario
- Lens: Optimize
- Complexity: M
- Intent: Limits that are set too tightly constrain business activity unnecessarily; limits that are too loose fail to protect the Bank from concentrated losses. The AI agent models limit recalibration scenarios, testing the impact of limit changes on historical breach frequency, expected loss exposure, and business line activity, enabling the risk committee to make evidence-based calibration decisions.
- Problem to solve: Limits are reviewed annually using judgmental approaches without systematic back-testing; calibration decisions are insufficiently grounded in the Bank's loss history and risk appetite consumption data. Some limits remain unchanged for multiple years regardless of portfolio evolution.
- Solution: The AI agent runs a structured calibration analysis for each material limit, back-testing current levels against historical exposure data, simulating alternative levels, and producing a ranked recommendation for the risk committee. Each recommendation is supported by a projected breach frequency and expected loss impact.
- OKR: Annual limit recalibration decisions are supported by a structured back-tested scenario analysis for each material limit dimension.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced calibration analyses used in ≥80% of annual limits review sessions within 12 months of deployment. |
| Acceptance | ≥75% of calibration recommendations adopted by the risk committee, in whole or with minor amendment. |
| Cycle | Limits calibration analysis preparation time reduced from ≥4 weeks of manual back-testing to ≤1 week. |

## Risk tolerance levels {#risk-tolerance-levels}

Risk tolerance levels are the specific quantitative and qualitative boundaries, cascaded from the RAS to business lines and risk categories, that define the acceptable range of risk outcomes in normal operating conditions. Tolerance levels are distinguished from risk limits: limits are operational controls; tolerance levels express the board's acceptable variance around target outcomes for metrics such as NPL ratio, NIM volatility, cost of risk, and liquidity coverage. Breaches of tolerance levels trigger management review and remediation plans rather than automatic hard stops.

### Tolerance Breach Monitoring Narrative

- URN: urn:financial-services:scenario:strategic-portfolio/risk-appetite/risk-tolerance-levels/tolerance-breach-monitoring-narrative
- Lens: Insights
- Complexity: S
- Intent: An AI agent reads current exposure against board-set tolerance levels across all risk types on a weekly cadence. Breaches and near-misses are severity-ranked and delivered to the risk committee as a structured narrative.
- Problem to solve: Risk tolerance levels are reported against actual exposure monthly or quarterly. Breaches and near-misses between reporting cycles are caught manually by risk officers reviewing raw data, with no consistent escalation format.
- Solution: The AI agent reads current exposure data across risk types, compares it against tolerance levels, and generates a weekly breach and near-miss narrative, severity-ranked, with a recommended escalation path. The risk committee receives a structured update without analyst assembly time and confirms the breaches and their severity ranking.
- OKR: Current exposure is compared against board-set tolerance levels across all risk types on a weekly cadence by an AI agent, with breaches and near-misses severity-ranked and delivered to the risk committee as a structured narrative with recommended escalation paths — replacing monthly or quarterly manual monitoring cycles.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces weekly tolerance breach and near-miss narratives for ≥50 consecutive weeks per year; severity ranking and escalation path recommendations included in ≥95% of weekly outputs. |
| Acceptance | ≥85% of AI-surfaced breaches and near-misses confirmed as genuine by the risk committee; severity rankings confirmed as correctly calibrated in ≥90% of reviewed weekly outputs. |
| Cycle | Tolerance-level monitoring cycle reduced from monthly or quarterly manual review to a weekly structured narrative, with breach identification lag reduced to ≤7 days from onset. |

### Risk tolerance recalibration optimization

- URN: urn:financial-services:scenario:strategic-portfolio/risk-appetite/risk-tolerance-levels/risk-tolerance-recalibration-optimisation
- Lens: Optimize
- Complexity: M
- Intent: Tolerance levels that are set below portfolio reality create chronic technical breaches; levels set too loosely fail to provide early warning. The AI agent runs a structured recalibration analysis, back-testing current tolerance levels against two years of metric history and modeling alternative levels against historical and projected breach frequencies, to support evidence-based annual recalibration.
- Problem to solve: Tolerance level recalibration is conducted judgmentally at the annual RAS review without systematic back-testing; some levels often go unadjusted for three or more years despite significant portfolio evolution. Chronic technical breaches consume governance capacity without reflecting genuine risk changes.
- Solution: The AI agent back-tests each tolerance level against historical metric data, identifies levels that are chronically breached or never approached, and models alternative calibrations with projected breach frequency and RAS alignment. The output is a ranked recalibration recommendation for the risk committee.
- OKR: Annual tolerance level recalibration is grounded in a systematic back-tested analysis, reducing chronic technical breaches by at least half within two years.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced recalibration analyses used in 100% of annual RAS review sessions from deployment. |
| Acceptance | ≥70% of recalibration recommendations adopted by the risk committee in whole or with minor amendment. |
| Cycle | Tolerance recalibration analysis preparation time reduced from ≥3 weeks to ≤5 business days. |

### Tolerance Recalibration Scenario Sandbox

- URN: urn:financial-services:scenario:strategic-portfolio/risk-appetite/risk-tolerance-levels/tolerance-recalibration-scenario-sandbox
- Lens: Enablement
- Complexity: L
- Intent: The CRO tests tolerance-level changes across risk types in an AI-backed sandbox and receives an integrated impact narrative — capital headroom shift, limit-utilization change, RAROC impact by BU — before committing a proposal to the board.
- Problem to solve: Recalibrating risk tolerance levels following a macro shock or regulatory change requires the risk team to model capital, liquidity, and P&L implications of alternative thresholds across all risk types. The exercise is bottlenecked on senior modelers and typically spans three to four weeks.
- Solution: An AI-backed sandbox accepts tolerance-parameter changes per risk type and generates an integrated impact narrative covering capital headroom change, limit-utilization shift, RAROC impact by BU, and regulator-alignment assessment. The CRO reviews the narrative, and the board submission starts from the AI-produced analysis.
- OKR: The CRO tests tolerance-level changes across risk types in an AI-backed sandbox and receives an integrated impact narrative — covering capital headroom shift, limit-utilization change, RAROC impact by BU, and regulator-alignment assessment — before committing a recalibration proposal to the board, compressing a 3–4 week modeling exercise into a working session.

| Dimension | Key result |
| --- | --- |
| Adoption | Sandbox in active use for ≥4 material tolerance recalibration exercises per year; integrated impact narrative covering all four dimensions delivered within 4 hours of parameter submission for ≥90% of sandbox runs. |
| Acceptance | ≥80% of AI-produced impact narratives accepted by the CRO as the board submission analytical basis without full re-derivation; capital headroom calculations confirmed accurate in ≥90% of reviewed sandbox outputs. |
| Cycle | Tolerance recalibration impact modeling cycle reduced from 3–4 weeks of senior modeler effort to ≤1 business day per scenario set. |

## Stress-testing thresholds {#stress-testing-thresholds}

Stress-testing thresholds define the minimum capital and liquidity positions the Bank must maintain under prescribed adverse and severely adverse macro scenarios — covering credit losses, NIM compression, market valuation shocks, and liquidity outflows. Under supervisory stress-testing requirements, threshold breaches in base, adverse, or severe scenarios are typically disclosed in the ICAAP and ILAAP and trigger capital plan remediation. Internal thresholds are typically set above regulatory floors to preserve management buffer ahead of supervisory triggers.

### Stress threshold breach early warning

- URN: urn:financial-services:scenario:strategic-portfolio/risk-appetite/stress-testing-thresholds/stress-threshold-breach-early-warning
- Lens: Insights
- Complexity: S
- Intent: Stress-testing thresholds define the levels at which macro or portfolio deterioration would trigger management action under the Bank's stress framework. Monitoring the trajectory toward these thresholds in continuous form — not just at formal stress test intervals — provides the risk function with an early warning of emerging stress conditions. The AI agent tracks macro and portfolio indicators against stress threshold triggers on a monthly basis.
- Problem to solve: Stress-testing thresholds are reviewed at the formal stress test cycle but are not monitored continuously; macro indicators that are converging toward stress trigger levels are not surfaced to management between formal stress exercises. Early warning signals are missed.
- Solution: The AI agent monitors key macro and portfolio indicators — NPL ratios, GDP growth, interest rate levels, LCR — against the Bank's defined stress threshold triggers on a monthly basis, producing a proximity dashboard with trend velocity signals. Indicators approaching the stress trigger within six months are escalated to the CRO once the risk team has validated the alert.
- OKR: Macro and portfolio indicators approaching stress thresholds are identified and escalated to the CRO at least two months before the threshold is reached, enabling pre-emptive management action.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces monthly stress threshold proximity dashboards for ≥10 consecutive months in the first year. |
| Acceptance | ≥85% of threshold proximity alerts validated by the risk team as accurate; no material stress condition reached without prior early warning from the AI agent. |
| Cycle | Stress threshold early warning lead time extended from formal stress test detection to ≥2-month forward visibility. |

### Stress threshold scenario design automation

- URN: urn:financial-services:scenario:strategic-portfolio/risk-appetite/stress-testing-thresholds/stress-threshold-scenario-design-automation
- Lens: Automation
- Complexity: M
- Intent: Stress scenarios must be tied to specific threshold levels to be actionable; designing the macro pathway from current conditions to each stress threshold requires modeling work that is rarely completed systematically. The AI agent automates the design of stress pathways for each material threshold, producing a scenario narrative and parameter set for the risk team's review.
- Problem to solve: Stress scenario pathways are designed manually for a small subset of thresholds; for most thresholds, the transition path from current conditions to the trigger level is undefined, undermining the credibility of the stress framework with both internal governance and supervisors.
- Solution: The AI agent generates a structured stress pathway for each defined threshold, specifying the macro sequence, time horizon, and portfolio impact, calibrated to the Bank's market. The risk team reviews and approves scenario pathways rather than constructing them.
- OKR: All material stress-testing thresholds are supported by a documented, regulator-credible scenario pathway, produced and maintained on an annual basis.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces stress pathway documentation for ≥90% of material thresholds within the first annual review cycle post-deployment. |
| Acceptance | ≥75% of scenario pathways accepted by the risk team and internal audit without requiring supplementary external modeling. |
| Cycle | Stress pathway documentation time reduced from ≥4 weeks per threshold set to ≤2 weeks for the full threshold library. |

### Stress-Test Results Interpretation and Narrative

- URN: urn:financial-services:scenario:strategic-portfolio/risk-appetite/stress-testing-thresholds/stress-test-results-interpretation
- Lens: Automation
- Complexity: L
- Intent: Stress-test model outputs are read by an AI agent that applies the Bank's standard narrative framework — impact by portfolio, driver identification, comparison to prior runs, and regulatory threshold commentary — producing a results narrative for board and supervisory use.
- Problem to solve: Stress-test results are produced by the risk modeling team and narrated manually by risk seniors. The lag between results availability and decision-ready communication is a consistent bottleneck, and narrative consistency across scenarios depends on the analyst assigned.
- Solution: The AI agent reads stress-test output and produces a structured narrative: impact by portfolio, key driver identification, comparison to prior runs, and regulatory threshold commentary. Risk seniors review and supplement with qualitative judgment before submission.
- OKR: Stress-test model outputs are read by an AI agent and interpreted against the Bank's standard narrative framework — impact by portfolio, driver identification, comparison to prior runs, and regulatory threshold commentary — producing a structured results narrative for board and supervisory use ahead of risk senior review.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces structured stress-test results narratives for 100% of stress scenario submissions; all four narrative dimensions (portfolio impact, key drivers, prior-run comparison, regulatory threshold commentary) included in ≥95% of outputs. |
| Acceptance | ≥80% of AI-produced narratives accepted by risk seniors as the working board/supervisory submission basis without full manual rewrite; driver identification confirmed consistent with model outputs in ≥90% of reviewed narratives. |
| Cycle | Stress-test results-to-decision-ready-narrative lag reduced from several days of manual senior risk authoring to ≤2 business days of AI drafting and risk senior review. |

## Risk capacity {#risk-capacity}

Risk capacity is the maximum risk the Bank can absorb without breaching its viability — determined by its capital base, liquidity resources, earnings generation, and the operating constraints imposed by regulation (minimum capital ratios, LCR, NSFR) and franchise stability considerations. Risk capacity defines the outer boundary within which risk appetite and tolerance levels must be set; the gap between capacity and appetite represents the strategic safety margin the board maintains against severe but plausible stress scenarios.

### Risk capacity continuous assessment

- URN: urn:financial-services:scenario:strategic-portfolio/risk-appetite/risk-capacity/risk-capacity-continuous-assessment-insights
- Lens: Insights
- Complexity: M
- Intent: Risk capacity — the maximum risk the Bank can absorb without breaching regulatory requirements, liquidity thresholds, or viability as a going concern — is the outer boundary that frames the RAS. Continuous assessment of risk capacity requires integrating capital adequacy, liquidity coverage, stress-loss estimates, and earnings volatility into a unified capacity view. The AI agent maintains this integrated view, refreshed monthly, for the CRO and CFO.
- Problem to solve: Risk capacity is assessed formally once or twice a year as part of the ICAAP and recovery planning process; between formal assessments, changes in capital position, liquidity, or macro conditions that affect capacity are not reflected in a single management view. Executives may set risk appetite relative to an outdated capacity estimate.
- Solution: The AI agent integrates capital adequacy, LCR/NSFR, stress-loss estimates, and earnings volatility data on a monthly basis, producing a risk capacity dashboard that shows how much risk budget remains between current appetite and the capacity boundary. Material capacity changes trigger an alert to the CRO and CFO. The CRO team reviews each monthly assessment for accuracy.
- OKR: Risk capacity is assessed and visible to the CRO and CFO on a monthly basis, ensuring risk appetite is always calibrated against a current capacity estimate.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces monthly risk capacity assessments for ≥10 consecutive months in the first year. |
| Acceptance | ≥80% of monthly assessments accepted by the CRO team as accurate and sufficient for appetite calibration purposes. |
| Cycle | Risk capacity visibility cycle compressed from a once- or twice-yearly formal assessment to a monthly read. |

### Risk capacity to appetite gap optimization

- URN: urn:financial-services:scenario:strategic-portfolio/risk-appetite/risk-capacity/risk-capacity-appetite-gap-optimisation
- Lens: Optimize
- Complexity: M
- Intent: The gap between risk capacity and risk appetite determines the Bank's effective risk buffer. A gap that is too large indicates over-capitalization; a gap too narrow leaves insufficient protection. The AI agent models the capacity-to-appetite gap under different capital deployment scenarios, helping the ALCO optimize the deployment of risk capacity while maintaining adequate safety margins.
- Problem to solve: Capacity-to-appetite gap analysis is performed as part of the annual ICAAP review; intra-year capital deployment decisions are not assessed against their impact on the gap, potentially allowing the buffer to narrow without management awareness.
- Solution: The AI agent maintains a continuous view of the capacity-to-appetite gap and models the impact of proposed capital deployment decisions on the gap. Scenarios that reduce the buffer below the internal operating threshold are flagged for ALCO review before the decision is finalized. The ALCO secretariat checks each assessment.
- OKR: ALCO capital deployment decisions are assessed against their impact on the capacity-to-appetite gap before approval, ensuring the buffer remains within the board-set operating range.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's gap-impact assessment used in ≥80% of material capital deployment decisions reviewed by ALCO within 12 months. |
| Acceptance | ≥80% of gap-impact assessments accepted by the ALCO secretariat as accurate and sufficient for deliberation. |
| Cycle | Gap-impact assessment production time reduced from ≥3 days of manual modeling to ≤4 hours on demand. |

### Risk capacity recovery scenario automation

- URN: urn:financial-services:scenario:strategic-portfolio/risk-appetite/risk-capacity/risk-capacity-recovery-scenario-automation
- Lens: Automation
- Complexity: L
- Intent: Recovery planning requires a bank to model scenarios in which risk capacity is severely stressed and demonstrate that recovery options — capital raising, asset disposals, liability management — can restore it to viability. The AI agent automates the production of recovery scenario packs from structured inputs, accelerating the annual recovery planning cycle.
- Problem to solve: Recovery scenario modeling is labor-intensive, requiring the risk, finance, and treasury teams to collaborate over six to eight weeks; the process limits the number of scenarios that can be modeled and increases the risk of late submission to the regulator.
- Solution: The AI agent generates recovery scenario packs from structured scenario parameters, modeling the capital and liquidity trajectory under each scenario and the effectiveness of defined recovery options. The risk team reviews and validates scenario outputs rather than building models from scratch.
- OKR: Recovery scenario packs are produced within three weeks of the scenario design sign-off, compressing the annual recovery planning timeline by at least two weeks.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces recovery scenario packs for 100% of annual recovery planning cycles from deployment. |
| Acceptance | ≥75% of scenario packs accepted by the risk team without major model rework; regulatory submission made on schedule. |
| Cycle | Recovery scenario pack production time reduced from 6–8 weeks to ≤3 weeks from scenario design sign-off. |

## Risk-adjusted performance metrics {#risk-adjusted-performance-metrics}

Risk-adjusted performance metrics — principally RAROC (Risk-Adjusted Return on Capital), RORAC, and EVA (economic value added) — convert business line and product-level revenue and loss estimates into a capital-efficiency measure comparable across different risk profiles. These metrics govern pricing floors, capital allocation decisions, and performance appraisal by ensuring that reported returns incorporate the cost of the regulatory and economic capital consumed, aligning business incentives with the Bank's overall risk-adjusted return target.

### RAROC continuous BU performance insights

- URN: urn:financial-services:scenario:strategic-portfolio/risk-appetite/risk-adjusted-performance-metrics/raroc-continuous-bu-performance-insights
- Lens: Insights
- Complexity: M
- Intent: RAROC and EVA at the business-unit level are the primary metrics for assessing whether each BU generates returns above the cost of capital on a risk-adjusted basis. The AI agent maintains a RAROC read per BU, refreshed monthly, incorporating updated expected loss, capital consumption, and revenue data, giving the executive committee a current view of value creation and destruction across the portfolio.
- Problem to solve: RAROC is calculated quarterly as part of the management accounts cycle; between quarters, BU heads and the CFO lack a current read of risk-adjusted performance. Strategic decisions on capital reallocation are made without up-to-date RAROC data.
- Solution: The AI agent integrates revenue, expected loss, capital consumption, and cost data per BU on a monthly basis, producing a RAROC and EVA dashboard with trend signals. BUs with deteriorating RAROC trends are flagged for executive committee attention with a brief diagnostic note. The CFO team reviews each dashboard for accuracy.
- OKR: RAROC and EVA are visible per BU on a monthly basis, enabling capital reallocation decisions grounded in current risk-adjusted performance data.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces monthly RAROC dashboards covering ≥90% of strategic BUs from deployment. |
| Acceptance | ≥80% of monthly dashboards accepted by the CFO team as accurate and sufficient for performance review without major rework. |
| Cycle | RAROC visibility cycle compressed from quarterly production to a monthly read. |

### Self-service RAROC sensitivity tool

- URN: urn:financial-services:scenario:strategic-portfolio/risk-appetite/risk-adjusted-performance-metrics/risk-adjusted-metrics-enablement-tool
- Lens: Enablement
- Complexity: M
- Intent: BU heads and product managers need to understand how pricing, volume, and credit quality decisions affect RAROC before they are made — not after. The AI agent provides a self-service RAROC sensitivity tool that allows business managers to model the risk-adjusted impact of deal-level or portfolio-level decisions without requiring finance team support for every query.
- Problem to solve: RAROC modeling is centralized in the finance team; BU heads must submit requests and wait days for outputs. This bottleneck discourages routine use of RAROC as a decision tool and leads to pricing and underwriting decisions made without explicit risk-adjusted consideration.
- Solution: The AI agent provides a conversational RAROC sensitivity interface for BU heads and product managers, accepting deal parameters or portfolio assumptions and returning RAROC, EVA, and capital consumption estimates with sensitivity ranges. Finance team approval is required only for outputs used in board submissions.
- OKR: BU heads and product managers have self-service access to RAROC modeling, reducing the finance team bottleneck and increasing the share of business decisions informed by risk-adjusted metrics.

| Dimension | Key result |
| --- | --- |
| Adoption | Self-service RAROC tool used for ≥50 distinct queries per month by BU heads and product managers within 12 months of deployment. |
| Acceptance | ≥75% of self-service queries rated as useful and accurate by the requesting business manager; finance team override rate ≤15%. |
| Cycle | RAROC sensitivity query turnaround time reduced from ≥2 analyst days to ≤30 minutes via self-service tool. |

### Risk-adjusted performance reporting automation

- URN: urn:financial-services:scenario:strategic-portfolio/risk-appetite/risk-adjusted-performance-metrics/risk-adjusted-performance-reporting-automation
- Lens: Automation
- Complexity: M
- Intent: Quarterly risk-adjusted performance reports — RAROC attribution, EVA bridge, capital consumption by risk type — require significant manual assembly from multiple source systems. The AI agent automates the end-to-end production of the quarterly risk-adjusted performance pack, from data extraction through attribution to narrative commentary.
- Problem to solve: The quarterly RAROC and EVA report is assembled manually by the finance and risk teams over two to three weeks; the process is error-prone, requires multiple reconciliation rounds, and often delivers the report after the key executive review meetings.
- Solution: The AI agent automates data extraction from risk, capital, and revenue systems, runs the RAROC and EVA attribution, and produces a complete quarterly pack with BU-level dashboard, attribution waterfall, and narrative commentary. The finance and risk teams review and approve the pack rather than constructing it.
- OKR: The quarterly risk-adjusted performance pack is available within five business days of the reporting period data freeze, enabling timely executive review.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces risk-adjusted performance packs for 100% of quarterly reporting cycles from deployment. |
| Acceptance | ≥80% of packs accepted by the finance and risk teams without major rework; pack delivery date consistently before the executive committee review meeting. |
| Cycle | Quarterly pack production time reduced from 2–3 weeks to ≤5 business days. |
