# AICC operating model: agile at scale, in business wrapping

> This page describes the lineage of the first corpus, now archived. See [Simplification](simplification.md) for what replaced it.

Where the operating model borrows from scaled agile practice, and how each construct is renamed in business terms. The charter documents use the business wording only and do not name the framework. This page keeps the lineage. Gathered 2026-09-29 from web search plus general knowledge of the framework. SAFe is a licensed framework, so the operating model reuses its principles, values, and constructs and does not copy it.

## Lens

SAFe organizes the enterprise in layers: portfolio (Lean Portfolio Management), large solution, program (Agile Release Train), and team, with technical agility (DevOps and continuous delivery) beneath. AICC applies the same layers to the adoption of AI, with business names.

## Mapping

| Scaled agile construct | AICC business wrapping | Where it lives in the charter |
| --- | --- | --- |
| Core values: alignment, transparency, respect for people, relentless improvement | Same four values | Operating model, principles |
| Lean-Agile principles (economic view, systems thinking, variability, incremental build, objective milestones, WIP and flow, cadence, decentralized decisions, motivation) | Seven Principles of Delivery | Operating model, principles |
| Lean Portfolio Management: strategy and investment funding, agile portfolio operations, lean governance | Portfolio management in three parts: strategy and investment, portfolio operations, lean governance | Operating model, portfolio management |
| Strategic themes | Strategic priorities, taken from the statement of intent (workday adoption, knowledge bases, routine-operations automation, software development, agentic platform) | Operating model |
| Lean budgeting, value stream funding, guardrails, participatory budgeting | Investment envelope per priority, funding of team capacity rather than projects, guardrails for thresholds and mix, quarterly re-allocation with the domain owners | Operating model; funding model (stub) |
| Epic with lean business case and minimum viable product | Initiative with an initiative brief (hypothesis, minimum viable scope, benefits, cost, risks) | Operating model, work structure |
| Capability, feature | Use case: a deliverable for one domain with a measurable benefit | Operating model, work structure |
| Story, task | Work item on the team board, managed by the delivery team and not defined in the charter | Operating model, work structure |
| Enablers (architecture, infrastructure, exploration, compliance) | Enabling work: platform, architecture, governance and policy, exploration | Operating model, work structure |
| Portfolio Kanban: funnel, reviewing, analyzing, backlog, implementing, done | Portfolio flow stages: intake (with triage), discovery (ending in a ranked ready queue), pilot, scale, operate, retire, with explicit entry and exit policies by risk tier | Operating model, portfolio flow |
| Weighted shortest job first (cost of delay over job size) | Ranking by value and urgency relative to effort, combined with evidence, capacity, dependencies, and the option to stop | Operating model, ranking |
| Explicit policies, limits on work in progress, pull | Same, stated as policies and limits on work in progress | Operating model, processes |
| Value Management Office / Agile Portfolio Management Office | Portfolio and Value Delivery Office | Operating model, hub |
| Lean-Agile Center of Excellence | Enablement group | Operating model, hub |
| Agile Release Train, program | Delivery program: all delivery teams on one cadence | Operating model, delivery program |
| Agile team with Product Owner, Scrum Master, developers | Delivery team: domain expert and AI solution engineer around use cases. The domain owner is the product owner | Operating model, roles |
| Release Train Engineer | Delivery Lead | Roles |
| System Architect | Lead Architect | Roles |
| Product Management | Portfolio Manager, together with the domain owners | Roles |
| Business Owners | Domain owners, who also score value achieved | Roles |
| Shared services and specialists | Control function contacts and the platform owner | Operating model, roles |
| PI planning | Quarterly planning and review event with objectives and commitment. The shared dependency board is deferred | Operating model, delivery program; evolution plan (stub) |
| System demo | Delivery review every two weeks with working solutions | Operating model, delivery program |
| Inspect and adapt | The review half of the quarterly event, including value scoring and improvements | Operating model, delivery program |
| Communities of practice | Communities of practice | Operating model, delivery program |
| DevOps and the continuous delivery pipeline | Continuous delivery of AI solutions by the same team that operates them: build, evaluate, release on demand, monitor, handle incidents and drift | Operating model, processes; stage "operate" |
| Flow, predictability, and DevOps measures | Value, flow, quality, predictability, and adoption measures | Metrics (stub) |
| Solution train (multiple release trains) | Not needed yet. Considered in the evolution plan when several delivery programs exist | Evolution plan (stub) |

## Design choices that differ from the reference framework

- **Flow-based teams on a shared cadence.** Teams pull work continuously with limits on work in progress instead of fixed iterations. SAFe allows flow-based teams inside a program on the common cadence.
- **Small scale.** One delivery program, not several trains. A solution train is deferred.
- **Domain owner as product owner and business owner.** SAFe separates these roles. At AICC's size they coincide, and the domain expert supplies the day-to-day domain knowledge.
- **Independent control.** Control function contacts and their validation sit outside the delivery flow's authority. This is a banking requirement and goes beyond the reference framework's "lean governance".
- **Domain as function or product line.** SAFe recommends organizing around value streams that cross functions. A stream that also crosses entities, such as KYC, lending, or payments, may need several domain owners acting together. This is an open item.

## Simplification applied (2026-09-30)

The first version had ten principles, four work levels, eight stages, seven cadences, fifteen roles, and 51 RACI rows. It was thinned without removing any layer.

| Layer | Before | After | Reason |
| --- | --- | --- | --- |
| Principles | 10 | 7 | Merged related principles. Added one for product speed within bank-grade control and legal-entity boundaries |
| Work levels | 4 | 4 | The Work Item remains a level and is managed by the Delivery Team on its own board (Operating Model 7.2) |
| Portfolio flow | 8 stages | 6 | Triage folded into intake, ready folded into discovery |
| Cadences | 7 | stated in Operating Model 14 | Planning, portfolio review, improvement workshop, and risk review merged into one quarterly event. Monthly service review dropped |
| Roles | 15 | 13 | Value Manager folded into the Portfolio Manager. Line Manager is part of the engineer arrangements, not a role |
| RACI rows | 51 | 43 | One decision per stage gate instead of one per activity |
| Deferred to the evolution plan | | Initiative briefs and guardrail thresholds until set, the dependency board, value-stream alignment, a second delivery program, a solution train, separating combined roles | Activate when scale requires |

Kept as they are: independence of the control functions and the separation rules, exactly one accountable role per row, the split between roles, positions, and named people, and the domain owner as product owner.

## Bank and fintech group flavor

Added because the organization is a bank and a group of fintech and digital businesses, not a bank alone. The wording is our own drafting from that context. Nothing about specific group entities is stated in the charter.

- Scope reaches the bank and the group's fintech and digital entities.
- A domain is a business function or a product line, so a fintech product has a domain owner who is its product owner.
- Each legal entity keeps its own regulator, accountability, control functions, and data. Control function contacts are named per entity and regulatory regime. Data is shared between entities only under a group arrangement.
- Product speed with bank-grade control: pilots can be controlled experiments with defined success measures, and release speed follows the risk tier, so low-risk changes move fast.
- The shared platform serves several entities, which the data classification and risk tier policies must respect.

## Sources

- [Lean portfolio management, strategic themes, lean budgeting, guardrails, participatory budgeting](https://www.ppm.express/blog/safe-lean-portfolio-management)
- [Lean budget guardrails](https://agility-at-scale.com/safe/lpm/portfolio-guardrails/)
- [Portfolio Kanban](https://agility-at-scale.com/safe/lpm/portfolio-kanban/)
- [Lean portfolio management](https://framework.scaledagile.com/lean-portfolio-management-discipline)
- [Value Management Office](https://framework.scaledagile.com/value-management-office)
- [Lean-Agile Center of Excellence](https://framework.scaledagile.com/lace)
- [Agile release train: structure, events, roles](https://agility-at-scale.com/safe/team-technical-agility/agile-release-train/)
- [Implementing essential SAFe](https://agility-at-scale.com/safe/essential/)
- [The Official Guide to the Kanban Method](https://kanban.university/kanban-guide/)
- [Disciplined Agile lean lifecycle](https://www.pmi.org/disciplined-agile/lifecycle/lean-lifecycle)

## Confidence and gaps

- The framework's official pages were not read directly. The mapping rests on secondary summaries and on general knowledge of the framework. The core values and principles listed here are from memory and should be checked against the official framework before anyone quotes them.
- The wording of every AICC construct is our own.
- No source was found on applying these constructs to the adoption of AI in a bank.
