# Responsible AI: alignment of the AICC principles

> Mechanisms named on this page refer to the first corpus (archived). The responsible-AI mapping still holds. See [Simplification](../simplification.md).

How the values and the principles of application in the [statement of intent](../../../../charter/documents/statement-of-intent.md) line up with
what banks, fintechs, standards bodies, and regulators publish. The charter carries no references. This page keeps the
lineage. Gathered 2026-09-30.

## Evidence pages

- [Global banks](banks-global.md): 22 banks reviewed, 11 with named principles.
- [Regional and emerging-market banks and regulators](banks-regional.md)
- [Fintech and payments](fintech-payments.md)
- [Standards, regulators, and international bodies](frameworks.md): 29 frameworks.

## How the trust principles align

Counts are from the evidence pages. They rest on the researchers' reading of principle names and, in places, on search
summaries, so treat them as approximate.

| AICC trust principle | Banks naming it (of 11) | Frameworks (of 11) | Notes |
| --- | --- | --- | --- |
| 1 Accountability | 8 | 11 | Named senior owners are common: HSBC, UBS, Santander, Standard Chartered, NatWest. HSBC applies its principles to third-party products, which is where "the bank answers for AI it buys" comes from |
| 2 Fairness | 10 | 9, plus 2 partial | "In the customer's interest" folds in the customer-benefit theme that 4 banks name |
| 3 Transparency and explainability | 10 | 11 | Santander requires users to know they deal with AI. Fintechs tie explainability to specific decisions such as credit adverse action |
| 4 Privacy and data protection | 7 | 10 | Entity boundaries are our addition for a group |
| 5 Security and reliability | 5 | 9, plus 1 partial | AI-specific attacks come from OWASP and the FSB. Fallback and exit plans come from the FSB third-party practice |
| 6 Human oversight and contestability | 4 as a named principle, many more in practice | 8, plus 1 partial (contestability 3) | Only NatWest publishes a right to contest and redress. Kept as a principle because the frameworks ask for it |
| 7 Compliance and proportionate control | Implicit in all, and shown in governance patterns | 10 (risk-based) | Risk tiering by materiality is the common mechanism across frameworks |

Not adopted as principles:

- **Sustainability:** named by 5 of 11 banks, mostly European or Australian. Recorded as an open item.
- **Skills and literacy:** named by 4 banks as a principle. UBS and Santander make training mandatory. It is a value (respect
  for people) and a stage policy (trained domain expert before pilot).

Values: integrity, prudence, and respect for people are the values of AI adoption in the statement of intent. They are our
own choice, because no group values were found (see [group context](../../soi/group-context.md)). Integrity and prudence map
to "compliance by design" and to risk-tiered speed.

## Mechanisms the frameworks ask for, and where the operating model has them

| Mechanism | Where it lives in the operating model | Status |
| --- | --- | --- |
| Human oversight | Risk tiers set the level. Control function contacts and the Domain Owner hold authority | Policy stub: risk tiers |
| Inventory and registry | Platform registry kept by the Platform Owner, entries by engineers | Covered. Platform owner open |
| Risk tiering | Intake stage, confirmed by the control function contacts | Covered |
| Impact assessment | Discovery stage for customer-affecting or higher-tier use cases | Added |
| Documentation | Engineers, with templates from the enablement group | Covered by templates |
| Logging and records | Platform evidence | Covered. Retention set by policy |
| Testing and monitoring | Pilot and Operate stages, validation by control function contacts | Covered |
| AI-specific security | Information security contact | Covered |
| Third-party AI | Third-party AI policy | Policy stub added |
| Incident reporting | AI incident policy, RACI row for reporting | Policy stub and RACI row added |
| Customer disclosure and contestability | AI use policy and risk tiers | Policy stubs |
| Fairness testing | Model risk and compliance contacts, at discovery and pilot | Covered |
| AI literacy | Enablement group, trained before pilot | Covered |
| Independent challenge and audit | Model risk and internal audit contacts | Covered |
| Board oversight and risk appetite | Board Committee report. AI risk appetite in the charter, RACI row added | Charter stub |

## Distinctive positions worth remembering

- HSBC's test: AI is not used for a decision that would be indefensible if a person made it.
- NatWest: the only published right to contest an AI decision and get redress.
- Santander: users must always know they are dealing with AI.
- UBS: three principles only, with mandatory annual training.
- Banks with no principles list (JPMorgan, Citi, Goldman, Barclays, Bank of America, Wells Fargo) rely on existing model
  risk and enterprise risk structures. That is a legitimate alternative. We publish principles because AICC needs a
  shared vocabulary across domains and entities.
- No bank reviewed publishes a list of prohibited uses. Ours will, in the AI use policy.
- Payments companies express trust as protocol design: scoped agent tokens, signed requests, spending caps, audit
  trails. This matters for agentic payments in the group.

## What binds locally

- Binding in Kyrgyzstan: the Digital Code, in force about February 2026. Its AI articles were not read. Existing NBKR
  requirements on risk, outsourcing, IT, and information security apply by their general terms.
- No NBKR rule on AI use by banks was found. The draft AI ethics regulation reported on 28 September 2026 does not
  mention banks.
- Binding only if a group entity has a link: Kazakhstan's AI law (in force 18 January 2026) and the EU AI Act.
- Voluntary: OECD, NIST, ISO 42001, FSB, MAS, and the other frameworks. They still matter through correspondent banks,
  card schemes, vendors, and financing parties.
- The charter therefore says "applicable law" and does not name statutes.

## Confidence and gaps

- Most sources were read only through search summaries. Each evidence page marks what was read at source.
- Many 2026 items are single-source or unverified. They are listed on the evidence pages.
- The theme counts and the fear-to-principle mapping are our own judgement.
- Which laws apply to each group entity is unknown and needs legal review.
