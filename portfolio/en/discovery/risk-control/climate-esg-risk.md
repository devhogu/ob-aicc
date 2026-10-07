# Climate & ESG risk

Climate and ESG risk covers the financial risks arising from climate change — physical risk (asset damage, revenue disruption from acute and chronic climate hazards) and transition risk (credit deterioration in high-emission sectors under carbon pricing regimes) — and the Bank's ESG obligations to investors, regulators, and counterparties. TCFD-aligned disclosure is mandatory for large banks in a growing number of jurisdictions; ISSB S1 and S2 standards set the emerging global baseline. Supervisory guidelines on climate risk and the NGFS scenario set provide the analytical framework; supervisors are increasingly incorporating climate risk into ICAAP expectations. **The GenAI opportunity is to operationalize NGFS scenario mapping at portfolio scale** — connecting loan book exposure to physical and transition risk scenarios — where manual analysis has been feasible only for a point-in-time annual view.

## Problems

### Physical & transition risk {#physical-transition-risk}

| Lens | Problem |
| --- | --- |
| Insights & analytics | Physical risk — the financial loss arising from flood, drought, heat stress, wildfire, or sea-level rise affecting collateral and borrower operations — is geographically concentrated but the loan portfolio is tracked by industry sector and borrower rating, not by asset location. Matching collateral locations to physical hazard scenarios requires cross-referencing systems that are not routinely integrated; the exercise is completed manually for ICAAP once per year. |
| Enablement | Transition risk analysis — estimating PD and LGD sensitivity by sector under NGFS transition scenarios — requires the credit risk team to map each sector's decarbonization pathway to the Bank's own PD and LGD model parameters (IRB parameters, where the Bank uses internal-ratings models). The mapping is a multi-week analytical exercise completed once or twice per year; between cycles, the transition risk view does not update as the portfolio evolves. |
| Automation | TCFD disclosure and ISSB S1/S2 reporting require assembling financed emissions by sector, physical risk heat map, governance framework descriptions, and climate scenario analysis summaries from multiple data sources and teams. The annual disclosure cycle consumes six to eight weeks of sustainability team time on data collection, narrative drafting, and prior-commitment cross-referencing. |
| New business opportunities | Banks that produce portfolio-level climate risk analysis at a quarterly cadence — updating the physical and transition risk heat map as the portfolio evolves — can demonstrate supervisory maturity that peers producing annual point-in-time views cannot. That maturity is directly observable in supervisory climate risk assessments and ICAAP reviews, and increasingly in institutional investor ESG due-diligence questionnaires. |

## Physical risk assessment {#physical-risk-assessment}

Physical climate risk assessment maps the Bank's loan and investment portfolio to geospatial physical hazard data — flood zones, drought indices, heat stress maps, wildfire risk surfaces — to quantify acute and chronic climate risk exposure at the asset and portfolio level. NGFS physical risk scenarios (Current Policies, Nationally Determined Contributions, Net Zero 2050) provide the scenario framework; supervisory climate risk guidelines, Pillar 3 ESG disclosure requirements, and the TCFD recommendations define the reporting expectations. The assessment requires linking collateral location registers to physical hazard layers — an integration exercise not routinely performed between annual ICAAP cycles.

### Physical Risk Collateral Heat Map

- URN: urn:financial-services:scenario:risk-control/climate-esg-risk/physical-risk-assessment/physical-risk-collateral-heat-map
- Lens: Automation
- Complexity: M
- Intent: The AI agent geocodes the collateral register and overlays NGFS physical hazard layers to produce a visual heat map of acute and chronic climate exposure by geography and asset class for the sustainability and credit risk teams.
- Problem to solve: Linking collateral location data to physical hazard layers requires geocoding the collateral register and joining to hazard datasets — a data integration task that is rarely automated between annual ICAAP cycles. The sustainability and credit risk teams rely on a point-in-time annual assessment; intra-year collateral additions are not reflected in the physical risk view.
- Solution: The AI agent reads the collateral register with property addresses, geocodes each asset, overlays NGFS flood, heat stress, drought, and wildfire hazard layers, and produces the exposure heat map by geography and asset class. It refreshes the map on a quarterly cadence aligned with the collateral register extract. The sustainability team reviews and integrates the output into the TCFD disclosure and ICAAP physical risk narrative.
- OKR: The sustainability and credit risk teams work from an AI-produced physical risk heat map — the geocoded collateral register overlaid with flood, heat stress, drought, and wildfire hazard layers by geography and asset class — refreshed quarterly rather than once a year.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced heat map covering ≥85% of the collateral register by exposure value within 12 months of go-live; map refreshed for ≥4 consecutive quarterly collateral register extracts. |
| Acceptance | ≥80% of heat map outputs accepted by the sustainability team for the TCFD disclosure and ICAAP physical risk narrative without material correction; geocoding accuracy confirmed at ≥95% on sample review. |
| Cycle | Heat map refreshed within 5 business days of each quarterly collateral register extract, versus a point-in-time annual assessment that did not reflect intra-year collateral additions. |

### Physical Risk Portfolio Assessment

- URN: urn:financial-services:scenario:risk-control/climate-esg-risk/physical-risk-assessment/physical-risk-portfolio-assessment
- Lens: Insights
- Complexity: L
- Intent: The AI agent maps the collateral and project finance portfolio against NGFS physical risk scenarios — flood, heat stress, wildfire, drought — to estimate exposure at risk and inform ICAAP physical risk quantification.
- Problem to solve: Physical risk assessment requires geocoding collateral and project assets, overlaying NGFS hazard maps, and estimating asset damage and income disruption under each scenario. The analysis is feasible for large individual exposures but not at portfolio scale with manual methods.
- Solution: The AI agent reads collateral register and project asset data with location attributes, applies NGFS physical risk hazard layers, estimates exposure at risk by asset class and geography, and produces the exposure-at-risk assessment that feeds the ICAAP physical risk quantification. The climate risk team reviews scenario parameters and validates assumptions for the highest-exposure segments.
- OKR: The CRO and climate risk team report ICAAP physical risk quantification based on an AI-produced exposure-at-risk assessment mapping the full collateral and project finance portfolio against NGFS flood, heat stress, wildfire, and drought hazard layers.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced physical risk assessment covering ≥80% of the collateral and project asset portfolio by exposure value within 18 months of go-live; all four NGFS physical hazard categories (flood, heat, wildfire, drought) applied from go-live. |
| Acceptance | ≥75% of AI-estimated exposure-at-risk figures accepted by the climate risk team as valid for ICAAP use without major recalculation; highest-exposure segment assumptions validated by the climate risk team in ≥90% of ICAAP runs. |
| Cycle | Full portfolio physical risk assessment delivered within 5 business days of data cut, enabling ICAAP physical risk section drafting to begin rather than awaiting ≥4 weeks of manual geocoding and overlay analysis. |

### Physical Risk Stress Scenario Narrative

- URN: urn:financial-services:scenario:risk-control/climate-esg-risk/physical-risk-assessment/physical-risk-stress-scenario-narrative
- Lens: Enablement
- Complexity: L
- Intent: The AI agent drafts the ICAAP physical risk stress narrative — exposure at risk by scenario and asset class, expected loss under each NGFS scenario, and management action options — for the climate risk and credit risk teams to review and submit.
- Problem to solve: ICAAP physical risk narrative drafting requires combining physical risk heat map outputs, supervisory stress scenario parameters, and credit risk loss estimates into a coherent narrative. Each input is owned by a different team; assembling a draft document that reconciles all three draws on senior climate and credit risk capacity during an already compressed ICAAP production cycle.
- Solution: The AI agent reads the physical risk heat map, supervisory and NGFS scenario specifications, and credit risk model outputs for the high-exposure asset classes. It drafts the ICAAP physical risk stress narrative in the prescribed structure — scenario description, exposure at risk quantification, expected loss range, and identified management actions. The climate risk and credit risk teams review and add forward-looking judgment before CRO sign-off.
- OKR: The climate risk and credit risk teams add forward-looking judgment to an AI-drafted ICAAP physical risk stress narrative — scenario description, exposure at risk, expected loss range, and management actions — before CRO sign-off.

| Dimension | Key result |
| --- | --- |
| Adoption | AI agent used to draft the physical risk stress narrative for ≥1 ICAAP cycle within 18 months of go-live; all four prescribed sections produced for every scenario in scope. |
| Acceptance | ≥75% of narrative sections accepted by the climate risk and credit risk teams without structural revision; figures in the narrative reconciled to the heat map and credit risk model outputs in 100% of drafts. |
| Cycle | Narrative draft delivered within 3 business days of receipt of the heat map, scenario specifications, and credit risk model outputs, versus ≥2 weeks of senior climate and credit risk drafting in the ICAAP production cycle. |

## ESG counterparty scoring {#esg-counterparty-scoring}

ESG counterparty scoring assigns environmental, social, and governance ratings to borrowers and investment counterparties — enabling the Bank to monitor ESG risk concentration, apply ESG criteria in credit decisions, and classify assets under a green taxonomy (such as the EU taxonomy). Data sources include third-party ESG rating providers (MSCI, Sustainalytics, S&P), sectoral carbon intensity benchmarks, and borrower-disclosed sustainability metrics. In many markets, ESG data availability is limited for SME and mid-corporate borrowers; proxy scoring using sector benchmarks and physical footprint data fills the gap. Financed emissions at the borrower level require activity-based emissions data that is often incomplete.

### ESG Score Trend Monitoring

- URN: urn:financial-services:scenario:risk-control/climate-esg-risk/esg-counterparty-scoring/esg-score-trend-monitoring
- Lens: Insights
- Complexity: S
- Intent: The AI agent monitors ESG score movements across the borrower portfolio on a quarterly basis, flags counterparties with deteriorating ESG scores, and delivers a trend digest to the sustainability team for credit review escalation.
- Problem to solve: ESG counterparty scores are updated when new third-party provider data is received, but the sustainability team has no systematic alert when a borrower's score deteriorates materially between reporting cycles. An ESG downgrade that affects the Bank's taxonomy-based green asset ratio or triggers an ESG covenant review is identified in the next periodic portfolio review rather than at score update.
- Solution: The AI agent reads quarterly ESG score updates from third-party providers, computes score movement per borrower, flags counterparties with material deterioration or controversy additions, and delivers the quarterly trend digest to the sustainability team. The sustainability team confirms the flags and routes those counterparties to credit review for ESG covenant and green asset ratio assessment.
- OKR: The sustainability team escalates deteriorating borrowers to credit review from a quarterly AI-produced ESG score trend digest, rather than discovering downgrades at the next periodic portfolio review.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced trend digest delivered to the sustainability team for ≥4 consecutive quarters within 15 months of go-live; ≥95% of scored borrowers covered in each digest. |
| Acceptance | ≥75% of counterparties flagged for material deterioration or new controversies confirmed by the sustainability team as warranting credit review; ≥90% of confirmed flags routed to credit review within the quarter. |
| Cycle | Score deterioration flagged within 5 business days of each quarterly provider update, versus identification at the next periodic portfolio review. |

### ESG Data Collection Outreach Support

- URN: urn:financial-services:scenario:risk-control/climate-esg-risk/esg-counterparty-scoring/esg-data-collection-outreach-support
- Lens: Automation
- Complexity: S
- Intent: The AI agent drafts outreach communications to borrowers with ESG data gaps, identifies the specific data fields required per borrower, and tracks response status for the sustainability and relationship management teams.
- Problem to solve: ESG scoring gaps for SME and mid-corporate borrowers require direct borrower outreach to collect sustainability metrics. Drafting outreach requests, tracking responses, and following up on non-responses is a relationship management task that the CRM workflow rarely supports systematically.
- Solution: The AI agent reads the ESG scoring gap register, identifies the specific data fields required per borrower, and drafts a tailored outreach communication referencing the borrower's sector and the Bank's ESG data requirements, which the relationship manager reviews and sends. It tracks response status and flags non-responses for relationship manager follow-up after the defined response window.
- OKR: Relationship managers and the sustainability team close ESG data gaps using AI-drafted borrower outreach — tailored to each borrower's sector and the specific data fields required — with response status tracked and non-responses flagged for follow-up.

| Dimension | Key result |
| --- | --- |
| Adoption | AI agent used to draft outreach for ≥90% of borrowers on the ESG scoring gap register within 12 months of go-live; response status tracked for 100% of outreach sent. |
| Acceptance | ≥80% of AI-drafted communications sent by relationship managers with only minor amendment; ≥50% of contacted borrowers returning the requested data within the defined response window. |
| Cycle | Outreach draft available within 2 business days of a borrower entering the gap register, and non-responses flagged at the close of the response window, versus ad hoc requests and follow-up outside the CRM workflow. |

### ESG Counterparty Scoring & Gap Analysis

- URN: urn:financial-services:scenario:risk-control/climate-esg-risk/esg-counterparty-scoring/esg-counterparty-scoring-gap-analysis
- Lens: Insights
- Complexity: M
- Intent: The AI agent assigns ESG scores to borrowers using available third-party data and sector proxies, identifies scoring gaps where borrower data is insufficient, and produces a portfolio-level ESG concentration view.
- Problem to solve: ESG counterparty data is available from third-party providers for large listed borrowers but absent or inconsistent for SME and mid-corporate borrowers. Manual data collection from borrowers is bottlenecked on relationship manager capacity; portfolio-level ESG concentration is not visible between reporting cycles.
- Solution: The AI agent reads third-party ESG rating data, sector carbon intensity benchmarks, and borrower-disclosed sustainability metrics. It assigns ESG scores using available data and sector proxies where borrower data is absent, flags scoring gaps requiring borrower outreach, and produces a portfolio-level ESG concentration view for the sustainability team, which reviews the proxy scores and acts on the gap flags.
- OKR: The sustainability team has a portfolio-level ESG concentration view with AI-assigned counterparty scores for all borrowers — using third-party data where available and sector proxies where not — and a prioritized scoring-gap flag list for outreach.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced ESG scoring covering ≥90% of the credit portfolio by exposure value within 12 months of go-live; portfolio-level ESG concentration view refreshed at least quarterly from go-live. |
| Acceptance | ≥75% of AI-assigned sector proxy scores rated as appropriate by the sustainability team on peer review; scoring-gap flag list actioned for ≥60% of flagged borrowers within 6 months of first production run. |
| Cycle | Full portfolio ESG scoring and gap analysis completed within 3 business days of data refresh, versus a best-efforts manual process that was constrained by relationship manager capacity. |

### Green Finance Pipeline Screening

- URN: urn:financial-services:scenario:risk-control/climate-esg-risk/esg-counterparty-scoring/green-finance-pipeline-screening
- Lens: New opps
- Complexity: M
- Intent: The AI agent screens new lending proposals against green taxonomy eligibility criteria and ESG policy thresholds, flagging eligible transactions for green bond allocation, where the Bank issues green bonds, and non-eligible transactions with the relevant exclusion criterion.
- Problem to solve: Green finance origination requires the sustainability team to review each new deal against the Bank's green taxonomy, external taxonomy alignment criteria (such as the EU taxonomy), and ESG sector exclusion policy. With a high volume of new deals per month, taxonomy screening is performed on a sample basis; eligible transactions go unidentified and green bond issuance capacity is under-utilized.
- Solution: The AI agent reads new deal submissions and screens each against the green taxonomy criteria library, external taxonomy technical screening criteria, and ESG sector exclusion list. It flags eligible transactions for green bond allocation with the eligibility rationale per criterion, and routes non-eligible deals with the applicable exclusion category. The sustainability team reviews flagged deals and finalizes allocation decisions.
- OKR: The sustainability team reviews AI-flagged green taxonomy-eligible transactions for green bond allocation, with non-eligible deals routed with their applicable exclusion criterion, on a per-deal basis across the full new lending pipeline.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's screening applied to ≥95% of new lending submissions within 12 months of go-live; external taxonomy technical screening criteria and ESG sector exclusion list applied in every run. |
| Acceptance | ≥85% of AI-assigned eligibility flags confirmed as accurate by the sustainability team on review; green bond allocation capacity identified per cycle increased by ≥20% versus the prior sampling-based screening approach. |
| Cycle | Taxonomy screening result delivered within 24 hours of new deal submission receipt, enabling same-week eligibility determination rather than batch review on a sampling schedule. |

## Transition risk & carbon exposure {#transition-risk-carbon-exposure}

Transition risk arises from the credit deterioration in high-emission sectors as carbon pricing, regulatory standards, and market preferences shift under decarbonization scenarios. The NGFS transition scenarios — Orderly, Disorderly, and Hot House World — calibrate the speed and smoothness of the policy transition; the credit impact is expressed as sector-level PD and LGD sensitivities under each scenario. Financed emissions — the Bank's share of borrower carbon emissions proportional to financing provided — is the primary metric for portfolio-level transition risk and for TCFD and ISSB disclosure. Supervisory guidelines on climate risk commonly expect transition risk analysis to be integrated into credit risk assessment and ICAAP.

### Financed Emissions Calculation

- URN: urn:financial-services:scenario:risk-control/climate-esg-risk/transition-risk-carbon-exposure/financed-emissions-calculation
- Lens: Automation
- Complexity: M
- Intent: The AI agent computes financed emissions per sector and borrower using PCAF methodology — combining portfolio exposure data with borrower-level carbon intensity where available and sector benchmarks where not — for TCFD disclosure and NGFS transition risk analysis.
- Problem to solve: Financed emissions computation requires matching each portfolio exposure to a carbon intensity estimate and applying the PCAF attribution factor. Borrower-level emissions data is available for a minority of counterparties; sector benchmarks must fill the gap for the remainder. The computation across 1,000–10,000 exposures with mixed data quality requires systematic processing that is not feasible manually on an annual cycle.
- Solution: The AI agent reads portfolio exposure data, borrower-level emissions disclosures where available, and sector carbon intensity benchmarks. It applies the PCAF methodology to compute financed emissions per exposure, aggregates by sector and asset class, and flags the proportion of emissions based on direct data versus proxies. The sustainability and credit risk teams review sector-level outputs before TCFD submission.
- OKR: The sustainability and credit risk teams review AI-computed financed emissions — PCAF methodology applied per exposure, aggregated by sector and asset class, with the share based on direct data versus proxies flagged — before TCFD submission.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's financed emissions calculation covering ≥90% of portfolio exposure by value within 12 months of go-live; PCAF attribution factor applied and data-source flag recorded for every exposure. |
| Acceptance | ≥80% of sector-level outputs accepted by the sustainability and credit risk teams without recalculation; direct-versus-proxy data classification confirmed as accurate in ≥95% of sampled exposures. |
| Cycle | Full-portfolio financed emissions calculation completed within 5 business days of the portfolio data cut, versus an annual computation not feasible manually across the full exposure population. |

### Transition Risk & Carbon Exposure Analysis

- URN: urn:financial-services:scenario:risk-control/climate-esg-risk/transition-risk-carbon-exposure/transition-risk-carbon-exposure-analysis
- Lens: Insights
- Complexity: L
- Intent: The AI agent scores the credit portfolio against NGFS transition scenarios, estimating PD/LGD sensitivities by sector and generating the transition risk and financed-emission narrative for ICAAP and TCFD disclosure.
- Problem to solve: Transition risk quantification requires mapping each portfolio sector to NGFS transition scenarios and estimating PD sensitivity under each; where the Bank uses internal-ratings models, the estimates are cross-referenced to its IRB model parameters. The analysis is performed once or twice per year; the transition risk view does not refresh as the portfolio evolves between ICAAP cycles.
- Solution: The AI agent maps the credit portfolio by sector to NGFS transition scenarios, estimates PD and LGD sensitivities using IRB model outputs, takes in the financed emissions calculated by sector and borrower, and generates the transition risk narrative for ICAAP and TCFD disclosure. The credit risk and ESG teams review scenario assumptions and add strategic context.
- OKR: The credit risk and ESG teams report ICAAP transition risk quantification and TCFD financed-emission disclosure from an AI-produced analysis mapping the full credit portfolio against NGFS transition scenarios with PD/LGD sensitivities estimated from IRB model outputs.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced transition risk analysis covering ≥85% of the credit portfolio by exposure value within 18 months of go-live; all prescribed NGFS transition pathways and the financed-emission narrative produced in every run from go-live. |
| Acceptance | ≥80% of AI-estimated PD/LGD sensitivities accepted by the credit risk team as valid for ICAAP use without major recalculation; TCFD financed-emission figures confirmed as consistent with supervisory disclosure requirements in ≥90% of runs. |
| Cycle | Transition risk and carbon exposure analysis delivered within 5 business days of portfolio data cut, versus a once-or-twice-annual manual exercise consuming ≥4 weeks of quantitative analyst effort. |

### Transition Risk Sector Stress Analysis

- URN: urn:financial-services:scenario:risk-control/climate-esg-risk/transition-risk-carbon-exposure/transition-risk-sector-stress-analysis
- Lens: Enablement
- Complexity: L
- Intent: The AI agent maps the credit portfolio's high-emission sector exposures to NGFS Disorderly transition scenario PD and LGD sensitivities, producing a sector-level stress output for ICAAP and supervisory climate risk reporting.
- Problem to solve: Supervisory climate risk guidelines commonly expect transition risk to be integrated into credit risk assessment, with sector-level PD and LGD sensitivity estimates under NGFS scenarios. Producing these estimates requires combining the credit portfolio sector mapping with published NGFS scenario credit risk parameters — a cross-functional exercise performed on an ad hoc basis rather than in an integrated workflow.
- Solution: The AI agent reads sector exposure data from the credit portfolio, NGFS Disorderly transition scenario credit risk sensitivity parameters by sector, and, where the Bank uses internal-ratings models, its IRB PD and LGD outputs. It computes sector-level transition risk stress outputs — PD uplift and LGD sensitivity by sector under the Disorderly scenario — and produces the input for the ICAAP climate risk section. The credit risk and climate risk teams review scenario parameter choices before ICAAP submission.
- OKR: The credit risk and climate risk teams review an AI-produced sector-level transition stress output — PD uplift and LGD sensitivity for high-emission sectors under the NGFS Disorderly scenario — as the input to the ICAAP climate risk section.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's sector stress analysis produced for ≥1 ICAAP cycle within 18 months of go-live; 100% of high-emission sector exposures covered in every run. |
| Acceptance | ≥75% of sector-level PD and LGD stress outputs accepted by the credit risk and climate risk teams without major recalculation; scenario parameter choices reviewed and confirmed before every ICAAP submission. |
| Cycle | Sector stress output delivered within 5 business days of the portfolio data cut, versus an ad hoc cross-functional exercise with no defined production timeline. |

## TCFD & ISSB disclosure {#tcfd-issb-disclosure}

TCFD (Task Force on Climate-related Financial Disclosures) and ISSB S1/S2 standards define the framework for climate and sustainability disclosure — covering governance, strategy, risk management, and metrics and targets. TCFD-aligned disclosure is mandatory for large banks in a growing number of jurisdictions and is increasingly expected by investors and lenders elsewhere; ISSB S1 and S2 set the global convergence baseline. The disclosure requires assembling financed emissions, physical and transition risk heat maps, governance framework descriptions, and climate scenario analysis summaries from multiple sources. Consistency with prior disclosure commitments — net-zero targets, sector phasedown timelines — must be verified against the current period's metrics.

### TCFD Prior Commitment Tracking

- URN: urn:financial-services:scenario:risk-control/climate-esg-risk/tcfd-issb-disclosure/tcfd-prior-commitment-tracking
- Lens: Insights
- Complexity: S
- Intent: The AI agent reads prior TCFD disclosures and current performance metrics, identifies commitments made in prior years, and produces a commitment-versus-progress tracking report for the sustainability team ahead of the annual disclosure cycle.
- Problem to solve: Each annual TCFD disclosure must be consistent with commitments made in prior-year disclosures — net-zero target timelines, sector phasedown pledges, and green finance volume targets. Tracking prior commitments against current metrics is performed manually; inconsistencies are identified during the editorial review process rather than before drafting begins.
- Solution: The AI agent reads the prior two years of TCFD disclosures, extracts commitments and targets with their reference year and deadline, and cross-references each against current metrics. It produces a commitment-versus-progress table flagging commitments where the current trajectory is inconsistent with the stated target, for the sustainability team to address before disclosure drafting begins.
- OKR: The sustainability team resolves inconsistencies with prior-year commitments before drafting begins, using an AI-produced commitment-versus-progress table built from the prior two years of TCFD disclosures and current metrics.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's commitment tracking report produced ahead of ≥1 annual disclosure cycle within 18 months of go-live; 100% of commitments and targets in the prior two years of disclosures extracted with reference year and deadline. |
| Acceptance | ≥90% of extracted commitments confirmed by the sustainability team as correctly captured; ≥80% of trajectory inconsistency flags confirmed as needing attention in the disclosure draft. |
| Cycle | Commitment-versus-progress table delivered ≥4 weeks before disclosure drafting begins, versus inconsistencies identified during editorial review of the draft. |

### TCFD & ISSB Disclosure Draft

- URN: urn:financial-services:scenario:risk-control/climate-esg-risk/tcfd-issb-disclosure/esg-disclosure-draft
- Lens: Automation
- Complexity: M
- Intent: The AI agent assembles the TCFD and ISSB disclosure draft from sustainability data, portfolio climate metrics, and prior disclosure text, with gap flags and prior-commitment cross-reference, for the sustainability team to validate.
- Problem to solve: Producing the annual TCFD and ISSB disclosure requires assembling financed emissions, governance framework descriptions, climate scenario analysis, and ESG metrics from multiple teams and systems. Data collection, narrative drafting, and prior-commitment cross-referencing consume the sustainability team's cycle capacity.
- Solution: The AI agent reads current ESG metrics, portfolio climate risk summaries, governance framework documentation, and prior TCFD disclosure. It assembles the structured disclosure draft in TCFD/ISSB format, cross-references prior commitments with current progress, and flags disclosure gaps. The sustainability team validates metrics and adds forward-looking commentary before publication.
- OKR: The sustainability team validates metrics and adds forward-looking commentary to an AI-assembled TCFD and ISSB disclosure draft — with gap flags and prior-commitment cross-reference — rather than constructing the document from component inputs.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-assembled disclosure draft used as the base document for ≥1 annual TCFD/ISSB disclosure cycle within 18 months of go-live; prior-commitment cross-reference applied to 100% of commitments from the preceding disclosure. |
| Acceptance | ≥80% of disclosure draft sections accepted by the sustainability team without structural revision; disclosure gap flags rated as accurate by sustainability team reviewers in ≥85% of instances. |
| Cycle | Initial TCFD/ISSB disclosure draft delivered within 5 business days of data cut, reducing the sustainability team's document assembly burden by ≥50% of total cycle time. |

### TCFD Metrics Data Collection & Reconciliation

- URN: urn:financial-services:scenario:risk-control/climate-esg-risk/tcfd-issb-disclosure/tcfd-metrics-data-collection
- Lens: Automation
- Complexity: M
- Intent: The AI agent reads sustainability data from internal systems and third-party ESG data providers, reconciles financed emissions and the other climate metrics across sources, and produces a metrics table aligned to the TCFD and ISSB S2 required disclosure set for the sustainability team's annual review.
- Problem to solve: TCFD and ISSB S2 metrics span financed emissions by sector, physical risk exposure, transition risk concentration, and governance indicators — each sourced from different internal and external data providers. Manual collection and reconciliation across these sources consumes the sustainability team's capacity in the months before the disclosure deadline.
- Solution: The AI agent reads portfolio data, ESG provider feeds, carbon accounting outputs, and governance documentation. It computes the required metrics set, flags data gaps where borrower-level data is unavailable and proxies are applied, and produces the reconciled metrics table in TCFD/ISSB format ready for the sustainability team's editorial review.
- OKR: The sustainability team begins its annual editorial review with an AI-produced reconciled metrics table in TCFD/ISSB format — financed emissions, physical risk exposure, transition risk concentration, and governance indicators — with data gaps and proxies flagged.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's metrics table produced for ≥1 annual disclosure cycle within 18 months of go-live; 100% of the required TCFD and ISSB S2 metrics set covered in the table. |
| Acceptance | ≥85% of metrics accepted by the sustainability team without manual recalculation; data-gap and proxy flags confirmed as accurate in ≥90% of instances. |
| Cycle | Reconciled metrics table delivered within 5 business days of the data cut, versus months of manual collection and reconciliation before the disclosure deadline. |
