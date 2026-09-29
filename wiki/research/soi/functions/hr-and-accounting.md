# HR and Accounting/Finance Operations: Generative and Agentic AI in Banks

Research date: 2026-09-29. Scope: how banks and comparable finance organisations use generative and agentic AI in (A) HR and (B) accounting and finance operations, with a short note on legal, procurement and admin.

## Why it matters

- These are internal, high-volume, document-heavy functions with no direct customer exposure. They are a lower-risk place to build AI skills, governance and platforms before customer-facing use.
- Large banks already give staff general LLM tools and are moving to agents. Examples: HSBC (LLM productivity tool and an "AI Academy"), Goldman Sachs (Claude-based agents for trade accounting and client onboarding, in development as of Feb 2026), BNY (100+ "digital employees").
- Deployment is not the same as value. Gartner reports that 88% of HR leaders say their organisations have not realised significant business value from AI tools, and that finance AI adoption levelled off in 2025 with realised value trailing expectations. Sequencing and measurement matter more than tool count.
- HR carries legal exposure that finance does not. Hiring and worker-management AI is a listed high-risk category in the EU AI Act, and a US court has let a class-style age-discrimination case proceed against a vendor of AI screening tools.

## Use cases

Maturity is the author's judgement from the evidence found. "Proven" means named-organisation production use is documented. "Emerging" means announced or limited production, or vendor-reported only. "Experimental" means pilots or thin evidence.

### A. HR

| Use case | What AI does | Maturity | Example bank or source |
|---|---|---|---|
| Employee HR helpdesk and policy Q&A | Answers policy, benefits, payroll and time-off questions with cited policy text and routes complex cases to HR staff | Proven | Bank of America "Erica for Employees" (launched 2020; 2023 expansion to benefits, payroll and tax forms; over 90% of employees use it, per the bank); Barclays "Colleague AI Agent" for HR queries (secondary source) |
| Enterprise knowledge search | Gen-AI search across internal documents for staff | Proven | DBS Enterprise Knowledge Base; HSBC group-wide LLM tool for document analysis and text help |
| AI literacy and upskilling | Mandatory prompt and responsible-AI training, adaptive learning paths, career matching | Proven | Citi mandatory prompt-training for about 175,000 staff (press reports of an internal memo); JPMorgan prompt-engineering training for new hires (press reports); HSBC mandatory responsible-AI training and AI Academy; DBS iGrow (AI/ML career matching, not specifically generative) |
| Recruiting: job descriptions, sourcing, candidate communication | Drafts job ads, summarises CVs, schedules interviews | Emerging | Gartner 2024 survey: 41% of HR leaders using or piloting gen-AI listed recruiting tasks. No named bank case with published results found |
| Candidate screening and ranking | Filters and scores applications | Emerging, high legal risk | No bank case found. Mobley v. Workday litigation and EU AI Act Annex III point 4 show the exposure |
| Onboarding assistant | Answers new-hire questions, prepares checklists, delivers training | Emerging | JPMorgan folds AI training into onboarding (press reports). No published bank onboarding-agent case found |
| Attrition analytics and workforce planning | Predicts leavers, models headcount and skills demand | Emerging (mostly classical ML, not gen-AI) | Academic work on bank employee data (arXiv 2209.07335 review); DBS reportedly uses predictive models for culture and turnover (secondary source). Standard Chartered links AI to planned cuts of more than 15% of back-office roles by 2030 (bank investor-day statements, press-reported) |
| Performance and behaviour monitoring, emotion analysis | Scores employees from behaviour or biometrics | Experimental, restricted | Emotion recognition in the workplace is prohibited under EU AI Act Art. 5(1)(f) (in force since Feb 2025) |
| HR agents (case handling, payroll queries, end-to-end tickets) | Resolves multi-step HR requests inside HRIS and ticketing | Emerging | Unnamed "global financial institution, 40,000+ employees" in a Kore.ai vendor case study (self-reported: 94% resolution, 83% ticket reduction; unverified) |

### B. Accounting and finance operations

| Use case | What AI does | Maturity | Example bank or source |
|---|---|---|---|
| Knowledge management for finance (policy, IFRS, procedures) | Answers finance-team questions from internal documents | Proven | Gartner finance survey 2025: 49% of finance AI users cited knowledge management as a use case (183 respondents; via Gartner summaries) |
| Invoice capture, coding and AP automation | Extracts fields from invoices, proposes GL coding, three-way match, routes exceptions | Proven for extraction; agentic exception handling emerging | Gartner: 37% of finance AI users cite AP automation. Deloitte Zora AI for Finance covers invoice and expense management (Deloitte press release; internal 25% cost and 40% productivity figures are self-reported) |
| Error and anomaly detection in ledgers | Flags misclassified or unusual entries | Proven (ML) / emerging (gen-AI) | Gartner: 34% of finance AI users. PwC GL.ai for GL and journal-entry review (secondary source). An unnamed large bank's month-end GL review (GSDC, unverified) |
| Reconciliations (nostro, intercompany, sub-ledger to GL) | Matches transactions, explains breaks, drafts break commentary | Emerging | Goldman Sachs testing agents on transaction reconciliation and trade accounting (CNBC and American Banker, Feb 2026, "early stages"). Vendor claims of large time savings are unverified |
| Payment and instruction validation, remediation | Agents validate payment data and clear exceptions | Emerging | BNY: digital employees validate payment instructions; bank reports under 30 seconds versus 5 to 6 minutes manually (Axios). Self-reported |
| Journal entries, accruals | Drafts standard and recurring entries for human approval | Emerging | IBM internal record-to-report with AI and RPA (company-reported: about 90% cycle-time cut; IBM is not a bank) |
| Financial close and management reporting | Automates close tasks, drafts variance commentary | Emerging | Gartner predicts embedded AI in cloud ERP will drive a 30% faster close by 2028 (prediction, not measurement). HPE and Deloitte expect a 50% cut in reporting production time (vendor expectation) |
| IFRS and disclosure drafting | Drafts narrative sections, checks disclosures against checklists | Emerging (narrative) / experimental (numbers and estimates) | FRC research (July 2026, via ICAEW): corporate reporting remains human-led; gen-AI useful in narrative reporting, limited in financial statements |
| Audit preparation | Assembles evidence, answers auditor requests, tests controls | Emerging | FRC guidance on generative and agentic AI in audit (Mar 2026) covers auditor-side use. Big Four tools: Deloitte Zora AI, PwC Agent OS and GL.ai, KPMG Workbench (last two via secondary sources) |
| Tax | Research, return preparation support, document extraction | Emerging | EY reports agents for tax professionals (secondary source; not verified) |
| Procurement, AR, collections | Contract and quote comparison, dunning drafts, dispute handling | Emerging | Gartner: data extraction, AP/AR automation and report creation generally return value in 9 to 10 months (Sept 2026 survey of 160 finance leaders) |

### Legal, procurement and admin (brief)

| Use case | What AI does | Maturity | Example bank or source |
|---|---|---|---|
| Commercial-loan contract review | Extracts clauses and attributes from agreements | Proven (ML extraction, pre-gen-AI) | JPMorgan COIN. The 360,000 hours per year is the bank's own estimate of prior manual workload (Bloomberg, 2017) |
| Credit and document write-ups | Drafts analysis from internal and external data | Proven | HSBC: gen-AI for credit analysis write-ups (bank website) |
| Contract lifecycle, vendor contract review | Summarises terms, flags deviations | Emerging | Mostly vendor content. No named bank case with results found |
| Admin agents (travel, expense, policy checks) | Books travel and checks policy by natural language | Emerging | Barclays Colleague AI Agent (secondary source) |

## Target state for O!Bank

"Fully adopted" means:

- One governed internal AI platform (approved models, retrieval over internal documents, logging, access control) serves both functions. HR and Finance do not buy separate stand-alone tools without AICC review.
- **HR:** A single employee assistant answers policy, benefits, payroll and leave questions in Russian, Kyrgyz and English from versioned HR policy, and hands over to HR staff with case context. Every employee has completed role-based AI literacy training. Recruiting AI supports drafting, scheduling and communication. Candidate ranking, if used at all, is advisory, tested for bias, documented, and always decided by a person. Workforce planning uses aggregated, explainable analytics. No emotion inference and no covert monitoring.
- **Finance:** Invoice intake, coding suggestions, three-way match and routine reconciliations run touchless within set tolerances. Exceptions arrive with a proposed resolution and evidence. Journal entries, accruals and variance commentary are drafted by AI and approved by a named preparer and reviewer. Close status, break ageing and audit-request responses are assembled from system data. IFRS and tax judgement stay with qualified staff.
- Agents act under their own identities with least-privilege access, complete audit trails, spend and value limits, and named human owners.
- Benefits are measured against a pre-AI baseline and reported to the AICC on a fixed cadence.

## Phased adoption path

**Foundation**
- Approve a staff-facing LLM with data-handling rules (what may and may not be entered). Publish an AI acceptable-use policy covering HR and finance data.
- Start AI literacy training for all staff, with deeper tracks for HR and Finance. Peer evidence: Citi, JPMorgan, HSBC.
- Build a read-only HR policy Q&A assistant and a finance policy/IFRS knowledge assistant over curated documents, with citations and human escalation.
- Inventory HR and finance data and systems. Classify AI use cases by risk. Mark any candidate-ranking or employee-evaluation use as high risk and require review before build.
- Set baselines (ticket volumes, invoice cycle time, close days, exception rates).

**Scale**
- HR: extend the assistant to personalised answers (leave balance, payslip explanations) via authenticated read access. Add job-description drafting, interview scheduling and onboarding checklists. Run bias and privacy assessment before any screening support.
- Finance: document extraction and GL coding suggestions for invoices, with human approval. Anomaly detection on journals. Reconciliation matching and break explanation for one or two high-volume accounts (for example nostro or card settlement). Draft variance commentary.
- Move from pilots to a run team with owners, a support model and a regression test set per use case.

**Platform**
- Shared services: document-intelligence pipeline, retrieval layer, prompt and evaluation library, model gateway, logging and monitoring, and an approval workflow for write-back.
- Integrate with HRIS, payroll, ERP/core-banking GL and the ticketing system through APIs, not screen scraping where avoidable.
- Standing model-risk and AI-governance review for each use case, with periodic re-validation.
- Selective write-back: post entries as drafts and park them for approval.

**Agentic**
- Agents own bounded end-to-end workflows: HR case resolution, invoice-to-pay exceptions, reconciliation break resolution, audit-request fulfilment, payment-instruction remediation. Peer signals: BNY digital employees, Goldman Sachs trade-accounting agents (early stage).
- Autonomy is tiered by value and risk. Only low-value, reversible actions run without approval. Every action is logged and attributable to an agent identity and a human owner.
- Adopt only after Scale metrics hold for a sustained period and audit and control owners have signed off. Include kill-switch and rollback.

## Data and system prerequisites

- **HR:** A current HRIS as system of record; a clean, versioned policy corpus (labour code, internal regulations, benefits) in the languages employees use; role-based access so the assistant sees only what the user may see; payroll data interfaces; job architecture and skills taxonomy for learning and workforce planning.
- **Finance:** A structured chart of accounts and cost-centre hierarchy; vendor master with data-quality controls; PO and goods-receipt data (or a defined non-PO process); digital invoices and contracts; API access to ERP/GL and core banking; bank-statement and settlement feeds; documented recurring entries and reconciliation rules; close calendar and task list.
- **Platform:** Identity and access management for people and agents; data classification; logging and retention; secure hosting decision for models handling employee and financial data; prompt and output evaluation tooling; a test set built from historical, human-resolved cases.
- **Legal and privacy (Kyrgyz Republic):** The Law "On Personal Information" (No. 58 of 2008, amended) governs employee and candidate data. The State Agency for Personal Data Protection oversees it, and holders of personal-data arrays must register them; security requirements come from Government Regulation No. 760 of 2017 (per DLA Piper and other summaries). Legal counsel must confirm cross-border transfer and localisation conditions for cloud or foreign-hosted models and the Labour Code rules on employee data. These were not confirmed in this research.
- Also check National Bank of the Kyrgyz Republic requirements on outsourcing, IT risk and model use. Not researched here.

## Risks and controls

| Risk | Control |
|---|---|
| Discriminatory or opaque hiring and promotion decisions. EU AI Act Annex III point 4 classes recruitment, selection, promotion, termination, task allocation and worker monitoring as high-risk. In Mobley v. Workday (N.D. Cal.), the court allowed claims that a vendor acted as the employer's "agent" and certified an age-discrimination collective in May 2025 (no merits ruling yet) | Human decision-maker for every employment decision. No fully automated rejection. Bias testing on outcomes by protected group where lawful and possible. Written explanation to candidates on request. Vendor contract terms on testing, logs and audit rights. Log overrides. Treat the EU Act as a benchmark: it applies only if O!Bank has EU-located activity or outputs used in the EU (confirm with counsel) |
| Prohibited practices: emotion recognition on employees | Ban emotion and biometric inference on staff and candidates in policy and vendor selection. Check vendor modules that are switched on by default (video interview tools, meeting analytics) |
| Employee and candidate personal data exposure (prompts, logs, vendor training) | Data-handling rules, no training on O!Bank data by vendors, role-based retrieval, retention limits, DPIA-style assessment, registration and consent per Kyrgyz law |
| Wrong policy or payroll answers (hallucination) | Answers only from cited policy text; show source and effective date; escalate when confidence is low or topic is sensitive (grievance, discipline, health); sample-audit answers monthly |
| Incorrect postings, misstated accounts, weak audit trail | AI proposes, humans approve; segregation of duties between preparer, approver and agent owner; reconciliation of AI output to source; immutable logs; materiality thresholds for autonomy; IFRS estimates and judgements stay human |
| Payment or vendor fraud through manipulated invoices or prompt injection | Vendor bank-detail change checks, duplicate detection, agent permissions limited to drafting, input sanitisation, red-team tests of document-borne instructions |
| Auditor and regulator acceptance | Involve external auditors early. The FRC guidance for auditors states that accountability stays with the human auditor and describes risks and mitigations for gen-AI and agentic tools. Prepare a model and use-case register, validation evidence and change control |
| Workforce anxiety and labour relations (StanChart has publicly tied AI to role reductions; others say headcount is unaffected) | State the workforce intent clearly, involve employee representatives, offer reskilling, and do not use "time saved" targets without a plan for the time (Gartner: only 7% of surveyed HR organisations gave guidance on time saved) |
| Vendor lock-in and third-party risk | Multi-model gateway, exit terms, data portability |
| Value shortfall | Baselines, benefit owners, stop criteria per use case. Prefer use cases Gartner reports as returning value in 9 to 10 months (extraction, AP/AR automation, report creation) |

## Metrics

**HR**
- Share of HR queries resolved without an HR agent; escalation rate; answer accuracy from sampled audits; employee satisfaction with HR service.
- Time-to-answer and HR ticket volume against baseline.
- AI training completion by role; active use of approved AI tools; self-reported and measured time saved.
- Time-to-hire and recruiter workload (recruiting), with selection-rate ratios by group for fairness monitoring.
- Voluntary attrition in critical roles and internal mobility rate (analytics use).
- Compliance: number of AI use cases risk-classified; open bias or privacy findings.

**Finance**
- Touchless invoice rate; extraction accuracy; exception rate and exception ageing; duplicate or fraudulent invoices caught.
- Cost per invoice and AP cycle time.
- Reconciliation auto-match rate; unmatched-item ageing; number and value of breaks.
- Days to close; number of manual journals; post-close adjustments; error rate in AI-drafted entries.
- Audit: time to fulfil auditor requests; number of control findings tied to AI use.
- Agent controls: percentage of agent actions with logged human approval where required; incidents and rollbacks.

**Programme**
- Realised benefit versus business case, tracked by named owner; adoption by team; cost per use case; model-risk review status.

## Sources

Bank and company primary or near-primary:
- [Bank of America newsroom: AI adoption by BofA's global workforce (Apr 2025)](https://newsroom.bankofamerica.com/content/newsroom/press-releases/2025/04/ai-adoption-by-bofa-s-global-workforce-improves-productivity--cl.html)
- [HSBC: Transforming HSBC with AI](https://www.hsbc.com/who-we-are/hsbc-and-digital/hsbc-and-ai/transforming-hsbc-with-ai)
- [DBS newsroom: Harvard Business School case on DBS AI strategy](https://www.dbs.com/newsroom/Harvard_Business_School_examines_DBS_AI_strategy_and_implementation_in_its_first_case_study_focusing_on_AI_in_an_Asian_bank)
- [Deloitte press release: Zora AI (Mar 2025)](https://www.prnewswire.com/news-releases/deloitte-unveils-zora-ai-agentic-ai-for-tomorrows-workforce-302404892.html)
- [CFO Dive: Deloitte and HPE AI agents for finance teams](https://www.cfodive.com/news/deloitte-hpe-team-up-to-offer-ai-agents-for-finance-teams/743011/)

Press coverage of bank programmes (not fetched in full unless noted):
- [CNBC: Goldman Sachs taps Anthropic's Claude to automate accounting, compliance (Feb 2026)](https://www.cnbc.com/2026/02/06/anthropic-goldman-sachs-ai-model-accounting.html) (site blocked direct fetch; content taken from search summary)
- [American Banker: Goldman equips AI agents to do trade accounting, onboarding](https://www.americanbanker.com/news/goldman-equips-ai-agents-do-trade-accounting-onboarding)
- [Axios: BNY has over 100 "digital employees" (Oct 2025)](https://www.axios.com/2025/10/17/ai-wall-street-digital-workers)
- [Microsoft customer story: BNY and Eliza](https://www.microsoft.com/en/customers/story/27322-bny-microsoft-365-copilot)
- [Banking Dive: Standard Chartered job cuts by 2030](https://www.bankingdive.com/news/standard-chartered-7800-job-cuts-ai-winters/820627/)
- [FStech: Standard Chartered to cut 7,800 roles](https://fstech.co.uk/fst/Standard_Chartered_To_Cut_7800_Roles.php)
- [Banking Dive: JPMorgan prompt-engineering training](https://www.bankingdive.com/news/jpmorgan-chase-ai-training-strategy-pinto-erdoes/717359/)
- [Fortune: Citi AI prompt training mandate (Oct 2025)](https://www.fortune.com/2025/10/01/citi-ai-prompt-training-mandate-employees-reskilling-workforce-business)
- [Emerj: AI at Barclays](https://emerj.com/artificial-intelligence-at-barclays/)
- [Bloomberg: JPMorgan COIN (2017)](https://www.bloomberg.com/news/articles/2017-02-28/jpmorgan-marshals-an-army-of-developers-to-automate-high-finance)
- [Fortune: banks lay groundwork for workforce cuts as AI takes hold (Jun 2026)](https://fortune.com/2026/06/07/banks-mass-workforce-cuts-ai-entry-level-jobs-junior-analysts/)

Analysts and professional bodies:
- [Gartner: Finance AI adoption remains steady in 2025 (Nov 2025)](https://www.gartner.com/en/newsroom/press-releases/2025-11-18-gartner-survey-shows-finance-ai-adoption-remains-steady-in-2025) (direct fetch blocked; figures from search summary)
- [Gartner: CFOs must take a more disciplined approach to finance AI investment (Sept 2026)](https://www.gartner.com/en/newsroom/press-releases/2026-09-24-gartner-says-cfos-must-take-a-more-disciplined-approach)
- [Gartner: Embedded AI in cloud ERP will drive 30% faster financial close by 2028 (Feb 2026)](https://www.gartner.com/en/newsroom/press-releases/2026-02-24-gartner-predicts-embedded-ai-in-cloud-erp-applications-will-drive-a-30-percent-faster-financial-close-by-2028)
- [Gartner: 38% of HR leaders piloting, planning or implementing gen-AI (Feb 2024)](https://www.gartner.com/en/newsroom/press-releases/2024-02-27-gartner-finds-38-percent-hr-leaders-piloting-generative-ai)
- [Gartner: 88% of HR leaders say no significant business value from AI tools (Oct 2025)](https://www.gartner.com/en/newsroom/press-releases/2025-10-28-gartner-survey-shows-88-percent-of-hr-leaders-say-their-organizations-have-not-realized-significant-business-value-from-ai-tools)
- [Gartner: AI in HR, separate hype from reality (Oct 2025)](https://www.gartner.com/en/newsroom/press-releases/2025-10-16-ai-in-hr-separate-hype-from-reality-to-achieve-business-goals)
- [McKinsey: AI in Asia, reimagining banking operations through agentic AI](https://www.mckinsey.com/capabilities/operations/our-insights/ai-in-asia-reimagining-banking-operations-through-agentic-ai) (page fetch timed out; only search-result description used)
- [FRC: AI in Audit guidance](https://www.frc.org.uk/library/standards-codes-policy/audit-assurance-and-ethics/guidance/ai-in-audit/)
- [ICAEW: How helpful is FRC's guidance on generative and agentic AI?](https://www.icaew.com/insights/viewpoints-on-the-news/2026/may-2026/how-helpful-is-frc-guidance-on-generative-and-agentic-ai)
- [ICAEW: What does client use of AI mean for the audit?](https://www.icaew.com/technical/audit-and-assurance/faculty-resources/audit-and-beyond/2026/what-does-client-use-of-ai-mean-for-the-audit)

Regulation and law:
- [EU AI Act Annex III (artificialintelligenceact.eu)](https://artificialintelligenceact.eu/annex/3/)
- [Council of the EU: AI Act simplification agreement (May 2026)](https://www.consilium.europa.eu/en/press/press-releases/2026/05/07/artificial-intelligence-council-and-parliament-agree-to-simplify-and-streamline-rules/)
- [Gibson Dunn: EU AI Act omnibus agreement](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/)
- [Wolters Kluwer: AI Act prohibition of emotion recognition in the workplace](https://legalblogs.wolterskluwer.com/global-workplace-law-and-policy/the-prohibition-of-ai-emotion-recognition-technologies-in-the-workplace-under-the-ai-act/)
- [Holland & Knight: collective action over alleged AI hiring bias (Mobley v. Workday)](https://www.hklaw.com/en/insights/publications/2025/05/federal-court-allows-collective-action-lawsuit-over-alleged)
- [Seyfarth: Mobley v. Workday agent theory](https://www.seyfarth.com/news-insights/mobley-v-workday-court-holds-ai-service-providers-could-be-directly-liable-for-employment-discrimination-under-agent-theory.html)
- [DLA Piper: Data protection laws in Kyrgyzstan](https://www.dlapiperdataprotection.com/?t=law&c=KG)
- [Kyrgyz State Agency for Personal Data Protection: Law "On Personal Information"](https://dpa.gov.kg/en/npa/4)
- [ICNL: Kyrgyzstan personal data guidance note (Aug 2025)](https://www.icnl.org/wp-content/uploads/KG-Personal-Data-Guidance-Note_August-2025_eng.pdf)

Vendor or secondary (used only where marked as such above):
- [Kore.ai: Agentic AI in HR, use cases and examples](https://www.kore.ai/blog/agentic-ai-in-hr)
- [Uptiq: AP automation for banks](https://www.uptiq.ai/document-ai/accounts-payable-automation)
- [IBM: Generative AI in finance](https://www.ibm.com/think/topics/gen-ai-for-finance)
- [GSDC: Generative AI in finance case studies](https://www.gsdcouncil.org/blogs/generative-ai-in-finance-case-studies-and-applications)
- [Emerj: AI in the accounting Big Four](https://emerj.com/ai-in-the-accounting-big-four-comparing-deloitte-pwc-kpmg-and-ey/)
- [ChatFin: Big 4 AI agents and finance teams](https://chatfin.ai/blog/big-4-ai-agents-ey-kpmg-deloitte-pwc-finance-teams-2026/)
- [arXiv 2209.07335: AI models and employee lifecycle management (review)](https://arxiv.org/pdf/2209.07335)

## Confidence and gaps

**Higher confidence**
- Bank of America Erica for Employees (bank-published, but usage and call-reduction figures are self-reported).
- HSBC and Citi/JPMorgan training programmes (bank site and press reports of internal memos).
- EU AI Act Annex III point 4 and the Article 5 emotion-recognition ban; the high-risk deadline moved to 2 December 2027 under the Digital Omnibus (several legal-firm and Council sources agree, but I did not read the Official Journal text).
- Mobley v. Workday procedural history (law-firm summaries; ongoing, no merits ruling as of the sources).
- Gartner survey figures, taken from Gartner releases as summarised in search results. Two Gartner pages could not be fetched directly (HTTP 403); some finance percentages (49%, 37%, 34%) came through summaries and should be checked against the release.

**Vendor-claimed or unverified**
- Kore.ai bank HR case (unnamed bank, 94% resolution, 83% ticket reduction): vendor-published, not independently verified. Do not use as a planning target.
- Deloitte internal Zora AI results (25% cost, 40% productivity) and HPE 50% report-time expectation: company or partner claims.
- BNY payment-validation times and dispute reduction: bank statements reported by Axios; not independently audited.
- IBM close figures: company-reported, and IBM is not a bank.
- PwC Agent OS, PwC GL.ai, KPMG Workbench, EY tax agents: found only in secondary or vendor-adjacent sources.
- Barclays Colleague AI Agent: Emerj summary of a Microsoft feature, not a Barclays disclosure.
- JPMorgan COIN: 2017 figure, is the bank's own estimate, and is ML extraction, not generative AI. An earlier search hit named "ChatCFO" as a JPMorgan tool. I found no supporting evidence and omitted it.
- Goldman Sachs Claude agents: announced as early-stage in Feb 2026; I did not find production results.
- Standard Chartered cut figures and CEO quotes: press-reported from an investor day; not read in the bank's own materials.
- Vendor statistics on AP accuracy (95 to 99%) and close-time cuts (50 to 60%) were seen in vendor content and are not used in the tables.

**Gaps**
- No named bank with published, independently verified results for gen-AI candidate screening, HR attrition analytics, reconciliation, journal entries or IFRS drafting. Evidence for these rows is thin; treat maturity ratings as provisional.
- No bank-specific data on tax, procurement, AR or intercompany automation.
- No IFRS-specific or IAASB guidance on AI-drafted disclosures found. The FRC/ICAEW material is UK auditor-focused.
- Kyrgyz law: data localisation, cross-border transfer rules, Labour Code provisions on employee data and any National Bank of the Kyrgyz Republic guidance on AI, outsourcing and model risk were not confirmed. EU AI Act applicability to O!Bank is untested and needs counsel.
- Central Asian and emerging-market bank examples were not found in this pass; language support (Kyrgyz, Russian) for HR assistants and document extraction is unresearched.
- McKinsey and Big Four finance-function primary reports were not read in full; the McKinsey banking-operations page timed out.
