# Marketing, Product, Ecosystem and Channels: Generative and Agentic AI at O!Bank

Scope: (A) marketing, brand, content and CRM/campaigns; (B) product management and digital channels; (C) strategy, market and competitor intelligence, customer insight; (D) payments, cards and ecosystem/telco-bank synergies, including agentic commerce; (E) branch network and channel optimisation. Research date: 2026-09-29. Figures are as reported by the source; none are O!Bank results. Context about ALGA Group, O! and O!Dengi is treated as unverified.

Reading note: most sources were read through search-result summaries only. Only the Grab press release and the DBS AI page were opened in full. Sources marked (summary) were not opened. Kaspi's 3Q 2025 results PDF and the McKinsey agents article could not be read (PDF unreadable, fetch timed out), so their claims are second-hand.

## Why it matters

- Marketing, product and channel work is where a bank meets the customer every day, and it is where the best-documented gen-AI results in retail banking sit. DBS reports 30 million personalised insights and nudges a month in Singapore alone (DBS, self-reported). Klarna reports lower marketing cost with more campaigns (Klarna, self-reported). Both are large, data-rich firms, so they are upper bounds for O!Bank.
- Super-app peers are moving fast. Kaspi (Kazakhstan, Kazakh and Russian) is rolling out AI tools for merchants and a consumer assistant, Grab has an AI assistant for merchants that will suggest financing, and Ant and Sber are rebuilding their apps around assistants. An ecosystem bank that lacks this will be compared with them by customers in the region (Kaspi, Grab, Ant, Sber via summaries or company releases).
- Control of the customer interface is shifting. McKinsey argues gen-AI agents threaten retail banks' customer relationships, and reports that LLMs recommend digital-native lenders and fintechs more often than web search does (survey n = 3,945, July 2025; McKinsey via summary). Card networks are building agent-payment rails that put the issuer behind an agent, not in front of the customer.
- Regulation is a design input. Financial advertising rules, consent for personal data, and (for any EU-linked activity) chatbot and synthetic-content disclosure apply to these use cases. Kyrgyz consent rules appear strict and formal, which limits personalisation until consent capture is fixed (see Risks).

## Use cases

Maturity key: proven = live at scale at named institutions or long-established; emerging = live at some institutions or early production, evidence is mostly company-reported; experimental = pilots, announcements, vendor claims, or no primary evidence found.

### A. Marketing, brand, content, CRM

| Use case | What AI does | Maturity | Example or source |
|---|---|---|---|
| Personalised nudges and next-best-action in the app | ML models choose the message; gen AI can write and vary the text | Proven (ML selection); gen-AI text emerging | DBS: 100+ AI/ML algorithms over an internal data mart of 15,000 customer data points, seven nudge types, 3.5m+ customers, 30m insights a month in Singapore (self-reported; [DBS](https://www.dbs.com/artificial-intelligence-machine-learning/index.html)). BofA: 1.7bn proactive insights from Erica by Aug 2025 (company release, summary; [BofA](https://newsroom.bankofamerica.com/content/newsroom/press-releases/2025/08/a-decade-of-ai-innovation--bofa-s-virtual-assistant-erica-surpas.html)) |
| Creative and image generation | Produces image variants and copy, adapts sizes and formats | Emerging | Klarna (May 2024): sales and marketing spend down 11% in Q1 2024 with more campaigns; AI credited with about USD 10m annualised savings, including image production; image cycle from six weeks to seven days; uses Midjourney, DALL-E, Firefly (self-reported, via summaries; [Klarna](https://www.klarna.com/international/press/ai-helps-klarna-cut-marketing-agency-spend-by-25-and-run-more-campaigns/)). Reports differ on whether the image saving was USD 1.5m in Q1 or 6m annualised |
| Copywriting assistant with brand voice | Drafts and rewrites copy inside approved tone and terminology | Emerging | Klarna says its Copy Assistant handles most copywriting (self-reported, summary). Nubank applies a versioned "tone and style" check per market to support conversations (summary; [Building Nubank](https://building.nubank.com/building-ai-agents-for-131-million-customers/)) |
| Marketing compliance pre-check | Reads a draft asset against regulation and internal policy, flags breaches, suggests fixes; human approver decides | Emerging | Onix case study of a digital bank using Vertex AI and document extraction over FCA Handbook, ASA guidelines and internal policy; multilingual checks were a planned next step (vendor case study, summary; [Onix](https://www.onixnet.com/case-study/digital-bank-automates-marketing-compliance-with-generative-ai/)) |
| Consent-aware audience selection and journey orchestration | Selects audience and channel using consent flags, frequency caps and suppression lists; generates variants only for permitted segments | Proven (orchestration); consent enforcement is an engineering task, not an AI feature | McKinsey "next best experience": generated messages usually reviewed by marketing or compliance at first, with guardrails and templates later allowing scale with less oversight (summary; [McKinsey](https://www.mckinsey.com/capabilities/growth-marketing-and-sales/our-insights/next-best-experience-how-ai-can-power-every-customer-interaction)) |
| Personalised, generated messages at individual level | Tailors text, tone, timing, visuals and price to each customer | Experimental for banks | McKinsey (April 2026) describes this as the direction and quotes banks reporting a 65% increase in cross-sales and 30% net annual growth in primary customers. This is a consultancy claim without a named bank (summary) |
| Localisation to Russian and Kyrgyz | Translates and adapts copy, checks tone, terminology and script | Russian: emerging. Kyrgyz: experimental | A July 2026 benchmark (KyrgyzLLM-Bench) is described as the first large-scale LLM evaluation in Kyrgyz, covering 26 models; Kyrgyz is described as underrepresented and morphologically rich. Model ranks transfer only partly from English (arXiv, summary; [arXiv](https://arxiv.org/abs/2607.17173)). Kaspi's Kasper works in Kazakh and Russian (press, summary) |
| Generative-engine visibility (how LLMs describe the bank) | Audits and improves how the bank and its products appear in LLM answers | Experimental | McKinsey survey above; Deloitte recommends auditing brand appearance in LLM results and making rates, fees and disclosures machine-readable (summary; [Deloitte](https://www.deloitte.com/us/en/insights/industry/financial-services/bank-customers-generative-ai-trust.html)) |

### B. Product management and digital channels

| Use case | What AI does | Maturity | Example or source |
|---|---|---|---|
| In-app assistant (money questions, card and account actions) | LLM assistant reads the customer's own app data, answers questions, prepares actions; sensitive actions need customer confirmation | Emerging | Revolut AIR, rolled out to 13m UK customers from 9 April 2026; uses only data already visible in the app, biometric approval for sensitive actions, zero data retention with AI partners (company statements via press, summary; [Fintech Weekly](https://www.fintechweekly.com/news/revolut-air-ai-assistant-uk-customers-launch-2026)). Sber put GigaChat in its mobile app in Dec 2024 (summary) |
| Virtual assistant at scale | Rule-plus-model assistant for balances, payments, insights | Proven | Bank of America Erica: over 3 billion interactions since 2018 by Aug 2025; about 20m users interacted nearly 700m times in 2025 (company; [BofA 2026 release](https://newsroom.bankofamerica.com/content/newsroom/press-releases/2026/03/bofa-ai-and-digital-innovations-fuel-30-billion-client-interacti.html), summary). Note: the user counts in the two releases are not comparable |
| Agentic customer service | Agents complete service tasks with an auditor model checking conversations | Emerging | Nubank: LLMs give the first response on about 60% of about 8.5m monthly contacts; an auditor LLM scores every conversation on binary criteria (Nubank engineering blog and secondary summaries; [Building Nubank](https://building.nubank.com/building-ai-agents-for-131-million-customers/)) |
| Conversational and voice channels in regional markets | Chat and voice agents in local languages for product questions, collections, deposits | Emerging | Uzbek banks have rolled out in-app assistants and voice agents in 2026 (commentary-style sources, summary; treat with caution). No Kyrgyz example found |
| Product discovery in the app | Search, guidance and recommendations surface the right feature at the right time | Emerging | Monzo says ML-driven discovery, search and guidance are being built with an in-house experimentation platform (Monzo blog, summary; [Monzo](https://monzo.com/blog/machine-learning-at-monzo-in-2025)) |
| Feature discovery from feedback | LLM clusters app-store reviews, support chats and survey text into themes and requests, translates, links themes to product areas | Emerging (methods published; no bank case found) | Methods: LLM-enhanced topic modelling and prompting to extract aspects, sentiment and actionable suggestions (arXiv 2509.20953, Medium blueprints; summary). Teradata describes LLM classification of bank complaint letters attached to customer records (vendor, summary) |
| Experimentation and A/B testing with AI support | AI drafts variants and analyses results; the statistical design stays with analysts | Proven (A/B testing); gen-AI variants emerging | Monzo reports structured trials with usage and satisfaction metrics, but for engineering tools, not customer A/B tests (podcast write-up, summary). No bank case of gen-AI-driven customer experiments verified |
| Rapid prototyping for product and design | Designers and PMs prototype flows with AI tools | Emerging | Monzo: designers can prototype with AI tools (podcast write-up, summary) |

### C. Strategy, market, competitor intelligence, customer insight

| Use case | What AI does | Maturity | Example or source |
|---|---|---|---|
| Voice of customer and complaints analytics | Classifies complaints and reviews by topic and severity in Russian, Kyrgyz and English; routes regulatory complaints; feeds churn signals | Emerging | Teradata bank example (vendor); research on mobile-banking app reviews ([arXiv 2503.11861](https://arxiv.org/pdf/2503.11861), summary). Kyrgyz text classification is a known weak point (see localisation row) |
| Market and competitor monitoring | Reads competitor pricing, product pages, app updates, press and regulatory notices; drafts a periodic brief | Emerging (mostly tooling, few bank disclosures) | No bank primary source found. McKinsey Panorama is a consultancy offering (summary) |
| Customer research synthesis | Summarises interviews, surveys and support logs; proposes hypotheses for testing | Emerging | McKinsey lists "content synthesis" and customer sentiment analysis as gen-AI use cases (summary). Synthetic respondents (AI-simulated panels) for banking: no credible source found; treat as experimental |
| Customer-trust sensing | Tracks how customers feel about AI in banking to set product design limits | Proven as survey method | Deloitte survey of nearly 2,600 US banking customers: 72% concerned about sharing financial information with gen-AI tools; 79% trust their bank's own website when researching products (summary) |
| Strategy support for leadership | Drafts scenario analysis and briefing notes from internal and external data | Experimental | Only consultancy commentary found; BCG reports 25% of institutions have built AI capabilities into strategy, the rest are in siloed pilots (summary; [BCG](https://www.bcg.com/publications/2025/for-banks-the-ai-reckoning-has-arrived)) |

### D. Payments, cards, ecosystem and telco-bank synergies

| Use case | What AI does | Maturity | Example or source |
|---|---|---|---|
| Ecosystem personalisation and cross-sell | Uses combined behaviour across services for offers | Proven (ML) in large ecosystems | Sber reports AI contributed over 350bn roubles of extra profit in 2024, covering all AI use, not gen AI alone (summary). Marketing lifts attributed to GigaChat come from a secondary blog with no numbers; not relied on |
| Merchant assistant (SME services) | Gives merchants advice, creates ad campaigns, edits menus and catalogues, later proposes financing | Emerging | Grab AI Merchant Assistant, unveiled 8 April 2025, built with OpenAI and Anthropic models; the release gives no performance figures; says it will soon suggest financing from GrabFin and Grab's digital banks ([Grab](https://www.grab.com/sg/press/others/grab-deploys-agentic-ai-to-empower-merchants-and-driver-partners/), read in full). Kaspi Ai for partners: product pages, AI photos and descriptions; about 500K popular marketplace products improved, full merchant rollout planned from January 2026 (Kaspi 3Q 2025 results via summary) |
| Merchant-built agents | Merchants build service agents without coding on the platform | Emerging | Ant Group AI agent platform, agents deployed in about a minute inside Alipay mini-programs (summary; [Ant](https://www.antgroup.com/en)) |
| Consumer life assistant across the ecosystem | Natural-language assistant that orders, books and pays inside the ecosystem | Emerging | Ant Zhixiaobao (2024); Kaspi Kasper (2026, Kazakh and Russian, Almaty first); Grab AI Assistant (Singapore first). Timing details differ across sources (summary) |
| Telco data for credit and offers | Uses airtime, mobile-money and top-up behaviour for scoring and offers | Proven (ML) in Africa | Safaricom M-Shwari and Fuliza, MTN with Jumo (summary; [PYMNTS](https://www.pymnts.com/digital-first-banking/2023/machine-learning-helps-expand-credit-access-in-emerging-markets)). A 2026 High Court petition in Kenya challenges Safaricom's AI chatbot and automated decisions on privacy and fair-administrative-action grounds (summary; [Nation](https://nation.africa/kenya/business/safaricom-sued-over-ai-use-in-customer-service-and-m-pesa-decisions-5433484)). Telco-data use needs a legal basis that Kyrgyz law may not readily give (see Risks) |
| Agent-initiated payments (issuer side) | Issues agent-bound tokens, checks agent identity and consent, lets the customer revoke | Emerging in advanced markets; experimental for Kyrgyzstan | Mastercard Agent Pay (Agentic Tokens, launched April 2025; Citi and US Bank pilot; first authenticated transactions in Australia, Singapore, India; UOB and DBS live in Singapore). Visa Intelligent Commerce and Trusted Agent Protocol; DBS first APAC bank pilot, Feb 2026 (network and press, summary; [Visa](https://www.visa.com/en-us/solutions/intelligent-commerce)). No Central Asian pilot found |
| Fraud and payment nudges | Human-set thresholds trigger warnings on risky payments | Proven | DBS describes nudges used for risk and fraud with humans setting thresholds and curating messages (summary; [DBS](https://www.dbs.com/artificial-intelligence-machine-learning/artificial-intelligence/agentic-ai-is-here-are-we-ready-to-govern-it.html)) |

### E. Branch network and channel optimisation

| Use case | What AI does | Maturity | Example or source |
|---|---|---|---|
| Site selection and network design | Models deposit and loan potential, cannibalisation and catchment; recommends open, close, relocate, downsize | Proven (analytics, not gen AI) | Vendor case studies only: Precisely (unnamed North American bank, 36 months of branch data in a data mart); Mapping Analytics (unnamed bank, alternative site with more deposit potential). Marketing claims; not independently checked (summary) |
| Footfall and mobility analytics | Uses mobility and traffic data to forecast branch demand | Emerging | Korem (vendor, summary) |
| Channel-mix decisions | Compares digital and branch cohorts on retention and value | Proven as analytics | Korem cites Novantas: first-year retention 50% for digitally opened accounts versus 80% for in-branch (secondary, unverified; US-specific) |
| Branch staff assistant | Prepares advisers with customer context and suggested topics | Emerging | DBS reports a platform prompting relationship managers on topics, linked to 16% higher client engagement (self-reported; [DBS](https://www.dbs.com/artificial-intelligence-machine-learning/index.html)); BofA EricaAssist supports 18,000+ service staff and cuts call time by nearly a minute (company, summary) |
| Generative AI for network decisions | LLM explains and drafts network proposals over the analytic outputs | Experimental | No source found; the decision model remains classical analytics |

## Target state for O!Bank

"Fully adopted" means:

- One consent and preference layer that every campaign, nudge and assistant reads. It records purpose, channel, language and withdrawal, and in code blocks any message to a customer without a valid basis.
- A content factory: approved brand voice, product facts and legal wording held as governed source material; gen AI drafts in Russian and Kyrgyz from that material; an automated compliance pre-check plus a named human approver for anything with prices, rates, returns or risk statements; a log of what was generated, checked and approved.
- Personalisation driven by a decision engine (rules and ML) that picks the offer, with gen AI only phrasing it. Offers are checked for suitability, fair treatment and frequency limits.
- An in-app assistant inside the O!Bank app, answering from the customer's own data and product documents in both languages, prepared to hand over to a person, and asking for confirmation before any money movement.
- A product-insight loop: reviews, chats, complaints and NPS text are classified continuously, tied to journeys and releases, and reviewed with product owners each cycle. Experiments run on a standard platform with pre-registered metrics.
- Ecosystem services with clear data boundaries between bank, telco and payment entities, using only data with a documented legal basis, so cross-sell is explainable to the customer and the regulator.
- Merchant and SME tools that help owners with catalogues, campaigns and cash-flow insight, with financing offers routed through normal credit policy.
- Agent-readiness for payments: a defined position on agent identity, tokenised credentials, spending limits and revocation, taken up when the card networks and local switch support it.
- A branch and channel model driven by cohort economics and catchment analytics, with closure decisions reviewed for access and customer harm.

## Phased adoption path

**Foundation**
- Agree an inventory and risk tier for marketing, product and channel use cases. Define what is never automated: final wording of rate, fee, return and risk statements; claims about guarantees; use of sensitive data.
- Fix consent capture and preference storage with local counsel review of Kyrgyz personal-data rules; assess whether current click-consent meets the law.
- Build approved-content library (product facts, disclosures, brand voice, glossary in Russian and Kyrgyz).
- Start low-risk internal uses: copy drafting with human approval, review and complaint theme mining on de-identified text, competitor and press summaries, meeting and research synthesis.
- Set a Kyrgyz-language evaluation set of real O!Bank texts (product terms, complaints, campaign copy) and test candidate models on it before any customer-facing use.

**Scale**
- Add an automated compliance pre-check ahead of human approval; measure agreement with approvers before relying on it.
- Personalised nudges through the decision engine with gen-AI phrasing, first for low-risk topics (education, feature tips, milestones), with control groups.
- Complaints and review analytics wired to product backlog and service quality; monthly insight review.
- Standard experimentation process; AI used to draft variants and summarise results.
- First branch-network analytics project on internal cohort data.
- Merchant-side tools for catalogue and campaign drafting if O!Dengi or the merchant base offers a channel.

**Platform**
- Customer-facing assistant in the app, read-only first (questions, insights, product explanations), grounded in product documents and the customer's own data, with human handover and conversation audit.
- Shared customer-data and feature platform across bank and ecosystem services under documented legal bases; unified journey analytics.
- Merchant assistant with financing suggestions through credit policy, where a lawful data basis exists.
- Continuous monitoring: message quality, bias across segments and languages, complaint rate after AI-driven contact.

**Agentic**
- Assistant that executes actions (payments, card controls, product applications) with strong authentication and per-action confirmation.
- Marketing agents that plan and run campaigns inside budget, audience and frequency limits, with a person approving each campaign and any wording change.
- Agent-initiated payments (issuer side: agent-bound tokens, limits, real-time revocation) once networks and local rules support it. Not a near-term item for Kyrgyzstan on the evidence found.
- Ecosystem agents spanning telecom, wallet and bank journeys, only where data-sharing consent, dispute handling and liability are defined.

## Data and system prerequisites

- Customer identity resolution across bank, wallet and telecom records, with purpose-tagged consent attached to each record.
- Consent and preference service, with real-time checks in campaign, messaging and assistant flows.
- Customer data platform or feature store with lineage, and a governed way to build and reuse features.
- Campaign and journey orchestration tool with suppression, frequency caps, and a full audit trail of what each customer received.
- Approved-content repository and retrieval layer (RAG) with versioning and owners; glossary for Russian and Kyrgyz.
- Model gateway: choice of models, prompt and output logging, PII redaction, region and data-residency controls, vendor exit plan.
- Evaluation harness for Russian and Kyrgyz quality, factual accuracy against product documents, and safety.
- Text pipeline for reviews, chats, call transcripts and complaints, including speech-to-text quality in Kyrgyz and Russian (not evidenced in the sources).
- Experimentation platform and product analytics events consistently defined across iOS, Android and web.
- Branch and ATM data: transactions by channel, staffing, catchment demographics, cohort value; mobility data where legally usable.
- For agentic payments: token service, strong customer authentication, agent registry, real-time revocation, dispute process. These depend on card network and national switch (Elcart, ELQR) readiness.

## Risks and controls

| Risk | Control |
|---|---|
| Misleading or non-compliant advertising (returns, fees, rates, guarantees) | Approved claims library; automated pre-check plus named human approver; log of approvals. Kyrgyz advertising rules bar guaranteeing or implying future returns on financial and investment services (summary); exact Law on Advertising and NBKR requirements were not verified: confirm with counsel |
| Consent and legal basis for personalisation | Kyrgyz law on personal data (No. 58 of 2008) requires free, specific, conscious consent, written or electronically signed; the Internet Society Kyrgyz Chapter study says click-box consent is legally uncertain and most surveyed firms did not inform users properly (summary). Registration rules for data holders changed in 2025-2026 and status should be checked with the data-protection agency. Fix consent first, get legal advice, and consider cross-border transfer wording in consent forms if models run offshore |
| Telco or ecosystem data reused across entities | Legal basis per purpose; separate consent for cross-entity sharing; minimum data; DPIA-style review. Kenyan litigation over Safaricom's automated systems shows the scrutiny risk (summary) |
| Hallucination in assistants (wrong fees, wrong rights) | Grounding on approved documents; answer only from retrieval; block topics that need a human; test sets updated with each product change. The CFPB flagged inaccurate chatbot answers, failure to recognise consumer rights, and blocked access to humans ([CFPB](https://www.consumerfinance.gov/about-us/newsroom/cfpb-issue-spotlight-analyzes-artificial-intelligence-chatbots-in-banking/), 2023, US) |
| Weak Kyrgyz quality | Evaluate on real O!Bank text; native-speaker review; fallback to Russian or human; do not release Kyrgyz marketing or assistant answers without a measured pass rate |
| Manipulative or dark-pattern personalisation, vulnerable customers | Rules on what may be personalised (no exploitation of distress signals); frequency caps; fairness and vulnerability review. EU AI Act bans manipulative techniques causing significant harm (summary); not binding in Kyrgyzstan but a useful design benchmark |
| Disclosure of AI use and synthetic content | Tell customers when they talk to AI; label synthetic media where required. EU AI Act Article 50 transparency applies from 2 August 2026 in the EU (summary; confirm current status). Kazakhstan's AI law (in force 18 January 2026) requires clear labelling of synthetic content (summary). Kyrgyzstan is described as favouring self-regulation, with a Digital Code recently adopted (Eurasianet via summary); applicable duties unverified |
| Third-party model and vendor risk | Contract terms on data retention and training; exit plan; model risk inventory. The FCA expects firms to keep responsibility for outcomes and to manage vendor risk (summary) |
| Brand and IP risk in generated creative | Rights and licence check for tools; human brand review; do not generate real-person likenesses or testimonials |
| Agentic payments: unauthorised or disputed agent transactions | Agent-bound tokens, spending limits, real-time revocation, clear liability rules; do not enable before dispute handling is defined |
| Disintermediation by outside assistants | Make product data, rates and disclosures accurate and machine-readable; monitor how external LLMs describe O!Bank (McKinsey, Deloitte via summaries) |
| Branch closures harming access | Access and customer-harm test before each closure; keep assisted channels for customers less able to use digital |
| Overstated vendor or consultancy benefits | Require control groups and O!Bank baselines; do not use published percentages as targets |

## Metrics

- Marketing: time from brief to approved asset; share of assets passing compliance pre-check first time; rework rounds; approval error rate found in audit; campaign response and conversion against control; opt-out and complaint rate after AI-driven contact; consent coverage of the active base.
- Personalisation: share of messages sent with valid consent; uplift versus control; frequency per customer; fairness across language and segment.
- Assistant and service: containment rate with resolution verified by an auditor; handover rate; accuracy score on a test set; complaint rate; customer satisfaction; time to human when requested.
- Product: time from review or complaint to backlog item; number of shipped changes traced to feedback themes; experiment count and share with valid design; feature adoption.
- Insight: coverage of complaints classified; precision of classification in Kyrgyz and Russian; time to detect a new issue.
- Ecosystem: cross-holding of products per customer; conversion of ecosystem offers; merchant activation and retention; share of offers with documented data basis.
- Payments: (later) agent-initiated transaction share, dispute and fraud rate, revocation time.
- Channels: contribution per branch and per channel; cannibalisation; customer retention by acquisition channel; access coverage after network changes.
- Governance: use-case inventory coverage; incidents per quarter; audit findings closed on time.

## Sources

Read in full:
- [Grab: AI Merchant Assistant and Driver Companion (press release)](https://www.grab.com/sg/press/others/grab-deploys-agentic-ai-to-empower-merchants-and-driver-partners/)
- [DBS: AI-powered personalised nudges](https://www.dbs.com/artificial-intelligence-machine-learning/index.html)

Read through search summaries only:
- [DBS: agentic AI and governance](https://www.dbs.com/artificial-intelligence-machine-learning/artificial-intelligence/agentic-ai-is-here-are-we-ready-to-govern-it.html)
- [DBS: CSO Assistant](https://www.dbs.com/newsroom/DBS_empowers_its_Customer_Service_Officers_with_Gen_AI_powered_virtual_assistant_to_reduce_toil_and_enhance_customer_experience)
- [Bank of America: Erica 3 billion interactions (Aug 2025)](https://newsroom.bankofamerica.com/content/newsroom/press-releases/2025/08/a-decade-of-ai-innovation--bofa-s-virtual-assistant-erica-surpas.html)
- [Bank of America: 30 billion client interactions (Mar 2026)](https://newsroom.bankofamerica.com/content/newsroom/press-releases/2026/03/bofa-ai-and-digital-innovations-fuel-30-billion-client-interacti.html)
- [Nubank: AI agents for 131 million customers](https://building.nubank.com/building-ai-agents-for-131-million-customers/)
- [Revolut AIR launch (Fintech Weekly)](https://www.fintechweekly.com/news/revolut-air-ai-assistant-uk-customers-launch-2026)
- [Klarna: AI cuts agency spend by 25% (company press release; page returned 403/empty, figures from Payments Dive, Marketing Dive and Yahoo Finance summaries)](https://www.klarna.com/international/press/ai-helps-klarna-cut-marketing-agency-spend-by-25-and-run-more-campaigns/)
- [Onix: digital bank automates marketing compliance (vendor case study)](https://www.onixnet.com/case-study/digital-bank-automates-marketing-compliance-with-generative-ai/)
- [McKinsey: next best experience](https://www.mckinsey.com/capabilities/growth-marketing-and-sales/our-insights/next-best-experience-how-ai-can-power-every-customer-interaction)
- [McKinsey: how gen AI agents threaten retail banks' customer relationships](https://www.mckinsey.com/industries/financial-services/our-insights/how-gen-ai-agents-threaten-retail-banks-customer-relationships) (fetch timed out)
- [Deloitte: bank customers' trust in gen AI](https://www.deloitte.com/us/en/insights/industry/financial-services/bank-customers-generative-ai-trust.html)
- [BCG: For banks, the AI reckoning has arrived](https://www.bcg.com/publications/2025/for-banks-the-ai-reckoning-has-arrived)
- [Kaspi 3Q and 9M 2025 results (PDF unreadable in fetch; content via search summary)](https://ir.kaspi.kz/media/3Q_2025_Results_.pdf)
- [Kaspi Kasper announcement (Yahoo Finance)](https://finance.yahoo.com/technology/ai/articles/watch-kaspi-event-mikheil-lomtadze-unveils-kasper.html)
- [Ant Group](https://www.antgroup.com/en) and [Zhixiaobao launch (Business Wire)](https://www.businesswire.com/news/home/20240904932587/en/Ant-Group-Launches-AI-Powered-Mobile-App-Zhixiaobao-at-2024-INCLUSIONConference-on-the-Bund)
- [Visa Intelligent Commerce](https://www.visa.com/en-us/solutions/intelligent-commerce); [Mastercard Australia first authenticated agentic transactions](https://www.mastercard.com/news/ap/en/newsroom/press-releases/en/2026/mastercard-accelerates-ai-powered-commerce-with-australia-s-first-authenticated-agentic-transactions-using-agent-pay/); [Finextra: Mastercard and Visa enlist banks for pilots](https://www.finextra.com/newsarticle/47316/mastercard-and-visa-enlist-banks-for-agentic-payment-pilots)
- [PYMNTS: ML and credit access in emerging markets](https://www.pymnts.com/digital-first-banking/2023/machine-learning-helps-expand-credit-access-in-emerging-markets); [Nation: Safaricom sued over AI use](https://nation.africa/kenya/business/safaricom-sued-over-ai-use-in-customer-service-and-m-pesa-decisions-5433484)
- [Monzo: machine learning in 2025](https://monzo.com/blog/machine-learning-at-monzo-in-2025)
- [arXiv 2509.20953: LLM review analysis](https://arxiv.org/pdf/2509.20953); [arXiv 2503.11861: mobile banking app reviews](https://arxiv.org/pdf/2503.11861); [Teradata: complaint resolution (vendor)](https://www.teradata.com/insights/data-analytics/optimizing-customer-complaint-resolution)
- [KyrgyzLLM-Bench (arXiv 2607.17173)](https://arxiv.org/abs/2607.17173); [KyrgyzBERT (arXiv 2511.20182)](https://arxiv.org/abs/2511.20182)
- [Kyrgyz Law on Personal Information (DPA)](https://dpa.gov.kg/en/npa/4); [DLA Piper: Kyrgyzstan data protection](https://www.dlapiperdataprotection.com/?t=law&c=KG); [ICNL guidance note, Aug 2025](https://www.icnl.org/wp-content/uploads/KG-Personal-Data-Guidance-Note_August-2025_eng.pdf); [Internet Society Kyrgyz Chapter study](https://isoc.kg/news/research-on-personal-data-in-the-commercial-sector-of-the-kyrgyz-republic/)
- [Eurasianet: Kyrgyzstan and AI self-regulation](https://eurasianet.org/more-carrot-than-stick-kyrgyzstan-embraces-self-regulation-for-ai-development) (fetch returned 403; via search summary); [EY: Kazakhstan AI law](https://www.ey.com/en_kz/technical/tax-alerts/2025/12/law-on-artificial-intelligence-kazakhstan)
- [CFPB: chatbots in banking](https://www.consumerfinance.gov/about-us/newsroom/cfpb-issue-spotlight-analyzes-artificial-intelligence-chatbots-in-banking/); [FCA: AI approach](https://www.fca.org.uk/firms/innovation/ai-approach); [EU AI Act Article 50 guide](https://artificialintelligenceact.eu/transparency-rules-article-50/)
- [ALGA Group about us](https://algagroup.com/about-us)
- Branch analytics (vendor): [Precisely case study](https://www.precisely.com/resource-center/customerstories/north-american-bank-uses-precisely-location-data-and-analytics-for-branch-sales-growth/); [Korem guide](https://www.korem.com/a-guide-to-branch-network-optimization/); [Mapping Analytics](http://www.mappinganalytics.com/site-selection/bank-marketing.html)

## Confidence and gaps

- Confidence is medium for the shape of use cases and maturity ratings, and low for any quantified effect. Almost all effect figures are self-reported by the firm (DBS, Klarna, BofA, Revolut, Nubank, Grab) or by consultancies without named banks (McKinsey, BCG). None are audited or transferable to O!Bank.
- Only two sources were opened in full. The rest were read as search summaries, and Kaspi's results document could not be read at all.
- No Kyrgyz-specific evidence found on: financial advertising rules (Law on Advertising, NBKR requirements), electronic consent practice, AI obligations under the new Digital Code, or the current status of data-holder registration. These need local counsel.
- No source describes O!Bank, O!Dengi or ALGA Group AI projects. ALGA's site says it uses AI and big data but names no products (summary).
- No bank case found for: gen-AI-driven customer A/B testing, synthetic respondents, gen-AI competitor monitoring, or Kyrgyz-language marketing generation.
- Branch optimisation evidence is vendor material with unnamed banks. Net effects of closures on customer harm and retention in Kyrgyzstan are unknown.
- Agentic commerce: no Central Asian pilot found. Network announcements describe capability, not customer adoption. Timeline differences between sources (for example Mastercard US rollout dates) come from third-party explainers.
- Dates in fast-moving items (Kasper launch, EU AI Act timing, Kyrgyz registration rules) differ between sources or may have changed; recheck before use.
