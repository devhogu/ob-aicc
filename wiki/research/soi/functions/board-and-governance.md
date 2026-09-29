# Board, executive committee and governance functions: AI for the board, oversight of AI, corporate secretary and legal, internal audit

Research note for the AICC. Covers (A) AI that serves the board and executive committee, (B) board oversight of AI, (C) corporate secretary and legal, (D) internal audit. Research date: 2026-09-29. Explanatory only; authority lives in `.grace/`.

Scope note: the user states O!Bank reports to investors and to its parent, ALGA Group. Listing status and ownership are not verified in this repo. Where this note says "listed-entity" concerns (Reg FD-like selective disclosure, MNPI), treat them as applying by analogy to any external audience for non-public results (parent, lenders, DFIs, rating agencies, minority holders) until Legal confirms the applicable Kyrgyz and exchange rules.

## Why it matters

- Board and executive materials are the most sensitive documents in the bank (results before release, strategy, M&A, supervisory correspondence, litigation, capital). The main risk of AI here is leakage or loss of privilege, not model quality. Use of public tools is not acceptable for this material.
- Regulators now name the board as the owner of AI risk. The FSB consultation report (June 2026) puts board and senior management oversight first among 12 sound practices; MAS proposes explicit board duties including AI literacy, risk appetite and an AI inventory. A board that has no AI inventory, risk appetite or literacy plan is exposed regardless of how it uses AI itself.
- The evidence base for boards using AI is thin. Deloitte's July 2026 survey of governance professionals found close to half of public companies have not formally enabled or standardised AI for board activities, and most respondents were unsure whether their boards use it. Informal, unsanctioned use by directors is the likely reality and is the gap to close first.
- Legal and audit have well-documented failure modes: fabricated case citations now number in the thousands of court decisions, and audit teams are adopting AI more slowly than the business they audit. Both functions need AI capability and verification discipline at the same time.

## Use cases

Maturity key: proven = repeated production use reported by named organisations or independent surveys; emerging = vendor products and early named deployments with limited independent evidence; experimental = prototypes, pilots, forward-looking claims.

### A. AI for the board and executive committee

| Use case | What AI does | Maturity | Example or source |
|---|---|---|---|
| Board pack summarisation and pre-read briefs | Condenses long packs into briefs with links to source pages; highlights issues for directors | emerging (products exist; independent evidence thin) | Nasdaq Boardvantage on Azure OpenAI (vendor; "up to 10-30 hours per month" saved is a vendor estimate). Board Intelligence Lucia. Bay Federal Credit Union named by Nasdaq |
| Interrogating the pack in natural language | Directors ask questions over a closed, access-controlled pack; answers cite the paper | emerging | Lloyds Banking Group trial of a Board Intelligence agent (reported by The Times, Apr 2026; read via trade press and secondary coverage) |
| Consistency and quality checks on papers | Flags inconsistencies between papers, missing risks, unstated assumptions, possible bias in a proposal | emerging | Lloyds trial as reported; Board Intelligence describes AI as editor and thinking partner, not author, and says it cannot yet be trusted to author board material (vendor) |
| Management-side paper drafting support | Helps executives structure and tighten papers before submission | emerging | Board Intelligence Lucia (vendor) |
| KPI and risk dashboards with natural-language drill-down | Answers "why did cost of risk rise in segment X" from governed data, showing query and source | emerging | Not board-specific. HPE "CFO Insights" (non-bank; company and Deloitte-reported figures) is in [ir-and-fpa.md](ir-and-fpa.md). Text-to-SQL research shows semantic errors (YoY vs QoQ) |
| Strategic and competitor intelligence for directors | Digests peer results, regulatory moves, market and news into short briefings tied to the bank's strategy | emerging | Lloyds tool reported to draw on external market and regulatory information (secondary); AlphaSense-type tools (vendor) |
| Decision support and pre-mortem | Generates counter-arguments, scenario questions, and "what would make this fail" for a proposal | experimental | Lloyds/Board Intelligence describe a possible second phase with live challenge in meetings; the vendor CEO calls giving AI a vote "a dangerous leap" |
| Minutes and action tracking | Drafts minutes from notes or recordings; extracts actions and owners; tracks due dates | emerging | Nasdaq Boardvantage Meeting Minutes feature (vendor). Skadden (Jun 2026) warns on privilege, discoverability and unvetted records when AI drafts minutes |
| Parent and group reporting | Assembles the periodic package to ALGA Group from the same governed numbers; checks consistency with local board pack | experimental for GenAI; ML/reporting automation proven | No named case found. See FP&A note. Design point, not a sourced claim |
| Investor-facing board intelligence | Brief directors on investor and lender questions, ownership changes, sentiment | emerging | See [ir-and-fpa.md](ir-and-fpa.md) (vendor tools only) |

### B. Board oversight of AI

| Use case | What AI does or what is needed | Maturity | Example or source |
|---|---|---|---|
| Director AI literacy programme | Structured education, briefings, assessment of competence | proven as practice | FSB (2026) reports large financial groups running master classes for board members with academic and consulting partners. EU AI Act imposes an AI-literacy duty on staff. MAS proposes board literacy |
| Board-approved AI risk appetite | Statement of what AI uses the bank will or will not accept, with thresholds | emerging | FSB SP1; MAS consultation; NACD guidance to recalibrate risk appetite (via secondary summary) |
| AI inventory and materiality tiering reported to the board | Register of AI use cases, models, third-party AI, ranked by impact, complexity, reliance | emerging (regulatory expectation, few public examples) | MAS consultation (Impact, Complexity, Reliance); FSB SP3 and SP12 (inventories, third-party registers) |
| Committee ownership | Assign AI to risk, audit or technology committee; cross-functional management committee | emerging | Committee split not settled. A vendor-sourced roundup states audit and risk committees are most often given AI oversight (not verified at primary source). Glass Lewis (2026, via summary): just over half of S&P 100 disclose board-level AI oversight |
| Board AI reporting pack | Periodic dashboard: inventory, incidents, model performance, third-party dependence, policy exceptions, training | experimental (no reference format found) | Basel governance principles ask for reporting against risk appetite and limits; apply the same shape to AI |
| Board policy on directors' own AI use | Approved tools, no public tools, recording and note-taker rules, retention | emerging | Goodwin (Jul 2026), Skadden (Aug 2025, Jun 2026), Simpson Grierson (law-firm guidance) |

### C. Corporate secretary and legal

| Use case | What AI does | Maturity | Example or source |
|---|---|---|---|
| Contract review and clause extraction against a playbook | Extracts terms, flags deviations from playbook, drafts redlines | proven for extraction; emerging for generative redlining | JPMorgan COiN (2017, ML not generative; the 360,000-hour figure is company-reported and repeated by secondary sources). A&O Shearman and Harvey ContractMatrix and loan-review agent (firm announcements; bank named nowhere in what was read) |
| Policy and procedure drafting and updating | First drafts and change tracking of policies against new rules | emerging | McKinsey describes a possible "risk intelligence center" partly automating policy updates (consultant view) |
| Regulatory tracking and horizon scanning | Reads new rules, summarises obligations and deadlines, maps to internal policies | emerging | Citigroup used GenAI to summarise 1,089 pages of new US capital rules (secondary report; interpretation after publication, not horizon scanning). Vendors (Corlytics, Regology) not read |
| Legal research and litigation support | Finds authority, summarises cases and filings | emerging, with measured error | Stanford RegLab (peer-reviewed, JELS 2025): leading legal research tools hallucinated in 17%-33% of tested queries; products tested may since have changed |
| Corporate secretarial work | Agenda building, resolutions, registers, shareholder meeting logistics, minute drafting | emerging | Board portal vendors (Nasdaq, Diligent); Diligent lists GovernAI (vendor comparison page, biased) |
| Group and subsidiary governance | Tracks resolutions and approvals across entities | experimental | No source found |
| Privilege and confidentiality triage | Classifies documents, flags privileged material before sharing | experimental | Not sourced; treat as design idea |

### D. Internal audit

| Use case | What AI does | Maturity | Example or source |
|---|---|---|---|
| Risk-based audit planning | Reads risk registers, incidents, regulatory and internal data to rank auditable entities | emerging | HSBC 20-F FY2024 describes an audit universe and risk assessment feeding the annual plan, with model risk, data management and cyber added or refocused; the excerpt does not say GenAI is used to plan |
| Full-population testing and anomaly detection | Tests all transactions or controls instead of samples | proven | Established analytics practice; Deloitte UK 2025 survey says most functions have digital plans integrated with strategy (figures via search summary) |
| Evidence review, workpaper drafting, report drafting | Summarises evidence, drafts test steps and findings, maps controls to standards | emerging | Gartner: 42% of CAEs rate embedding GenAI in audit workflow an important 2025 priority; most are still exploring (28%) or piloting (21%) (via search summary) |
| Continuous monitoring and issue tracking | Watches indicators, chases remediation | emerging | Vendors (AuditBoard, Fieldguide); Fieldguide figures are vendor claims |
| Auditing AI systems | Assures governance, data, model, third-party and human oversight of AI | emerging | IIA AI Auditing Framework (2017, updated 2023 and Sept 2024); IIA hands-on AI audit course aligned to ISO/IEC 42001 and NIST AI RMF |
| Audit of AI-enabled fraud readiness | Tests whether the bank can detect AI-enabled fraud | emerging | IIA and AuditBoard survey (Feb 2026): fewer than 40% believe their function is adequately prepared (via search summary) |

## Target state for O!Bank

"Fully adopted" means the following, all with human accountability.

**Board and executive committee**
- One sanctioned, closed board-intelligence environment: board portal with AI, hosted with enterprise data terms (no training on bank data, retention controls, audit log, in-region if required). Directors and the executive committee do not use consumer tools for any board material.
- Every board paper has an AI-assisted pre-read brief that cites page and source, plus a consistency check. Executives write the papers; AI edits and challenges.
- KPI and risk dashboards read from the governed finance and risk layer. Natural-language questions show the query and source. Numbers are pulled, not generated.
- Minutes: secretary owns the record. Any AI-drafted minute is a draft that the secretary edits; raw transcripts and interim AI summaries follow a written retention rule agreed with Legal.
- Group reporting to ALGA Group and any investor-facing board intelligence built from the same numbers as the local board pack, with lock and tie-out before release.

**Oversight of AI**
- A board-approved AI policy and risk appetite; an owner committee (proposed: risk committee, with audit committee receiving assurance and technology input from management); a named executive accountable for AI.
- An AI inventory with materiality tiers, reported to the board at least twice a year and on incident. Includes third-party and embedded vendor AI.
- Annual director AI literacy plan and a self-assessment.
- Clear separation: developers and business owners (first line), risk and compliance (second), internal audit (third).

**Corporate secretary and legal**
- Enterprise legal AI for contract extraction, policy drafting support, regulatory change summaries, with citations to source text. Lawyers own the output. No AI-cited authority enters a filing, opinion or board paper without checking against the primary source.
- A single regulatory-change register covering NBKR, EAEU or other applicable sources, and group requirements, linked to policy owners.

**Internal audit**
- Audit universe includes AI use cases and AI vendors. A reusable AI audit programme built on the IIA framework.
- AI-supported planning, full-population testing, workpaper drafting, and report drafting with reviewer sign-off. Internal audit uses its own use policy.

## Phased adoption path

### Phase 1: Foundation
- Ban public consumer AI for board, executive and legal material; publish approved tools and data classes.
- Adopt a short board-level AI policy, an interim risk appetite statement and an initial AI inventory (even a spreadsheet).
- Director and executive AI briefing; baseline literacy assessment.
- Low-risk pilots inside an enterprise environment: pre-read summaries for non-sensitive committee papers; regulatory change summaries for Legal; audit analytics on one process.
- Decide policy on recording, transcription and AI note-takers in board and committee meetings; brief the corporate secretary on privilege and discoverability.
- Confirm with Legal: listing and disclosure obligations, Kyrgyz data-residency and confidentiality rules, and which regulator rules on board oversight apply.

### Phase 2: Scale
- Board portal with AI features for summarisation, consistency checks and Q&A over packs, after a security review; limit first to one committee.
- Board AI dashboard (inventory, tiers, incidents, training) delivered regularly.
- Contract clause extraction against a playbook for high-volume contract types.
- AI-assisted audit planning and workpaper support; first audit of a live AI use case.
- Minutes drafting as a secretary-owned draft, with agreed retention rules.

### Phase 3: Platform
- Governed data layer feeding board dashboards, group reporting and investor briefings from one source.
- Central inventory and lifecycle records integrated with model risk, third-party risk and audit universe.
- Regulatory-change register linked to policies and controls; policy drafting assisted with change tracking.
- Continuous monitoring and issue-tracking across audit and compliance.

### Phase 4: Agentic
- Agents that prepare board packs from source systems, track actions to closure, monitor regulatory feeds, and pre-test audit controls. Each agent has a named owner, permissions, thresholds and logs.
- Live-meeting AI, if ever used, is a research aid to directors and never a decision-maker (Lloyds' own vendor rejects AI voting). Preparers do not approve.
- Progress gate: move up only after measured accuracy and control evidence for the previous phase.

## Data and system prerequisites

- Board portal or secure document platform with role-based access, per-document permissions, watermarking, and an audit log. Confirm where the AI runs, whether prompts and outputs are retained, and whether the vendor trains on them.
- Data classification scheme that marks board, MNPI-like and privileged material and blocks it from non-approved tools.
- Governed finance and risk data (see [ir-and-fpa.md](ir-and-fpa.md)) with a semantic layer and KPI glossary, so dashboards agree with the board pack.
- AI inventory and third-party register (fields: owner, purpose, data, vendor, materiality tier, validation status, human-oversight design).
- Document and contract repository with clean metadata for contract extraction; policy library with owners and versions.
- Regulatory sources feed (NBKR, group, and any exchange or investor rules) and a way to link each requirement to a policy and control.
- Audit management system with data connectors for full-population testing.
- Language: Kyrgyz, Russian and English. No source found measuring model quality on Kyrgyz or Russian legal and financial text; test on real papers before relying on it.
- Retention and records policy that covers prompts, transcripts, AI summaries and drafts.
- Enterprise LLM access with logging, in-region or private hosting where required, and an evaluation harness.

## Risks and controls

| Risk | Control |
|---|---|
| Leakage of board or executive material into public or unapproved tools (including via director personal devices and AI note-takers) | Approved-tools-only policy for directors and management; closed environment; no public tools; device and access controls; ban third-party recorders or transcribers in meetings and with counsel unless approved |
| Selective disclosure or MNPI-type leakage of pre-release results, guidance or transactions | Enterprise-only tools; information barriers on pre-release data; no autonomous external communication; log prompts. Reg FD is a US rule and the theory that a prompt to a vendor is a disclosure is contested (search-summarised commentary; no enforcement action found). Confirm the Kyrgyz and exchange position with counsel and apply the strict standard by analogy |
| Loss of privilege and creation of discoverable records | Skadden (2025, 2026) and Goodwin (2026): communications with AI tools are generally not privileged; AI-drafted material may not get work-product protection; extra transcripts and summaries create discoverable records. Control: secretary-owned record, retention rule, no AI tools in counsel discussions unless approved and contractually protected. Jurisdiction-dependent: Kyrgyz law is unresearched here |
| Hallucinated citations in legal work, board papers or reports | Verify every authority against primary source; citation checks; no AI-generated authority in filings or opinions without lawyer check. Evidence: Stanford RegLab 17%-33% error in legal research tools; Mata v. Avianca (US, 2023, US$5,000 sanction); Charlotin database lists over 2,000 court decisions with hallucinated content (count changes daily; database figure read via search summary); Deloitte Australia refunded part of a government report fee over AI-generated errors (2025) |
| Directors over-trust summaries; loss of independent judgment | Summaries always cite pages; directors read the source for key decisions; AI is challenger, not author; document that AI output is advisory |
| Chilling effect and altered deliberation (recordings, transcripts) | Board decides recording and minute policy explicitly; minutes stay concise and secretary-owned (Goodwin) |
| AI risk unowned or unreported at board level | Named committee owner; inventory and tiering; regular board reporting; risk appetite. FSB SP1 to SP3; MAS consultation |
| Regulatory posture unclear in Kyrgyzstan | See Confidence and gaps. Track Ministry of Digital Development draft ethics-of-AI regulation, NBKR requirements, Digital Code |
| Vendor concentration and data terms (board portals, legal AI) | Third-party risk review; contract terms on training, retention, hosting; exit plan. FSB SP12 |
| Internal audit independence and over-reliance on AI | Auditors validate AI output; AI does not conclude; documented use policy; separate audit of the bank's own AI use. Banking.Vision commentary: analysis gives hypotheses, not findings |
| Internal audit skill gap | Train auditors; use IIA framework and course; start with a micro-audit (Weaver suggestion, May 2025) |
| AI washing in investor or group communications | Legal review of every AI claim in results materials and reports |

## Metrics

Baseline first; no target values are asserted because none are sourced for a bank of this size.

**Board and executive committee**
- Director prep time per meeting (self-reported) and share of directors using sanctioned tools
- Share of papers with AI pre-read brief and consistency check; issues caught before circulation
- Share of dashboard answers matching a known-answer test set
- Time from meeting to approved minutes; action-closure rate and overdue actions
- Incidents: material in unapproved tools, misdirected AI summaries

**Oversight of AI**
- Inventory completeness (use cases found by audit or discovery not in inventory)
- Share of high-materiality use cases with validation and named owner
- Board and committee time on AI; director literacy assessment coverage
- AI incidents, policy exceptions and time to close

**Corporate secretary and legal**
- Contract review cycle time; share of AI-extracted terms overridden on review
- Fabricated or unverifiable citations caught in review, and any reaching a filing (target: zero)
- Time from publication of a rule to owner assessment; policies updated on time

**Internal audit**
- Audit plan coverage of AI use cases and AI vendors
- Share of audits using full-population testing; hours per audit
- Edit rate on AI-drafted workpapers and reports
- Findings from AI-assisted work confirmed on review

## Sources

Regulators, standard setters, surveys
- [FSB, Sound Practices for Financial Institutions' Responsible AI Adoption: Consultation Report (June 2026, PDF)](https://www.fsb.org/uploads/P100626.pdf) (text extracted and read directly; consultation, comments due 22 July 2026; final status not checked)
- [BIS FSI Insights No 35, Humans keeping AI in check (2021)](https://www.bis.org/fsi/publ/insights35.pdf) (search summary only)
- [BIS FSI Occasional Paper 24, Managing explanations: how regulators can address AI explainability (2025)](https://www.bis.org/fsi/fsipapers24.pdf) (search summary only)
- [BIS FSI Briefs 26, gen AI stocktake by supervisors](https://www.bis.org/fsi/fsibriefs26.pdf) (search summary only)
- [BCBS, Corporate governance principles for banks (2015)](https://www.bis.org/publ/bcbs294.pdf) (search summary only)
- [G20/OECD Principles of Corporate Governance 2023, board responsibilities](https://www.oecd.org/en/publications/2023/09/g20-oecd-principles-of-corporate-governance-2023_60836fcb/full-report/component-8.html) (search summary only; no AI-specific text seen)
- [EBA, AI Act implications for the EU banking and payments sector (Nov 2025)](https://www.eba.europa.eu/sites/default/files/2025-11/d8b999ce-a1d9-4964-9606-971bbc2aaf89/AI%20Act%20implications%20for%20the%20EU%20banking%20sector.pdf) (search summary only; the EBA says it is not a statement of supervisory expectations)
- [OCC Bulletin 2026-13, Model Risk Management: Revised Guidance (Apr 2026)](https://www.occ.gov/news-issuances/bulletins/2026/bulletin-2026-13.html) and [Fed SR 26-2](https://www.federalreserve.gov/supervisionreg/srletters/SR2602.pdf) (search summaries only; replace SR 11-7; generative and agentic AI excluded from scope)
- [Sullivan & Cromwell memo on the revised model risk guidance (Apr 2026)](https://www.sullcrom.com/insights/memo/2026/April/OCC-Fed-FDIC-Issue-Revised-Guidance-Model-Risk-Management)
- [MAS, Consultation Paper on Guidelines on AI Risk Management (Nov 2025)](https://www.mas.gov.sg/-/media/mas-media-library/publications/consultations/bd/2025/final_consultation_paper_on_guidelines_on_ai_risk_management_forrelease.pdf) and [Bird & Bird summary](https://www.twobirds.com/en/insights/2026/singapore/mas-consults-on-proposed-guidelines-on-artificial-intelligence-risk-management) (search summaries only; final status not checked)
- [Bank of England PRA, roundtable on AI and model risk management (Nov 2025)](https://www.bankofengland.co.uk/prudential-regulation/publication/2025/november/pra-holds-model-risk-management-roundtable-on-ai) (search summary only; SS1/23 background via vendor blogs)
- [IIA, AI Auditing Framework](https://www.theiia.org/en/content/tools/professional/2023/the-iias-updated-ai-auditing-framework/) and [Sept 2024 update PDF](https://www.theiia.org/globalassets/site/content/tools/professional/aiframework-sept-2024-update2.pdf) (PDF could not be read; content via search summaries and secondary sites)
- [IIA, 2024 Global Internal Audit Standards](https://www.theiia.org/en/standards/2024-standards/global-internal-audit-standards/) (Standard 10.3 via KPMG and other commentary, search summaries)
- [IIA and AuditBoard survey on AI-enabled fraud (Feb 2026)](https://www.theiia.org/en/content/communications/press-releases/2026/new-survey-from-the-iia-and-auditboard-report-reveals-growing-awareness-of-ai-enabled-fraud-varying-perception-of-audit-preparedness/) (search summary only)
- [NACD, Survey Analysis: AI (2025 Public Company Board Practices and Oversight Survey)](https://www.nacdonline.org/all-governance/governance-resources/governance-surveys/surveys-benchmarking/2025-public-company-board-practices--oversight-survey/2025-board-practices-oversight-ai/) and [Director Essentials: Implementing AI Governance](https://www.nacdonline.org/all-governance/governance-resources/governance-research/director-faqs-and-essentials/implementing-ai-governance/) (search summaries only; member-only tables)
- [ICGN, Investor Viewpoint: Artificial Intelligence, an engagement guide (Mar 2024)](https://www.icgn.org/icgn-investor-viewpoint-artificial-intelligence-engagement-guide) (search summary only)
- [Glass Lewis, US AI oversight through three lenses (2026)](https://www.glasslewis.com/article/us-ai-oversight-through-three-lenses-investor-expectations-sp-100-company-specific-analysis) (search summary only)
- [Deloitte Center for Board Effectiveness, How boards are using AI today (Board Practices Quarterly, Jul 2026)](https://www.deloitte.com/us/en/programs/center-for-board-effectiveness/articles/board-of-director-ai-use.html) (page read; full PDF not read)
- [Gartner, Benchmarking generative AI in internal audit](https://www.gartner.com/en/audit-risk/trends/genai-in-audit) and [Deloitte UK internal audit digital and analytics survey 2025](https://www.deloitte.com/uk/en/services/consulting-risk/research/internal-audit-digital-analytics-survey.html) (search summaries only)

Board tooling, bank and company cases
- [Digit.fyi, Lloyds trials AI boardroom bot](https://www.digit.fyi/lloyds-trials-ai-boardroom-bot-in-ftse-first/) and [Retail Banker International, Lloyds to use AI tool in board meetings](https://www.retailbankerinternational.com/news/lloyds-bank-board-ai-tool/) (search summaries; the original Times report was not read; the "first FTSE 100" claim is press-reported)
- [Perplexity AI Magazine, Lloyds board bot (May 2026)](https://perplexityaimagazine.com/ai-news/ai-news-lloyds-banking-ai-board-bot-ftse-100-first-2026/) (read; low-quality secondary source, many figures unsourced and not used here)
- [Nasdaq, Boardvantage AI for Boards](https://www.nasdaq.com/en-gb/products/governance/boardvantage/ai-for-boards) and [Microsoft customer story](https://www.microsoft.com/en/customers/story/25682-nasdaq-azure) (vendor; search summaries)
- [Board Intelligence, AI for board performance](https://www.boardintelligence.com/ai-for-board-performance) (vendor; search summary)
- [Diligent vs Boardvantage comparison](https://www.diligent.com/lp/diligent-vs-boardvantage-new) (vendor marketing, biased)
- [HSBC Form 20-F FY2024, Global Internal Audit planning](https://www.sec.gov/Archives/edgar/data/0001089113/000108911325000040/hsbc-20241231.htm) (search excerpt only)
- [A&O Shearman and Harvey agentic agents](https://www.aoshearman.com/en/news/ao-shearman-and-harvey-to-roll-out-agentic-ai-agents-targeting-complex-legal-workflows) (firm announcement; search summary)
- JPMorgan COiN: secondary explainers only (for example [Emre Ates](https://www.emreates.co.uk/research-2/jpmorgan's-coin-(contract-intelligence)-platform:-using-ai-in-mergers-&-acquisitions-and-commercial-lending)); no primary source read
- [McKinsey, How generative AI can help banks manage risk and compliance](https://www.mckinsey.com/capabilities/risk-and-resilience/our-insights/how-generative-ai-can-help-banks-manage-risk-and-compliance) (search summary; Citigroup 1,089-page example came in the same result set, secondary)

Legal, privilege, hallucination
- [Skadden, AI drafting board minutes (Jun 2026)](https://www.skadden.com/insights/publications/2026/06/the-informed-board/ai-drafting-board-minutes) and [Do's and Don'ts of using AI: a director's guide (Aug 2025)](https://www.skadden.com/insights/publications/2025/08/the-informed-board/dos-and-donts-of-using-ai) (search summaries)
- [Goodwin, Governing the board's own use of AI (Jul 2026)](https://www.goodwinlaw.com/en/insights/publications/2026/07/alerts-practices-aiml-pca-governing-boards-ai-fiduciary-duties-risks-practical-safeguards) and [Simpson Grierson, Directors take note](https://www.simpsongrierson.com/insights-news/legal-updates/directors-take-note-the-legal-pitfalls-of-ai-in-the-boardroom) (search summaries)
- [Stanford RegLab / JELS, Hallucination-free? Assessing the reliability of leading AI legal research tools](https://onlinelibrary.wiley.com/doi/full/10.1111/jels.12413) (search summary)
- [Damien Charlotin, AI Hallucination Cases database](https://www.damiencharlotin.com/hallucinations/) (count via search summary)
- Mata v. Avianca: secondary summaries only (for example [Esquire Deposition Solutions](https://www.esquiresolutions.com/federal-court-turns-up-the-heat-on-attorneys-using-chatgpt-for-research/)); the court decision was not read
- [CFO Dive, Deloitte refund over AI errors in Australian government report](https://www.cfodive.com/news/deloitte-refunds-60k-report-ai-errors-australian-government-accounting/803321/) and [OECD.AI incident record](https://oecd.ai/en/incidents/2025-10-05-be45) (search summaries; reported figures differ)
- [FINRA Regulatory Notice 24-09](https://www.finra.org/rules-guidance/notices/24-09) (broker-dealer context; search summary) and [Finrep, LLM MNPI leakage and Reg FD (vendor blog)](https://www.finrep.ai/blog/llm-mnpi-data-leakage-and-reg-fd-a-2026-compliance-walkthrough) (vendor; arguments not settled law)

Kyrgyzstan and region
- [Economist.kg, draft AI ethics regulation (28 Sep 2026)](https://economist.kg/technology/2026/09/28/pravila-etiki-ii-kyrgyzstan/) (page read; draft from the Ministry of Digital Development, public consultation)
- [Akchabar, NBKR to use AI and big data for banking supervision](https://www.akchabar.kg/en/news/natsbank-vnedrit-tekhnologii-ii-i-bolshikh-dannikh-dlya-nadzora-za-bankami-rqyiydsudaburyyn) and [Open.kg, NBKR SupTech concept and roadmap 2026-2031](https://open.kg/en/news/economy/122684-postanovleniem-pravlenija-nacbanka-kyrgyzstana-utverzhdena-koncepcija-i-dorozhnaja-karta-razvitija-nadzornyh-tehnologij-suptech-na-20262031-gody.html) (search summaries; NBKR using AI to supervise, not a rule for banks)
- [Law of the Kyrgyz Republic No 93 of 11 Aug 2022 On Banks and Banking Activity](https://cbd.minjust.gov.kg/4-3214/edition/1241184/ru) (article titles via search summary only; Chapter 4 on bank management includes board and board committees, articles 33 to 39)
- [Times of Central Asia, Kazakhstan's approach to AI regulation in finance](https://timesca.com/kazakhstan-adopts-pragmatic-ai-regulation-in-financial-sector/) and [EY Kazakhstan on the Law on Artificial Intelligence](https://www.ey.com/ru_kz/technical/tax-alerts/2025/12/law-on-artificial-intelligence-kazakhstan) (comparison only)

## Confidence and gaps

- Highest confidence: the FSB consultation text (read directly from the extracted PDF), the Economist.kg draft ethics regulation (page read), and the Deloitte board survey page. Everything else about regulators, NACD, ICGN, Glass Lewis, IIA, MAS, EBA, OCC/Fed, Skadden, Goodwin and Stanford was read only through search-result summaries; check the originals before citing externally. The IIA framework PDF and several law-firm pieces could not be opened.
- Board-AI evidence is thin and mostly vendor or press. The one named bank case is Lloyds (a trial, reported through The Times and trade press; scope and results not published). No named bank case found for: board pack summarisation in production at a bank, parent-group reporting with AI, AI-supported audit planning at a named bank, or regulatory horizon scanning in production. Vendor claims (Nasdaq 10-30 hours, Board Intelligence, Diligent, Fieldguide, AuditBoard) are unverified marketing.
- JPMorgan COiN figures are company-reported and read via secondary blogs. Citi's 1,089-page rule summary is a secondary report.
- Regulatory scope: none of the bodies named is binding on O!Bank. FSB, BIS, OECD, ICGN and IIA are non-binding; EU and US texts apply only by analogy. Basel and OECD-G20 text on AI specifically was not found; the OECD-G20 principles carry general risk-oversight and digital-expertise language only. The FSB report is a consultation; the MAS paper was a consultation when last seen. The US agencies replaced SR 11-7 in April 2026 and excluded generative and agentic AI from the new guidance (secondary summaries).
- Kyrgyzstan: no NBKR rule on banks' own use of AI or on board oversight of AI was found. The draft AI ethics regulation would make ethics self-assessment mandatory for state bodies and high-risk systems and only recommended for other private systems (as reported; banks not mentioned). A Digital Code effective 2026 was mentioned in a search summary and not read. The banking law's board chapter was identified by article titles only; board duties, committees and NBKR corporate-governance requirements were not read. No EAEU-level rule on AI in banks was found. Confirm all with Legal and NBKR.
- Listing, Reg FD analogue and MNPI: O!Bank's listing status and disclosure regime are unverified. Reg FD material found is US and mostly commentary; no enforcement action treating an AI prompt as selective disclosure was found. Privilege findings are from US and NZ law-firm guidance; Kyrgyz privilege and discovery rules were not researched.
- Not researched: cost of tools, ISO/IEC 42001 and NIST AI RMF text, EU AI Act obligations beyond literacy, Protiviti and Big Four internal audit surveys beyond summaries, DFI or rating-agency governance expectations, and language quality on Kyrgyz and Russian legal text.
