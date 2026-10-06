# Delivery Pipeline (Projects): audit, 6 October 2026

Scope: the section landing page and the one project in it, "Customer Intelligence–Enabled Service Resolution", a workbook of nine documents (about 123,000 characters in English). Read for sense, process logic, structure, content for its readers, wording, and fit with the AICC corpus. The detailed findings are in [review-business-case-and-charters.md](review-business-case-and-charters.md) and [review-technical-documents.md](review-technical-documents.md); this page holds the conclusion and the plan.

## Conclusion

The pilot idea is sound and well bounded: one journey, one team, facts only from the Bank's systems, the employee reviews and approves every step, regulated decisions excluded, a manual fallback, and a context-only comparison that isolates what AI adds. The documents around it are not yet usable: they run a project process of their own instead of the corpus, leave out what an approver needs, and are about three times longer than necessary.

## What must change

1. **A parallel process.** The workbook routes the work through "the bank's normal project-initiation process", a Project Manager, a RAID log, its own forum and its own gates. AICC, Initiative, Domain Owner, Executive Sponsor, Risk Tier, Solution Definition and AI Registry do not appear once. The corpus already holds related work as INI-006, Customer experience intelligence (PRI-1, Discovery). The project must be expressed as an Initiative with an Initiative Brief, an MVP and a Solution Definition, through the Portfolio Kanban and the Solution Lifecycle Model.
2. **Risk and approvals.** The Head of Customer Service "confirms the risk classification", where the AI Policy gives that to the AICC Lead. Risk Tier 2 is never stated, information security is missing from the approvals, and model risk is "where required". Live use, scale and suspension are given to the wrong people.
3. **The AI holds write tools,** two of them without employee approval, while the text also says it changes no state. Write rights over systems place a use in Risk Tier 3. The model should only read; every write is the employee's action.
4. **Model hosting.** A managed external model is presented as the fastest route for customer data, with no provider check or data-class approval. With the Lab on the Bank's own infrastructure, the route should be in-bank unless a provider passes the check.
5. **No cost, effort, duration or time-box,** and a circular order: the baseline is a condition of approval and also what the approval pays for.
6. **Three acceptance rules** that differ between documents; one of them cannot fail.
7. **"Customer intelligence" in the name and the intent** reads as profiling and conflicts with purpose limitation; inferences are said both to become a reusable asset and not to become customer facts.
8. **Over-built for one journey:** ten "minimum" platform components, thirteen IT functions, a three-arm live trial needing thousands of cases per arm, automatic model failover and cohort widening that bypass change and release rules.
9. **Local realism:** records in Russian, Kyrgyz and mixed text; systems that may lack read interfaces, shared customer keys or case timestamps; UK and EU vocabulary ("vulnerable customer", "non-inferiority"); no jurisdiction named.
10. **Structure and wording:** about 70% of each charter repeats the business case; platform and reuse content appears in seven places; invented capitalized names ("Limited-Authority Service Resolution Assistant"); undefined acronyms; "charter" collides with the AICC Charter; "Proposal" is used for the first stage, where the corpus uses it for the end of an Experiment.
11. **Section level:** the section is "Delivery Pipeline" in English and «Проекты» in Russian; a second, older version of the project text (`portal/sections/projects/{en,ru}/service-resolution.md`) is no longer used by the build.

## Proposed structure of the project

1. **Overview:** the status in corpus terms, the decision sought and who takes it, expected Risk Tier 2, the time-box, and the three journey options in one table.
2. **Initiative Brief:** one page on the corpus template; hypothesis, 2–4 leading indicators as references to their sources, MVP (one journey, one team, read-only), cost and effort, time-box, Risk Tier, and the role mapping.
3. **Journey options:** one comparison table with the selection rule, then a one-page annex per journey with only what differs.
4. **How the pilot works:** problem, what is built, the case workflow, what the employee can do, the scope boundary.
5. **Controls and evidence:** data and model hosting, the Tier 2 obligations, mandatory gates, the one acceptance rule, evidence sizes that fit the Bank's volumes.
6. **Technical design** (the blueprint at about 40%), **journey technical profiles** (kept, aligned), **IT readiness checklist** (the platform map, as the single home for technical decisions).

## Refit into the AICC flows

The owner's direction: keep the intent, the scenario and a recognizable project-management shape, and refit the project into the AICC flows, assuming they can carry the discipline; add only what is missing. Two readings of the full corpus against the project produced the detailed maps: [refit-intake-portfolio-engagement.md](refit-intake-portfolio-engagement.md) and [refit-lifecycle-delivery-controls.md](refit-lifecycle-delivery-controls.md). This section is the combined design.

### The project in AICC terms

- **What it is:** an Engagement with Customer Service as the client function, under Strategic Priority 1 (customer intelligence), in the service category Workplace automation, whose catalog already names case assistance reviewed by a person (Business Model 4.5). It is a new Initiative, linked to INI-006: INI-006 studies front-office inefficiency in aggregate and ends in a proposal; this project builds a case-level assistant for one team.
- **Who decides:** the Domain Owner (Head of Customer Service) approves the business case and the Solution Definition and accepts the result; the AICC Lead runs the Initiative and assigns the Risk Tier; the Control Function Contacts clear and validate; the journey's process function (Payments, Disputes or Onboarding) is a Dependency that approves its action list and supplies experts, unless it claims part of the benefit.
- **Risk Tier 2,** on one condition: the model is an Assistant that holds no tools; every write is the employee's action in the workspace. With write rights it would be Tier 3.
- **Model hosting:** in the Bank. An external model only after the provider check and approval for the data class; introducing one later is a significant change.

### The path, with the project's own steps kept

| Project step (kept as the reader knows it) | AICC step | Decided by | Record |
| --- | --- | --- | --- |
| Idea and journey shortlist | Funnel (Proposed) | AICC Lead takes it in | Portfolio Backlog entry |
| Journey selection, ownership, baseline from existing figures | Reviewing (Discovery: Scoping), then Analyzing (Discovery: Business case) | AICC Lead with the Domain Owner | Initiative Brief and journey annex; Service Agreement for the study |
| Charter approval | Approval of the business case after clearance by the Control Function Contacts | Domain Owner | Initiative Brief, Control Sign-Offs, Decision Record |
| Mobilization | Ranked and pulled into the MVP | AICC Lead | Portfolio Backlog |
| Historical validation (reconstruct past cases, check accuracy) | Phase 1 of the MVP: an Experiment in the Lab on read-only extracts, ending in an Outcome Report | AICC Lead; Domain Owner reviews | Solution Definition (Experiment), Outcome Report |
| Readiness for live use | Validation by the Control Function Contacts, Team final acceptance, the Bank's change management | Contacts; AICC Lead; change management | Control Sign-Offs; release block |
| Controlled live use by one team | Phase 2 of the MVP: the first Solution (a Service run by AICC, with a sunset rule) deployed to its first users | Domain Owner accepts | Solution Definition (Service), business acceptance |
| Pilot acceptance and the scale decision | Decision after the MVP: continue, pivot, defer or reject (or return with an extension) | Domain Owner | Decision Record, Decision Log |
| Scale and continuing ownership | Release with the Acceptance Checklist, or a Proposal and a Handover to an IT function as Receiver | Domain Owner; Receiver | Acceptance Checklist; Proposal; Handover |

The two readings differed on one point: whether the live pilot is an Experiment (which the corpus confines to the Lab, without a consumer) or a Service. Splitting the MVP as above resolves it without changing the corpus: the Experiment covers the project's own historical validation in the Lab, and the live pilot is a Service with first users. This is the order the project already proposed.

### Project-management content kept, and where it lives

- **Charter:** kept as the name of the page, holding the Initiative Brief and the journey annex. "Decision requested", "Approval record" and "Ownership to name before signature" map to Brief section 6, the Control Sign-Offs and the Decision Record.
- **RACI:** kept as a table on the governance page, with corpus Roles and at most three Bank roles (process-function head, Service Operations Manager, source owner of the figures); builders removed from acceptance.
- **Workstreams:** kept as a view; each Feature is labelled with its workstream, and Service Agreement Part B names who works on each.
- **RAID log, decision log, change control:** the Risks and Issues Record, the Decision Log, and the significant-change rule; no separate logs.
- **Governance forum:** the Iteration Review and Demo and the monthly Steering; no separate forum.
- **Gates A–Q and the "CTO decision":** become the evidence checklist that the corpus deciders read; reuse of components becomes a Proposal to the Platform Owner.

### Gaps and the smallest additions

1. **Cost, effort and time-box of the MVP,** and the business team's capacity: Brief section 4 asks for the full-scope estimate but not the MVP's; add one line there, and list contributing Roles and availability in Service Agreement Part B. PRI-1 has no Envelope yet: a Steering action.
2. **Measurement and evidence design** (eligibility, formulas, comparison design, sample sizes, observation period): a project annex to the Brief.
3. **IT commitments and operating readiness before the first users:** a project annex (IT readiness checklist) and one row in the release block.
4. **"Extend and measure more":** use the gate's existing Return, with the extension stated in the Decision Record.

### The page set

1. **Overview:** what the pilot does, its status in AICC terms, the decision sought and by whom, Risk Tier 2, the time-box, the three journey options.
2. **Charter:** the Initiative Brief and the measurement annex.
3. **Journey options:** one comparison table and selection rule; one short annex per journey.
4. **Governance and roles:** the path above, the RACI on corpus Roles, workstreams, records.
5. **How the pilot works:** problem, what is built, the case workflow, what the employee can do, the scope boundary.
6. **Controls and evidence:** data and model hosting, Tier 2 obligations, gates as evidence, one acceptance rule.
7. **Technical design** (the blueprint, cut to about 40%), **journey technical profiles** (kept, aligned), **IT readiness checklist** (the platform map, as the single home for technical decisions).
