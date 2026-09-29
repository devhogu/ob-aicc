# Risk Management, Treasury, ALM and Markets: Generative and Agentic AI

Research date: 2026-09-29. Scope: (A) risk management (credit, market and liquidity, operational, enterprise risk and stress testing, model risk, third-party risk, regulatory capital and prudential reporting, early warning); (B) treasury, ALM and markets (liquidity forecasting, FX and cash management, deposit pricing and behavioural models, market commentary, dealing support, treasury operations). Figures are quoted from the source named and are not independently verified unless stated. Most pages were read only through search summaries; the Sources section marks which.

## Why it matters

- Risk and treasury run on the bank's most sensitive numbers and are the most model-heavy functions. Regulators accept AI here but hold the bank fully accountable. The ECB says "AI does not dilute responsibility" and expects second-line assessment before deployment and monitoring afterwards (ECB speech, Feb 2026).
- The regulatory position on generative AI (GenAI) and agentic AI is unsettled. The US revised model risk guidance (SR 26-2, Apr 2026) puts GenAI and agentic AI outside its scope and tells banks to govern them under their own risk practices (footnote text seen via secondary sources). The PRA applies its existing SS1/23 principles to AI without new rules. No Kyrgyz AI rule for banks was found. O!Bank must therefore write its own standard and be able to defend it to the National Bank of the Kyrgyz Republic (NBKR).
- The best-documented gains are in document-heavy work (credit memos, monitoring, reporting narratives), not in autonomous decisions. In the IACPM/McKinsey credit study, all participating institutions were testing at least one GenAI credit use case, but progress was slower than expected (via search summary).
- Concentration in a few AI and cloud providers is a named prudential concern (FSB, ECB, Bank of England). A digital bank in a small market that depends on foreign LLM providers carries this risk directly.

## Use cases

Maturity key: proven = live at scale at named or multiple institutions; emerging = pilots or early production, mostly consultancy, vendor or survey evidence; experimental = designs, demos, papers or unnamed reports.

### A. Risk management

| Use case | What AI does | Maturity | Example or source |
|---|---|---|---|
| Credit scoring and PD/LGD models (classical ML) | Gradient-boosted or similar models for scoring, early warning, pricing | proven | Deloitte internal benchmark: about three-quarters of banks use ML for credit scoring, early warning and pricing (via search summary). ECB says banks feel well prepared here because they build on existing validation (ECB speech). |
| Credit memo drafting and information synthesis | LLM reads filings, spreads and research, drafts memo sections with citations; analyst edits; a checker compares the draft with credit policy | emerging | IACPM/McKinsey (Jul 2025): synthesis and memo drafting are the most common GenAI credit use cases. Secondary sources cite 20-60% analyst productivity gains in case examples (not verified; not averages). An arXiv workflow evaluation (EnterpriseVal) describes cited drafting plus policy-guidance checking. |
| Portfolio monitoring and early warning | LLM reads news, filings and covenant text and flags borrowers or segments; natural-language queries over the portfolio | emerging | McKinsey survey: portfolio monitoring is the leading GenAI credit area, about 60% of surveyed institutions pursuing it (via search summary). Moody's and Newgen sell products (vendor). No named-bank result found. |
| Covenant and document extraction | Extracts terms and financials from loan documents, flags missing or conflicting values | emerging | Vendor guides only. No named-bank case with published results. |
| Operational risk: RCSA support | Mines past RCSAs, drafts scenario narratives from loss history, proposes ratings from observable data, acts as a challenger to first-line ratings | emerging | BCG (2026) describes the design and says it needs about 24 months; no figures given (BCG-reported). No named bank. |
| Operational risk: control library and loss-event analysis | Finds duplicate or weak controls, standardises control narratives, classifies incidents to a taxonomy (for example the ORX Reference Taxonomy), links events to controls | experimental | Cognizant blog and V7 Labs agent are vendor material. No named-bank GenAI case found; a MetricStream case at a bank was a platform rollout without GenAI. |
| Market and liquidity risk analytics | ML on market-stress indicators and funding data; LLM commentary on limit breaches and P&L or risk drivers | emerging | BIS Working Paper 1250 (2025): ML forecasting of market-stress indicators for US Treasury, FX and other markets (ML, not LLM; via search summary). No named-bank LLM case found. |
| Enterprise risk and stress testing | Drafts scenario narratives, translates them to model drivers, writes stress-test reports; agents run scenarios | experimental | Conceptual papers and vendor blogs only. None names a bank or regulator pilot. Bank of England plans to test AI-agent herding in its own stress work (via search summary). |
| Model risk management: model inventory, documentation and testing support | Drafts documentation, first-pass automated evaluation (groundedness, PII leakage) before independent validation | experimental | Databricks blog proposes it (vendor). No named bank found. |
| Model risk management: validating LLM systems | Validates prompt, retrieval setup, base model and agent steps as one system using an in-domain test set, hallucination rate and logged outputs | emerging (practice forming) | Seekr (vendor) and arXiv "Benchmarks Are Not Validation" (Jul 2026) argue for system-level validation, not generic benchmarks. PRA questions standard techniques such as cross-validation for complex models (via Jaywing summary of PRA slides). |
| Third-party risk | Reads vendor contracts and due-diligence packs, checks clauses against a requirements list, drafts register entries | emerging | PwC describes AI-assisted contract review. Third Party Risk Institute cites a financial-services case with 70% less due-diligence time (unnamed, unverified). Human review of critical-function classification is needed. |
| Regulatory capital and prudential reporting | Checks data lineage and consistency, flags anomalies, drafts narrative and reconciliation notes; rules-based engines do the calculation | experimental | ECB tested ML for plausibility checks on supervisory data (older paper). No source found for GenAI producing regulatory returns. Calculation must stay deterministic. |

### B. Treasury, ALM and markets

| Use case | What AI does | Maturity | Example or source |
|---|---|---|---|
| Liquidity and cash-flow forecasting | Time-series and ML models forecast inflows and outflows by product, segment or channel | proven (ML) | JPMorgan article (Nov 2024) describes neural, tree and ensemble methods and claims error cuts "by up to 50%" from unnamed corporate case studies (thought leadership, weakly evidenced). Coforge describes a bank ML forecasting project (vendor). Bank of America and U.S. Bank offer AI forecasting to clients (via search summary). |
| Variance narration and treasury Q&A | LLM explains forecast variance from bank data in plain language; treasurer queries positions in natural language | emerging | GTreasury and Ripple describe the pattern (vendors). Grounding in real treasury data is the stated control. |
| Deposit behaviour, decay and pricing | ML for non-maturity deposit decay, segment-level rate sensitivity (deposit beta), churn; frequent recalibration | emerging | KPMG: banks integrate ML "where governance permits" alongside survival analysis and regression. Mirai and SouthState describe approaches (vendor and bank-correspondent material). EBA guidelines cap the average duration assigned to non-maturity deposits (via search summary). |
| Interest rate risk (IRRBB) scenarios | ML or generative rate-scenario models, Monte Carlo term-structure models | emerging | Finalyse notes VAR is simplest and LSTM is an option (consultancy). Stays inside the model risk framework. |
| FX and cash management for clients | AI-assisted hedging rules, payment routing, exposure forecasting | emerging | Citi FX tools (awards coverage, not a technical case). BCG (2026) says AI agents will route payments and manage exposure within corporate policy. |
| Intraday liquidity management by agents | Agent decides funding moves during the day | experimental | A BIS working paper tested a GenAI agent on intraday liquidity in a payment system (seen only through a PYMNTS summary; not read). |
| Market commentary and research assistants | LLM summarises research, drafts client emails and morning notes from approved sources | emerging | Morgan Stanley AskResearchGPT (serves sales and trading staff since 2024), Goldman GS AI Assistant, JPMorgan LLM Suite (via search summaries of press coverage). No FX-specific tool with published results found. |
| Dealing support and trading copilots | Pre-trade analytics, client-flow summaries | experimental | Bank of America Maestro reported in a review paper (secondary). Bank of England warns about correlated behaviour if many firms use similar AI trading models. |
| Treasury operations | Payment repair, reconciliation, exception handling, confirmations | proven (automation) / emerging (GenAI) | BCG says BNY has wire repair in production at scale (via search summary; BCG-reported). |

## Target state for O!Bank

"Fully adopted" means risk and treasury run on one governed data layer. Deterministic engines produce every number. Models and agents assemble, explain, challenge and draft. Named owners approve every consequential decision.

**Risk management (A)**
- **Credit:** The credit file is assembled by AI from documents, registers and financials with citations. The analyst owns the memo. Scores and limits come from validated models. The LLM writes narrative and never sets a rating.
- **Early warning:** Structured signals (repayment behaviour, cash flows, covenant data) trigger alerts. An LLM adds a read of news and documents and explains why a name was flagged. Watchlist and classification changes are made by credit officers.
- **Operational risk:** Incidents and loss events are classified to one taxonomy with AI help. AI proposes RCSA ratings and control gaps from observed data. The first line owns ratings and the second line challenges them.
- **Stress testing and ERM:** Scenario design stays with the risk committee. AI helps draft narratives, map them to drivers and produce reports. Calculation runs in validated models.
- **Model risk:** One inventory covers statistical models, ML models and LLM applications. Each is tiered by materiality. LLM applications are validated as whole systems (prompt, retrieval, base model, tools) on in-domain test sets. Independent validators sign off on material uses.
- **Third-party:** Every AI provider is in the vendor register with concentration, exit and data-location review. AI reads contracts and drafts assessments. Humans classify critical services and approve.
- **Prudential reporting:** The calculation and submission chain is deterministic with lineage. AI checks consistency and drafts commentary. The CFO or Head of Risk attests.

**Treasury, ALM and markets (B)**
- **Forecasting:** ML forecasts liquidity, cash and deposit flows from bank data with back-testing. An LLM layer explains variances and answers questions, grounded on the same data. Treasury sets buffers and funding actions.
- **ALM:** Behavioural models (deposit decay, rate sensitivity, prepayment) are recalibrated often under model governance. ALCO approves assumptions. Deposit pricing recommendations go to the pricing committee with drivers shown.
- **FX and dealing:** AI drafts market commentary and desk notes from approved sources with citations. Limits, pricing authority and trade execution stay with dealers and hard-coded controls. Any autonomous action is capped by tight limits and monitored.
- **Operations:** Payment repair, reconciliation and exception handling are automated, with exceptions queued for staff.

**Where humans must stay in the loop (all areas)**
- Credit approval and rating overrides, watchlist and impairment or provisioning judgments.
- Approval of models, assumptions, scenarios and stress-test results.
- Limit setting, breach decisions and risk appetite.
- Funding, hedging and dealing decisions above a low autonomous limit, and any change to pricing authority.
- Regulatory returns, capital and liquidity attestations.
- Critical-function classification and exit decisions for third parties.
- Risk tiering of AI systems (do not classify an AI system as low tier to reduce governance; the PRA raised this concern, via Jaywing's summary of its slides).

## Phased adoption path

**Foundation**
- Set an AI use-case register and model inventory covering ML and LLM applications, with risk tiering and owners. Adopt a written AI model risk standard for GenAI (US guidance leaves the gap open, so write it and align with SS1/23 principles and the ECB expectations).
- Stand up a secured LLM environment: logging, no customer or position data to public models, retrieval index over policies, credit policy and regulations. Decide data residency and provider options (open item for the AICC).
- Build the data basics: consistent customer, account and counterparty keys, a treasury and ALM data mart, loss-event and incident history in one taxonomy.
- Low-risk pilots with human review: credit memo drafting on one segment, policy and regulation Q&A, incident classification in shadow mode, contract review for vendor assessments, treasury variance narratives, research summaries.
- Baseline metrics before any pilot.

**Scale**
- Move proven pilots to production for defined perimeters. Add ML liquidity and deposit forecasting alongside current methods (champion/challenger), with back-testing reported to ALCO.
- Portfolio monitoring with news and document signals for the business-lending book.
- RCSA support and control-library clean-up in two or three risk areas, as BCG suggests (start with a few non-financial risks, not a big-bang redesign).
- Formal LLM validation (system-level) and periodic performance reporting to the risk committee.

**Platform**
- Shared services: document extraction, citation checking, evaluation harness, audit logging, model registry, prompt and version control.
- One integrated view: credit, liquidity, market and operational signals, with reused data and lineage into prudential reporting.
- Continuous behavioural-model recalibration with automated monitoring and drift alerts.
- Third-party register with AI-assisted monitoring and concentration analysis.

**Agentic**
- Role-based agents (for example: credit file assembly, monitoring, incident triage, treasury reporting, limit-monitoring) work inside tightly scoped tools and read-only data by default. Write actions are limited to drafts, tickets and queues.
- Any agent that can move money, change limits or submit a return needs explicit approval, hard limits and a kill switch. Start in a bounded perimeter.
- Expand only against measured quality, override rates and regulator comfort. The FSB defines agentic AI as systems acting with limited human oversight, so autonomy is earned, not assumed. Agents from different banks using similar models can also produce correlated behaviour in markets (Bank of England, Apr 2025).

## Data and system prerequisites

- Core banking, loan and deposit data at account level with history, plus consistent customer and counterparty IDs.
- Financial statements, collateral and covenant data in structured form. Loan documents and credit files digitised and indexed.
- Treasury and ALM data: cash positions, payment flows, nostro and correspondent balances, deposit behaviour, market data feeds, curve and FX history. Data quality is the main limit on forecasting accuracy (Coforge and JPMorgan both stress data quality).
- Loss-event, incident, audit-finding and control data in one taxonomy.
- Regulatory reporting data with lineage (in line with BCBS 239 principles).
- Model inventory and registry with tiering, owners, validation status, monitoring results.
- Secured LLM environment: data residency decision, PII redaction or in-perimeter hosting, prompt and output logging, model versioning, evaluation harness, red-team capability. In-house Russian- and Kyrgyz-language evaluation sets are needed because vendor benchmarks are generic.
- Vendor register with contracts, sub-outsourcing chains, exit plans.
- Skills: quantitative modelling, model validation with LLM competence, treasury data engineering.
- Supervisory reporting interfaces to NBKR. NBKR approved a SupTech concept and roadmap for 2026-2031 that includes AI, machine learning and big data and standards for connecting banks' systems to NBKR (Akchabar, 17 Sep 2026; read directly). Watch for reporting and data-format consequences.

## Risks and controls

| Risk | Control |
|---|---|
| Hallucination or unsupported statements in memos, commentary and reports | Retrieval with mandatory source citation, a fact-checker on cited numbers, numbers taken from deterministic systems, hallucination rate measured in validation |
| Model risk for LLMs (non-deterministic output, no fixed specification, third-party base model) | Validate the whole system (prompt, retrieval, base model, tools) on in-domain test sets. Version everything. Log outputs. Do not rely on generic benchmarks alone. Re-validate on model or prompt change. |
| Regulatory gap for GenAI | SR 26-2 excludes GenAI and agentic AI, and the PRA applies SS1/23 without GenAI-specific rules. Adopt an internal standard mapped to SS1/23 and ECB expectations and engage NBKR early. Examiners are reported to ask about coverage anyway (commentary, not regulator text). |
| Under-tiering to avoid governance | Independent review of tier assignments by second line. Materiality drives the tier, not convenience (PRA concern, via Jaywing). |
| Accountability and explainability | Named business owner per use case. Reason codes for scores and alerts. Explanation must let risk managers and auditors challenge the output (ECB). |
| Drift and behavioural model breaks (deposits, forecasts) | Frequent recalibration with back-testing, stress and outlier checks, ALCO challenge. Static assumptions failed in 2023 according to practitioner sources. |
| Bias and fair lending | Bias testing on credit models. Under the EU AI Act, creditworthiness assessment of natural persons is high-risk, with obligations delayed to Dec 2027 (Regulation (EU) 2026/1744, via secondary sources). Not binding in Kyrgyzstan but a useful benchmark. |
| Third-party and concentration risk | Register, due diligence, audit and exit rights, multi-provider options, tested fallback. FSB and ECB flag concentration and lock-in. A GenAI vendor that reads contracts is itself a third party. |
| Market herding and correlated behaviour | Position and order limits on any automated dealing, independent monitoring, scenario testing of AI-driven flows (Bank of England FPC). |
| Data leakage and confidentiality | No confidential data or positions to public models, in-perimeter hosting or approved contracts, role-based retrieval. |
| Prompt injection and agent misuse | Least-privilege tool access, read-only defaults, human approval for write actions, red-team tests, full action logs. |
| Reliance on vendor claims | Test every claim on O!Bank data in a pilot before contracting. Most accuracy and time-saving figures found are self-reported. |
| Over-reliance and skill loss | Sampling of AI-assisted work, override-rate tracking, periodic non-AI exercises for analysts and validators. |

## Metrics

Measure against a pre-pilot baseline. No targets are set here because no reliable local benchmark was found.

- Credit: time to draft and approve a memo, analyst edit rate, citation accuracy, factual errors found in QA, early-warning lead time and hit rate, watchlist false positives.
- Operational risk: incident classification accuracy vs human sample, share of controls linked to events, RCSA cycle time, rating overrides by challengers.
- Model risk: percentage of AI systems in the inventory and validated, validation backlog and cycle time, incidents and drift alerts, hallucination rate on the test set.
- Third-party: vendor reviews completed on time, concentration indicators, contract-clause coverage.
- Reporting: data-quality exceptions before submission, resubmissions, time to close.
- Liquidity and treasury: forecast error (by horizon and product) vs current method, buffer held vs need, intraday shortfalls, time spent on reporting.
- ALM and pricing: deposit-runoff back-test error, NII and EVE sensitivity back-tests, pricing decision cycle time, deposit attrition.
- Markets and operations: straight-through-processing rate, payment repair time, limit breaches, commentary review edit rate.
- Governance: percentage of use cases tiered and with named owner, regulator or audit findings, reviewer override rate.

## Sources

Regulators and standard setters
- [Federal Reserve, SR 26-2 Revised Guidance on Model Risk Management (17 Apr 2026)](https://www.federalreserve.gov/supervisionreg/srletters/SR2602.htm) (cover letter read; attached guidance and GenAI footnote seen only through secondary summaries)
- [Domino, What changes with SR 26-2](https://domino.ai/blog/what-changes-with-sr-26-2) (vendor; secondary source for scope changes and GenAI exclusion)
- [PRA, SS1/23 Model risk management principles for banks](https://www.bankofengland.co.uk/prudential-regulation/publication/2023/may/model-risk-management-principles-for-banks-ss) (seen via search summary)
- [PRA, Model risk management AI and ML roundtable (Nov 2025)](https://www.bankofengland.co.uk/prudential-regulation/publication/2025/november/pra-holds-model-risk-management-roundtable-on-ai) (announcement page read; slides PDF could not be read, so the themes come from Jaywing's summary)
- [Jaywing, The PRA's AI roundtable: a governance reality check](https://risk.jaywing.com/news-views/the-pra-s-ai-roundtable-a-governance-reality-check-for-uk-banks/) (secondary; seen via search summary)
- [ECB Banking Supervision, Technology is neutral, governance is not (Feb 2026)](https://www.bankingsupervision.europa.eu/press/speeches/date/2026/html/ssm.sp260224~6c5b64a77a.en.html) (read)
- [ECB, Supervisory priorities 2026-28](https://www.bankingsupervision.europa.eu/framework/priorities/html/ssm.supervisory_priorities202511.en.html) (search summary)
- [FSB, Financial Stability Implications of AI (Nov 2024)](https://www.fsb.org/2024/11/the-financial-stability-implications-of-artificial-intelligence/) (search summary)
- [FSB, Monitoring Adoption of AI and Related Vulnerabilities (Oct 2025)](https://www.fsb.org/2025/10/monitoring-adoption-of-artificial-intelligence-and-related-vulnerabilities-in-the-financial-sector/) (search summary)
- [Basel Committee press release, 20 May 2026 (AI and cyber; liquidity principles review)](https://www.bis.org/press/p260520.htm) (search summary)
- [BIS FSI, How regulators can address AI explainability](https://www.bis.org/fsi/fsipapers24.pdf) (search summary)
- [BIS Working Paper 1250, Predicting financial market stress with machine learning](https://www.bis.org/publ/work1250.pdf) (search summary)
- [Bank of England, Financial Stability in Focus: AI in the financial system (Apr 2025)](https://www.bankofengland.co.uk/-/media/boe/files/financial-stability-in-focus/2025/financial-stability-in-focus-artificial-intelligence-in-the-financial-system.pdf) (search summary)
- [EBA, Guidelines on management of third-party risk (non-ICT)](https://www.eba.europa.eu/publications-and-media/press-releases/eba-publishes-its-final-guidelines-management-third-party-risk-delivering-more-proportionate-and) (search summary)
- [Regulation (EU) 2026/1744, Digital Omnibus on AI, summary](https://www.bankingnewsai.com/ai-regulation/documents/eu-digital-omnibus-ai-regulation-2026-1744) (secondary; check EUR-Lex)

Consultancies, banks, vendors
- [IACPM/McKinsey, Banking on gen AI in the credit business (Jul 2025)](https://members.iacpm.org/common/Uploaded%20files/Samples/Downloadable%20content/Research%202025/IACPM%20McKinsey%202025%20-%20Banking-on-Gen-AI-in-the-Credit-Business-the-route-to-value-creation.pdf) (PDF unreadable through fetch; findings from search summaries)
- [McKinsey, Embracing generative AI in credit risk](https://www.mckinsey.com/capabilities/risk-and-resilience/our-insights/embracing-generative-ai-in-credit-risk) (search summary)
- [BCG, AI-Powered Risk Self-Assessments for Banks (2026)](https://www.bcg.com/publications/2026/ai-risk-self-assessments-banking) (read; BCG-reported, no quantified results)
- [BCG, How AI Agents Are Reshaping Corporate Treasury (2026)](https://www.bcg.com/publications/2026/ai-agents-reshaping-corporate-treasury) (search summary)
- [ORX, Large Language Models and operational risk (Sep 2023)](https://orx.org/blog/large-language-models-and-operational-risk) (read)
- [Deloitte, CTRL + Operational Risk: ORX perspectives on AI in banking](https://www.deloitte.com/dk/en/Industries/banking-capital-markets/perspectives/ai-and-operational-risk-banking.html) (search summary)
- [JPMorgan, AI-driven cash flow forecasting (Nov 2024)](https://www.jpmorgan.com/insights/treasury/forecasting-planning/ai-driven-cash-flow-forecasting-the-future-of-treasury) (read; thought leadership, commercial purpose)
- [BNY, AI decision intelligence in treasury management](https://www.bny.com/corporate/global/en/insights/ai-decision-intelligence-treasury-management.html) (search summary)
- [Coforge, AI-driven liquidity planning case study](https://www.coforge.com/success-stories/enhancing-liquidity-planning-with-ai-driven-payment-settlement-forecasting) (vendor; search summary)
- [KPMG, Margin stabilisation (deposit modelling)](https://assets.kpmg.com/content/dam/kpmg/ie/pdf/2025/08/ie-margin-stabilisation.pdf) (search summary)
- [Finalyse, Non-maturity deposit modelling](https://www.finalyse.com/blog/non-maturity-deposit-modelling) (search summary)
- [Seekr, Model risk management for generative AI](https://www.seekr.com/resource/model-risk-management-generative-ai-sr-11-7/) (vendor; search summary)
- [arXiv, Benchmarks Are Not Validation (Jul 2026)](https://arxiv.org/pdf/2607.28840) (search summary)
- [arXiv, Model Risk Management for Generative AI in Financial Institutions](https://arxiv.org/pdf/2503.15668) (search summary)
- [arXiv, EnterpriseVal](https://arxiv.org/pdf/2609.21841) (search summary)
- [PwC, Third-party risk management](https://www.pwc.com/gx/en/services/managed-services/third-party-risk-management.html) and [Third Party Risk Institute, Modernizing TPRM with AI](https://thirdpartyriskinstitute.com/modernizing-third-party-risk-management-with-ai/) (search summaries)
- [PYMNTS, AI agents help treasurers move faster (2026)](https://www.pymnts.com/news/artificial-intelligence/2026/ai-agents-help-treasurers-move-faster/) (search summary; secondary route to the BIS intraday liquidity paper)
- [Goldman Sachs AI assistant rollout, NBC News](https://www.nbcnews.com/business/business-news/goldman-sachs-launches-ai-assistant-employees-artificial-intelligence-rcna188643) (search summary)
- [Cognizant, GenAI in RCSA](https://www.cognizant.com/us/en/insights/insights-blog/gen-ai-in-banking-rcsa) and [V7 Labs, operational risk agent](https://www.v7labs.com/agents/ai-agent-for-operational-risk-managers) (vendor)

Kyrgyz context
- [Akchabar, NBKR to implement AI and big data for banking supervision (17 Sep 2026)](https://www.akchabar.kg/en/news/natsbank-vnedrit-tekhnologii-ii-i-bolshikh-dannikh-dlya-nadzora-za-bankami-rqyiydsudaburyyn) (read)
- [24.kg, National Bank: AI and digital payments require strengthened cybersecurity](https://24.kg/english/382480_National_Bank_AI_and_digital_payments_require_strengthened_cybersecurity/) (search summary)

## Confidence and gaps

- **Strongest evidence:** the regulatory position (ECB speech, read directly; Fed SR 26-2 scope, confirmed through several secondary sources but the footnote itself not read in the primary PDF; PRA SS1/23 as principles applied to AI). Also the NBKR SupTech roadmap (read directly).
- **Seen only through search summaries:** PRA roundtable slides (the PDF could not be read; the themes on tiering and validation come from Jaywing), FSB reports, Basel items, BIS papers, IACPM/McKinsey findings (the PDF returned no text), most bank and vendor items.
- **Self-reported or vendor figures:** all productivity ranges (20-60% memo drafting via secondary summary of IACPM/McKinsey; 70% due diligence; JPMorgan "up to 50%" error reduction from unnamed cases); Deloitte three-quarters ML use; McKinsey 60% portfolio monitoring share; all BCG statements. None independently verified. Numbers whose source could not be traced were omitted.
- **Thin or absent evidence:** named-bank GenAI cases for RCSA and control libraries, loss-event classification, stress testing, regulatory return production, market and liquidity risk, model validation with LLMs, and FX-specific market commentary. Treat these as emerging or experimental. The BIS intraday liquidity agent paper was not read.
- **Not found for Kyrgyzstan:** any NBKR expectation on GenAI or model risk in banks, local treasury or ALM AI cases, and local deposit-behaviour or FX-market specifics. Kyrgyz-language and Russian-language LLM performance on risk and treasury text was not researched.
- **Not covered:** vendor selection, cost and ROI, market-risk capital rules (FRTB) and IFRS 9 expected-credit-loss models, and Basel liquidity principle updates (the Committee said in May 2026 it will consider targeted updates; content unknown).
- **Legal points to verify at source:** SR 26-2 guidance text and GenAI footnote (OCC Bulletin 2026-13), Regulation (EU) 2026/1744 on EUR-Lex, SS1/23 text.
