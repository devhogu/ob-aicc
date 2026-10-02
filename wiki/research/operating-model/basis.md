# AICC operating model: basis

> This page describes the lineage of the first corpus, now archived. See [Simplification](simplification.md) for what replaced it.

Where the elements of [charter/documents/operating-model.md](../../../charter/documents/operating-model.md) come from. The charter documents carry no references. This page keeps the lineage. Gathered 2026-09-29 from web search.

## What comes from where

| Element | Basis |
| --- | --- |
| Program office that supports rather than controls | PMI describes a supportive PMO that provides guidance, templates, and coaching without heavy oversight. |
| Enablement group as agile center of excellence | Agile centers of excellence and value delivery offices focus on agility, coaching, and continuous learning rather than control (PMBOK 7 commentary). |
| Portfolio and Value Delivery Office | SAFe's Value Management Office facilitates Lean Portfolio Management and lean governance. "Value Delivery Office" is not a Disciplined Agile term. Disciplined Agile covers the work through its portfolio management, governance, and transformation areas. Combining agile program office, value delivery, and portfolio management in one office is our own synthesis. |
| Small dedicated hub | SAFe describes a Lean-Agile Center of Excellence as a dedicated team of 3 to 5 people that itself works in an agile way. |
| Hub and domain network | AI centers of excellence commonly use hub-and-spoke: the hub sets standards, governance, and shared infrastructure, and the spokes carry use cases and results. |
| Continuous flow, limits on work in progress, explicit stage policies, cadences | The operating model is flow-based under the hood, following the Kanban Method: visualize work, limit work in progress, manage flow, make policies explicit, use feedback loops (replenishment, delivery review, service delivery review, operations and risk review), improve collaboratively. Disciplined Agile's lean lifecycle is the same idea: pull new work when capacity allows, no fixed iterations, ceremonies only as needed. Portfolio-level flow follows the portfolio Kanban idea in SAFe, where limits on work in progress align demand with capacity. The charter documents deliberately use neutral wording and do not name the method. The wider mapping to scaled agile constructs is in [agile mapping](agile-mapping.md). |
| Lead Architect, Delivery Lead, and engineer roles held by the AICC Lead | Our own drafting from the described way of working. The Delivery Lead role corresponds to the scrum master or release train engineer role in scaled agile terms and is deliberately named neutrally. |
| Values integrity, prudence, and respect for people; the principles of application (trust) in the statement of intent | Aligned to what banks, fintechs, standards bodies, and regulators publish. The mapping, counts, and sources are in [responsible AI alignment](responsible-ai/README.md). The principle wording is our own. |
| Risk-based gates, evidence from platform logs | Disciplined Agile's lean governance: visibility over reporting, automation, risk-based milestones. |
| Charter contents | AI center-of-excellence sources list mission, scope, decision rights, governance responsibilities, intake, approved tools, risk review, training, metrics, and executive sponsorship. They advise writing the charter first. |
| Domain experts as early adopters and AI solution engineers under functional direction | Our own drafting from the way of working described for the bank. Functional (dotted-line) direction is a common matrix arrangement in banks. Not taken from the sources below. |
| Bank and fintech group scope, entity boundaries, product-line domains | Our own drafting from the stated context of a bank within a group of fintech and digital businesses. Regulatory regimes differ by entity, so control roles are held per entity. See [agile mapping](agile-mapping.md). Nothing about specific entities was verified. |
| Control function contacts outside AICC | Our own drafting. It follows the independence expected of model risk validation, compliance, and audit. |
| First-line placement with independent validation | Our own addition. It follows the three-lines model used in banks and the independence expected of model risk validation. It is not taken from the sources below. |
| Names kept out of foundational documents | Our own drafting rule, to keep the defining documents stable. |

## Design alternatives

The three usual operating models for an AI center of excellence:

```
Centralized              Hub-and-spoke                 Federated
(hub does the work)      (hub sets rules, spokes do)   (domains run themselves, thin center)

      HUB                       HUB                        thin CENTER
   builds and runs         standards, platform,          policy, risk, shared tools
   everything              governance, coaching                 |
        |                       |                 |-----------|-----------|
   requests from          |-----|-----|           DOMAIN     DOMAIN     DOMAIN
   the business         SPOKE SPOKE SPOKE         own teams,  own teams,  own teams,
                        (domain specialists       own backlog own backlog own backlog
                         deliver in domain)
```

- **Centralized:** strong control and cost efficiency, but a bottleneck. Common at low maturity.
- **Hub-and-spoke:** the hub sets standards, governance, and shared infrastructure. Domain specialists deliver and are accountable for results. Most large enterprises settle here.
- **Federated:** governance of data privacy, model quality, compliance, and risk stays central, but execution and prioritization sit in the domains, each with its own teams and backlog. It gives domains the most freedom, and risks inconsistent tools and standards unless the central policy layer is strong. One banking-focused source recommends this variant for banks because it combines domain flexibility with central control.

| | Hub-and-spoke | Federated |
| --- | --- | --- |
| Who prioritizes | Hub, with domains | Each domain |
| Shared platform | Hub-led standard | Central policy, domains choose within it |
| Hub size | Small to medium | Smallest |
| Fits when | Domains are still building capability | Domains already have their own AI teams |

## Sources

- [PMBOK 7 commentary on the PMO](https://projectmanagementcompass.substack.com/p/inside-pmbok-7-rethinking-the-pmo)
- [PMI Agile Practice Guide](https://www.pmi.org/standards/agile) (table of contents only)
- [SAFe Value Management Office](https://framework.scaledagile.com/value-management-office)
- [SAFe Lean-Agile Center of Excellence](https://framework.scaledagile.com/lace)
- [Disciplined Agile governance](https://www.pmi.org/disciplined-agile/process/governance)
- [Disciplined Agile value streams](https://www.pmi.org/disciplined-agile/process/value-streams)
- [The Official Guide to the Kanban Method](https://kanban.university/kanban-guide/)
- [The Kanban Method glossary](https://kanban.university/glossary/)
- [Kanban cadences](https://teachingagile.com/kanban/introduction/kanban-cadences)
- [Disciplined Agile lean (Kanban-based) lifecycle](https://www.pmi.org/disciplined-agile/lifecycle/lean-lifecycle)
- [SAFe portfolio Kanban](https://agility-at-scale.com/safe/lpm/portfolio-kanban/)
- [Tredence: AI center of excellence](https://www.tredence.com/blog/ai-center-of-excellence)
- [Atlan: AI center of excellence charter, roles, playbook](https://atlan.com/know/ai-agent/ai-agent-governance/how-to-build-ai-center-of-excellence/)
- [Agility at Scale: AI center of excellence](https://agility-at-scale.com/ai/people-change/ai-center-of-excellence/)

## Confidence and gaps

- The PMI primary texts (PMBOK 7, Agile Practice Guide) were not read. The PMO and value delivery office points come from commentary and PMI web pages.
- Most AI center-of-excellence sources are vendor or consultancy writing.
- A vendor summary cites IBM research that centralized or hub-and-spoke models return more than decentralized ones. It was not checked against the original, so it is not relied on.
- No regulator guidance on the operating model of an AI unit in a bank was searched.
