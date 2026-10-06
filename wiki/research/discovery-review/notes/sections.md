# Portfolio, Delivery Pipeline, CloudLab: review of the English content and of the originals

Reviewer id: `sections`. Read on 6 October 2026. Read-only: nothing was changed except this file and `fixmap/sections.jsonl`.

## Summary

- The three small sections together hold six pages and about 1,170 words. They are honest about their state (empty register, proposal, concept) and contain no broken text, placeholders or wrong facts. Their weakness is what they leave out and what they do not relate to.
- Portfolio (3 pages): an overview, seven selection questions, and an empty register. It never says what "selected" means, who selects, or what statuses an initiative can have, and it reports "0 initiatives" while the Registry's Portfolio Backlog holds ten Initiatives.
- Delivery Pipeline (2 pages): a one-row table and a 411-word summary of the CSR proposal. The pipeline has no stated stages, and its only entry is an unapproved proposal that is not in the Portfolio.
- CloudLab (1 page): a 237-word concept. It does not say whether CloudLab is the charter's Lab, it disclaims the cloud its name asserts, and it leaves out the data rules that both the origin and the charter state most firmly.
- Main losses from the originals: CSR keeps about 2.5% of the source by words and loses the problem statement, the customer outcome, every number, the decision requested, the governance, and all the technical content; "customer intelligence" survives only in the title. CloudLab loses the six-stage by five-concern grid of 41 activities, the 20-guardrail scorecard, and the read-only data rule.
- `html/cloudlab`, `html/csr` and `html/sts` match `html-alt` in content. Each adds a little navigation text of its own; the additions are listed in section 3.
- STS is an IT service management framework with no AI content. It is not integrated as a section and does not need to be: its lifecycle already feeds the charter's "life of a Service".
- The four neighbours restate, under other names, four things the charter side already places: the backlog of scenarios, the Portfolio Backlog, the Solutions in delivery, and the Lab with its Experiments. This is the root of most naming clashes.
- The fix map has 42 entries for text that can be corrected now: 16 for Portfolio, 17 for the Delivery Pipeline and 9 for CloudLab, one of each being a change of the label above the title. Nine are high severity. Everything that depends on a definition or a name is in "Questions for the owner".

## 1. Findings across the three sections, most serious first

### 1.1. The neighbours duplicate charter concepts under different names

The charter side already describes the same chain. `portal/content/en/portfolio/roles-and-records.md` 3.1 reads the Portfolio "in four groups", the last being "the backlog of scenarios by Domain, screened and ranked, from which the funnel is fed", and adds: "the live state is in the Portfolio Backlog of the Registry". The front-door screening (Portfolio Management Model 5.5) even uses the Discovery Catalog's own lens and size scales.

| Neighbour section | What it holds | What the charter already calls this | Where the charter side puts it |
| --- | --- | --- | --- |
| Discovery Catalog | 1,101 scenario cards | The backlog of scenarios by Domain | Portfolio, roles and records 3.1 |
| Portfolio (`/initiatives/`) | Selected initiatives, live | The Portfolio Backlog, with one Initiative Brief each | The Registry |
| Delivery Pipeline (`/projects/`) | Projects by status | Initiatives that are Active, and their Solutions; an Engagement where there is a client function | Portfolio Backlog, Program Backlog, the catalog of Solutions |
| CloudLab (`/lab/`) | Experiment environment and workflow | The Lab and the Experiment | Solution Lifecycle Model 8.13; the page "The Experiment workflow: the Lab" |

The integration decision (C-PORTAL-NEIGHBOURS) made the sections independent on purpose: no links and no citations between a neighbour and the charter. That rule keeps the lifecycles apart, but it also means nothing on the page tells a reader how the two "Portfolio"s or the two "Lab"s relate. A reader who meets both will assume they are the same thing and find that they disagree.

### 1.2. "0 initiatives" contradicts the Registry

The Portfolio landing says "No initiatives have been entered yet" and the register carries the status "0 initiatives". `registry/en/portfolio-backlog.md` lists ten Initiatives: six ranked ones in Discovery: Scoping (INI-002, 006, 004, 003, 007, 008) and four Standing Initiatives that are Approved. The section is only correct if "selected" means something narrower than "in the Portfolio Backlog", and the section never defines it. The empty register was a deliberate constraint of the integration ("do not import the existing AICC initiative records"), so this is a definition to make, not an error to correct.

### 1.3. The chain between the sections is broken

The order of the navigation suggests a flow: opportunities, selected initiatives, projects in delivery, experiments. The content does not follow it. The only project (CSR) is not a selected initiative, has no owner, and is not approved, yet it sits in a section called "Delivery Pipeline". By its own text it is a candidate that has not passed selection. In charter terms it is an idea in the funnel (state Proposed) and a candidate for an Engagement; the research note `wiki/research/services/service-ideas.md` records it exactly so. No section says what turns an opportunity into an initiative, an initiative into a project, or when an experiment is used instead of a project.

### 1.4. None of the six pages says whose it is

"Bank", "O!Bank" and "AICC" do not appear once in the six files. "CloudLab is a concept for a controlled environment": whose? "The portfolio presents initiatives selected": by whom? Every page reads as generic guidance that could belong to any organization.

### 1.5. The unit of each section is never defined

The words opportunity, idea, initiative, project, pilot, proposal, journey, solution, experiment and hypothesis are all used, and none is defined or distinguished from its neighbour. The charter defines Initiative, Solution, Experiment and Proposal, and warns that "Project is a general work designation".

### 1.6. Status labels are of three different kinds

The label above each title is a content type on some pages ("Selected initiatives", "Project register", "Guidance"), a count on one ("0 initiatives"), and a lifecycle state on two ("Proposal", "Concept"). "Selected initiatives" sits above a page that says there are none. "Project register" is not a status. "Proposal" is also a defined charter term with another meaning (a proposal to adopt a Solution at scale, the outcome of an Experiment).

### 1.7. Spelling and punctuation differ from the charter

The lab page uses British forms ("behaviour", "authorise"); the charter's Vocabulary 3.2 requires American spelling. All six files omit the serial comma; the charter uses it throughout. The charter capitalizes its defined terms; the sections use the same words in lower case with looser meanings.

### 1.8. Matters for the layout work, noted here because a reader sees them

- The browser title of each landing page repeats itself: "Portfolio · Portfolio", "Delivery Pipeline · Delivery Pipeline", "CloudLab · CloudLab".
- The local navigation repeats the section name as its first item; under CloudLab it is the only item.
- The footer and sidebar of every neighbour page read "Version 2.2 · October 2026". That is the edition of the charter corpus. On a neighbour page it reads as the version of the section's content, which the integration decision said must not carry charter baseline stamps.
- No neighbour page shows a date of last update, although the Portfolio text promises "the date of its latest update".

## 2. Section by section

### 2.1. Portfolio (`portal/sections/initiatives/en/`, three pages, 426 words)

**Overview (`index.md`), label "Selected initiatives".**

| Block | What is there | Finding |
| --- | --- | --- |
| Opening paragraph | The portfolio presents initiatives "selected for further development" with problem, outcome, scope, evidence | "Selected" by whom and from what is not said. "Further development" can be read as software development. The owner is missing from the list of what an entry shows. |
| Empty state | "No initiatives have been entered yet." | "Entered" here, "selected" on the register page: these mean different things (none chosen, or chosen but not written up). |
| Explore this section | Two links with one-line descriptions | "establish a worthwhile initiative" is clumsy. The register is described as holding "selected initiatives and their recorded status" with no hint that it is empty. |
| What an initiative presents | Need, owner, scope, outcome; facts against assumptions | The heading is odd: the paragraph is about what a record contains. This is the only attempt at a definition, and it does not separate an initiative from an opportunity or a project. |
| Closing paragraph | Selection, commitment to delivery, confirmation of benefit are separate decisions | The strongest sentence of the section. It does not say who takes each decision, and the three decisions never become a list of statuses. |

Missing from the page: who owns the list; how an initiative gets on it; the statuses; any count or date.

**Selection approach (`selection.md`), label "Guidance".**

| Block | What is there | Finding |
| --- | --- | --- |
| Opening | "Start with the service problem…" | An instruction with no addressee. "Service problem" is narrower than the table below it. |
| Questions to resolve | Seven questions with what the assessment should establish | Coherent and well worded. It leaves out fit with the Bank's priorities, whether an existing solution already answers the need, and the risk level; the charter's own screening asks all three. One row says "idea" where the rest of the section says "opportunity". |
| Basis for selection | What a selection record states | A third, different list of record fields (see below). |
| Indicative estimates | "An indicative benefit or complexity estimate is a starting assumption." | This points at the Discovery Catalog's complexity and OKR figures without saying so. Read alone, the sentence has no referent. |

The page is called an approach but gives only questions. It does not say who assesses, who decides, what the possible results are (selected, returned, deferred, declined), or how two candidates are compared. "Selection" implies a choice among several; the page describes the assessment of one. It is also a second selection method beside the charter's (intake screening in 5.5, five business-case questions in 6.2, ranking in 6.5). The two do not contradict each other, but they use different questions and different words for the same gate.

**Initiative register (`register.md`), label "0 initiatives".**

Two sentences and a link. The empty state is clear. There is no table, so the reader cannot see what a filled register will look like. The fields promised here (business problem, intended outcome, owner, scope, decision, current status) differ from the overview (problem, outcome, scope, evidence) and from the selection page (scope, benefit, assumptions, dependencies, reason to proceed). One record, three field lists.

**Clashes with the charter.** Two pages carry the title "Portfolio": the neighbour at `/en/initiatives/` and the charter course at `/en/portfolio/`, whose navigation label is "Portfolio management" but whose heading is "Portfolio". The address `/portfolio/` leads to the charter page, not to the section named Portfolio. The charter defines Portfolio as "the Initiatives of AICC and the Solutions and Packages that they deliver"; the neighbour holds initiatives only. The repository also has a `portfolio/` folder (the catalog of Solutions and Packages). "Initiative register" sits beside the charter's "Registry" and "AI Registry"; in Russian both are "Реестр".

### 2.2. Delivery Pipeline (`portal/sections/projects/en/`, two pages, 510 words)

**Landing (`index.md`), label "Project register".**

| Block | What is there | Finding |
| --- | --- | --- |
| Opening | Project definitions "and the evidence of their progress"; "a proposal, an implementation and an operating solution can be distinguished" | There is no evidence of progress to show. The three states are named in passing and never listed as the stages of the pipeline. What a project is, and how it differs from an initiative, is not said. |
| Project register | One row: CSR, intended outcome, status Proposal | Clear. No owner and no date column. |
| Note | "The first entry defines a proposed pilot…" | Honest and useful. "Approval to operate" is ambiguous; "approval for live use" is meant. |

The section has three names: "Delivery Pipeline" (title), "Project register" (heading and label), and "projects" (address, and the Russian label "Проекты"). A pipeline implies stages; the page has none.

**Customer Intelligence–Enabled Service Resolution (`service-resolution.md`), label "Proposal".**

| Block | What is there | Finding |
| --- | --- | --- |
| Status line | "Status: proposal. A controlled employee-assist pilot for one customer-service journey and one team." | Repeats the label above the title. Does not say what the pilot is for. |
| Intended outcome | Help the servicing employee understand, verify, identify the next step | There is no problem statement before it. The outcome is the employee's; the original's outcome is the customer's (fewer repeat contacts, faster confirmed resolution). |
| Candidate journeys | Three journeys with scope | The relative complexity and the reason for choosing payments first are gone. |
| Proposed delivery approach | Six steps | Step 4 says "protected acceptance cases", which is unclear (the original: locked cases unseen during development). The silent-evaluation step is missing. A stray instruction follows the list: "Compare the existing process, a context-only workspace and an AI-assisted workspace." It is about evaluation, not delivery, and has no subject. |
| Boundaries | What is excluded; what happens when evidence is missing | Good. "Onboarding decisions" is confusing next to a candidate journey called Onboarding/KYC Progress Support; approval or rejection of onboarding is meant. |
| Evidence and continuing ownership | What evaluation covers; what must be named before commitment | No figure of any kind. The benefit owner and the sponsor are not mentioned. |

Missing from the page: the problem; what would be built; what "customer intelligence" means (the phrase is only in the title); what decision is being asked and of whom; any date or author; the fact that a full proposal exists. The page says "servicing employee" and the landing says "service employees".

**Clashes with the charter.** The AICC section has "Delivery" (navigation label "Delivery model", heading "Delivery"), which is the method; "Delivery" is also a charter Stage of a Solution; and the charter uses "continuous delivery pipeline" for the engineering loops. "Project" is not a level of the charter's work hierarchy. "Pilot" corresponds to the charter's MVP. "Proposal" as a status collides with the defined term Proposal; the matching charter state is Proposed.

### 2.3. CloudLab (`portal/sections/lab/en/index.md`, one page, 237 words), label "Concept"

| Block | What is there | Finding |
| --- | --- | --- |
| Opening | A concept for a controlled environment; an experiment starts with a question, a scope "and evidence that could confirm or reject the hypothesis" | At the start there is no evidence, only a statement of what evidence would decide. Whose environment, and whether it exists, is not said outright. |
| Approach | Named owner, permitted data, limited access, budget, reproducible evaluation, explicit decision; no provider selected | "Keeping each experiment accountable": people are accountable, not experiments. "Permitted data" is all the page says about data. |
| Experiment workflow | Define, Prepare, Build, Evaluate, Decide | The last step is called Decide but only records and recommends; who decides is not said. "Observable actions and a manual stop" is jargon. |
| Disclaimer | Evidence does not authorise production access | Good; it matches the charter's "an environment and not an authority". |
| Guidance to develop | A list of topics the guidance "will cover"; then a paragraph on successive experiments | The heading is ambiguous. The list is a placeholder. The second paragraph belongs under Approach. |

Missing from the page: the data rule (read-only extracts, no write-back, personal data reduced before entry); who runs the environment and who may ask for an experiment; the five concerns of the original; a list of experiments or a statement that none has run; what would move the Lab from concept to operation.

**Clashes with the charter and within the portal.**

- Three names: "CloudLab" (section), "Lab" (charter: "the isolated and logged environment of AICC in which an Experiment runs"), "Cloud LAB" (original; "Cloud Lab" in its stage names). The original also names an "On-Prem Lab" that nothing defines. The AICC home page calls AICC itself "the Bank's own Artificial Intelligence Lab".
- The name asserts a cloud; the text says "the concept does not select a cloud provider". Under Solution Lifecycle Model 8.13(d) a cloud environment is a provider and must pass the provider check before use, so the name runs ahead of a decision.
- Three workflows for the same thing: the original has six stages (Define Scenarios, Establish Cloud Lab, Choose Scenario, Prepare Data, Agentic Workflow, Validate); the charter-side page "The Experiment workflow: the Lab" has six steps (Define, Establish, Prepare data, Build, Evaluate, Review) and says it draws on the Cloud LAB; the new page has five (Define, Prepare, Build, Evaluate, Decide).
- Three sets of outcomes: "further work, a revised hypothesis or closure" (new page); "promoted toward production or shelved" (original); "accepted with its lessons and closed, a Proposal, or rejected" (charter). The Vocabulary says expressly that "promote or shelve do not define a separate outcome".
- The charter treats the Lab as an environment with rules in force; the neighbour calls it a concept. Both can be true only if the page says which is which.

## 3. Origin versus integration

### 3.1. CloudLab

**Content map of the original** (`html-alt/cloudlab/index.html`, one page, about 1,140 words, titled "Cloud LAB · Scenario Hypothesis Validation"; the footer places it in the "GenAI-enabled Banking and Financial Services Framework").

| Part | Content |
| --- | --- |
| Header | The lab "runs continuously"; scenarios enter at any time; "data flows from production into the sandbox via read-only ETL"; workflows are "promoted toward production or shelved"; the lab "persists indefinitely as the bank's GenAI exploration runtime" |
| Matrix | Six stages by five concerns (Governance & Decisions 11 cards, Risk & Controls 7, Operations & Processes 8, Data & Analytics 8, Observability 7): 41 activity cards, three empty cells |
| The Dual Operating System | System A Human Governance (A.1 to A.5), System B Agentic Intelligence (B.1 to B.5); "Decision rights remain human" |
| Business Agility | Seven capabilities: Analyze, Reason, Decide, Act, Learn, Govern, Engage |
| The Intent Loop | Intent, Insight, Action, Audit |
| Governance Guardrails Scorecard | 20 guardrails in the five concerns, each with a one-line posture and a coverage value from 20% to 90% that is shown only as the length of a bar |

**What reached the integrated page.** The idea of a controlled place to test a hypothesis; a workflow reduced from six stages to five steps; the principle that evidence does not authorize production use. Nothing else.

**Lost.** The whole matrix (41 activities); the five concerns; the scorecard; the data rule (read-only extracts, no write-back, personal data masked or excluded), which is the most concrete content of the original and agrees with the charter; the stakeholder demonstration and benchmark against baseline; the Dual Operating System, Business Agility and Intent Loop frames.

**Changed in meaning.**

- The original speaks of an operating lab in the present tense ("ETL pipeline operational", "Hard list maintained"). The integration calls it a concept that establishes no environment. This is a correction, since no lab exists, but it means the scorecard's postures and percentages describe nothing real and should not be carried over as facts.
- The original names AWS twice ("AWS approvals", "Build read-only export to AWS"). The integration selects no provider.
- The original's unit is the scenario, the same word as the Discovery Catalog's cards, and its "Hypothesis OKRs" are the OKRs on those cards. The integration speaks of "AI hypotheses" and a "business question" and drops the word scenario, so the link from the catalog to the lab is no longer visible.
- The original has the "Sponsor + IT lead authorise scenario promotion". The integration names no one. The charter gives acceptance to the Domain Owner or the Executive Sponsor.
- The original aims at "the minimum guardrails required to maintain exploratory freedom". The integration stresses accountability.

**Defects in the original itself**, should it be used as a source: "Performance Metrics (KRIs)" is described as "Scenario-level KPIs tracked"; "Pick next scenario from validated backlog" comes before any validation; "ETL Execution" is listed before "ETL Pipeline" (run before build); the scorecard gives the lifecycle as "choose → build → validate" against six stages; "On-Prem Lab" is undefined; spelling is mixed ("analyzes", "authorized" beside "authorise", "prioritisation", "formalised").

**`html/cloudlab` against `html-alt/cloudlab`.** The same 41 cards, the same 20 scorecard rows with the same coverage values, and every paragraph. The converted copy adds: a header line "AICC · scenario validation" (the original does not mention AICC); a section menu; a heading "Six-stage flow map" with a reading instruction; a "Selected activity" panel; and "Six stages, five concerns", which repeats the 41 cards as lists. One structural difference: the heading and paragraph "The Dual Operating System" now stand above the flow map, and the System A and System B panels they introduce follow the map without a heading.

### 3.2. CSR

**Content map of the original** (`html-alt/intelligent-customer-service-resolution/en/index.html`, one long page per language, about 16,800 words, 140 headings, 34 diagrams, labelled "Project proposal · Three selectable charters").

| Part | Content | Key tables and numbers |
| --- | --- | --- |
| Executive orientation | Promise, expected value for customer, operations and strategic capability, three candidate journeys with complexity | Lower, medium, medium–high |
| Business use case (17 sub-sections) | Intent, problem, pilot scope, journey selection, benefit baseline, domain placement, what is built, process integration map, delivery action workflow, workstreams, governance, risk position, acceptance, dependencies, continuing ownership, scope boundary, reuse | 5 candidate journeys; 9-step process map; 10-step delivery workflow; 4 workstreams; 8 decisions; a RACI of 12 activities by 8 roles; 10 risk and conduct areas; 9 dependencies |
| Selection and evidence guide | Selection rule, acceptance logic, evidence sizing, control limits | 200 to 500 reviewed historical cases; at least 100 live cases; about 1,000 to 3,000 cases per population for an outcome claim; a worked example (30% repeat contact reduced by 15% relative is 25.5%) |
| Three candidate charters | Decision requested, intent, ownership, scope and exclusions, baseline, success measures, acceptance rule, risk position, approval record | 15 to 20% relative improvement as a planning hypothesis; use in at least 80% of eligible cases; at least 80% acceptance; at least 95% status quality; zero-tolerance events |
| Technical pilot blueprint (22 sub-sections) | Where GenAI adds value and where it does not; five architectural responsibilities; context service; limited-authority assistant; tools; workspace; reusable foundation; deployment; tests; three-mode comparison; validation progression; pilot-to-platform evolution | 7 capability layers; 10 registered tools; 10 foundation capabilities; 3 deployment positions; 9 test layers; 13 IT functions; 10 progression steps; 12 validation criteria; 5 evolution states |
| Journey technical profiles | Per journey: required capabilities with fallback, functional allocation, validation | 9 completion decisions; 6 capabilities per journey |
| Platform capability and readiness map | Capability map, decisions before commitment, readiness gates, CTO decision | 17 capabilities; 4 dispositions (reuse, extend, pilot-local, narrow or block); 10 decisions; 5 readiness gates |

The charters carry intended blanks (`[name]`, `[value]`, `[record]`, `[document version or commit]`) and a heading "Customer and process workflow" with a diagram and no text.

**What reached the integrated page** (411 words, about 2.5%). The three journeys with their scope; payments as first candidate; a six-step approach; the exclusions; the fallback rule; the list of what evaluation covers; the list of owners still to be named.

**Lost.** The problem statement; the expected value; the customer outcome; the two further candidate journeys (loan application status, complaints); every number; the decision requested and what approval would and would not authorize; the roles and the proposed sponsor; the RACI and decision structure; what is built; the whole technical side, including the statement of what AI does not establish; the rule that each step leaves an owned reusable asset; the 34 diagrams. The integration decision asked for this compression ("do not bulk-import its full operating model") and asked that the full proposal stay available. It is not available from the portal: `html/csr` is outside the published site, and the page does not say that a longer proposal exists.

**Changed in meaning.**

- The outcome moved from the customer to the employee. Original: "fewer repeat contacts and faster confirmed resolution". Integrated: "Help the servicing employee understand what happened".
- "Customer intelligence" is the point of the original (the pilot "creates a first practical customer-intelligence asset"). On the integrated page it is a phrase in the title with nothing behind it.
- "Locked acceptance cases unseen during development" became "protected acceptance cases".
- The closing decision "scale, revise, reuse for another journey, or close" became "extend, refine or close"; reuse was dropped.
- The exclusion list dropped eligibility, pricing and suitability decisions and added "onboarding decisions".
- "Recommended first implementation" was softened to "initial candidate". This is consistent with the proposal status.

**`html/csr` against `html-alt`.** All 1,807 text blocks of the original are present and unchanged. The converted copy adds one feature on the landing, "From contact to recorded outcome": an eight-stage map built from the nine-row process integration map, with the ninth row shown as a learning loop. Its caption ends in an unpunctuated fragment: "…a separate improvement backlog. aggregate repeat-contact and upstream failure patterns". The new header reads "CSR · Customer Service Resolution", which expands the abbreviation differently from the title (it drops "Intelligence–Enabled") and adds "conceptual explorer".

### 3.3. STS

**What it is.** "Shared Technology Services (STS) Framework" (`html-alt/sts/en/`): eight English pages and a topology data file. It is an explorer of IT service management built on ITIL 4 and IT4IT. It has an overview; an outer model, "STS Operating Model", of five domains; an inner model, "STS Managed Service Model", of five domains; a reference view (three lifecycle models, three practice groups, 34 practices, four journey lenses, 14 guidance questions); and four prototype pages under "SPOM" (Service Portfolio and Operating Model): a control-plane map, a seven-state managed-service lifecycle (Candidate, Admitted, Catalogued, Active, Improving, Transition Planned, Migrating), and a portfolio view that is a stub. It mentions AI nowhere.

**State.** The two model pages are five-item lists. The topology has 72 relationships, no dependency edges and no disciplines. A statistics tile reads "3 Shared Technology Services (STS) Framework Journey" where "3 lifecycle models" is meant. The introduction mentions an "empty dependency structure". "Catalog" and "catalogue" are both used.

**`html/sts` against `html-alt`.** Text is identical on all eight pages. The converted copy adds a header tagline and, on the overview, a strip "From candidate to migration" showing the seven states.

**Is it used?** Not in any neighbour section. It is already used on the charter side: the seven service steps of Solution Lifecycle Model 8.8 and the pages "The life of a Service" and "Service operations" come from it, as `wiki/research/services/service-ideas.md` records (the charter renames STS's "Active" to "In service", because Active is a charter state).

**Should it feed a section?** No new section. It is about running technology services, which is charter territory already covered. Its one possible use here is the end of the Delivery Pipeline: if the pipeline is to show what happens to a project after it goes live, the words should be the charter's service steps, which already carry the STS content, and not a second copy.

## 4. Proposed definitions (outline only)

### 4.1. Portfolio

**Proposed purpose.** The staff-readable list of the initiatives the Bank has selected, with the decision actually taken on each. It is a projection of the Portfolio Backlog for readers. It does not copy the Initiative Brief: scores, rank, figures, agreements and clearances stay in the Registry.

| Page | The question it answers | Source that feeds it |
| --- | --- | --- |
| Overview | What is this list, what does "selected" mean, how many initiatives are at each status, when was it last updated | Present `index.md`; the "Portfolio at a glance" groups of roles and records 3.1 |
| How initiatives are selected | What is asked of an opportunity, who assesses, who decides, what the possible results are | Present `selection.md`; Portfolio Management Model 5.5 (screening), 6.2 (five questions), 6.3 (who approves), 6.5 (ranking), restated briefly and not as a rule |
| Initiative register | Which initiatives are selected, for whom, with what decision and status | `registry/en/portfolio-backlog.md`: identifier, title, client function, state and Stage, dates. Not copied: scores, rank, Service Agreement |
| One page per initiative | What problem, what outcome, what scope, who owns it, what has been decided so far | Initiative Brief sections 1 (hypothesis) and 2 (outcomes and leading indicators, names only), the scope, and the decision history |
| Status legend (a block on the register page) | What each status word means | Vocabulary 4.2 states: Proposed, Discovery, Approved, Active, Accepted, Closed, Deferred, Rejected, Pivoted |

Needs the owner's input: what "selected" means in charter terms (taken in, which gives six today; or business case approved, which gives none of the ranked six); whether Standing Initiatives appear; whether the ban on citing the charter still holds for this section, since a projection of the Portfolio Backlog cannot honestly avoid naming it; how much of a brief may be shown; who updates the list and how often.

### 4.2. CloudLab

**Proposed purpose.** The section about the Lab: what it is, how an experiment runs in it, under which rules, and what has been run. The origin supplies the workflow grid and the guardrail list; the charter supplies the rules and the decision rights.

| Page | The question it answers | Source that feeds it |
| --- | --- | --- |
| Overview | What the Lab is and is not, who it serves, whether it exists yet, how to ask for an experiment | Present `index.md`; Vocabulary "Lab" and "Experiment"; Solution Lifecycle Model 8.13(a); the origin's header |
| Setting up the Lab (once) | What must be in place before the first experiment | Origin stages 1 and 2 (Define Scenarios, Establish Cloud Lab): sponsor, account and vendor sign-off, access policies, isolation, guardrails, services, data pipeline design; 8.13(d) provider check |
| Running an experiment (each time) | The steps, and what each concern contributes at each step | Origin stages 3 to 6 with their activity cards under the five concerns; the charter-side page "The Experiment workflow: the Lab" for the step names and records |
| Rules and guardrails | What data may enter, who may access, what is logged, what stops an experiment | 8.13(b), (c), (e), (f); the origin's 20 guardrails as the list of topics; the present "Guidance to develop" list |
| Decisions and outcomes | Who decides at the end and what can follow | Solution Lifecycle Model 8.1 and 7.3(c); the origin's Decision Rights and Promotion Pathway rows, corrected to the charter's outcomes |
| Experiment list | What has been run, with hypothesis, owner, time-box and result | Nothing yet: an honest empty state |

The origin mixes one-time set-up (stages 1 and 2) with the per-scenario cycle (stages 3 to 6); its own scorecard gives the cycle as "choose → build → validate". Separating the two is the main structural suggestion.

Needs the owner's input: whether CloudLab is the charter's Lab or a separate thing; the name; the provider (the origin assumes AWS; nothing is decided); whether the scorecard's coverage percentages may be shown at all, since they have no stated method and describe a lab that does not exist; whether the Dual Operating System, Business Agility and Intent Loop frames belong here (they describe the Bank's operating model, not the Lab) or on an explanatory page elsewhere, or nowhere; one set of step names; what "On-Prem Lab" was meant to be.

## 5. Uniformity: inconsistencies and a recommended single form

| # | Subject | Forms found | Recommended single form |
| --- | --- | --- | --- |
| 1 | The list of selected initiatives | "Portfolio" (label, title); `/initiatives/` (address); "Портфель инициатив" (Russian); against the charter page titled "Portfolio" and the defined term Portfolio (Initiatives, Solutions and Packages) | "Initiative Portfolio", which matches the Russian label and leaves "Portfolio" to the defined term. Rename the charter page heading to its own label, "Portfolio management". |
| 2 | The list of projects | "Delivery Pipeline"; "Project register"; `/projects/`; "Проекты"; against "Delivery" and "Delivery model" in AICC, the Stage Delivery, and "continuous delivery pipeline" | "Projects" in both languages. Keep "Delivery" for the charter's method. |
| 3 | The experiment environment | "CloudLab"; "Cloud LAB"; "Cloud Lab"; "On-Prem Lab"; "Lab" (charter); "Artificial Intelligence Lab" (AICC about itself on the home page) | "Lab" for the concept everywhere. Use "CloudLab" only if the owner wants it as the proper name of one environment, and say so once. |
| 4 | The catalog | "Discovery Catalog"; "Каталог возможностей" (catalog of opportunities); against the charter state Discovery and "the backlog of scenarios" | Owner's choice between "Scenario Catalog" and "Opportunity Catalog"; either is closer to the Russian label and avoids the state Discovery. |
| 5 | The catalog's unit | scenario (cards); opportunity (landing text, selection page); idea (selection page) | "scenario" |
| 6 | The selected unit | initiative, in lower case and loosely defined; Initiative (charter: "a business program… held in the Portfolio Backlog") | "Initiative" with the charter's meaning |
| 7 | The delivery unit | project; pilot; proposal; "operating solution"; against Solution, MVP, Engagement | "Solution" for what is delivered and "MVP" for the first trial with users; if "project" is kept, define it once as the work to deliver one Solution. |
| 8 | The lab unit | experiment; hypothesis; scenario (origin); Experiment (charter) | "Experiment"; the hypothesis is what it tests. |
| 9 | Status of a record | Proposal, Concept, Selected, "0 initiatives"; against the charter states | Charter state words: Proposed, Discovery, Approved, Active, Accepted, Closed, Deferred, Rejected. "Proposal" stays reserved for the defined term. |
| 10 | Label above a page title | Content type, count and state mixed | One meaning: the state of what the page shows. Pages that are not records get no state label. |
| 11 | Outcome of a decision | "continuing, changing direction or stopping"; "extend, refine or close"; "further work, a revised hypothesis or closure"; "promote or shelve"; "scale, revise, reuse, or close" | Charter sets: continue, pivot, defer, reject after an MVP; accepted and closed, a Proposal, or rejected for an Experiment. |
| 12 | Workflow of an experiment | Six stages (origin); six steps (charter-side page); five steps (CloudLab page) | The six steps of the charter-side page |
| 13 | A list of records | register; registry; backlog; catalog | "list" for a neighbour's own table; "Registry", "Portfolio Backlog" and "Catalog" stay with their charter meanings. |
| 14 | Spelling | British in the lab page and parts of both origins; American in the charter | American (Vocabulary 3.2) |
| 15 | Serial comma | Absent in the six section files; used in the charter | Serial comma |
| 16 | The bank | "the bank" (both origins); no mention at all in the six section files; "the Bank" (charter) | "the Bank" |
| 17 | The acting system | "Agent", "agentic workflow", "Agentic Intelligence" (CloudLab origin); "AI assistant", "agent" (CSR origin); "AI agent" (charter) | "AI agent"; "workflow or AI agent" where the origin says "agentic workflow". |
| 18 | The technology | "GenAI" (both origins, never in the charter); "AI" (sections, charter) | "AI"; "generative AI" where the distinction matters. |
| 19 | The first trial | pilot (CSR); MVP (charter); Experiment (charter, without a consumer) | "MVP" for a trial with a client function; "Experiment" for a trial without one. |
| 20 | Owners | "accountable owner", "business owner", "process owner", "measurement owner", "sponsor"; against Domain Owner, Domain Expert, Executive Sponsor | Charter Roles where a Role is meant; say once which CSR role maps to which. |
| 21 | Heading case | "Delivery Pipeline", "Discovery Catalog" in title case; "Selection approach", "Initiative register", and all AICC labels in sentence case | Sentence case for labels and headings (Vocabulary 3.7) |
| 22 | The CSR name | "Customer Intelligence–Enabled Service Resolution"; "CSR · Customer Service Resolution" (converted copy); "CSR" | The full title; if a short form is wanted, "Service Resolution", since CSR is widely read as corporate social responsibility. |
| 23 | Edition stamp | "Version 2.2 · October 2026" on neighbour pages | No charter edition on neighbour pages; a date of last update per page. |

## 6. Notes for the fix round

- The fix map covers the English files only. The Russian files under `portal/sections/*/ru/` must receive the same changes; the integration decision requires equivalent content in both languages.
- `portal/tests/test_neighbours.py` requires the string "No initiatives have been selected" in `initiatives/en/register.md` and "**Status: proposal.**" in `projects/en/service-resolution.md`. The proposed texts keep both.
- The build stops with "Landing title drift" if a page's first heading differs from its title in `portal/sections/pages.json`. No fix in the map changes a first heading. Any rename decided from section 5 must change both places and the label in `navigation.json`.
- `portal/tools/check_neighbours.py` rejects a link in a neighbour's body that leaves its section. No proposed text adds one.
- Three entries (sections-016 to 018) change the `status` value in `pages.json` rather than a Markdown file, because that is where the label above a title is kept.
- Two entries are marked "OWNER DECISION FIRST" in their note and should wait for the answer to the question they name: sections-014 (how an assessment ends) and sections-033 (the planning figures on the CSR page).
- The entries were applied in order to a copy of the six files as a check: each `current` text is found exactly once at its turn, the two strings the test requires survive, no first heading changes, and `pages.json` stays valid.
- Applied in full, the fix map takes the CSR page from 411 to about 900 words and the CloudLab page from 237 to about 370. That is still a summary; question 8 decides whether more of the proposal should follow.
- Proposed texts follow each file's present punctuation and use a serial comma only where an item of the list itself contains "and". Item 15 of section 5 is one decision for all six files and is not applied piecemeal.

## Questions for the owner

1. Is the neighbour "Portfolio" the same thing as the charter's Portfolio Backlog, shown for readers, or a separate list with its own selection? Everything else about the section follows from this.
2. If it is the same: which state makes an Initiative "selected"? Taken in (six today), business case approved (none of the six today), or pulled into work? Do the four Standing Initiatives appear?
3. The integration decision forbids a neighbour to cite or link the charter. Does that still hold now that the sections are to be made uniform with the charter? Without a plain statement of the relation, two pages titled "Portfolio" and two things called "Lab" will keep reading as contradictions.
4. Is CloudLab the charter's Lab, a planned environment that would become the Lab, or something else? Should the section be called "Lab"?
5. Does the Lab exist in any form today? The charter states its rules in the present tense; the neighbour calls it a concept; the origin describes an operating AWS sandbox. Which is true, and has a provider been considered?
6. Should CSR stay in the Delivery Pipeline while it is unapproved and unowned, or move to the Portfolio as a candidate, with the pipeline left empty until something is approved? Is CSR related to INI-006, Customer experience intelligence: discovery?
7. What are the stages of the Delivery Pipeline? The page implies proposal, implementation and operation. Should they be the charter's states instead?
8. Where may a reader find the full CSR proposal? Should the Delivery Pipeline carry more of it (the charters, the evidence rules, a technical summary), or link to a published copy?
9. May the CSR page show the planning figures of the original (200 to 500 cases, 80%, 95%, 15 to 20%) as hypotheses, as the fix map proposes, or should a proposal page carry no figures?
10. Which CloudLab origin material is wanted: the six-by-five activity grid; the guardrail list; the coverage percentages (which have no stated method); the Dual Operating System, Business Agility and Intent Loop frames?
11. One workflow for an experiment: the six steps of the charter-side page, the origin's six stages, or the five on the CloudLab page?
12. Names (section 5, items 1 to 4): "Initiative Portfolio", "Projects", "Lab", and "Scenario Catalog" or "Opportunity Catalog"? Should the English and Russian labels be literal equivalents of each other? Today "Delivery Pipeline" is "Проекты" and "Discovery Catalog" is "Каталог возможностей".
13. Status words: adopt the charter's state words for initiatives, projects and experiments, and replace "Proposal" with "Proposed"? This changes a string that a test checks.
14. Spelling and the serial comma: American spelling with the serial comma for all neighbour sections, as in the charter?
15. Should neighbour pages stop showing the charter's "Version 2.2" and show their own date of last update?
16. STS: confirm that it stays a research source and is not to become a section.
