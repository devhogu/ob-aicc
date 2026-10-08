# Research report: Other agile portfolio methods

Collected on 2026-10-08 by an independent research agent for the flow redesign (change C-FLOW-REDESIGN), from the brief in this folder. Source quality is stated in each report: claims marked unverified come from memory, and several official pages (SAFe, PMI, ITIL) were gated or paywalled, so summaries and practitioner pages were used.

**Recommendation in one line:** at three people, treat the four levels as four views of one Kanban board with a few written policies. Do not run them as four forums with approval gates.

**1. Best-fit practices**
1. **Kanban explicit policies and pull criteria (Portfolio, Program, controls).** Write one short policy per board column: pull criteria, WIP limit, exit criterion, who may move a card. A policy replaces a meeting. It suits a small unit because the board then holds the process.
2. **Classes of service (Portfolio, Program).** Use three classes at most, for example Run-rate, Initiative and Urgent or Regulatory. Each class has its own pull rule and service-level expectation. This covers your two modes of work without extra gates.
3. **Disciplined Agile "value first, cost second" and lightweight milestones (Portfolio, decision-making).** Keep the milestones few and risk-based, for example stakeholder-vision agreed, proven architecture and proven outcome. Each is tied to a go, pivot or stop call. This fits the MVP decision you already have.
4. **Lean Startup innovation accounting and pivot/persevere (Discover, Portfolio).** Before the MVP, write down the one measurable hypothesis and the continue, pivot or stop threshold. After the MVP, the evidence decides. The decision is quick because the threshold was set in advance.
5. **Beyond Budgeting (Portfolio, controls).** Separate three things: targets, forecasts and resource allocation. Fund capacity (people-weeks per quarter) per strategic priority, and review forecasts when events happen. Do not set a per-project budget.
6. **Product operating model (Cagan, Perri) (Portfolio, Program).** Fund the team against outcomes and let the team choose the work. Set a small number of outcome "bets" with a measure. Treat a long list of initiatives with fixed scope as a warning sign, since it is the project-funding pattern that SVPG criticises.
7. **Scrum@Scale MetaScrum (decision-making).** One forum where leaders and stakeholders set priorities, change budgets and realign people, with one prioritised backlog. This lets one monthly slot replace your three Steering forums.
8. **OKRs (Portfolio, Program).** Use quarterly objectives and key results, graded simply and kept separate from pay. They give alignment without a separate planning process.

**2. Decision rights and forums**
- **Team (daily):** the team decides the order of Stories and tasks inside the Iteration. No meeting beyond the daily sync.
- **Program (monthly):** the AICC lead, acting as chief product owner, orders Features and Capabilities. WSJF is a tiebreak for the lead, not a ritual.
- **Portfolio (one monthly MetaScrum-style slot, plus a quarterly OKR reset):** the Domain Owner or Executive Sponsor decides Approval, MVP continue/pivot/defer/reject, and envelope shifts. The evidence is the one-page brief, the pre-agreed threshold and the measured result.
- **Decided by rule, not meeting:**
  - Pull happens when WIP is free and the pull criteria are met.
  - Run-rate requests start within the Iteration if they fit the class policy and the standing Initiative.
  - Stop is automatic if the pre-agreed threshold is missed or an item ages beyond its service-level limit. The sponsor can overrule, and the overrule is logged.
  - Urgent items are limited to one at a time.
- **Yearly:** fold it into the Q4 quarterly session.

**3. Artefacts**
- **Keep:**
  - The scenario catalog and the Funnel (Discover).
  - A one-page Initiative Brief with the hypothesis, threshold, owner and risk tier (Portfolio).
  - A decision log with date, decider, evidence and result.
  - The OKRs.
  - The policy sheet (the explicit board policies).
  - The Jira Features and Stories.
  - An MVP result note.
- **Drop:**
  - The six-section brief for run-rate work, and separate Approval for small Features.
  - Duplicate status reports. The Jira board and the site projection are the status.
  - Any per-Initiative budget document, and PI planning documents beyond the quarterly OKRs.

**4. Avoid or discard for your size**
- Large-scale framework roles: LeSS Huge area product owners, Nexus integration teams, and Scrum@Scale scrum-of-scrums. These coordinate many teams, and you have one.
- Spotify squads, tribes and guilds. Kniberg says it is not a framework and was a snapshot. Take only its autonomy-with-alignment idea.
- Three Steering forums.
- WSJF scoring of every item. Use it only when two Initiatives genuinely compete.
- Enterprise Services Planning and Portfolio Kanban at full depth. One board with classes of service is enough.
- Annual budgets that are fixed per Initiative.

**5. Regulated bank**
- Keep the gates that the regulator or internal control requires: model-risk and information-security clearance, data-class approval, independent testing, audit read access. Make them explicit pull criteria on the board rather than extra forums.
- The decision log and the policy sheet are the audit trail, so keep them dated and attributable.
- An Urgent or Regulatory class of service needs a named approver.
- Segregation of duties: the person who proposes an Initiative should not be the sole approver or the independent tester. With three people, assign the independent role to someone outside the unit.
- Keep fund-by-outcome language compatible with the bank's budget cycle. Show the annual envelope to Finance, and manage capacity internally.

**6. Sources** (all fetched or searched in this session unless marked)
- Scrum@Scale Guide, Scrum Inc., current: https://www.scrumatscale.com/scrum-at-scale-guide-online/ (MetaScrum, chief product owner; fetched, no login).
- SVPG, "Project-based funding", Marty Cagan: https://www.svpg.com/project-based-funding/ (fund product teams, not projects; fetched).
- Agile Alliance beyond-budgeting article, undated: https://www.agilealliance.org/?p=8005143 (rolling forecasts, separating target, forecast and allocation; fetched).
- WhatMatters.com OKR FAQ, undated: https://www.whatmatters.com/faqs/okr-meaning-definition-example (quarterly cadence, grading, separate from pay; fetched).
- Planview blog, "Make process policies explicit": https://blog.planview.com/make-process-policies-explicit/ (a vendor page, so weaker evidence).
- PMI Disciplined Agile portfolio mindset: https://www.pmi.org/disciplined-agile/process/portfolio-management/portfolio-management-mindset (returned 403 on fetch; the "value first, cost second" wording comes from a search summary only). The lightweight-milestones blog at projectmanagement.com also returned 403.
- LeSS overview: https://less.works/less/management/index. The page said little on portfolio or funding, so I made no LeSS claims from it.
- Lean Startup, Ries (2011), and Highsmith, *Agile Project Management* (2009): search summaries only, no primary page read.
- Unverified (from memory, no source read):
  - Kanban classes of service as named by Anderson, and Portfolio Kanban, with Enterprise Services Planning.
  - Teresa Torres's continuous discovery and Perri's *Escaping the Build Trap* (2018) detail.
  - Kniberg's Spotify paper (2012) and his "snapshot of a moving target" remark. This is from search snippets only.
  - Highsmith's governance specifics.
  - The idea of a standing "overrule is logged" rule. This is my own suggestion, not from a source.
