---
key: "technical-design"
label: "Technical design"
section: "Technical"
---

## Technical design {#technical-design-page}

This page describes what the pilot builds, so that IT can estimate it and the Control Function Contacts can test it. It explains section 3 (architecture and data) of the Solution Definition; the full design is kept in the architecture repository of the Competence Center, and product and framework choices go to the Decision Log. It names no systems, figures or data of the Bank. What the pilot asks of IT is on the [IT readiness checklist](#it-readiness); what differs by journey is in the [journey technical profiles](#journey-profiles). The design is journey-neutral: Payment Issue Resolution is the technical recommendation, subject to the journey selected at the business case.

### Summary for approvers {#technical-design-summary}

| Question | Position |
| --- | --- |
| What is built | One assistant for one service journey and one service team. A customer context service brings the customer's contacts, cases and status together; a fixed workflow asks an AI model to summarize them and propose a next step; a workspace panel shows the result to the employee, who decides and acts. |
| What the assistant may do | Read the context the workflow gives it and return structured output: a timeline, the likely blocker marked as an inference, the procedure with its source, a next step from the approved action list, and draft wording. |
| What it may not do | Hold tools or write anything; establish identity, status, eligibility or deadlines; move funds, change a case state, take a regulated decision or send anything to a customer. Every write is the employee's action in the workspace. |
| Expected Risk Tier | 2: customer personal data; the output informs the employee's decision and reaches the customer only after review. A model holding write tools would make it Tier 3. |
| Where the model runs | In the Bank. An external model only after the provider check and approval for the data class; introducing one later is a significant change (see [Deployment and model route](#technical-design-model-route)). |
| Phases | 1: an Experiment in the Lab on read-only extracts, ending in an Outcome Report. 2: the first Solution, a Service run by the Competence Center with a sunset rule, deployed to its first users (one service team) after validation, Team final acceptance and the Bank's change management. |
| Who builds, tests, approves | The Competence Center Lead builds as Solution Engineer; a person other than the builder tests and checks (Operating Model 4.4); the Executive Sponsor approves the Solution Definition and the use of the data class. |
| Asked of IT | Read access to the journey's sources, an in-Bank model route, environments, logging, support and change: see the [IT readiness checklist](#it-readiness). |
| Effort, time-box, cost | [Competence Center Lead's estimate: effort by Role, Iterations per phase]; [Competence Center Lead's estimate: run cost and model cost per case, with source]. The cost limits per case go to the Conditions of use. |

### Where generative AI adds value {#technical-design-genai-value}

Generative AI (GenAI) is used for work that is hard to write as stable rules: interpreting fragmented contact notes, chats, cases and complaints, in Russian, Kyrgyz or mixed text; reconstructing a short timeline; telling the current need apart from earlier requests; explaining the likely blocker; applying the relevant approved procedure; proposing a permitted next step; and drafting a source-grounded explanation for the employee's review.

GenAI does not establish customer identity, payment status, eligibility, deadlines, permissions, or transaction outcome. Those remain facts and decisions supplied by authoritative banking systems and approved policy. This sentence goes into the Conditions of use of the Solution Definition.

### Architecture {#technical-design-architecture}

| Component | Responsibility |
| --- | --- |
| Banking systems | Hold the facts and run the Bank's processes. The pilot reads them and changes nothing in them. |
| Customer context service | Builds the minimum authorized view for the journey: linked records, a timeline, a source reference for each value. It is not a customer 360. |
| Assistant: fixed workflow, AI model behind the AI gateway, knowledge retrieval | The workflow calls the read services and the retrieval, sends the context to the model and checks its structured output. The model calls nothing and writes nothing. |
| Workspace | Shows the result beside the service desktop. The employee accepts, corrects, rejects, investigates or escalates, and acts. It sends nothing on its own. |
| Decision and outcome record | Keeps the AI's contribution, the employee's decision and the outcome in the pilot's own store. Nothing is written back to the Bank's systems. |

For each case: the employee opens an eligible case; the workflow checks the employee, purpose and eligibility, reads the sources and retrieves the procedure; the model returns structured output through the AI gateway; the workflow checks schema, citations and the action code against the approved list. If a check fails, a required source is missing or two sources conflict, no proposal is shown and the case follows the manual route. The employee then acts, and the record keeps what the AI proposed and what the employee decided.

### Information paths {#technical-design-information-paths}

- **Historical extracts in the Lab (phase 1).** Read-only extracts enter the Lab, each with its source owner and class. They become historical cases for building, evaluation and the baseline. Personal data is minimized and assessed with the data protection Contact first. Nothing is written back.
- **The live read path (phase 2).** After validation, read interfaces or adapters fetch the current state when an eligible case is opened. Each value carries its source and freshness. Missing, stale, conflicting or mislinked information is shown as an exception and follows the existing manual route.

The sources are the customer master or CRM, the journey system, the case system, contact platforms, complaints, knowledge repositories, identity services and management information; each keeps its authority, and only the fields the journey needs are read. Integration rules: versioned contracts, so that model, workflow, workspace and adapters can be replaced separately; journey logic kept in the Solution; snapshots for evaluation, never as a live source of truth; no model access to core databases, credentials, message buses or open search; source references kept from context to outcome.

**Assumptions to confirm in discovery, each with its fallback:**

- no read interface: a scheduled extract for the Lab, and a narrower live scope;
- no shared customer key: an approved matching rule, with uncertain matches quarantined;
- no step timestamps in the case system: handling effort from another named source, or that measure dropped;
- records in Russian, Kyrgyz, mixed or transliterated text: the Evaluation set covers each language in use;
- voice calls: out of the pilot, with no transcription;
- no deep links: the record reference is shown instead.

### Customer context service {#technical-design-context-service}

A journey-specific service. It links customer, journey event, open case and related contacts by the Bank's identifiers; normalizes them into one timeline of service events; keeps facts, calculated values and inferences apart; applies purpose, role, field and retention restrictions; gives the source, time, freshness and owner of each value; and produces a reproducible snapshot for every model call and employee action. Each event holds its identifiers, source record, type and business time, status or reason code, owning queue, access class and freshness. Inferences are stored apart, with their evidence, model and prompt version and expiry, and never become customer facts. The pilot's outputs serve only service resolution and the evaluation of the assistant.

### The assistant and the employee's actions {#technical-design-assistant}

The assistant is an Assistant in the corpus sense: it drafts for the employee and takes no action beyond its output. It is one fixed workflow, not an open loop. The workflow enforces a fixed sequence and step limit; schemas for requests and responses; time, call and cost limits per case; citation checks; separation of facts and inferences; a rule-based stop on missing or conflicting sources; a manual fallback at every failure; and the employee's decision before any communication or action. The workflow engine is a Team decision in the Decision Log; the model, prompt and retrieval versions are attached to each case trace. No agent protocols are used: there is one workflow and no AI agent.

#### Functions and who uses them {#technical-design-functions}

| Function | Used by | Effect |
| --- | --- | --- |
| `get_customer_service_context`, `get_journey_status`, `get_related_contacts`, `get_open_case`, `get_applicable_procedure`, `get_permitted_actions` | the workflow | read only, within the journey profile |
| Timeline, likely blocker, next step (an action code), draft explanation, draft case note, prefilled referral | the model, as output | none outside the workspace |
| Record the decision and feedback; record the service outcome | the employee, by a click | write to the pilot store |
| Create a specialist referral; save the case note | the employee, after review | write through the existing interface, or by hand where none exists |
| Explain to the customer | the employee, in their own words or by sending an edited draft from the existing channel | the Solution sends nothing |

No function moves or reverses money, changes an authoritative journey state, makes a regulated decision, determines reimbursement, alters fraud, anti-money-laundering or sanctions state, or sends an unreviewed customer message. Each journey profile may only remove items from this list.

**Workspace.** A side panel in the service desktop, or a separate screen if the desktop cannot be extended. It shows the customer's request; what happened, with evidence; the verified current state; the likely blocker, marked as an inference; the applicable procedure; the permitted next step; the suggested explanation, marked as drafted by AI; the record references; and the employee's decision. It offers no open chat.

### Deployment and model route {#technical-design-model-route}

| Option | Use | Before Bank data reaches it |
| --- | --- | --- |
| In-Bank model on existing internal serving | Lab and live (default) | provider check of an in-Bank or open model (AI Policy 4.4); license recorded (ARC-006); approval for the data class |
| New in-Bank model serving | Lab and live, if no internal serving exists | the same, sized from the Lab measurements ([capacity observations](#it-readiness-capacity)) |
| External managed model | live only, never in the Lab | provider check by information security, data protection and legal (AI Policy 4.1, 4.3); approval for the data class; EXT-001 and EXT-002 confirmed by the Contacts |

The AI gateway lets the Bank change the model later; every change of model, version or route is a significant change. Workspace, workflow and context service run on ordinary application servers; graphics processors are needed only for model serving.

Operating the Service in phase 2:

- three environments: the Lab, non-production test, production; infrastructure as code, managed secrets, a workload identity;
- one trace per case from request to outcome; alert levels for performance, drift, the human override and correction rate, incidents and cost, each with who watches it (ARC-008);
- fallback to the context-only view or the manual route is always allowed; a second model route only if validated beforehand and named in the Solution Definition; no automatic failover;
- the first users are named in the Solution Definition; widening them is a Domain Owner decision, never automatic;
- rollback under the Bank's change management; an AI Incident goes through the Bank's incident management, with the Competence Center Lead told; a tested suspension control that keeps the record of use (PLT-005, ARC-002).

### Engineering and test approach {#technical-design-engineering}

Code, infrastructure, prompts, schemas, retrieval settings, knowledge versions and evaluation data are versioned. Tests are built with each component; a person other than the builder runs them, and the result is referenced in each Feature (Solution Lifecycle Model 7.1).

| Test layer | What it shows |
| --- | --- |
| Unit, interface and contract | rules, schemas, redaction and workflow steps work; contracts stay compatible and enforce authorization |
| Data quality | identifiers, status mappings, freshness, exclusions and quarantine work |
| Retrieval | the effective source is returned; stale, restricted and irrelevant sources are handled |
| Model evaluation | factual support, interpretation, next step, abstention and draft quality meet the acceptance criteria, in each language of the records |
| Workflow path | allowed paths and limits hold; the model holds no function |
| Bias and error | no materially different treatment across relevant customer groups, before the first deployment to real users or data and in monitoring |
| Security | prompt injection through customer messages, exfiltration, cross-customer access and open components are resisted |
| Resilience | source failure, degraded mode, recovery, latency and suspension work |
| Expert review | Domain Experts confirm representative states and exceptions, as evidence for the Evaluation set |

A failed mandatory test stops the Feature at Verify. Deployment follows the Bank's change management, with the change ticket and test result; nothing is promoted automatically. A changed model, prompt, corpus, mapping or workflow runs its regression set, and the Competence Center Lead decides whether it is a significant change needing a new validation.

### Data and evaluation assets {#technical-design-evaluation}

Three separate assets, owned by people who did not build the Solution: development cases; locked acceptance cases, unseen during building, which form the Evaluation set agreed with the Domain and labelled by Domain Experts; and monitoring samples from live cases, within the purpose approved for the data class. Historical cases are pseudonymized so that the links between customer, event, contact and case stay realistic; dates are shifted only where process order stays valid. Free text in Russian or Kyrgyz is hard to pseudonymize fully; where it cannot be done reliably, identifiable data stays in the Lab under the data protection Contact's sign-off, and any re-identification mapping stays outside it. Each case records the source state, expected interpretation, permitted action, procedure, exclusions and the expert's reasons.

| Mode | Employee receives | Question | Compared |
| --- | --- | --- | --- |
| Existing process | current systems and procedures | what is the baseline? | live, against the first users |
| Context-only view | linked facts, rule-based timeline, record references | what does bringing the data together give? | on the locked cases; also the degraded mode |
| GenAI-assisted view | context plus summary, blocker, procedure, next step and draft | what does GenAI add? | on the locked cases, and live with the first users |

If the context-only view gives most of the improvement, the result supports investment in customer context and limits further GenAI investment. The added value of GenAI is an input to the decision after the MVP, not a pass or fail criterion. Case numbers are in the measurement annex of the [Charter](#charter); the acceptance rule is on [Controls and evidence](#controls).

### Fit with the AI Platform and the Standards {#technical-design-platform-standards}

The pilot uses the AI Platform where it exists. A pilot-local stand-in for a Platform function is recorded in section 3 of the Solution Definition and as a Dependency on the Platform Owner, who accepts it for this Solution. The evidence is on [Controls and evidence](#controls).

| AI Platform function or Standard | In this design |
| --- | --- |
| Model gateway (PLT-004) | the AI gateway, or one authenticated proxy as a stand-in; data separated by class |
| Knowledge layer (ARC-001) | one approved corpus; outputs cite sources; each source has an owner and review date in the AI Registry |
| Tool gateway (ARC-007) | not needed: the model holds no tools and is not an AI agent |
| Guardrails (ARC-005) | customer messages treated as untrusted input and filtered; output checks; a person before every action |
| Human oversight (ARC-004) | the employee decides each case; the record keeps the AI's contribution and the decision |
| Observability (PLT-002, ARC-008) | logging with the required retention; a trace per case; alert levels with watchers |
| AI Registry (PLT-001) | model and version, data classes, knowledge sources; "AI agents and permissions: none" |
| Suspension (PLT-005, ARC-002) | generation or the Service switched off without losing the record |
| Open components (ARC-006) | licenses in the Solution Definition; covered by the security test |
| The Lab (LAB-001 to LAB-007) | isolated, logged, read-only extracts with owners, personal data assessed, Evaluation set with grounding, drift and bias checks, Outcome Report at the end |

### Later, outside this pilot {#technical-design-later}

- A shared tool gateway, policy service, workflow runtime or event streams: only if a second journey needs them, as a Proposal to the Platform Owner.
- Reuse of components: a Package Definition; shared use needs a second consumer (Solution Lifecycle Model 8.12).
- Use beyond the first users: the decision after the MVP, then a release with the Acceptance Checklist, or a Proposal and a Handover to an IT function as Receiver.
- Customer self-service or customer actions: each would be a separate Initiative or Proposal with its own Risk Tier; an AI acting for customers would be Tier 3.
