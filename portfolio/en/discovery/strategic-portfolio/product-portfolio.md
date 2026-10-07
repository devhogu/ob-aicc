# Product portfolio

Product portfolio defines the mix of banking products the Bank offers — how each product is positioned, priced, and structured across the liability, asset, and fee-income stacks — and governs the lifecycle decisions (launch, reprice, retire) that determine portfolio composition over time. Product P&L, cross-sell penetration, share-of-wallet, and cannibalization dynamics are the operating measures that govern the portfolio's health. **The opportunity for GenAI is to deliver continuous product-economics visibility at the product-variant level, accelerate product-mix what-ifs across changing market conditions, and compress the cycle from product-design signal to executive decision.**

## Problems

### Product portfolio {#product-portfolio}

| Lens | Problem |
| --- | --- |
| Insights & analytics | Product economics for lending, deposits, cards, investment, insurance, and treasury services are assembled monthly or quarterly at aggregate level. Product-variant and segment-level margins, net flows, and penetration are not produced routinely, so mix shifts and cannibalization are identified only after they appear in the P&L. |
| Enablement | Product heads and relationship managers depend on analysts and product specialists for product-mix what-ifs, suitability boundaries, treasury coverage guidance, and competitor benchmarks. Turnaround takes days, so pricing decisions and sales conversations proceed without them. |
| Automation | Deposit product lifecycle reviews and bancassurance partner performance packs are assembled manually from three or four source systems on an annual or quarterly cycle. Below-threshold products persist for months, and partner reviews proceed without current data. |
| New business opportunities | Regulatory windows for new investment products and cross-sell or bundling opportunities across treasury services are identified ad hoc, often after competitors have moved. With continuous monitoring and fee-income impact estimated per opportunity, the Bank can time launches and prioritize the pipeline within the current commercial cycle. |

## Lending products {#lending-products}

The lending portfolio encompasses the full asset-side product range — mortgage, consumer, SME, corporate, and syndicated loans, along with trade finance and overdraft facilities — measured on outstandings, NIM, origination volume, credit loss rate, and risk-adjusted return by product type. Lending product decisions span pricing policy, underwriting criteria, portfolio limits by product and sector, and lifecycle management from origination through workout and recovery.

### Lending Product P&L Attribution

- URN: urn:financial-services:scenario:strategic-portfolio/product-portfolio/lending-products/lending-product-pl-attribution
- Lens: Insights
- Complexity: M
- Intent: Per-product P&L covering NIM, credit cost, and origination volume drivers is auto-drafted from finance and risk feeds on a weekly cadence. Margin movements are attributed by driver and surface to the product head without manual assembly.
- Problem to solve: Retail and SME lending-product P&L is assembled manually each cycle. The product team lacks continuous visibility into which products — by tenor, segment, and geography — are driving margin compression or expansion, and cross-product cannibalization is identified only at quarterly reviews.
- Solution: The AI agent reads origination data, credit cost, and NIM signals across the lending product stack and produces a weekly per-product P&L narrative. The product head reviews the attribution and focuses on forward pricing decisions while the AI agent maintains the attribution baseline.
- OKR: Per-product P&L covering NIM, credit cost, and origination volume drivers is auto-drafted from finance and risk feeds on a weekly cadence with margin-movement attribution by driver — giving the product head a continuous view in place of quarterly manual assembly.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces weekly lending P&L attribution narratives for ≥50 consecutive weeks per year; all products by tenor, segment, and geography covered in ≥95% of weekly outputs. |
| Acceptance | ≥85% of weekly attributions accepted by the product head as accurate without manual re-derivation; NIM driver attribution confirmed consistent with subsequent quarterly P&L actuals in ≥85% of reviewed weeks. |
| Cycle | Lending product P&L attribution cycle reduced from quarterly manual assembly to a weekly view, with margin compression signals available ≥10 weeks earlier per quarter. |

### Lending product pricing optimization

- URN: urn:financial-services:scenario:strategic-portfolio/product-portfolio/lending-products/lending-product-pricing-optimisation
- Lens: Optimize
- Complexity: M
- Intent: Lending product pricing must balance risk-adjusted return, competitive positioning, and volume objectives across the credit cycle. The AI agent models repricing scenarios across the lending product suite — mortgage, SME, consumer, and corporate — estimating RAROC impact, volume elasticity, and portfolio mix implications for the ALCO pricing committee.
- Problem to solve: Lending pricing decisions are made by separate product teams using inconsistent RAROC models; the portfolio-level impact of simultaneous repricing across products is not modeled, and volume elasticity assumptions are not validated against recent origination data.
- Solution: The AI agent runs a standardized repricing scenario grid across all lending products using a common RAROC framework, applying volume elasticity estimates calibrated to recent origination data. Each scenario delivers RAROC, estimated volume impact, and portfolio mix change for ALCO review.
- OKR: Lending repricing decisions are supported by a standardized cross-product scenario grid produced within two business days of a repricing trigger.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced repricing scenarios used in ≥80% of ALCO lending pricing reviews within 12 months of deployment. |
| Acceptance | ≥75% of repricing scenarios accepted by the ALCO pricing committee as the basis for deliberation without material re-derivation. |
| Cycle | Cross-product repricing scenario pack production time reduced from ≥5 days to ≤2 business days. |

### Lending product-mix what-if sandbox

- URN: urn:financial-services:scenario:strategic-portfolio/product-portfolio/lending-products/lending-product-mix-optimisation
- Lens: Enablement
- Complexity: L
- Intent: A what-if sandbox covers the full lending product stack by segment, tenor, and geography. Product heads explore repricing scenarios, LTV-band adjustments, and, where the Bank offers them, Islamic-product variants, with NIM and volume impact rendered simultaneously.
- Problem to solve: Product-mix decisions for the lending book — repricing a mortgage tenor, adjusting SME revolving-facility limits, or modeling murabaha structures — require multi-day modeling exercises. Product heads have limited ability to test pricing changes without booking analyst time.
- Solution: A sandbox backed by the AI agent accepts parameter changes from product heads across the lending product stack and renders NIM and volume impact simultaneously. Analyst follow-up is reserved for scenarios requiring regulatory-capital sensitivity validation.
- OKR: A what-if sandbox covering the full lending product stack by segment, tenor, and geography allows product heads to explore repricing scenarios, LTV-band adjustments, and Islamic-product variants with NIM and volume impact rendered simultaneously — removing the multi-day modeling cycle from product-strategy sessions.

| Dimension | Key result |
| --- | --- |
| Adoption | Sandbox in active use for ≥12 product-strategy sessions in year 1; parameter change to simultaneous NIM and volume output delivered within 30 minutes for ≥90% of sandbox runs. |
| Acceptance | ≥80% of sandbox scenario outputs accepted by product heads as analytically sound without requiring full analyst re-derivation; model error rate on regulatory-capital sensitivity validation checks ≤3%. |
| Cycle | Per-scenario product-mix modeling cycle reduced from multi-day analyst exercises to ≤30 minutes per sandbox run. |

## Investment products {#investment-products}

Investment products — mutual funds, structured products, bonds, and brokerage services distributed to Retail, Wealth, and Corporate clients — generate fee and commission income and deepen the Bank's share of financial asset wallet. Portfolio management tracks AUM, net sales flow, fee yield, and product suitability compliance under applicable securities-market regulation. Product mix decisions balance income generation against the fiduciary and conduct risk obligations of investment intermediation.

### Investment product AUM mix insights

- URN: urn:financial-services:scenario:strategic-portfolio/product-portfolio/investment-products/investment-product-aum-mix-insights
- Lens: Insights
- Complexity: S
- Intent: AUM mix across investment product categories — structured deposits, mutual funds, discretionary mandates, and capital market products — determines fee income trajectory and the Bank's positioning in the wealth value chain. The AI agent tracks AUM composition, net flows, and margin per product category in continuous form, surfacing mix shifts before they affect fee income materially.
- Problem to solve: Investment product AUM mix is reviewed monthly at an aggregate level; product-category net flows and margin trends are not visible between reviews. By the time a mix shift is identified, the fee income impact is already evident in the P&L.
- Solution: The AI agent integrates AUM, net flow, and fee income data by investment product category on a weekly basis, producing a mix dashboard with trend signals per category. Categories with sustained net outflows or margin compression trigger a flag for the investment product committee.
- OKR: Investment product AUM mix and net flow trends are visible to the investment product committee on a weekly basis, enabling pre-emptive product and pricing responses to mix deterioration.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces weekly AUM mix dashboards covering ≥90% of active investment product categories from deployment. |
| Acceptance | ≥80% of weekly dashboards accepted by the investment product committee as accurate without material data reconciliation. |
| Cycle | AUM mix visibility cycle compressed from monthly aggregate to weekly product-category level. |

### Investment product regulatory window opportunities

- URN: urn:financial-services:scenario:strategic-portfolio/product-portfolio/investment-products/investment-product-new-opps-regulatory-window
- Lens: New opps
- Complexity: M
- Intent: Regulatory changes — new investment product licensing frameworks, changes to collective investment scheme rules, securities market liberalization — create windows for banks to launch new investment product categories ahead of competitors. The AI agent monitors regulatory developments from the securities-market regulator, identifying product opportunity windows and estimating market timing.
- Problem to solve: Regulatory window monitoring for investment products is performed ad hoc by the product development team; windows are often identified late, after competitors have already moved. There is no structured process for translating regulatory changes into product opportunity assessments.
- Solution: The AI agent monitors securities market and investment fund regulatory publications, classifies changes by product opportunity type, and produces a quarterly opportunity assessment for the investment product committee. Each opportunity includes an estimated window duration and competitive timing estimate.
- OKR: Investment product regulatory windows are identified and assessed within four weeks of the relevant regulatory publication, giving the product development team a first-mover opportunity to respond.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent assesses ≥90% of relevant securities-market and investment-fund regulatory publications within four weeks of publication and consolidates them into a quarterly opportunity assessment for the investment product committee. |
| Acceptance | ≥70% of opportunity assessments accepted by the investment product committee as actionable and warranting a product feasibility review. |
| Cycle | Regulatory window identification-to-assessment time reduced from ≥8 weeks to ≤4 weeks. |

### Investment product suitability assessment enablement

- URN: urn:financial-services:scenario:strategic-portfolio/product-portfolio/investment-products/investment-product-client-suitability-enablement
- Lens: Enablement
- Complexity: M
- Intent: Investment product suitability assessment requires relationship managers (RMs) to match client risk profiles with eligible product categories under the applicable investor-protection and conduct rules. The AI agent provides RM-facing guidance on suitability boundaries per product and client risk tier, reducing conduct risk while accelerating the sales conversation.
- Problem to solve: Relationship managers must navigate complex suitability rules that vary by product and client risk tier; inconsistent application is a conduct risk and a common source of supervisory examination findings. Training alone is insufficient to maintain consistent suitability practice across a distributed RM network.
- Solution: The AI agent provides a real-time suitability guidance tool for RMs, accepting client risk tier and product of interest as inputs and returning the applicable suitability boundary, documentation requirement, and disclosure language for that combination. Exceptions require documented approval, and compliance samples the guidance responses for correctness.
- OKR: RM-facing suitability guidance is available at point of sale for all investment product categories, reducing conduct exceptions attributable to suitability misapplication.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent's suitability tool used in ≥60% of investment product sales conversations within 12 months of deployment. |
| Acceptance | ≥90% of suitability guidance responses confirmed correct on compliance sampling; conduct exception rate attributable to suitability misapplication reduced by ≥50% from the prior-year baseline. |
| Cycle | RM suitability check time reduced from ≥10 minutes of manual reference to ≤2 minutes per transaction. |

## Deposit products {#deposit-products}

Deposit products form the liability side of the Bank's balance sheet — covering demand accounts, savings, term deposits, and notice accounts across Retail, SME, Corporate, and Treasury segments. Deposit portfolio management governs funding cost, maturity structure, repricing sensitivity under ALCO policy, and the contribution of deposit balances to LCR and NSFR compliance in line with the Basel III liquidity standards. Product economics are measured by cost of funds, retention rates, and cross-sell conversion from the deposit base.

### Deposit portfolio economics insights

- URN: urn:financial-services:scenario:strategic-portfolio/product-portfolio/deposit-products/deposit-portfolio-economics-insights
- Lens: Insights
- Complexity: S
- Intent: Deposit portfolio economics — cost of funds, behavioral duration, balance stability, and cross-sell penetration — determine the Bank's funding efficiency and the strategic value of each deposit product. The AI agent synthesizes deposit P&L and behavioral analytics into a continuous product-level economics view for the ALCO and product management committee.
- Problem to solve: Deposit product economics are assembled quarterly from FTP system outputs and segmentation data; between cycles, rate movements and balance shifts are not reflected in the product-level P&L picture. ALCO decisions on deposit pricing are made without a current view of cost-of-funds implications by product.
- Solution: The AI agent integrates FTP rates, deposit balance data, and behavioral duration models on a monthly basis to produce a cost-of-funds and margin view per deposit product. Products with deteriorating economics or balance outflows are flagged for repricing review, and the ALCO secretariat checks each report before pricing deliberation.
- OKR: Deposit product economics are visible at the product level on a monthly basis, enabling ALCO pricing decisions grounded in current cost-of-funds data.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces monthly deposit economics reports covering ≥90% of active deposit product variants from deployment. |
| Acceptance | ≥80% of reports accepted by the ALCO secretariat as accurate and sufficient for pricing deliberation. |
| Cycle | Deposit product economics visibility compressed from quarterly assembly to a monthly read. |

### Deposit product lifecycle review

- URN: urn:financial-services:scenario:strategic-portfolio/product-portfolio/deposit-products/deposit-product-lifecycle-review-automation
- Lens: Automation
- Complexity: S
- Intent: Deposit products that are below minimum volume thresholds or cost-inefficient to maintain consume operational resources without contributing to the funding strategy. The AI agent automates the quarterly lifecycle review, scoring each deposit product against volume, profitability, and strategic fit criteria, and generating a prioritized list for retirement or redesign.
- Problem to solve: Deposit product lifecycle reviews are conducted annually as part of the product governance cycle; products that fall below viability thresholds persist for months before being reviewed, consuming servicing cost and creating customer confusion.
- Solution: The AI agent runs a quarterly lifecycle review across all deposit products, scoring each on balance volume trend, cost-of-funds contribution, cross-sell rate, and operational complexity. Products scoring below the retirement threshold are flagged with a draft retirement rationale for the product governance committee.
- OKR: Below-threshold deposit products are identified and referred to the product governance committee on a quarterly basis, reducing the average time-to-retirement by half.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces quarterly lifecycle reviews covering 100% of active deposit products from deployment. |
| Acceptance | ≥80% of lifecycle reports accepted by the product governance committee as accurate and sufficient for retirement decisions. |
| Cycle | Deposit product lifecycle review cycle compressed from annual to quarterly. |

### Deposit pricing scenario optimization

- URN: urn:financial-services:scenario:strategic-portfolio/product-portfolio/deposit-products/deposit-pricing-scenario-optimisation
- Lens: Optimize
- Complexity: M
- Intent: Deposit pricing decisions require balancing funding cost, balance retention, and competitive positioning across the rate cycle. The AI agent models repricing scenarios across the deposit product suite, estimating balance elasticity, cost-of-funds impact, and ALCO-relevant sensitivities for each scenario.
- Problem to solve: Deposit repricing analysis is produced ad hoc by the treasury and product teams using separate models; assumptions on balance elasticity are inconsistent across products and not validated against observed customer behavior. ALCO receives pricing recommendations without a structured sensitivity analysis.
- Solution: The AI agent runs a standardized repricing scenario grid across all deposit products, applying behavioral elasticity estimates calibrated to recent balance flow data. Each scenario delivers cost-of-funds impact, estimated balance retention, and net funding benefit; treasury and product management review it before ALCO deliberation.
- OKR: Deposit repricing decisions are supported by a standardized scenario grid produced within two business days of a repricing trigger.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced repricing scenarios used in ≥80% of ALCO deposit pricing reviews within 12 months of deployment. |
| Acceptance | ≥75% of repricing scenarios accepted by treasury and product management as analytically sound for ALCO deliberation. |
| Cycle | Repricing scenario pack production time reduced from ≥5 days to ≤2 business days. |

## Insurance products {#insurance-products}

Insurance products distributed through or manufactured by the Bank — including life, general, credit life, and bancassurance arrangements — represent a fee-income and cross-sell layer on top of the core banking product set. Portfolio management covers distribution penetration rates, commission and fee income per product, claims ratio for underwritten products, and the regulatory framework governing insurance intermediary activity under applicable financial services licensing rules.

### Insurance product penetration insights

- URN: urn:financial-services:scenario:strategic-portfolio/product-portfolio/insurance-products/insurance-product-penetration-insights
- Lens: Insights
- Complexity: S
- Intent: Bancassurance economics depend on penetration rates across the eligible customer base and the profitability of the distribution arrangement with insurance partners. The AI agent tracks penetration by product type, segment, and channel, surfacing concentration risks and underperforming distribution channels for the bancassurance product committee.
- Problem to solve: Insurance product penetration data is held across the bancassurance partnership system and the Bank's own CRM; a coherent penetration view requires manual extraction and reconciliation that is performed quarterly. Between reviews, sales momentum signals are invisible to product management.
- Solution: The AI agent integrates bancassurance sales data with the Bank's customer and channel records on a monthly basis, producing a penetration dashboard by product, segment, and channel. Distribution channels with penetration below target for two consecutive periods trigger a diagnostic note for the bancassurance product committee.
- OKR: Insurance product penetration is visible to the bancassurance product committee by channel and segment on a monthly basis, enabling distribution investment decisions without waiting for the quarterly review cycle.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces monthly penetration reports covering ≥90% of active insurance product lines from deployment. |
| Acceptance | ≥80% of monthly reports accepted by the bancassurance product committee as accurate and sufficient for distribution review. |
| Cycle | Insurance penetration visibility cycle compressed from quarterly assembly to a monthly read. |

### Insurance partner performance pack

- URN: urn:financial-services:scenario:strategic-portfolio/product-portfolio/insurance-products/insurance-partner-performance-pack
- Lens: Automation
- Complexity: M
- Intent: Bancassurance partnerships are governed by performance agreements that require regular partner reviews covering claims ratios, customer satisfaction, commission economics, and product compliance. The AI agent automates the assembly of the quarterly partner performance pack, drawing from claims data, customer feedback, and financial reconciliation records.
- Problem to solve: Partner performance packs are assembled manually by the bancassurance team from data held across three or four source systems; pack preparation takes one to two weeks and is often delayed, causing partner reviews to proceed without current data.
- Solution: The AI agent extracts and reconciles partner performance data from claims systems, CRM, and financial records, assembling a structured quarterly pack with KPI dashboard, trend commentary, and exception flags for each partner. The bancassurance team reviews and approves rather than constructing the pack.
- OKR: Quarterly partner performance packs are available to the bancassurance team within three business days of the data freeze, enabling timely partner reviews with current data.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces partner performance packs for 100% of quarterly reviews from deployment. |
| Acceptance | ≥80% of packs accepted by the bancassurance team without requiring material data re-extraction or reconciliation. |
| Cycle | Partner performance pack production time reduced from 1–2 weeks to ≤3 business days. |

### Insurance product regulatory compliance monitor

- URN: urn:financial-services:scenario:strategic-portfolio/product-portfolio/insurance-products/insurance-product-regulatory-compliance-monitor
- Lens: Enablement
- Complexity: M
- Intent: Bancassurance products are subject to conduct and disclosure requirements that change with supervisory guidance and insurance regulation. The AI agent monitors regulatory publications affecting bancassurance, maps changes to specific product and process obligations, and equips the compliance team with a structured impact assessment.
- Problem to solve: Insurance regulatory monitoring is distributed between the Bank's compliance team and its insurance partners; no single function owns a consolidated view of bancassurance regulatory obligations, and changes are sometimes identified late in the implementation cycle.
- Solution: The AI agent monitors insurance regulatory publications, classifies changes by product impact type, and produces a structured compliance impact assessment for the compliance team to review. Process and disclosure updates are mapped to the specific products and channels affected.
- OKR: Bancassurance regulatory changes are identified and mapped to specific products and channels within 48 hours of publication, giving the compliance team sufficient lead time for implementation.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent covers ≥95% of insurance regulatory publications relevant to bancassurance from deployment. |
| Acceptance | ≥80% of regulatory change assessments accepted by the compliance team as complete and accurately mapped without major additions. |
| Cycle | Insurance regulatory change identification-to-assessment time reduced from ≥5 business days to ≤48 hours. |

## Cards {#cards}

The cards portfolio covers debit, credit, and prepaid card products across consumer and commercial segments — tracked on outstandings, interchange and fee income, NIM on revolving balances, activation rates, spend penetration per cardholder, and delinquency. Cards portfolio decisions span product design (credit limit policy, reward structure, co-brand terms), pricing, and lifecycle management (activation campaigns, limit reviews, product retirement) against the economics of the Bank's issuing and acquiring positions.

### Cards portfolio economics insights

- URN: urn:financial-services:scenario:strategic-portfolio/product-portfolio/cards/cards-portfolio-economics-insights
- Lens: Insights
- Complexity: S
- Intent: Cards portfolio economics — interchange income, interest margin, reward cost, fraud loss, and credit loss — must be tracked at the product variant and segment level to identify where the portfolio creates and destroys value. The AI agent synthesizes card P&L components into a continuous product-level economics view for the product management committee.
- Problem to solve: Cards P&L is assembled monthly at an aggregate level; product-variant and segment-level economics are not produced routinely, making it difficult to identify which card products are value-accretive and which should be repriced or retired.
- Solution: The AI agent disaggregates cards P&L to the product variant and segment level on a monthly basis, producing a ranked economics view with trend signals. Product variants below the RAROC hurdle for two consecutive periods are flagged to the product management committee for repricing or lifecycle review.
- OKR: Cards product economics are visible at the variant and segment level on a monthly basis, enabling lifecycle decisions grounded in current P&L data.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces monthly cards economics reports covering ≥90% of active card product variants from deployment. |
| Acceptance | ≥80% of monthly reports accepted by the product management committee as accurate and sufficient for lifecycle decision-making. |
| Cycle | Cards product economics visibility moves from a monthly aggregate P&L to a monthly read at product-variant and segment level. |

### Cards competitor feature benchmark

- URN: urn:financial-services:scenario:strategic-portfolio/product-portfolio/cards/cards-competitor-feature-benchmark
- Lens: Enablement
- Complexity: S
- Intent: Cards product positioning requires a structured view of peer pricing, rewards programs, credit limits, and digital features across the main domestic and regional competitors. The AI agent synthesizes peer card product disclosures into a quarterly benchmark that equips the product team to identify competitive gaps and inform the product roadmap.
- Problem to solve: Cards competitor analysis relies on periodic manual research by product managers; coverage is incomplete, frequency is ad hoc, and the analysis is rarely current when product roadmap decisions are made.
- Solution: The AI agent aggregates peer card product disclosures — rates, fees, rewards, limits, digital features — on a quarterly basis and produces a structured competitive benchmark. Product managers receive a gap analysis showing where the Bank's card portfolio is at a competitive disadvantage.
- OKR: A structured competitive benchmark is available to the product team each quarter, ensuring roadmap decisions reflect current peer positioning.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces quarterly competitive benchmarks for ≥4 consecutive quarters within 15 months of deployment. |
| Acceptance | ≥75% of benchmarks accepted by the product team as accurate and sufficient for roadmap prioritization. |
| Cycle | Competitive benchmark production time reduced from ≥3 weeks of manual research to ≤5 business days. |

### Cross-Product Cannibalization Detection

- URN: urn:financial-services:scenario:strategic-portfolio/product-portfolio/cards/card-cannibalisation-detection
- Lens: Optimize
- Complexity: M
- Intent: Cannibalization patterns between card tiers and between card-credit and personal-loan products are detected from transaction and balance-migration signals before they appear in quarterly P&L. Product managers act on pricing or positioning adjustments within the current cycle.
- Problem to solve: When the Bank reprices a premium card tier or launches an adjacent personal-loan product, balance-migration signals accumulate in transaction data weeks before they appear in quarterly product P&L. The product team identifies shifts only at cycle-end, by which point repricing damage is embedded.
- Solution: The AI agent monitors transaction-level and balance-migration signals across the card and retail-credit book, surfacing cannibalization patterns with volume and margin estimates on a weekly cadence. Product managers review alerts and act before the pattern is confirmed in quarterly results.
- OKR: Cannibalization patterns between card tiers and between card-credit and personal-loan products are surfaced to product managers from transaction and balance-migration signals on a weekly cadence — before they appear in quarterly P&L — giving the product team a pricing and positioning adjustment window within the current cycle.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces cannibalization monitoring outputs for ≥95% of card and retail-credit product combinations on a weekly cadence; margin-impact estimates included in ≥90% of surfaced patterns. |
| Acceptance | ≥75% of AI-surfaced cannibalization alerts confirmed as material by product managers; volume and margin estimates within ±10% of subsequent quarterly P&L actuals in ≥80% of validated alerts. |
| Cycle | Cannibalization pattern identification lag reduced from quarter-end P&L review to ≤7 days from signal onset. |

## Treasury services {#treasury-services}

Treasury services covers the Bank's foreign exchange, money markets, fixed income, and derivatives products offered to corporate and institutional clients — including FX spot and forward, interest rate swaps, structured hedging, and liquidity management products. Revenue is tracked on trading income, net interest from Treasury's own-book position, and fee income from client hedging mandates. Product scope, client eligibility, and limit frameworks for treasury services are set by ALCO and the Risk Committee under applicable market conduct rules.

### Treasury services client economics insights

- URN: urn:financial-services:scenario:strategic-portfolio/product-portfolio/treasury-services/treasury-services-client-economics-insights
- Lens: Insights
- Complexity: S
- Intent: Treasury services revenue — FX, derivatives, cash management, trade finance — is typically concentrated in a small number of corporate and institutional clients. The AI agent synthesizes client-level revenue, product penetration, and wallet share data into a continuous economics view for the corporate and institutional banking head, surfacing revenue concentration risk and cross-sell opportunities.
- Problem to solve: Treasury services client economics are assembled quarterly from transaction banking and capital markets data; wallet share estimates are produced annually. Between reviews, revenue concentration and client profitability signals are not visible, limiting the relationship team's ability to act on shifting client dynamics.
- Solution: The AI agent integrates treasury services transaction data by client and product type on a monthly basis, producing a ranked client economics view with wallet share trend signals. Clients with declining revenue share or product concentration risk are flagged for relationship manager review.
- OKR: Treasury services client economics are visible on a monthly basis, enabling the relationship team to identify and respond to revenue concentration or wallet share loss before quarter-end.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces monthly client economics reports covering ≥80% of top-tier treasury services clients from deployment. |
| Acceptance | ≥80% of monthly reports accepted by the corporate and institutional banking team as accurate and actionable. |
| Cycle | Treasury services client economics visibility cycle compressed from quarterly assembly to a monthly read. |

### Treasury services product coverage enablement

- URN: urn:financial-services:scenario:strategic-portfolio/product-portfolio/treasury-services/treasury-services-product-coverage-enablement
- Lens: Enablement
- Complexity: M
- Intent: Corporate relationship managers (RMs) are expected to identify treasury services opportunities across their client portfolios — FX hedging, interest rate derivatives, supply chain finance — but often lack the product knowledge depth to recognize the triggers and structure conversations effectively. The AI agent provides RM-facing coverage guidance that maps client financial characteristics to applicable treasury product solutions.
- Problem to solve: Treasury product coverage is concentrated among a small number of experienced RMs; coverage quality is inconsistent across the corporate portfolio, and treasury services revenue is below wallet share potential in mid-tier corporate segments. Product training alone has not closed the coverage gap.
- Solution: The AI agent analyzes client financial data — revenue, balance sheet structure, FX exposure, payables cycle — and generates a treasury product coverage brief for the RM, identifying applicable product solutions, trigger conditions, and suggested conversation starters. Coverage briefs are produced on demand and refreshed quarterly.
- OKR: Treasury product coverage briefs are available for ≥80% of the corporate client portfolio, increasing coverage quality and wallet share capture in mid-tier corporate segments.

| Dimension | Key result |
| --- | --- |
| Adoption | AI-produced coverage briefs used in ≥60% of corporate client treasury conversations within 12 months of deployment. |
| Acceptance | ≥70% of coverage briefs rated as useful and accurate by RMs; mid-tier corporate treasury revenue per RM increases by ≥10% within 12 months. |
| Cycle | Coverage brief production time reduced from ≥2 days of product specialist preparation to ≤30 minutes on demand. |

### Treasury services cross-sell and bundling opportunities

- URN: urn:financial-services:scenario:strategic-portfolio/product-portfolio/treasury-services/treasury-product-mix-optimisation
- Lens: New opps
- Complexity: L
- Intent: Cross-sell and product-bundling opportunities across the treasury-services stack are identified by client segment, with fee-income impact modeled for relationship-level negotiation and pipeline prioritization.
- Problem to solve: Cross-sell opportunities across treasury-services lines — bundling FX with trade-finance facilities, expanding cash management into new geographies — depend on infrequent relationship-level reviews. Repricing and bundling windows that would increase fee income are missed between cycles.
- Solution: The AI agent monitors transaction and relationship signals across the corporate book and surfaces cross-sell and bundling opportunities by client and product line with fee-income impact estimated per scenario. Relationship managers receive a ranked opportunity list weekly; product heads use the aggregate view to refine pricing and packaging strategy.
- OKR: Cross-sell and product-bundling opportunities across the treasury-services stack — identified from transaction and relationship signals by client segment with fee-income impact estimated per scenario — are surfaced to relationship managers weekly and aggregated for product heads, enabling pipeline prioritization and repricing decisions within current commercial cycles.

| Dimension | Key result |
| --- | --- |
| Adoption | The AI agent produces weekly treasury cross-sell opportunity lists for ≥48 consecutive weeks per year; fee-income impact estimates included in ≥90% of surfaced opportunities per client and product line. |
| Acceptance | ≥75% of AI-surfaced cross-sell opportunities confirmed as actionable by relationship managers; fee-income estimates within ±15% of realized revenue in ≥80% of converted opportunities. |
| Cycle | Treasury cross-sell opportunity identification cycle reduced from infrequent relationship-level reviews to a weekly ranked opportunity list, with bundling and repricing windows identified ≥8 weeks earlier per cycle. |
