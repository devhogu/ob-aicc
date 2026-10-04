# Shared Business and Technology Terminology

Edition 1.5 · 4 October 2026

## 1. Purpose and scope

1.1. This reference forms part of the AICC charter corpus. It specifies the shared names, meanings and permitted language variants of business, finance, delivery and technology terms used in the corpus and its portal.

1.2. Established industry terminology shall be used where it accurately identifies the concept. An AICC-specific name shall be used where it expresses a distinct concept, responsibility, Record or state.

1.3. This reference and Vocabulary and Style have the following complementary functions.

| Reference | Function |
| --- | --- |
| [Vocabulary and Style](documents/vocabulary.md) | Defines AICC concepts, Roles, authority, work items, states, controls and Records |
| Shared Business and Technology Terminology | Specifies shared names, abbreviations, aliases, definitions and their application |

1.4. A term shall retain the meaning and operational application established in the governing documents. Its inclusion in this reference does not establish a service commitment, authorize a system or product, or change a control, measurement boundary or decision right.

1.5. Each language edition shall provide definitions and application in its own language. Corresponding entries shall describe equivalent concepts. Fixed names shall remain consistent across language versions.

## 2. Terminology conventions

2.1. Entries are grouped by subject and identify a universal term, meaning and application. The universal term is the shared entry name across language editions; its application specifies whether its exact form is required. The Russian-language edition additionally provides a Russian-language term immediately after the universal term. This column gives the corresponding professional name and identifies the context of AICC-specific designations. It supports concept matching and explanation of fixed names. The Application column governs usage: a fixed form is retained across languages; a permitted language variant follows the language of the document; a context-specific form follows the identified methodology, system or Record.

2.2. Fixed names shall retain their spelling, script and internal capitalization. AI and IT use Latin letters. Product names, including CloudWatch when used without a company name, shall be preserved. Sentence and heading capitalization may vary for ordinary words.

2.3. The surrounding text shall follow the grammar of its language. Examples include AI capabilities, an IT function, workflow execution, an FSM model, a DAG and CloudWatch metrics.

2.4. Recorded singular and plural forms of fixed names shall be preserved. Inflection shall be expressed through the surrounding text where the fixed form does not support the grammar of that language. Translatable adjectives shall follow the language and meaning of the sentence.

2.5. A full name may precede its abbreviation at first use: Finite State Machine (FSM), directed acyclic graph (DAG), Amazon Web Services (AWS). Subsequent references may use the abbreviation. An explanatory translation does not replace a fixed name.

2.6. A name shall be applied to the complete concept or entity it identifies. Generic words shall not be treated as product names solely because their spelling occurs within such a name. Service Management does not identify a particular vendor product unless that product is specified.

2.7. Exact identifiers, interface labels, schema keys, file paths and quoted titles shall retain their original form. Terminology changes shall preserve the identity of historical Records and the distinctions between defined AICC concepts.

## 3. Business and governance terms

3.1. These terms describe business justification, governance, responsibilities and performance.

| Universal term | Meaning | Application |
| --- | --- | --- |
| business case | The justification for an investment or change: the problem or opportunity, alternatives, expected benefits, costs, risks, and the basis for deciding whether to proceed | Fixed form. Plural form: business cases. Business case identifies the reasoning and justification. The Initiative Brief is the AICC record that captures it; the record name and the concept have different purposes. A business case need not be a long document |
| business intelligence / customer intelligence | Analysis supporting business decisions / analysis of customers, their behavior, and experience | Permitted language variant. Intelligence identifies analytical activity; the term alone does not establish the use of AI. |
| dashboard | A consolidated view of selected measures and status information for a defined audience or decision | Permitted language variant. The defined Dashboard Record has the scope assigned in the governing documents. A generic dashboard does not acquire Record status through terminology alone. Operating Model 7.1; Solution Lifecycle Model 4.4 |
| ESG | Environmental, social, and governance. A grouping of environmental, social, and governance considerations | Fixed form. Statement of Intent 3.2. ESG is the fixed abbreviation. Its use does not constitute certification or evidence of performance |
| HR | Human resources | Permitted language variant. HR identifies the human resources function |
| KPI | Key performance indicator. A measure selected as particularly important for assessing progress or performance against an objective | Fixed form. A KPI is a Measure designated as key to an objective. Its objective, definition, source, responsible Role and review basis shall be specified. Other metrics remain Measures without KPI designation |
| KYC | Know your customer. The discipline of establishing and maintaining knowledge of a customer's identity and relevant risk characteristics | Fixed form. Statement of Intent 11.3.1. KYC is the fixed abbreviation. The applicable customer identification requirements remain those established by the Bank |
| OKR | Objectives and key results: a method of relating objectives to measurable results | Context-specific form. OKR identifies the method or a set of objectives and key results. PI Objective retains its distinct AICC definition and scoring |
| RACI | Responsible, Accountable, Consulted, Informed. A matrix distinguishing the performer, the owner answerable for the result, those consulted, and those informed | Fixed form. Organization guide, section 4; Appointments Record template. RACI and its letters are retained. Responsible identifies the performer; Accountable identifies the person answerable for the result |
| SOW | Statement of work: a description of the scope, deliverables, and related conditions of work | Context-specific form. SOW identifies the statement of work. Its relationship to a Service Agreement depends on the scope and standing of the actual documents; the terms are not automatically equivalent |

References: Vocabulary and Style; Business Model; Operating Model. Industry references: [IBM on metrics and KPIs](https://www.ibm.com/think/insights/sales-metrics) and [Atlassian: RACI](https://www.atlassian.com/work-management/project-management/raci-chart).

## 4. Delivery and workflow terms

4.1. These terms describe the organization, movement, delivery and operation of work and services.

| Universal term | Meaning | Application |
| --- | --- | --- |
| backlog | An ordered collection of work to be considered or carried out; its level and admission rules determine what it contains | Permitted language variant. Backlog identifies the general concept. Portfolio Backlog, Program Backlog and Iteration Backlog identify the respective levels. Vocabulary and Style; Solution Lifecycle Model section 4 |
| code review | Examination of source code to understand a proposed change and identify defects or weaknesses | Permitted language variant. Code review identifies the examination of source code. It does not replace the charter's broader Check or the Control Functions' Validation. Statement of Intent 9.8 |
| cutover | The controlled transition at which an agreed new system or way of working takes over from the previous one | Permitted language variant. AICC uses it specifically for moving working state from the Registry to Jira and Confluence; it does not move the evidence store. Operating Model 7.1–7.3; Collaboration tooling |
| deployment | Placing and configuring a version in a target environment so it can run | Permitted language variant. Initial deployment and the Release decision are distinct events in AICC. |
| Epic / issue / sub-task | Jira item names or types used to organize work at different levels | Context-specific form. Configured item labels shall retain their exact form. In AICC's Jira mapping, Capability maps to Epic, Feature to an issue type, and Work Item to sub-task. Use in another framework is explained in that context and does not change this mapping |
| Kanban | A method of managing the flow of work through explicit workflow policies, visualization, and control of work in progress | Permitted language variant. Kanban identifies the method. The defined names Portfolio Kanban and Program Kanban identify the respective AICC boards. Vocabulary and Style; Solution Lifecycle Model |
| lead time / cycle time | Elapsed-time measures with explicitly chosen start and end points | Permitted language variant. Solution Lifecycle Model 10.3 specifies the measurement boundaries applicable to AICC. |
| MVP | Minimum viable product. A deliberately limited first version used to test a value hypothesis with evidence, rather than to deliver all intended capability | Fixed form. Vocabulary and Style; Portfolio Management Model 6.8 and section 7. MVP tests the hypothesis of an Initiative in AICC; pilots and prototypes have their respective purposes |
| PI / IP | In this charter, Program Increment / Innovation and Planning week | Fixed form. PI and IP are the fixed short forms in AICC. PI is a quarter here; IP does not mean Internet Protocol or intellectual property in this context |
| production | The operating environment serving actual users or business processes | Permitted language variant. The Environment of use rule determines the transition applicable to AICC. |
| release | Making a version available for an intended audience; in AICC, the decision to allow use beyond the first users | Permitted language variant. The defined AICC decision authorizes use beyond the First users. |
| root cause analysis | Investigation of the causal conditions behind a failure so that corrective action addresses its cause | Permitted language variant. The analysis identifies causal conditions as the basis for corrective action. |
| service desk | The contact and coordination point for users' service requests and incidents | Permitted language variant. The term identifies the user contact function within Service Management. |
| Service Management | The Bank's system and processes for handling requests and incidents, as the charter uses the name | Context-specific form. The name alone identifies no vendor or product. A specific product name applies only where that product is identified in the relevant system record |
| SLA | Service-level agreement. An agreement between a service provider and its consumer setting out the service levels, their measurement, responsibilities, and the handling of missed targets | Fixed form. SLA identifies an actual agreement on service levels, including an internal agreement. It may be a part of the broader Service Agreement. A support category or a unilateral target alone is not the whole SLA. The name alone introduces neither financial penalties nor new guarantees |
| sprint / sprint backlog | A timeboxed iteration and its selected work in Scrum | Permitted language variant. These terms identify Scrum concepts. AICC's current Iteration is a calendar month; terminology alignment alone does not adopt Scrum or change that cadence |
| story points / velocity | Relative estimates of work / a team's completed estimate units over an iteration | Permitted language variant. Solution Lifecycle Model 10.1 specifies flow measures for AICC. Use of the terms story points and velocity does not change that measurement basis |
| throughput | Completed output counted per stated period, with the completion condition specified | Permitted language variant. AICC counts accepted Features per Iteration; this measure is distinct from individual staff productivity. |
| value stream | The end-to-end sequence of activities through which a need is turned into an outcome of value for a customer or other recipient | Fixed form. Plural form: value streams. Value stream identifies the end-to-end view across functions and steps. A workflow describes how work proceeds and can cover part or all of a value stream. The charter's service-delivery workflow already describes AICC's value stream |
| WIP | Work in progress. Work that has entered a defined system or activity and has not yet left it; also the amount of that work at a particular time | Fixed form. WIP shall be stated with its counting boundary. AICC's current measures specify their states and counting rules; adopting the short name does not silently change those rules |
| WIP limit | The maximum amount of WIP permitted within a defined part of a workflow | Fixed form. Plural form: WIP limits. WIP limit is the established short name for Limit on Work in Progress. Its scope shall identify the relevant state, lane, Domain or system. WIP is the actual amount; its limit is the permitted maximum |
| workflow | An organized flow of tasks, decisions, and transitions that produces an outcome. It may involve people, software, or both, and may branch, wait, repeat, or require approval. In the charter, a Workflow is the explanatory description of an AICC loop or flow; that narrower meaning does not imply executable automation. | Fixed form. Plural form: workflows. Workflow is the fixed name in all language versions. A workflow may contain cycles and therefore need not be a DAG. Automation alone does not make a workflow an AI agent. Corpus: [Vocabulary and Style](documents/vocabulary.md), Workflow; [workflow index](workflows/README.md). |
| WSJF | Weighted shortest job first. A relative prioritization method that compares the cost of delaying work with its relative size or duration | Fixed form. Portfolio Management Model 6.5 specifies AICC's scoring and permitted departure from the ranking. The WSJF abbreviation is retained; the formula applicable to AICC is the one specified in that document |

References: Vocabulary and Style; Portfolio Management Model; Solution Lifecycle Model; [Service delivery workflow](workflows/service-delivery.md). Industry references: [Scaled Agile: WSJF](https://framework.scaledagile.com/wsjf/), [Atlassian on internal and external SLAs](https://www.atlassian.com/itsm/service-request-management/slas), and [Kanban University on WIP and WIP limits](https://kanban.university/glossary/).

## 5. Technology and AI terms

5.1. These terms describe computational systems, AI, data, architecture and technical controls.

| Universal term | Meaning | Application |
| --- | --- | --- |
| access control | Rules and mechanisms determining which identities may access resources or perform operations | Permitted language variant. Access control includes permissions for resources and actions beyond authentication. |
| ACL | In this corpus, the identifier prefix of the Acceptance Checklist; elsewhere in IT, often access control list | Context-specific form. `ACL-[nnn]` identifies an Acceptance Checklist. The expansion access control list applies only where the technical context establishes that meaning |
| agentic | Describing behavior in which AI agents can choose or carry out steps toward a task | Permitted language variant. The adjective describes AI agent behavior without conferring unrestricted autonomy. |
| AI | Artificial intelligence. The field and family of computational systems that produce predictions, content, recommendations, decisions, or actions for specified purposes. AI includes more than conversational systems; the name alone says nothing about a system's autonomy, reliability, or permitted use. | Fixed form. AI is the fixed name in all language versions. Corpus context: [Statement of Intent](documents/statement-of-intent.md), sections 2 and 9; [AI Policy](documents/ai-policy.md), section 2. |
| AI agent / AI agents | An AI system that uses tools to act toward a task, within the functions, permissions, and limits assigned to it. Its design may allow it to choose intermediate steps and respond to results. Autonomy is a design property with a bounded scope, not a grant of organizational authority. | Fixed form. The charter's AI agent definition controls the AICC meaning. Assistant remains the distinct charter concept for a system that answers or drafts without acting beyond its output. A monitoring agent or a software installation agent is not necessarily an AI agent. Corpus: [Vocabulary and Style](documents/vocabulary.md), AI agent and Assistant; [AI Policy](documents/ai-policy.md), 3.6. Technical context: [Anthropic's explanation of workflows and agents](https://www.anthropic.com/engineering/building-effective-agents). |
| audit trail | A sequence of records that allows actions and decisions to be reconstructed | Permitted language variant. An audit trail supports reconstruction of actions; it does not by itself establish their lawfulness. |
| cloud | Remotely provided computing resources and services | Permitted language variant. The generic term does not identify AWS or any other provider. |
| DAG | Directed acyclic graph. A graph whose edges have a direction and whose directed paths contain no cycle. In task execution, its nodes can represent tasks and its edges their dependencies, allowing independent tasks to run concurrently. The graph structure alone does not specify retries, permissions, or failure handling. | Fixed form. DAG is the fixed name in all language versions. A workflow with an actual dependency cycle is not a DAG. A retry of a task need not introduce a cycle into its dependency graph. Reference: [Apache Airflow: Dags](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html); Airflow also uses *Dag* for its richer execution object, whose product-specific spelling is preserved in quotations and code. |
| drift | A change over time in data, behavior, or performance relative to a reference | Permitted language variant. The context shall identify whether the change concerns data, behavior or performance. |
| evaluation set | Cases and expected results used to assess a model or Solution | Permitted language variant. Composition and approval follow the governing requirements for the Solution. |
| fallback | An alternative operating method, component, or provider used when the normal path fails or is unavailable | Permitted language variant. Fallback is broader than rollback, which restores an earlier version or state. AI Policy 3.7 and 4.1; Solution Lifecycle Model 8.10; Statement of Intent 10.5 |
| Finite State Machine / FSM | A behavioral model with a finite set of states and rules for transitions triggered by events or inputs. It describes which state a system can occupy and how that state changes. An FSM may contain cycles: returning to an earlier state is not an error in the model. | Fixed form. The abbreviation is FSM. A state table in the charter can be explained using this concept without changing its states or gates. FSM and DAG describe different properties and are not interchangeable. Reference: [Stately: state machines and statecharts](https://stately.ai/docs/state-machines-and-statecharts). |
| human oversight | Human supervision of outputs or actions, including approval or the ability to intervene | Permitted language variant. The required form of oversight follows the Risk Tier and the governing rules. |
| ICT | Information and communication technology. Computing and communication systems considered together | Fixed form. AI Policy 5.2 uses ICT-related incidents. ICT is retained in technical labels and references to external sources. An IT incident is classified as an AI Incident only where it meets that definition |
| IT | Information technology. Computing technology and the capabilities used to build, integrate, operate, secure, and support information systems. An IT function is an organizational function responsible for technology; IT is not the name of a particular team or product. | Fixed form. IT is the fixed form in all language versions. It does not abbreviate Iteration. Corpus: [Vocabulary and Style](documents/vocabulary.md), IT function and Short forms; [Statement of Intent](documents/statement-of-intent.md), 9.7. |
| knowledge base | An organized collection of information maintained for reuse | Permitted language variant. A knowledge base does not inherently require AI. |
| knowledge layer | The part of a system that makes managed knowledge available for retrieval, with ownership, access, and source information | Permitted language variant. A knowledge layer includes managed access and source context beyond storage. The term alone does not identify a RAG architecture. Statement of Intent 11.2 |
| language model | A model that processes or generates language | Permitted language variant. LLM applies only where the model is a large language model. |
| lineage | Information tracing where data or an output came from and which transformations contributed to it | Permitted language variant. A qualifier, such as data lineage, identifies the subject. Lineage differs from a chronological audit trail. Statement of Intent 11.2 |
| logging | Recording relevant events and their context for later inspection | Permitted language variant. Event recording alone does not establish complete observability. |
| model gateway | A controlled access point through which applications reach models, with routing and the relevant access, data, and cost controls | Permitted language variant. Model gateway identifies controlled access to models. Statement of Intent 11.2 defines its place in the AI Platform |
| monitoring | Observing selected conditions and measures to detect changes or problems | Permitted language variant. The monitored conditions and measures define the scope of monitoring. |
| observability | The ability to investigate a system's internal behavior from the information it exposes, including logs, metrics, and traces | Permitted language variant. Observability concerns investigation of system behavior; monitoring concerns observation of specified conditions. Statement of Intent 11.2; Vocabulary and Style, AI Platform. [Yandex Cloud terminology reference](https://yandex.cloud/ru/docs/glossary/observability) |
| open model | A model made available with some degree of access to its artifacts or implementation | Permitted language variant. The degree of access and the applicable license determine the available rights of use. |
| pipeline | A connected set of processing steps through which data or work passes, with defined inputs, transformations, and outputs | Permitted language variant. Business Model 4.5 describes Pipelines. A qualifier, such as data pipeline, identifies the scope where necessary. A pipeline may branch; it is not automatically a DAG |
| Platform guardrails | Technical checks and restrictions that filter model inputs or outputs and limit an AI agent's actions | Permitted language variant. Platform guardrails identifies technical restrictions. The unqualified defined term Guardrails identifies Investment Guardrails under Vocabulary and Style |
| prompt injection | Input that causes an AI system to treat supplied content as instructions and deviate from its intended task or constraints; it can arrive through a user prompt or material the system reads | Permitted language variant. Prompt injection identifies this security concept. It is not an ordinary user request or a synonym for every attack on AI. AI Policy 3.3; [OWASP explanation](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) |
| read-only | Access permitting reading but not modification | Permitted language variant. Read-only access may disclose information even though modification is prohibited. |
| repository / protected main branch | A managed store with version history; a main branch whose changes are restricted | Permitted language variant. Literal branch names, including `main`, retain their identity. |
| retrieval | Finding and returning relevant material from a collection for a query or task | Permitted language variant. Retrieval identifies the search and return of relevant material. Retrieval alone is neither model training nor a complete answer-generation architecture. Statement of Intent 11.2 |
| tool gateway | A controlled access point through which AI reaches permitted tools and system interfaces | Permitted language variant. Tool gateway governs access to tools; model gateway governs access to models. Statement of Intent 11.2; Vocabulary and Style, AI Platform |

References: Vocabulary and Style; AI Policy; Statement of Intent; Operating Model. The applicable controls and measurement boundaries are specified in the governing documents.

## 6. Organizations, products and protected names

6.1. Company, organizational and product names shall retain their stated forms. Inclusion of a product does not record its adoption, procurement or approval for Bank data.

| Universal term | Meaning | Application |
| --- | --- | --- |
| AICC | AI Competence Center, the Bank's internal consulting and innovation lab for AI adoption, as the charter defines it | Fixed form. AICC is the shared organizational short name. The governing vocabulary controls its mandate and organizational meaning |
| Amazon CloudWatch / CloudWatch | An AWS monitoring and observability service for metrics, logs, alarms, dashboards, and other operational information | Fixed form. Official full name: Amazon CloudWatch. Protected short name: CloudWatch. AWS CloudWatch is a recognizable descriptive alias, not the preferred full product name. CloudWatch is retained when used alone and is not subject to literal translation |
| Amazon Web Services / AWS | Amazon's provider and family of cloud computing services | Fixed form. Amazon Web Services (AWS) is the full form on introduction; AWS is the abbreviated form. Both forms are retained in all language versions |
| Atlassian | The company that provides Jira and Confluence | Fixed form. Atlassian identifies the company; Jira and Confluence identify its products |
| Confluence | Atlassian's workspace for collaborative pages and documentation | Fixed form. Confluence is the fixed product name, including when used without Atlassian. The charter specifies its use by AICC |
| Jira | Atlassian's work-tracking product, with work items, workflows, and boards | Fixed form. Jira is the fixed written form in all language versions. AICC's item mappings are those in Portfolio Management Model 8.3 |
| O!Bank | The Bank identified by this charter | Fixed form. The spelling O!Bank includes the exclamation mark. Legal entity names remain those established by the Bank |

References: Vocabulary and Style; Operating Model, section 7; [Collaboration tooling](workflows/collaboration-tooling.md). Product identities: [Atlassian product documentation](https://confluence.atlassian.com/) and [Amazon CloudWatch documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html).

## 7. Maintenance

7.1. Amendments to this reference shall follow the document maintenance and change provisions of the Document Catalog. Amendments affecting the meaning of a defined AICC concept shall be reconciled with Vocabulary and Style and the relevant governing document.

7.2. Each entry shall identify the universal term, permitted form or forms, meaning and scope of application in the language of its edition. Russian-language names shall reflect professional usage supported by developer documentation, industry methodologies or specialist publications. Names with a meaning specific to AICC shall identify that context. Abbreviations, product-name variants and distinctions from related concepts shall be included where relevant.

7.3. Company and product names shall be verified against the provider's documentation. Former names shall be identified as historical aliases where required to interpret an existing Record or quotation.

7.4. A change from a permitted language variant to a fixed shared name shall be stated in the revised entry. Familiarity with an English expression alone does not make its exact spelling mandatory in other languages.

7.5. Terminology amendments shall be reflected consistently in affected text, headings, tables, diagrams, navigation, search entries and accessible labels. The corpus and its portal projections shall use equivalent meanings.

## 8. Change log

| Edition | Date | Change |
| --- | --- | --- |
| 0.1 | 2026-10-04 | Initial terminology reference with definitions and protected product names |
| 0.2 | 2026-10-04 | Extended coverage to business and delivery terminology, including KPI, SLA, WIP, WIP limit, business case and value stream |
| 1.0 | 2026-10-04 | Aligned terminology with Vocabulary and Style and the Document Catalog under DR-2026-064 |
| 1.1 | 2026-10-04 | Restated the reference in formal institutional language; distinguished fixed names from permitted language variants and removed drafting provenance from the operative text |
| 1.2 | 2026-10-04 | Consolidated all entries by subject using a uniform explanatory structure; definitions and application distinctions retained |
| 1.3 | 2026-10-04 | Established separate language editions, each containing definitions and application in its own language |
| 1.4 | 2026-10-04 | Standardised the universal term column and added professional Russian-language names to the Russian edition while preserving application rules |
| 1.5 | 2026-10-04 | Aligned corpus references with fixed international names and recorded plural forms used in the corpus; meanings and usage classes retained. |
