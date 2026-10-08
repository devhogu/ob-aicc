# Credit risk

Credit risk is the largest consumer of a bank's regulatory capital — the risk that a borrower or counterparty fails to meet contractual obligations, generating an unexpected loss that erodes CET1. Under prudential requirements, credit risk is governed through PD/LGD/EAD model suites, IFRS 9 ECL provisioning, concentration limits, and watchlist management. Basel III/IV sets the capital floor; where a bank uses internal models, they calibrate within that constraint. **The GenAI opportunity is to compress the credit-review cycle** — from quarterly portfolio packs assembled manually over weeks to weekly AI-generated analysis that surfaces migration signals, concentration patterns, and watchlist risk in a single integrated view.

## Problems

### Counterparty exposure {#counterparty-exposure}

| Lens | Problem |
| --- | --- |
| Insights & analytics | PD migration, watchlist deterioration, and counterparty exposure analytics are each produced within their own reporting cycle from separate risk and credit systems. The CRO and Chief Credit Officer lack a continuous view of how individual counterparty quality is moving relative to the portfolio; emerging watchlist credits surface only at the monthly credit review committee, weeks after early-warning signals appeared in the data. |
| Enablement | Credit review preparation — assembling the counterparty dossier, reconciling current financials against the credit approval memo, and preparing the committee presentation — absorbs 60–80% of a relationship manager's or credit analyst's pre-meeting time. The analytical work the committee is convened to perform starts only after the assembly is complete. |
| Automation | Watchlist reports, credit portfolio packs for the Risk Committee, and IFRS 9 ECL provision narratives are assembled from credit system exports, management accounts, and model outputs on a monthly or quarterly cycle. Each has a defined format and known source data; the assembly is repeatable and data-intensive. |
| New business opportunities | A continuously instrumented credit book — weekly migration signals, real-time concentration headroom, and vintage performance by origination cohort — gives the Chief Credit Officer a forward signal that quarterly review cycles cannot provide. Credit appetite deployment decisions and portfolio rebalancing moves can be timed against current position rather than last month's report. |

## Counterparty exposure analytics {#counterparty-exposure-analytics}

The aggregation of all on- and off-balance-sheet exposure to a single counterparty or economic group — covering loans, commitments, derivatives, and trade finance — reported against single-name concentration limits. Large-exposure rules, in line with the Basel large-exposures framework, commonly require enhanced reporting once a single-name exposure exceeds 10% of Tier 1 capital. Counterparty exposure analytics consolidate the total exposure picture across product types and entities, enabling limit monitoring and credit review preparation.

### Counterparty Exposure Breach Notification Pack

- URN: urn:financial-services:scenario:risk-control/credit-risk/counterparty-exposure-analytics/counterparty-exposure-breach-pack
- Lens: Enablement
- Complexity: S
- Intent: The AI agent assembles the supervisory notification pack when a single-name exposure breaches the regulatory large-exposure limit, pulling the full exposure breakdown and entity structure for the CRO response.
- Problem to solve: A large-exposure breach triggers a mandatory notification to the regulator under large-exposure rules. Assembling the notification pack — total exposure by product, entity relationship map, origination timeline, and management action — draws on multiple systems and consumes analyst hours in the window before the regulatory deadline.
- Solution: The AI agent detects the limit breach from the daily exposure register, retrieves the full product-level breakdown, maps the entity structure, and generates the supervisory notification pack in the prescribed format. The CRO reviews and approves before submission.
- OKR: The CRO reviews and approves an AI-assembled supervisory notification pack — total exposure by product, entity relationship map, and origination timeline — for every large-exposure breach, rather than waiting on analyst assembly in the window before the regulatory deadline.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent is used to assemble the notification pack for ≥95% of large-exposure breaches detected in the daily exposure register within 12 months of go-live; product-level breakdown and entity structure map included in every pack from go-live. |
| Acceptance | ≥85% of AI-assembled packs approved by the CRO without material supplementation before submission; product-level exposure figures confirmed accurate against source systems in ≥95% of packs on quality review. |
| Cycle | Notification pack delivered to the CRO within 4 hours of breach detection, versus ≥1 business day of analyst assembly across multiple systems under the prior approach. |

### Counterparty Exposure Aggregation

- URN: urn:financial-services:scenario:risk-control/credit-risk/counterparty-exposure-analytics/counterparty-exposure-aggregation
- Lens: Automation
- Complexity: M
- Intent: The AI agent aggregates on- and off-balance-sheet exposure to each counterparty and economic group across loans, commitments, derivatives, and trade finance, producing a single-name exposure report for large-exposure limit monitoring.
- Problem to solve: Single-name exposure aggregation requires joining loan management, derivatives, and trade finance systems by counterparty. Entity-relationship mapping — identifying where a subsidiary exposure should roll up to the parent economic group — is performed manually and is error-prone, particularly for multi-jurisdiction corporate groups.
- Solution: The AI agent reads exposure data from loan management, derivatives, and trade finance systems, applies the Bank's entity-relationship hierarchy to aggregate to economic group level, and produces the single-name exposure register with limit utilization and large-exposure threshold flags. The credit risk officer reviews entity mapping for any new counterparty structures before releasing the report.
- OKR: The credit risk officer releases a single-name exposure register — aggregated to economic group level across loans, commitments, derivatives, and trade finance, with limit utilization and large-exposure threshold flags — after reviewing only new counterparty structures rather than mapping entities by hand.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent is used to produce the single-name exposure register for ≥95% of reporting cycles within 6 months of go-live; loan management, derivatives, and trade finance exposures aggregated to economic group level in every run from go-live. |
| Acceptance | ≥90% of AI-produced registers released by the credit risk officer without correction to the entity mapping of existing counterparties; group-level roll-up errors found on quality review reduced to ≤2% of counterparties. |
| Cycle | Exposure register available to the credit risk officer within 2 hours of the source-system data cut, versus ≥1 business day of manual cross-system joining and entity mapping under the prior approach. |

### Counterparty Exposure Trend Analysis

- URN: urn:financial-services:scenario:risk-control/credit-risk/counterparty-exposure-analytics/counterparty-exposure-trend-analysis
- Lens: Insights
- Complexity: M
- Intent: The AI agent tracks single-name and sector concentration trends over rolling 12 months, identifying counterparties with accelerating exposure growth relative to limit headroom for the Chief Credit Officer's weekly review.
- Problem to solve: Limit utilization snapshots show the current position but not the rate of change. A counterparty approaching its large-exposure limit through incremental draws over several months is visible in a trend view but not in a point-in-time report; the credit team's attention is typically directed to current breaches rather than trajectory.
- Solution: The AI agent reads 12 months of daily exposure registers, computes utilization trend and velocity for each counterparty and sector, and flags names where the trajectory points to a limit breach within the next 90 days. The Chief Credit Officer receives a weekly trend digest alongside the standard limit utilization report.
- OKR: The Chief Credit Officer receives a weekly trend digest identifying counterparties and sectors whose exposure trajectory points to a limit breach within 90 days, alongside the standard limit utilization report.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's trend analysis runs on 12 months of daily exposure registers every week within 6 months of go-live; weekly trend digest delivered to the Chief Credit Officer for ≥45 consecutive weeks in year 1. |
| Acceptance | ≥75% of AI-flagged names rated as warranting review by the Chief Credit Officer; ≥80% of counterparties that reach their limit during the year flagged by the AI agent at least 30 days beforehand. |
| Cycle | Weekly trend digest delivered within 1 business day of the week-end exposure data cut, moving detection from the point of breach to up to 90 days ahead of it. |

## Concentration & sector risk {#concentration-sector-risk}

Concentration risk is the incremental loss risk arising when a significant portion of the portfolio is exposed to a single counterparty, group, industry, geography, or correlated cluster. Large-exposure rules commonly require supervisory notification when single-name concentration exceeds 25% of Tier 1 capital; sector concentration limits are set internally in the Risk Appetite Statement. The BCBS 239 principles call for risk data aggregation that supports timely concentration monitoring, including under stress. Standard concentration reports cover the expected dimensions; correlated cross-dimensional concentrations require dedicated analytical work.

### Portfolio Concentration Analysis

- URN: urn:financial-services:scenario:risk-control/credit-risk/concentration-sector-risk/portfolio-concentration-analysis
- Lens: Insights
- Complexity: M
- Intent: The AI agent scans the credit portfolio for concentration patterns across five dimensions — industry, geography, single-name, collateral, and correlated cross-sector clusters — and maps distance-to-limit for each.
- Problem to solve: Standard concentration reports cover industry, geography, and single-name dimensions. Correlated concentrations — geographic-sector overlap, supply-chain clusters across top borrowers, collateral correlation across counterparties — are not visible in standard outputs and require bespoke analysis commissioned after a sector event has already developed.
- Solution: The AI agent reads the full loan portfolio and maps exposures across all five concentration dimensions, including multi-dimensional correlated patterns. It computes distance-to-limit for each dimension and models concentration impact under a sector stress scenario. The Chief Credit Officer receives a weekly concentration watch with escalation flags.
- OKR: The Chief Credit Officer manages credit concentration risk from a weekly AI-generated analysis across five dimensions — industry, geography, single-name, collateral, and correlated cross-sector clusters — with distance-to-limit computed and escalation flags applied.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's concentration analysis covering all five dimensions runs weekly within 6 months of go-live; weekly watch delivered to the Chief Credit Officer for ≥45 consecutive weeks in year 1. |
| Acceptance | ≥80% of escalation flags rated as material by the Chief Credit Officer on review; correlated cross-sector concentration patterns identified by the AI agent cited in ≥1 credit committee remediation discussion per quarter. |
| Cycle | Weekly concentration analysis delivered within 1 business day of loan portfolio data cut, versus ≥1 week of bespoke manual analysis commissioned reactively after sector events under the prior approach. |

### Sector Stress Concentration Scenario

- URN: urn:financial-services:scenario:risk-control/credit-risk/concentration-sector-risk/sector-stress-concentration-scenario
- Lens: Enablement
- Complexity: M
- Intent: The AI agent models a defined sector stress scenario — commodity price collapse, real estate correction, or sovereign downgrade — against the current portfolio concentration profile, producing an expected loss estimate for the Credit Committee stress discussion.
- Problem to solve: Ad hoc sector stress scenario analysis is commissioned following a sector event. The analysis requires combining current sector exposure data with historical loss rates or supervisory stress parameters, a cross-system exercise that takes several days of analyst effort and is typically completed after the relevant Credit Committee meeting.
- Solution: The AI agent reads current sector exposure, applies the defined stress parameter set — PD uplift, LGD widening, correlation assumption — from the Bank's stress testing library, computes expected loss by sector and total portfolio impact, and produces the scenario output within one business day of trigger. The Credit Committee uses it as the basis for its stress discussion.
- OKR: The Credit Committee discusses a sector stress event with an AI-produced scenario output — expected loss by sector and total portfolio impact under the defined PD, LGD, and correlation stress parameters — available before the meeting rather than after it.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent is used to produce the scenario output for ≥90% of sector stress scenarios requested for the Credit Committee within 12 months of go-live; stress parameters drawn from the Bank's stress testing library in every run from go-live. |
| Acceptance | ≥80% of AI-produced scenario outputs accepted by the Credit Committee as the basis for the stress discussion without supplementary analyst modeling; expected loss figures reconciled to current sector exposure data in ≥95% of outputs on quality review. |
| Cycle | Scenario output delivered to the Credit Committee within 1 business day of trigger, versus several days of cross-system analyst effort completed after the relevant meeting under the prior approach. |

### Concentration Limit Calibration Review

- URN: urn:financial-services:scenario:risk-control/credit-risk/concentration-sector-risk/concentration-limit-calibration-review
- Lens: Optimize
- Complexity: M
- Intent: The AI agent compares current portfolio concentration against sector limit calibration assumptions, identifies limits where the current macro or sector outlook has changed the risk basis used at calibration, and delivers a limit review signal to the Chief Credit Officer.
- Problem to solve: Sector concentration limits are calibrated at the annual risk appetite review. Changes in sector credit conditions — a sector upgrade or downgrade by rating agencies, a regulatory change affecting sector economics — alter the risk basis underlying the limit but are not reflected until the next annual calibration.
- Solution: The AI agent reads the current sector limit calibration assumptions and compares them with current sector credit conditions from rating agency reports, regulatory guidance, and macroeconomic data. It flags limits where the calibration basis has materially changed and delivers a review signal to the Chief Credit Officer for out-of-cycle limit adjustment where warranted.
- OKR: The Chief Credit Officer receives a limit review signal whenever the sector credit conditions underlying a concentration limit have materially changed since calibration, enabling out-of-cycle limit adjustment rather than waiting for the annual risk appetite review.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's comparison of calibration assumptions against current sector conditions runs across 100% of sector concentration limits at least quarterly within 6 months of go-live; rating agency reports, regulatory guidance, and macroeconomic data read in every run. |
| Acceptance | ≥70% of AI-flagged limits confirmed by the Chief Credit Officer as warranting review; ≥1 out-of-cycle limit adjustment per year initiated from the AI agent's review signal. |
| Cycle | Review signal delivered within 5 business days of a material change in sector credit conditions, versus up to 12 months until the next annual calibration under the prior approach. |

## PD/LGD/EAD model outputs {#pd-lgd-ead-model-outputs}

Where the Bank uses internal ratings-based (IRB) models under Basel III Pillar 1, they produce the three core parameter estimates — probability of default (PD), loss given default (LGD), and exposure at default (EAD). PD/LGD/EAD outputs drive regulatory capital (RWA), IFRS 9 ECL, and credit pricing. Supervisory approval of IRB models requires continuous monitoring of model performance; material deterioration triggers recalibration and notification of the supervisor. The model outputs are regenerated each month and consumed by capital, credit risk, and finance teams.

### PD/LGD/EAD Monthly Output Narrative

- URN: urn:financial-services:scenario:risk-control/credit-risk/pd-lgd-ead-model-outputs/pd-lgd-ead-monthly-output-narrative
- Lens: Automation
- Complexity: M
- Intent: Where the Bank uses IRB models, the AI agent generates the monthly PD/LGD/EAD output narrative — parameter movements by segment, macro overlay impact, and variance to prior month — from the IRB model run for the capital and finance teams.
- Problem to solve: Monthly IRB model output requires a narrative explaining parameter movements before the capital and finance teams can act on the numbers. Drafting the narrative requires cross-referencing model outputs, macro overlay inputs, and prior-month values held in separate systems; the analyst assembles it manually before any downstream use begins.
- Solution: The AI agent reads the monthly model run outputs, macro overlay parameters, and prior-month values. It generates the standard narrative covering PD movement by segment, LGD and EAD drivers, macro overlay effect, and variance flags. The credit risk officer reviews the narrative and releases it to the capital and finance teams.
- OKR: The credit risk officer releases the monthly PD/LGD/EAD output narrative — parameter movements by segment, macro overlay effect, and variance to prior month — to the capital and finance teams after reviewing an AI-generated draft rather than assembling it manually.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent is used to generate the PD/LGD/EAD output narrative for ≥11 of 12 monthly model runs within 12 months of go-live; all standard sections (PD movement by segment, LGD and EAD drivers, macro overlay effect, variance flags) produced in every run. |
| Acceptance | ≥85% of AI-generated narratives released by the credit risk officer with only minor editorial amendment; parameter movement figures matching the model run outputs in ≥98% of narrative items on quality review. |
| Cycle | Narrative draft available to the credit risk officer within 1 business day of the monthly model run, versus ≥3 business days of manual cross-system assembly before downstream use could begin under the prior approach. |

### IRB Model Performance Signal Watch

- URN: urn:financial-services:scenario:risk-control/credit-risk/pd-lgd-ead-model-outputs/irb-model-performance-signal
- Lens: Insights
- Complexity: M
- Intent: Where the Bank uses IRB models, the AI agent monitors PD/LGD/EAD model output distributions each month for calibration drift, PSI breaches, and actual-vs-predicted divergence, delivering an early-warning signal to the Chief Model Risk Officer before a formal out-of-cycle validation is triggered.
- Problem to solve: Model performance deterioration is detected in the scheduled validation cycle, which runs annually or biennially in line with model-risk guidance. Calibration drift visible in the monthly output distributions — predicted default rates diverging from realized rates at segment level — is not surfaced until the next scheduled review, narrowing the response window.
- Solution: The AI agent reads monthly PD/LGD/EAD output distributions and realized default and loss data, computes PSI for input stability, Gini and KS for discrimination, and predicted-vs-actual divergence by segment. It flags segments breaching defined performance bands and delivers a monthly performance signal watch to the Chief Model Risk Officer.
- OKR: The Chief Model Risk Officer receives a monthly performance signal watch on the PD/LGD/EAD models — PSI, Gini, KS, and predicted-versus-actual divergence by segment — so calibration drift is acted on before the next scheduled validation.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's performance monitoring runs on 100% of PD/LGD/EAD model output distributions each month within 6 months of go-live; monthly signal watch delivered to the Chief Model Risk Officer for ≥10 consecutive months in year 1. |
| Acceptance | ≥75% of AI-flagged segment breaches confirmed as genuine performance deterioration by the Chief Model Risk Officer on review; ≥1 out-of-cycle validation or recalibration per year initiated from the AI agent's signal. |
| Cycle | Monthly signal watch delivered within 3 business days of realized default and loss data availability, versus detection at the annual or biennial scheduled validation under the prior approach. |

### RWA & Capital Attribution Pack

- URN: urn:financial-services:scenario:risk-control/credit-risk/pd-lgd-ead-model-outputs/rwa-capital-attribution-pack
- Lens: Automation
- Complexity: M
- Intent: Where the Bank uses IRB models, the AI agent assembles the monthly RWA attribution pack — decomposing RWA movement into PD, LGD, EAD, and portfolio mix drivers — for the Capital Committee and ICAAP capital adequacy narrative.
- Problem to solve: Monthly RWA movements must be explained to the Capital Committee and documented in the ICAAP narrative. Attribution across PD, LGD, EAD, and portfolio composition drivers requires combining model outputs with portfolio exposure data; the capital team assembles the decomposition manually before each committee cycle.
- Solution: The AI agent reads monthly IRB outputs, exposure data, and prior-month RWA. It decomposes RWA movement into parameter and mix drivers, produces the Capital Committee attribution table, and drafts the ICAAP capital adequacy narrative section covering credit risk RWA. The capital team reviews the pack and integrates it into the full ICAAP pack.
- OKR: The capital team reviews an AI-assembled monthly RWA attribution pack — RWA movement decomposed into PD, LGD, EAD, and portfolio mix drivers, with the credit risk RWA section of the ICAAP narrative drafted — rather than building the decomposition manually before each Capital Committee cycle.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent is used to assemble the RWA attribution pack for ≥11 of 12 monthly Capital Committee cycles within 12 months of go-live; all four drivers (PD, LGD, EAD, portfolio mix) decomposed in every run from go-live. |
| Acceptance | ≥85% of AI-assembled attribution tables accepted by the capital team without recomputation; unexplained residual in the RWA movement decomposition held to ≤2% of total monthly movement. |
| Cycle | Attribution pack delivered to the capital team within 2 business days of the monthly IRB output run, versus ≥5 business days of manual decomposition before each committee cycle under the prior approach. |

## Vintage cohort & migration {#vintage-cohort-migration}

Vintage cohort analysis tracks the credit performance of loans originated in a given period — comparing default rates, loss rates, and migration patterns across origination cohorts to assess credit quality trajectory by underwriting vintage. Migration analysis tracks the flow of exposures between rating grades or asset-quality classifications over time. Together they provide the forward-looking credit quality signal that point-in-time PD estimates and stock-level impairment ratios cannot deliver alone. IFRS 9 ECL staging decisions depend on significant-increase-in-credit-risk (SICR) triggers that are informed by migration analysis.

### Migration Matrix Trend Watch

- URN: urn:financial-services:scenario:risk-control/credit-risk/vintage-cohort-migration/migration-matrix-trend-watch
- Lens: Insights
- Complexity: S
- Intent: The AI agent produces a rolling 12-month migration matrix by rating grade and asset class, flagging accelerating downgrade flow for the CRO and Credit Committee.
- Problem to solve: The credit risk team monitors current-period migration as part of the monthly portfolio pack. Trend in migration rates — a gradual acceleration in Stage 1 to Stage 2 flow over several quarters — is not directly visible from month-to-month migration snapshots without time-series analysis.
- Solution: The AI agent reads monthly migration registers, constructs rolling migration matrices by grade and asset class, computes trend in each transition probability, and flags grade pairs where the downgrade probability is accelerating beyond a defined threshold. The CRO and Credit Committee receive the trend watch alongside the standard migration matrix.
- OKR: The CRO and Credit Committee receive a rolling 12-month migration trend watch by rating grade and asset class — with accelerating downgrade flows flagged — alongside the standard monthly migration matrix.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's trend watch is produced from the monthly migration registers for ≥11 of 12 months within 12 months of go-live; all rating grades and asset classes covered in every run from go-live. |
| Acceptance | ≥75% of grade pairs flagged for accelerating downgrade flow rated as warranting discussion by the CRO; the AI agent's trend flags cited in ≥1 Credit Committee discussion per quarter. |
| Cycle | Trend watch delivered within 2 business days of the monthly migration register cut, versus acceleration becoming visible only after several quarters of month-to-month snapshots under the prior approach. |

### Vintage Cohort Performance Report

- URN: urn:financial-services:scenario:risk-control/credit-risk/vintage-cohort-migration/vintage-cohort-performance-report
- Lens: Insights
- Complexity: M
- Intent: The AI agent generates quarterly vintage cohort performance reports — default rates, loss rates, and prepayment speeds by origination vintage and segment — enabling the Chief Credit Officer to compare credit quality across underwriting periods.
- Problem to solve: Vintage performance comparison requires constructing cohort time series from loan transaction data across multiple origination periods. The analysis is produced on an ad hoc basis when credit quality concerns arise; a systematic quarterly view is not available between those requests.
- Solution: The AI agent reads loan origination and performance data, constructs cohort time series by vintage, segment, and product, and generates the quarterly report covering default rates, loss rates, and prepayment speeds. The Chief Credit Officer uses the output to identify underwriting vintage deterioration and inform PD recalibration timing.
- OKR: The Chief Credit Officer compares credit quality across underwriting periods from an AI-generated quarterly vintage cohort report — default rates, loss rates, and prepayment speeds by origination vintage and segment — rather than commissioning the analysis ad hoc.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent is used to generate the vintage cohort performance report for ≥4 consecutive quarters within 18 months of go-live; all origination vintages, segments, and products covered in every run from go-live. |
| Acceptance | ≥80% of quarterly reports accepted by the Chief Credit Officer without supplementary cohort analysis; vintage deterioration identified in the report cited in ≥1 underwriting or PD recalibration decision per year. |
| Cycle | Quarterly report delivered within 5 business days of the quarter-end loan performance data cut, versus ≥2 weeks of ad hoc cohort construction each time a credit quality concern arose under the prior approach. |

### SICR Migration Trigger Analysis

- URN: urn:financial-services:scenario:risk-control/credit-risk/vintage-cohort-migration/sicr-migration-trigger-analysis
- Lens: Automation
- Complexity: M
- Intent: The AI agent applies the IFRS 9 SICR criteria to the loan portfolio each month, identifies exposures with significant increases in credit risk, and produces the staging migration register for the finance and credit risk teams.
- Problem to solve: IFRS 9 Stage 2 classification requires identifying exposures where credit risk has increased significantly since origination. Applying SICR quantitative tests — lifetime PD comparison, backstop DPD trigger, qualitative override criteria — across a large portfolio requires systematic data extraction and rule application that is prone to inconsistency when performed manually.
- Solution: The AI agent reads current PD estimates, origination PD benchmarks, payment behavior data, and qualitative override flags. It applies the SICR criteria, generates the staging migration register with the triggering criterion per exposure, and flags population-level migration patterns for the finance controller's review before ECL provisioning.
- OKR: The finance controller reviews an AI-generated monthly staging migration register — with the SICR criterion that triggered each exposure and population-level migration patterns flagged — before ECL provisioning, rather than relying on manually applied staging rules.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent is used to apply the SICR criteria to 100% of in-scope exposures for ≥11 of 12 monthly cycles within 12 months of go-live; lifetime PD comparison, backstop DPD trigger, and qualitative override criteria applied in every run. |
| Acceptance | ≥95% of AI-assigned staging outcomes accepted by the finance controller without reclassification; staging inconsistencies raised in quality review reduced by ≥50% versus the prior manual approach. |
| Cycle | Staging migration register delivered within 2 business days of month-end PD and payment data availability, versus ≥5 business days of manual extraction and rule application under the prior approach. |

## Watchlist & early-warning {#watchlist-early-warning}

The portfolio monitoring framework that identifies credits showing early deterioration signals — financial covenant strain, payment irregularity, adverse sector news, collateral value decline — before default. Watchlist management is a supervisory expectation under credit-risk management requirements; each watchlisted credit requires an enhanced monitoring plan and periodic committee review. Early-warning indicator frameworks define the trigger conditions for watchlist entry and the escalation path to Special Mention or Substandard classification.

### Watchlist Covenant Breach Tracker

- URN: urn:financial-services:scenario:risk-control/credit-risk/watchlist-early-warning/watchlist-covenant-tracker
- Lens: Automation
- Complexity: M
- Intent: The AI agent reads financial statements and covenant test submissions for watchlist credits, applies covenant compliance tests, and generates the covenant status register with breach flags and headroom calculations for each credit ahead of the review cycle.
- Problem to solve: Covenant compliance monitoring for watchlist credits requires the credit analyst to calculate test results from borrower financial submissions and compare against the covenant schedule. With multiple covenants per credit and submissions on varying cadences, tracking compliance status across the full watchlist manually introduces the risk of missed breach identification.
- Solution: The AI agent reads borrower financial submissions and applies the covenant test calculations per the facility agreement terms. It computes compliance status and headroom for each covenant, flags breaches and waivers required, and generates the covenant status register across the full watchlist population. The credit analyst reviews and escalates confirmed breaches per the credit policy.
- OKR: The credit analyst reviews an AI-generated covenant status register — compliance status, headroom, breach flags, and waivers required for every watchlist credit — ahead of each review cycle, rather than calculating covenant tests by hand from borrower submissions.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent is used to apply covenant tests to ≥95% of borrower financial submissions for watchlist credits within 6 months of go-live; covenant status register covering the full watchlist population generated ahead of every review cycle. |
| Acceptance | ≥90% of AI-flagged covenant breaches confirmed by the credit analyst on review; covenant breaches first identified after the review cycle in which they occurred reduced to zero. |
| Cycle | Covenant status updated within 1 business day of receipt of a borrower financial submission, versus calculation deferred to the analyst's preparation for the next review cycle under the prior approach. |

### Watchlist Dossier Assembly

- URN: urn:financial-services:scenario:risk-control/credit-risk/watchlist-early-warning/watchlist-loan-review-prep
- Lens: Automation
- Complexity: M
- Intent: The AI agent assembles the watchlist dossier per credit — combining current financials, covenant status, collateral valuations, and prior committee minutes — into a committee-ready pack ahead of each review cycle.
- Problem to solve: Preparing each watchlist review dossier consumes two to four analyst hours before the committee meeting. Current financials, covenant breach status, collateral valuations, and prior meeting minutes reside in separate systems; the credit analyst assembles them by hand each cycle.
- Solution: The AI agent reads loan management, financial data, covenant tracker, and committee records and auto-assembles each dossier in a standard format. The credit analyst reviews the generated pack, adds forward judgment on borrower trajectory, and clears it for committee.
- OKR: The credit analyst adds forward judgment on borrower trajectory to an AI-assembled watchlist dossier — combining current financials, covenant status, collateral valuations, and prior committee minutes — for every credit ahead of each review cycle.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent is used to auto-assemble watchlist dossiers for ≥95% of watchlist credits in each review cycle within 6 months of go-live; all four dossier components (financials, covenant status, collateral valuations, prior minutes) populated from connected systems in every run. |
| Acceptance | ≥85% of AI-assembled dossiers accepted by credit analysts as complete for committee review without manual supplementation; committee chairs confirm ≥80% of dossiers as adequate for discussion in post-meeting quality reviews. |
| Cycle | Watchlist dossier assembled within 30 minutes of cycle trigger, versus 2–4 hours of manual assembly per credit under the prior approach. |

### Credit Early-Warning Signal Enrichment

- URN: urn:financial-services:scenario:risk-control/credit-risk/watchlist-early-warning/credit-early-warning-signal-enrichment
- Lens: Insights
- Complexity: M
- Intent: The AI agent continuously monitors external signals — news, regulatory filings, payment-behavior proxies, and sector data — and enriches the watchlist early-warning register with flags for review by the Chief Credit Officer.
- Problem to solve: Watchlist identification depends on periodic relationship manager reviews and covenant breach triggers. External signals — adverse media, supply-chain stress, sector rating actions — reach the credit team after the risk has materialized in the borrower's financials, narrowing the response window.
- Solution: The AI agent reads news feeds, regulatory filings databases, sector data, and payment-behavior proxies, cross-references against the active credit portfolio, and flags borrowers with emerging signal clusters. The Chief Credit Officer receives a daily alert digest; triggered credits enter watchlist review without waiting for the next scheduled relationship manager review.
- OKR: The Chief Credit Officer receives a daily alert digest of borrowers with emerging external signal clusters, enabling watchlist review to begin before risk materializes in financial statements.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent monitors external signals across ≥90% of the active credit portfolio by counterparty within 12 months of go-live; daily alert digest delivered to the Chief Credit Officer for ≥200 business days per year once live. |
| Acceptance | ≥80% of AI-generated watchlist flags confirmed as material by the Chief Credit Officer on review, with ≤20% of daily flagged credits subsequently assessed as immaterial. |
| Cycle | External signal alert delivered to the Chief Credit Officer within 24 hours of signal identification, versus a lag of days-to-weeks under the prior relationship manager review cycle. |

### Watchlist Migration Probability Scoring

- URN: urn:financial-services:scenario:risk-control/credit-risk/watchlist-early-warning/watchlist-migration-probability-scoring
- Lens: Insights
- Complexity: M
- Intent: The AI agent computes a migration probability score for each watchlist credit — combining financial trend, covenant headroom, collateral coverage, and external signal data — enabling the Chief Credit Officer to prioritize review attention across the watchlist population.
- Problem to solve: Watchlist credits are reviewed on a standard cycle without systematic prioritization of those with the highest probability of migration to default. With 30–80 credits typically on the watchlist at any time, uniform review cadence under-resources high-migration-risk credits and over-resources stable watchlist names.
- Solution: The AI agent reads financial trend data, covenant headroom calculations, collateral coverage ratios, and external signal clusters for each watchlist credit. It computes a migration probability score using the Bank's early-warning indicator framework and delivers a ranked watchlist to the Chief Credit Officer, enabling differentiated review intensity by migration probability band.
- OKR: The Chief Credit Officer prioritizes watchlist review attention from an AI-ranked watchlist — each credit scored for migration probability from financial trend, covenant headroom, collateral coverage, and external signals — rather than applying a uniform review cadence.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's migration probability score is computed for 100% of watchlist credits ahead of every review cycle within 6 months of go-live; all four inputs (financial trend, covenant headroom, collateral coverage, external signals) used in every run. |
| Acceptance | ≥75% of credits in the top migration probability band confirmed by the Chief Credit Officer as warranting intensified review; ≥70% of watchlist credits that migrate to default during the year ranked in the top band beforehand. |
| Cycle | Ranked watchlist delivered ≥3 business days before each review cycle, replacing a uniform review cadence with review intensity set by migration probability band. |

## ECL & IFRS 9 provisions {#ecl-ifrs9-provisions}

Expected Credit Loss (ECL) under IFRS 9 is the probability-weighted forward-looking estimate of credit losses, staged by credit quality deterioration — Stage 1 (12-month ECL), Stage 2 (lifetime ECL on SICR credits), and Stage 3 (lifetime ECL on credit-impaired exposures). The ECL calculation combines PD, LGD, EAD, and forward-looking macroeconomic adjustment factors across origination cohorts and portfolio segments. The ECL calculation is typically performed quarterly, with the provision balance reported to the regulator and disclosed in the financial statements.

### ECL Provision Narrative

- URN: urn:financial-services:scenario:risk-control/credit-risk/ecl-ifrs9-provisions/ecl-provision-narrative
- Lens: Automation
- Complexity: M
- Intent: The AI agent assembles the quarterly IFRS 9 ECL provision narrative — stage movements, macro overlay rationale, and variance to prior quarter — for review by the finance controller and CRO.
- Problem to solve: The quarterly IFRS 9 ECL narrative requires the credit risk and finance teams to cross-reference model outputs, macro overlay inputs, and prior disclosures before drafting begins. Stage movement explanations, macro overlay assumptions, and variance analysis must be reconciled across separate systems, with ECL, PD/LGD/EAD, and staging data held in different repositories.
- Solution: The AI agent reads current ECL model outputs, staging flow data, macro overlay assumptions, and prior quarter disclosures. It generates the provision narrative in the prescribed format — stage movement explanation, macro overlay rationale, and variance analysis — ready for the finance controller and CRO to review and sign off.
- OKR: The finance controller and CRO review an AI-assembled quarterly IFRS 9 ECL provision narrative — with stage movements, macro overlay rationale, and prior-quarter variance analysis — drafted from model outputs in the prescribed format.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent is used to draft the ECL provision narrative for ≥4 consecutive quarterly reporting cycles within 18 months of go-live; all prescribed narrative sections (stage movements, macro overlay, variance analysis) populated from model data in every run. |
| Acceptance | ≥80% of AI-drafted ECL narratives accepted by the finance controller and CRO with only minor editorial amendment; cross-system reconciliation errors in stage movement data reduced to ≤3% of narrative items on quality review. |
| Cycle | ECL provision narrative draft delivered within 2 business days of quarterly model output lock, versus ≥1 week of manual cross-system assembly under the prior approach. |

### Macro Overlay Calibration Support

- URN: urn:financial-services:scenario:risk-control/credit-risk/ecl-ifrs9-provisions/macro-overlay-calibration-support
- Lens: Enablement
- Complexity: M
- Intent: The AI agent reads current macroeconomic forecasts from the Bank's approved scenarios and prior overlay calibration records, and produces a structured calibration input document for the credit risk and finance teams' quarterly macro overlay review.
- Problem to solve: IFRS 9 macro overlay calibration requires the credit risk team to assess whether model-generated ECL adequately reflects the macroeconomic outlook, applying management judgment where it does not. The calibration discussion is prepared by the credit risk analyst drawing on multiple macro data sources and prior overlay history; the preparation step consumes capacity before the substantive discussion can begin.
- Solution: The AI agent reads the Bank's approved macroeconomic scenarios, prior overlay decisions and their rationale, and current ECL model outputs. It produces a structured calibration input document — current macro scenario parameters, comparison to prior overlay assumptions, ECL sensitivity to scenario change, and key judgment questions — for the credit risk and finance teams' quarterly overlay review meeting.
- OKR: The credit risk and finance teams open the quarterly macro overlay review with an AI-produced calibration input document — current scenario parameters, comparison to prior overlay assumptions, ECL sensitivity to scenario change, and key judgment questions — rather than spending analyst capacity on preparation.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent is used to produce the calibration input document for ≥4 consecutive quarterly overlay reviews within 18 months of go-live; approved macroeconomic scenarios, prior overlay decisions, and current ECL model outputs read in every run. |
| Acceptance | ≥80% of calibration input documents accepted by the credit risk and finance teams as the basis for the overlay discussion without supplementary analyst preparation; ≥75% of the key judgment questions raised rated as relevant by the review meeting. |
| Cycle | Calibration input document delivered ≥3 business days before the quarterly overlay review meeting, versus ≥1 week of credit risk analyst preparation under the prior approach. |

### ECL Staging Distribution Analysis

- URN: urn:financial-services:scenario:risk-control/credit-risk/ecl-ifrs9-provisions/ecl-staging-distribution-analysis
- Lens: Insights
- Complexity: M
- Intent: The AI agent tracks Stage 1/2/3 distribution movements across portfolios each quarter, identifies segment-level trends inconsistent with the macro environment, and delivers a distribution analysis to the Chief Credit Officer ahead of the quarterly ECL review.
- Problem to solve: Stage distribution movements are reported in the quarterly IFRS 9 narrative but not analyzed for consistency with macro and portfolio signals. A Stage 2 stock declining in a deteriorating macro environment, or a Stage 2 concentration building in a specific segment, may indicate SICR criteria that require recalibration — a signal not visible in the summary narrative alone.
- Solution: The AI agent reads quarterly staging distributions by segment and product, computes movement trends, and cross-references against macro indicators and portfolio credit quality signals. It flags distribution patterns inconsistent with the macro environment and delivers the analysis to the Chief Credit Officer ahead of the quarterly ECL model and overlay review.
- OKR: The Chief Credit Officer receives a quarterly staging distribution analysis — Stage 1/2/3 movements by segment and product, cross-referenced to macro indicators and portfolio credit quality signals — flagging patterns inconsistent with the macro environment ahead of the ECL review.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's staging distribution analysis is produced for ≥4 consecutive quarters within 18 months of go-live; all portfolio segments and products covered in every run from go-live. |
| Acceptance | ≥70% of AI-flagged distribution patterns rated as warranting investigation by the Chief Credit Officer; ≥1 SICR criteria review per year initiated from an AI-flagged pattern. |
| Cycle | Analysis delivered ≥5 business days before the quarterly ECL model and overlay review, versus no consistency analysis of stage movements beyond the summary narrative under the prior approach. |
