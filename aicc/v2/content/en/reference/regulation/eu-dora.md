---
title: Digital Operational Resilience Act (DORA)
summary: The European law on how financial institutions manage information technology risk, incidents, and suppliers; the clearest model of what supervisors expect, including for AI services.
nav: false
source_hash: 0a08cc537231
---
## Briefly {#short}

DORA (Digital Operational Resilience Act) is the European Union regulation on digital operational resilience for the financial sector (Regulation (EU) 2022/2554 of 14 December 2022). It has applied since 17 January 2025 and is binding on banks, insurers, investment firms, and other financial institutions in the EU. The European supervisory authorities, the EBA, EIOPA, and ESMA, prepare the detailed technical standards for it. DORA is not binding on us, but it is the best example of what supervisors expect on outages, resilience, and suppliers.

## What it means in practice {#practice}

For a bank, an AI service is above all an information service from a third-party supplier. In DORA's logic, an organization must know which suppliers it depends on, what the contract says, what happens if the service stops working, and how to leave it if necessary. That is why new AI tools are connected only through the agreed procedure, never on your own: this way the supplier is entered in the shared records and gets reviewed.

For an employee, this means three things. Use only the tools and accounts approved in your organization: an unrecorded service is [[shadow-ai|shadow AI]] that nobody knows about when something fails. If an AI tool behaves oddly, shows someone else's data, or stops working in an important process, report it at once: it may be an [[ai-incident|AI incident]]. And an important process where AI helps must have a fallback: work must not stop if the service is unavailable.

## Key ideas {#ideas}

- **ICT risk management.** The organization has a framework that helps it identify threats to its information and communication technology (ICT), protect itself, detect failures, respond, and recover. Ultimate responsibility lies with management.
- **Incident reporting.** Major ICT incidents are classified under common rules and reported to the supervisor.
- **Resilience testing.** Systems are tested regularly, from basic vulnerability checks to advanced tests that simulate a real attack for larger institutions.
- **Third-party risk.** Contracts with ICT suppliers contain mandatory terms, and the organization keeps a register of such contracts and an exit plan in case it has to switch suppliers.
- **Oversight of critical suppliers.** The largest suppliers that the whole financial sector depends on, such as cloud providers, are under the direct oversight of the European authorities.
- **Information sharing.** Financial institutions can share information about cyber threats with each other on a voluntary basis.

## Good to know {#details}

- Adopted on 14 December 2022, applied since 17 January 2025.
- Oversight: the national financial regulators of the EU countries; critical suppliers are overseen by the three European supervisory authorities: the EBA (banking), EIOPA (insurance and pensions), and ESMA (securities and markets).
- On 18 November 2025 these authorities designated the first list of critical ICT third-party providers for the financial sector; they now assess how these providers manage risk.
- DORA covers ICT in general, not AI specifically. But the AI services an organization gets from suppliers fall under the same rules on supplier risk and incidents.

## Where to read more {#read}

- [Regulation (EU) 2022/2554 on EUR-Lex](https://eur-lex.europa.eu/eli/reg/2022/2554/oj/eng) — the official text; official versions exist in the EU languages, not in Russian · language: English
- [DORA on the EIOPA website](https://www.eiopa.europa.eu/digital-operational-resilience-act-dora_en) — a clear overview of the main parts of the law and its dates · language: English
- [DORA on the EBA website](https://www.eba.europa.eu/activities/direct-supervision-and-oversight/digital-operational-resilience-act) — oversight of critical suppliers and the technical standards · language: English
- [Designation of critical ICT third-party providers (ESMA)](https://www.esma.europa.eu/press-news/esma-news/european-supervisory-authorities-designate-critical-ict-third-party-providers) — the European supervisory authorities' announcement of 18 November 2025 · language: English

## Related {#related}

- [EU Artificial Intelligence Act (AI Act)](page:reference/regulation/eu-ai-act)
- [National Bank of the Kyrgyz Republic](page:reference/regulation/nbkr)
- [Responsible AI](page:responsible-ai)
- [Regulatory Horizon](page:catalog/regulatory-horizon)
