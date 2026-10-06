# 

source: html-alt/financial-services/en/risk-control/index.html


[PAGE TEXT]
Financial risks
Credit risk (19)
Counterparty exposure
Counterparty exposure analytics (3)
·
PD/LGD/EAD model outputs (3)
·
Watchlist & early-warning (4)
Concentration sector
Concentration & sector risk (3)
·
Vintage cohort & migration (3)
·
ECL & IFRS 9 provisions (3)
Non-financial risks
Compliance & financial crime (18)
Aml sanctions financial crime
AML transaction monitoring (3)
·
SAR & case management (3)
·
Sanctions & PEP screening (3)
Conduct regulatory adherence
Regulatory licensing & filings (3)
·
Conduct & complaints (3)
·
Regulatory examination management (3)
Risk governance
Risk Cycles (25)
Identification & assessment
RCSA cycle (risk & control self-assessment) (5)
Stress testing cycle (ICAAP, ILAAP, climate) (5)
Governance & oversight
Limits & breach governance cycle (5)
Risk reporting cycle (ERMC & board) (5)
Model validation cycle (SR 11-7) (5)
Financial risks
Market risk (12)
Var sensitivity
VaR & expected shortfall (3)
·
Sensitivity & Greeks monitoring (3)
Pl attribution backtest
P&L attribution & backtesting (3)
·
Market risk limits utilization (3)
Financial risks
Liquidity risk (12)
Funding adequacy runoff
LCR & NSFR reporting (3)
·
Intraday liquidity monitoring (3)
·
Funding runoff & concentration (3)
Stress contingency
Stress & contingency funding (3)
Non-financial risks
Operational risk (12)
Loss events kris
Loss events & near-misses (3)
·
RCSA & KRI monitoring (3)
Control testing tprm
Third-party & TPRM (3)
·
Business continuity & DR (3)
Non-financial risks
Cyber risk (12)
Threat exposure detection
Threat intelligence & exposure (3)
·
Vulnerability & patch management (3)
Resilience response
Incident detection & response (3)
·
Cyber resilience & recovery (3)
Non-financial risks
Model risk (12)
Model lifecycle validation
Model inventory & governance (3)
·
Model validation (3)
Model performance monitoring
Model performance monitoring (3)
·
Model risk reporting (3)
Non-financial risks
Strategic & reputational risk (12)
Strategic decision risk
Strategic-decision risk analysis (3)
·
Competitive & industry signals (3)
Reputational signal response
Reputational signal monitoring (3)
·
Crisis response & narrative (3)
Non-financial risks
Climate & ESG risk (13)
Physical transition risk
Physical risk assessment (3)
·
Transition risk & carbon exposure (3)
Esg exposure disclosure
ESG counterparty scoring (4)
·
TCFD & ISSB disclosure (3)
Independent assurance
Internal audit (12)
Audit planning execution
Audit universe & risk ranking (3)
·
Audit execution & workpapers (3)
Findings remediation
Findings & thematic synthesis (3)
·
Remediation tracking (3)
Scenarios
Lens
Scenario
Intent
Complexity

### CARD 1 [Automation|M] ICAAP/ILAAP Narrative Assembly
urn: urn:financial-services:scenario:risk-control/icaap-ilaap-narrative-assembly
intent: Agent assembles the ICAAP and ILAAP narrative chapters from stress model outputs, pillar-by-pillar capital adequacy assessments, and liquidity survival analysis across all risk disciplines, producing a draft document for the CRO and CFO to review before regulatory submission.
Problem to solve: The ICAAP and ILAAP narrative spans credit, market, liquidity, operational, model, climate, and strategic risk disciplines, each owned by a separate team. Assembling chapters, reconciling cross-references, and producing a coherent CRO narrative statement from fourteen to twenty contributor inputs consumes several weeks of senior risk management coordination per cycle.
Solution: Agent reads stress model outputs, capital adequacy assessments, and liquidity survival narratives from all contributing risk functions. It assembles the prescribed ICAAP/ILAAP structure — risk profile, internal capital adequacy assessment, stress scenario outcomes, management actions, and CRO attestation draft — with cross-references resolved and prior-year comparisons inserted. The CRO and CFO review the assembled document and apply judgement to forward-looking statements before supervisory submission.
OKR objective: The CRO and CFO apply enterprise risk judgement to an agent-assembled ICAAP/ILAAP draft — with all prescribed sections populated, cross-references resolved, and prior-year comparisons inserted — rather than coordinating fourteen to twenty contributor inputs.
OKR KR [Adoption]: Agent-assembled ICAAP/ILAAP narrative used as the submission base document for ≥1 annual supervisory submission cycle within 18 months of go-live; all prescribed sections (risk profile, ICAA, stress outcomes, management actions, CRO attestation draft) covered from go-live.
OKR KR [Acceptance]: ≥80% of assembled narrative sections accepted by the CRO without structural revision; cross-reference errors between sections identified by supervisors reduced to ≤2 per submission cycle.
OKR KR [Cycle]: Full ICAAP/ILAAP narrative assembly completed within 5 business days of all contributor inputs received, reducing the overall coordination and assembly phase from ≥4 weeks.

### CARD 2 [Enablement|M] Risk Appetite Breach Investigation Pack
urn: urn:financial-services:scenario:risk-control/risk-appetite-breach-investigation
intent: Agent assembles the CRO investigation pack when a risk appetite metric breaches its threshold — pulling the current cross-discipline position, breach history, and relevant stress context — so the CRO can respond to the Board or regulator within the required window.
Problem to solve: RAF metric breaches require the CRO to present a structured response covering the position that caused the breach, its trajectory, related metrics across disciplines, and a proposed management action. Assembling this context draws on credit, market, liquidity, operational, and capital data from separate reporting systems, typically consuming days of analyst preparation.
Solution: Agent reads the triggered RAF metric, retrieves the current position across all related cross-discipline metrics, surfaces the breach history and trajectory, maps the breach to the relevant stress scenario context, and generates the investigation pack in the bank's standard RAF response format. The CRO reviews, adds the management action proposal, and presents to the Board Risk Committee or regulator within the required window.
OKR objective: The CRO presents a structured RAF metric breach response — with current cross-discipline position, breach history, and stress context assembled by the agent — to the Board Risk Committee or regulator within the required governance window.
OKR KR [Adoption]: Agent used to assemble the CRO investigation pack for ≥90% of RAF metric threshold breaches within 12 months of go-live; all five risk disciplines (credit, market, liquidity, operational, capital) covered in each pack from go-live.
OKR KR [Acceptance]: ≥80% of agent-assembled investigation packs accepted by the CRO without material supplementation before Board or regulatory presentation; cross-discipline data accuracy confirmed at ≥95% on quality review.
OKR KR [Cycle]: Investigation pack delivered to the CRO within 4 hours of RAF metric breach notification, versus ≥2 business days of analyst preparation under the prior approach.

### CARD 3 [Optimize|M] RAF Threshold Calibration Synthesis
urn: urn:financial-services:scenario:risk-control/raf-threshold-calibration-synthesis
intent: Agent analyses RAF metric performance across the full risk appetite framework — reviewing breach frequency, stress proximity, and portfolio trajectory for each metric — and surfaces candidates where thresholds are misaligned with current portfolio composition or the bank's stated risk tolerance.
Problem to solve: RAF threshold reviews are conducted annually as a judgement exercise by each risk discipline owner, without a cross-discipline view of how the full metric set is performing collectively. Thresholds that have become systematically tight or loose relative to actual portfolio risk — visible only in aggregate across credit, market, liquidity, and capital metrics — are identified by exception rather than by design.
Solution: Agent reads 24 months of RAF metric performance data across all disciplines, computes breach frequency, distance-to-threshold distribution, and portfolio trend for each metric, and identifies candidates where recalibration is warranted. It cross-references each candidate against the bank's risk tolerance statement and peer benchmark ranges, and produces a calibration review pack for the CRO and Board Risk Committee. Risk discipline owners review the flagged candidates and confirm or adjust thresholds before the annual RAF update.
OKR objective: The CRO and Board Risk Committee receive an agent-produced RAF threshold calibration review pack — with candidates identified by breach frequency, stress proximity, and portfolio trajectory across all risk disciplines — ahead of each annual RAF update.
OKR KR [Adoption]: Agent calibration review pack incorporating 24 months of RAF metric performance data produced for ≥1 annual RAF update cycle within 18 months of go-live; all four risk discipline categories (credit, market, liquidity, capital) covered in every run.
OKR KR [Acceptance]: ≥70% of agent-identified recalibration candidates confirmed by risk discipline owners as warranting threshold review; ≥1 material RAF threshold adjustment per annual update attributable to agent-identified metric performance signal.
OKR KR [Cycle]: Calibration review pack delivered within 5 business days of annual performance data cut, replacing a manual judgement exercise with no defined analytical cycle completion date.

### CARD 4 [New opps|M] Regulatory Capital Efficiency Signal Detection
urn: urn:financial-services:scenario:risk-control/regulatory-capital-efficiency-signals
intent: Agent scans the bank's risk-weighted asset composition across credit, market, and operational risk to identify structural capital inefficiencies — dense RWA pockets, model methodology gaps, and collateral recognition shortfalls — and presents a ranked signal set to the CRO and CFO ahead of the ICAAP capital planning window.
Problem to solve: RWA optimisation opportunities are assessed separately by credit risk (IRB eligibility, collateral recognition), market risk (SA/IMA methodology selection), and operational risk (SMA calibration). The CRO and CFO have no integrated cross-discipline view of where capital efficiency improvements are achievable within current regulatory permissions until the ICAAP capital planning cycle is already underway.
Solution: Agent reads RWA composition and density data from credit, market, and operational risk systems, applies the bank's current regulatory permission set, and identifies candidates where model methodology upgrades, improved collateral documentation, or netting agreement enhancements would reduce capital requirements within permitted bounds. It ranks signals by estimated RWA impact and regulatory feasibility and delivers the pack to the CRO and CFO ahead of the ICAAP capital planning cycle. The risk and finance teams validate estimates and commission the highest-priority workstreams.
OKR objective: The CRO and CFO enter the ICAAP capital planning window with an agent-produced ranked signal set identifying RWA inefficiencies — across credit IRB eligibility, market risk methodology, and operational risk SMA calibration — with estimated RWA impact and regulatory feasibility scores.
OKR KR [Adoption]: Agent capital efficiency signal analysis produced ahead of ≥1 ICAAP capital planning cycle within 18 months of go-live; all three RWA disciplines (credit, market, operational) covered in every run from go-live.
OKR KR [Acceptance]: ≥65% of agent-ranked signals confirmed as material by the CRO and CFO on review; ≥1 RWA optimisation workstream per annual planning cycle initiated from agent-identified signals.
OKR KR [Cycle]: Capital efficiency signal pack delivered ≥4 weeks before the ICAAP capital planning window opens, enabling the risk and finance teams to commission feasibility analysis before the planning cycle constrains the calendar.

### CARD 5 [Insights|L] CRO Risk Synthesis
urn: urn:financial-services:scenario:risk-control/cro-risk-synthesis
intent: Agent synthesises stress-test outputs, cross-domain emerging risk signals, and adverse scenario narratives into a structured Board Risk Committee pack for the CRO. The pack spans credit, market, liquidity, operational, and non-financial risk disciplines in a single coherent view.
Problem to solve: The CRO must present a coherent enterprise-wide risk picture to the Board Risk Committee covering all material risk disciplines. Stress-test narratives are drafted separately by the risk modelling team; emerging risk signals are monitored in domain silos; crisis narrative frameworks are assembled reactively. Assembling these into a single board-ready view consumes senior risk management hours in the week before each meeting.
Solution: Agent reads stress-test model outputs and applies the bank's standard narrative framework — portfolio impact, key drivers, comparison to prior runs, and regulatory threshold commentary. It aggregates cross-domain emerging risk signals from external intelligence, peer analysis, and internal monitoring, and maintains pre-drafted stakeholder-specific crisis narrative frameworks for plausible adverse scenarios. The CRO reviews the synthesised pack and applies enterprise risk judgement before Board Risk Committee submission.
OKR objective: The CRO presents the Board Risk Committee with an agent-synthesised enterprise risk pack — spanning credit, market, liquidity, operational, and non-financial risk — reviewed and judgement-annotated by the CRO rather than assembled from scratch.
OKR KR [Adoption]: Agent-synthesised Board Risk Committee pack used for ≥6 committee meetings in year 1; all material risk disciplines covered in each pack from go-live.
OKR KR [Acceptance]: ≥80% of synthesised pack sections accepted by the CRO without structural revision; pre-drafted crisis narrative frameworks rated as deployable without major revision in ≥75% of scenarios reviewed.
OKR KR [Cycle]: Full board pack synthesis completed within 2 business days of input data availability, reducing senior risk management assembly time from ≥5 days to ≤1 day of CRO editorial review.

[PAGE TEXT]
GenAI-enabled Banking and Financial Services Framework · v11i
