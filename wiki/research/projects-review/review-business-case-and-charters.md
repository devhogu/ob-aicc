# Review A: Business case and the three journey charters (EN)

Scope: en-1 Business case, en-3 Payment Issue Resolution, en-4 Card Dispute Progress Support, en-5 Onboarding/KYC Progress Support, read with en-0 Overview, en-2 Selection guide, the rendered diagrams, and the AICC corpus (Business Model, Portfolio Management Model, Solution Lifecycle Model, AI Policy, Vocabulary, Initiative Brief and Solution Definition templates).

## Verdict

1. The pilot itself is sensible and well bounded: one journey, one team, employee review of everything, regulated decisions excluded, historical validation before live use.
2. The documents describe a separate bank project process. AICC, Initiative, Domain Owner, Executive Sponsor, Risk Tier, Solution Definition, and AI Registry do not appear once in the six documents.
3. An approver cannot decide on them as written. There is no cost, effort, duration, or time-box, and the order of baseline, approval, and initiation is circular.
4. Risk classification, control approvals, and release authority contradict the AI Policy and the Solution Lifecycle Model.
5. The material is about three times longer than it needs to be. About 70% of each charter repeats the business case. Fix the corpus mapping first, then merge and cut.

Note on the brief: the corpus offering types are Experiment, Product, and Service (Business Model 4.3). A Proposal is the output of an Experiment, not an offering type.

## Critical findings

### C1. A parallel project process replaces the AICC portfolio and lifecycle

- Where: en-1 "Project Manager initiation responsibilities", "Project governance", and "Scope boundary"; en-2 opening; en-3/4/5 "Ownership to name before signature".
- Evidence: "it enters the bank's normal project-initiation process" (en-2). "The Project Manager converts this use-case definition into the bank's project-initiation form" (en-1). "maintain the project backlog, RAID log, decision log, change control" (en-1). "establish the governance forum, reporting path, escalation route, and decision cadence" (en-1).
- Problem: The work never enters the Portfolio Kanban (Funnel, then Reviewing, then Analyzing, then Approval, then MVP). It has no Initiative Brief, no Service Agreement, no Solution Definition, and no AI Registry entry. It also sets up its own records and forum, although Portfolio Management Model 9.4 says "the AICC Lead shall add no other record to track the Portfolio" and Solution Lifecycle Model 6.8 allows no other delivery event. The site register lists the item in AICC's Delivery Pipeline, so a reader will assume AICC governance applies, yet the text routes everything to a bank PMO. Vocabulary 3.9 says portal pages "use the terms of this Vocabulary and state no rule of their own". These pages state many rules and none of the terms.
- Recommendation: Declare the item an Initiative and an Engagement, with Customer Service as the client function. Give it an INI identifier and its corpus state, which today is Proposed or Discovery: Scoping. The business case becomes an Initiative Brief. The pilot becomes the MVP: the first Solution, with its own Solution Definition. Use the corpus records: Decision Log, Risks and Issues Record, Portfolio Backlog, and Steering. If the bank's PMO or IT intake must also run, for funding outside AICC or for IT build capacity, say so in one sentence and record it as a Dependency. It should not be the governing route. Add a role-mapping table (see "Target structure").

### C2. Risk classification, control approvals, and model hosting contradict the AI Policy

- Where: en-1 "Decision structure" and "RACI" (row "Confirm risk classification and operating limits"), en-1 "Initial risk position" and "Banking dependencies" (row "Analytics environment"), and en-3/4/5 "Required control approvals" and "Approval record".
- Evidence: "confirm risk classification and operating limits: Head of Customer Service with required control-function concurrence". "Privacy/Data Use, Compliance/Conduct, and AI/Operational Risk — [names/functions]". "AI/Operational Risk [name/function, where required]". "approved processing, model access where used". "GenAI, and agentic solution" (en-2).
- Problem: Under AI Policy 3.2, the AICC Lead assigns the Risk Tier, any Control Function Contact may raise it, and only model risk may lower it. A business head does not confirm it. The use reads customer data and informs work that reaches customers under human review, which is Risk Tier 2 under AI Policy 3.1, yet no document says so. Tier 2 has these consequences, and all of them are missing:
  - the Control Function Contacts must clear the business case before approval (Portfolio Management Model 6.4);
  - model risk and information security must always validate (AI Policy 3.3), so "where required" is wrong, and information security is missing from every approval list;
  - bias and error testing is required before first deployment;
  - the Domain Owner must approve the use for the data class (AI Policy 2.1–2.2);
  - the model or provider must pass a provider check by information security, data protection, and legal before any customer data reaches it (AI Policy 4.1, 4.4).

  Where the model runs (on premises or with an external provider) is the most important bank-safety question here, and en-1 covers it in four words. "Agentic" in en-2 suggests an agent with rights over systems, which would be Tier 3 (AI Policy 3.1).
- Recommendation: State "Expected Risk Tier 2" in the overview and in each charter, with the four attributes and the reason. Name the Control Function Contacts the corpus requires: model risk, information security, data protection, compliance (which covers AML and conduct), and legal. Mark each as required at business-case clearance and at validation. Remove "where required". For KYC, state Financial Crime as the AML remit within compliance. Add one line: "The assistant has read-only access and no rights to execute actions or move funds." This keeps the use out of Tier 3. Add a dependency row for "Model hosting and provider check", owned by the Platform Owner, with the check under AI Policy 4.1.

### C3. The decision requested has no cost, effort, duration, or time-box

- Where: en-3/4/5 "Decision requested", en-1 "Benefit baseline" and "Project workstreams", and en-0.
- Evidence: "Authorize the named business team and capacity to establish the baseline, complete control decisions, operate the pilot, and return with evidence". The only economic content is "cost per contact or case where reliable data exists".
- Problem: An approver is asked to commit people and time with no figure for either. Portfolio Management Model 6.2 asks "Can it be afforded? The cost is within the Envelope", and the Initiative Brief needs "Cost and value" and a "Period". Nothing gives a pilot length, an observation period, a headcount or FTE estimate for the four workstreams, or the cost of model use. No document says who pays: under Business Model 6.2 the Domain pays run, license, and provider costs, and AICC does not charge.
- Recommendation: Add a short "Cost, effort and timeline" block. Cover the estimated effort per role for each phase (selection and baseline, historical validation, live pilot, comparison), the pilot time-box in Iterations, the observation period, run and provider cost as a reference to financial planning, and the Envelope. State that figures stay in the source systems and the brief references them.

### C4. The order of baseline, approval, and initiation is circular

- Where: en-1 "Benefit baseline" and "Pilot acceptance", en-2 opening, and en-3/4/5 "Decision requested".
- Evidence: "Before approval, the Benefit Owner and Measurement Owner establish a baseline" (en-1). "Charter approval authorizes mobilization, baseline work" (en-2). "Authorize … capacity to establish the baseline" (en-3). "meet the targets recorded in the project-initiation record" (en-1).
- Problem: The baseline is a precondition of approval and also something the approval pays for. The documents use three overlapping approval records: the charter, the project-initiation form, and the project-initiation record. A reader cannot tell which is authoritative or in what order they are signed.
- Recommendation: Use the corpus sequence. In Discovery: Scoping, the AICC Lead and the Domain Owner select the journey and confirm that a baseline source exists. In Discovery: Business case, the Initiative Brief names the 2–4 leading indicators and references their source, with the full baseline computed as the first MVP task. The Control Function Contacts clear the brief. The approver approves it, and the Decision Record is the approval. Then pull, MVP, first users, and the decision after the MVP. Keep one record (the Initiative Brief) and delete "project-initiation form/record".

## Major findings

### M1. Corpus terms are used with different meanings

- Where: the Delivery Pipeline register status, en-0 eyebrow, en-1 title, en-2 and charter titles, and en-1 RACI legend.
- Evidence: Status "Proposal". "Project proposal". "Candidate Project Charter". "Business Sponsor", "Co-sponsor", "Sponsor". "DO: relevant Data and Source-System Owners". The page labelled "Business case" contains no costs or options.
- Problem:
  - In the corpus, a Proposal is what an Experiment ends in: a proposal to adopt at scale (Proposal template). Here it is used for the very first stage.
  - "Charter" collides with the AICC Charter.
  - Vocabulary says Executive Sponsor "identifies the defined AICC Role, rather than any person providing general sponsorship", yet "Sponsor" here means the Head of Customer Service.
  - "DO" is the natural short form of Domain Owner.
  - The Vocabulary defines a business case as "need, options, expected benefits, costs, risks". This page has none of the costs or options.
- Recommendation: Use "Proposed (Funnel)" or "Discovery: Scoping" as the status. Rename "project charter" to "journey option" or "journey annex to the Initiative Brief". Replace Sponsor with Domain Owner, and with Executive Sponsor where Portfolio Management Model 6.3 requires. Rename the "Business case" page to "Delivery and operating approach" unless it gains costs and options. Spell out Data Owners.

### M2. Live use, scale, and reuse are approved by the wrong person, and the corpus gates are missing

- Where: en-1 "Decision structure", "Project controls", and "Pilot acceptance"; en-3/4/5 "Acceptance rule".
- Evidence: "approve controlled live use: Head of Customer Service". "approve scale or reuse: Business Sponsor". "The Sponsor may approve scale when…". "suspend live use: Service Operations Manager or designated control authority".
- Problem: Under Solution Lifecycle Model 7, live use by one team is the first deployment to First users. That requires a test by someone other than the builder, Tier 2 validation by the Control Function Contacts, the AICC Lead's final acceptance of the Team, and the Bank's change management. The business acceptance by the Domain Owner follows, and then a separate release decision beyond the first users with a signed Acceptance Checklist. "Scale" is the decision after the MVP (continue, pivot, defer, or reject) by the approver under Portfolio Management Model 6.3. Because AICC does not run a Solution at Bank scale (Business Model 2.5), scaling also needs a named Receiver and a Handover.

  Two further gaps. Reuse in another journey (lending, complaints) is a new Initiative or Capability for another Domain, not a decision for Customer Service. And the documents never say whether Payments, Disputes, or KYC operations are separate Domains. If they are, the Initiative spans Domains, and the Executive Sponsor approves it and accepts it (Portfolio Management Model 6.3, Solution Lifecycle Model 7.3(c)). AI Policy 5.6 gives suspension authority to the AICC Lead and any Control Function Contact, and they are not listed.
- Recommendation: Rewrite the decision table on the corpus gates in this order:
  1. Business case approval.
  2. Solution Definition and Risk Tier.
  3. Validation.
  4. Team final acceptance.
  5. First deployment to the named pilot team.
  6. Business acceptance.
  7. Decision after the MVP.
  8. Release with the Acceptance Checklist, or a Proposal and a Handover to an IT Receiver.

  Decide whether the process functions are Domains, or are Dependencies that supply sign-offs. Add the AICC Lead and the Control Function Contacts to the suspension authority.

### M3. Too many roles with unstable names, and the separation of duties is broken

- Where: en-1 "Benefit baseline", "Project workstreams", "Project Manager initiation responsibilities", and "RACI"; en-3/4/5 "Ownership" tables.
- Evidence: "Benefit Owner", "Measurement Owner", "Service Owner owns the customer outcome", "Service Quality Lead", "SQL: Service Quality and Measurement Lead", and "Service Quality / Management Information owner independent of delivery acceptance". In the RACI, "Accept analytical and workflow quality" has TDL = R and SQL = R.
- Problem: About fourteen roles appear for a one-team pilot. "Service Owner" and "Benefit Owner" are never defined. They may be the Head of Customer Service, who is already the "Sponsor". The Measurement Owner is declared independent, but the same function owns the controls-and-measurement workstream and is R in quality acceptance. The Technology/Data Delivery Lead builds the capability and is also R in accepting it, against Solution Lifecycle Model 7.5 ("The person who builds … shall not test, check, or validate it"). "SQL" as an abbreviation will confuse every technical reader.
- Recommendation: Collapse the roles to the corpus Roles plus at most three bank roles. Domain Owner (Head of Customer Service) owns the outcome and the benefit. AICC Lead runs the Initiative and is product owner. Solution Engineer builds. Domain Experts come from the pilot team and the process function. The Control Function Contacts clear and validate. The three bank roles are the process-function head (who approves the action catalogue), the Service Operations Manager (who runs the pilot team), and the MI source owner (who provides the figures). Remove builders from acceptance. Drop all abbreviations from the RACI.

### M4. Three different acceptance rules

- Where: en-1 "Pilot acceptance", en-2 "Common acceptance logic", and en-3/4/5 "Acceptance rule" and "Proposed success measures".
- Evidence: en-1 says "meet the targets … or provide sufficient directional evidence for the Sponsor's stated next decision", and it also lists "Investigation or handling effort improves" and "Repeat contact … improves" without any condition. en-2 says "passes only when all mandatory quality and control-limit criteria pass and the primary outcome provides sufficient evidence for the Sponsor's stated scale decision". en-3 says "primary customer outcome and one operational benefit meet their confirmed targets". Also: "Proposed targets are starting thresholds … confirm or replace them" against "no lower than 95%".
- Problem: The pass condition differs between documents. The en-1 version cannot fail, because whatever the evidence supports counts as success. A floor that can be "replaced" is not a floor. The documents never say which criteria are mandatory gates and which are measures.
- Recommendation: State one rule, once, in the common part. Split it into (a) mandatory gates, as Solution Definition acceptance criteria in Given/When/Then form (traceability, critical-error handling, control limits), and (b) 2–4 leading indicators in the Initiative Brief, with the decision after the MVP mapped to the evidence: targets met means continue; gates pass but the result is inconclusive means pivot or defer with a defined extension; a gate fails means reject or stop. The charters then hold only journey-specific values.

### M5. The "customer intelligence" framing is not bank-safe

- Where: en-0 title and lead, en-1 "Use-case intent" and "Execution rule".
- Evidence: "records the outcome as reusable customer intelligence". "creates a first practical customer-intelligence asset". "Reusable customer intelligence" (en-0). These sit against "Inferred blockers … do not become permanent customer facts" (en-1).
- Problem: In a bank, "customer intelligence" suggests profiling and marketing reuse, which goes beyond the stated purpose (service resolution) and conflicts with purpose limitation and data minimization (AI Policy 2.5). The documents contradict themselves: outcomes become a reusable asset, yet inferences are not kept as facts. Data protection is likely to reject the name.
- Recommendation: Rename the project to plain words, for example "Service Case Assistant: one view of a customer's unresolved issue". State that pilot outputs are used only for service resolution and for evaluating the assistant. Reuse for another purpose needs its own approval. "Reusable" should refer to components and evaluation sets, not to customer data.

### M6. Evidence sizes and targets do not fit a one-team pilot in a mid-size bank

- Where: en-1 "Pilot acceptance", en-2 "Minimum evidence expectation", and en-3/4/5 "Proposed success measures".
- Evidence: "approximately 1,000–3,000 eligible cases in each pilot and comparison population". "planning hypothesis: 15–20% relative improvement" appears for every measure in all three charters.
- Problem: The arithmetic is correct: 30% to 25.5% needs about 1,500 cases per arm. But one disputes or onboarding-support team at a mid-size Kyrgyz bank is unlikely to see that many eligible open disputes or stalled applications in a pilot period. The documents never say how the comparison population is built (other teams, a period before the pilot, or alternating cases), so the outcome claim has no design. Identical 15–20% hypotheses for three different journeys, and for every measure within a journey, read as placeholders.
- Recommendation: In each journey annex, give an order-of-magnitude monthly volume (as a reference to its MI source) and the resulting feasible claim. Lead with operational and quality measures that a small sample can show (handling time, correct next step, repeated information requests). Treat the customer-outcome effect as directional unless the volume supports more. Name the comparison design. Set journey-specific planning hypotheses, or none.

### M7. Local realism: language, systems, functions, and foreign concepts

- Where: en-1 "Banking dependencies", "Business-domain placement", and "Risk, Compliance, Conduct, and Privacy coverage"; en-2 "Control-limit expectation"; en-3 exclusion table; en-4 "Excluded".
- Evidence: "calls, chat, email, branch". "median investigation or handling effort [workforce/case source]". "Compliance/Conduct". "vulnerability indicators". "monitored non-inferiority measures". "statutory or scheme deadlines". "cross-border or correspondent payments" (excluded).
- Problems:
  - Contact notes and chats will be in Russian, Kyrgyz, and mixed or transliterated text. Neither the GenAI interpretation nor the 95% quality floor accounts for that.
  - Calls need transcription, which is weak for Kyrgyz.
  - The documents assume a stable customer ID across systems, a case-workflow system with step timestamps, workforce data for handling time, a service-desktop side panel, and separate Disputes Operations, Conduct, Service Quality/MI, and Knowledge-owner functions. A mid-size bank may have only some of these.
  - "Vulnerable customer" and "non-inferiority" are UK/EU regulatory and statistical vocabulary.
  - The documents do not name the jurisdiction once. They mention "local regulatory obligations" a single time.
  - Excluding cross-border transfers may remove the largest payment-contact category, inbound remittances.
- Recommendation:
  - Add a "Local assumptions to confirm" list: languages of the records, whether voice transcription is in scope (suggest excluding it from the pilot), which system holds the case state, and how handling time is measured today.
  - Refer to the Bank's own requirements (NBKR consumer-protection rules for banking services, personal-data and bank-secrecy law, and card-scheme rules including Elcart), as confirmed by the compliance and legal Control Function Contacts under AI Policy 1.3.
  - Fold Conduct into Compliance.
  - Replace "non-inferiority" with "must not get worse than the baseline by more than the agreed tolerance".
  - Check payment-contact volumes by type before excluding cross-border transfers.

### M8. The communication control cannot be measured

- Where: en-1 "Initial risk position", en-2 "Control-limit expectation", and en-3/4/5 "Customer protection and control limits".
- Evidence: "Every customer communication and operational action receives employee approval". "zero … unreviewed communication".
- Problem: Most contacts are phone or branch conversations, where the employee speaks and there is nothing to "approve" or count. The control only makes sense if the assistant drafts written text (chat, SMS) and the documents say whether it does.
- Recommendation: Say exactly what the assistant produces. One version: "It produces no customer-facing text; the employee explains in their own words". Another: "It drafts written replies that the employee edits and sends from the existing channel; nothing is sent automatically". Define the zero-tolerance event to match, for example "a message sent without an employee send action".

### M9. Structure: the reader meets the playbook before the decision

- Where: all four documents.
- Evidence: en-1 is about 3,900 words, with nine H3 sections, eight diagrams, and six tables before the dependencies. In each charter, "Common delivery commitments", the ownership table, the evidence schedule paragraph, six of the eight risk bullets, and the approval record are word-for-word or near-identical.
- Problem: An approver needs the following, in this order: what is asked, of whom, at what cost, at which Risk Tier, by when, and how success is judged. That is spread across, or absent from, roughly 7,000 words. Only about 30% of each charter is specific to its journey: scope and exclusions, baseline measures, the quality criterion, and the stop conditions.
- Recommendation: See "Target structure". Keep one common Initiative Brief and one-page journey annexes that hold only the differences.

## Minor findings

### m1. Disclosure is treated as open, but the AI Policy already answers it

- Where: en-1, "Risk, Compliance, Conduct, and Privacy coverage".
- Evidence: "is AI transparency required?"
- Problem and recommendation: AI Policy 3.3 already answers this for Tier 2: disclosure is required where output reaches or affects a customer. Restate the question as "how disclosure is given, if written drafts reach customers".

### m2. Cohort and bias testing appears only in the KYC charter

- Where: en-5.
- Evidence: "test for materially different treatment across relevant customer cohorts".
- Problem and recommendation: Tier 2 requires bias and error testing wherever output affects persons. Move the requirement to the common part so it applies to all three journeys.

### m3. "Confidence" and "does not invent process steps" are claims, not controls

- Where: en-1 "Actions available to the employee" and "Initial risk position".
- Evidence: "It does not invent process steps." "Low-confidence … routes the case".
- Problem and recommendation: A language model cannot guarantee either. Rewrite as controls: "Proposed actions are limited to catalogue codes; any other output is discarded". "A case is routed to manual investigation when a required source record is missing or two records conflict." The second is rule-based and does not rely on the model's own confidence.

### m4. A later "customer-visible" stage is implied but never defined

- Where: en-1 "Project controls".
- Evidence: "Employee use with full review precedes customer-visible intervention."
- Problem and recommendation: This implies a stage that is out of scope everywhere else. Delete it, or state that such a stage would be a significant change with a new Risk Tier assessment.

### m5. "Zero critical errors" cannot be proven on a sample

- Where: en-3/4/5 quality rows.
- Evidence: "zero critical state … errors in release evaluation".
- Problem and recommendation: A 200–500 case sample cannot show a zero error rate. Use "no critical error found in the evaluation set; any critical error found blocks release until corrected and retested".

### m6. Charter structure differs across the three journeys

- Where: en-3/4/5 "Problem and selected scope"; en-5 ownership table.
- Evidence: Payment gives a table of exclusions with reasons, Dispute one sentence, and KYC a paragraph plus an information boundary. The KYC sponsor is "Head of Customer Service or Onboarding".
- Problem and recommendation: Use the same table in all three annexes. Name a single Domain Owner for KYC.

### m7. Baseline placeholders invite Bank figures onto the portal

- Where: en-3/4/5 "Benefit baseline to populate".
- Evidence: "[value]".
- Problem and recommendation: The Initiative Brief "carries no figures of the Bank: a figure is a reference to its source". Completed charters published on the portal would expose complaint and contact rates. Replace "[value]" with "[reference to MI report]".

### m8. Spelling and abbreviations

- Where: en-1 and en-3.
- Evidence: "catalogue" (4 times), "Contact-Centre", "RAID", "SSO", "IAM", "SOM", "TDL", "JPO", "CRC", and "[document version or commit]".
- Problem and recommendation: Vocabulary 3.2 requires American spelling: use "catalog" and "Contact Center". Spell out the abbreviations, or drop them. "Commit" is a version-control term managers do not use; use "version and date".

### m9. Page names do not match

- Where: en-1 and en-2 page labels.
- Evidence: en-1 is labelled "Business case" on the page and "Business use case" in the diagram labels. en-2 is "Candidate Project Charters" as a heading, "Project charters" as the eyebrow, and "Selection and evidence guide" in its diagrams.
- Problem and recommendation: Use one name per page.

### m10. The business case lists five journeys but only three have charters

- Where: en-1 "Journey selection".
- Problem and recommendation: The loan and complaint journeys are listed but get no charter, and the text does not say why. Add one sentence, for example "not proposed for the first pilot because…", or remove them.

### m11. Inflated or vague wording

| Current | Suggested |
| --- | --- |
| "assembles authoritative service context, uses governed GenAI to interpret what happened" | "brings the customer's contacts, cases and status together, and uses an approved AI model to summarize them" |
| "Each step must leave an owned reusable asset" | cut, or "Each step leaves a named output with an owner" |
| "The Head of Customer Service is the natural business sponsor" | "The Head of Customer Service is the proposed Domain Owner" |
| "evidence-sizing approach", "decision-sized evidence", "directional evidence" | "how many cases are needed", "enough cases for the decision", "an indication, not proof" |
| "The charter selects one primary customer outcome" | "The Domain Owner selects…" (documents do not decide) |

## Target structure

Role mapping, to be published once in the common part:

| Current term | Corpus equivalent |
| --- | --- |
| Business Sponsor / Sponsor / Service Owner / Benefit Owner | Domain Owner (Head of Customer Service); Executive Sponsor where the Initiative spans Domains or exceeds a guardrail |
| Journey Process Owner | Head of the process function, as Domain Owner if that function is a second Domain, otherwise a named Dependency owner whose approvals (action catalog, ground truth) are recorded; their specialists act as Domain Experts |
| Project Manager | AICC Lead (Initiative, portfolio, product owner), with Solution Engineer for build and deployment |
| Technology/Data Delivery Lead | Solution Engineer; Platform Owner for the AI Platform; Bank IT as Receiver at scale |
| Measurement Owner / Service Quality Lead | MI source owner; benefit confirmed by the Domain Owner (Business Model 7.3) |
| CRC / required control approvals | Control Function Contacts: model risk, information security, data protection, compliance (incl. AML/conduct), legal |
| Charter approval / project-initiation form | Approval of the Initiative Brief (Decision Record) after Control Function clearance |
| Controlled live use | First deployment to First users (the pilot team) after validation and Team final acceptance |
| Scale / refine / close | Decision after the MVP (continue / pivot / defer / reject); release with Acceptance Checklist, or Proposal and Handover |

Proposed set of pages:

1. **Overview (keep, rewrite).** State the status in corpus terms (INI id, Proposed or Discovery: Scoping), the decision sought and who decides, expected Risk Tier 2, the pilot time-box, and the three journey options in one table. Then the plain-language intent and limits: what the assistant does and does not do.
2. **Initiative Brief (new; replaces the front of the "Business case" and the common half of every charter).** One page on the corpus template: hypothesis, 2–4 leading indicators as references, scope and MVP (one journey, one team, read-only, employee review), cost, effort and timeline, risks and Risk Tier with the Control Function Contacts to clear it, the decision table, and the role mapping.
3. **Journey options (merge en-2 with en-3/4/5).** One comparison table with selection criteria, then one short annex per journey holding only what differs: scope and exclusions (same table format), baseline measures as source references, the journey quality criterion, stop conditions, extra control remit (AML for KYC; scheme rules for disputes), and feasible volume. Rename from "charter" to "journey option".
4. **How the pilot works (trimmed from en-1).** Keep: problem, what is built, the process integration map, the per-case operational workflow and diagram, the employee action list, and the scope boundary. Replace the delivery action workflow, workstreams, RACI, and governance tables with one sequence on the corpus gates (Discovery → Approval → MVP with Solution Definition → validation → first users → business acceptance → decision after MVP → release or Handover) and a short RACI using corpus roles.
5. **Controls and evidence (merge en-1 risk coverage and pilot acceptance with en-2 evidence and control limits).** This becomes the draft of Solution Definition sections 3–6: the data and model-hosting statement, the risk-coverage table, mandatory gates as Given/When/Then, control limits with suspension thresholds, and the evidence-sizing rule, with the worked statistics in a collapsible note.
6. **Cut or shrink.**
   - Cut entirely: "Project Manager initiation responsibilities" (replaced by corpus records), "Project controls" (duplicates the gates), "Execution rule", and the five-row domain-pairing table (keep only the chosen journey's pair).
   - Shrink: "Continuing ownership" becomes the Receiver field plus two lines; "Reuse after validation" becomes two lines, noting that reuse is a new Initiative or Capability.
   - Move "Benefit baseline dimensions" to the Initiative Brief guidance.
