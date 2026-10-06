# 

source: html-alt/financial-services/en/risk-control/climate-esg-risk/index.html


[PAGE TEXT]
Physical risk assessment
Physical climate risk assessment maps the bank's loan and investment portfolio to geospatial physical hazard data — flood zones, drought indices, heat stress maps, wildfire risk surfaces — to quantify acute and chronic climate risk exposure at the asset and portfolio level. NGFS physical risk scenarios (Current Policies, Nationally Determined Contributions, Net Zero 2050) provide the scenario framework; EBA climate risk guidelines and TCFD Pillar 3 disclosure requirements define the reporting expectations. The assessment requires linking collateral location registers to physical hazard layers — an integration exercise not routinely performed between annual ICAAP cycles.
Lens
Scenario
Intent
Complexity

### CARD 1 [Automation|M] Physical Risk Collateral Heat Map
urn: urn:financial-services:scenario:risk-control/climate-esg-risk/physical-risk-assessment/physical-risk-collateral-heat-map
intent: Agent geocodes the collateral register and overlays NGFS physical hazard layers to produce a visual heat map of acute and chronic climate exposure by geography and asset class for the sustainability and credit risk teams.
Problem to solve: Linking collateral location data to physical hazard layers requires geocoding the collateral register and joining to hazard datasets — a data integration task that has not been automated between annual ICAAP cycles. The climate risk team relies on a point-in-time annual assessment; intra-year collateral additions are not reflected in the physical risk view.
Solution: Agent reads the collateral register with property addresses, geocodes each asset, overlays NGFS flood, heat stress, drought, and wildfire hazard layers, and produces the exposure heat map by geography and asset class. It refreshes the map on a quarterly cadence aligned with the collateral register extract. The sustainability team reviews and integrates the output into the TCFD disclosure and ICAAP physical risk narrative.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 2 [Insights|L] Physical Risk Portfolio Assessment
urn: urn:financial-services:scenario:risk-control/climate-esg-risk/physical-risk-assessment/physical-risk-portfolio-assessment
intent: Agent maps the collateral and project finance portfolio against NGFS physical risk scenarios — flood, heat stress, wildfire, drought — to estimate exposure at risk and inform ICAAP physical risk quantification.
Problem to solve: Physical risk assessment requires geocoding collateral and project assets, overlaying NGFS hazard maps, and estimating asset damage and income disruption under each scenario. The analysis is feasible for large individual exposures but not at portfolio scale with manual methods.
Solution: Agent reads collateral register and project asset data with location attributes, applies NGFS physical risk hazard layers, estimates exposure at risk by asset class and geography, and produces the physical risk narrative for ICAAP. The climate risk team reviews scenario parameters and validates assumptions for the highest-exposure segments.
OKR objective: The CRO and climate risk team report ICAAP physical risk quantification based on an agent-produced exposure-at-risk assessment mapping the full collateral and project finance portfolio against NGFS flood, heat stress, wildfire, and drought hazard layers.
OKR KR [Adoption]: Agent physical risk assessment covering ≥80% of collateral and project asset portfolio by exposure value within 18 months of go-live; all four NGFS physical hazard categories (flood, heat, wildfire, drought) applied from go-live.
OKR KR [Acceptance]: ≥75% of agent-estimated exposure-at-risk figures accepted by the climate risk team as valid for ICAAP use without major recalculation; highest-exposure segment assumptions validated by the climate risk team in ≥90% of ICAAP runs.
OKR KR [Cycle]: Full portfolio physical risk assessment delivered within 5 business days of data cut, enabling ICAAP physical risk section drafting to begin rather than awaiting ≥4 weeks of manual geocoding and overlay analysis.

### CARD 3 [Enablement|L] Physical Risk Stress Scenario Narrative
urn: urn:financial-services:scenario:risk-control/climate-esg-risk/physical-risk-assessment/physical-risk-stress-scenario-narrative
intent: Agent drafts the ICAAP physical risk stress narrative — exposure at risk by scenario and asset class, expected loss under each NGFS scenario, and management action options — for the climate risk and credit risk teams to review and submit.
Problem to solve: ICAAP physical risk narrative drafting requires combining physical risk heat map outputs, EBA stress scenario parameters, and credit risk loss estimates into a coherent narrative. Each input is owned by a different team; assembling a draft document that reconciles all three draws on senior climate and credit risk capacity during an already compressed ICAAP production cycle.
Solution: Agent reads the physical risk heat map, EBA and NGFS scenario specifications, and credit risk model outputs for the high-exposure asset classes. It drafts the ICAAP physical risk stress narrative in the prescribed structure — scenario description, exposure at risk quantification, expected loss range, and identified management actions. The climate risk and credit risk teams review and add forward-looking judgement before CRO sign-off.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
ESG counterparty scoring
ESG counterparty scoring assigns environmental, social, and governance ratings to borrowers and investment counterparties — enabling the bank to monitor ESG risk concentration, apply ESG criteria in credit decisions, and classify assets under EU taxonomy green asset frameworks. Data sources include third-party ESG rating providers (MSCI, Sustainalytics, S&P), sectoral carbon intensity benchmarks, and borrower-disclosed sustainability metrics. In the Central Asian market, ESG data availability is limited for SME and mid-corporate borrowers; proxy scoring using sector benchmarks and physical footprint data fills the gap. Financed emissions at the borrower level require activity-based emissions data that is often incomplete.
Lens
Scenario
Intent
Complexity

### CARD 4 [Insights|S] ESG Score Trend Monitoring
urn: urn:financial-services:scenario:risk-control/climate-esg-risk/esg-counterparty-scoring/esg-score-trend-monitoring
intent: Agent monitors ESG score movements across the borrower portfolio on a quarterly basis, flags counterparties with deteriorating ESG scores, and delivers a trend digest to the sustainability team for credit review escalation.
Problem to solve: ESG counterparty scores are updated when new third-party provider data is received, but the sustainability team has no systematic alert when a borrower's score deteriorates materially between reporting cycles. An ESG downgrade that affects the bank's EU taxonomy green asset ratio or triggers an ESG covenant review is identified in the next periodic portfolio review rather than at score update.
Solution: Agent reads quarterly ESG score updates from third-party providers, computes score movement per borrower, flags counterparties with material deterioration or controversy additions, and delivers the quarterly trend digest to the sustainability team. Flagged counterparties are routed to credit review for ESG covenant and green asset ratio assessment.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 5 [Automation|S] ESG Data Collection Outreach Support
urn: urn:financial-services:scenario:risk-control/climate-esg-risk/esg-counterparty-scoring/esg-data-collection-outreach-support
intent: Agent drafts outreach communications to borrowers with ESG data gaps, identifies the specific data fields required per borrower, and tracks response status for the sustainability and relationship management teams.
Problem to solve: ESG scoring gaps for SME and mid-corporate borrowers require direct borrower outreach to collect sustainability metrics. Drafting outreach requests, tracking responses, and following up on non-responses is a relationship management task not systematically supported by the current CRM workflow.
Solution: Agent reads the ESG scoring gap register, identifies the specific data fields required per borrower, and drafts a tailored outreach communication referencing the borrower's sector and the bank's ESG data requirements. It tracks response status and flags non-responses for relationship manager follow-up after the defined response window.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 6 [Insights|M] ESG Counterparty Scoring & Gap Analysis
urn: urn:financial-services:scenario:risk-control/climate-esg-risk/esg-counterparty-scoring/esg-counterparty-scoring-gap-analysis
intent: Agent assigns ESG scores to borrowers using available third-party data and sector proxies, identifies scoring gaps where borrower data is insufficient, and produces a portfolio-level ESG concentration view.
Problem to solve: ESG counterparty data is available from third-party providers for large listed borrowers but absent or inconsistent for SME and mid-corporate borrowers. Manual data collection from borrowers is bottlenecked on relationship manager capacity; portfolio-level ESG concentration is not visible between reporting cycles.
Solution: Agent reads third-party ESG rating data, sector carbon intensity benchmarks, and borrower-disclosed sustainability metrics. It assigns ESG scores using available data and sector proxies where borrower data is absent, flags scoring gaps requiring borrower outreach, and produces a portfolio-level ESG concentration view for the sustainability team.
OKR objective: The sustainability team has a portfolio-level ESG concentration view with agent-assigned counterparty scores for all borrowers — using third-party data where available and sector proxies where not — and a prioritised scoring-gap flag list for outreach.
OKR KR [Adoption]: Agent ESG scoring covering ≥90% of the credit portfolio by exposure value within 12 months of go-live; portfolio-level ESG concentration view refreshed at least quarterly from go-live.
OKR KR [Acceptance]: ≥75% of agent-assigned sector proxy scores rated as appropriate by the sustainability team on peer review; scoring-gap flag list actioned for ≥60% of flagged borrowers within 6 months of first production run.
OKR KR [Cycle]: Full portfolio ESG scoring and gap analysis completed within 3 business days of data refresh, versus a best-efforts manual process that was constrained by relationship manager capacity.

### CARD 7 [New opps|M] Green Finance Pipeline Screening
urn: urn:financial-services:scenario:risk-control/climate-esg-risk/esg-counterparty-scoring/green-finance-pipeline-screening
intent: Agent screens new lending proposals against green taxonomy eligibility criteria and ESG policy thresholds, flagging eligible transactions for green bond allocation and non-eligible transactions with the relevant exclusion criterion.
Problem to solve: Green finance origination requires the sustainability team to review each new deal against the bank's green taxonomy, EU taxonomy alignment criteria, and ESG sector exclusion policy. With a high volume of new deals per month, taxonomy screening is performed on a sample basis; eligible transactions go unidentified and green bond issuance capacity is under-utilised.
Solution: Agent reads new deal submissions and screens each against the green taxonomy criteria library, EU taxonomy technical screening criteria, and ESG sector exclusion list. It flags eligible transactions for green bond allocation with the eligibility rationale per criterion, and routes non-eligible deals with the applicable exclusion category. The sustainability team reviews flagged deals and finalises allocation decisions.
OKR objective: The sustainability team reviews agent-flagged green taxonomy-eligible transactions for green bond allocation, with non-eligible deals routed with their applicable exclusion criterion, on a per-deal basis across the full new lending pipeline.
OKR KR [Adoption]: Agent screening applied to ≥95% of new lending submissions within 12 months of go-live; EU taxonomy technical screening criteria and ESG sector exclusion list applied in every run.
OKR KR [Acceptance]: ≥85% of agent-assigned eligibility flags confirmed as accurate by the sustainability team on review; green bond allocation capacity identified per cycle increased by ≥20% versus the prior sampling-based screening approach.
OKR KR [Cycle]: Taxonomy screening result delivered within 24 hours of new deal submission receipt, enabling same-week eligibility determination rather than batch review on a sampling schedule.

[PAGE TEXT]
Transition risk & carbon exposure
Transition risk arises from the credit deterioration in high-emission sectors as carbon pricing, regulatory standards, and market preferences shift under decarbonisation scenarios. The NGFS transition scenarios — Orderly, Disorderly, and Hot House World — calibrate the speed and smoothness of the policy transition; the credit impact is expressed as sector-level PD and LGD sensitivities under each scenario. Financed emissions — the bank's share of borrower carbon emissions proportional to financing provided — is the primary metric for portfolio-level transition risk and for TCFD and ISSB disclosure. EBA guidelines on climate risk require transition risk analysis to be integrated into credit risk assessment and ICAAP.
Lens
Scenario
Intent
Complexity

### CARD 8 [Automation|M] Financed Emissions Calculation
urn: urn:financial-services:scenario:risk-control/climate-esg-risk/transition-risk-carbon-exposure/financed-emissions-calculation
intent: Agent computes financed emissions per sector and borrower using PCAF methodology — combining portfolio exposure data with borrower-level carbon intensity where available and sector benchmarks where not — for TCFD disclosure and NGFS transition risk analysis.
Problem to solve: Financed emissions computation requires matching each portfolio exposure to a carbon intensity estimate and applying the PCAF attribution factor. Borrower-level emissions data is available for a minority of counterparties; sector benchmarks must fill the gap for the remainder. The computation across 1,000-10,000 exposures with mixed data quality requires systematic processing that is not feasible manually on an annual cycle.
Solution: Agent reads portfolio exposure data, borrower-level emissions disclosures where available, and sector carbon intensity benchmarks. It applies the PCAF methodology to compute financed emissions per exposure, aggregates by sector and asset class, and flags the proportion of emissions based on direct data versus proxies. The sustainability and credit risk teams review sector-level outputs before TCFD submission.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 9 [Insights|L] Transition Risk & Carbon Exposure Analysis
urn: urn:financial-services:scenario:risk-control/climate-esg-risk/transition-risk-carbon-exposure/transition-risk-carbon-exposure-analysis
intent: Agent scores the credit portfolio against NGFS transition scenarios, estimating PD/LGD sensitivities by sector and generating the financed-emission narrative for ICAAP and supervisory stress tests.
Problem to solve: Transition risk quantification requires mapping each portfolio sector to NGFS transition scenarios and estimating PD sensitivity under each, cross-referencing the bank's IRB model parameters. The analysis is performed once or twice per year; the transition risk view does not refresh as the portfolio evolves between ICAAP cycles.
Solution: Agent maps the credit portfolio by sector to NGFS transition scenarios, estimates PD and LGD sensitivities using IRB model outputs, computes financed emissions by sector and borrower, and generates the transition risk narrative for ICAAP and TCFD disclosure. The credit risk and ESG teams review scenario assumptions and add strategic context.
OKR objective: The credit risk and ESG teams report ICAAP transition risk quantification and TCFD financed-emission disclosure from an agent-produced analysis mapping the full credit portfolio against NGFS transition scenarios with PD/LGD sensitivities estimated from IRB model outputs.
OKR KR [Adoption]: Agent transition risk analysis covering ≥85% of the credit portfolio by exposure value within 18 months of go-live; all prescribed NGFS transition pathways and financed emission calculations produced in every run from go-live.
OKR KR [Acceptance]: ≥80% of agent-estimated PD/LGD sensitivities accepted by the credit risk team as valid for ICAAP use without major recalculation; TCFD financed-emission figures confirmed as consistent with supervisory disclosure requirements in ≥90% of runs.
OKR KR [Cycle]: Transition risk and carbon exposure analysis delivered within 5 business days of portfolio data cut, versus a once-or-twice-annual manual exercise consuming ≥4 weeks of quantitative analyst effort.

### CARD 10 [Enablement|L] Transition Risk Sector Stress Analysis
urn: urn:financial-services:scenario:risk-control/climate-esg-risk/transition-risk-carbon-exposure/transition-risk-sector-stress-analysis
intent: Agent maps the credit portfolio's high-emission sector exposures to NGFS Disorderly transition scenario PD and LGD sensitivities, producing a sector-level stress output for ICAAP and EBA climate risk reporting.
Problem to solve: EBA climate risk guidelines require transition risk to be integrated into credit risk assessment, with sector-level PD and LGD sensitivity estimates under NGFS scenarios. Producing these estimates requires combining the credit portfolio sector mapping with published NGFS scenario credit risk parameters — a cross-functional exercise performed on an ad hoc basis rather than in an integrated workflow.
Solution: Agent reads sector exposure data from the credit portfolio, NGFS Disorderly transition scenario credit risk sensitivity parameters by sector, and the bank's IRB PD and LGD outputs. It computes sector-level transition risk stress outputs — PD uplift and LGD sensitivity by sector under the Disorderly scenario — and produces the input for the ICAAP climate risk section. The credit risk and climate risk teams review scenario parameter choices before ICAAP submission.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
TCFD & ISSB disclosure
TCFD (Task Force on Climate-related Financial Disclosures) and ISSB S1/S2 standards define the framework for climate and sustainability disclosure — covering governance, strategy, risk management, and metrics and targets. TCFD disclosure is mandatory for regulated banks in the UK (PRA), EU (CSRD), and increasingly in NBKR and CBR frameworks; ISSB S1 and S2 set the global convergence baseline. The disclosure requires assembling financed emissions, physical and transition risk heat maps, governance framework descriptions, and climate scenario analysis summaries from multiple sources. Consistency with prior disclosure commitments — net-zero targets, sector phasedown timelines — must be verified against the current period's metrics.
Lens
Scenario
Intent
Complexity

### CARD 11 [Insights|S] TCFD Prior Commitment Tracking
urn: urn:financial-services:scenario:risk-control/climate-esg-risk/tcfd-issb-disclosure/tcfd-prior-commitment-tracking
intent: Agent reads prior TCFD disclosures and current performance metrics, identifies commitments made in prior years, and produces a commitment-vs-progress tracking report for the sustainability team ahead of the annual disclosure cycle.
Problem to solve: Each annual TCFD disclosure must be consistent with commitments made in prior-year disclosures — net-zero target timelines, sector phasedown pledges, and green finance volume targets. Tracking prior commitments against current metrics is performed manually; inconsistencies are identified during the editorial review process rather than before drafting begins.
Solution: Agent reads the prior two years of TCFD disclosures, extracts commitments and targets with their reference year and deadline, and cross-references each against current metrics. It produces a commitment-vs-progress table flagging commitments where the current trajectory is inconsistent with the stated target, for the sustainability team to address before the disclosure draft is finalised.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

### CARD 12 [Automation|M] ESG Disclosure Draft
urn: urn:financial-services:scenario:risk-control/climate-esg-risk/tcfd-issb-disclosure/esg-disclosure-draft
intent: Agent assembles the TCFD and ISSB disclosure draft from sustainability data, portfolio climate metrics, and prior disclosure text, with gap flags and prior-commitment cross-reference.
Problem to solve: Producing the annual TCFD and ISSB disclosure requires assembling financed emissions, governance framework descriptions, climate scenario analysis, and ESG metrics from multiple teams and systems. Data collection, narrative drafting, and prior-commitment cross-referencing consume the sustainability team's cycle capacity.
Solution: Agent reads current ESG metrics, portfolio climate risk summaries, governance framework documentation, and prior TCFD disclosure. It assembles the structured disclosure draft in TCFD/ISSB format, cross-references prior commitments with current progress, and flags disclosure gaps. The sustainability team validates metrics and adds forward-looking commentary before publication.
OKR objective: The sustainability team validates metrics and adds forward-looking commentary to an agent-assembled TCFD and ISSB disclosure draft — with gap flags and prior-commitment cross-reference — rather than constructing the document from component inputs.
OKR KR [Adoption]: Agent-assembled disclosure draft used as the base document for ≥1 annual TCFD/ISSB disclosure cycle within 18 months of go-live; prior-commitment cross-reference applied to 100% of commitments from the preceding disclosure.
OKR KR [Acceptance]: ≥80% of disclosure draft sections accepted by the sustainability team without structural revision; disclosure gap flags rated as accurate by sustainability team reviewers in ≥85% of instances.
OKR KR [Cycle]: Initial TCFD/ISSB disclosure draft delivered within 5 business days of data cut, reducing the sustainability team's document assembly burden by ≥50% of total cycle time.

### CARD 13 [Automation|M] TCFD Metrics Data Collection & Reconciliation
urn: urn:financial-services:scenario:risk-control/climate-esg-risk/tcfd-issb-disclosure/tcfd-metrics-data-collection
intent: Agent reads sustainability data from internal systems and third-party ESG data providers, reconciles financed emissions, and produces a metrics table aligned to the TCFD and ISSB S2 required disclosure set for the sustainability team's annual review.
Problem to solve: TCFD and ISSB S2 metrics span financed emissions by sector, physical risk exposure, transition risk concentration, and governance indicators — each sourced from different internal and external data providers. Manual collection and reconciliation across these sources consumes the sustainability team's capacity in the months before the disclosure deadline.
Solution: Agent reads portfolio data, ESG provider feeds, carbon accounting outputs, and governance documentation. It computes the required metrics set, flags data gaps where borrower-level data is unavailable and proxies are applied, and produces the reconciled metrics table in TCFD/ISSB format ready for the sustainability team's editorial review.
OKR objective: (EMPTY)
OKR KRs: (EMPTY)

[PAGE TEXT]
GenAI-enabled Banking and Financial Services Framework · v11i
