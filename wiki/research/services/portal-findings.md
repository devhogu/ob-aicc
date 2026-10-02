# Findings: the four concept portals, read for the services of AICC

Recorded 2026-10-02. A reading of the four static portals kept in the repository beside the charter site: `html/financial-services`, `html/cloudlab`, `html/sts`, and `html/csr`. All four call themselves conceptual: the Financial Services framework is labelled a conceptual framework, STS states that it does not establish a current service inventory, CSR states that it is not a claim about current practice, and Cloud LAB is branded as AICC scenario validation. None of them is a record of the Bank. They are read here as a source of service ideas, of constructs for the charter and the portal, and of candidates for the Portfolio of AICC. The convergence is pending; this page records, and [service-ideas.md](service-ideas.md) organizes.

## 1. Inventory

| Portal | Pages | Languages | Completeness | Generator and source |
| --- | --- | --- | --- | --- |
| html/financial-services, "GenAI-enabled Banking and Financial Services Framework" | 76 EN and 76 RU | EN, RU | Broad and deep: about 1,100 scenario cards (S 442, M 609, L 47, XL 7); 319 cards have an empty OKR; two peer frameworks (Enterprise Services, Information Technology) are one-line stubs | `finance-portal/build.py` from `html-alt/financial-services` |
| html/cloudlab, "Cloud LAB: Scenario Hypothesis Validation" | 1 | EN | Complete as one concept page; its own guardrails scorecard shows the gaps | `html-alt/cloudlab`; no build folder found |
| html/sts, "Shared Technology Services Framework" | 8, plus `data/sts-topology.json` | EN | Overview, the reference explorer, and the prototypes 01 and 02 are substantive; the two model pages are thin; prototype 03 is a static stub; the topology has no dependency edges and its contribution map is pending | `sts-portal/build.py` from `html-alt/sts/en` |
| html/csr, "Customer Intelligence-Enabled Service Resolution" | 1 EN and 1 RU, long, 34 diagrams | EN, RU | A complete proposal; its charter fields (baselines, owners) are left to fill | `csr-portal/build.py` from `html-alt/intelligent-customer-service-resolution` |

## 2. What each portal is

### 2.1. Financial Services framework

A uniform map of the whole Bank for executives and AI planners, with the stated aim of adopting generative AI as an enabler across every aspect of banking. Regulation is framed for Kyrgyzstan, Kazakhstan, and Russia. The home page groups eight concern areas under posture labels: Strategic Banking Portfolio (operating state), Strategic Initiatives and Transformation (change state), Operational Value Streams (primary value chain), Customer and Market Intelligence (analytics), Customer and Channels (operations), Risk and Control (control), Shared Banking Capabilities (operating engines), Finance and Treasury (financial control), and Banking Data and Analytics (foundation).

Four page types: a concern page with four problem lenses (Insights and analytics, Enablement, Automation, New business opportunities), cards for its sub-areas, a Cycles card, and cross-cutting scenarios; a sub-area page with the lenses and four to six topics of three scenarios each; a cycle page with four or five governance cycles drawn as stage chevrons, the lenses Analyze, Optimize, Automate, Enrich, and scenarios; and a value streams page that opens with the lean problems (waste, variability, overload, quality at source) and draws eleven flows as stage chevrons with a modal for each stage.

The unit of content is the scenario card: lens, complexity (S to XL), intent, problem to solve, solution, and an OKR of one objective and the key results Adoption, Acceptance, and Cycle. Every scenario has an identifier of the form `urn:financial-services:scenario:...`. The scenarios follow one pattern: an agent drafts or analyzes, and a person signs off.

Worth keeping from its UX: the home page as a capability map with counts; stage chevrons with modals; an expandable lens, scenario, intent, and complexity table; the problem-lens tab table; the EN and RU toggle on every page.

### 2.2. Cloud LAB

One page that describes a permanent sandbox for generative AI exploration: production data reaches it through read-only extracts into a cloud account, agentic workflows are built and validated there, and each is promoted toward production or shelved. Its parts: a six-stage flow (Define Scenarios, Establish Cloud Lab, Choose Scenario, Prepare Data, Agentic Workflow, Validate) crossed with five concerns (Governance and Decisions, Risk and Controls, Operations and Processes, Data and Analytics, Observability), giving a grid of 41 activity cards with a detail panel; a "Dual Operating System" of human governance (strategic direction to sense-making) and agentic intelligence (continuous sensing to closed-loop learning); seven verbs of business agility (Analyze, Reason, Decide, Act, Learn, Govern, Engage); an "Intent Loop" of Intent, Insight, Action, Audit; stage notes; and a governance guardrails scorecard of twenty guardrails with a coverage bar each, among them Sandbox Isolation 90 percent, PII Protection 85 percent, Promotion Pathway 45 percent (an informal handoff), Failure Protocol 30 percent, Operational Lifecycles 25 percent, and Disagreement Protocol 20 percent (not formalized).

Worth keeping: the stage by concern grid with a detail panel, the expand-map control, the light and dark theme, and the scorecard bars.

### 2.3. Shared Technology Services framework

A service-management explorer for running shared technology platforms as managed services. Two navigation groups: Models and reference (Overview, Operating model, Managed service, Industry reference) and Prototype lab (Control plane, Portfolio lifecycle, Portfolio view). The home page draws a lifecycle of seven states grouped as Onboarding, In service, and Transition: Candidate, Admitted, Catalogued, Active, Improving, Transition Planned, Migrating.

The outer model, "STS Operating Model", has five domains: Service Portfolio and Adoption; Ownership, Governance, and Standards; Platform and Automation Enablement; Operations, Reliability, and Assurance; Portfolio Economics and Improvement. The inner model, "STS Managed Service Model", has five: Service Definition, Consumer Interface, Delivery Structure, Runtime Structure, Control and Learning. Both pages are a five-domain breakdown only. The reference explorer presents the ITIL service value system and value chain, the IT4IT digital product lifecycle, three practice groups and 34 practices, four journey lenses, and fourteen guidance questions.

Of the prototypes, 01 "SPOM as a portfolio control plane" is interactive, with a service front door, an admission policy, an assurance gate, a portfolio state store, an API, a scheduler, controller loops, and health signals, and four example managed services (CI/CD, database, observability, identity integration). 02 "Managed Service Portfolio Lifecycle" is the richest: for each state it gives input, requirements, and transition, then a control flow of required state, assessment, validation, decision, crossed with five portfolio lenses (catalog and adoption, governance and ownership, operations and reliability, risk and assurance, economics and roadmap), each with a question, signals, and an action. 03 is a static mock-up of labels. The topology file is a typed graph of nine node types and 72 containment relationships with flow edges that carry an edge basis and a status; it asserts no edge until a basis is recorded, which is a discipline worth keeping. AI is not mentioned anywhere in STS.

### 2.4. Customer Intelligence-Enabled Service Resolution

A proposal to resolve repeat and stalled customer requests with governed generative AI that assists employees, addressed to the head of customer service, the process owners, and the CTO. Five parts: the business use case; candidate charters for three journeys (Payment Issue Resolution, recommended first; Card Dispute Progress Support; Onboarding and KYC Progress Support), with loan application status and complaint resolution listed as further candidates; a technical pilot blueprint; journey technical profiles; and a platform capability and readiness map. The front door is an eight-stage case map from contact intake to closure, each stage pairing the service work with the proposed assistance and an accountable process role, followed by a learning loop of quality and improvement.

Its content model is the most charter-like of the four: a charter per journey, a RACI, a decision structure, evidence sizing (200 to 500 historical cases, at least 100 live cases, 1,000 to 3,000 for an outcome claim), zero-tolerance control limits, a capability disposition per platform capability (reuse, extend, pilot-local, narrow-block), and a pilot-to-platform evolution with the rule that a capability becomes shared only when it has another committed consumer and a named product owner. It names a minimum reusable AI foundation: model gateway, model and prompt registry, governed retrieval, evaluation service, safety controls, workflow runtime, tool broker, observability, a use-case registry that carries a risk tier, and suspension controls; and a ten-step validation progression from silent evaluation to limited-authority action.

## 3. Services and use cases stated or implied

### 3.1. Financial Services framework, by domain

| Domain | Representative scenarios |
| --- | --- |
| Finance: FP&A, performance, close, tax | CFO ad-hoc financial question answering; finance production calendar sequencing; budget assumption quality scan; ICAAP and budget consistency check; in-period variance flash; close narrative drafting; GL reconciliation break triage; RAROC and EVA attribution; transfer pricing local file; FATCA and CRS submission validation |
| Treasury, ALM, capital | ALCO rate-scenario pack; NII and EVE driver decomposition; FTP curve backtesting; daily LCR and NSFR monitoring with commentary; contingency funding plan stress analysis; CET1 headroom projection; ICAAP narrative drafting; intraday liquidity copilot |
| Regulatory reporting and data | COREP and FINREP data quality validation; submission pre-dispatch quality gate; BCBS 239 lineage gap detection; supervisory query response knowledge base; data residency compliance check |
| Risk | CRO risk synthesis; watchlist dossier assembly; ECL provision narrative; VaR backtesting pack; incident notification drafting; threat intelligence briefing; KRI breach alert; financed emissions calculation; validation report drafting |
| Model risk and AI governance | Shadow model identification scan; model inventory and documentation completeness check; model performance deterioration alert; validation schedule re-prioritization; validation findings synthesis |
| Compliance and financial crime | AML alert investigation pack; suspicious activity narrative drafting; sanctions false-positive triage; false-positive rule analysis; examination readiness; license renewal pack |
| Internal audit | Audit universe risk ranking; dynamic audit plan re-ranking; workpaper pre-population; remediation evidence quality check |
| Channels | Agent real-time knowledge assist; post-call documentation; complaint triage and classification; IVR containment and routing; relationship manager meeting brief; onboarding abandonment recovery; ATM cash load optimization; open banking API compliance monitoring; incident postmortem drafting |
| Customer intelligence | Contact root-cause intelligence; repeat-contact and poor-outcome correlation; NPS driver decomposition; voice-of-customer to backlog mapping; at-risk scoring; next-best-offer prioritization; salary-switch risk alert; competitor move brief; sentiment crisis alert |
| Shared operations and servicing | Frontline service copilot; interaction summarization; KYC extraction and CDD classification; underwriter application synthesis; covenant monitoring; nostro reconciliation commentary; payment investigation triage; legal referral triage; research note drafting; vendor performance review pack |
| Product value streams | Dispute resolution automation; credit decision copilot; client review pack; policy lapse early warning; FX corridor exception analytics; lifecycle stage agent execution |
| Strategy, portfolio, and change | Board strategic narrative drafting; integrated what-if engine; whitespace detection; steering committee pre-read synthesis; benefit realization trajectory; due-diligence cross-workstream synthesis; TCFD report drafting |
| Innovation management (mirrors AICC) | Pipeline screening synthesis; stage-gate review synthesis; hypothesis design review; MVP test results interpretation; portfolio kill recommendation; experiment knowledge accumulation; innovation P&L attribution |
| Data foundation | Data quality remediation; enterprise data self-service; catalog auto-enrichment; golden record deduplication; customer 360 assembly; end-of-day price validation gate |

### 3.2. Cloud LAB, the lab services it implies

Scenario intake and sponsorship (commitment, scenario identification, prioritization from a validated backlog); sandbox provisioning (account registration with vendor sign-off, IAM and policies, isolation, setup); data preparation (read-only extracts, data ownership, PII assessment, export rules with no write-back, extract and quality control, data quality metrics); agentic build (architecture selection, workflow build, data and analytics flows, guardrails for drift, bias, and grounding); validation (hypothesis OKRs, scenario metric, benchmarking against baseline and cost, acceptance criteria, data correctness, stakeholder demo); promotion (promote or discard to an on-premises lab or the shelf, adoption guidelines).

### 3.3. STS, technology operations and service management

Managed shared services named: CI/CD platform, database platform, observability, identity integration. Portfolio services implied: service intake through a front door, admission and assurance gates, catalog publication, health signals (service levels, incidents, adoption, cost), an improvement backlog, transition and migration management. A practice vocabulary of 34 ITIL practices, among them service catalogue, service level, incident, problem, change enablement, knowledge, portfolio, service financial, and supplier management.

### 3.4. CSR, servicing, customer intelligence, and the AI platform

Employee assistance at each of the eight stages of a case: detecting related contacts, proposing routing, an evidence-linked timeline, blocker diagnosis, the permitted next step, a grounded explanation draft, a structured closure record, aggregation of failure patterns. Platform components: a purpose-bound customer context service, a limited-authority service resolution assistant, a service resolution workspace, a tool catalogue of ten tools, and the minimum reusable AI foundation named in 2.4. Strategic path: pilot, then an enterprise AI and agentic workflow platform, then a customer intelligence and action platform.

## 4. Constructs worth absorbing

| Construct and source | What it adds | Where in AICC |
| --- | --- | --- |
| Problem lenses and five-lens scenario typing with S to XL complexity (Financial Services) | One way to classify demand and to catalogue use-case ideas | Portfolio funnel; Knowledge base |
| Scenario card: problem, solution, OKR with Adoption, Acceptance, Cycle (Financial Services) | A template for the hypotheses and leading indicators of an Initiative Brief | Portfolio; Delivery |
| Domain map and cycle catalogue with stage chevrons (Financial Services) | A heat map of opportunities by Domain, against which Engagements are placed | Services; Knowledge base |
| Stable identifiers for every node (Financial Services, STS) | Links between registry, portal, and Solutions that survive renaming | Knowledge base; Registry |
| Six-stage by five-concern validation grid (Cloud LAB) | A concrete Experiment workflow with activities per concern | A Lab page or section; Delivery |
| Guardrails scorecard with coverage (Cloud LAB) | A visible readout per concern, which can feed the Maturity Level evidence | Lab; Governance and oversight |
| Dual operating system and intent loop (Cloud LAB) | A human-oversight narrative: decision rights remain with people | Responsible AI; Lab |
| Seven-state managed-service lifecycle with the required state, assessment, validation, decision flow and five lenses (STS) | A finer model of a Service after go-live, with gates per state: Operate, Evolve, Retire become Admitted, Catalogued, Active, Improving, Transition Planned, Migrating, each with its question, signals, and action | Delivery (Solution Lifecycle Model 8); the operation of the Services of AICC |
| The ITSM practices applied to the Services of AICC (STS): request and incident handling by class of service, problem management, change enablement, knowledge, service level, service financial management, supplier management | The operating processes behind "support through Service Management" and the response targets of the Service Agreement, which the charter names and does not yet describe | Delivery; a run-book of the Services of AICC in the Knowledge base |
| Health signals per Service: service levels, incidents, adoption, cost (STS) | The live review of a Service at the Iteration Review and Demo made concrete, and the input to the sunset rule | Delivery; Governance and oversight |
| Transition and migration states (STS) | The hand-over of a proven Solution to a platform team or IT as a managed state with its own gate, which is the pilot-to-platform offer | Delivery; Assurance and governance support |
| Portfolio control plane: front door, admission policy, state store, scheduler, controller loops, health signals (STS) | Maps onto intake, the AI Registry, Envelopes and Guardrails, and the health review | Portfolio |
| Outer and inner models (STS) | Separates how the portfolio is run from how one Solution is decomposed | Services; Knowledge base |
| Typed topology with edge basis and status (STS) | Evidence-led linking: no edge without a recorded basis | Knowledge base; the data layer of the portal |
| Charter template, evidence sizing, zero-tolerance control limits, "each step leaves an owned reusable asset" (CSR) | Concrete acceptance and evidence rules for an Engagement | Delivery; Portfolio |
| Capability disposition (reuse, extend, pilot-local, narrow-block) and the promotion rule (CSR) | An objective test for Experiment to Product to Service, and for the growth of the AI Platform | Services; Lab |
| Ten-step validation progression from silent evaluation to limited-authority action (CSR) | Exposure gating that maps to the Risk Tiers | Delivery; Responsible AI |

## 5. Overlaps and contradictions with the charter

- Lifecycles. The innovation stage-gate of the Financial Services framework (ideate, screen, pilot, scale, industrialize) overlaps the portfolio Kanban in other terms. The STS states refine the Service Stages Operate, Evolve, Retire (Improving matches Evolve), and STS has no Retire state.
- "Service" means three things: a shared technology platform in STS, an offering type that AICC runs in the charter, and a bank function ("capability") in the Financial Services framework, which is not the Capability of the Solution Lifecycle Model.
- "Control loop" and "Steering" differ: STS controller loops compare desired with observed state; the charter's control loops are plan, do, check, act cycles run at Steering; the Cloud LAB intent loop is a third model; the "steering cycles" of the Financial Services framework are the strategic steering of the Bank.
- Risk Tiers. The Financial Services framework classifies by complexity and has no Risk Tier; Cloud LAB has a per-scenario risk envelope and a lab risk register; only CSR aligns, with a use-case registry that carries a risk tier confirmed against the Bank's AI risk classification.
- Decision rights. Cloud LAB has the sponsor and the IT lead authorize promotion, and its disagreement protocol is not formalized; the charter requires business acceptance by the Domain Owner or the Executive Sponsor, validation by the Control Function Contacts for Risk Tier 2 and 3, and a separate release decision. The cloud sandbox of Cloud LAB would pass the provider check of AI Policy 4.1.
- CSR as an Engagement. It maps onto an Engagement with customer service as the client function, its charter onto an Initiative Brief and a Service Agreement, its pilot onto the MVP, and its "pilot approval does not authorize broader rollout" onto the separate release decision. It uses "project" and "charter" against the Vocabulary, and its roles (journey process owner, benefit owner, measurement owner, service quality lead) have no direct equivalents beside Domain Owner, Domain Expert, and product owner. Its reusable foundation duplicates the AI Platform of the Statement of Intent, and its use-case registry duplicates the AI Registry; consistent, but the ownership needs reconciling.
- The Model risk sub-area of the Financial Services framework overlaps the AI Registry and the validation gates.

## 6. Candidates for the Portfolio of AICC

Recorded for the convergence, not decided. CSR is a ready Engagement candidate with customer service as the client (Payment Issue Resolution first). Cloud LAB is a candidate for the Lab of AICC and for the Experiment workflow, subject to the provider check and to the decision rights of the charter. The Financial Services scenarios are a use-case backlog by Domain for the funnel, to be screened by the lenses and the Strategic Priorities; its innovation-management and model-risk scenarios apply to AICC itself. STS is about the service management processes: how a service is admitted, catalogued, operated, improved, and transitioned, and the practices that carry it (incident, request, problem, change enablement, knowledge, service level, service financial, supplier). It has no AI content, and that is why it matters to AICC in a different way than the other three: it is the source for how AICC operates the Services it runs (Business Model 4.2: requests and incidents through the Service Management queue, response targets in the Service Agreement), for the gates of the delivery life cycle (Solution Lifecycle Model 7 and 8), and for the hand-over of a Solution to the platform teams and IT (Transition Planned, Migrating). Its seven states and its per-state control flow of required state, assessment, validation, and decision are the finest model in the four portals of the life of a Service after go-live.
