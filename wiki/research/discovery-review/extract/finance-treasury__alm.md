# 

source: html-alt/financial-services/en/finance-treasury/alm/index.html


[PAGE TEXT]
NII & EVE sensitivity
NII sensitivity quantifies the impact of rate shocks on net interest income over a one-year horizon; EVE sensitivity quantifies the present-value impact across the full balance sheet. Together they are the primary IRRBB metrics under BCBS 368 and regional supervisory guidance. Both are measured across six standard rate scenarios plus bank-internal scenarios, with NII and EVE limit utilization reported to ALCO each month.
Lens
Scenario
Intent
Complexity

### CARD 1 [Automation|S] Deposit Repricing Assumption Calibration
urn: urn:financial-services:scenario:finance-treasury/alm/nii-eve-sensitivity/deposit-repricing-assumption-calibration
intent: Agent backtests the deposit repricing assumptions embedded in the NII and EVE sensitivity model against observed deposit rate changes over the prior four quarters and recommends updated beta and lag estimates for the ALM team's quarterly assumption review.
Problem to solve: Deposit repricing assumptions — beta coefficients and lag structures — are reviewed periodically but without a systematic backtest of how well the prior assumptions predicted actual deposit rate movements. Stale repricing assumptions embed systematic NII and EVE sensitivity errors that may not be visible until a significant rate move exposes the calibration gap.
Solution: Agent reads the current NII/EVE model's deposit repricing assumption set and the actual deposit rate data for each product category over the prior four quarters. It computes the prediction error for each product's beta and lag assumption against observed repricing, identifies products with systematic overestimation or underestimation of pass-through, and produces a recommended assumption revision set for the ALM team's review. The team validates the recommendations against current market conditions before updating the model.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 2 [New opps|M] FTP-Driven Product Pricing Signals
urn: urn:financial-services:scenario:finance-treasury/alm/nii-eve-sensitivity/ftp-product-pricing-signals
intent: Agent reads the approved FTP curve and current product margin data to identify loan and deposit products where FTP-implied pricing diverges from market, surfacing pricing adjustment opportunities for product teams and ALCO.
Problem to solve: Product pricing decisions are made by commercial business lines with reference to market rates and internal hurdles. The FTP curve's signal about which products generate a positive Treasury spread — and which are compressing NIM at current volumes — is not systematically connected to commercial pricing decisions between ALCO cycles.
Solution: Agent reads the approved FTP curve, product-level NIM attribution, competitor rate data where available, and origination volume by product. It identifies products where the FTP spread is contracting, expanding, or inverted relative to the approved hurdle, and generates a ranked product pricing signal for review by Treasury and commercial BU heads. ALCO reviews the signal in the context of the FTP curve decision; commercial heads adjust pricing within delegated authority.
OKR objective: Products and deposit segments where FTP-implied pricing diverges materially from current market or where the FTP spread is contracting or inverting against approved hurdles are identified and surfaced to Treasury and commercial business unit heads on a monthly basis.
OKR KR [Adoption]: Agent-produced FTP product pricing signals delivered for ≥10 of 12 monthly cycles in year 1; all material loan and deposit products covered in each cycle.
OKR KR [Acceptance]: ≥70% of pricing divergence signals confirmed as requiring commercial review by Treasury and BU heads; NIM attribution underlying each signal reconciles to the approved FTP curve in ≥95% of reviewed outputs.
OKR KR [Cycle]: FTP pricing divergence signal available to Treasury and BU heads within 5 business days of the monthly FTP curve update, vs. quarterly ALCO cycle review only in the prior process.

### CARD 3 [Insights|M] NII & EVE Driver Decomposition
urn: urn:financial-services:scenario:finance-treasury/alm/nii-eve-sensitivity/nii-eve-driver-decomposition
intent: Agent decomposes each period's change in NII and EVE sensitivity into its contributing drivers — balance sheet volume changes, rate environment moves, hedge portfolio changes, and repricing assumption revisions — presenting an attributed delta analysis alongside the standard sensitivity output for ALCO.
Problem to solve: NII and EVE sensitivity figures are reported monthly without a systematic attribution of how the figures moved relative to the prior period. ALCO cannot readily determine whether a tightening in NII sensitivity reflects balance sheet growth, hedge roll-off, a rate environment shift, or a revision to deposit repricing assumptions — the distinction that determines the correct management response.
Solution: Agent reads the current and prior-period NII and EVE sensitivity model inputs and outputs. It attributes the period-on-period sensitivity movement to four driver buckets — volume and mix changes, rate environment shifts, hedge portfolio changes, and repricing assumption revisions — and presents the decomposition as a delta waterfall alongside the standard ALCO sensitivity table. ALM team validates the attribution before the ALCO pack is distributed.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
FTP curve governance
The FTP curve is reviewed and approved by ALCO quarterly — or ad hoc when market rates move materially. The quarterly review requires Treasury to produce a memo justifying any proposed curve changes, with reference to current market rates, deposit repricing evidence, and peer benchmarks. The approved curve is applied to all new loan and deposit origination, directly determining NIM attribution between business lines and Treasury.
Lens
Scenario
Intent
Complexity

### CARD 4 [Optimize|S] FTP Sensitivity to Rate Regime Change
urn: urn:financial-services:scenario:finance-treasury/alm/ftp-curve-governance/ftp-sensitivity-to-rate-regime-change
intent: When a central bank rate decision or material market rate movement occurs, agent models the implied revision to each tenor bucket of the FTP curve and quantifies the NIM attribution impact on each BU if the curve is or is not updated before the next scheduled quarterly review.
Problem to solve: The FTP curve is reviewed on a quarterly schedule, but significant central bank rate movements between scheduled reviews create a lag between market rates and the curve applied to new origination. The NIM attribution error this creates — between Treasury and originating BUs — accumulates over the inter-review period without a quantified assessment of the cost of waiting for the next scheduled review.
Solution: Agent reads the current approved FTP curve, the central bank rate decision or market rate movement, and the prior deposit repricing evidence. It computes the implied FTP curve revision at each tenor bucket and the NIM attribution impact per BU for the inter-review period if no ad hoc update is made. Treasury reviews the analysis and determines whether the materiality threshold for an ad hoc review is met. The output is presented to ALCO as support for the ad hoc review decision.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 5 [Automation|M] FTP Curve Review Memo
urn: urn:financial-services:scenario:finance-treasury/alm/ftp-curve-governance/ftp-curve-review-memo
intent: Agent drafts the quarterly FTP curve review memo from current market rates, deposit repricing data, peer benchmarks, and the prior ALCO-approved curve, with explicit rationale for each proposed adjustment.
Problem to solve: The FTP curve review memo requires Treasury to cross-reference current yield curves, peer FTP benchmarks, deposit repricing evidence, and the prior approved curve before each quarterly ALCO submission. The drafting exercise is frequently compressed into the days immediately before the ALCO meeting.
Solution: Agent reads the current market yield curves, prior approved FTP curve, deposit repricing data, and available peer FTP benchmarks. It generates the review memo with rationale for each proposed tenor adjustment and flags tenors where the current curve is materially out of alignment with market. Treasury reviews the generated memo and submits to ALCO.
OKR objective: The quarterly FTP curve review memo — with rationale for each proposed adjustment, market yield curve cross-reference, deposit repricing evidence, and peer benchmarks — is available for Treasury review before the ALCO submission deadline.
OKR KR [Adoption]: Agent-produced FTP curve review memo used for ≥4 quarterly ALCO submissions within year 1.
OKR KR [Acceptance]: ≥80% of agent-drafted FTP review memos accepted by Treasury without material restatement of the adjustment rationale; proposed tenor adjustments validated against current market yield curves in ≥95% of reviewed memos.
OKR KR [Cycle]: FTP review memo available for Treasury review ≥5 business days before the ALCO meeting, vs. 2–3 days under compressed manual drafting in the prior process.

### CARD 6 [Insights|M] FTP Curve Backtesting
urn: urn:financial-services:scenario:finance-treasury/alm/ftp-curve-governance/ftp-curve-backtesting
intent: Agent backtests the approved FTP curve against actual deposit repricing behaviour and funding costs over the preceding four quarters, quantifying the funding cost error per tenor bucket and identifying systematic calibration biases that the ALCO review should address.
Problem to solve: The FTP curve is reviewed at least quarterly but without systematic backtesting of how well the prior-period curve reflected actual deposit repricing and funding costs. Curve calibration biases — consistently over-charging or under-charging specific tenor buckets — accumulate in the NIM attribution between business lines and Treasury without a formal assessment of their origin.
Solution: Agent reads the approved FTP curve rates by tenor bucket for each prior quarter, actual deposit repricing data for the corresponding products, and realised wholesale funding costs at each tenor. It computes the error between the FTP rate and the realised funding cost for each tenor bucket over the four-quarter backtest window, identifies tenor buckets with persistent systematic bias, and presents the findings for the ALCO quarterly FTP review as a backtesting annex. ALCO uses the annex to calibrate curve adjustments on an evidenced basis.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
IRRBB limit monitoring
NII and EVE IRRBB limits are board-set thresholds that cap the bank's interest-rate risk exposure in the banking book. Limit utilization is reported to ALCO monthly and to the Risk Committee quarterly. Approaching a limit triggers management action — hedge increase, repricing, or BU origination constraint — before the limit is breached and supervisory notification is required under NBKR, NBK/ARDFM, and CBR IRRBB frameworks.
Lens
Scenario
Intent
Complexity

### CARD 7 [Automation|S] IRRBB Limit Utilisation Dashboard
urn: urn:financial-services:scenario:finance-treasury/alm/irrbb-limit-monitoring/irrbb-limit-utilisation-dashboard
intent: Agent generates the monthly IRRBB limit utilisation report for ALCO — covering NII and EVE limit headroom across all approved scenarios, trend in utilisation over the rolling six months, and the top three drivers of utilisation change since the prior cycle.
Problem to solve: The monthly IRRBB limit utilisation report is produced by the ALM team from NII and EVE scenario outputs and the approved limit schedule. The assembly process — extracting scenario results, mapping to limits, computing headroom, and drafting the ALCO presentation page — takes two to three days and produces a report that reflects the state at data extraction rather than at the ALCO meeting date.
Solution: Agent reads the current NII and EVE scenario outputs and the board-approved limit schedule. It computes headroom against each NII and EVE limit across all approved scenarios, appends a six-month utilisation trend for each scenario, and attributes the period-on-period utilisation change to its top three drivers — volume changes, rate environment, and hedge portfolio movement. The report is available for ALCO review on the day the scenario model run completes and is refreshed if rates move materially before the meeting.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 8 [Insights|M] IRRBB Early Warning Signal
urn: urn:financial-services:scenario:finance-treasury/alm/irrbb-limit-monitoring/irrbb-early-warning-signal
intent: Agent monitors intra-month balance sheet changes — loan origination volumes, deposit repricing events, hedge roll-offs, and AOCI movements — and estimates their NII and EVE sensitivity impact in real time, alerting the ALM desk when the estimated impact on limit utilisation is material before the formal monthly model run.
Problem to solve: IRRBB limit utilisation is measured at the formal monthly scenario model run. Intra-month events that materially increase utilisation — a large fixed-rate loan origination tranche, a deposit repricing event, or a hedge expiry — are not reflected in a limit-related metric until the next scheduled run. An ALM desk managing limit proximity has no forward view of intra-month utilisation drift until the model run is complete.
Solution: Agent monitors daily origination feeds, deposit repricing notices, hedge position changes, and AOCI movements. Using a parametric sensitivity model calibrated to the bank's last formal IRRBB model run, it estimates the cumulative NII and EVE sensitivity delta from intra-month events and maintains a running estimated utilisation figure for each limit. When the estimated utilisation in any scenario moves within a defined proximity band of the limit, an alert is issued to the ALM desk with the estimated impact attributable to each recent event. The ALM desk uses the alert to decide whether to trigger an intra-month hedge action or origination constraint ahead of the formal run.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 9 [Enablement|M] IRRBB Supervisory Assessment Preparation
urn: urn:financial-services:scenario:finance-treasury/alm/irrbb-limit-monitoring/irrbb-supervisory-assessment-prep
intent: Agent assembles the documentation package for NBKR, NBK/ARDFM, or CBR IRRBB supervisory reviews — scenario results, limit utilisation history, methodology documentation, and governance attestation — from current ALM data and prior submissions, substantially reducing ALM team preparation time.
Problem to solve: IRRBB supervisory assessments require the ALM team to compile scenario results, limit utilisation history, model documentation, and governance narrative into a regulator-prescribed package. The compilation draws on data from the IRRBB model system, the limit register, board minutes for limit approvals, and the ICAAP for stress context. Assembly takes one to two weeks and is managed as a standalone exercise each assessment cycle.
Solution: Agent reads the current and prior-period IRRBB scenario outputs, the limit utilisation history register, the model methodology documentation, and the governance calendar for limit approvals. It assembles the supervisory assessment documentation package in the prescribed structure — scenario results table, twelve-month utilisation history, methodology summary, limit governance timeline, and management attestation sections — with prior-period consistency checks applied automatically. The ALM team reviews the assembled package and adds judgment-intensive commentary before submission.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
ALCO rate-scenario pack
The monthly ALCO rate-scenario pack synthesizes NII and EVE sensitivity across all approved scenarios into a management presentation — with driver decomposition, limit utilization, hedge cost-benefit, and the CFO's and Treasurer's commentary. It is the primary basis for ALCO's interest-rate risk decisions each month and the document that regulators review in IRRBB supervisory assessments.
Lens
Scenario
Intent
Complexity

### CARD 10 [Optimize|S] Hedge Portfolio Effectiveness Review
urn: urn:financial-services:scenario:finance-treasury/alm/alco-rate-pack/hedge-portfolio-effectiveness-review
intent: Agent assesses whether the current IR derivative hedge portfolio is reducing NII and EVE sensitivity within the ALCO-approved target range across standard rate scenarios, and identifies hedges approaching maturity that require rolling before the next ALCO cycle.
Problem to solve: The ALCO rate-scenario pack reports net NII and EVE sensitivity after hedging but does not present the marginal hedge effectiveness — whether each tranche of the hedge book is still performing its risk-reduction function as rates have moved since the hedge was executed. Hedges that have shifted in-the-money or out-of-the-money may no longer provide the sensitivity reduction that was modelled at inception.
Solution: Agent reads the current hedge register, the mark-to-market of each instrument, and the current unhedged NII and EVE sensitivities. It computes the marginal NII and EVE reduction attributable to each hedge tranche under the standard BCBS 368 scenarios, identifies tranches where effectiveness has declined below the target threshold, and flags instruments maturing within 90 days that require roll decision. The hedge effectiveness summary is appended to the ALCO rate-scenario pack and reviewed by Treasury and ALM before each ALCO session.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 11 [Automation|M] ALCO Rate-Scenario Pack
urn: urn:financial-services:scenario:finance-treasury/alm/alco-rate-pack/alco-rate-scenario-pack
intent: Agent synthesizes multi-scenario NII and EVE outputs into a complete ALCO rate-scenario pack — with driver decomposition, limit utilization, hedge cost-benefit framing, and narrative — delivered before each ALCO meeting.
Problem to solve: The ALM team assembles the rate sensitivity pack manually each month, including cross-scenario comparison, assumption attribution, and hedge cost-benefit analysis. The drafting cycle consumes the majority of the production window available before ALCO.
Solution: Agent reads multi-scenario NII and EVE output files, maps each sensitivity driver — deposit beta, decay rate, prepayment, repricing gap — and generates the full ALCO pack with scenario comparison tables, driver decomposition, limit utilization against board-set thresholds, and hedge-programme cost-benefit narrative. ALCO enters each session focused on rate decisions rather than data walkthrough.
OKR objective: A complete ALCO rate-scenario pack — with multi-scenario NII and EVE comparison, driver decomposition, limit utilisation, hedge cost-benefit, and narrative — is available before each ALCO meeting, produced from ALM model outputs without manual drafting.
OKR KR [Adoption]: Agent-produced ALCO rate-scenario pack used for ≥11 of 12 monthly ALCO meetings in year 1.
OKR KR [Acceptance]: ≥85% of agent-produced packs accepted by the ALM team for ALCO distribution without material amendment; cross-scenario figures reconcile to ALM model outputs in ≥98% of reviewed packs.
OKR KR [Cycle]: ALCO rate-scenario pack production time reduced from the majority of the 2-day pre-ALCO window to ≤4 hours of ALM officer review and approval.

### CARD 12 [Insights|M] Rate Scenario Sensitivity Decomposition
urn: urn:financial-services:scenario:finance-treasury/alm/alco-rate-pack/rate-scenario-sensitivity-decomposition
intent: Agent decomposes each ALCO rate scenario's NII impact into its component drivers — asset repricing, liability repricing, hedge cost, and basis effects — and ranks the scenarios by their net NII and EVE impact, presenting a driver-attributed sensitivity table alongside the standard ALCO pack.
Problem to solve: The ALCO rate-scenario pack presents NII and EVE sensitivity as net figures per scenario without driver decomposition. ALCO cannot determine whether a compression in the upward-rate scenario reflects asset repricing lag, hedge cost, deposit beta assumptions, or basis movements — distinctions that determine which management action is appropriate and which BU bears the primary risk.
Solution: Agent reads the NII and EVE scenario model outputs at the component level — asset repricing by product, liability repricing by product, net hedge cost per scenario, and basis effects. It allocates the total NII sensitivity per scenario to each driver, ranks scenarios from most to least capital-consuming, and presents the decomposition as an addendum table to the standard ALCO pack. ALCO uses the decomposition to direct hedging or repricing actions to the material driver rather than the aggregate metric.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
GenAI-enabled Banking and Financial Services Framework · v11i
