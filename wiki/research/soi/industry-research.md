# Industry Research Notes

Basis for the [statement of intent](../../statement-of-intent.md). Gathered 2026-09-29 from web search. Many figures are **self-reported by banks or from vendor blogs**. Verify against primary sources before external use.

## Direction of the industry

- BCG and OpenAI (March 2026) project AI could lift retail-bank profitability by 30% and cut costs by 30–40% by 2030. Front-office agents take routine tasks. Back-office agents extract data from documents, analyse cases, escalate exceptions, and keep audit trails. [BCG](https://www.bcg.com/publications/2026/how-retail-banks-can-put-agentic-ai-to-work)
- McKinsey describes agentic systems that plan, use tools, and collaborate with people and other agents. It warns much of the value is still hypothetical and calls for rewiring the enterprise, not adding pilots. [McKinsey](https://www.mckinsey.com/industries/financial-services/our-insights/extracting-value-from-ai-in-banking-rewiring-the-enterprise)
- Deloitte advises banks to keep an agent registry with owners, scope, datasets, and risk limits. [Deloitte](https://www.deloitte.com/us/en/insights/industry/financial-services/agentic-ai-banking.html)

## Workdesk and knowledge bases

- Morgan Stanley: GPT-4 assistant over about 100,000 documents, over 98% adoption in advisor teams (company-reported). The hard parts were authorised sources, traceable answers, and evaluation as models and documents change. [ZenML](https://www.zenml.io/llmops-database/enterprise-knowledge-management-with-llms-morgan-stanley-s-gpt-4-implementation), [Conscious Engines](https://consciousengines.com/blog/morgan-stanley-eval-driven-rag-case-study)
- JPMorgan: internal LLM Suite reported at 230,000+ employees and 500+ use cases in production (roundup source, unverified). [Roundup](https://financeaicareers.com/ai-in-investment-banking)
- Federal Reserve Board experiment: information gathering fell from 5–6 minutes to 30–40 seconds per query. Quality improved only for simple questions. [UXDA](https://www.theuxda.com/blog/ai-gold-rush-21-digital-banking-ai-case-studies-cx-transformation)

## Operations automation

- ING: GenAI customer-due-diligence reports save about two hours per client, used in all 19 countries. Best-documented result found. [KickstartAI](https://kickstart.ai/news/ing-innovating-wholesale-banking-ai)
- KYC and AML remain heavy cost centres, and auditability is the critical requirement (vendor sources). [Encompass](https://www.encompasscorporation.com/blog/transforming-kyc-onboarding-with-genai-a-new-era-in-banking/)

## Software development

Self-reported, not comparable:

| Bank | Reported result |
|---|---|
| JPMorgan | 10–20% engineer productivity gain |
| Goldman Sachs | About 20% for 12,000 developers. Autonomous coding agents piloted from July 2025 |
| Bank of America | 20% lift in focused parts of the lifecycle, 18,000 developers |
| Citi | 9% productivity gain. One million AI code reviews in 2025 |
| Wells Fargo | Up to 35% |
| Morgan Stanley | Legacy-code-to-spec tool: 9M lines, about 280,000 hours saved |

Source: [roundup](https://www.artificialintelligence-news.com/news/wall-street-ai-gains-are-here-banks-plan-for-fewer-people/), [Deloitte](https://deloitte.com/us/en/insights/industry/financial-services/financial-services-industry-predictions/2025/ai-and-bank-software-development.html), [Yahoo Finance](https://finance.yahoo.com/news/jpmorgan-engineers-efficiency-jumps-much-190410471.html)

## Agentic platform pattern

Common reference architecture across sources: agent registry, MCP-style tool gateway, guardrails and policy enforcement, human-in-the-loop, observability and evaluation. Existing access control covers human identities, not autonomous agents acting for them. Approval channels should be separate from the agent's own execution. Mostly vendor and academic sources. [Databricks](https://answers.databricks.com/best-platforms-ai-agents-banking), [Financial Brand](https://thefinancialbrand.com/news/banking-technology/why-banks-need-mcp-guardrails-before-access-control-slips-197265), [Context Kubernetes](https://arxiv.org/pdf/2604.11623)

## Governance and regulation

- US: April 2026 model-risk guidance (SR 26-2) excludes generative and agentic AI from formal scope. Supervisors examine them through third-party, resilience, cyber, and consumer-protection frameworks. Secondary source. [Grant Thornton](https://www.grantthornton.ie/insights/factsheets/ai-banking-risk-regulation-governance/)
- Other anchors: BIS on explainability ([FSI Papers 24](https://www.bis.org/fsi/fsipapers24.pdf)), FSB 2024 AI report, PRA SS1/23, FINMA Guidance 08/2024, EBA internal-governance guidelines, NIST AI 600-1 for GenAI risks. A claimed set of FSB sound practices from June 2026 is unconfirmed.
- Practitioner consensus: fold AI into existing model-risk programmes, keep an AI inventory, treat AI as high risk by default, and use human oversight.

## Local context: Kyrgyzstan

- NBKR approved a SupTech concept and roadmap for 2026–2031, using AI, ML, and big data to supervise banks. This is about the regulator's own tools, not rules for banks. [Open.kg](https://open.kg/en/news/economy/122684-postanovleniem-pravlenija-nacbanka-kyrgyzstana-utverzhdena-koncepcija-i-dorozhnaja-karta-razvitija-nadzornyh-tehnologij-suptech-na-20262031-gody.html)
- No binding NBKR rule on bank AI use was found. **Check nbkr.kg and its legal-acts database directly.**
- Kazakhstan's central bank reports about 75% of its banks use AI. [Times of Central Asia](https://timesca.com/kazakhstan-adopts-pragmatic-ai-regulation-in-financial-sector/)

## Gaps

- No verified BBVA or Commonwealth Bank material, and none for Citi or HSBC on operations.
- No data on regional banks in Kyrgyzstan.
- Regulatory items above need confirmation from primary documents.
