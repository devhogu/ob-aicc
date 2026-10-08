# Research report: PMI and PMO practice

Collected on 2026-10-08 by an independent research agent for the flow redesign (change C-FLOW-REDESIGN), from the brief in this folder. Source quality is stated in each report: claims marked unverified come from memory, and several official pages (SAFe, PMI, ITIL) were gated or paywalled, so summaries and practitioner pages were used.

**Research return: a light portfolio-to-team process for a small AI unit in a bank**

I checked sources 1, 2, 3, 4 and 6 through search or fetch. SAFe's own page is behind a login. The PMI pages returned 403 for fetch, so for PMI I relied on search summaries. Claims marked "unverified" come from my memory.

**1. Best-fit practices**
- **PMBOK 7 "tailor based on context" plus "focus on value" (controls, Portfolio).** Tailoring is a principle, not an exception. The unit should publish its own tailored profile, not carry the full process by default.
- **Guardrails and thresholds instead of per-item approval (Portfolio, decision-making).** SAFe Lean Portfolio Management uses investment horizons, capacity allocation, an approval threshold and business-owner engagement. Work below the threshold is authorised inside the value stream, and only large or risky work gets a formal review with a short business case. For three people this replaces most approval layers.
- **Appetite plus circuit breaker, from Shape Up (Portfolio, Program).** Each initiative gets a fixed time and effort budget decided before work starts. If it does not finish, it is not extended by default; it goes back for reshaping or is dropped. This replaces the "Decision after MVP" ceremony with a pre-agreed rule.
- **Benefits management (Discover, Portfolio, closure).** Record one named owner, a measurable benefit and a measurement date per initiative. Check the benefit after delivery, not only at "Done". The UK Government guidance calls for benefits that are specific, measurable, agreed, realistic and time bound.
- **Flow metrics and WIP limits (Program, Team).** Track cycle time, throughput, age of items in progress and blocked items. Use these as the evidence for decisions and drop status reports. (Kanban, Lean; unverified as to a specific source.)
- **Agile Practice Guide hybrid thinking (Team, Program).** Choose the approach per kind of work. Run-rate work is a flow system; an initiative is timeboxed and iterative. This supports having one profile per kind of work.
- **PMI portfolio standard: governance, strategic alignment, performance.** Keep these three questions at the portfolio level and nothing heavier. Its governance domain asks who decides, how and with what accountability.
- **Lightweight lessons learned (closure).** Hold a 30-minute retrospective at closure. Record at most five reusable lessons and link them to the relevant risk tier or control. (Unverified as a specific PMI rule.)

**2. Decision rights and forums**
- **Intake and Scoped.** The Discover lead (the unit lead) decides on a pre-agreed rule: strategic fit, risk tier assigned, data class known. No meeting.
- **Approval of an Initiative Brief.** The Domain Owner or Executive Sponsor decides asynchronously on a one-page brief. Hold a meeting only above the threshold of cost, risk tier or cross-function impact, and set the threshold in advance.
- **Prioritisation.** Rank by WSJF at one monthly session. Capacity allocation (for example 60% initiatives, 20% run-rate, 20% enablers and debt) is set quarterly. Within that, the team pulls without asking.
- **Decision after the MVP (continue, pivot, defer, reject).** Make it by rule. Stop automatically when the appetite or the benefit hypothesis fails; otherwise continue, with no meeting. The sponsor is told and may object within a fixed window.
- **Acceptance.** The Domain Owner signs off against the criteria in the card. Independent testing and model-risk sign-offs are separate control gates (see point 5).
- **Forums.** Keep one monthly forum (priorities, WIP, blocked items, benefits due) and one quarterly forum (envelopes, guardrails, strategy). Fold the yearly forum into the Q4 quarterly. Do not add a separate Program-level forum for a unit this size.

**3. Artefacts to keep, and paperwork to drop**
- **Discover.** Keep the scenario catalogue and the Funnel as a list with a status and a reason for each exit. Drop detailed requirements at this stage.
- **Portfolio.** Keep the one-page Initiative Brief (problem, outcome and measure, owner, appetite, risk tier, data class, rule for stopping). Keep the decision log and the benefits register. Drop the long business case below the threshold.
- **Program.** Keep a Feature list with dependencies, the PI or Iteration goals, and a combined risk and impediment log. Drop PI-level status decks.
- **Team.** Keep Jira stories and bugs with flow data, Definition of Done and acceptance evidence. Drop effort estimation beyond relative sizing.
- **Minimum fields of a live project card.** The card is the single place a reader looks, and its fields come from the artefacts above.
  - Identity: ID, title, kind (run-rate or initiative), level and stage.
  - People: sponsor or domain owner, delivery lead, and RACI (who is responsible, accountable, consulted, informed).
  - Outcome: problem, intended outcome, benefit measure with baseline, target and date.
  - Constraints: appetite (time and effort), start date, planned review date.
  - Regulated context: risk tier, data class, and links to clearances (model risk, information security, independent testing).
  - Live state: status, next step, top three risks and impediments, dependencies.
  - Audit trail: decisions with date, who decided and why, scope changes, and a link to the Jira epic.
  - Closure: result, benefit check date, and up to five lessons.

**4. What to avoid or discard**
- **Stage-gate sign-offs on every move across the Kanban.** Keep gates only where an external control requires them. With three people, a gate costs a day of the unit's capacity. A Kanban column is a state, not an approval. (Stage-gate versus lean-agile: practitioner consensus, unverified as a specific source.)
- **Parallel forums at each level.** They mostly repeat each other with the same few people.
- **Full SAFe machinery.** Program Increments with planning events, Release Train roles and a large Lean Business Case do not fit a team of three. Keep the vocabulary only where it does real work.
- **Status reports, Gantt plans and detailed baselines.** Replace them with live card data and flow metrics.
- **Two sources of truth.** The site is a projection of Jira and must not hold state of its own.
- **Automatic extensions.** They hide failing work.

**5. Points that matter in a regulated bank**
- Control gates must be **mandatory and independent**. Model-risk, information-security, data-class and independent-testing clearances are not "agile ceremony" and must not be merged into team ownership. Record each as a field and link to the evidence.
- Keep the **decision log and audit read access**: who approved what, on which evidence, on which date. Make it immutable or versioned. The card and the Jira history serve this.
- Assign **risk tier at intake** and let it drive the threshold. A higher tier gets a formal review and a longer path; a low tier follows the light path.
- Retain records for the period set by the bank's policy. (Retention period: unverified, check with Compliance.)
- Write the pre-agreed rules down and get them **approved by the Executive Sponsor and Risk once**. A rule-based decision then counts as governed, not ad hoc.

**6. Sources**
1. Project Management Institute, "PMBOK Guide 7th ed. and Standard for Project Management", 2021, search summary only: https://www.skillsoft.com/book/the-standard-for-project-management-and-a-guide-to-the-project-management-body-of-knowledge-pmbok-guide-seventh-edition-8a4cd99c-b774-445e-8cf3-d3070211e59d (unofficial listing; the official text is in a paid guide).
2. Agility at Scale, "SAFe Lean Budget Guardrails", practitioner write-up of SAFe LPM, current: https://agility-at-scale.com/safe/lpm/portfolio-guardrails/. Official page behind a login: https://framework.scaledagile.com/lean-portfolio-management
3. Basecamp, "Shape Up, The Circuit Breaker", 2019: https://basecamp.com/shapeup/2.2-chapter-08
4. Project Management Institute, "The Standard for Portfolio Management, Fourth Edition", 2017: https://www.pmi.org/pmbok-guide-standards/foundational/standard-for-portfolio-management (fetch returned 403; only search summary read).
5. Project Management Institute, "Agile Practice Guide", 2017, shop listing only: https://www.pmi.org/shop/p-/book/agile-practice-guide-(italian)/00101603201
6. UK Government, "Guide for effective benefits management in major projects", UK Government Project Delivery Function, search summary only: https://www.gov.uk/government/publications/guide-for-effective-benefits-management-in-major-projects
