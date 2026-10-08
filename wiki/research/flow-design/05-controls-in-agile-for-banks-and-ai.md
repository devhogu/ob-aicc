# Research report: Controls in agile for banks and AI

Collected on 2026-10-08 by an independent research agent for the flow redesign (change C-FLOW-REDESIGN), from the brief in this folder. Source quality is stated in each report: claims marked unverified come from memory, and several official pages (SAFe, PMI, ITIL) were gated or paywalled, so summaries and practitioner pages were used.

**Research return: light governance for a small AI unit in a bank (about 690 words)**

**1. Best-fit practices**
1. **Risk-tiered approval (controls, Portfolio).** Classify each Initiative into 3 tiers at Intake. The EU AI Act's four tiers (banned, high, limited, minimal) are a pattern, not Kyrgyz law. Tier 3 (internal, no customer impact, no personal data) is self-certified by the team. Tier 1 (customer-facing, decisioning, personal data) gets the full clearances. This keeps the number of gates the same for the unit but makes most work skip most of them.
2. **Compliance inside the Definition of Done (Team).** Risk and security checks are acceptance items on the story or feature, not separate phases. This is the McKinsey "risk by design" and compliance-as-code pattern, with controls embedded in the delivery flow. For three people, DoD lines per tier are cheaper than any forum.
3. **Three Lines applied lightly (controls).** The AICC is first line and owns its risks. Information security, model risk and compliance are second line and give advice and oversight. Internal audit is third line. The IIA stresses collaboration among the lines, not separate silos. Second-line people are consulted on request and are not squad members, because they must stay independent. ING did this: legal, finance and operational risk are "not part of a squad" but can be called on (secondary snippet).
4. **Effective challenge, proportionate (controls).** SR 11-7 required independent validation and a model inventory. It was superseded on 17 April 2026 by SR 26-2, which is risk-based and judges independence by the quality of the review, not the org chart. Generative and agentic AI are reportedly outside SR 26-2, which I have only from a third-party summary. Adopt the principle: depth of validation scales with materiality, and the reviewer must be competent and not the builder.
5. **A thin AI management system (Portfolio, controls).** ISO/IEC 42001 gives the skeleton: an AI inventory, a risk and impact assessment per system, and a Statement of Applicability showing which controls apply and why. NIST AI RMF (Govern, Map, Measure, Manage) is the same loop without certification. Use both as checklists, not as programmes. ISO/IEC 38507 asks the governing body to set direction and accountability, which is what the Steering forums should do.
6. **Pre-agreed rules instead of meetings (decision-making).** Decide by rule: WSJF threshold, WIP limits, tier-based approver, envelope limits. Escalate only on exceptions. This follows SAFe-style guardrails (unverified, from memory).
7. **Four-eyes by Pull Request (Team).** Every change to a prompt, model or data pipeline is approved by a second person. Tier 1 needs a reviewer outside the team. This is the cheapest independent check in a short cycle.
8. **Registry plus decision log as the only audit trail (artefacts).** One AI registry row per solution and one dated decision record per gate.

**2. Decision rights and forums**
- Discover: the unit lead triages the Funnel weekly in async mode. There is no forum. A tier is assigned on entry using a short checklist.
- Portfolio: Domain Owner approval of the Brief stays, but only for tier 1 and 2 and for work above a size threshold. Tier 3 and run-rate work go to Pull on a rule. Fewer than 3 people means one monthly Steering forum, with quarterly and yearly reviews held as agenda items inside it.
- Program: the lead sequences Features within the envelope. Escalate only when the envelope, tier or WIP limit is breached.
- Team: the product owner accepts. The independent test or reviewer signs off by tier.
- Rule-decided: tier assignment, Pull while WIP is available, and the post-MVP decision using pre-agreed continue, pivot, defer, reject criteria.
- Meeting-decided: a new tier-1 Initiative, a tier change, and an exception.

**3. Artefacts**
Keep:
- the Initiative Brief (tiered, one page for tiers 2 and 3)
- the AI registry (owner, tier, data class, clearances, status, validation date)
- the decision log
- tier-1 validation or test reports
- the Jira DoD evidence (PR, test result)
- a monthly Steering note (decisions only)

Drop:
- separate status decks per level
- duplicate Kanban views kept off Jira
- per-Iteration plans written outside Jira
- retrospectives written up as documents
- full impact assessments for tier 3

**4. Avoid or discard**
- Four levels of full SAFe ceremony. PI planning, ART sync and scrum-of-scrums for three people are overhead (my judgement).
- Separate Discover and Portfolio approval gates: merge Intake, Scoped and Approval into one tiered decision.
- A forum for each cadence: one monthly forum with three agenda depths.
- WSJF scoring of everything: use it only to break ties above the WIP limit.
- Full ISO 42001 certification. It is not needed at this size, so use the structure only.
- Second-line sign-off on tier 3 work.

**5. Regulated-bank points**
- Independence matters more than speed: the builder cannot validate their own tier-1 solution, and the third line must stay out of second-line decisions.
- Keep audit read access to the registry, the log and Jira. Evidence should be produced as a by-product of work, not written afterwards.
- Check which current NBKR rules (model risk, outsourcing, personal data) apply. I did not research Kyrgyz regulation, so this is **unverified**.
- A material change (new model, new data class) re-triggers the tier check, so the tier is not a one-time label.
- The model-risk definition is narrowing in some regimes, so state in the AICC policy that generative AI is in scope. This is my recommendation.

**6. Sources** (all public, no login)
- IIA, Three Lines Model, 2020, updated 2024: https://www.theiia.org/ThreeLines (fetched)
- Federal Reserve, SR 26-2, 17 April 2026, supersedes SR 11-7: https://www.federalreserve.gov/supervisionreg/srletters/sr2602.htm (fetched). The generative-AI exclusion comes only from https://www.creditbenchmark.com/knowledge-base/sr-26-2-model-risk-management/ (2026, secondary).
- Federal Reserve, SR 11-7, 2011 (superseded): https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm (search result only)
- NIST, AI RMF 1.0, January 2023, and Generative AI Profile, July 2024: https://www.nist.gov/itl/ai-risk-management-framework (fetched)
- ISO/IEC 38507:2022, ISO/IEC JTC 1/SC 42: https://committee.iso.org/sites/jtc1sc40/home/projects/wg-1/published-wg1/content-left-area/list-of-publications/iso-iec-38507-2022.html (search result only)
- ISO/IEC 42001:2023 (inventory, SoA, Annex A of 38 controls): https://www.surecloud.com/resource-hub/iso-42001-annex-a-controls (vendor summary, secondary)
- EU AI Act tiers: https://gdprlocal.com/europe-ai-act-summary/ (secondary summary; the legal text is on EUR-Lex)
- McKinsey, "ING's agile transformation", 2017: https://www.mckinsey.com/industries/financial-services/our-insights/ings-agile-transformation (search snippet only; the fetch timed out)
- McKinsey, "How agile operating models benefit risk and compliance functions": https://mckinsey.com/capabilities/risk-and-resilience/our-insights/how-agile-operating-models-benefit-risk-and-compliance-functions (search snippet only)
- McKinsey, "Lessons from banking to improve risk and compliance", compliance as code and risk by design: https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/lessons-from-banking-to-improve-risk-and-compliance-and-speed-up-digital-transformations (search snippet only)

**Unverified (memory only):** Capital One, Danske and Sberbank governance specifics (searches found nothing specific), and the SAFe guardrails and lean portfolio claims.
