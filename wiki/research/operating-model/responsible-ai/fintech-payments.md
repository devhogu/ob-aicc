# Responsible AI positioning: fintechs, payments companies and digital-finance players

Research note for the AI Competence Center, O!Bank Kyrgyzstan. Researched 2026-09-30.

**Reading key.** [F] means the company's own page or a linked document was fetched and read. [S] means the point was read only through a web-search summary and has not been checked against the primary page. Where nothing public was found, the entry says so. Nothing here is a quotation unless it is in quotation marks and was seen in a fetched page or a search summary that quoted it.

## Company entries

### Mastercard (payments network)
- **Principles.** "Data & Tech Responsibility Principles". Sources describe them as privacy and security, transparency, accountability, fairness and inclusion. One summary also lists innovation and positive impact. [S] The official page returned HTTP 403 and was not read.
- **Governance.** An AI Governance program that reviews built and bought AI systems for fairness, efficacy and transparency, reportedly begun in 2019. [S] An AI Governance Council is reported. [S] A vendor case study (Credo AI) [F] describes an AI Governance team, a review group drawn from Security, Legal, Privacy, Brand, Technology and Strategy, an enterprise risk categorisation that routes each generative AI use case to a matching level of oversight, an AI registry of internal and third-party AI, an intake questionnaire, and a vendor evidence portal. The case study names no council, no risk tiers and no start year.
- **Distinctive.** Agentic commerce. Agent Pay (announced April 2025) uses agentic tokens limited by agent, merchant, category, amount and time. A "Know Your Agent" registration step and "Verifiable Intent" (March 2026) provide proof of authorisation and an audit trail. [S] Mastercard research reported that only about 10% of consumers would let an agent complete a purchase autonomously. [S]

### Visa (payments network)
- **Principles.** No standalone responsible AI principles found. The public material is product-led: Intelligent Commerce and the Trusted Agent Protocol. [S]
- **Governance.** Not published. Visa says it has more than 30 years of AI and machine-learning use in risk and fraud. [S]
- **Distinctive.** Consumers set spending limits and conditions, and only the consumer instructs the agent or activates a credential. Agent-initiated purchases carry distinct identifiers so banks can adjust risk rules, and agent-bound tokens tie a credential to a specific authorised agent. [S] The Trusted Agent Protocol (developed with Cloudflare) lets merchants verify signed agent requests. It is designed to resist replay and to separate trusted agents from rogue bots. [S] Visa's page states that described features are potential features of the fully deployed product. [S]

### PayPal
- **Principles.** In an August 2024 reply to the US Treasury, five principles: Privacy, Security, Fairness, Transparency, Explainability. [F, press release] The FY2026 proxy words them differently: data and privacy, security and resilience, fairness, explainability and reliability, accountability and transparency. [S]
- **Governance.** An "enterprise risk management approach to AI" [F]. Filings describe an AI Governance Charter, an AI Governance Executive Council (cross-functional, quarterly, reporting to the ERM Committee) and working groups. The FY2024 report used "Responsible AI Steering Committee". [S] A read of the FY2026 proxy itself found no AI governance section in the text returned, so the governance detail rests on the search summary.
- **Distinctive.** Fraud and AML/CTF use of AI is stated in the submission. [F] The Cosmos.AI platform blog cites training-data governance, explainable AI and human-in-the-loop review. [S] The PayPal developer blog on recourse (appeals, manual review) is general guidance and not stated policy. [S]

### Stripe
- **Principles.** No public AI principles or responsible AI page found. [S]
- **Governance.** Not published.
- **Distinctive.** Trust is expressed through infrastructure. The Agentic Commerce Protocol was co-developed with OpenAI. Shared Payment Tokens can be limited to a seller, time and amount, and carry Radar risk signals that help tell high-intent agents from bots. [S] Stripe describes foundation-model fraud detection that can explain why a charge looks risky. [S] The "38% less fraud" figure comes from a partner (PwC) press release and is not independent. [S]

### Block (Square, Cash App, Afterpay)
- **Principles.** No formal responsible AI principles page found. [S]
- **Governance.** The open-source agent goose was contributed to the Agentic AI Foundation (Linux Foundation) in December 2025, with governance reportedly moving in 2026. [S] This is governance of a tool, not of Block's AI use.
- **Distinctive.** Product pages describe Moneybot (Cash App) and Managerbot (Square), where sellers review and approve proposed actions. Human approval is the nearest thing to a stated design principle. [S]

### Klarna
- **Principles.** No official responsible AI principles found. [S] The annual report excerpts seen show no AI governance section. Klarna Bank AB is a Swedish licensed bank supervised by Finansinspektionen, and Klarna reports sharing input with the Swedish AI Commission. [S]
- **Governance.** Board, management team and an Audit, Compliance & Risk Committee (general structure, not AI-specific). [S]
- **Distinctive.** The public position was shaped by events. After the 2024 claim that its assistant did the work of 700 agents, the CEO said in May 2025 that cost had been too dominant and quality suffered, and Klarna rehired human agents. Its stated position is that a customer can always reach a human. [S] Klarna says callers are told when they are speaking to an AI voice clone. [S] Headcount-equivalence figures are company-reported.

### Revolut
- **Principles.** No public AI principles found. [S]
- **Governance.** Not found.
- **Distinctive.** Public statements centre on AI scam detection for card payments (February 2024): decline, an in-app intervention and access to a human fraud specialist. The head of fraud describes proportionality (no blanket blocks). A reported 30% fall in card-scam losses on investment scams is company-reported. [S] Figures about the Sherlock system come from a secondary source. [S]

### Wise
- **Principles.** No public AI principles or governance disclosure found. [S] The only Wise item found is a March 2026 outlook on how business customers will use agentic AI. [S]
- **Governance.** Not found. The annual report was not read.

### Monzo
- **Principles.** No standalone principles document found. [S]
- **Governance.** In the FCA's AI Live Testing programme (first cohort) Monzo tested a savings assistant. Its blog [F] describes assurance across the whole system: ownership, monitoring, change review and testing before release, and escalation, continuing as models and data change. It pairs generative AI explanations with "predictable, auditable systems" for follow-on actions. It flags hidden assumptions, overconfidence and over-reliance as risks beyond factual errors, and keeps a narrow scope to make good outcomes definable.
- **Distinctive.** Favours an "outcomes-based, principles-led approach" to regulation, combining clear outcomes with practical evidence and controls. [F] The FCA says AI has no dedicated Senior Manager function and falls under existing SM&CR. [S] Monzo received a GBP 21m FCA fine for financial-crime controls, which is not AI-specific. [S]

### N26
- **Principles.** No published AI principles found. [S]
- **Governance.** Not found.
- **Distinctive.** Public material is technical: machine-learning fraud detection with a 500 ms decision window and an 80% fraud reduction in 2023 (from an AWS case study, company-reported), and ML-based identity verification via Fourthline. [S] BaFin's guidance (January 2026, under DORA) requires an inventory of AI systems including "shadow AI" and places ultimate responsibility on management. [S]

### Nubank
- **Principles.** No standalone responsible AI document found. Statements are scattered: data protection and "the best AI ethics practices" in credit, and in HR "clear ethical boundaries", bias monitoring and refining governance frameworks. [S]
- **Governance.** Not detailed.
- **Distinctive.** AI agents are described as elevating human staff, not replacing them. Nubank says it prefers autonomy and judgment to a rigid rulebook. [S]

### Adyen
- **Principles.** No standalone responsible AI principles found. The cultural tenets in its AI article are long-term thinking, control and flexibility, and curiosity. [F]
- **Governance.** No formal framework in the article [F]. A job posting for Senior AI Governance Counsel shows a programme in build: an AI inventory, risk classification, proportionate risk-tiered "green paths", fairness, bias and red-team testing, human-oversight protocols, and partners in Risk, Security, Compliance and Engineering. [S]
- **Distinctive.** All GenAI workflows are "designed for Human in the Loop". Open-source models are hosted and fine-tuned in-house for privacy and security. Fraud models are tree-based ensembles with merchant-set rules, and new models are promoted only after A/B/n testing. [F] Adyen joined the Agentic AI Foundation in April 2026. [S] Merchant-control principles for agentic payments (verifiable intent, merchant control, data ownership) come from a third-party analysis. [S]

### Ant Group
- **Principles.** ESG page: legal compliance, transparency, value-driven action, and safeguards for data security and privacy. It does not set out AI ethics principles. [S] A ChinAI profile says Ant's Tiansuan Lab bases trustworthy AI on privacy protection, robustness, interpretability and fairness. [S]
- **Governance.** Ant International's 2025 report describes a Risk Management Committee mechanism from corporate to unit level. [S] A newsletter reports that nearly 20% of large-model technical staff work on ethics issues. [S] Committee structure not found.
- **Distinctive.** The 2025 sustainability report reportedly cites an Agentic Commerce Trust Protocol for China. [S] Chinese national AI principles apply in the background.

### Grab
- **Principles.** The November 2024 article [F] says a working group reviewed OECD, UNESCO, WEF, Singapore, EU, Australia, Japan and China frameworks and proposed principles "aligned across Grab". The principles appear only in an image, so their names were not read.
- **Governance.** An AI risk framework, with each risk type mapped to an existing risk function. An interdisciplinary AI governance task force (integrity, data governance, cybersecurity, legal, privacy, communications) assesses AI features before launch. Training uses workshops and quizzes. The stated next step is governance rules embedded in the development lifecycle with real-time monitoring. [F]
- **Distinctive.** Over 1,000 AI/ML models deployed. No detail on fraud, credit or data use in the article. [F]

### Kaspi
- **Principles.** No public AI ethics principles or responsible AI policy found. [S] Nothing in the search results mentions Kaspi. The relevant local context is Kazakhstan's Law "On Artificial Intelligence" (signed November 2025, in force January 2026). Its seven principles are legality, fairness and equality, transparency and explainability, accountability, protection of human welfare and autonomy, data confidentiality and security, with a risk-based regime. [S]

### Intuit
- **Principles.** Six, read on the company page [F]: Powering prosperity; Enhancing human talent; Fairness; Accountability; Transparency; Privacy and security.
- **Governance.** An AI Governance Committee gives executive-level oversight (senior leaders from data, legal, technology, communications, cybersecurity and people). There is a structured internal review, employee training and forums, and public feedback through the Intuit Integrity Line. [F] Responsible AI training is reportedly the first step in its GenStudio development environment. [S] Partner on AI membership and NIST CAISI membership are reported. [S]
- **Distinctive.** Explainability is tied to customer-facing features (Credit Karma Approval Odds, QuickBooks Capital decisions, TurboTax ExplainWhy). [F] The stated fairness aim covers people historically excluded from financial services. [F]

### Affirm
- **Principles.** No Affirm responsible AI or fair lending statement found; the search returned only general material. [S] The relevant external constraint is US adverse-action rules. A CFPB circular reported for May 2026 says complex models do not excuse specific, accurate adverse-action reasons. [S]

### Upstart (fair lending)
- **Principles.** No principles list found. Fairness is shown through supervision and testing. [S]
- **Governance.** CFPB no-action letters (2017, replaced December 2020) required a model risk and compliance plan, group-level adverse impact and accuracy testing, less-discriminatory-alternative research and reporting to the CFPB. Upstart asked the CFPB to end the letter in 2022, and the CFPB noted it "has never endorsed Upstart's model". A voluntary independent fair lending monitorship by Relman Colfax ran 2020 to 2024, and results are shared with lending partners. [S]
- **Distinctive.** Bank partners are consumers of the fairness evidence. Approval and APR uplift claims are company-reported. [S]

### Zest AI (credit-model vendor)
- **Principles.** No single principles document found. Stated positions: models optimised for accuracy and fairness, less-discriminatory-alternative searches, adversarial debiasing, multi-variate explainability, ongoing monitoring. These appear in policy comments to OMB and the CFPB and in House testimony. [S]
- **Distinctive.** Argues "fair enough" is not the standard. A critic argues the transparency mainly serves lenders and borrowers get vague denial reasons. [S] Performance claims are company-reported.

### Plaid (data aggregator)
- **Principles.** No AI principles found. Consent principles (September 2025 blog): transparency, data minimisation and enforcement of approved data types. [S] Its privacy policy allows use of aggregated or de-identified data for lawful purposes, which is the clause to read for AI training questions. [S]

### Coinbase
- **Principles.** No responsible AI policy found. [S]
- **Governance.** The x402 protocol is overseen by an x402 Foundation launched with Cloudflare (2025). [S]
- **Distinctive.** Control by limits. Agentic Wallets (February 2026) have session caps, per-transaction limits and readable audit trails. [S] Public policy material frames agentic commerce as an opportunity for regulators. [S]

## Common themes
- Principle sets are short (five or six items) and very similar: privacy and security, fairness, transparency or explainability, accountability. Only Intuit and Mastercard publish named sets on their own pages, and PayPal names its set in a regulator submission.
- Many fintechs publish no principles at all (Stripe, Block, Revolut, Wise, N26, Kaspi, Affirm, Coinbase, Klarna, Visa in the sources found). The absence may reflect the search, not the company.
- Human in the loop is the most common concrete claim: Adyen, Block, Klarna, Revolut, Nubank, Monzo, PayPal.
- Explainability is tied to specific customer decisions such as credit and adverse action, not to abstract principles.
- Fraud, scam and AML use is presented as a benefit of AI, not as a risk to govern.
- Governance bodies are cross-functional councils or task forces (Mastercard, PayPal, Intuit, Grab), sometimes with an AI inventory or registry.

## How fintech positioning differs from banks
Comparison is drawn from the sources above and general knowledge, not from a bank sample gathered here.
- **Speed.** Fintechs use lighter, product-led statements and engineering blog posts. Adyen's "green paths" and Grab's embedded lifecycle governance aim to keep governance from slowing teams. Nubank explicitly prefers autonomy over a rigid rulebook.
- **Partner-bank and regulator dependence.** Many fintechs reach customers through licensed partners or are supervised as payment institutions. Their assurance is shaped by others: Upstart shares fairness results with lending partners, Zest and Upstart engage regulators directly, and Plaid's obligations run through consent and developer policy. Licensed banks (Klarna Bank AB, N26, Monzo) sit under supervisory expectations such as BaFin and the FCA.
- **Customer-facing agents.** Chat assistants are launched openly and then corrected in public (Klarna). Monzo tests its assistant in a regulator sandbox. Position statements centre on human escalation and disclosure of AI.
- **Agentic commerce.** This is where payments companies are most specific, and their answer is technical: scoped tokens, agent identity and registration, signed requests, spending caps and audit trails (Mastercard, Visa, Stripe, Coinbase, Adyen). Principles become protocol design.
- **Consent.** Consent is treated as a control on the transaction (per-agent, per-merchant, per-amount) and as data-sharing permission (Plaid, Visa), not as a general AI principle.
- **Consumer trust gap.** Reported surveys show low consumer comfort with autonomous purchasing (about 10% for Mastercard research, 47% for a Salesforce figure quoted with Visa). [S]

## Governance patterns
1. **Central council plus working groups** (PayPal, Mastercard, Intuit), reporting into enterprise risk.
2. **Risk-tiered intake with an AI inventory or registry** (Mastercard, Adyen, aligned with BaFin's inventory expectation).
3. **Task force reviewing features before launch** (Grab).
4. **Regulator-facing assurance** (Monzo with the FCA; Upstart with the CFPB and an independent monitor).
5. **Fairness evidence shared with partners** (Upstart, Zest).
6. **Training as a gate** (Intuit's GenStudio, Grab workshops).
7. **Governance by protocol and foundation** (x402 Foundation, Agentic AI Foundation, Trusted Agent Protocol).
8. **Accountability under existing regimes.** The FCA adds no AI-specific senior manager role. BaFin puts ultimate responsibility on management.

## Sources
Fetched and read [F]:
- [Intuit Responsible AI Principles](https://www.intuit.com/privacy/responsible-ai/)
- [PayPal response to US Treasury (press release, 13 Aug 2024)](https://newsroom.paypal-corp.com/2024-08-13-PayPal-Responds-To-US-Department-Of-The-Treasury-On-AI-In-The-Financial-Sector)
- [Grab: how Grab set up a framework for ethical AI use (Nov 2024)](https://www.grab.com/inside-grab/stories/harnessing-ai-for-public-good-grabs-approach-to-ai-governance/)
- [Monzo: Helping people save with AI, FCA live testing insights](https://monzo.com/blog/fca-ai-live-testing-insights)
- [Adyen: how Adyen uses AI](https://www.adyen.com/knowledge-hub/how-adyen-does-ai)
- [Credo AI case study: Mastercard](https://www.credo.ai/casestudies/mastercard)
- [PayPal FY2026 proxy (SEC)](https://www.sec.gov/Archives/edgar/data/1633917/000119312526145721/d59508ddef14a.htm), partial text only

Read only through search summaries [S], pages listed for follow-up:
- [Mastercard privacy and data responsibility](https://www.mastercard.com/us/en/for-the-world/about-us/mastercard-privacy-and-data-responsibility.html) (403 on fetch)
- [Mastercard responsible AI perspective, 2023](https://www.mastercard.com/news/perspectives/2023/driving-responsible-ai-how-to-set-the-rules-of-the-road/) (403 on fetch)
- [Mastercard agentic token framework](https://www.mastercard.com/global/en/news-and-trends/stories/2025/agentic-commerce-framework.html)
- [Mastercard Verifiable Intent](https://www.mastercard.com/us/en/news-and-trends/stories/2026/verifiable-intent.html)
- [Visa Intelligent Commerce](https://www.visa.com/en-us/solutions/intelligent-commerce)
- [Visa: trust is the ultimate currency](https://corporate.visa.com/en/sites/visa-perspectives/security-trust/trust-is-ultimate-currency.html)
- [Visa Trusted Agent Protocol](https://corporate.visa.com/en/sites/visa-perspectives/newsroom/visa-unveils-trusted-agent-protocol-for-ai-commerce.html)
- [PayPal responsible business practices](https://about.pypl.com/how-we-work/responsible-business-practices/default.aspx)
- [PayPal developer blog: building responsible AI](https://developer.paypal.com/community/blog/building-responsible-ai/)
- [Stripe agentic commerce solutions](https://stripe.com/blog/introducing-our-agentic-commerce-solutions)
- [Block AI](https://block.xyz/ai)
- [Revolut AI scam feature](https://www.revolut.com/en-US/news/revolut_launches_ai_feature_to_protect_customers_from_card_scams_and_break_the_scammers_spell/)
- [Intuit AI governance page](https://www.intuit.com/privacy/responsible-ai/governance/) (429 on fetch)
- [FCA: AI and the FCA, our approach](https://www.fca.org.uk/firms/innovation/ai-approach)
- [N26 blog on AI in payments](https://n26.com/en-eu/blog/the-role-of-ai-in-payments-and-financial-markets)
- [BaFin AI and ICT risk guidance summary](https://www.bakertilly.de/en/post/ict-risks-when-using-ai-new-bafin-guidance)
- [Nubank governance](https://international.nubank.com.br/governance/)
- [Nubank: building AI agents for 131 million customers](https://building.nubank.com/building-ai-agents-for-131-million-customers/)
- [Adyen: Senior AI Governance Counsel posting](https://careers.adyen.com/vacancies/8107347-senior-ai-governance-counsel)
- [Adyen joins the Agentic AI Foundation](https://www.adyen.com/knowledge-hub/adyen-joins-agentic-ai-foundation)
- [Ant Group ESG: openness and trustworthiness](https://www.antgroup.com/en/esg/eco)
- [ChinAI #204: Ant and trustworthy AI](https://chinai.substack.com/p/chinai-204-ant-gets-antsy-about-trustworthy)
- [EY Kazakhstan: Law on Artificial Intelligence](https://www.ey.com/en_kz/technical/tax-alerts/2025/12/law-on-artificial-intelligence-kazakhstan)
- [Zest AI comments to OMB](https://www.zest.ai/learn/blog/zest-ai-comments-on-the-federal-guidance-for-regulating-ai/)
- [CFPB no-action letter to Upstart (2020)](https://files.consumerfinance.gov/f/documents/cfpb_upstart-network-inc_no-action-letter_2020-11.pdf)
- [Relman Colfax monitorship report on Upstart](https://www.relmanlaw.com/media/cases/1088_Upstart%20Initial%20Report%20-%20Final.pdf)
- [Plaid: permissioned data access](https://plaid.com/blog/open-finance-trust-security/)
- [Coinbase Institute: crypto and agentic commerce](https://www.coinbase.com/public-policy/advocacy/documents/crypto-and-agentic-commerce)
- [Klarna Bank AB annual report 2024](https://s205.q4cdn.com/644747736/files/doc_financials/2024/q4/2024-KBAB-Annual-Report-ENG.pdf)
- [CX Dive: Klarna rehires humans](https://www.customerexperiencedive.com/news/klarna-reinvests-human-talent-customer-service-AI-chatbot/747586/)

## Confidence and gaps
- **Higher confidence.** Intuit (six principles and governance, page read), PayPal five principles (press release read), Grab governance shape, Monzo assurance approach, Adyen practices.
- **Medium.** Mastercard principle names and council (several consistent search summaries, primary page blocked; vendor case study did not confirm council or start year). PayPal governance bodies (proxy text not obtained).
- **Low or absent.** Visa, Stripe, Block, Klarna, Revolut, Wise, N26, Kaspi, Affirm, Plaid, Coinbase: no formal principles found, and this is the finding as far as the searches went. Company annual reports, sustainability reports and trust pages for Wise, Revolut, N26, Klarna, Kaspi and Affirm were not read.
- **Not read.** Grab's principle names (image only), Nubank, Ant and Upstart primary pages, Zest's own site, Mastercard's official pages.
- **Company-reported figures** (fraud reductions, agent-equivalent headcount, approval uplift, Radar effect) are unaudited and some come from vendors or partners.
- **Dates.** Several items are dated 2026 in search results (Coinbase, Mastercard, Visa, Klarna, CFPB circular, BaFin) and were not verified beyond the summaries.
- **Bank comparison.** The bank contrast is a working view and should be checked against the companion bank research.
