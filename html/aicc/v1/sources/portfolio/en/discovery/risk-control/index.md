# Risk & Control

Risk & Control is the Bank's integrated risk-management pillar — a Basel III/IV-aligned taxonomy spanning financial risks (credit, market, liquidity), non-financial risks (operational, compliance & financial crime, cyber, model, strategic & reputational, climate & ESG), and an independent assurance function (internal audit). Under the regulator's supervisory framework, each risk domain carries its own regulatory capital, reporting, and governance obligations; together they constitute the institution's three-lines-of-defense architecture. **The GenAI opportunity is to instrument risk monitoring continuously** — compressing the lag between position movement and management signal from months to days across every domain in the taxonomy.

## Problems

### Financial risks {#financial-risks}

| Lens | Problem |
| --- | --- |
| Insights & analytics | Credit migration and concentration, VaR and sensitivity movements, and LCR and funding runoff signals are each produced by a separate risk system on its own reporting cycle. The CRO lacks a consolidated view of financial risk-appetite consumption between committee cycles; a counterparty approaching its exposure limit, a risk-factor concentration building across desks, or a funding concentration forming is identified only when the next scheduled report surfaces it. |
| Enablement | Sector stress scenarios, stressed VaR narratives, and ILAAP survival-horizon modeling each require credit, market, and treasury risk analysts to assemble exposure, position, and funding data from multiple systems before analysis can begin. The Credit Committee, Market Risk Committee, and ALCO frequently receive the analysis after the meeting it was meant to inform. |
| Automation | ECL provision narratives, PD/LGD/EAD output commentary, daily VaR and P&L attribution narratives, limit utilization reports, and LCR/NSFR management narratives are produced on fixed daily, monthly, or quarterly cycles from structured model and system outputs. Each has a defined format, known source data, and a recurring assembly pattern that makes it a candidate for AI-driven drafting with human review and sign-off. |
| New business opportunities | A continuously instrumented financial risk position — weekly concentration and migration signals, current limit headroom, and a refreshed liquidity survival horizon — lets the CRO, Chief Credit Officer, and Head of Treasury deploy credit appetite, risk budget, and liquidity buffers against the current position rather than last month's report. |

### Non-financial risks {#non-financial-risks}

| Lens | Problem |
| --- | --- |
| Insights & analytics | Operational risk events, AML alert volumes, cyber threat signals, model performance metrics, reputational media mentions, and ESG exposure data each feed separate domain dashboards with their own reporting cycle. The CRO lacks a consolidated view of non-financial risk-budget consumption across these domains between quarterly committee cycles; emerging cross-domain patterns — an operational incident cluster correlated with a model failure, or an ESG transition signal amplifying credit risk — are not detected systematically. |
| Enablement | RCSA refresh, AML model tuning, cyber resilience assessments, model validation exercises, strategic risk scenario analysis, and climate stress tests each require risk officers to assemble data from multiple systems before substantive analysis can begin. Across the non-financial risk domains, data-assembly overhead consumes a material proportion of senior specialist time — compressing the window available for judgment and response. |
| Automation | Regulatory reporting across non-financial risk domains — operational-resilience reports, STR filings, regulatory examination response packs, model risk committee packs, ESG/TCFD disclosures — is produced on fixed cycles from structured inputs. Each report type has a defined format, known source data, and a recurring assembly pattern that makes it a candidate for AI-driven drafting with human review and sign-off. |
| New business opportunities | Banks with continuously instrumented non-financial risk postures — real-time AML disposition rates, weekly cyber exposure scores, monthly ESG portfolio heat maps — can demonstrate supervisory maturity that peers assembling the same picture quarterly cannot. That posture quality translates into faster regulatory approval cycles for new products, reduced supervisory scrutiny, and a reputational advantage in institutional client due-diligence processes. |

## Overview

### Credit risk {#credit-risk}

- Group: Financial risks

| Sub-group | Items |
| --- | --- |
| Counterparty exposure | counterparty-exposure-analytics, pd-lgd-ead-model-outputs, watchlist-early-warning |
| Portfolio concentration & provisions | concentration-sector-risk, vintage-cohort-migration, ecl-ifrs9-provisions |

### Compliance & financial crime {#compliance-financial-crime}

- Group: Non-financial risks

| Sub-group | Items |
| --- | --- |
| AML, sanctions & financial crime | aml-transaction-monitoring, sar-case-management, sanctions-pep-screening |
| Conduct & regulatory adherence | regulatory-licensing-filings, conduct-complaints, regulatory-examination-management |

### Risk Cycles {#risk-cycles}

- Group: Risk governance

| Section | List name | Flows |
| --- | --- | --- |
| Identification & assessment | Identification & assessment | rcsa-cycle, stress-testing-cycle |
| Governance & oversight | Governance & oversight | limits-breach-governance-cycle, risk-reporting-cycle, model-validation-cycle |

### Market risk {#market-risk}

- Group: Financial risks

| Sub-group | Items |
| --- | --- |
| VaR & sensitivity | var-expected-shortfall, sensitivity-greeks-monitoring |
| P&L attribution & limits | pl-attribution-backtesting, market-risk-limits-utilization |

### Liquidity risk {#liquidity-risk}

- Group: Financial risks

| Sub-group | Items |
| --- | --- |
| Funding adequacy & runoff | lcr-nsfr-reporting, intraday-liquidity-monitoring, funding-runoff-concentration |
| Stress & contingency | stress-contingency-funding |

### Operational risk {#operational-risk}

- Group: Non-financial risks

| Sub-group | Items |
| --- | --- |
| Loss events & KRIs | loss-events-near-misses, rcsa-kri-monitoring |
| Third parties & continuity | third-party-tprm, business-continuity-dr |

### Cyber risk {#cyber-risk}

- Group: Non-financial risks

| Sub-group | Items |
| --- | --- |
| Threat & vulnerability exposure | threat-intelligence-exposure, vulnerability-patch-management |
| Response & resilience | incident-detection-response, cyber-resilience-recovery |

### Model risk {#model-risk}

- Group: Non-financial risks

| Sub-group | Items |
| --- | --- |
| Model lifecycle & validation | model-inventory-governance, model-validation |
| Model monitoring & reporting | model-performance-monitoring, model-risk-reporting |
| AI governance | ai-governance |

### Strategic & reputational risk {#strategic-reputational-risk}

- Group: Non-financial risks

| Sub-group | Items |
| --- | --- |
| Strategic decision risk | strategic-decision-risk-analysis, competitive-industry-signals |
| Reputational signal & response | reputational-signal-monitoring, crisis-response-narrative |

### Climate & ESG risk {#climate-esg-risk}

- Group: Non-financial risks

| Sub-group | Items |
| --- | --- |
| Physical & transition risk | physical-risk-assessment, transition-risk-carbon-exposure |
| ESG exposure & disclosure | esg-counterparty-scoring, tcfd-issb-disclosure |

### Internal audit {#internal-audit}

- Group: Independent assurance

| Sub-group | Items |
| --- | --- |
| Audit planning & execution | audit-universe-risk-ranking, audit-execution-workpapers |
| Findings & remediation | findings-thematic-synthesis, remediation-tracking |

## Scenarios

### ICAAP/ILAAP Narrative Assembly

- URN: urn:financial-services:scenario:risk-control/icaap-ilaap-narrative-assembly
- Lens: Automation
- Complexity: L
- Intent: The AI agent assembles the ICAAP and ILAAP narrative chapters from stress model outputs, pillar-by-pillar capital adequacy assessments, and liquidity survival analysis across all risk disciplines, producing a draft document for the CRO and CFO to review before regulatory submission.
- Problem to solve: The ICAAP and ILAAP narrative spans credit, market, liquidity, operational, model, climate, and strategic risk disciplines, each owned by a separate team. Assembling chapters, reconciling cross-references, and producing a coherent CRO narrative statement from fourteen to twenty contributor inputs consumes several weeks of senior risk management coordination per cycle.
- Solution: The AI agent reads stress model outputs, capital adequacy assessments, and liquidity survival narratives from all contributing risk functions. It assembles the prescribed ICAAP/ILAAP structure — risk profile, internal capital adequacy assessment, stress scenario outcomes, management actions, and CRO attestation draft — with cross-references resolved and prior-year comparisons inserted. The CRO and CFO review the assembled document and apply judgment to forward-looking statements before supervisory submission.
- OKR: The CRO and CFO apply enterprise risk judgment to an AI-assembled ICAAP/ILAAP draft — with all prescribed sections populated, cross-references resolved, and prior-year comparisons inserted — rather than coordinating fourteen to twenty contributor inputs.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-assembled ICAAP/ILAAP narrative used as the submission base document for ≥1 annual supervisory submission cycle within 18 months of go-live; all prescribed sections (risk profile, internal capital adequacy assessment, stress outcomes, management actions, CRO attestation draft) covered from go-live. |
| Acceptance | ≥80% of assembled narrative sections accepted by the CRO without structural revision; cross-reference errors between sections identified by supervisors reduced to ≤2 per submission cycle. |
| Cycle | Full ICAAP/ILAAP narrative assembly completed within 5 business days of all contributor inputs received, reducing the overall coordination and assembly phase from ≥4 weeks. |

### Risk Appetite Breach Investigation Pack

- URN: urn:financial-services:scenario:risk-control/risk-appetite-breach-investigation
- Lens: Enablement
- Complexity: M
- Intent: The AI agent assembles the CRO investigation pack when a risk appetite metric breaches its threshold — pulling the current cross-discipline position, breach history, and relevant stress context — so the CRO can respond to the Board or the regulator within the required window.
- Problem to solve: Breaches of risk appetite framework (RAF) metrics require the CRO to present a structured response covering the position that caused the breach, its trajectory, related metrics across disciplines, and a proposed management action. Assembling this context draws on credit, market, liquidity, operational, and capital data from separate reporting systems, typically consuming days of analyst preparation.
- Solution: The AI agent reads the triggered RAF metric, retrieves the current position across all related cross-discipline metrics, surfaces the breach history and trajectory, maps the breach to the relevant stress scenario context, and generates the investigation pack in the Bank's standard RAF response format. The CRO reviews, adds the management action proposal, and presents to the Board Risk Committee or the regulator within the required window.
- OKR: The CRO presents a structured RAF metric breach response — with current cross-discipline position, breach history, and stress context assembled by the AI agent — to the Board Risk Committee or the regulator within the required governance window.

| Dimension | Key result |
| --- | --- |
| Adoption | AI agent used to assemble the CRO investigation pack for ≥90% of RAF metric threshold breaches within 12 months of go-live; all five risk disciplines (credit, market, liquidity, operational, capital) covered in each pack from go-live. |
| Acceptance | ≥80% of AI-assembled investigation packs accepted by the CRO without material supplementation before Board or regulatory presentation; cross-discipline data accuracy confirmed at ≥95% on quality review. |
| Cycle | Investigation pack delivered to the CRO within 4 hours of RAF metric breach notification, versus ≥2 business days of analyst preparation under the prior approach. |

### RAF Threshold Calibration Synthesis

- URN: urn:financial-services:scenario:risk-control/raf-threshold-calibration-synthesis
- Lens: Optimize
- Complexity: M
- Intent: The AI agent analyzes RAF metric performance across the full risk appetite framework — reviewing breach frequency, stress proximity, and portfolio trajectory for each metric — and surfaces candidates where thresholds are misaligned with current portfolio composition or the Bank's stated risk tolerance.
- Problem to solve: RAF threshold reviews are conducted annually as a judgment exercise by each risk discipline owner, without a cross-discipline view of how the full metric set is performing collectively. Thresholds that have become systematically tight or loose relative to actual portfolio risk — visible only in aggregate across credit, market, liquidity, and capital metrics — are identified by exception rather than by design.
- Solution: The AI agent reads 24 months of RAF metric performance data across all disciplines, computes breach frequency, distance-to-threshold distribution, and portfolio trend for each metric, and identifies candidates where recalibration is warranted. It cross-references each candidate against the Bank's risk tolerance statement and peer benchmark ranges, and produces a calibration review pack for the CRO and Board Risk Committee. Risk discipline owners review the flagged candidates and confirm or adjust thresholds before the annual RAF update.
- OKR: The CRO and Board Risk Committee receive an AI-produced RAF threshold calibration review pack — with candidates identified by breach frequency, stress proximity, and portfolio trajectory across all risk disciplines — ahead of each annual RAF update.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced calibration review pack incorporating 24 months of RAF metric performance data delivered for ≥1 annual RAF update cycle within 18 months of go-live; all four risk discipline categories (credit, market, liquidity, capital) covered in every run. |
| Acceptance | ≥70% of AI-identified recalibration candidates confirmed by risk discipline owners as warranting threshold review; ≥1 material RAF threshold adjustment per annual update attributable to an AI-identified metric performance signal. |
| Cycle | Calibration review pack delivered within 5 business days of annual performance data cut, versus an annual judgment exercise by each risk discipline owner with no defined completion date under the prior approach. |

### Regulatory Capital Efficiency Signal Detection

- URN: urn:financial-services:scenario:risk-control/regulatory-capital-efficiency-signals
- Lens: New opps
- Complexity: M
- Intent: The AI agent scans the Bank's risk-weighted asset composition across credit, market, and operational risk to identify structural capital inefficiencies — dense RWA pockets, model methodology gaps, and collateral recognition shortfalls — and presents a ranked signal set to the CRO and CFO ahead of the ICAAP capital planning window.
- Problem to solve: RWA optimization opportunities are assessed separately by credit risk (collateral recognition), market risk (methodology selection), and operational risk (SMA calibration) — and, where the Bank uses or may apply for internal models, by IRB eligibility and the choice between SA and IMA. The CRO and CFO have no integrated cross-discipline view of where capital efficiency improvements are achievable within current regulatory permissions until the ICAAP capital planning cycle is already underway.
- Solution: The AI agent reads RWA composition and density data from credit, market, and operational risk systems, applies the Bank's current regulatory permission set, and identifies candidates where model methodology upgrades, improved collateral documentation, or netting agreement enhancements would reduce capital requirements within permitted bounds. It ranks signals by estimated RWA impact and regulatory feasibility and delivers the pack to the CRO and CFO ahead of the ICAAP capital planning cycle. The risk and finance teams validate estimates and commission the highest-priority workstreams.
- OKR: The CRO and CFO enter the ICAAP capital planning window with an AI-produced ranked signal set identifying RWA inefficiencies — across credit collateral recognition and IRB eligibility, market risk methodology, and operational risk SMA calibration — with estimated RWA impact and regulatory feasibility scores.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's capital efficiency signal analysis produced ahead of ≥1 ICAAP capital planning cycle within 18 months of go-live; all three RWA disciplines (credit, market, operational) covered in every run from go-live. |
| Acceptance | ≥65% of AI-ranked signals confirmed as material by the CRO and CFO on review; ≥1 RWA optimization workstream per annual planning cycle initiated from AI-identified signals. |
| Cycle | Capital efficiency signal pack delivered ≥4 weeks before the ICAAP capital planning window opens — rather than once the planning cycle is already underway — enabling the risk and finance teams to commission feasibility analysis before the planning cycle constrains the calendar. |

### CRO Risk Synthesis

- URN: urn:financial-services:scenario:risk-control/cro-risk-synthesis
- Lens: Insights
- Complexity: L
- Intent: The AI agent synthesizes stress-test outputs, cross-domain emerging risk signals, and adverse scenario narratives into a structured Board Risk Committee pack for the CRO. The pack spans credit, market, liquidity, operational, and other non-financial risk disciplines in a single coherent view.
- Problem to solve: The CRO must present a coherent enterprise-wide risk picture to the Board Risk Committee covering all material risk disciplines. Stress-test narratives are drafted separately by the risk modeling team; emerging risk signals are monitored in domain silos; crisis narrative frameworks are assembled reactively. Assembling these into a single board-ready view consumes senior risk management hours in the week before each meeting.
- Solution: The AI agent reads stress-test model outputs and applies the Bank's standard narrative framework — portfolio impact, key drivers, comparison to prior runs, and regulatory threshold commentary. It aggregates cross-domain emerging risk signals from external intelligence, peer analysis, and internal monitoring, and maintains pre-drafted stakeholder-specific crisis narrative frameworks for plausible adverse scenarios. The CRO reviews the synthesized pack and applies enterprise risk judgment before Board Risk Committee submission.
- OKR: The CRO presents the Board Risk Committee with an AI-synthesized enterprise risk pack — spanning credit, market, liquidity, operational, and other non-financial risk — reviewed and judgment-annotated by the CRO rather than assembled from scratch.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-synthesized Board Risk Committee pack used for ≥6 committee meetings in year 1; all material risk disciplines covered in each pack from go-live. |
| Acceptance | ≥80% of synthesized pack sections accepted by the CRO without structural revision; pre-drafted crisis narrative frameworks rated as deployable without major revision in ≥75% of scenarios reviewed. |
| Cycle | Full board pack synthesis completed within 2 business days of input data availability, reducing senior risk management assembly time from ≥5 days to ≤1 day of CRO editorial review. |
