# Statement of intent: basis for the strategic priorities and the maturity roadmap

Where the priorities and the maturity roadmap in the [statement of intent](../../../charter/documents/statement-of-intent.md) come from. The charter carries no references. Gathered 2026-09-30, on top of the earlier [industry research](industry-research.md) and the [function pages](functions/README.md).

## Priorities

| Priority | Basis | Evidence status |
| --- | --- | --- |
| 1 Customer intelligence | A unified customer view is described as the operational foundation AI needs. Risk and fraud signals run through the whole customer lifecycle, not only at login or onboarding. Onboarding friction is a named problem, and agentic KYC is offered as the fix ([Backbase](https://www.backbase.com/blog/ai-banking-trends-2026), [Aspire Systems](https://www.aspiresys.com/blog/banking-financial-services/artificial-intelligence-in-banking/ai-in-banking-2026-scaling-agentic-workflows-for-core-modernization/), [Alkami](https://www.alkami.com/blog/the-top-5-financial-data-technology-trends-and-predictions-for-2026/)). Santander UK's head of data and AI describes credit, fraud, and compliance handoffs as friction that an agentic flow could remove, and calls it early-stage. KYC and financial-crime detail is in the [compliance and KYC page](functions/compliance-and-kyc.md) | Mostly vendor sources. Performance figures are marketing claims and were not used |
| 2 Business intelligence | Reporting, analysis, forecasting, benchmarking, and investor and Board intelligence use cases, with maturity ratings, are in the [IR and FP&A page](functions/ir-and-fpa.md). The independent evidence there is a 2025 finance-leader survey and regulator material. No named bank with published results for IR or bank FP&A was found | Thin for banks. Described honestly as emerging |
| 3 Adoption within business functions | Bank-wide assistants and function-level automation: [industry research](industry-research.md) (JPMorgan's internal assistant, ING's due-diligence reports) and the [HR and accounting](functions/hr-and-accounting.md) and [service and operations](functions/service-operations-front-office.md) pages | Self-reported by banks |
| 4 Expertise at the point of work | Morgan Stanley's advisor assistant over about 100,000 documents and its evaluation approach, and a Federal Reserve experiment on faster information gathering ([industry research](industry-research.md)). It is framed by what governed knowledge enables, not as a repository | Company-reported |
| 5 AI in banking operations and systems | Generative AI works best as a copilot inside workflows, with final approval and accountability with qualified staff. The most effective deployments sit inside origination platforms, core banking, and CRM tools. McKinsey describes a credit-manager copilot that orchestrates the credit workflow with humans defining procedures. Many bank AI tools do not initiate payment instructions or fund transfers. The FCA's assurance framework covers human-in-the-loop controls ([McKinsey](https://www.mckinsey.com/industries/financial-services/our-insights/extracting-value-from-ai-in-banking-rewiring-the-enterprise), [Automation Anywhere](https://www.automationanywhere.com/company/blog/automation-ai/ai-banking-how-banks-use-ai-improve-risk-and-operations), [Master of Code](https://masterofcode.com/blog/generative-ai-in-banking)) | Design pattern is consistent. Named-bank evidence for payment exceptions and reconciliation is thin. Vendor sources |
| 6 IT operations and service lifecycle | Common AIOps use cases: root cause analysis, predictive monitoring, incident management, and service desk copilots. Legacy integration is a stated obstacle ([Dynatrace](https://www.dynatrace.com/platform/aiops/), [tBlocks](https://tblocks.com/articles/aiops-use-cases-examples/), [HEAL Software](https://healsoftware.ai/blog/aiops-use-cases-for-it-operations.html)). Banking systems and security detail is in the [IT and banking systems page](functions/it-and-banking-systems.md) | No named bank case found. Cited outcomes come from vendors or from a telecom. Treated as emerging |
| 7 Software engineering | Bank-reported productivity gains and agents in the [industry research](industry-research.md) and the [IT and banking systems page](functions/it-and-banking-systems.md) | Self-reported |

Order: customer and business intelligence first, as decided. Then the functions and knowledge that support daily work, then embedding in banking flows, then technology operations and engineering.

## Maturity roadmap

| Element | Basis |
| --- | --- |
| Five levels | Gartner's five stages (foundational, emerging, operational, scaled, transformational), Microsoft's five levels for agentic adoption (initial, repeatable, defined, capable, efficient), and other five-stage models ([Gartner](https://www.gartner.com/en/chief-information-officer/research/ai-maturity-model-toolkit), [Microsoft Learn](https://learn.microsoft.com/en-us/agents/adoption-maturity-model/), [WitnessAI](https://witness.ai/blog/ai-maturity-model/), [Digital Applied](https://www.digitalapplied.com/blog/agentic-ai-maturity-model-enterprise-self-assessment-guide)). Level names are our own |
| Banking mapping | A mapping of the Gartner stages to banking value, organization, and governance ([Chris Shayan](https://www.chrisshayan.com/blog-posts/the-ai-maturity-model-for-banking)) |
| Measure by deployment type | nCino argues for measuring maturity by type of AI deployment rather than one blended rate ([nCino](https://www.ncino.com/blog/ai-in-banking-today-three-deployments)). The roadmap therefore measures per level and per priority |
| Governance maturity | Databricks suggests reaching level 3 in governance within about 12 months and level 4 within 24, reviewed quarterly ([Databricks](https://www.databricks.com/blog/ai-governance-maturity-model)). Not adopted as targets. Timing belongs in the portfolio roadmap |
| Platform capability per level | Our own design, using the platform layers in the earlier statement (model gateway, knowledge layer, tool gateway, registry, guardrails, oversight, observability) |
| Measures per level | Our own drafting from the priorities and the trust principles. No targets, which the metrics document sets |

## Confidence and gaps

- Most sources are vendor writing. Where they gave figures, the figures were left out.
- No named bank case was found for AIOps, payment exceptions, or reconciliation. The priorities on operations and IT operations rest on design patterns and vendor material.
- The maturity models are general. Only one banking-specific mapping was found, and it is a practitioner's blog.
- The priority order, level names, and per-level measures are our own judgement.
