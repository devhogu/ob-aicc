# Generative and agentic AI in IT and banking systems

Research note for the AICC. Scope: software delivery, core/legacy modernization, IT operations, cybersecurity and AI security, data and platform readiness, and operational resilience. Research date: September 2026. Figures marked "(self-reported)" come from a bank executive or vendor and were not independently verified.

## Why it matters

- Software delivery is the most mature bank use of GenAI. Large banks report gains, but the evidence is uneven: gains are reported as task-level or phase-level, and independent studies show a much smaller or even negative effect in some settings.
- Legacy code (COBOL and similar) is the main brake on change at most banks. GenAI is now credible for the discovery, documentation and test-generation parts of modernization, less so as an unsupervised translator.
- The same tools that speed delivery add new attack surface (prompt injection, over-privileged agents, insecure generated code) and new third-party dependence on a handful of model and cloud providers. Supervisors in the EU already treat both as operational-resilience matters.
- For a mid-size bank, the platform choices (model gateway, tool layer, agent identity, evaluation) matter more than any single assistant. They decide whether later agentic use is safe and reversible.

## Use cases

| Use case | What AI does | Maturity | Example bank or source |
|---|---|---|---|
| Coding assistant (completion, chat) | Suggests, explains and refactors code in the IDE | proven | Bank of America: ~18,000 developers, "over 20%" efficiency in selected lifecycle phases (self-reported); JPMorgan: 10-20% engineer efficiency (secondary source, self-reported); Lloyds: ~5,000 engineers on GitHub Copilot |
| Automated code review and PR summaries | Reviews changes, writes PR descriptions, flags issues | proven / emerging | Citi Squad: 740,000 automated reviews, ~100,000 hours/week saved (self-reported) |
| Autonomous coding agents on bounded tasks | Patches, dependency upgrades, language rewrites, doc and test creation; outputs go to a human | emerging | Citi (Devin, 40,000 developers; agents cannot deploy code); Goldman Sachs (Devin, 3-4x claim, executive claim only) |
| Test generation and QA | Drafts test scenarios and regression tests, including for migrated code | emerging | GFT with a global bank (test scenarios and documentation for COBOL-to-Java); no named-bank quantified QA case found |
| Requirements and user stories | Drafts stories and acceptance criteria from source material | experimental / emerging | Thoughtworks pilot (client not confirmed as a bank) |
| Documentation and knowledge extraction | Explains legacy code, reconstructs business rules, produces specs | emerging (strongest modernization use) | Lloyds (agentic re-documentation of mortgage COBOL); Accenture COBOL tool (2024) |
| Legacy code translation (COBOL to Java) | Converts code, usually paired with deterministic converters | emerging | GFT and a global bank with 80M+ customers (hybrid, no quantified results published); Microsoft and Bankdata (agent framework, no public report); Lloyds pricing app refactored in ~6 months, running in parallel with the old one (executive interview) |
| DevSecOps / secure coding | Finds and fixes vulnerabilities, secrets, misconfigurations in pipeline | emerging | Evidence is mostly about risk: Veracode found ~45% of AI-generated samples failed security tests (vendor test) |
| IT service desk and employee assistant | Answers IT requests, resets, device activation | proven | Bank of America Erica for Employees: over 90% of employees use it, IT service-desk calls down over 50% (self-reported) |
| AIOps: alert correlation, incident summary, root-cause suggestion | Groups alerts, summarizes incidents, drafts post-incident reports | emerging | Vendor material only (ServiceNow, BigPanda); no named-bank result verified |
| Agentic remediation in IT operations | Selects and executes remediation in connected systems | experimental | Vendor descriptions only |
| SOC alert triage and investigation | Summarizes alerts, enriches, correlates, drafts response; analyst approves | emerging | Microsoft reports ~30% lower MTTR with Security Copilot (vendor research, not bank-specific); Google Cloud reference architecture for multi-agent triage |
| Multi-agent platform for business workflows | Orchestrated agents behind a central gateway | emerging | Lloyds "Envoy" platform with a central LLM gateway, A2A and MCP (executive interview; the COO says a gap remains between promise and practice) |

## Target state for O!Bank

"Fully adopted" means AI is a governed engineering and operations capability, not a set of separate tools.

**Delivery**
- Every engineer has an approved assistant. Review, test generation and documentation agents run in the pipeline; agents open pull requests but never deploy. Humans own merges and releases.
- Generated code passes the same automated tests, static analysis, dependency and secret scanning as human code. Small batches and strong automated testing are the precondition (DORA 2025: AI amplifies existing strengths and weaknesses).

**Modernization**
- Legacy estate is inventoried and documented with AI assistance. Business rules are extracted into reviewed specifications, and new code is validated against the legacy system by parallel runs and regression tests before cut-over.
- Deterministic converters do the mechanical translation where they exist; GenAI does discovery, documentation, test creation and readability.

**Operations and security**
- AI summarizes incidents, correlates alerts and proposes runbook steps. Low-risk, reversible actions may be automated after evidence; the rest require approval.
- SOC analysts use AI for triage and enrichment, with human approval for containment. AI systems themselves are inside SOC monitoring.

**Agentic platform foundations** (shared by all of the above)
1. Model gateway: one front door for all model calls (commercial API, and open-weight models where hosted), with authentication, per-team budgets, PII masking, logging and routing. Lloyds routes all model access through a central gateway; JPMorgan's LLM Suite is model-agnostic. Both are examples, not proof of benefit.
2. Tool layer: internal systems exposed to agents through a small set of governed APIs or MCP servers, each with least-privilege scopes, audience-bound tokens, and an inventory.
3. Agent identity: each agent is a registered non-human identity with an owner, entitlements, expiry and audit trail. Citi's CTO describes agents as technology systems needing entitlements, identity and quality checks.
4. Evaluation and observability: versioned prompts, test sets per use case, regression evals on model change, traces of tool calls, and cost monitoring.
5. Policy and human oversight: autonomy levels per use case (suggest / act with approval / act autonomously), kill switch, and action logs.
6. Exit plan: a documented ability to swap model or cloud provider for each critical use.

## Phased adoption path

**Foundation (0-6 months)**
- Approve one or two coding assistants and a private, enterprise-terms model endpoint. Publish acceptable-use, data classification for prompts, and a register of AI use cases.
- Stand up a minimal model gateway with logging and PII masking. Baseline delivery metrics before rollout.
- Start SOC and IT-service use cases that keep a human in the loop (alert summaries, ticket triage, knowledge search).
- Inventory legacy systems and third-party AI dependencies.

**Scale (6-18 months)**
- Roll assistants out to all engineers with training and pipeline security gates. Add AI code review and test generation.
- Run a bounded modernization pilot on one non-critical legacy component: documentation and rule extraction first, then translation with parallel run.
- Add AIOps correlation and incident summarization. Introduce an evaluation harness and red-team testing.

**Platform (12-30 months)**
- Consolidate on the gateway and tool layer for all AI use. Publish governed APIs and MCP servers for priority systems. Introduce agent identity and a central agent registry.
- Decide build / buy / open-weight per workload, based on data sensitivity, cost and exit ability (see prerequisites).
- Extend modernization to additional components using the pattern proven in the pilot.

**Agentic (24 months onward, gated by evidence)**
- Coding agents on well-defined backlog items; SOC and IT-ops agents that act on low-risk, reversible steps; multi-agent workflows across systems.
- Promote an agent to a higher autonomy level only after eval results, incident review and risk sign-off. Timings are indicative; one vendor-authored guide puts scale at 24-36 months, but this is not a validated benchmark.

## Data and system prerequisites

- **Engineering hygiene.** Version control, CI with automated tests, trunk-based or small-batch delivery, and platform quality. Without these AI raises instability rather than throughput (DORA 2025 reports AI adoption still associated with higher delivery instability).
- **Legacy visibility.** Source code access, dependency maps, batch job schedules, copybook/data-dictionary coverage, and a regression suite or a means to capture production behavior for comparison. Modernization pilots report hidden complexity such as implicit date handling, packed decimals and undocumented rules (Anthropic playbook, vendor).
- **Language and locale.** Bankdata found local-language comments and identifiers needed handling. Expect the same with Russian and Kyrgyz text in code, tickets and knowledge bases; test models on it.
- **APIs and integration.** Stable, documented APIs or events in front of core systems so agents call governed interfaces rather than databases or screens. Event streaming helps with real-time context but no bank-specific evidence was found tying it to agent outcomes.
- **Data governance.** Data classification, access controls that carry through to retrieval (RAG must respect entitlements), lineage for knowledge sources, and a rule on what may leave the bank in a prompt. McKinsey describes leading banks building an ontology of workflows and knowledge for agents (consultancy view).
- **Identity and access.** Workload identity for agents, SSO-backed OAuth for tool access, secrets management.
- **Observability.** Central logs of prompts, tool calls, decisions and costs, retained under bank audit rules.
- **Hosting choice.** Commercial API for general productivity; private/on-prem or in-country open-weight hosting for the most sensitive code and customer data. Self-hosting shifts GPU capacity, serving, patching and model lifecycle to the bank. One source claims open-weight cost/performance now rivals proprietary APIs; treat as unverified and benchmark on O!Bank tasks.

## Risks and controls

| Risk | Control |
|---|---|
| Prompt injection (OWASP LLM01) and indirect injection via documents, tickets, web pages, code | Treat all retrieved content as untrusted; separate instructions from data; restrict tool actions; require approval for consequential actions; test with red-team suites |
| Excessive agency (LLM06) | Minimal tool set, least-privilege scopes, per-action limits, human approval by autonomy level, kill switch |
| Sensitive information disclosure (LLM02), data leakage into prompts or logs | Data classification, PII masking at the gateway, enterprise-terms endpoints, no training on bank data, log redaction, DLP |
| Supply chain and poisoning (LLM03/04), malicious or vulnerable MCP servers and packages | Approved-server inventory, signed and reviewed connectors, sandboxing, dependency scanning |
| Agent identity sprawl and confused deputy | Registered agent identities with owners and expiry; audience-bound tokens; MCP spec forbids token passthrough and requires token audience validation; user-scoped delegation rather than shared service accounts |
| Insecure or wrong generated code | Same security gates as human code; mandatory human review; test-first practice; do not measure success by lines generated. Veracode (vendor) reports ~45% of samples failed security tests |
| Migration errors that alter financial calculations | Parallel run, regression and reconciliation tests, staged cut-over, rule sign-off by business owners |
| Overstated productivity | Baseline before rollout; measure delivery outcomes, not usage. METR's 2025 randomized trial found experienced developers 19% slower with AI on their own mature repositories while believing they were 20% faster (small sample, early-2025 tools, METR now marks it historical) |
| Agent project failure and "agent washing" | Fund use cases with defined value; Gartner (forecast, June 2025) predicts over 40% of agentic AI projects cancelled by end 2027 due to cost, unclear value or weak risk controls |
| Third-party and concentration risk | Register of AI providers and their subcontractors, criticality assessment, exit and substitution plan, multi-model gateway, contractual audit and incident-notification terms |
| Data residency and jurisdiction | Map where prompts, logs and embeddings are stored and processed; keep restricted data in-country or on-prem; confirm with local counsel (see gaps) |
| Frontier-AI cyber threat | Faster patching, monitoring of AI-enabled attacks, resilience testing; ECB supervision stresses faster attacks and shorter defender time |
| Model risk and governance | Apply existing model and technology risk management to AI; use NIST AI RMF and the GenAI Profile (NIST AI 600-1) as a control catalogue |

Regulatory reference points (for method, not as Kyrgyz law): DORA (in application in the EU since 17 January 2025) requires an ICT third-party register, concentration assessment and exit strategies. In January 2026 BaFin said AI systems are governed within existing ICT governance, testing and third-party frameworks (via secondary source). On 31 July 2026 the EBA, EIOPA and ESMA issued a joint statement on ICT risks from frontier AI models. US SR 26-2 (17 April 2026) replaced SR 11-7 and puts generative and agentic AI outside its scope, leaving institutions to apply general risk principles.

## Metrics

Delivery
- Lead time for changes, deployment frequency, change failure rate, time to restore (DORA measures), before and after AI rollout.
- Share of merged code that is AI-assisted, with defect and vulnerability rate of that code versus the rest.
- Pull-request cycle time, review turnaround, test coverage change.
- Assistant weekly active use and developer-reported trust (usage alone is not value).

Modernization
- Legacy components documented; business rules extracted and signed off; parallel-run discrepancy rate; components migrated and retired; cost and time per component versus estimate.

Operations and security
- Incident MTTR and MTTA, alert volume per incident, share of tickets resolved without human touch, service-desk call volume.
- SOC triage time, analyst-overturned AI verdict rate, false-negative findings from audits.

Platform and control
- Share of AI traffic via the gateway; number of registered agents with named owner; policy violations blocked; eval pass rate per release; cost per use case.
- Provider concentration (share of AI spend and critical functions per provider); tested exit plans; incidents and near-misses involving AI.

## Sources

Software delivery
- [American Banker: Citi is rolling out agentic AI to its 40,000 developers](https://www.americanbanker.com/news/citi-is-rolling-out-agentic-ai-to-its-40-000-developers)
- [IBM: Goldman Sachs and Devin](https://www.ibm.com/think/news/goldman-sachs-first-ai-employee-devin)
- [Bank of America newsroom: AI adoption by global workforce (April 2025)](https://newsroom.bankofamerica.com/content/newsroom/press-releases/2025/04/ai-adoption-by-bofa-s-global-workforce-improves-productivity--cl.html)
- [McKinsey: Unleash developer productivity with generative AI](https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/unleashing-developer-productivity-with-generative-ai)
- [METR: Early-2025 AI and experienced open-source developer productivity](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)
- [DORA: State of AI-assisted Software Development 2025](https://dora.dev/dora-report-2025/)
- [Google Cloud: Announcing the 2025 DORA report](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report)
- [Veracode: 2025 GenAI Code Security Report](https://www.veracode.com/blog/genai-code-security-report/)
- [Veracode: Spring 2026 update](https://www.veracode.com/blog/spring-2026-genai-code-security/)
- [Emerj: JPMorgan Chase AI (LLM Suite, secondary)](https://emerj.com/artificial-intelligence-at-jpmorgan-chase/)
- [Thoughtworks: AI for requirements analysis, case study](https://www.thoughtworks.com/insights/blog/generative-ai/using-ai-requirements-analysis-case-study)

Modernization
- [GFT: Modernizing core banking with generative AI](https://www.gft.com/us/en/insights/success-stories/modernizing-core-banking-next-generation-architecture-generative-ai)
- [The Stack: Lloyds COO on agents, COBOL, IAM](https://www.thestack.technology/ron-van-kemanade-group-coo-lloyds-on-pivoting-to-agents-eying-200-cobol-applications/)
- [TechRepublic: Lloyds projects GBP 100M value from AI in 2026](https://www.techrepublic.com/article/news-lloyds-bank-ai-value/)
- [Microsoft: AI agents for COBOL migration (Bankdata)](https://devblogs.microsoft.com/all-things-azure/how-we-use-ai-agents-for-cobol-migration-and-mainframe-modernization/)
- [CIO Dive: Banks to deploy AI to retool legacy apps](https://www.ciodive.com/news/banks-leverage-generative-AI-cobol-coding-assistants/703988/)
- [Anthropic: Code Modernization Playbook (vendor)](https://resources.anthropic.com/hubfs/Code%20Modernization%20Playbook.pdf)
- [Accenture: Core banking modernization with generative AI](https://bankingblog.accenture.com/core-banking-modernization-unlocking-legacy-code-with-generative-ai)

IT operations and security operations
- [Kellton: ServiceNow in BFSI (vendor partner)](https://www.kellton.com/kellton-tech-blog/servicenow-in-bfsi-how-banks-insurers-use-genai-to-transform-it-operations)
- [BigPanda: agentic AI in major incident management (vendor)](https://www.bigpanda.io/blog/use-cases-agentic-ai-itsm/)
- [Google Cloud: agentic AI for security operations workflows](https://docs.cloud.google.com/architecture/agentic-ai-orchestrate-security-ops-workflows)
- [Microsoft research: Generative AI and SOC productivity (vendor)](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/final/en-us/microsoft-brand/documents/Generative-AI-and-Security-Operations-Center-Productivity-Evidence-from-Live-Operations_v2.5-FINAL.pdf)

AI security
- [OWASP GenAI Security Project: Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/)
- [MCP specification: Authorization (2025-06-18)](https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization)
- [Coalition for Secure AI: MCP security](https://www.coalitionforsecureai.org/wp-content/uploads/2026/03/model-context-protocol-security-1.pdf)
- [BankInfoSecurity: 6 ways to contain enterprise risk in MCP](https://www.bankinfosecurity.com/blogs/6-ways-to-contain-enterprise-risk-in-model-context-protocol-p-4134)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) and [NIST AI 600-1 GenAI Profile](https://doi.org/10.6028/NIST.AI.600-1)

Platform, strategy and gateway
- [McKinsey: Agentic AI in banking](https://www.mckinsey.com/industries/financial-services/our-insights/agentic-ai-is-here-is-your-banks-frontline-team-ready)
- [Gartner: Over 40% of agentic AI projects will be canceled by end of 2027](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027)
- [LiteLLM AI gateway (vendor)](https://www.litellm.ai/ai-gateway)

Resilience, regulation, residency
- [FSB: Monitoring adoption of AI and related vulnerabilities in the financial sector (Oct 2025)](https://www.fsb.org/2025/10/monitoring-adoption-of-artificial-intelligence-and-related-vulnerabilities-in-the-financial-sector/)
- [EBA/EIOPA/ESMA statement on ICT risks from frontier AI (31 July 2026)](https://www.eba.europa.eu/publications-and-media/press-releases/eba-eiopa-and-esma-call-enhanced-governance-and-consistent-supervision-mitigate-ict-risks-frontier)
- [ECB Banking Supervision: Elderson speech on operational resilience in the age of AI (3 June 2026)](https://www.bankingsupervision.europa.eu/press/speeches/date/2026/html/ssm.sp260603~255bec155b.en.html)
- [Federal Reserve: SR 26-2 Revised Guidance on Model Risk Management](https://www.federalreserve.gov/supervisionreg/srletters/SR2602.htm)
- [DORA overview and CTPP designations (secondary)](https://www.regulation-dora.eu/blog/critical-ict-third-party-designations-october-2025)
- [Kyrgyz Republic Law on Personal Information (dpa.gov.kg)](https://dpa.gov.kg/en/npa/4)
- [DLA Piper: Data protection laws in Kyrgyzstan](https://www.dlapiperdataprotection.com/?t=law&c=KG)
- [Eurasianet: Kyrgyzstan embraces self-regulation for AI](https://eurasianet.org/more-carrot-than-stick-kyrgyzstan-embraces-self-regulation-for-ai-development)

## Confidence and gaps

Higher confidence
- OWASP LLM Top 10 2025 item names and IDs (fetched from the OWASP page).
- MCP authorization requirements (fetched from the specification).
- Citi statements and controls (American Banker, July 2025); SR 26-2 existence and scope carve-out (Federal Reserve); ESAs statement date and ECB speech content (fetched from regulator pages); GFT and Lloyds descriptions (fetched pages).

Vendor or self-reported (do not treat as validated)
- All bank productivity figures: Bank of America (20%, 50%), JPMorgan (10-20%), Citi (5-15% for Copilot, 2x-20x for agents, 740,000 reviews / 100,000 hours), Goldman (3-4x), Lloyds ("50% improvement in converting code", from a trade article). None was independently measured.
- Microsoft's 30% MTTR figure, ReliaQuest and AIOps MTTR claims, and the Veracode 45% figure are vendor-produced tests or claims.
- The GFT case reports no quantified results and the bank is unnamed. The CLPS Hong Kong COBOL result is a vendor press release and is not relied on here.
- The Lloyds "200 COBOL applications" is a hypothetical scope used by the COO, not a program size.

Gaps
- No named-bank, quantified case was found for test generation, requirements engineering, AIOps or GenAI in a bank SOC. These rows rely on vendor material or reference architectures.
- The claims "over 30% of significant-bank outsourcing budget on 10 ICT providers" and "over 65% of EU financial entities use two hyperscalers" appeared only in vendor guides and are excluded from the body.
- The BaFin January 2026 point was seen only in a secondary source.
- Kyrgyz specifics were not resolved. No National Bank of the Kyrgyz Republic (NBKR) rule on cloud outsourcing, data location or IT third-party risk was found in English sources, and no Kyrgyz AI statute was found (an AI ethics draft and a self-regulation approach were reported). The Kyrgyz personal data law's localization position is unclear from what was retrieved. Check NBKR acts (likely Russian or Kyrgyz only) and local counsel before deciding hosting. DORA, ECB and EBA material is a method reference, not applicable law.
- Data-platform items (event streaming, evaluation tooling, open-weight versus commercial cost) rest on consultancy or vendor commentary; no bank case with measured results was found.
- The DORA 2025 report's seven capabilities and its throughput figures were not retrieved; only the headline "amplifier" finding and instability caveat were confirmed from secondary summaries and the DORA page.
- This is a desk review of search results and a few fetched pages; several search snippets were not opened at source.
