# Research report: SAFe: portfolio and program

Collected on 2026-10-08 by an independent research agent for the flow redesign (change C-FLOW-REDESIGN), from the brief in this folder. Source quality is stated in each report: claims marked unverified come from memory, and several official pages (SAFe, PMI, ITIL) were gated or paywalled, so summaries and practitioner pages were used.

**SAFe research for a unit of about three people** (official framework pages are mostly behind a login, so I used practitioner and archived pages)

**1. Best-fit practices**
- **Funnel to Done states with an exit decision at each transition** (Portfolio, decision-making). The Funnel has no WIP limit. Reviewing is a quick screen: is this worth analysis time? Analyzing produces a Lean Business Case, and approval is a go/no-go. The Portfolio Backlog is sequenced. Implementing runs the MVP and stops at Done, when governance is no longer needed. Your seven states already match this. Keep them, but give each a one-line entry/exit rule and a WIP limit.
- **Epic Hypothesis plus MVP plus persevere/pivot/stop** (Portfolio). The MVP is the minimum scope that tests the benefit hypothesis. One named Epic Owner decides to persevere, pivot or stop, using leading-indicator data. This maps onto your "Decision after the MVP" with no new forum.
- **Epic approval threshold** (controls). Leadership sets a threshold on cost, number of PIs and strategic importance. Below it, the Program Kanban approves. Above it, the epic needs a Lean Business Case and Portfolio Kanban approval. This supports your run-rate versus Initiative split. Use one number, such as person-weeks.
- **Lean budget guardrails** (controls). SAFe names four: investment horizons, capacity allocation, the approval threshold, and continuous business-owner engagement. Fund the unit as a standing capacity split (for example run-rate, Initiatives, enablers) and don't fund project by project.
- **WSJF** (Portfolio and Program). It is cost of delay divided by job size. Cost of delay has three parts: user-business value, time criticality, and risk reduction or opportunity enablement. Scores are relative, on a Fibonacci scale. It works as a pre-agreed sequencing rule, so no meeting is needed to debate order.
- **Decentralise by criteria** (decision-making). Centralise decisions that are infrequent, long-lasting and carry large economies of scale. Decentralise those that are frequent, time-critical or need local context.
- **Compliance built into the flow** (controls). Compliance stories sit in the Definition of Done, are automated where possible, and produce objective verification evidence as a by-product.
- **Inspect and Adapt** (Program). Hold it at the end of each quarterly increment: demo, metrics review, then a problem-solving workshop. Keep it as one session.

**2. Decision rights and forums**
- Rule-based, no meeting: WSJF order, WIP limits, the epic threshold, and capacity split.
- Epic Owner alone: Reviewing to Analyzing, and pulling a Feature below the threshold.
- Sponsor or Domain Owner, quarterly: approve a Lean Business Case above the threshold, and set the investment envelopes.
- Persevere/pivot/stop at the MVP: Epic Owner presents the evidence and the Sponsor confirms (this is practitioner wording, not official).
- Two cadences are enough: a monthly operational sync and a quarterly strategic review. One practitioner page suggests monthly Portfolio Sync for fewer than five active epics. Its agenda is status by exception only, and each item ends in approve, escalate or note. A decision log is kept.
- Escalate only on a guardrail breach or a cross-function conflict.

**3. Artefacts**
- **Keep:**
  - Portfolio: a one-page Lean Business Case, only above the threshold. It covers cost, ongoing cost, benefits, time-to-market, risk, and the MVP definition.
  - Program: the Feature list with WSJF scores.
  - Team: stories with compliance DoD evidence.
  - All levels: a decision log.
- **Drop:**
  - A Lean Business Case for run-rate work.
  - Epic Hypothesis statements for run-rate work.
  - Separate Portfolio Kanban and Program Kanban status reports. One board with a Jira projection is enough.

**4. Avoid or discard for our size**
- Large-organisation parts: multiple value streams and Participatory Budgeting among value streams, the Value Management Office, a LACE team, Solution Trains, and the RTE role. One source says the portfolio layer starts only after several ARTs run.
- The two-day PI Planning for 50-125 people, and ROAM boards. Replace them with a one-hour quarterly planning session.
- ART Sync, as a separate meeting from the monthly sync.
- Three steering forums. Two cadences cover the same ground.
- A SAFe-trained-roles structure. One source says SAFe isn't needed "if you have 1-2 independent teams".

**5. Regulated bank**
- Compliance in the flow still needs manual steps. SAFe says some activities, such as audits and FMEA, can't be automated.
- Keep model-risk, information-security and data-class clearances as explicit exit criteria on the Kanban states, not as extra forums.
- Evidence should be a by-product of work, readable by auditors.
- The threshold and guardrails should be written down and approved once, then applied by rule.
- Keep stop decisions central. High risk and costly reversal favour central decisions.

**6. Sources**
- [Atlassian (Russian), "Что такое Scaled Agile Framework (SAFe)"](https://www.atlassian.com/ru/agile/agile-at-scale/what-is-safe), publisher Atlassian, year not captured. It came up only in search results; I did not fetch it or rely on it for any claim above.
- [Portfolio Kanban states and decision gates](https://agility-at-scale.com/safe/lpm/portfolio-kanban/), agility-at-scale.com, 2025 (unverified date). Practitioner summary. The WIP numbers (3-5, 15-20) are its own figures.
- [Portfolio Sync cadence and agenda](https://agility-at-scale.com/safe/lpm/portfolio-sync/), agility-at-scale.com, 2025 (unverified date).
- [Lean Budget Guardrails](https://agility-at-scale.com/safe/lpm/portfolio-guardrails/), agility-at-scale.com, 2025 (unverified date). The fourth guardrail is named differently on the practitioner page versus a search result: "continuous compliance" versus "continuous business-owner engagement". I used the latter, which matches my memory of SAFe 5/6 (unverified).
- [Epics, Lean Business Case, MVP, persevere/pivot/stop](https://agility-at-scale.com/safe/lpm/epics/), agility-at-scale.com, 2025 (unverified date). The "decided at PI boundaries" detail comes from this page only.
- [Epic approval threshold, via search snippet of SAFe 4.6 epic page](https://v46.scaledagileframework.com/epic), Scaled Agile Inc., 2018. The page itself failed to load (SSL error), so the threshold wording comes from the search summary only.
- [Decentralize decision-making, SAFe principle 9](https://scaledagileframework.com/decentralize-decision-making), Scaled Agile Inc. The centralise/decentralise criteria come from search summaries, not a full read. The official site is mostly gated.
- [Decision-making criteria (Highsmith's dials)](https://agility-at-scale.com/?p=150818), agility-at-scale.com, 2025 (unverified date).
- [Compliance, search summary](https://framework.scaledagile.com/compliance), Scaled Agile Inc.; the PDF "Achieving Regulatory and Industry Standards Compliance with SAFe 4.5" (2018) would not render.
- [Overhead and small-team limits (Russian)](https://habr.com/ru/articles/994492), Habr, 2025 (unverified date).
- [Inspect and Adapt](https://framework.scaledagile.com/inspect-and-adapt/), Scaled Agile Inc. Search-summary only.

Gaps:
- The official portfolio-kanban, budgets and decentralised-decision pages are login-gated, so I could not read them directly.
- The SALSA PDF "Dynamics of Decision Making within the Portfolio Kanban" would not extract. It is at https://salsa.scaledagile.com/wp-content/uploads/Dynamics-of-Decision-Making-within-the-Portfolio-Kanban.pdf, and I did not read it.
- Program/ART Kanban state names, the PI Planning agenda, and the WSJF scale details are partly from my memory (unverified).
