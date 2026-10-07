# Capital allocation

Capital allocation governs how the Bank deploys regulatory and economic capital across business lines — ensuring adequate Tier 1 and Tier 2 capital, meeting buffer requirements (CCB, SIFI, countercyclical), and producing ICAAP-ready disclosures. **The opportunity for GenAI is to compress the production cycle of capital metrics, attribution, and narrative** — turning a quarterly assembly exercise into continuous forward visibility.

## Problems

### Capital allocation {#capital-allocation}

| Lens | Problem |
| --- | --- |
| Insights & analytics | Tier 1 and Tier 2 headroom, the total capital ratio, and buffer consumption are calculated in monthly and quarterly production runs by the capital reporting team. Between runs, RWA movements, earnings events, and instrument amortization are not reflected, so the CFO and ALCO may decide on a stale capital picture. |
| Enablement | ICAAP stress-scenario design and capital-plan sensitivities depend on a few senior risk officers and planning analysts. Scenarios are reused across years with minor adjustments, and only two or three combinations are modeled before each review. |
| Automation | Tier 2 eligibility tables, RWA driver attribution, buffer-change impact briefings, and the ICAAP narrative are assembled by hand each cycle from treasury, finance, and risk sub-ledgers. The formats are prescribed and the sources known, yet each pack takes days to weeks and several reconciliation rounds. |
| New business opportunities | Capital allocation across business lines is set annually, and reallocation requests are evaluated ad hoc in bespoke spreadsheets. With reallocation candidates surfaced weekly and ranked by expected RAROC improvement, the Executive Committee can move capital toward emerging segments within the quarter instead of at the next annual cycle. |

## Tier 1 capital {#tier-1-capital}

Tier 1 capital — comprising Common Equity Tier 1 (CET1) and, where the Bank issues them, Additional Tier 1 (AT1) instruments — is the primary loss-absorbing layer of the Bank's regulatory capital stack, measured against risk-weighted assets to produce the CET1 and Tier 1 ratios defined under Basel III and required by the regulator's capital adequacy framework. Tier 1 capital planning covers retained earnings forecasts, dividend policy, capital instrument issuance, and deduction items (goodwill, deferred tax assets) that affect the ratio in each planning horizon.

### Tier 1 issuance window monitor

- URN: urn:financial-services:scenario:strategic-portfolio/capital-allocation/tier-1-capital/tier-1-issuance-window-monitor
- Lens: Automation
- Complexity: S
- Intent: Where the Bank issues AT1 or CET1 instruments in the market, issuance windows are constrained by market conditions, regulatory quiet periods, and the Bank's own capital trajectory. The AI agent monitors market spread conditions, peer issuance activity, and the Bank's CET1 headroom to flag optimal issuance windows and trigger the pre-issuance preparation checklist.
- Problem to solve: Treasury and capital management teams track issuance conditions manually from market data subscriptions and peer announcements; window identification is reactive and preparation lead time is often insufficient to capture favorable conditions.
- Solution: The AI agent aggregates AT1 spread data, peer issuance calendars, regulatory quiet period schedules, and the Bank's capital trajectory to produce a weekly issuance readiness signal. When conditions cross the pre-defined threshold, the AI agent triggers the preparation workflow; treasury validates each signal as timely and actionable.
- OKR: Treasury initiates capital issuance preparation at least two weeks before optimal market windows close, based on AI-generated readiness signals.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces weekly issuance readiness signals for ≥48 of 52 weeks in the first year of operation. |
| Acceptance | ≥80% of window signals validated by treasury as timely and actionable; no material issuance missed due to preparation lag. |
| Cycle | Window identification to preparation initiation reduced from ≥5 days to same-day trigger. |

### Tier 1 Ratio Variance Attribution

- URN: urn:financial-services:scenario:strategic-portfolio/capital-allocation/tier-1-capital/tier-1-ratio-variance-attribution
- Lens: Insights
- Complexity: M
- Intent: Monthly Tier 1 ratio variance is attributed by driver category — RWA growth, retained earnings, AT1 movements where the Bank has such instruments, model-parameter changes — and drafted as a ranked CFO narrative from sub-ledger feeds. The attribution is available within the reporting cycle.
- Problem to solve: The CFO's monthly Tier 1 commentary requires manual triangulation across treasury, finance, and risk sub-ledgers. Identifying which factor dominated is a multi-day exercise per cycle, and narrative consistency across analysts is not assured.
- Solution: The AI agent reads sub-ledger movements, classifies each into Tier 1 driver categories, and produces a draft narrative ranked by materiality. The CFO reviews the generated attribution and adjusts forward-looking framing before sign-off.
- OKR: Monthly Tier 1 ratio variance is attributed by driver category — RWA growth, retained earnings, AT1 movements, model-parameter changes — and drafted as a ranked CFO narrative from sub-ledger feeds within the reporting cycle, replacing the multi-day manual triangulation across treasury, finance, and risk systems.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces monthly Tier 1 variance attribution narratives for ≥11 calendar months per year; all four driver categories ranked by materiality and included in ≥95% of monthly outputs. |
| Acceptance | ≥85% of AI-produced attributions accepted by the CFO as analytically accurate without requiring re-derivation; driver classification confirmed consistent with treasury and risk source data in ≥90% of reviewed months. |
| Cycle | Monthly Tier 1 attribution cycle reduced from a multi-day manual triangulation across sub-ledgers to ≤1 business day of AI agent production and CFO framing review. |

### Tier 1 capital plan sensitivity analysis

- URN: urn:financial-services:scenario:strategic-portfolio/capital-allocation/tier-1-capital/tier-1-capital-plan-sensitivity
- Lens: Optimize
- Complexity: M
- Intent: The Bank's capital plan for CET1 and, where it issues them, AT1 instruments must remain robust across a range of earnings, RWA, and dividend scenarios. The AI agent runs multi-period sensitivity analyses against the capital plan, quantifying the impact of earnings shortfalls, RWA inflation, and dividend commitments on projected Tier 1 ratios over the planning horizon.
- Problem to solve: Capital plan sensitivities are produced once at plan inception and rarely updated intra-year; when macro conditions shift, the plan's resilience is unknown until the next formal review. Stress scenarios are limited to the two or three combinations modeled by the planning team.
- Solution: The AI agent runs a continuous sensitivity grid over the capital plan, updating projections as earnings actuals, RWA movements, and macro inputs are refreshed. The capital planning team reviews each weekly sensitivity summary, and the CFO office receives it showing Tier 1 ratio trajectory under base, downside, and adverse assumptions.
- OKR: Tier 1 capital plan sensitivity is visible to the CFO office on a weekly basis, covering at least five earnings and RWA scenario combinations at all times.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces weekly sensitivity updates for ≥80% of weeks in the 12-month post-deployment period. |
| Acceptance | ≥80% of weekly sensitivity outputs accepted by the capital planning team without material re-derivation. |
| Cycle | Time to produce an updated Tier 1 sensitivity grid reduced from ≥2 days of analyst time to ≤2 hours. |

## Capital allocation by business line {#capital-allocation-by-business-line}

Distribution of regulatory and economic capital across the Bank's business lines — Retail, Corporate, Treasury, fee-income units and, where the Bank has one, Private Banking — in proportion to risk-weighted assets, RAROC hurdles, and strategic growth mandates set by the Capital Committee. The allocation governs each business line's lending capacity, balance-sheet headroom, and performance measurement under risk-adjusted return frameworks.

### RAROC Narrative per Business Line

- URN: urn:financial-services:scenario:strategic-portfolio/capital-allocation/capital-allocation-by-business-line/raroc-narrative-per-bu
- Lens: Insights
- Complexity: M
- Intent: Per-BU RAROC, economic profit, and capital-utilization narrative is auto-drafted from finance and risk feeds on a quarterly cadence. Cross-BU comparison is rendered with driver decomposition for CFO sign-off at each performance review.
- Problem to solve: Quarterly performance review across business lines requires assembling RAROC, capital usage, and economic profit from separate finance and risk systems. Cross-BU comparison depends on individual analysts, and methodology consistency varies by cycle.
- Solution: The AI agent reads BU-level risk-weighted assets, expected loss, and P&L from current feeds and produces a per-BU narrative with driver decomposition. Cross-BU ranking is auto-generated. The CFO reviews, adjusts judgment calls, and signs off.
- OKR: Per-BU RAROC, economic profit, and capital-utilization narrative with driver decomposition is auto-drafted from finance and risk feeds on a quarterly cadence, giving the CFO a structured cross-BU comparison and sign-off task rather than a multi-system manual assembly exercise.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces per-BU RAROC narratives for 100% of quarterly performance review cycles; cross-BU ranking and driver decomposition included in ≥95% of quarterly outputs. |
| Acceptance | ≥85% of AI-produced narratives accepted by the CFO as accurate without material re-derivation; RAROC calculation consistency confirmed against risk system source data in ≥90% of reviewed cycles. |
| Cycle | Quarterly RAROC narrative assembly cycle reduced from multi-system manual data triangulation spanning several days to ≤2 business days post-close. |

### BU capital reallocation scenario engine

- URN: urn:financial-services:scenario:strategic-portfolio/capital-allocation/capital-allocation-by-business-line/bu-capital-reallocation-scenario-engine
- Lens: Optimize
- Complexity: M
- Intent: Business-line capital allocation is refreshed quarterly, but intra-quarter performance divergence — margin compression in one BU, credit outperformance in another — creates misallocation that persists until the next cycle. The AI agent models reallocation scenarios against RAROC hurdles, capital constraints, and regulatory floors, allowing the CFO office to test and rank alternatives before the next ALCO. Each scenario carries a capital release or consumption estimate alongside P&L sensitivity.
- Problem to solve: Capital reallocation requests from BU heads are evaluated ad hoc by finance teams using bespoke spreadsheets; scenarios are not standardized, assumptions diverge, and the CFO office cannot compare options on a common basis. Reallocation decisions therefore lag the underlying performance signal by one or more quarters.
- Solution: The AI agent parameterizes reallocation scenarios from BU inputs and enterprise constraints, scores each against RAROC, CET1 headroom, and concentration limits, and ranks alternatives with a narrative rationale. The CFO office reviews ranked outputs rather than assembling them.
- OKR: The CFO office evaluates capital reallocation options on a standardized, scenario-ranked basis within days of a performance trigger.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent is used for ≥80% of intra-quarter capital reallocation analyses within 12 months of go-live. |
| Acceptance | ≥75% of scenario outputs accepted by the CFO office as analytically sound without material re-derivation. |
| Cycle | Time from reallocation request to ranked scenario pack reduced from ≥5 days to ≤1 business day. |

### Dynamic Capital Reallocation Across Business Lines

- URN: urn:financial-services:scenario:strategic-portfolio/capital-allocation/capital-allocation-by-business-line/dynamic-bu-reallocation
- Lens: New opps
- Complexity: XL
- Intent: Continuous monitoring of segment performance signals against capital adequacy headroom surfaces reallocation candidates weekly. Capital allocation shifts from an annual exercise to a standing Executive Committee agenda item.
- Problem to solve: Capital allocation across business lines is set annually. Emerging-segment opportunities and struggling-segment risks wait up to twelve months for a capital response, and competitors with faster allocation cycles capture intervening upside.
- Solution: The AI agent monitors segment performance and capital headroom on a continuous basis, surfacing reallocation candidates weekly with capital-impact estimates and ranking by expected RAROC improvement. The decision rests with the Executive Committee on a defined weekly cadence.
- OKR: Continuous monitoring of segment performance signals against capital adequacy headroom surfaces reallocation candidates weekly with capital-impact estimates and RAROC improvement rankings — shifting capital allocation from an annual exercise to a standing Executive Committee agenda item.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent monitors segment performance and capital headroom signals weekly for ≥48 consecutive weeks per year; reallocation candidates with capital-impact estimates presented at ≥90% of scheduled weekly Executive Committee (EC) sessions. |
| Acceptance | ≥75% of AI-surfaced reallocation candidates rated as actionable by the EC; RAROC improvement ranking methodology confirmed as consistent by the CFO office in ≥90% of reviewed outputs. |
| Cycle | Capital reallocation decision cycle reduced from an annual process to a standing weekly EC agenda item, with the first reallocation decision enabled within 90 days of go-live. |

## Tier 2 capital {#tier-2-capital}

Tier 2 capital — subordinated debt and eligible provisions — supplements Tier 1 as the secondary loss-absorbing layer and determines the Total Capital Ratio headroom above the Tier 1 floor. Tier 2 instrument management covers issuance and maturity scheduling, call-option exercise decisions, and the interaction between general provisions and regulatory Tier 2 eligibility limits under the regulator's capital adequacy rules.

### Tier 2 instrument adequacy monitor

- URN: urn:financial-services:scenario:strategic-portfolio/capital-allocation/tier-2-capital/tier-2-instrument-adequacy-insights
- Lens: Insights
- Complexity: S
- Intent: Tier 2 capital — subordinated debt, general provisions, and revaluation reserves — must meet prescribed limits relative to Tier 1 and total capital. The AI agent tracks Tier 2 instrument balances, amortization schedules, and headroom against Basel III limits, producing a continuous adequacy read for the capital management desk.
- Problem to solve: Tier 2 adequacy is reviewed monthly as part of the capital reporting cycle; amortization-driven erosion of Tier 2 headroom is not visible between cycles, and the capital management desk may miss optimal refinancing windows for maturing subordinated instruments.
- Solution: The AI agent maintains a live Tier 2 instrument register, projects forward balances allowing for amortization, and flags headroom compression and upcoming maturity events. A weekly summary reaches the capital management desk and treasury.
- OKR: Tier 2 headroom and instrument maturity events are visible on a continuous basis, with alerts reaching the capital management desk at least 90 days before a material maturity.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces weekly Tier 2 adequacy summaries for ≥48 of 52 weeks in the first year. |
| Acceptance | ≥90% of instrument balance estimates validated against month-end actuals within ±2% tolerance. |
| Cycle | Maturity alert lead time extended from 30-day reactive identification to ≥90-day forward visibility. |

### Tier 2 regulatory limit tracking

- URN: urn:financial-services:scenario:strategic-portfolio/capital-allocation/tier-2-capital/tier-2-regulatory-limit-tracking
- Lens: Automation
- Complexity: S
- Intent: Basel III caps Tier 2 capital eligible for inclusion in total capital; breaching these limits requires the excess to be deducted. The AI agent automates the calculation and tracking of Tier 2 eligibility limits, flagging excess positions and producing the regulatory disclosure tables for quarterly capital reporting.
- Problem to solve: Tier 2 limit calculations are performed manually each quarter as part of the capital reporting pack; the calculation is error-prone and requires reconciliation between the capital team and finance. Limit breaches discovered late in the reporting cycle delay submission.
- Solution: The AI agent automates the end-to-end Tier 2 eligibility calculation each quarter, including haircuts, amortization adjustments, and the Tier 1 cap. The output is a disclosure table, verified by the capital team, ready for insertion into the regulatory capital report, with any limit breaches flagged for management action.
- OKR: Tier 2 eligibility calculations are produced automatically each quarter, eliminating manual reconstruction and reducing error risk.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces Tier 2 eligibility tables for 100% of quarterly capital reporting cycles from deployment. |
| Acceptance | ≥95% of automated calculations match manual verification within ±0.01% tolerance; zero late-cycle limit-breach discoveries. |
| Cycle | Tier 2 calculation time within the quarterly reporting cycle reduced from ≥2 days to ≤4 hours. |

### Tier 2 refinancing scenario pack

- URN: urn:financial-services:scenario:strategic-portfolio/capital-allocation/tier-2-capital/tier-2-refinancing-scenario-pack
- Lens: Optimize
- Complexity: M
- Intent: Refinancing maturing Tier 2 instruments requires scenario analysis across issuance size, tenor, coupon, and the resulting impact on total capital ratio and cost of capital. The AI agent models refinancing options ahead of maturity events, producing a ranked scenario pack for the ALCO and board risk committee.
- Problem to solve: Tier 2 refinancing analysis is prepared ad hoc as instruments approach maturity, typically leaving insufficient lead time for optimal market timing. The analysis is not standardized, making it difficult to compare options across different instruments or issuance structures.
- Solution: The AI agent runs a structured refinancing scenario pack for each maturing Tier 2 instrument 12 months in advance, covering size, tenor, and structure variants. Each scenario includes post-issuance total capital ratio, cost impact, and headroom against Basel III limits. Treasury and capital management review the pack before ALCO deliberation.
- OKR: Tier 2 refinancing decisions are supported by a standardized scenario pack produced at least 12 months before maturity.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces refinancing scenario packs for 100% of Tier 2 instruments with maturities within the 18-month horizon. |
| Acceptance | ≥75% of scenario packs accepted by treasury and capital management as the basis for ALCO deliberation without major rework. |
| Cycle | Refinancing scenario pack preparation time reduced from ≥5 days to ≤1 business day. |

## ICAAP {#icaap}

The Internal Capital Adequacy Assessment Process (ICAAP) is the Bank's own forward-looking assessment of capital sufficiency under its risk profile, stress scenarios, and strategic plan — covering Pillar 2 risks not fully captured under Pillar 1 (concentration risk, pension risk, interest rate risk in the banking book). Typically submitted annually to the regulator as a supervisory review document under Pillar 2, the ICAAP requires cross-functional data assembly across finance, risk, and treasury, with narrative synthesis of scenario results and management actions.

### ICAAP capital adequacy insights pack

- URN: urn:financial-services:scenario:strategic-portfolio/capital-allocation/icaap/icaap-capital-adequacy-insights-pack
- Lens: Insights
- Complexity: M
- Intent: The ICAAP requires the Bank to demonstrate that its internal capital assessment captures all material risks and that the capital plan is adequate under stress. The AI agent synthesizes risk-by-risk capital consumption data into a continuous adequacy view, surfacing emerging gaps between Pillar 1 and Pillar 2 capital requirements before the annual ICAAP submission cycle begins.
- Problem to solve: ICAAP adequacy analysis is assembled annually from inputs across credit, market, operational, liquidity, and concentration risk teams; the assembly takes six to eight weeks and reflects a backward-looking picture by the time it reaches the regulator. Intra-year capital deterioration is not visible in the ICAAP narrative.
- Solution: The AI agent aggregates risk-capital consumption across all material risk categories on a monthly basis, tracks it against ICAAP-stated capital supply, and flags emerging adequacy gaps. The capital team validates each monthly snapshot, and the output feeds directly into the ICAAP drafting process, compressing the annual assembly cycle.
- OKR: ICAAP adequacy gaps are visible to the capital team on a monthly basis and the annual submission cycle starts from a continuously maintained dataset rather than a point-in-time assembly.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces monthly ICAAP adequacy snapshots for ≥10 consecutive months within the first year. |
| Acceptance | ≥85% of monthly snapshots validated by the capital team as consistent with underlying risk-capital data without material rework. |
| Cycle | Annual ICAAP assembly timeline reduced by ≥4 weeks due to availability of the continuous adequacy dataset. |

### ICAAP stress scenario design support

- URN: urn:financial-services:scenario:strategic-portfolio/capital-allocation/icaap/icaap-stress-scenario-design-support
- Lens: Enablement
- Complexity: M
- Intent: ICAAP stress scenarios must be severe but plausible, calibrated to the Bank's specific risk profile and the macroeconomic context of its market. The AI agent assists scenario design teams by generating candidate scenarios grounded in historical stress episodes, BCBS guidance, and current macro conditions in the domestic and regional markets.
- Problem to solve: Stress scenario design relies on senior risk officers with limited time; scenarios are often reused across years with minor adjustments, reducing their credibility with supervisors. Generating genuinely novel, market-specific scenarios requires research and calibration capacity that is rarely available.
- Solution: The AI agent synthesizes macro data, supervisory guidance, and historical stress episodes to generate candidate ICAAP stress scenarios with narrative rationale and initial macro-financial parameter ranges. Risk teams select and calibrate from the candidate set rather than designing from a blank page.
- OKR: Risk teams design ICAAP stress scenarios from a structured candidate set that covers the Bank's material risk factors in its market.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-generated candidate scenarios used as the starting point for ≥80% of ICAAP stress scenario design sessions. |
| Acceptance | ≥70% of AI-proposed scenario candidates retained by risk teams (in whole or adapted form) in the final ICAAP submission. |
| Cycle | Stress scenario design phase of ICAAP production reduced from ≥4 weeks to ≤2 weeks. |

### ICAAP narrative drafting

- URN: urn:financial-services:scenario:strategic-portfolio/capital-allocation/icaap/icaap-narrative-drafting-automation
- Lens: Automation
- Complexity: L
- Intent: The ICAAP document requires board-grade narrative connecting the Bank's risk profile, stress test results, and capital adequacy conclusion — a drafting exercise that consumes significant senior resource. The AI agent drafts each section from structured inputs (risk capital data, stress results, capital plan) in supervisory-standard language, leaving reviewers to verify substance rather than construct prose.
- Problem to solve: ICAAP narrative drafting is distributed across risk, finance, and compliance authors who work from separate templates; the resulting document requires multiple reconciliation rounds before it achieves coherent narrative. Drafting typically consumes six to eight weeks of senior analyst time.
- Solution: The AI agent ingests structured inputs per ICAAP section — risk register, stress results, capital position, management actions — and produces a complete first-draft document in the regulator's supervisory format. Section authors review and amend rather than drafting from scratch.
- OKR: A complete ICAAP first draft is available to section authors within two weeks of input data freeze, cutting total drafting time by half.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent is used to produce the first-draft ICAAP narrative for 100% of annual ICAAP submissions from year 1 of deployment. |
| Acceptance | ≥75% of drafted sections accepted by section authors without structural revision; supervisor challenge rate no higher than prior-year baseline. |
| Cycle | Time from data freeze to approved ICAAP draft reduced from 6–8 weeks to ≤3 weeks. |

## Total capital ratio {#total-capital-ratio}

The Total Capital Ratio — Tier 1 plus Tier 2 capital over total risk-weighted assets — is the headline capital adequacy measure reported to the regulator, disclosed to investors, and monitored by the board against internal target ranges and minimum supervisory floors. Total Capital Ratio trajectory is the output metric that integrates capital generation, RWA growth, buffer consumption, and instrument issuance across all capital planning workstreams.

### Total capital ratio continuous dashboard

- URN: urn:financial-services:scenario:strategic-portfolio/capital-allocation/total-capital-ratio/total-capital-ratio-continuous-dashboard
- Lens: Insights
- Complexity: S
- Intent: The total capital ratio (TCR) is the primary solvency signal for the regulator, rating agencies, and senior management. The AI agent maintains a continuously refreshed TCR read from daily RWA feeds, capital instrument balances, and retained earnings estimates, giving the CFO a live picture of distance to the regulatory minimum and internal operating floor.
- Problem to solve: TCR is typically reported quarterly to the regulator and calculated monthly for internal management; between production runs, material RWA movements or earnings events are not reflected in the capital adequacy picture. Management decisions in ALCO or the Executive Committee may be made on a stale TCR.
- Solution: The AI agent integrates daily RWA estimates, capital instrument registers, and earnings accrual data to produce a continuously updated TCR alongside Tier 1, CET1, and leverage ratio. The dashboard is accessible to the CFO, ALCO secretary, and capital management desk at all times.
- OKR: The CFO and ALCO have continuous access to a TCR read updated within one business day of a material RWA or capital event.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces daily TCR updates for ≥95% of business days within six months of deployment. |
| Acceptance | ≥90% of daily TCR estimates fall within ±10 bps of month-end actuals; the CFO office adopts the dashboard as its primary intra-month capital monitor. |
| Cycle | Capital adequacy visibility cycle compressed from monthly production to daily refresh. |

### TCR RWA driver attribution

- URN: urn:financial-services:scenario:strategic-portfolio/capital-allocation/total-capital-ratio/total-capital-ratio-rwa-driver-attribution
- Lens: Automation
- Complexity: M
- Intent: When the TCR moves, management needs to know which RWA drivers — credit, market, operational, or CVA — are responsible and which business lines drove the change. The AI agent automates period-over-period RWA attribution, decomposing TCR movements into their constituent drivers and producing an ALCO-ready attribution narrative.
- Problem to solve: RWA attribution is a manual analyst task performed quarterly; it takes three to four days and is often incomplete by the time the ALCO pack is finalized. Without a clean attribution, ALCO cannot target corrective actions to the right business line.
- Solution: The AI agent runs a structured RWA attribution each period, decomposing TCR movement into credit, market, operational, and CVA components at BU level, and generates a narrative ALCO briefing. The capital team reviews the attribution output, which is produced within one business day of the RWA data freeze.
- OKR: TCR movements are attributed to constituent RWA drivers at BU level and available to ALCO within one business day of each data freeze.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces RWA attribution packs for ≥90% of quarterly ALCO cycles from deployment. |
| Acceptance | ≥85% of attribution packs accepted by the capital team without material revision; attribution narrative adopted in ≥80% of ALCO packs. |
| Cycle | Attribution preparation time reduced from 3–4 analyst days to ≤1 business day. |

### TCR forecast and threshold alert

- URN: urn:financial-services:scenario:strategic-portfolio/capital-allocation/total-capital-ratio/total-capital-ratio-forecast-alert
- Lens: Optimize
- Complexity: M
- Intent: Proactive capital management requires a forward view of where the TCR will land at quarter-end under current trajectory and alternative scenarios. The AI agent maintains a rolling 90-day TCR forecast, updates it weekly as actuals emerge, and alerts the capital management desk when the projected ratio approaches the internal operating floor.
- Problem to solve: Capital planning teams produce point-in-time TCR forecasts at quarter start but do not update them systematically as actuals deviate from plan. By the time a TCR breach risk is identified, the response window is often inadequate.
- Solution: The AI agent maintains a rolling 90-day TCR forecast using current RWA trajectory, earnings run-rate, and capital plan assumptions. The forecast is updated weekly; a configurable alert fires when the projected quarter-end ratio is within 50 bps of the internal operating floor.
- OKR: The capital management desk has a continuously maintained 90-day TCR forecast with threshold alerts that trigger at least four weeks before a potential floor breach.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces weekly TCR forecast updates for ≥80% of weeks in the 12-month post-deployment period. |
| Acceptance | ≥85% of quarter-end TCR forecasts fall within ±15 bps of the actual quarter-end TCR; no floor breach occurs without a prior alert after deployment. |
| Cycle | Forecast refresh cycle compressed from quarterly point-in-time to weekly rolling update. |

## Capital buffers (CCB, SIFI, countercyclical) {#capital-buffers}

Management of the three Basel III capital buffer layers — Capital Conservation Buffer (CCB), SIFI surcharge where applicable, and the countercyclical capital buffer (CCyB) activated by the macroprudential authority — above the minimum Tier 1 and Total Capital Ratio floors. Buffer consumption and headroom are monitored continuously against regulatory thresholds, with breach-proximity triggers requiring board notification and dividend restriction assessment under the regulator's capital adequacy rules.

### Capital buffer headroom monitor

- URN: urn:financial-services:scenario:strategic-portfolio/capital-allocation/capital-buffers/capital-buffer-headroom-continuous-monitor
- Lens: Insights
- Complexity: S
- Intent: CCB, SIFI surcharge (where it applies), and countercyclical buffer (CCyB) requirements change with macro and supervisory conditions; headroom against each buffer must be monitored continuously to avoid breaching combined buffer requirements. The AI agent maintains a live read of buffer consumption across each applicable component, flags headroom compression, and quantifies the distance to the regulatory floor in capital terms.
- Problem to solve: Buffer headroom is calculated monthly by the capital reporting team; intra-month deterioration in RWA or retained earnings is invisible until the next production run. Supervisors commonly expect management to evidence ongoing awareness of buffer adequacy, not just point-in-time disclosure.
- Solution: The AI agent integrates daily RWA feeds, retained earnings estimates, and published buffer rates to produce a continuously refreshed buffer-headroom dashboard. Threshold breaches trigger automated alerts to the capital management desk and CFO office.
- OKR: Buffer headroom is visible in continuous form, with threshold alerts reaching the capital management desk before end-of-day on the trigger date.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces daily buffer-headroom updates for ≥95% of trading days within six months of deployment. |
| Acceptance | ≥90% of headroom estimates validated against month-end production figures within a ±5 bps tolerance. |
| Cycle | Headroom alert latency reduced from monthly production cycle to same-day trigger detection. |

### Buffer requirement change briefing

- URN: urn:financial-services:scenario:strategic-portfolio/capital-allocation/capital-buffers/capital-buffer-requirement-change-briefing
- Lens: Automation
- Complexity: S
- Intent: Supervisory changes to CCyB rates and SIFI surcharge tiers require rapid assessment of their capital impact and board communication. The AI agent monitors published announcements from the regulator and BCBS, quantifies the incremental capital requirement, and produces a board-ready impact briefing.
- Problem to solve: When a CCyB rate is raised or a SIFI designation changes, the capital team must manually translate the announcement into an impact estimate, draft a briefing, and circulate it — a process that typically takes two to three days. During that window, senior management is operating without a quantified view.
- Solution: The AI agent detects regulatory announcements via structured supervisory feeds, applies current RWA and capital base to compute the incremental buffer requirement, and drafts a two-page impact briefing for the CFO and board risk committee. The capital team reviews and approves before circulation.
- OKR: Impact briefings for buffer-requirement changes are available to the CFO office within four hours of the supervisory announcement.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces impact briefings for ≥90% of material CCyB or SIFI surcharge changes within the first year. |
| Acceptance | ≥80% of briefings accepted by the capital team without material amendment to impact estimates or narrative. |
| Cycle | Briefing production time reduced from 2–3 days of manual assembly to ≤4 hours from announcement to draft. |

### Buffer optimization scenario

- URN: urn:financial-services:scenario:strategic-portfolio/capital-allocation/capital-buffers/capital-buffer-optimisation-scenario
- Lens: Optimize
- Complexity: M
- Intent: Maintaining excess buffers above regulatory minima has an opportunity cost; holding too little creates supervisory risk. The AI agent models the cost-benefit of different buffer level strategies — including dividend policy and, where the Bank issues such instruments, AT1 issuance options — against the Bank's capital plan horizon, yielding a buffer-level recommendation for the ALCO.
- Problem to solve: Buffer calibration decisions are made judgmentally at ALCO with limited scenario analysis; the trade-off between capital efficiency and regulatory safety margin is not formally modeled. This creates both over-capitalization risk and last-minute capital actions when buffers compress unexpectedly.
- Solution: The AI agent runs multi-period buffer scenarios against the capital plan, testing dividend, buyback, and AT1 issuance levers under base and stress assumptions. The output is an ALCO-ready scenario table with a recommended buffer range and sensitivities; the buffer-level decision rests with ALCO.
- OKR: ALCO buffer-level decisions are supported by a formal scenario analysis covering at least three strategic levers.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced buffer scenarios used in ≥80% of ALCO capital sessions within 12 months of deployment. |
| Acceptance | ≥75% of scenario outputs adopted as the basis for ALCO deliberation without material re-work. |
| Cycle | Buffer scenario pack preparation time reduced from ≥3 days to ≤4 hours ahead of each ALCO. |
