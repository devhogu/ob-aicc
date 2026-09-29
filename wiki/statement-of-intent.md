# AICC Statement of Intent

Status: **DRAFT** for AICC leadership review. Not approved policy.
Evidence base: [industry research](industry-research.md).

## Purpose

The AI Competence Center (AICC) makes generative AI a safe, governed, everyday part of how O!Bank works. We move the bank from isolated pilots to one bank-native AI layer that staff, engineers, and eventually autonomous agents share.

## Principles

1. **Governed by default.** Every AI system is inventoried, owned, risk-tiered, and auditable before it reaches production. AI sits inside the bank's existing risk, model-risk, third-party, and information-security frameworks.
2. **Human accountability.** People own outcomes. Humans review high-stakes decisions such as credit, AML/SAR, and customer-impacting actions.
3. **Grounded in bank knowledge.** Answers come from approved, current, traceable bank sources and cite them.
4. **Measured value.** Each initiative has a baseline and a measured result. We report adoption and outcomes, not activity.
5. **Data stays protected.** Data classification and residency rules decide which data may reach which model, and where it runs.
6. **Build once, reuse everywhere.** Shared platform components come before one-off solutions.

## Four commitments

### 1. Workdesk adoption
Give every employee a safe AI assistant for daily work: drafting, summarising, search, analysis, translation. Pair it with role-based training, usage guidelines, and a simple way to request new use cases.
*Industry signal:* large banks run internal LLM assistants across their workforce (for example, JPMorgan's LLM Suite).

### 2. Knowledge bases
Turn policies, procedures, product rules, and regulations into governed, searchable knowledge with named owners, review cycles, and access control. Grounded retrieval with source citations is the standard.
*Industry signal:* Morgan Stanley's advisor assistant over about 100,000 documents, reported at over 98% adoption in advisor teams. The critical factor was retrieval quality and evaluation.

### 3. Routine-operations automation
Automate document-heavy, rule-bound work such as onboarding and due diligence, case preparation, reporting, reconciliation, and customer-request handling. Start with human review, and relax it only as measured evidence supports.
*Industry signal:* ING's GenAI due-diligence reports save about two hours per client across its markets.

### 4. Software development
Make AI a standard part of the engineering lifecycle: coding assistants, code review, testing, legacy-code understanding, and documentation. Add coding agents under review controls once assistants are established. Track delivery outcomes and quality, not code volume.
*Industry signal:* banks report roughly 10–20% developer productivity gains from assistants (JPMorgan, Goldman Sachs, Bank of America). Reports are self-measured and not comparable.

## Priority functions

The four commitments apply to every function. These functions are high priority, and each has a research page with use cases, target state, adoption path, risks, and metrics.

| Function | Intent | Human decision points | Page |
|---|---|---|---|
| Board and executive committee | Board-level focus. Sourced intelligence for directors: pack synthesis, KPI and risk drill-down, peer and competitor view, parent and investor reporting. Board oversight of AI itself: AI inventory, risk appetite, director literacy | Directors decide. Board materials never go into public tools | [Board and governance](functions/board-and-governance.md) |
| Investor relations | Give IR on-the-spot intelligence for the Board and investors (ALGA Group): question forecasts with sourced answers, peer comparison, consistency checks across materials, drafted results materials | Disclosure committee sign-off. MNPI controls. Every public number tied to a locked source | [IR and FP&A](functions/ir-and-fpa.md) |
| FP&A | Monthly and quarterly packs, driver commentary, forecasts and scenarios, ALM and cost-of-risk analytics, peer and operational benchmarking, natural-language access to one governed finance data layer | Analysts approve commentary. Numbers come from queries, not from the model | [IR and FP&A](functions/ir-and-fpa.md) |
| Compliance | Regulatory change mapped to an obligations register, cited policy assistant, AI-assisted controls testing and reporting | Compliance and Internal Audit decide on results | [Compliance and KYC](functions/compliance-and-kyc.md) |
| KYC end to end | Onboarding with liveness and deepfake detection, continuous screening, CDD and UBO assembly, perpetual KYC, immutable case records | Rejection, exit, PEP and EDD stay human. The risk score is deterministic, and the LLM only drafts the narrative | [Compliance and KYC](functions/compliance-and-kyc.md) |
| AML and fraud | Alert triage with reasons, pre-built case packs, STR drafts with citations, shared fraud and AML signals | The MLRO reviews and files every STR | [Compliance and KYC](functions/compliance-and-kyc.md) |
| HR | One multilingual employee assistant, AI literacy for all staff, recruiting support | Hiring decisions are always human. Any candidate ranking is advisory and bias-tested | [HR and accounting](functions/hr-and-accounting.md) |
| Accounting | Touchless invoice matching and routine reconciliations, drafted journals and commentary, faster close | Named preparer and reviewer approve entries. IFRS and tax judgement stay with qualified staff | [HR and accounting](functions/hr-and-accounting.md) |
| Loans (retail, SME, corporate) | One credit workbench: document extraction, memo drafting, covenant and early-warning monitoring, collections support | Approvals and declines come from a validated engine plus a human approver. Applicants can request review | [Lending and insurance](functions/lending-and-insurance.md) |
| Insurance | Bancassurance offers in customer journeys on insurer-approved text, claims intake and triage with the partner insurer | The insurer keeps underwriting and claims decisions | [Lending and insurance](functions/lending-and-insurance.md) |
| Customer support | Copilot for every agent, tier-1 assistant in app and messaging, Russian and Kyrgyz support at measured quality | A customer can always reach a human | [Service, operations, front office](functions/service-operations-front-office.md) |
| Operations | AI-prepared cases for disputes, trade documents, account maintenance, and KYC files | Humans approve exceptions and anything that moves money | [Service, operations, front office](functions/service-operations-front-office.md) |
| Customer front office: retail, SME, corporate sales | Client briefs before meetings, drafted summaries and CRM entries, next-best-action from the bank's own data, consent-aware marketing | Staff own the client relationship and advice | [Service, operations, front office](functions/service-operations-front-office.md) |
| IT and banking systems | AI in the full delivery lifecycle, legacy documentation and modernization, AI-assisted incident handling and SOC, the platform foundations below | Humans own merges, releases, and containment actions | [IT and banking systems](functions/it-and-banking-systems.md) |
| Risk management | Credit, market, liquidity, and operational risk analytics, early warning, stress testing support, model risk including validation of AI models | Risk owners decide. Validated models and human approval for material decisions | [Risk and treasury](functions/risk-and-treasury.md) |
| Treasury and ALM | Liquidity and deposit forecasting, cash and FX management, market commentary, treasury operations | Dealers and the ALCO own positions and limits | [Risk and treasury](functions/risk-and-treasury.md) |
| Legal and corporate secretary | Contract review, policy drafting, regulatory tracking, legal research | Lawyers verify every citation and sign off. Privilege and confidentiality rules apply | [Board and governance](functions/board-and-governance.md) |
| Internal audit | AI-assisted audit planning, population testing, evidence review, and audit of AI systems | Auditors form the opinion | [Board and governance](functions/board-and-governance.md) |
| Marketing, product, digital channels | Consent-aware personalisation, content in Russian and Kyrgyz, in-app assistant, product analytics, customer insight, competitor intelligence | Marketing compliance approves campaigns. Consent is enforced in code | [Marketing, product, ecosystem](functions/marketing-product-ecosystem.md) |
| Payments, cards, ecosystem | Ecosystem cross-sell, merchant and SME services, agent-initiated payment readiness | Customers authorise payments | [Marketing, product, ecosystem](functions/marketing-product-ecosystem.md) |
| Procurement and administration | Contract lifecycle and vendor management, facilities, cash logistics support | Budget owners approve spend | [Corporate services, data, AICC](functions/corporate-services-data-and-aicc-operating-model.md) |
| Data office | Data quality, governance, lineage, and self-service analytics that every AI function depends on | Data owners approve access | [Corporate services, data, AICC](functions/corporate-services-data-and-aicc-operating-model.md) |
| AICC itself | Use-case intake, prioritisation, ROI measurement, AI champions network, vendor and model selection | AICC leadership and the Board committee approve the portfolio | [Corporate services, data, AICC](functions/corporate-services-data-and-aicc-operating-model.md) |

Further functions are added as pages under `functions/` when needed.

## Destination: the bank's agentic platform

One uniform layer that makes AI native to bank operations. It grows out of the four commitments rather than replacing them. Its building blocks:

| Layer | Role |
|---|---|
| Model gateway | One controlled access point to models, with routing, cost control, and data-protection policy |
| Knowledge layer | Governed retrieval over bank knowledge, shared by all assistants and agents |
| Tool gateway (MCP-style) | Standard, permissioned access from agents to bank systems and APIs |
| Agent registry | Every agent's owner, scope, data access, and risk limits |
| Guardrails and policy | Enforced permissions, limits, and deterministic checks before actions execute |
| Human-in-the-loop | Approval points for high-stakes actions, on channels the agent cannot influence |
| Observability and evaluation | Full audit trail, domain-specific evaluation, monitoring, and lineage |

## Sequence

1. **Foundation:** governance, AI inventory, data classification rules, secure model access, first assistant, initial knowledge bases.
2. **Scale:** workforce rollout, engineering adoption, first automated operations flows with human review.
3. **Platform:** shared gateways, registry, and guardrails. Agents take on bounded operational tasks.
4. **Agentic bank:** agents integrated into core operations under continuous evaluation and human oversight.

Timing and scope belong in the roadmap, not here.

## Success measures (to be baselined)

- Share of staff actively using approved AI tools
- Knowledge coverage: share of key processes with an owned, current source
- Hours saved and cycle-time change in automated operations flows
- Engineering delivery metrics: cycle time, review time, defect rate
- Share of AI systems inventoried, tiered, and reviewed
- Incidents and escalations per use case

## Open items for leadership

- Local regulatory position: no National Bank of the Kyrgyz Republic (NBKR) rule on bank AI use was found. Data localization and cross-border transfer for AI hosting are unclear and need local counsel. See [industry research](industry-research.md).
- Kyrgyz and Russian language quality: unmeasured for most use cases. Test per language before customer-facing use.
- Confirm the listing venue and reporting duties to investors (ALGA Group). IR AI work is scoped at Board level: sourced intelligence for the Board and IR, with disclosure controls. Ownership details from web search are unverified.
- Function priority order: which of the functions above goes first.
- Approved model providers and hosting: cloud, local, or hybrid, given data residency.
- Audience and classification of this document.
- Ownership: who chairs AI governance and approves use cases.
