# Investor Relations and FP&A: generative and agentic AI in banks

Research note for the AICC. Covers (A) Investor Relations (IR) and (B) FP&A, management and financial reporting. Research date: 2026-09-29. Explanatory only; authority lives in `.grace/`.

Scope note: it is not confirmed in this repo whether O!Bank has listed equity or public debt. Where this note says "investors", read shareholders, the parent group, bond holders, lenders, DFIs and rating agencies as well as analysts. The IR governance points apply to any external audience for financial numbers.

## Why it matters

- Both functions are text- and number-heavy, run on fixed calendars, and are staffed by very small teams. In a Q4/NIRI survey of IR professionals, 90% of respondents were on teams of 3 or fewer, 42% worked solo, and 66% spent 40+ hours on earnings prep per quarter (vendor-run survey, sample size not disclosed). AI targets exactly this load.
- Adoption in finance is broad but shallow. Gartner's 2025 survey of 183 finance leaders found 59% of finance functions use AI (58% in 2024), and 91% of them reported only low or moderate impact at first. Deloitte's Q4 2025 CFO Signals reports 63% "fully deployed" AI solutions but only 21% seeing tangible value, and 14% with AI agents fully integrated. Value comes from getting past pilots.
- External audiences are also using AI on the bank's disclosures (transcript summarizers, AI search over IR sites). Consistent, machine-readable, correct disclosure now matters for how the bank is read, not only how it is written.
- Errors here are public and hard to reverse: a wrong number in results materials, or an unintended disclosure, is a regulatory and reputational event. This function needs stricter controls than most GenAI use cases.

## Use cases

Maturity key: proven = repeated production use reported by named organisations or independent surveys; emerging = vendor products and early named deployments, limited independent evidence; experimental = prototypes, research papers, forward-looking claims.

### A. Investor Relations

| Use case | What AI does | Maturity | Example bank or source |
|---|---|---|---|
| Peer transcript and filing summarisation | Summarises peer earnings calls, decks and disclosures; extracts themes, KPIs and guidance language | proven (as general tooling) | AlphaSense Smart Summaries, Q4 call summaries (vendors); IR Impact and Euronext list it as the low-risk starting point |
| Analyst Q&A anticipation and mock questions | Generates likely analyst questions from recent results, peer narratives and past question history; drafts answer outlines; runs mock Q&A for executives | emerging | AlphaSense "Anticipatory Q&A" agent; Q4 AI Earnings Co-Pilot (both vendor claims). No bank case study found |
| Analyst question theme tracking | Tracks how analyst/investor concerns shift across calls over time | emerging | AlphaSense "Thematic Analysis of Analyst Q&A"; IR Impact (2026) |
| Sentiment and perception analysis | Reads analyst notes, meeting notes, Q&A and surveys for directional sentiment and top concerns | emerging | Euronext Corporate Solutions (2026), Nasdaq IR Insight (vendor) |
| Shareholder and investor targeting | Mines CRM history and ownership data to profile holders, flag concentration, score prospects | emerging | Q4 AI-native CRM (Apr 2026, vendor); IR Impact describes behavioural targeting as pilot-stage |
| Peer benchmarking on disclosures | Compares guidance language, KPI definitions and phrasing across peers' materials | emerging | Euronext (2026); AlphaSense (vendor) |
| Drafting results materials | First drafts of prepared remarks, scripts, press release text, shareholder letter, FAQ; repurposing one transcript into multiple assets | emerging | McKinsey (CFO guide, 2023) notes multinationals using AI for first drafts of securities filings and stakeholder reports; Q4 Earnings Co-Pilot (vendor) |
| Disclosure consistency and pre-checks | Compares wording and numbers across press release, deck, annual report and translations; flags vague or over-optimistic language before legal review | emerging | Euronext (2026): described as a pre-check only |
| Management briefing packs | Turns investor profiles and transcripts into briefing notes and one-pagers for the CEO/CFO | emerging | Euronext; Nasdaq IR Assistant (vendor) |
| Multilingual transcripts and IR site search | Real-time transcripts and translation of webcasts; better IR website search | emerging | Euronext EngageStream (vendor) |
| ESG and regulatory disclosure drafting | Drafts narratives and maps disclosures to framework requirements (ESRS/ISSB) with an audit trail | emerging | Workiva agents (vendor, 2026); BCG white paper on AI-enabled ESG reporting. Assurance concerns are open (see Risks) |
| Answer-engine visibility of IR content | Structures IR pages so external AI assistants cite them correctly | experimental | Q4 "AEO for IR Web" (Mar 2026, vendor) |
| Agentic IR workflows | Agents research a target fund, draft outreach, check calendars, log to CRM | experimental | IR Impact (Mar 2026): recommends human-in-the-loop, full autonomy "late 2020s" |
| Public investor-facing chatbot | Answers investor questions from published material | experimental | BNY paper lists interactive IR chatbots as a possible use case; no production example found. Highest disclosure risk |

### B. FP&A, management and financial reporting

| Use case | What AI does | Maturity | Example bank or source |
|---|---|---|---|
| Knowledge management over finance policy, accounting manuals, regulations | Retrieval-based Q&A over internal documents | proven | Gartner 2025: top finance AI use case (49% of respondents); Citi Assist searches internal policies (press) |
| Anomaly and error detection in ledgers and reports | ML flags unusual entries, breaks, and reconciling items | proven | Gartner 2025: 34% of respondents; BlackLine and OneStream offer it (vendors) |
| Reconciliation and trade/transaction accounting | Agents match, explain and route breaks | emerging | Goldman Sachs with Anthropic: Claude-based agents for trade and transaction accounting, in early stages as of Feb 2026 (CIO statement via CNBC/Finextra; launch status not confirmed) |
| Variance and driver analysis | Walks the driver tree, isolates root causes, ranks drivers of movement in NII, fees, opex, cost of risk | emerging | McKinsey CFO guide: multinationals using AI to find drivers of budget variances. BCG (2026) describes an FP&A agent at an unnamed large tech company answering variance queries in under 30 seconds vs 2-3 days (single client case, not a bank) |
| Commentary and narrative generation | Drafts management commentary for monthly/quarterly packs from the numbers, for analyst edit | emerging | McKinsey; KPMG (US public sector paper); vendor content. No named bank case found |
| Natural-language access to finance data | Users ask questions of the ledger or planning data in plain language; answers with source lines | emerging | HPE with Deloitte/NVIDIA "CFO Insights": natural-language queries over about 300M line items; HPE reports about 40% faster reporting cycle and 25%+ lower processing cost (company and Deloitte-reported; not a bank; earlier statement was about 50%). Text-to-SQL research shows errors such as mixing YoY and QoQ (arXiv, FINCH/FinStat2SQL) |
| Reporting pack and board deck production | Assembles decks and drill-down from governed data; replaces static slide packs | emerging | HPE (as above). BCG (2026) projects fully automated standard reporting as a target state, not as an achieved one |
| Forecasting, budgeting and rolling forecasts | Classical ML for time series and driver forecasts; LLMs used to build and explain models | emerging | Deloitte CFO Signals Q2 2026: 44% of surveyed North American CFOs use AI for planning and budgeting (cross-industry). MIT Tech Review Insights (Deloitte-sponsored) notes LLM mathematical limits for forecasting |
| Scenario and stress planning | Generates and compares scenarios across rates, FX, credit and liquidity; explains P&L and capital impact | experimental | BCG (2026) forward-looking; arXiv 2026 prototype of BVAR-based multi-scenario rate forecasting with sentiment module |
| ALM, NIM and deposit pricing | ML on contract-level data for deposit behaviour, prepayment and rate sensitivity; pricing optimisation vs competitors | emerging | Coforge case for an unnamed UK bank (vendor, no quantified result); Mirai (vendor). Classical ML is more mature here than GenAI |
| Cost-of-risk and cost-to-income (CIR) analytics | Explains movements by segment, cohort, product; links to opex drivers | experimental for GenAI; ML proven | No named bank case found for the GenAI layer |
| Peer benchmarking from public filings | Extracts KPIs and definitions from peer reports and IR decks into a comparable dataset | emerging | Multi-agent KPI/guidance extraction research (arXiv 2505.19197); AlphaSense (vendor) |
| Operational KPI monitoring | Continuous KPI vs expectation monitoring across channels and products | emerging | BCG 2026 unnamed tech company case (gross adds, churn vs expected) |
| Regulatory transformation across finance, risk, controls | AI used to speed data and control work in regulatory programmes | emerging | Citi CFO (Apr 2026): AI being used to automate parts of its multi-year regulatory transformation; no metrics given |
| Close acceleration and continuous close | Agents draft journals, reconcile continuously, flag exceptions | experimental | BCG "AI-First Finance Function" (Jun 2026): targets such as real-time close within three years, forward-looking, vendor-consultant perspective |
| Cash application, invoice, expense automation | Touchless matching and processing | proven | BCG/SAP (May 2026) cites vendor-reported touchless rates above 90% for cash application. Not bank-specific |

## Target state for O!Bank

"Fully adopted" means the following, all under human sign-off for anything external or ledger-affecting.

### IR
- One governed, bank-hosted AI workspace for IR and Finance with enterprise data terms (no training on bank data, retention controls, audit log). No public consumer tools for anything non-public.
- A curated corpus: own filings and reports, peer filings and transcripts, analyst and lender questions, rating-agency and DFI correspondence, an approved KPI glossary. Every AI answer cites document and page.
- Calendar-driven prep: after each reporting cycle the IR team gets an auto-drafted peer comparison, a question forecast with draft answers linked to source numbers, and a consistency report across all materials.
- Results materials drafted from the same governed numbers as the finance reporting layer, so figures are pulled, not retyped. Every public number is tied to a locked source.
- Investor and lender interaction log analysed for themes and sentiment; a small stakeholder map with concentration flags.
- Disclosure committee sign-off, MNPI controls and pre-release checks built into the workflow. Public-facing AI (chatbot) only over already-published content, if at all.

### FP&A
- One governed finance data layer (unified chart of accounts, definitions for NII, NIM, CIR, cost of risk, and cross-system hierarchies) that both people and AI read.
- Monthly and quarterly packs are generated from that layer. AI writes first-draft commentary and driver explanations; analysts review and approve, with numbers pulled by query, not written by the model.
- Natural-language access for finance and business managers to the same layer, with permissions, lineage and displayed query/source.
- Rolling forecasts and scenarios using ML for numerics, LLMs for explanation and scenario setup, and full model documentation. ALM, deposit pricing and cost-of-risk analytics are integrated with the planning view.
- Continuous reconciliation and anomaly detection shorten the close; exceptions go to owners.
- Peer benchmarking dataset refreshed from public filings each quarter, shared with IR.
- Agents handle routine monitoring and drafting; humans own judgement, exceptions and approvals.

## Phased adoption path

### Phase 1: Foundation
- Approve a finance and IR AI usage policy: allowed tools, data classes, MNPI rule, human review, logging.
- Deploy an enterprise-grade assistant with data protections; ban public tools for non-public content.
- Low-risk internal use only: summarise peer transcripts and filings, mock Q&A, draft internal briefing notes, RAG over accounting policies and manuals.
- Start a finance data audit: definitions, sources, ownership. Fix the KPI glossary before adding AI on top.
- Baseline metrics (prep hours, close days, pack production hours, error rate).

### Phase 2: Scale
- First-draft commentary for monthly management pack, edited by analysts; track edit rates.
- Disclosure consistency checker across press release, deck, annual report and translations (pre-legal check).
- Peer benchmarking dataset built from public filings with human validation of extracted KPIs.
- Natural-language query over one governed dataset (for example the management P&L), with a curated semantic layer and answer verification.
- Anomaly and error detection on ledger and packs.
- ML forecasting pilots for a few lines (NII, fees, opex), compared against current forecasts before adoption.

### Phase 3: Platform
- Governed finance data platform and semantic layer used by reporting, planning, IR and AI. Lineage from every reported figure to source.
- Shared prompt/agent library, evaluation set and monitoring for finance and IR; model inventory and validation.
- Integrated planning: driver-based rolling forecast, scenarios, ALM and cost-of-risk views on the same data.
- IR CRM/analytics with sentiment and stakeholder insights, integrated with disclosure workflow.
- ESG and regulatory disclosure drafting with traceable evidence, aligned to assurance provider expectations.

### Phase 4: Agentic
- Agents for continuous reconciliation, variance triage, forecast refresh, pack assembly and KPI watchdogs; each with defined permissions, thresholds and escalation.
- IR agents for prep cycles (research, draft, consistency check), stopping at human approval; no autonomous external communication.
- Agent actions logged, separation of duties preserved (an agent that prepares does not approve).
- Progress gate: each step up only after measured accuracy and control evidence. BCG's own stated position is "AI proposes, human disposes" in early stages.

## Data and system prerequisites

- Finance data: general ledger, sub-ledgers, management accounting/P&L, planning data, FTP and ALM data, credit-risk provisioning data, all with reconciled definitions. BCG/SAP (2026) names fragmented data and inconsistent definitions (for example "margin" defined differently by region) as the main cause of plausible but wrong answers.
- Semantic layer: unified chart of accounts, master data, hierarchies, driver relationships, and links from financial to operational data.
- Data lineage and access control by role, including information barriers for pre-release results data.
- IR data: CRM, shareholder/lender register, meeting notes, ownership data, web analytics, published-disclosure archive. IR Impact (2026) notes such tools often sit apart; it cites (without clear attribution) 73% of IR teams reporting integration challenges.
- Corpus of peer filings and transcripts with licensing checked (many transcript and research sources restrict AI use).
- Local language: Kyrgyz, Russian and English materials; test model quality on Kyrgyz and Russian financial text before relying on it. No source in this research measured this; treat it as a gap.
- Enterprise LLM access with data-use protections, private or in-region hosting where required, logging, prompt and output retention, evaluation harness.
- Planning/consolidation and close tools with their own AI features (evaluate vendor roadmaps), or a bank-owned layer on top.
- Model inventory and validation process that covers GenAI in finance.

## Risks and controls

| Risk | Control |
|---|---|
| Selective disclosure or unintended disclosure of material non-public information (MNPI) through prompts, uploaded drafts, or an AI tool answering investors | Enterprise-only tools; no MNPI in external or consumer tools; access control and information barriers on pre-release data; no autonomous external communication; public chatbots limited to published content; log prompts. Regulator sources (FINRA, SEC-adjacent) say the same rules apply whether a human or a tool produced the communication. These apply to registrants; for an issuer, apply by analogy and confirm with legal counsel |
| Hallucinated or wrong numbers in public materials | Numbers pulled from the governed source by query, never generated; automated tie-out of every figure in drafts to source; second-person review; locked source versions; test set of known-answer checks |
| Wrong answers from natural-language data access (semantically valid but wrong queries, e.g. YoY vs QoQ) | Curated semantic layer; show query and source lines to the user; deterministic mode where possible (HPE reports engineering for deterministic outputs); regression tests on standard questions |
| Confident but unsourced variance narrative (the model invents a cause) | Require the model to walk the driver tree first and mark hypotheses as conjecture (approach BCG/SAP describes); analyst must confirm causes with business owners |
| LLM weakness at numerical forecasting | Use conventional statistical/ML models for numbers; LLM for scenario setup and explanation; backtest against existing forecasts; model documentation |
| Disclosure inconsistency between channels or languages | Automated consistency check as a pre-check, not a replacement for disclosure committee or legal review |
| ESG or regulatory disclosure that cannot be evidenced, and auditor over-trust of AI output | Evidence trail from each statement to source; keep human ownership; agree approach with assurance provider early |
| Over-claiming AI capability in own disclosures ("AI washing") | Legal review of any AI statement in IR materials; SEC and commentators flag AI-washing as an enforcement theme (US context) |
| Audit, segregation of duties and accountability for agents | Agents have roles and thresholds; preparer/approver separation; inspectable outputs; retain records |
| Vendor and third-party concentration, data leakage | Third-party risk review; contract terms on training and retention; exit plan. FSB (Nov 2024, Oct 2025) identifies third-party dependency and concentration, model risk and data quality as key AI vulnerabilities |
| Records and discovery: AI prompts and outputs may be records | Retention policy for prompts/outputs in IR and finance workflows; legal check (ABA article, 2026, discusses this in a US context) |
| Regulatory posture in Kyrgyzstan unclear | No dedicated NBKR AI rule for banks was found in this research. Check current NBKR requirements and data-localisation rules before deployment. Kazakhstan's regulator follows a technology-neutral approach (existing risk, data protection and cybersecurity rules apply to algorithms) |
| Skills and change: "70% of AI success is people and process" (BCG, self-reported from client work) | Training, role redesign, named process owners |

## Metrics

Baseline first; target values to be set by the AICC with Finance and IR. No target figures are asserted here because none are sourced for a bank of O!Bank's size.

**IR**
- Analyst and executive prep hours per reporting cycle
- Share of analyst questions on the call that were on the forecast list
- Errors caught by the consistency check before release, and errors found after release (target: zero after release)
- Time to produce peer comparison after peers report
- Share of public figures with automated source tie-out
- Response time to investor and lender information requests
- MNPI incidents and policy exceptions

**FP&A**
- Working days to close and to issue the management pack
- Analyst hours per pack and per commentary
- Edit rate on AI-drafted commentary (share of text changed)
- Forecast accuracy (NII, fees, opex, provisions) vs baseline, and forecast cycle time
- Number of reconciling items and anomalies detected and time to resolve
- Accuracy of natural-language queries on a fixed test set; adoption by managers
- Share of standard reports generated without manual data assembly
- Value tracked to P&L, not to pilot counts (Gartner and Deloitte both show that few reach measured value)

## Sources

Consulting, analysts, regulators, surveys
- [Gartner, Finance AI adoption remains steady in 2025 (press release, Nov 2025)](https://www.gartner.com/en/newsroom/press-releases/2025-11-18-gartner-survey-shows-finance-ai-adoption-remains-steady-in-2025) (access blocked when fetched; figures read via [CFO Dive](https://www.cfodive.com/news/cfos-ai-adoption-slows-challenges-mount-gartner/805949/))
- [Deloitte, Q2 2026 CFO Signals](https://www.deloitte.com/us/en/insights/topics/business-strategy-growth/2q-2026-cfo-signals-survey.html) and [Q4 2025 CFO Signals](https://www.deloitte.com/us/en/about/press-room/deloitte-q4-2025-cfo-signals-survey.html) (figures read via search summaries)
- [Deloitte, Harnessing gen AI in financial services: why pioneers lead the way (Feb 2025)](https://www.deloitte.com/us/en/insights/industry/financial-services/generative-ai-financial-services-pioneers.html)
- [BCG, The AI-First Finance Function (Jun 2026)](https://www.bcg.com/publications/2026/the-artificial-intelligence-first-finance-function)
- [BCG and SAP, The CFO's AI Agenda: From Automation to Advantage (May 2026)](https://www.bcg.com/publications/2026/the-cfos-ai-agenda-from-automation-to-advantage)
- [BCG, Applying Agentic AI in the Finance function (PDF)](https://www.bcg.com/assets/2026/executive-perspectives-applying-agentic-ai-in-the-finance-function-for-transformative-impact.pdf) (PDF could not be parsed here; the 30-second variance figure was read via search summary)
- [McKinsey, Gen AI: A guide for CFOs (2023)](https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights/gen-ai-a-guide-for-cfos)
- [McKinsey, AI in finance: driving automation and business value](https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights/how-finance-teams-are-putting-ai-to-work-today) (not read directly; fetch timed out)
- [McKinsey, Capturing the full value of generative AI in banking](https://www.mckinsey.com/industries/financial-services/our-insights/capturing-the-full-value-of-generative-ai-in-banking)
- [MIT Technology Review Insights with Deloitte, Partnering with generative AI in the finance function (Sep 2025)](https://www.technologyreview.com/2025/09/11/1123508/partnering-with-generative-ai-in-the-finance-function/) (sponsored content)
- [FSB, The Financial Stability Implications of AI (Nov 2024)](https://www.fsb.org/2024/11/the-financial-stability-implications-of-artificial-intelligence/)
- [FSB, Monitoring Adoption of AI and Related Vulnerabilities in the Financial Sector (Oct 2025)](https://www.fsb.org/2025/10/monitoring-adoption-of-artificial-intelligence-and-related-vulnerabilities-in-the-financial-sector/)
- [FINRA, Artificial Intelligence key topics](https://www.finra.org/rules-guidance/key-topics/artificial-intelligence)
- [Times of Central Asia, Kazakhstan adopts pragmatic AI regulation in financial sector (Mar 2026)](https://timesca.com/kazakhstan-adopts-pragmatic-ai-regulation-in-financial-sector/)

Bank and company examples
- [CNBC, Goldman Sachs taps Anthropic's Claude to automate accounting and compliance (Feb 2026)](https://www.cnbc.com/2026/02/06/anthropic-goldman-sachs-ai-model-accounting.html) (blocked when fetched; content read via search summaries including [Finextra](https://www.finextra.com/newsarticle/47306/goldman-sachs-enlists-anthropic-for-accounting-and-compliance-ai-agents))
- [Fortune, Citi's new CFO touts AI gains (Apr 2026)](https://fortune.com/2026/04/15/citi-new-cfo-touts-ai-gains-bank-posts-record-24-6-billion-revenue-quarter/)
- [Citigroup, Citi Stylus Workspaces with agentic AI (Sep 2025)](https://www.citigroup.com/global/news/press-release/2025/citi-unveils-citi-stylus-workspaces-agentic-ai-turbocharging-productivity)
- [CFO Dive, Deloitte and HPE AI agents for finance teams](https://www.cfodive.com/news/deloitte-hpe-team-up-to-offer-ai-agents-for-finance-teams/743011/) and [HPE CFO agentic AI priorities](https://www.cfodive.com/news/hpe-cfo-puts-agentic-ai-center-2026-finance-priorities/812097/)
- [Coforge, AI-driven deposit pricing for a UK bank (vendor)](https://www.coforge.com/success-stories/optimizing-deposit-pricing-with-ai-driven-interest-rate-intelligence)

IR sources
- [BNY, Generative AI and the Capital Markets: Transforming Investor Relations (PDF)](https://www.bny.com/assets/corporate/documents/pdf/insights/generative-ai-impact-on-investor-relations.pdf) (PDF text not extracted here; contents known only from search summaries)
- [IR Impact, AI-driven investor relations: from static targeting to agentic workflows (Mar 2026)](https://www.ir-impact.com/2026/03/ai-driven-investor-relations-from-static-targeting-to-agentic-workflows/)
- [Euronext Corporate Solutions, 10 ways AI is transforming investor relations (Jun 2026)](https://www.corporatesolutions.euronext.com/blog/10-ways-ai-is-transforming-investor-relations) (vendor)
- [Q4 and NIRI, Survey says: GenAI poised to impact IR](https://www.q4inc.com/resource-center/blog/survey-says-genai-poised-to-impact-ir-in-a-major-transformative-way) (vendor-run survey)
- [AlphaSense, AI for Investor Relations (Aug 2026)](https://www.alpha-sense.com/resources/research-articles/ai-investor-relations/) (vendor)
- [Q4, AI-native CRM launch (Apr 2026)](https://finance.yahoo.com/sectors/technology/articles/q4-launches-ai-native-crm-121500262.html) and [Q4 AEO for IR Web (Mar 2026)](https://www.businesswire.com/news/home/20260303509243/en/Q4-Launches-AEO-for-IR-Web-to-Help-Public-Companies-Stand-Out-in-AI-Generated-Answers) (vendor)
- [Nasdaq IR Insight](https://www.nasdaq.com/products/ir-intelligence/ir-insight) (vendor)
- [BCG, AI-enabled ESG reporting (white paper)](https://www.bcg.com/assets/2026/white-paper-ai-enabled-esg-reporting.pdf) (not read directly)
- [Workiva, banking solutions](https://www.workiva.com/solutions/banking) (vendor)
- [FINCH: financial text-to-SQL (arXiv 2510.01887)](https://arxiv.org/abs/2510.01887)
- [Multi-agent system for extracting financial KPIs and guidance (arXiv 2505.19197)](https://arxiv.org/pdf/2505.19197)

## Confidence and gaps

- Named-bank evidence is thin. I found no primary-source case of a named bank using GenAI for IR (earnings Q&A prep, sentiment, disclosure checks) or for bank FP&A commentary, NIM/ALM or CIR analytics. Bank items found are adjacent: Goldman Sachs (trade accounting agents, early stage, per CIO statement in press), Citi (agentic platform, regulatory transformation), HPE (non-bank finance case). Nothing here shows a bank-specific quantified benefit.
- IR use-case maturity ratings rest mainly on vendor pages (AlphaSense, Q4, Nasdaq, Euronext) and consultant or industry commentary. Vendor product claims are marketing and unverified independently.
- Vendor or self-reported figures: HPE 40%/50% cycle and 25% cost figures (company and Deloitte; the two figures differ by date); BCG 30-second variance case (single unnamed client); BCG "70% of AI success is people and process" and "staff could fall by half" (BCG estimates); Q4/NIRI survey (sample size not disclosed, 74% expect AI to be standard within five years, 56% cite security as barrier); cash application touchless rate above 90% (vendor-reported, via BCG/SAP).
- Independent or survey-based: Gartner 2025 (183 respondents), Deloitte CFO Signals (North America, cross-industry, not banks), Deloitte 2024 gen AI survey (2,773 leaders, 542 in financial services), FSB reports.
- I could not read several primary documents: the BCG agentic PDF and BNY IR paper (PDF extraction unavailable), the Gartner press release and CNBC (HTTP 403), and the McKinsey finance article (timeout). For those, claims come from search summaries and secondary coverage and should be checked against the originals before external citation.
- A vendor-blog claim that 44% of CFOs use gen AI for five or more use cases (McKinsey, 102 CFOs) was reported by search results but not verified on a McKinsey page; it is not used above.
- Regulatory sources on Reg FD, MNPI and AI are US-oriented (SEC, FINRA) and mostly address advisers and broker-dealers, not issuers. Their application to O!Bank is by analogy. No Kyrgyz-specific rule on AI in banks or on AI in disclosures was found; needs legal and NBKR confirmation.
- No evidence gathered on model performance in Kyrgyz or Russian financial text, or on data-residency constraints in Kyrgyzstan; both are open.
- Not researched: rating-agency and DFI/lender communication practices, IFRS-specific AI reporting guidance, and costs of the tools above.
