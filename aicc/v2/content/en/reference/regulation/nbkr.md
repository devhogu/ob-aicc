---
title: National Bank of the Kyrgyz Republic
summary: The central bank and supervisor of banks; its requirements on information security, outsourcing, and bank secrecy apply to any use of AI that touches banking processes and customer data.
nav: false
source_hash: 362580521bbb
---
## Briefly {#short}

The National Bank of the Kyrgyz Republic is the country's central bank. It licenses banks, supervises them, and issues regulations that are binding on them: on risk, information security, outsourcing, remote services, and payment systems. Its status is set by the 2022 constitutional law on the National Bank, and the work of banks by the 2022 Law on Banks and Banking Activities. We did not find a separate National Bank act on AI, but its general requirements apply to AI as well.

## What it means in practice {#practice}

**An outside company's AI service is outsourcing.** The law allows a bank to engage another party under contract for services it needs, and the National Bank sets the requirements for such outsourcing. Its information security regulation directly requires assessing the risk of outsourcing, including data centers, cloud technologies, and cloud services. A cloud AI service falls here too.

**The contract with the provider must have mandatory sections:** on information security and the safekeeping of personal data and secrets, on business continuity and recovery, and on cooperating with National Bank inspections. In its continuity plan, the bank decides in advance how it will get back the data it handed over and keep working if the provider has a failure.

**Customer data is a bank secret.** Bank secrecy covers any information the customer gave the bank or that arose from the bank's relationship with the customer. As a rule, the bank may disclose it to others only with the customer's separate written consent. So customer details must not be pasted into an unapproved AI tool, even “just to word a letter” (see [What you can and cannot share with AI](page:kb/guides/what-to-share)).

**For employees.** Use the internet and online services only for purposes the bank has approved: the National Bank's regulation requires exactly this. Approved AI tools are those that have passed a risk assessment and are connected by the rules; personal accounts and free versions that bypass these rules are [[shadow-ai|shadow AI]].

## Key ideas {#ideas}

- **Outsourcing.** Engaging an outside provider to perform certain work and services on an ongoing basis. Before doing so, the bank assesses the risk using all the information it has about the provider and shows this assessment to the National Bank on request.
- **Information security.** Uniform requirements for banks: access management, event logs, risk management, business continuity, backups, data protection, and handling incidents and vulnerabilities.
- **Data protection.** The bank must protect personal data, bank secrets, and other information protected by law, and process personal data as the law requires, which today means the Digital Code.
- **Bank secrecy.** Information about a customer and their relationship with the bank. The rules on it also apply to other organizations the National Bank supervises.
- **Incidents.** Information security incidents are identified, assessed, and analyzed so that they don't happen again. If data leaked through an AI tool or it behaved in a dangerous way, report it at once, as with any [[ai-incident|AI incident]].

## Good to know {#details}

- Constitutional Law No. 92 on the National Bank of the Kyrgyz Republic and Law No. 93 on Banks and Banking Activities were adopted on 11 August 2022.
- The Regulation on Information Security Requirements in Commercial Banks of the Kyrgyz Republic was approved by Resolution No. 2021-P-20/72-8-(NPA) of the National Bank Board of 22 December 2021; it has since been amended, including on information security audits.
- The National Bank has separate regulations on risk management, remote services, and remote identification of customers; all of them are published in the regulations section of nbkr.kg.
- National Bank regulations are binding on banks, and the National Bank may inspect how a bank complies with them.

## Where to read more {#read}

- [Regulation on Information Security Requirements in Commercial Banks](https://www.nbkr.kg/contout.jsp?item=2145&lang=RUS&material=106193) — the official text on the National Bank's website; outsourcing and cloud are in Chapter 19 · language: Russian
- [National Bank regulations](https://www.nbkr.kg/index1.jsp?item=2145&lang=RUS) — the full list of regulations for banks, including amendments · language: Russian
- [Law on Banks and Banking Activities](https://cbd.minjust.gov.kg/4-3214/edition/57502/ru) — the official text; outsourcing is in Article 48, bank secrecy in the chapter on bank secrecy (Articles 66–72) · language: Russian
- [Constitutional Law on the National Bank of the Kyrgyz Republic](https://cbd.minjust.gov.kg/112424/edition/40032/ru) — the National Bank's status, objectives, and powers · language: Russian
- [National Bank of the Kyrgyz Republic](https://www.nbkr.kg/index.jsp?lang=ENG) — the English version of the National Bank's website; we did not find official English translations of these acts · language: English

## Related {#related}

- [Digital Code of the Kyrgyz Republic](page:reference/regulation/kg-digital-code)
- [Anti-money laundering and countering the financing of terrorism](page:reference/regulation/kg-aml-body)
- [Requirements for the hazard assessment of AI systems (Resolution No. 770)](page:reference/regulation/kg-high-risk-ai-requirements)
- [FSB, Basel Committee and BIS on AI](page:reference/regulation/financial-standard-setters-on-ai)
- [Digital Operational Resilience Act (DORA)](page:reference/regulation/eu-dora) — similar requirements for ICT providers in the EU
- [Responsible AI](page:responsible-ai) and [What you can and cannot share with AI](page:kb/guides/what-to-share)
- [Regulatory Horizon](page:catalog/regulatory-horizon)
