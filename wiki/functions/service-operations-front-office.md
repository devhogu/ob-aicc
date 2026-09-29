# Service, Operations and Front Office: Generative and Agentic AI in Banking

Scope: (A) customer support and contact centers, (B) banking operations, (C) customer-facing front office (retail, SME, corporate). Research date: 2026-09-29. Figures are marked **[self-reported]** (bank or its AI vendor partner), **[vendor]** (technology vendor marketing), **[academic]**, **[analyst]** or **[regulator]**.

## Why it matters

- Service and operations are where banks report the first measurable results. The strongest independent evidence is on agent assist: a peer-reviewed study of 5,179 support agents found about 14% more issues resolved per hour, and 34% for novice agents, with little change for experienced agents [academic].
- Fully autonomous customer-facing bots carry the most risk. Klarna's assistant handled two-thirds of chats in month one, but its CEO later said cost had been too dominant a factor and quality fell. CBA reversed 45 job cuts after its voice-bot did not cut call volumes as claimed. A regulator (CFPB) and a tribunal ruling (Air Canada) put liability on the institution, not the bot.
- For O!Bank, language is a specific constraint. Kyrgyz is low-resource, spoken Kyrgyz differs from written Kyrgyz, and Kyrgyz-Russian code-switching is common. FINCA Bank Kyrgyzstan reports it had to train its own speech models to get a usable Kyrgyz voice bot, so O!Bank should not assume off-the-shelf language quality.
- Front-office copilots for relationship managers and advisors are the main path to revenue effects, but public evidence is thinner and mostly vendor or consultancy claims. Named bank evidence is mostly time saved on preparation and follow-up, not proven revenue uplift.

## Use cases

| Use case | What AI does | Maturity | Example bank or source |
|---|---|---|---|
| **A. Customer support and contact centers** | | | |
| Agent assist (real-time) | Transcribes calls, retrieves knowledge base answers, suggests replies, summarises, pre-fills service request fields | Proven | Brynjolfsson et al. [academic]; DBS CSO Assistant (projected up to 20% shorter handling time [self-reported]; measured savings so far reported in seconds per call by a secondary source only); Nubank copilot (over 45% of agents use key features [self-reported]) |
| Internal knowledge assistant for frontline staff | Answers staff questions from approved internal articles | Proven | Lloyds Athena: time to find information 59s to 20s, 20,000 colleagues [self-reported] |
| Text chat assistant, tier-1 | Answers routine questions, escalates to human after limits | Proven for routine; emerging for complex | Nubank AI Assistant on GPT-4o: 55% of tier-1 inquiries resolved, 2M+ chats a month [self-reported via OpenAI]; Klarna: two-thirds of chats in month one [self-reported], later partly reversed |
| Transactional virtual assistant in the app | Balance, spending insight, payments, guided navigation | Proven (mostly non-generative) | Bank of America Erica: 3B+ interactions since 2018, 58M+ a month [self-reported] |
| Voice bot / IVR replacement | Speech recognition, intent detection, spoken answers, hand-off to human | Emerging | FINCA Bank Kyrgyzstan Kyrgyz voice bot in production, no metrics published; CBA voice-bot call-volume claim disputed by union |
| 100% conversation QA and coaching | Scores every call or chat against a scorecard, flags compliance issues, supports coaching | Emerging (bank-named evidence is weak) | Vendor material only found (NiCE, Level AI, CallMiner); a UK vendor survey claims 46.7% of 285 FCA-regulated contact centres review every call with AI [vendor] |
| Complaints triage and drafting | Classifies complaints, flags vulnerability, summarises, drafts responses for human sign-off | Emerging | NatWest piloting agentic AI for complaints (reported Dec 2025 via trade press); PwC UK guidance |
| Multilingual support incl. low-resource languages | ASR/TTS and LLM fine-tuning for Kyrgyz, Uzbek, Kazakh; Russian-Kyrgyz code-switching | Experimental to emerging | FINCA Kyrgyz voice bot; TBC Uzbekistan and Aiphoria on-premise fine-tuning of open models; ISSAI KAZ-LLM (Kazakh, Russian, English, Turkish) |
| Scam and fraud conversation support | Alerts, name and caller checks, agentic detection of new patterns | Emerging | CBA: reports 50% lower customer scam losses and 30% fewer customer-reported frauds [self-reported] |
| **B. Banking operations** | | | |
| Document intake and extraction | Reads, classifies and extracts data from unstructured documents, drafts case notes | Proven for extraction; emerging for LLM reasoning | JPMorgan COiN and LLM Suite (hours-saved figures come from secondary analyses; unverified) |
| Disputes and chargebacks | Assembles case file, validates documents, drafts merchant and customer correspondence, recommends action to agent | Emerging | HCLTech European bank case: human oversees every AI decision in pilot [vendor]; Sutherland: 60% less manual effort, 40% faster [vendor, mostly ML/RPA]; Backbase 70-80% straight-through claim [vendor] |
| Payment exceptions and investigations (ISO 20022 E&I) | Parses investigation messages, creates cases, proposes resolution, routes | Experimental | Vendor material only (Validata, Backbase); no named bank result found |
| Reconciliation | Matches records, classifies breaks, proposes matches for review | Emerging | Vendor demos only; no named bank result found |
| Trade finance document checking | Reads LC and presentation documents, checks against UCP 600 rules and LC conditions, flags discrepancies | Emerging | HSBC Smart Checking announced 28 Sep 2026 (human-in-the-loop, over a million presentations a year [self-reported]); Microsoft, ANZ, HSBC, Lloyds proof of concept |
| KYC and credit memo workflows | Multi-agent drafting with QA agent and full audit trail | Emerging | McKinsey describes one unnamed global bank's KYC "agentic AI factory"; productivity multipliers quoted on vendor blogs are unverified |
| Back-office workflow automation | Handles requests such as payment deferrals, account maintenance, status queries | Proven (RPA plus conversational) | OTP Bank via Druid: 3x requests with same team, 10 minutes to 20 seconds [vendor] |
| **C. Customer-facing front office** | | | |
| Advisor/RM meeting prep, notes, follow-up | Consolidates client context, transcribes meetings with consent, drafts email and CRM entry | Proven in wealth; emerging in SME/corporate | Morgan Stanley: 98% of advisor teams use Assistant [self-reported]; Debrief notes to Salesforce; BofA/Merrill Meeting Journey, up to 4 hours saved per meeting [self-reported] |
| RM copilot and next-best-action for SME/corporate | Surfaces product gaps, covenant or utilisation alerts, prioritised leads, drafts outreach | Emerging | McKinsey reports 3-15% higher revenue per RM and 20-40% lower cost to serve for banks that rewire a frontline domain [analyst, could not re-verify the page]; vendor claims (Backbase, Iguazio) not independent |
| SME credit decision support | Drafts credit memos, extracts financials, assists analyst | Experimental to emerging | CNCB (Hong Kong) sandbox trial of AI Approver Assistant; Bankwell pilot (Census working paper) |
| Agentic customer-facing assistant for a B2B channel | Multi-agent assistant compares products, quotes financing, books appointments | Emerging | Capital One Chat Concierge on auto dealer sites (built on Llama); one dealer reports 10-15% more sales [self-reported, single anecdote] |
| Personalised financial assistant | Conversational spending insights and guidance | Emerging | Lloyds AI financial assistant, planned for 21M+ accounts in 2026 [self-reported] |
| Marketing personalisation and content | Generates variants, segments, timing | Emerging | No named bank result with credible metrics found in this research |
| Branch staff support | Same knowledge assistants and meeting tools used at counter | Proven (knowledge); emerging (sales) | Lloyds Athena covers branches and call centers |

## Target state for O!Bank

"Fully adopted" means:

- **Contact center:** every agent has a copilot (live transcript, knowledge answers, summary, pre-filled request). Russian and Kyrgyz are supported at measured quality. A tier-1 assistant in app and messaging handles routine, low-risk intents and hands over with full context. Every conversation is scored for quality and compliance, and QA staff review the flagged ones. Complaints are triaged and drafted by AI; humans decide.
- **Operations:** document-heavy queues (disputes, trade documents, account maintenance, KYC files) run as AI-prepared cases. Humans approve exceptions and anything that moves money or gives a customer a final decision. Each AI step leaves an audit trail.
- **Front office:** every RM, SME banker and branch employee gets a client brief before meetings and a drafted summary and CRM entry afterward. Prioritised next-best-action suggestions come from O!Bank's own data. Marketing uses consent-aware personalisation.
- **Common:** one governed platform (models, retrieval, guardrails, logging, evaluation). One escalation rule everywhere: a customer can always reach a human. Evaluations are run per language and per product.

## Phased adoption path

**Foundation**
- Choose 3-5 use cases where a human stays in the loop: agent assist, internal knowledge assistant, call and chat summarisation, meeting notes for RMs, document extraction for one ops queue.
- Clean and version the knowledge base (products, tariffs, procedures) in Russian and Kyrgyz; assign an owner for content.
- Build a Russian/Kyrgyz evaluation set from real calls and chats (anonymised). Benchmark ASR and LLM quality before buying.
- Set up baseline metrics (handling time, first-contact resolution, QA scores, RM prep time) before any pilot.
- Agree policy on customer consent for recording and AI notes, data residency, and vendor model use.

**Scale**
- Roll agent assist to all agents; add 100% QA scoring and complaints triage with human sign-off.
- Launch a tier-1 chat assistant limited to a defined intent list, with visible human hand-off.
- Move disputes and one or two other operations queues to AI-prepared cases.
- Give RMs and branch staff a copilot integrated with CRM; start next-best-action on a narrow product set.
- Pilot a Kyrgyz voice bot on a small set of inbound intents, with fallback to an agent.

**Platform**
- Consolidate to a shared AI platform: retrieval over approved content, guardrails, prompt and model versioning, central logging, automated regression evaluation.
- Expose core actions (block card, dispute status, statement, limit change) as governed tools/APIs that assistants can call under customer authentication.
- Standardise metrics, incident process and model risk review across use cases.

**Agentic**
- Allow agents to execute bounded, reversible actions (create case, gather evidence, draft and queue response, book appointment) with defined authority limits and human approval above thresholds.
- Multi-agent workflows with a QA agent for KYC files, credit memos, trade document checks and investigations, each with audit trail.
- Proactive outreach and next-best-action executed by agents inside marketing consent and conduct rules.
- Prepare for customers' own AI agents contacting the bank (Gartner flags this as a coming traffic source).
- Entry gate: measured error rates, working rollback, and regulator-facing explainability for each autonomous action.

## Data and system prerequisites

- **Knowledge:** current, owned, versioned product and procedure content in Russian and Kyrgyz; retrieval must cite its source article.
- **Conversation data:** recorded calls and chat logs with consent basis, retention rules and anonymisation for training and evaluation.
- **Speech stack:** ASR and TTS that handle Kyrgyz, Russian and mixed speech, tested on telephony audio. Evidence suggests generic services are often insufficient and fine-tuning on the bank's own scenarios was needed (FINCA). Consider on-premise or in-country deployment for open models (TBC Uzbekistan approach).
- **Core and channel integration:** APIs from core banking, cards, payments and CRM for customer context and actions; single customer identity across channels; authentication before any account-level answer.
- **Contact-center platform:** telephony and CRM that expose transcripts, events and case fields to the assistant; case management with a clean disposition taxonomy.
- **Operations data:** structured case records for disputes, exceptions and trade files with outcome labels; document repositories with access control.
- **Front office:** a CRM with reliable client, product-holding and interaction data; consent flags for marketing and meeting recording.
- **AI platform:** model gateway, logging of prompts, retrieved passages and outputs, evaluation harness, cost monitoring, human feedback capture.

## Risks and controls

| Risk | Control |
|---|---|
| Wrong or invented answers (product, fees, rights). Liability sits with the bank: Air Canada was held liable for its chatbot's misstatement (BC tribunal, 2024); the CFPB warns wrong information can cause fees, default or wrong product choice | Answer only from approved retrieval sources with citation; refuse when unsupported; regression tests on top intents; legal review of high-risk topics (fees, rates, complaints, disputes) |
| "Doom loops" and blocked access to humans (CFPB 2023) | Visible one-step hand-off; escalate after failed attempts or on complaint or distress signals; measure hand-off failures |
| Hard-to-service customers, weaker language quality | Per-language evaluation; Kyrgyz and mixed-language test sets; do not launch bot channels where quality is below agent-assist baseline |
| Over-claiming savings and cutting staff too early (Klarna reversal, CBA reversal) | Start with assist, not replacement; report resolution and repeat-contact rates, not only containment; keep human capacity while measuring |
| Privacy, recording consent and data leakage | Consent flows for AI notes; PII masking; data residency; vendor terms on training; access control on retrieval |
| Prompt injection, impersonation, chatbot phishing | Authenticate before account data; limit tool permissions; input filtering; red-team before launch |
| Agent actions that move money or change accounts | Bounded authority, thresholds, human approval, reversibility, full audit log |
| Decision and conduct risk in complaints and SME credit | AI drafts, human decides; bias testing; explainable rationale; sample review |
| Automation bias and de-skilling of staff | Show sources; track override rates; keep coaching |
| Model or vendor change breaks behavior | Versioned prompts, pinned models, automated regression suite, exit plan |
| Regulatory uncertainty | No specific NBKR rule on banks' use of AI was found. NBKR has a 2026-2031 SupTech roadmap covering its own use of AI. Check the Russian-language NBKR site and confirm with Compliance; design to consumer-protection principles that regulators elsewhere (CFPB, FCA) already apply |

## Metrics

Track against a pre-pilot baseline and a control group where possible.

- **Contact center:** average handling time; first-contact resolution; repeat contact within 7 days; containment plus resolution (not containment alone); hand-off rate and hand-off success; CSAT/NPS by channel and language; QA score and QA coverage; agent adoption and suggestion acceptance rate; new-agent ramp time; complaint volume and time to resolution.
- **Language:** word error rate for Russian, Kyrgyz and mixed speech; intent accuracy by language; answer groundedness rate.
- **Operations:** cases per FTE; straight-through rate; time per dispute or exception; rework and error rate; SLA and regulatory deadline breaches; audit findings.
- **Front office:** RM time in client dialogue; prep and follow-up time; CRM data completeness; next-best-action acceptance and conversion; revenue per RM; SME onboarding and credit turnaround.
- **Control:** hallucination or wrong-answer rate from sampled review; escalations for AI error; privacy incidents; cost per interaction and platform cost.

## Sources

Regulators and academic
- [CFPB, Chatbots in consumer finance (June 2023)](https://www.consumerfinance.gov/data-research/research-reports/chatbots-in-consumer-finance/chatbots-in-consumer-finance/)
- [Brynjolfsson, Li, Raymond, Generative AI at Work, NBER w31161](https://www.nber.org/papers/w31161)
- [Moffatt v. Air Canada, 2024 BCCRT 149 (commentary, ABA)](https://www.americanbar.org/groups/business_law/resources/business-law-today/2024-february/bc-tribunal-confirms-companies-remain-liable-information-provided-ai-chatbot/)
- [NBKR SupTech roadmap coverage (Akchabar)](https://www.akchabar.kg/en/news/natsbank-vnedrit-tekhnologii-ii-i-bolshikh-dannikh-dlya-nadzora-za-bankami-rqyiydsudaburyyn)
- [WilmerHale, AI and the UK FCA (April 2026)](https://www.wilmerhale.com/en/insights/client-alerts/20260429-ai-and-the-uk-financial-conduct-authority)
- [PwC UK, Scaling customer-facing AI and Consumer Duty](https://www.pwc.co.uk/industries/financial-services/understanding-regulatory-developments/scaling-customer-facing-ai-unlocking-better-outcomes-and-consumer-duty-compliance.html)

Analysts and consultancies
- [McKinsey, The economic potential of generative AI](https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/the-economic-potential-of-generative-ai-the-next-productivity-frontier)
- [McKinsey, Gen AI in customer care: early successes and challenges](https://www.mckinsey.com/capabilities/operations/our-insights/gen-ai-in-customer-care-early-successes-and-challenges)
- [McKinsey, Agentic AI is here. Is your bank's frontline team ready?](https://www.mckinsey.com/industries/financial-services/our-insights/agentic-ai-is-here-is-your-banks-frontline-team-ready)
- [McKinsey, The paradigm shift: how agentic AI is redefining banking operations](https://www.mckinsey.com/capabilities/operations/our-insights/the-paradigm-shift-how-agentic-ai-is-redefining-banking-operations)
- [McKinsey, How agentic AI can change the way banks fight financial crime](https://www.mckinsey.com/capabilities/risk-and-resilience/our-insights/how-agentic-ai-can-change-the-way-banks-fight-financial-crime)
- [Gartner, agentic AI to resolve 80% of common service issues by 2029 (prediction, March 2025)](https://www.gartner.com/en/newsroom/press-releases/2025-03-05-gartner-predicts-agentic-ai-will-autonomously-resolve-80-percent-of-common-customer-service-issues-without-human-intervention-by-20290)

Bank and company disclosures
- [Bank of America, Erica passes 3 billion interactions (Aug 2025)](https://newsroom.bankofamerica.com/content/newsroom/press-releases/2025/08/a-decade-of-ai-innovation--bofa-s-virtual-assistant-erica-surpas.html)
- [Bank of America, Merrill and Private Bank AI-Powered Meeting Journey (Mar 2026)](https://newsroom.bankofamerica.com/content/newsroom/press-releases/2026/03/merrill-and-bank-of-america-private-bank-launch-ai-powered-meeti.html)
- [Klarna press release, AI assistant first month (Feb 2024)](https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/)
- [OpenAI, Klarna case study](https://openai.com/index/klarna/)
- [CX Dive, Klarna rehires humans (May 2025)](https://www.customerexperiencedive.com/news/klarna-reinvests-human-talent-customer-service-AI-chatbot/747586/)
- [OpenAI, Nubank case study](https://openai.com/index/nubank/)
- [DBS newsroom, CSO Assistant](https://www.dbs.com/newsroom/DBS_empowers_its_Customer_Service_Officers_with_Gen_AI_powered_virtual_assistant_to_reduce_toil_and_enhance_customer_experience)
- [Computer Weekly, DBS AI assistant](https://www.computerweekly.com/news/366622932/CW-Innovation-Awards-DBS-AI-assistant-slashes-call-times-and-boosts-productivity)
- [ABC News, CBA reverses AI job cuts (Aug 2025)](https://www.abc.net.au/news/2025-08-21/cba-backtracks-on-ai-job-cuts-as-chatbot-lifts-call-volumes/105679492)
- [Bloomberg, CBA AI cuts scam losses (Nov 2024)](https://www.bloomberg.com/news/articles/2024-11-28/ai-cuts-scam-losses-speeds-up-home-loans-at-top-australia-bank)
- [FINCA Bank Kyrgyzstan, Kyrgyz-language voice AI bot](https://fincabank.kg/en/news-en/how-finca-bank-created-its-first-kyrgyz-language-voice-ai-bot/)
- [Aiphoria, open-source LLMs for banking in Uzbekistan](https://aiphoria.ai/blog/when-languages-lack-data-making-open-source-llms-work-for-banking-in-uzbekistan)
- [ISSAI KAZ-LLM](https://issai.nu.edu.kz/kazllm/)
- [Lloyds Banking Group, Athena](https://www.lloydsbankinggroup.com/media/press-releases/2025/lloyds-banking-group-2025/lloyds-accelerates-with-athena.html)
- [FStech, Lloyds AI value 2025 and 2026 target](https://www.fstech.co.uk/fst/Lloyds_Banking_Group_Targets_100m_AI_Value.php)
- [Morgan Stanley, AI @ Morgan Stanley Debrief](https://www.morganstanley.com/press-releases/ai-at-morgan-stanley-debrief-launch)
- [Capital One Chat Concierge (The Financial Brand)](https://thefinancialbrand.com/news/banking-products/capital-ones-chat-concierge-puts-agentic-ai-on-car-dealers-websites-187128)
- [HSBC Smart Checking (IT Digest)](https://itdigest.com/fintech/hsbc-advances-digital-trade-with-new-document-checking-solution/)
- [Microsoft, trade finance AI proof of concept with ANZ, HSBC, Lloyds](https://www.microsoft.com/en-us/microsoft-cloud/blog/financial-services/2026/04/20/reimagining-trade-finance-with-ai-a-collaborative-proof-of-concept-from-microsoft-anz-hsbc-and-lloyds/)
- [CNCB Hong Kong, GenAI SME credit approver use case](https://www.cncbinternational.com/_document/sme/aigen/en/GenAI-use-case-summary.pdf)

Vendor material (claims not independent)
- [HCLTech, chargeback automation](https://www.hcltech.com/case-study/reimagining-financial-workflows-with-ai-driven-chargeback-automation)
- [Sutherland, credit card dispute case](https://www.sutherlandglobal.com/insights/case-study/leading-bank-achieving-reduction-in-manual-effort-and-cost-savings)
- [Backbase, AI banking dispute resolution](https://www.backbase.com/blog/ai-banking-dispute-resolution-automation)
- [Backbase, RM productivity in commercial banking](https://www.backbase.com/blog/how-ai-is-transforming-relationship-manager-productivity-in-commercial-banking)
- [Druid AI, agentic AI use cases in banking (OTP Bank)](https://www.druidai.com/blog/7-use-cases-for-agentic-ai-in-banking)
- [Validata, ISO 20022 exceptions with agentic AI](https://www.validata-software.com/blog/transforming-iso-20022-payment-exceptions-investigations-with-agentic-ai/)
- [MaxContact, speech analytics use cases](https://www.maxcontact.com/articles/10-speech-analytics-use-cases-to-transform-your-contact-centre)

## Confidence and gaps

- **Highest confidence:** agent-assist productivity (peer-reviewed, one large firm, not a bank, and English-language support), CFPB risk findings, the Air Canada ruling (small tribunal claim, widely cited), and the Klarna and CBA reversals (reported by Bloomberg and ABC).
- **Self-reported, not independently audited:** Erica volumes, Nubank resolution rates (from an OpenAI case study; the write-up gives two slightly different figures, 55% and "up to 50%"), Klarna's first-month figures (700-agent equivalence is a modelled number), DBS (20% was a projection at launch; measured seconds-per-call came from a secondary site), CBA scam-loss and wait-time results, Lloyds time-to-answer and value figures, Morgan Stanley adoption (share of advisor teams, not individuals), BofA "up to four hours per meeting", Capital One dealer result (one dealer).
- **Not re-verified:** the McKinsey frontline figures (3-15% revenue per RM, 20-40% lower cost to serve) came from a search summary of the article; the page fetch timed out. Verify before citing externally. Statistics attributed to McKinsey on vendor blogs (credit memo gains, KYC multipliers, 15-20% cost reduction) were not found in McKinsey pages and are omitted from the tables.
- **Vendor claims:** all figures for disputes, reconciliation, payment exceptions, QA at 100% coverage, SME RM copilots and OTP Bank are vendor or vendor-hosted case studies. No named-bank, independently reported results were found for payment exceptions or reconciliation.
- **Not found:** credible personalisation or marketing metrics (no ING or Lloyds NBA results surfaced); a BCG banking report matching the brief; any Kyrgyz-language quantitative benchmark for banking (FINCA published no metrics; a Kyrgyz LLM benchmark was mentioned in search results but not opened); any NBKR rule on banks' AI use.
- **Recent items to re-check:** HSBC Smart Checking (announced the day before this research), the FINCA article (dated August 2026), Lloyds 2026 plans, and the CBA agentic fraud system (April 2026) were taken from search results and are not fully verified.
- **Transferability:** most named cases are from large banks in the US, UK, Australia, Brazil or Singapore with far more data, scale and language resources than O!Bank. Treat their percentages as directional.
