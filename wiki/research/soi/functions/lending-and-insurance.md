# Lending and Insurance: Generative and Agentic AI at O!Bank

Scope: (A) retail, SME and corporate/B2B lending across the full loan lifecycle; (B) insurance sold by or inside the bank (bancassurance). Research date: 2026-09-29. Figures are marked as reported by the source; none are O!Bank results.

## Why it matters

- Lending is the bank's core risk-taking activity and is document-heavy. Drafting, spreading, monitoring and servicing consume analyst and relationship-manager time, and this is where generative AI has the clearest early evidence. McKinsey's 2024 survey of 44 institutions (with IACPM) found executives saw most potential in early-warning systems, credit memo drafting and customer engagement, while adoption was uneven and concentrated in larger banks.
- Credit decisions carry legal duties: explainable reasons, non-discrimination, human review of automated decisions. AI that touches a decision needs controls built in at the start, not added later.
- Bancassurance is a fee and retention lever, but digital channels convert worse than branches. BCG reports insurance cross-sell in digital channels was up to 50% lower than in branches for some clients, and that contextual, in-flow offers lift conversion (consultancy examples, not audited).
- Kyrgyz context: the market has two credit bureaus (KIB Ishenim, KIB SES). Since 1 Nov 2025 citizens can self-ban loans via the Tunduk portal, and lenders must check the ban before issuing. Any origination automation must include this check.

## Use cases

Maturity key: proven = live at scale at named institutions or long-established; emerging = live at some institutions or in regulated pilots, evidence is company-reported; experimental = pilots, vendor claims, or no primary evidence found.

### A. Lending

| Use case | What AI does | Maturity | Example bank or source |
|---|---|---|---|
| Document intake and data extraction (loan agreements, financials, collateral valuations) | Classifies and extracts fields from unstructured documents; flags exceptions for humans | Proven (OCR/IDP); LLM extraction emerging | JPMorgan COiN contract analysis (reported by an LTM blog, secondary); EY case study of a global commercial bank using AI for commercial loan document review ([EY](https://www.ey.com/en_us/insights/banking-capital-markets/case-study-ai-powered-commercial-loan-document-review)) |
| Credit memo / credit write-up drafting | Pulls data from internal and external sources, drafts sections, computes ratios, scores its own confidence, suggests follow-up questions; analyst reviews | Emerging | HSBC states it uses gen AI for credit analysis write-ups, no figure published ([HSBC](https://www.hsbc.com/who-we-are/hsbc-and-digital/hsbc-and-ai/transforming-hsbc-with-ai)); McKinsey retail-bank proof of concept: 20-60% productivity gain, 30% faster credit turnaround (potential, not production; [McKinsey](https://www.mckinsey.com/capabilities/quantumblack/our-insights/seizing-the-agentic-ai-advantage)) |
| Credit analysis of financials (spreading, ratio analysis, business-model risk) | Multi-agent drafting of financial-risk assessments for corporate clients | Emerging | Deutsche Bank CRO interview: financial analysis and business-model risk among first applications, humans kept in the loop ([McKinsey](https://www.mckinsey.com/capabilities/risk-and-resilience/our-insights/the-future-is-agentic-ais-role-in-the-end-to-end-corporate-credit-process)) |
| SME underwriting support | Assistant supports approvers with data and analysis instead of static, manual, heuristic review | Experimental | China CITIC Bank International "AI Approver Assistant", trial completed in the HKMA GenA.I. Sandbox, Oct 2025; results not visible in the document retrieved ([CNCBI](https://www.cncbinternational.com/_document/sme/aigen/en/GenAI-use-case-summary.pdf)) |
| Automated scoring / decisioning for retail and SME | Classic ML scoring with explainability layer; gen AI is not the decision engine | Proven (ML); gen AI as decider is not recommended | CFPB adverse-action guidance applies to any model (see Risks) |
| Covenant monitoring | Reads compliance certificates and financials, tests covenants, raises exceptions | Emerging (mostly vendor products) | Moody's Lending Suite describes AI-assisted covenant testing (vendor claim; [Moody's](https://www.moodys.com/web/en/us/solutions/lending/loan-monitoring.html)) |
| Early-warning and portfolio monitoring | LLMs read news, disclosures and borrower communications to add signals to structured triggers; summarises portfolio changes for RMs | Emerging | McKinsey/IACPM survey ranks early warning as a top-potential area; Newgen and others sell agents (vendor claims; [Newgen](https://newgensoft.com/solutions/industries/financial-institutions/ai-agents-early-warning-system/)) |
| RM assistance (meeting prep, client emails, application alerts) | Drafts meeting materials and client communications | Proven for drafting | Bank of America says drafting meeting materials could save "tens of thousands of hours" a year in commercial banking ([American Banker](https://www.americanbanker.com/news/bank-of-america-jpmorganchase-execs-report-returns-on-ai)); McKinsey example of an agent alerting an RM to a new application |
| Loan servicing (customer questions on loans, mortgages, overdrafts; agent assist) | Conversational assistant; live-call knowledge retrieval and call summaries | Proven for assistants | NatWest Cora+ (secondary source: [Banking Dive](https://www.bankingdive.com/news/lloyds-natwest-truist-evident-insights-ai-artificial-intelligence/750398/)); Lloyds reports about GBP 50m gen AI value in 2025 across 50+ use cases (secondary); HSBC gen AI assistant for corporate servicing teams, 3 million client interactions a year (HSBC page) |
| Collections: inbound payment-status and promise-to-pay | Voice/chat agent handles constrained journeys (payment link, status, promise to pay), hands off complex cases | Emerging | Almost entirely vendor material (Haptik, Moveo, Kompato); no bank primary source found. Treat recovery-uplift claims as unverified |
| Collections: hardship, disputes, vulnerable customers | Detects vulnerability signals and routes to trained staff; AI supports agent, does not decide treatment | Experimental for AI-led; assist is emerging | UK FCA Consumer Duty expectations (secondary summary: [Grant Thornton](https://www.grantthornton.co.uk/insights/debt-collection-at-a-crossroads-ai-and-the-race-for-efficiency/), [BCLP](https://www.bclplaw.com/en-US/events-insights-news/ai-regulation-in-financial-services-turning-principles-into-practice.html)) |
| Regulatory-reporting and case-narrative analysis (adjacent) | Reads case narratives and documents at full coverage | Emerging | HKMA GenA.I. Sandbox first cohort: banks reported 30-80% less preparation time for suspicious transaction reports and memo processing cut from a day to minutes (secondary: [Fintech Hong Kong](https://fintechnews.hk/36534/ai/hkma-genai-sandbox-report/); primary is the HKMA report) |

### B. Bancassurance and insurance

| Use case | What AI does | Maturity | Example bank or source |
|---|---|---|---|
| Sales support: in-app advisor, contextual offers, RM co-pilot | Explains cover in plain language, triggers offers at moments such as loan disbursement, prepares RM meeting briefs with coverage gaps | Emerging | BCG bancassurance work: real-time digital offers raised conversion five-fold at an Asian bank and four-fold with pre-quote offers at a European bank (consultancy examples, unnamed banks; [BCG](https://www.bcg.com/publications/2024/benefits-of-bancassurance)) |
| Underwriting support (submission intake, triage, document summary) | Digitises submissions, extracts risk data, summarises, surfaces guideline conflicts; underwriter decides | Emerging to proven (commercial lines) | Zurich: UK commercial underwriting workbench and Cytora intake; reported manual triage time cut from 75 to 15 minutes and intake straight-through processing from 10% to 95% (company/vendor news via [Reinsurance News](https://www.reinsurancene.ws/zurich-insurance-scales-cytora-ai-platform-across-global-underwriting-operations/); not independently audited) |
| Simple-product underwriting (term life, credit life, health questionnaires) | Adaptive question flow, medical triage | Experimental | Datamatics multi-agent case, "80% faster" is a vendor claim ([Datamatics](https://www.datamatics.com/resources/case-studies/agentic-ai-powered-digital-underwriting)) |
| Claims intake and triage | Extracts first-notice-of-loss data, checks coverage, flags urgent or suspicious cases | Emerging | Allianz Project Nemo: seven agents (planner, cyber, coverage, weather, fraud, payout, audit) on Australian food-spoilage claims under AUD 500; live July 2025, built in under 100 days; Allianz reports 80% less processing and settlement time; payout decisions are never automated, a claims professional reviews ([Allianz](https://www.allianz.com/en/mediacenter/news/articles/251103-when-the-storm-clears-so-should-the-claim-queue.html)) |
| Claims handling at scale | AI across first notification to settlement | Emerging | Aviva (McKinsey "Rewired in action" write-up, [link](https://www.mckinsey.com/capabilities/tech-and-ai/how-we-help-clients/rewired-in-action/aviva-rewiring-the-insurance-claims-journey-with-ai)); figures seen only in secondary roundups, not used here |
| Fraud detection | ML anomaly detection plus rules; increasingly forensic checks on AI-altered photos and documents | Proven (ML); gen-AI-specific defence emerging | AXA five-year Shift Technology renewal across 15 countries ([Insurance Business](https://insurancebusinessmag.com/nz/news/breaking-news/axa-scales-governed-ai-infrastructure-across-global-operations-589001.aspx)); AI-doctored evidence is a rising fraud vector, prevalence figures are vendor-sourced |
| Servicing (policy questions, renewals, endorsements) | RAG assistant grounded on policy documents; escalation to human | Proven for grounded assistants | Vendor guidance (Infobip, Digiqt); no named-bank result verified |

## Target state for O!Bank

"Fully adopted" means:

- One governed credit workbench for retail, SME and corporate. Documents are ingested once, extracted with confidence scores, and reused across origination, memo, monitoring and review. Analysts review exceptions and low-confidence items instead of retyping.
- Credit decisions stay with an explainable, validated scoring or policy engine plus a human approver where required. Generative AI drafts, summarises, retrieves and monitors. It does not issue approvals or declines by itself.
- Every customer-facing decline or adverse term can be given with accurate, specific reasons, in Kyrgyz and Russian, traceable to the factors actually used. Applicants can ask for human review.
- Portfolio monitoring runs continuously: covenant tests, financial-statement triggers and external signals feed one early-warning queue with reasons attached. RMs get drafted actions, not raw alerts.
- Collections uses AI for right-party contact, payment journeys and agent assist under strict scripts. Hardship, vulnerability, dispute and legal cases route to trained staff. Contact rules are enforced in code.
- Bancassurance offers appear in the loan and account journey (for example after a loan is disbursed), are grounded on insurer-approved product text, and pass suitability and disclosure checks. Claims intake and triage are handled with the partner insurer; the insurer keeps underwriting and claims decisions.
- A model and use-case inventory, monitoring, and audit logs cover all of the above, with regulator-ready evidence.

## Phased adoption path

**Foundation**
- Build inventory, risk-tiering and approval rules for AI use cases. Define which outputs may never be automated (declines, pricing, claim denials, collections escalation).
- Start with internal, human-reviewed uses: document extraction with human check, RM meeting and email drafting, credit-policy and product Q&A for staff, call summaries.
- Fix data foundations: document store, loan and payment data, bureau feeds (KIB Ishenim, KIB SES), self-ban check.
- Establish golden test sets and reviewer sign-off measures before any pilot.

**Scale**
- Credit memo and financial-spreading drafts for SME and corporate, with confidence scores and analyst edit tracking.
- Covenant tracking and early-warning summaries for the corporate book; signal precision reviewed monthly.
- Loan-servicing assistant in the app and contact centre, grounded on product documents; agent assist in collections.
- Bancassurance: RM co-pilot and in-app, insurer-approved explainers; claims FNOL intake support with the partner insurer.

**Platform**
- Shared services: document AI, retrieval over policy and product content, evaluation harness, guardrails, logging, prompt and model registry. Reuse across lending and insurance.
- Explainability service that maps model factors to reason codes for adverse-action style notices.
- Policy-as-code for contact frequency, hours, vulnerability routing and consent.
- Integrated monitoring: override rates, drift, complaint linkage.

**Agentic**
- Multi-agent workflows for narrow, bounded tasks, following patterns such as Allianz Nemo (coverage, fraud, payout and audit agents, human sign-off): pre-fill and pre-check applications, run full memo packs, run monitoring loops that draft RM actions, and handle simple claims triage.
- Enter only after audit trails, least-privilege tool access, and kill-switches are proven. Autonomy limited to low-value, reversible steps. Approve, decline, pay and legal actions stay human.
- McKinsey's position is that value at this stage needs redesigned workflows, not agents bolted onto old ones; plan process redesign with the business owner.

## Data and system prerequisites

- Loan origination and servicing system with APIs to read application, exposure, repayment and delinquency data.
- Document management with consistent metadata; scanned and photographed documents in Kyrgyz and Russian (extraction quality in these languages must be tested, no source evaluated it).
- Financial statement data: standardised spreading templates for SME and corporate, with audited versus management accounts distinguished.
- Bureau and registry integration; self-ban check via the state portal; internal customer data with consent basis for use.
- Collateral and covenant registers as structured data, not only in PDFs.
- For collections: contact history, consent and channel preferences, vulnerability flags, complaint records.
- For bancassurance: partner insurer product, price and eligibility APIs; policy documents as approved knowledge base; claims system interface and identity link between bank customer and policy.
- Platform: access control, PII redaction before model calls, private or contractually protected model hosting, prompt and output logging, evaluation datasets, model registry.
- Local regulatory basis: NBKR requirements for lenders and the personal data law. This research did not find NBKR rules specific to automated credit decisions or the applicability of the personal data law to scoring; legal counsel must confirm.

## Risks and controls

| Risk | Control |
|---|---|
| Unexplainable or inaccurate decline reasons. Under US ECOA/Regulation B, creditors must give specific reasons reflecting factors actually considered, and complexity is not a defence (CFPB Circulars 2022-03 and 2023-03) | Keep the decision on a model whose reasons can be derived; do not let an LLM invent reasons. Map factors to reason codes and test them. Use as a benchmark even though US law does not apply directly |
| Automated decisions without human recourse. GDPR Art. 22 gives a right to human intervention and contestation; the CJEU (Dec 2023) held credit scoring can fall under Art. 22 | Offer human review on adverse decisions; log overrides; design for contestability, not disclosure alone |
| EU AI Act treats creditworthiness scoring of natural persons and life/health insurance risk assessment and pricing as high-risk (Annex III point 5), with obligations on risk management, data governance, logging, transparency, human oversight. Fraud detection is carved out of the credit point | Not binding in Kyrgyzstan, but it is the clearest reference standard; use it as a design baseline. Application dates were unclear in sources (see gaps) |
| Fair lending and proxy discrimination (bias, proxies in alternative data) | Bias testing before and after launch, by segment; restrict alternative data to justified, documented features; independent validation |
| Hallucination in memos and monitoring summaries | Ground on retrieved source documents; show citations and confidence; analyst must accept each section; sample audits |
| Model risk for LLMs. US agencies' April 2026 revised model risk guidance (SR 26-2 / OCC 2026-13) reportedly places gen AI outside formal scope but expects governance through broader risk frameworks (from secondary sources) | Apply model-risk practices anyway: use-case documentation, known limits, vendor evidence, change monitoring, revalidation triggers |
| Third-party and concentration risk (foundation model vendor; insurer partner). NAIC model bulletin makes insurers responsible for vendors, with audit rights | Contractual audit and data terms, exit plan, data residency review |
| Collections conduct: harassment, wrong-party contact, vulnerable customers, contact frequency. FCA Consumer Duty expects evidence of good outcomes and special care for vulnerable customers | Deterministic contact rules; vulnerability detection with immediate human handoff; one narrow agent per journey, not a universal agent; record why treatment was chosen; supervisor review of transcripts |
| Bancassurance mis-selling and unsuitable advice from a chat assistant | Restrict to insurer-approved content; disclosures and consent captured; no personalised recommendation without suitability questions; human path; conduct testing of scripts |
| Claims and underwriting decisions denied by AI. IAIS (July 2025) and NAIC stress governance, fairness testing, and human oversight | Claims denial and underwriting declines by qualified staff only; AI supports; complaint handling covers AI-assisted decisions |
| Fraud with AI-altered documents and media, and deepfake applicants | Metadata and image forensics, liveness checks, escalation to fraud unit; test in sandbox-style adversarial drills (HKMA second cohort is doing this) |
| Data leakage and privacy | PII redaction, private hosting, logging, role-based access, retention limits |
| Automation bias: reviewers rubber-stamp AI output | Track edit and override rates; sample blind reviews; keep reviewers accountable |

Where humans must stay in the loop:

- Credit approval, decline, pricing, restructuring, write-off.
- Any adverse action notice content and its review.
- Collections treatment for hardship, dispute, vulnerable, deceased, legal and complaint cases.
- Insurance underwriting declines, claim denials and payouts (Allianz keeps payout decisions human).
- Exception handling and any low-confidence output.
- Model changes, prompt changes and threshold changes affecting decisions.

## Metrics

Track against a pre-AI baseline measured before pilot.

Lending:
- Cycle time from application to decision (by segment); credit memo prep time; touches per application.
- Extraction accuracy and exception rate; analyst edit rate on drafted memos; confidence-score calibration.
- Decision quality: approval rate, early delinquency, loss rate versus baseline; override rates (both directions).
- Early warning: precision and lead time of flags before delinquency; false-alert rate; time from alert to action.
- Covenant breach detection time.
- Collections: right-party contact, promise-to-pay kept rate, roll rates, cost to collect, complaint rate, share of cases escalated to humans, vulnerability-flag handling time.
- Servicing: containment with satisfactory outcome, repeat contact, handling time.
- Fairness: outcome and error-rate differences across segments.

Insurance:
- Offer-to-quote and quote-to-bind conversion in bank channels; attach rate per loan disbursed.
- Complaint and cancellation rate on bank-sold policies (mis-selling signal).
- Claims intake time, straight-through rate for simple claims, reopen and dispute rate, leakage, fraud referral precision.
- Partner insurer SLA and audit findings.

Governance:
- Share of use cases in inventory with completed risk tiering and validation; incidents; time to detect drift; audit-finding closure.

## Sources

- McKinsey, [Seizing the agentic AI advantage](https://www.mckinsey.com/capabilities/quantumblack/our-insights/seizing-the-agentic-ai-advantage) (credit memo proof of concept; read via search summary, page fetch timed out)
- McKinsey, [The future is agentic: AI's role in the end-to-end corporate credit process](https://www.mckinsey.com/capabilities/risk-and-resilience/our-insights/the-future-is-agentic-ais-role-in-the-end-to-end-corporate-credit-process) (Deutsche Bank CRO; search summary)
- McKinsey/IACPM, [Banking on gen AI in the credit business](https://www.mckinsey.com/capabilities/risk-and-resilience/our-insights/banking-on-gen-ai-in-the-credit-business-the-route-to-value-creation) (survey of 44 institutions; search summary)
- McKinsey, [Embracing generative AI in credit risk](https://www.mckinsey.com/capabilities/risk-and-resilience/our-insights/embracing-generative-ai-in-credit-risk)
- HSBC, [Transforming HSBC with AI](https://www.hsbc.com/who-we-are/hsbc-and-digital/hsbc-and-ai/transforming-hsbc-with-ai)
- China CITIC Bank International, [AI Approver Assistant summary](https://www.cncbinternational.com/_document/sme/aigen/en/GenAI-use-case-summary.pdf)
- HKMA, [GenA.I. Sandbox second cohort press release](https://www.hkma.gov.hk/eng/news-and-media/press-releases/2025/10/20251015-4/) and [Responsible Innovation with GenA.I. in the Banking Industry](https://brdr.hkma.gov.hk/eng/doc-ldg/docId/getPdf/20251031-6-EN/20251031-6-EN.pdf) (PDF text not extractable; figures via secondary)
- American Banker, [Bank of America, JPMorganChase execs report returns on AI](https://www.americanbanker.com/news/bank-of-america-jpmorganchase-execs-report-returns-on-ai)
- Banking Dive, [How 3 banks are capitalizing on AI](https://www.bankingdive.com/news/lloyds-natwest-truist-evident-insights-ai-artificial-intelligence/750398/)
- EY, [AI-powered commercial loan document review](https://www.ey.com/en_us/insights/banking-capital-markets/case-study-ai-powered-commercial-loan-document-review)
- CFPB, [Providing adverse action notices when using AI/ML models](https://www.consumerfinance.gov/about-us/blog/innovation-spotlight-providing-adverse-action-notices-when-using-ai-ml-models/) (2020, archived note points to Circular 2022-03); Circulars 2022-03 and 2023-03 via law-firm summaries: [Skadden](https://www.skadden.com/insights/publications/2024/01/cfpb-applies-adverse-action-notification-requirement), [Venable](https://www.venable.com/insights/publications/2023/09/cfpb-weighs-in-on-credit-denials-by-lenders)
- EU AI Act, [Annex III](https://artificialintelligenceact.eu/annex/3/) and [Commission AI Act Service Desk](https://ai-act-service-desk.ec.europa.eu/en/ai-act/annex-3)
- EBA, [Guidelines on loan origination and monitoring](https://www.eba.europa.eu/activities/single-rulebook/regulatory-activities/credit-risk/guidelines-loan-origination-and-monitoring)
- BIS FSI, [How regulators can address AI explainability](https://www.bis.org/fsi/fsipapers24.pdf)
- Hunton, [CJEU: GDPR automated decision-making prohibition applies to credit scoring](https://www.hunton.com/privacy-and-cybersecurity-law-blog/cjeu-rules-that-gdpr-prohibition-on-automated-decision-making-applies-to-credit-scoring)
- US model risk guidance, [SR 11-7](https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm) and the April 2026 revision (SR 26-2, per secondary sources: [Seekr](https://www.seekr.com/resource/model-risk-management-generative-ai-sr-11-7/))
- IAIS, [Application Paper on the supervision of AI](https://www.iais.org/uploads/2025/07/Application-Paper-on-the-supervision-of-artificial-intelligence.pdf) (July 2025)
- NAIC, [Model Bulletin: Use of AI Systems by Insurers](https://content.naic.org/sites/default/files/inline-files/2023-12-4%20Model%20Bulletin_Adopted_0.pdf)
- Allianz, [Project Nemo](https://www.allianz.com/en/mediacenter/news/articles/251103-when-the-storm-clears-so-should-the-claim-queue.html)
- Zurich, [AI at Zurich](https://www.zurich.com/about-us/ai-at-zurich); [Reinsurance News on Cytora](https://www.reinsurancene.ws/zurich-insurance-scales-cytora-ai-platform-across-global-underwriting-operations/)
- Aviva, [McKinsey Rewired in action](https://www.mckinsey.com/capabilities/tech-and-ai/how-we-help-clients/rewired-in-action/aviva-rewiring-the-insurance-claims-journey-with-ai)
- AXA, [Insurance Business](https://insurancebusinessmag.com/nz/news/breaking-news/axa-scales-governed-ai-infrastructure-across-global-operations-589001.aspx)
- BCG, [Unlocking the Benefits of Bancassurance](https://www.bcg.com/publications/2024/benefits-of-bancassurance) and [Steps for scaling AI-powered bancassurance](https://www.bcg.com/publications/2023/steps-for-scaling-ai-powered-bancassurance)
- Collections and conduct: [Grant Thornton](https://www.grantthornton.co.uk/insights/debt-collection-at-a-crossroads-ai-and-the-race-for-efficiency/), [BCLP](https://www.bclplaw.com/en-US/events-insights-news/ai-regulation-in-financial-services-turning-principles-into-practice.html), [IDAI](https://www.imayandigital.com/perspectives/ai-voice-agents-for-regulated-collections)
- Kyrgyzstan: [NBKR credit risk](https://www.nbkr.kg/contout.jsp?item=105&lang=ENG&material=108536), [IFC credit infrastructure case study](https://www.ifc.org/content/dam/ifc/doclink/2024/reforming-credit-infrastructure-kyrgyz-republic-en.pdf), [self-ban on loans (Kabar)](https://en.kabar.kg/news/citizens-of-kyrgyzstan-can-impose-self-ban-on-taking-loans/), [NBKR SupTech concept (open.kg)](https://open.kg/en/news/economy/122684-postanovleniem-pravlenija-nacbanka-kyrgyzstana-utverzhdena-koncepcija-i-dorozhnaja-karta-razvitija-nadzornyh-tehnologij-suptech-na-20262031-gody.html)
- Vendor material (claims not verified): [Newgen](https://newgensoft.com/solutions/industries/financial-institutions/ai-agents-early-warning-system/), [Moody's](https://www.moodys.com/web/en/us/solutions/lending/loan-monitoring.html), [Datamatics](https://www.datamatics.com/resources/case-studies/agentic-ai-powered-digital-underwriting)

## Confidence and gaps

- Strongest evidence: Allianz Nemo (company primary, narrow claim type), HSBC statement (primary, no numbers), regulator texts on explainability and governance (CFPB, EU Annex III, IAIS, NAIC).
- Self-reported or vendor figures: McKinsey credit memo gains (proof of concept, potential); Zurich and Cytora intake numbers (company/vendor news, not audited); HKMA cohort figures (participant-reported, read via secondary); Lloyds and NatWest numbers (secondary); all collections recovery uplifts (vendor blogs); Datamatics "80% faster"; BCG conversion multiples (unnamed banks).
- Several primary pages could not be read in full: McKinsey pages timed out (summaries via search), the CNCBI and HKMA PDFs were not text-extractable. Details from them are limited to what search summaries stated.
- No named-bank primary source found for: LLM covenant monitoring, LLM early warning, bank collections voice agents, and bancassurance gen AI with a named bank and insurer. These rows rely on vendor or consultancy material. Nothing found on Kyrgyz, Kazakh or Central Asian bank gen AI in lending.
- Unconfirmed regulatory points: EU AI Act application date for Annex III (sources conflicted, 2026 vs 2027, possible delay); a reported 2026 CFPB circular (single source, not used); details of the April 2026 US model risk guidance (secondary sources only); CFPB posture has shifted over time, so confirm which circulars are current.
- Kyrgyz law: no NBKR rule on automated credit decisions or application of the personal data law to scoring was found. Legal review needed before deployment. The EU, US, UK and HK rules cited are reference standards, not binding on O!Bank.
- Not researched: Islamic or microfinance-specific rules, pricing and dynamic-limit models, and insurer-side regulation in Kyrgyzstan.
