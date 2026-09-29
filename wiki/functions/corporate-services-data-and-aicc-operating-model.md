# Corporate Services, Data Office, PMO and the AICC Operating Model: Generative and Agentic AI in Banks

Research date: 2026-09-29. Scope: (A) procurement, vendor management and contracts; (B) administration, facilities, physical security, cash logistics and ATM operations; (C) data office; (D) PMO, transformation, change and AI adoption; (E) the AICC's own operating model.

Evidence note: only the M&T Bank article was read in full. Every other source was read through search-result summaries and not opened on the publisher page (McKinsey, Lloyds, DBS and BCG pages timed out, returned an error, or were blocked when fetched). Treat all figures below as unverified against the primary page unless stated otherwise.

## Why it matters

- These functions are internal, document- and data-heavy, and have no direct customer exposure. They are lower-risk places to build AI skills, controls and platforms. The data office (C) and the operating model (E) also decide whether every other AICC use case scales.
- Named-bank evidence is thin for A, B and D and strong for C and E. For procurement, facilities and PMO the main sources are vendors, consultancies and academic papers. Plan for these as "build and measure", not "copy a bank".
- Value comes from operating discipline more than from tools. McKinsey (State of AI 2025, via summaries) reports that AI high performers are 2.8x more likely to have fundamentally redesigned workflows (55% vs 20%). BCG's 10-20-70 rule puts about 70% of effort in people, process and organisation. Gartner predicts over 40% of agentic AI projects will be cancelled by end of 2027 because of cost, unclear value or weak risk controls.
- Outsourced AI is third-party risk. Basel Committee third-party principles (Dec 2025, via summary) say firms stay fully accountable for outsourced services. The AICC's vendor and model selection therefore belongs inside the bank's vendor-risk process, not beside it.

## Use cases

Maturity is the author's judgement. "Proven" = named-organisation production use documented. "Emerging" = announced, limited, or vendor-reported only. "Experimental" = pilots, academic work or thin evidence. "(vendor)" = figure or claim is self-reported by a seller.

### A. Procurement, vendor management, contract lifecycle

| Use case | What AI does | Maturity | Example or source |
|---|---|---|---|
| Contract clause extraction and review | Extracts and classifies clauses, flags deviations from a playbook, summarises obligations | Proven (loan contracts); emerging for supplier contracts | JPMorgan COiN: Bloomberg (2017) reported it replaced about 360,000 hours a year of lawyer and loan-officer work on commercial loan agreements. This is the bank's estimate, not an audit. No bank case found for supplier contracts |
| Contract drafting from clause library | Generates first drafts from guided questions and approved clauses, routes only non-standard terms to Legal | Emerging | Sirion and EY descriptions (vendor and consultancy). Ivalua claims up to 80% less manual review time (vendor) |
| Obligation and renewal tracking | Pulls dates, SLAs and penalties from executed contracts into alerts | Emerging | Generic CLM vendor material; no bank case found |
| Vendor due-diligence questionnaire automation | Pre-fills questionnaires from SOC 2, ISO and past answers, summarises vendor documents, checks vendor claims against public records | Emerging | CENTRL Vendor360 (vendor claim). A 70% due-diligence time cut is reported for Grasshopper Bank, but that is client onboarding, not vendor risk |
| AI-vendor assessment (buying AI safely) | Structured scoring of a proposed AI vendor into three due-diligence levels | Proven as a method | FS-ISAC Generative AI Vendor Evaluation and Qualitative Risk Assessment (Feb 2024): five domains (use case, business integration, data sensitivity, business resiliency, exposure risk) |
| Sourcing support (RFP drafting, bid comparison, spend classification) | Drafts RFPs, compares bids, classifies spend | Emerging | Ivalua, Beroe (vendor and advisory). No bank case found |

### B. Administration, facilities, physical security, cash logistics

| Use case | What AI does | Maturity | Example or source |
|---|---|---|---|
| ATM and branch cash demand forecasting | Forecasts daily cash need per machine, sets load size | Proven in research and vendor practice; mostly classical ML | Peer-reviewed studies on real bank data: López Lázaro et al. (ScienceDirect, 2018, forecasting plus robust optimisation); Indian bank study (40 ATMs, two years); VTB-affiliated authors (Springer, 2022). One simulation study reports 15-20% lower ATM cost under some interest-rate conditions. No named bank publishes deployed results in the sources found |
| Cash replenishment routing | Joins forecasts with vehicle routing for cash-in-transit | Emerging | 2025 paper on forecasting plus vehicle routing (academic) |
| ATM predictive maintenance and health monitoring | Predicts failures, diagnoses root cause, dispatches technicians | Proven (OEM tooling) | Diebold Nixdorf DN AllConnect Data Engine (vendor description) |
| ATM and branch video analytics | Detects skimmer installation, vehicle ramming, duress, loitering, damage, empty paper or jammed trays | Emerging | NCR Atleos capabilities as described in search summary (vendor); Agrex AI claims 30-50% lower fraud losses (vendor, unverified) |
| Physical-security anomaly correlation | Links branch and parking-lot camera events to alarms | Experimental | Bank of America patents (patents are not deployment evidence) |
| Facilities: work orders, energy, space use, helpdesk | Triages requests, predicts building-system faults, answers staff FAQs | Emerging | Generic; no bank case found. CBA's internal "ChatIT" for IT support is a comparable helpdesk pattern (reported as resolving issues seven times faster than ticketing; secondary source) |
| Admin knowledge assistant (travel, expenses, policies) | Answers staff policy questions with cited text | Proven | Lloyds Athena (RAG over about 13,000 approved articles), DBS-GPT (role-based access to policy content). Both are general knowledge assistants, not admin-specific |

### C. Data office

| Use case | What AI does | Maturity | Example or source |
|---|---|---|---|
| Automated metadata and lineage capture | Parses SQL, stored procedures, BI tools, files and mainframe code to draw lineage | Proven | M&T Bank uses Solidatus and Monte Carlo; lineage built as a core capability, mainframe code the hardest part (American Banker, Sept 2025; read in full) |
| Grounding gen AI on governed data | RAG limited to internal governed sources, with lineage carried into the assistant | Proven | M&T Bank: Copilot for about 16,000 of 22,000 staff; chief data officer says gen AI gets work "about 60%" of the way. Lineage-through-Copilot is a wish, not yet delivered |
| Data-quality monitoring and rule generation | Detects drift and anomalies, drafts rules, flags affected downstream models | Emerging | Monte Carlo at M&T; Alation and Atlan material (vendor) |
| Glossary, catalog descriptions, data classification | Drafts business definitions and tags for steward approval | Emerging | Vendor material (Alation, Atlan, Semarchy); no bank metrics found |
| Master data matching and golden record | Probabilistic and ML entity resolution, steward review of uncertain matches | Proven (ML matching); emerging (gen-AI enrichment) | Practitioner guides; platforms include Informatica, IBM, Profisee, Semarchy, SAP MDG. No named bank result found |
| Self-service analytics, text-to-SQL | Turns questions into SQL over a governed semantic layer | Emerging | Snowflake Cortex Analyst (Bayer example, not a bank), LinkedIn SQL Bot, Wren AI. Sources say raw-schema text-to-SQL has low accuracy and a semantic layer is the usual fix. No bank case found |
| Data-access and regulatory-report support (BCBS 239 style) | Traces report numbers to sources, drafts data-lineage evidence | Emerging | IBM and Solidatus commentary (vendor) |

### D. PMO, transformation, change management, AI adoption

| Use case | What AI does | Maturity | Example or source |
|---|---|---|---|
| Status reports and steering-committee packs | Drafts first version from plan and ticket data; PMO validates | Emerging | Microsoft Planner Copilot, ServiceNow SPM (vendor); no bank case found |
| Schedule, budget and risk prediction | Flags likely slippage and repeated risks across programmes | Emerging | Consultancy and vendor material. Gartner (via summary): AI agents cannot be accountable entities, so PMO staff review outputs |
| Portfolio and resource balancing | Suggests reallocation and dependency conflicts | Experimental | Vendor material only |
| Enterprise AI assistant rollout with champions | Peer network drives adoption and finds use cases | Proven | BBVA: ChatGPT Enterprise from about 3,000 to 11,000 licences, then all 120,000 staff (Dec 2025); "champions" oversee adoption and "wizards" are heavy users who help peers; 250 top directors trained; over 2,900 custom GPTs; about 3 hours saved per week in the 11,000-user pilot (BBVA and Bloomberg via summaries) |
| Role-based AI upskilling | Academies, executive programmes, hands-on workshops | Proven | Lloyds "Leading with AI" (80 hours, 300+ senior leaders expected by end 2026); DBS identified 11,000+ staff in AI-impacted roles for deeper training; Evident: 37 of 50 banks (74%) offer AI-specific training. KBank champion approach is from a Microsoft customer story (vendor-published; its 50% productivity claim is self-reported) |
| Change-impact analysis and comms drafting | Drafts impact assessments, FAQs, training material | Emerging | Generic; no bank case found |

### E. AICC operating model (bank evidence)

| Practice | What the bank does | Maturity | Example or source |
|---|---|---|---|
| Central CoE plus shared platform | One team owns platform, guardrails, logging; use cases built on it | Proven | Lloyds: central AI centre of excellence, Vertex AI-based platform, central logging and platform-layer guardrails; Athena serves 35,000+ colleagues (Lloyds post, June 2026, via summary); 50+ gen-AI solutions deployed in 2025 |
| Central data and AI platforms with responsible-use gate | Two platforms (ADA for data, ALAN for AI) and a cross-functional Responsible Data Use Committee reviewing every use case (PURE criteria) | Proven | DBS; 2025 annual report (via summary) cites 430+ use cases, 2,000+ models, about S$1bn economic value from all analytics and AI/ML, not gen AI alone. Value is measured against control groups and counts revenue, cost saving and risk avoidance |
| Firmwide CDO sets standards, business units execute | Central data governance, model-agnostic LLM platform, bottom-up idea intake | Proven (platform); intake process is not published | JPMorgan LLM Suite (230,000+ users per search summaries). Use-case counts vary across sources (400+, 450+, 500+); ROI is described as tracked per initiative. Mostly secondary sources |
| Central team plus partner co-development | AWS "AI Factory", multi-year OpenAI partnership, chief AI officer role | Proven | CommBank (Aug 2025 partnership; ChatGPT Enterprise rolling out to about 52,000 staff, per CBA newsroom via summary). Multi-vendor pattern |
| Build with risk in the room from day one | Seven-week gen-AI chatbot with QuantumBlack; risk co-designed guardrails; daily regression on 500 real chats; hybrid with existing NLP bot | Proven | ING (via summaries). ING's formal CoE or federation model was not found |
| Group-level ROI disclosure | Publishes value from AI portfolio | Emerging | Evident AI Index 2025: eight banks report group-level ROI estimates (none in the UK). Lloyds says about GBP 50m from gen AI in 2025 and expects over GBP 100m more in 2026 (bank-reported) |

McKinsey guidance (via summaries of "Scaling gen AI in banking" and "Decentering gen AI"): among financial institutions, the share with gen AI use cases in production was 75% for highly centralised, 50% for each of the two middle archetypes, and 30% for highly decentralised. McKinsey expects a later swing toward federated execution as maturity grows, with risk, architecture and partnership choices staying central. BCG (via summary): fewer central priorities (three to four), dedicated governance and transformation capability, and adoption planning. The Financial Brand (secondary) says leading banks centralise strategy, governance and cost management and devolve execution.

## Target state for O!Bank

- Sequencing: a small, centrally led AICC for the first 12 to 24 months, consistent with the McKinsey centralisation evidence. Move execution to business "spokes" only after platform, guardrails and measurement are stable. This is a recommendation, not a bank-proven fact for a bank of O!Bank's size.
- AICC owns: intake and triage, risk tiering, shared LLM gateway and RAG platform, evaluation harness, vendor and model shortlist, value tracking, and the champions network. Business owners own the use case, baseline and benefit. No use case without a named business owner and baseline.
- Intake and prioritisation: one form; risk tier by customer impact, financial impact, data sensitivity, autonomy, reversibility and regulatory relevance (Avenga-style dimensions); score value, feasibility and risk; cap active priorities at a small number (BCG suggests three to four). Weights and thresholds are for O!Bank to set.
- Approval: a cross-functional AI governance group (Risk, Compliance, IT security, Legal, Data, business) in the DBS RDU-committee style. Lower-risk internal assistants get a fast lane. Customer-affecting or decision-making uses get full review.
- Product ownership: each AI product has a business product owner and a technical owner, with a run-cost budget and retirement criteria. The AICC funds shared platform and enablement centrally. Use-case build cost is co-funded by the sponsoring function. No source found gives a funding model to copy, so treat this as a design choice.
- Model and vendor selection: model-agnostic gateway (JPMorgan, Goldman and Lloyds all describe multi-model or replaceable-model designs). Run FS-ISAC-style tiered due diligence on each vendor. Require exit plans, change-notification for model updates, and data-residency terms. Check Kyrgyz personal-data and localisation rules with local counsel before sending client data to foreign APIs (not confirmed in sources; Kazakhstan requires local storage, Kyrgyzstan not verified).
- Champions network: two or three volunteers per function, plus an analytics-based way to spot heavy users (BBVA "wizards"). Give them a use-case backlog, office hours and a light stipend of time, not a central curriculum.
- Data office: treat lineage, glossary and a governed semantic layer as prerequisites for RAG and text-to-SQL, not as a separate programme.
- Corporate services: start with knowledge assistants and contract or vendor-document review (human decides). Use classical ML for ATM cash forecasting. Treat video analytics as a security and privacy project with its own approval.

## Phased adoption path

| Phase | Corporate services (A, B) | Data office (C) | PMO and adoption (D) | AICC operating model (E) |
|---|---|---|---|---|
| Foundation | Policy and contract Q&A assistant over approved documents; clause extraction pilot on a sample of vendor contracts; baseline ATM forecast error and emergency-dispatch counts | Inventory critical data; name owners; glossary for top domains; automated lineage on one priority domain | AI literacy for all; executive session; first champions; PMO drafts status reports with human check | Charter, intake form, risk tiers, governance group, baseline-before-build rule, initial vendor due diligence |
| Scale | Contract obligation tracking; vendor questionnaire pre-fill; ML cash forecasting per ATM; ATM health alerts | Data-quality monitoring on critical elements; steward-reviewed AI descriptions; MDM matching for customers and vendors | Role-based learning paths; champion metrics; PMO risk and slippage flags | Shared LLM gateway, evaluation set, per-initiative value tracking, quarterly portfolio review |
| Platform | Sourcing-to-contract workflow on one platform; routing optimisation for cash-in-transit; facilities request triage | Governed semantic layer; text-to-SQL for named analyst groups; lineage into assistants (M&T's stated goal) | Federated champions with function backlogs; AI in onboarding of new staff | Move execution to business spokes; standard reusable components; funding rules; annual ROI reporting |
| Agentic | Agents that draft vendor renewals and prepare contract redlines for approval; agent-assisted exception handling in cash logistics | Agents that raise data-quality tickets and propose fixes with steward sign-off | PMO agents that chase actions and update plans within set limits | Agent registry, identity and permission limits, human-in-the-loop rules (McKinsey: 65% of high performers define validation vs 23% of others), retirement of failing agents |

## Data and system prerequisites

- Contracts: a single repository of executed contracts with metadata (party, dates, value, owner). Scanned or unstructured contracts need OCR quality checks. Russian, Kyrgyz and English language handling needs testing (no source evaluated this).
- Vendor data: a vendor master with clean identifiers and an inventory of AI features inside existing vendor products.
- ATM and cash: per-ATM transaction history, replenishment records, calendar and event data, holidays, machine status logs. Cash-in-transit contracts and cut-off times as routing constraints.
- Security and facilities: camera inventory, retention rules, an incident log, a work-order system.
- Data office: catalog, glossary, named owners, lineage for critical elements, quality metrics, access classification. A semantic layer of governed metric definitions before any text-to-SQL.
- AICC platform: LLM gateway with logging, prompt and output retention, PII redaction, role-based access, evaluation harness, cost tracking, model registry.
- PMO: consistent project data (plans, risks, budget actuals) in one tool. Gartner (via summary) links AI accuracy to AI-ready data.
- Intake data: baseline measures per use case, otherwise benefit attribution is not possible (arXiv ROI framework, academic).

## Risks and controls

| Risk | Control |
|---|---|
| Hallucinated contract terms or missed clauses | Human sign-off; extraction with source-page citations; test set from historic contracts; no automatic acceptance of legal positions |
| Vendor or model lock-in, concentration, unannounced model changes | Model-agnostic gateway; exit plan; contract clause for change notice; FS-ISAC-tiered due diligence; regulator-aligned third-party register |
| Confidential vendor or client data leaving the bank | Private or in-country hosting where required; PII redaction; contractual no-training terms; legal check on Kyrgyz data-protection and cross-border rules |
| Wrong ATM cash forecasts (empty machines, idle cash) | Service-level target at a stated confidence; fallback rules; monitor forecast error and emergency dispatches |
| Video analytics: privacy, false alarms, staff surveillance | Separate privacy review; retention limits; human review of alerts; no use for employee performance scoring |
| Text-to-SQL returns inconsistent or wrong numbers | Semantic layer; certified metrics only; visible query and lineage; restrict to defined user groups |
| Poor data quality and unknown lineage | Named owners; automated lineage; quality gates before RAG sources go live |
| Shadow AI and uneven adoption | Approved tools with easy access; champions; usage analytics; clear acceptable-use policy (FS-ISAC publishes an acceptable-use framework for external gen AI) |
| Pilot sprawl and agentic hype ("agent washing") | Cap on active priorities; baseline and kill criteria per use case; Gartner cancellation prediction as a caution |
| Over-trust in PMO or forecasting AI | Managers still challenge predictions; AI cannot hold accountability |
| AICC becomes a bottleneck or a silo | Fast lane for low-risk uses; service levels for intake; federated execution once mature |

## Metrics

- Adoption: weekly active users by function; share of staff who completed role-based training; champions per function; custom assistants created (BBVA reports these; usage figures across BBVA sources conflict, so define your own measurement).
- Value: benefit per initiative against its baseline; hours saved converted to a stated use (capacity redeployed or cost avoided), not only reported hours; portfolio-level value versus AI spend. DBS uses control groups where it can.
- Delivery: time from intake to decision; time from decision to production; share of intake approved, deferred, rejected; number of active priorities.
- Procurement and contracts: contract review cycle time; share of contracts with extracted metadata; missed renewals; vendor due-diligence turnaround.
- Cash and ATM: forecast error per ATM; out-of-cash hours; emergency replenishment count; idle cash; replenishment cost per ATM.
- Security and facilities: alert precision; incident response time; work-order resolution time.
- Data office: critical data elements with owner, definition and lineage; data-quality score on critical elements; share of assistant answers from governed sources; text-to-SQL accuracy on a test set.
- PMO: report preparation effort; forecast accuracy for milestones; risks caught early.
- Control: incidents; evaluation pass rate; audit findings; vendors with completed tiered due diligence.

## Sources

Read in full:
- [How M&T Bank ensures data quality as it implements gen AI, American Banker](https://www.americanbanker.com/news/how-m-t-bank-ensures-data-quality-as-it-implements-gen-ai)

Read through search summaries only (page not opened, or fetch failed):
- [Scaling gen AI in banking: Choosing the best operating model, McKinsey](https://www.mckinsey.com/industries/financial-services/our-insights/scaling-gen-ai-in-banking-choosing-the-best-operating-model)
- [Decentering gen AI, McKinsey](https://www.mckinsey.com/featured-insights/charts/decentering-gen-ai)
- [Extracting value from AI in banking: Rewiring the enterprise, McKinsey](https://www.mckinsey.com/industries/financial-services/our-insights/extracting-value-from-ai-in-banking-rewiring-the-enterprise)
- [The state of AI in 2025, McKinsey](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai)
- [AI Transformation Is a Workforce Transformation, BCG](https://www.bcg.com/publications/2026/ai-transformation-is-a-workforce-transformation)
- [AI Talk Is Cheap. Value Creation Is Rare., BCG](https://www.bcg.com/publications/2026/how-ai-leaders-create-competitive-advantage)
- [DBS AI-powered digital transformation, DBS](https://www.dbs.com/artificial-intelligence-machine-learning/artificial-intelligence/dbs-ai-powered-digital-transformation.html)
- [DBS scales AI across 430 use cases, QA Financial](https://qa-financial.com/dbs-bank-scales-ai-across-430-use-cases-as-resilience-demands-grow/)
- [DBS 2025 Annual Report, MarketScreener](https://www.marketscreener.com/news/dbs-2025-annual-report-ce7e5fd9da8af723)
- [DBS approach to AI at scale, Frontier Enterprise](https://www.frontier-enterprise.com/dbss-approach-to-ai-at-scale/)
- [Athena at Lloyds Banking Group, Lloyds Medium](https://medium.com/ai-at-lloyds-banking-group/athena-building-an-ai-powered-knowledge-platform-at-lloyds-banking-group-6b18107e23c9)
- [Lloyds says GenAI delivered GBP 50m of value in 2025, Banking Exchange](https://www.bankingexchange.com/news-feed/item/10536-lloyds-says-genai-delivered-50m-of-value-in-2025)
- [Lloyds champions AI transformation with executive training, BankersGlobe](https://bankersglobe.com/topics/lloyds-champions-ai-transformation-with-executive-training-blitz)
- [CommBank and OpenAI partnership, CommBank newsroom](https://www.commbank.com.au/articles/newsroom/2025/08/tech-ai-partnership.html)
- [CommBank activates AI Factory with AWS, CommBank newsroom](https://www.commbank.com.au/articles/newsroom/2024/09/cba-activates-ai-factory.html)
- [Transforming ING's contact center with generative AI, ING Blog](https://medium.com/ing-blog/transforming-ings-contact-center-with-generative-ai-02cb4f24c542)
- [JPMorgan LLM Suite, The Digital Banker](https://thedigitalbanker.com/jpmorgan-chases-llm-suite-drives-ai-transformation-across-the-enterprise/)
- [JPMorgan COiN, Bloomberg (2017)](https://www.bloomberg.com/news/articles/2017-02-28/jpmorgan-marshals-an-army-of-developers-to-automate-high-finance)
- [JPMorgan COiN, ABA Journal](https://www.abajournal.com/news/article/jpmorgan_chase_uses_tech_to_save_360000_hours_of_annual_work_by_lawyers_and)
- [BBVA ChatGPT Enterprise rollout, Bloomberg](https://www.bloomberg.com/news/articles/2025-12-12/bbva-rolls-out-chatgpt-to-almost-all-employees-in-openai-deal)
- [BBVA and Harvard Business Review, BBVA](https://www.bbva.com/en/innovation/harvard-business-review-recognizes-bbva-as-a-benchmark-for-corporate-ai-adoption/)
- [KBank human-first agentic AI, Microsoft customer story (vendor)](https://www.microsoft.com/en/customers/story/26245-kbank-azure-openai-in-foundry-models)
- [Evident AI Index for banks](https://evidentinsights.com/ai-index/)
- [Evident AI Talent Report, April 2025](https://evidentinsights.com/insights/talent-report/)
- [Gartner: over 40% of agentic AI projects will be canceled by end of 2027](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027)
- [FS-ISAC Generative AI Vendor Evaluation and Qualitative Risk Assessment (Feb 2024)](https://www.fsisac.com/hubfs/Knowledge/AI/FSISAC_GenerativeAI-VendorEvaluation&QualitativeRiskAssessment.pdf)
- [FS-ISAC AI risk papers announcement](https://www.fsisac.com/newsroom/pr-ai-risk-papers)
- [BCBS third-party risk principles, ORX summary](https://orx.org/blog/bcbs-third-party-risk-principles-what-you-need-to-know)
- [EBA proposed third-party risk guidelines, Travers Smith](https://www.traverssmith.com/knowledge/knowledge-container/the-ebas-proposed-expansion-of-third-party-risk-management-requirements/)
- [Improving cash logistics in bank branches with ML and robust optimization, ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0957417417306474)
- [ATM cash demand forecasting in an Indian bank, arXiv](https://arxiv.org/pdf/2008.10365)
- [ATM cash flow prediction, local and global models, PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9791642)
- [Banking video analytics for ATM and branch security, Agrex AI (vendor)](https://www.agrexai.com/banking-video-analytics-for-atm-and-branch/)
- [The future of ATM security, Hyosung Americas (vendor)](https://hyosungamericas.com/blogs/the-future-of-atm-security/)
- [Cortex Analyst self-service analytics, Snowflake (vendor)](https://www.snowflake.com/en/blog/cortex-analyst-ai-self-service-analytics/)
- [Wren AI, GitHub](https://github.com/Canner/WrenAI)
- [How Gen AI is redefining master data management, ZS Associates](https://medium.com/zs-associates/how-gen-ai-is-redefining-master-data-management-7f220bab0b75)
- [Data lineage in banking, Atlan (vendor)](https://atlan.com/know/data-governance/data-lineage-in-banking/)
- [AI in the Project Management Office, Digital Project Manager](https://thedigitalprojectmanager.com/project-management/ai-in-project-management-office/)
- [From oversight to intelligence, CIO](https://www.cio.com/article/4100116/from-oversight-to-intelligence-ais-impact-on-project-management-and-business-transformation.html)
- [Transforming contract management with generative AI, EY](https://www.ey.com/en_us/coo/transforming-contract-management-with-generative-ai)
- [Generative AI in Procurement, Ivalua (vendor)](https://www.ivalua.com/blog/generative-ai-and-the-future-of-procurement-a-recap/)
- [Winning AI playbooks from Chase, BofA, NatWest, The Financial Brand](https://thefinancialbrand.com/news/artificial-intelligence-banking/winning-ai-playbooks-from-chase-bofa-natwest-and-other-retail-banking-leaders-188315)
- [Generative AI in Financial Institution: a global survey, arXiv](https://arxiv.org/pdf/2504.21574)
- [Data protection laws in Kyrgyzstan, DLA Piper](https://www.dlapiperdataprotection.com/?t=law&c=KG)

## Confidence and gaps

- Confidence is highest for E (multiple named banks, McKinsey and BCG guidance, though mostly via summaries) and for C (M&T read in full). Confidence is medium for cash forecasting (solid academic work, no named-bank deployment results). It is low for procurement, facilities and PMO (vendor and generic material; no bank case with results).
- Not found: a primary description of ING's CoE or federation model; JPMorgan's intake and prioritisation process (the sources are secondary, counts vary, and a claimed target of 1,000 use cases by end 2026 was not verified); CBA's formal operating-model document; any bank publishing procurement-AI results; any bank text-to-SQL case; any bank funding model for its AI centre.
- Primary pages for McKinsey, BCG, Lloyds and DBS were not read directly. Quotes and percentages from them should be checked before external use.
- Self-reported figures: DBS S$1bn and Lloyds GBP 50m and GBP 100m value estimates, BBVA time savings, KBank productivity, COiN 360,000 hours, and all vendor percentages. Evident notes only eight banks disclose group-level ROI, so cross-bank comparison is weak.
- Legal points for Kyrgyzstan (personal-data registration, cross-border transfer, localisation, NBKR expectations on outsourcing and AI) were not confirmed. The search found the NBKR SupTech roadmap for 2026-2031, which is about the regulator's own use of AI, not a rulebook for banks. Obtain local legal advice before design decisions.
- Language coverage (Kyrgyz, Russian) for contract extraction and assistants was not evaluated in any source.
- Maturity ratings and the recommended target state are the author's judgement, not findings of the cited sources.
