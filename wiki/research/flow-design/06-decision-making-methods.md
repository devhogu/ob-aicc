# Research report: Decision-making methods

Collected on 2026-10-08 by an independent research agent for the flow redesign (change C-FLOW-REDESIGN), from the brief in this folder. Source quality is stated in each report: claims marked unverified come from memory, and several official pages (SAFe, PMI, ITIL) were gated or paywalled, so summaries and practitioner pages were used.

Not fetched in full: the RACI-limits claim, Team Topologies' size guidance, and bank-regulator specifics beyond SR 11-7 (all marked unverified below). The Bezos letter fetch returned a muddled summary, so I cite it only for the Type 1 / Type 2 idea.

## 1. Best-fit practices (7)

1. **One-way / two-way doors** (decision-making, all levels). Classify each decision as hard or cheap to reverse. Two-way decisions go to one person immediately, and only one-way decisions get deliberation. This removes most gates for a team of three.
2. **Advice process** (Portfolio, Program). Anyone may decide, but must consult the people affected and the experts, and record the advice. A weekly or fortnightly advisory slot reviews decisions that are already written up. It is a record-and-consult step, not an approval queue.
3. **Kanban explicit policies + Service Level Expectation** (Portfolio, Program, Team). Pull criteria, WIP limits, definitions of ready/done and classes of service are written on the board. The Kanban Guide expresses the SLE as a time and a probability, taken from cycle-time history. Policies are decided once and then applied as a rule, with no meeting.
4. **Four classes of service** (Portfolio, Program). The classes are expedite, fixed date, standard and intangible. They cover the exceptions without a new forum. Allow one expedite item at a time.
5. **WSJF as a tie-breaker** (Portfolio). Use relative cost of delay divided by relative size, and score only when more than WIP-limit items compete. Skip it for run-rate work.
6. **Light decision record** (controls). One ADR/MADR-style entry per decision: context, options, decision, consequences, advice received, status. Keep it to 5-10 lines.
7. **Consent for forum decisions** (Portfolio). Ask "do you object?" with the test "good enough for now, safe enough to try". Objections must be argued as harm. This avoids the stalemate that consensus produces.

DACI/RAPID: use only the vocabulary, as three roles on the card (Driver, Decider, Consulted). Do not run it as a framework.

## 2. Decision rights and forums

| Decision | Decider | Evidence | Rhythm / mechanism |
|---|---|---|---|
| Intake, Scoped | Unit lead (or the Driver) | One-line need, owner named | Async on the board, within an SLE (for example 3 working days) |
| Approval of an Initiative | Domain Owner (one person, per RAPID "Decide") | Brief, cut to one page | Monthly forum, or async if no objection in 5 days |
| Pull into WIP | Rule | Free slot + WSJF rank + class of service | No meeting |
| Run-rate work | Unit lead | Fits the standing Initiative's envelope | No meeting |
| Decision after MVP (continue, pivot, defer, reject) | Domain Owner, advised by the unit | Pre-agreed exit criterion and the measured result | Quarterly forum |
| Acceptance | Named acceptor, plus independent test where the tier requires it | Acceptance criteria | At Feature level, async |
| Strategy, envelopes, guardrails, shared services (data, platform, clearances) | Executive Sponsor | Yearly review | Yearly forum |

Rules that replace meetings:
- WIP limits.
- The envelope: spend within it needs no approval.
- Kill criteria: a stalled item with no movement for N days goes to a "stop or resume" check automatically.
- Class-of-service policies.
- Two-way decisions need no forum.

Keep central: strategy, guardrails, risk tiers, shared services. Decentralise everything inside them.

## 3. Artefacts

**Keep**
- Discover: one scenario catalog and the Funnel list, each need with a name and a one-line value.
- Portfolio: the Initiative card (one-page Brief, tier, owner, WSJF inputs), the decision log, and the exit criterion set at approval.
- Program: Feature cards, a monthly cumulative flow or aging view, and risk and clearance status.
- Team: the Jira stories.
- Controls: the clearance trail (model risk, security, data class) linked from the card, and the audit read access.

**Drop**
- A separate status report (the board is the status).
- Monthly slide decks.
- RACI matrices per Initiative.
- Duplicate site copies of live data.
- Full WSJF scoring for run-rate work.
- A six-section Brief for small Initiatives (use a short form and expand it for higher tiers).

## 4. Avoid or discard

- Three standing forums for three people: merge them. Hold one monthly Portfolio forum of 45 minutes, plus a yearly strategy review. Make the quarterly review a section of the monthly forum every third month.
- Separate Reviewing and Analyzing columns can be one "Shaping" column. Two states for one activity create waiting.
- RACI as a design tool: it describes who is involved, not who decides, and it multiplies "consulted" (unverified, from memory). Name a single Decider.
- Four levels of Kanban at this size: keep at most Portfolio and Program boards, and keep Team in Jira.
- Consensus and committee approvals.
- Quarterly Program Increment planning events: a rolling three-month forecast on the Program board does the job.
- Decision queues: set a timebox on every pending decision. If the SLE lapses, the default is "proceed" for two-way decisions and "escalate to the Domain Owner" for one-way ones. Escalation is one step up, with a named person.

## 5. Regulated bank

- Independence is not optional. The tester, the validator and the model-risk clearer must differ from the builder. Put them as Consulted-with-veto on the card, not as a forum.
- SR 11-7 (US, but widely used as a reference) asks that validation rigor match model materiality and that challenge be effective. So run a tiered path: low-tier work follows the light path, and higher tiers add clearances. Check the National Bank of the Kyrgyz Republic requirements locally (unverified).
- Every one-way door in a bank (production data class, customer-facing model, vendor) needs a recorded decider, advice and date. The ADR log can serve as audit evidence if it is append-only and read-accessible.
- Expedite must still pass the controls. Class of service changes order, never clearance.

## 6. Retro and forum recipes

**Portfolio forum (45 min, monthly)**
- Inputs, circulated 2 days ahead: board snapshot, new Briefs, items past their SLE, WSJF for contested pulls, decisions made async since last time.
- Agenda: (1) ratify async decisions (5 min); (2) objections on new Briefs, by consent (15); (3) post-MVP decisions (10); (4) stuck items and blockers (10); (5) policy changes (5).
- Outputs: log entries only, with decision, decider, date, review date.

**Decision retro (30 min, quarterly, inside the forum)** Sample 5 logged decisions. For each ask: Was it reversible, and did we treat it so? How long did it wait? Did the advice change it? Would we decide the same today? Then change one policy (a limit, a timebox or a tier threshold). Track decision lead time as the single metric.

## 7. Sources

- Fowler, "Scaling the Practice of Architecture, Conversationally" (advice process, ADR): https://martinfowler.com/articles/scaling-architecture-conversationally.html (Thoughtworks, 2021). Fetched.
- Amazon 2016 shareholder letter, Type 1/Type 2 decisions: https://www.sec.gov/Archives/edgar/data/1018724/000119312516530910/d168744dex991.htm (Amazon via SEC, 2017). Fetched; the summary was partly garbled.
- Atlassian DACI play: https://www.atlassian.com/team-playbook/plays/daci (Atlassian, undated). Fetched. Its "25% higher success rate" figure is unverified.
- Bain RAPID: https://www.bain.com/insights/rapid-tool-to-clarify-decision-accountability/ (Bain, undated). Fetched.
- Sociocracy For All, consent: https://www.sociocracyforall.org/consent-decision-making/ (SoFA, undated). It returned 403 on direct fetch; content seen via search snippets only.
- ADR site and MADR: https://adr.github.io/ (ADR community, undated). Fetched.
- Kanban Guide: https://kanbanguides.org/the-kanban-guide/2020.12 (Orderly Disruption and Vacanti, 2020). Seen via search snippets.
- Kanban glossary (classes of service): https://kanban.university/wp-content/uploads/2023/04/The-Official-Kanban-Guide_Glossary.pdf (Kanban University, 2023). Seen via snippets.
- SAFe WSJF: https://framework.scaledagile.com/wsjf/ (Scaled Agile, undated). Fetched.
- CD3: https://www.emergn.com/insights/the-cost-of-delay/ (Emergn, undated). Snippets only.
- Team Topologies interaction modes: https://teamtopologies.com/key-concepts (Team Topologies, undated). Fetched.
- SR 11-7: https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm (Federal Reserve/OCC, 2011). Snippets only.
- Unverified (memory): the RACI limits, the monthly-forum timings, the SLE defaults, and the Kyrgyz regulator requirements.
