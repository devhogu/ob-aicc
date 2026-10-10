---
title: Model risk and AI in lending
summary: US rules on how banks review their models and how they explain a credit refusal to a customer; a model of practice you will find under any supervisor.
nav: false
source_hash: 5f96ba403e1a
---
## Briefly {#short}

The banking world looks to the United States as a model on two topics. The first is [[model-risk-management|model risk management]]: supervisory guidance from the Federal Reserve, the Office of the Comptroller of the Currency (OCC), and the Federal Deposit Insurance Corporation (FDIC) on how a bank builds, reviews, and controls its models. The second is the Equal Credit Opportunity Act and its Regulation B: a lender must give a customer the specific reasons for refusing credit, however complex the model. None of this is binding on us; it is a benchmark of best practice.

## What it means in practice {#practice}

A model that influences decisions about customers, such as a scoring model or a fraud detection model, can't simply be bought and switched on. It is reviewed by someone who took no part in building it, its performance is monitored after launch, and its limitations are written down. This is [[independent-review|independent review]], and it is needed even when the model comes from a well-known supplier.

If AI takes part in a credit decision, the bank must be able to explain to the person why they were refused, in plain and specific words: “high debt burden,” not “did not pass scoring.” That is why [[explainability]] is built into a solution from the start. For an employee, the takeaway is this: an AI result about a customer is a hint you must understand and be able to explain, not a ready answer.

## Key ideas {#ideas}

- **Model risk.** A model can be wrong or used for the wrong purpose, leading to losses and bad decisions. This risk is managed like any other.
- **The full model life cycle.** Attention at every step: development and use, validation and monitoring, governance and controls, and separately, models and products from suppliers.
- **[[independent-review|Independent review]].** A model is reviewed by people not involved in building it, and after launch it is checked regularly to see whether it has gotten worse.
- **Scaled to risk.** The more important a model and the greater its impact, the deeper the review; small, simple models need less. This is the [[risk-based-approach|risk-based approach]].
- **Specific reasons for refusal.** When credit is refused, the customer is told the main specific reasons. The rule expressly says that phrases like “does not meet our internal standards” or “insufficient credit score” are not enough.

## Good to know {#details}

- For 15 years the model was the Federal Reserve's guidance SR 11-7 of 4 April 2011 (and the matching OCC Bulletin 2011-12). On 17 April 2026 the Federal Reserve, the OCC, and the FDIC replaced them with new joint guidance: SR 26-2 and OCC Bulletin 2026-13.
- The new guidance is shorter and built on principles. It is most relevant to banks with more than $30 billion in assets; the agencies state plainly that a bank will not be criticized by supervisors for not following it.
- [[generative-ai|Generative AI]] and [[ai-agent|AI agents]] are outside the new guidance: the agencies call them novel and rapidly evolving and promise a separate request for information on banks' use of AI. Whether that request has been issued is not confirmed.
- The requirement to give specific reasons for refusal is set out in Regulation B, which the Consumer Financial Protection Bureau (CFPB) interprets. On 12 May 2025 the CFPB withdrew a number of its guidance documents, including a 2022 one on how this requirement applies to credit decisions made with complex algorithms. The Regulation B requirement itself still applies.

## Where to read more {#read}

- [SR 26-2 on the Federal Reserve website](https://www.federalreserve.gov/supervisionreg/srletters/SR2602.htm) — the official letter on the new model risk management guidance and what it replaces · language: English
- [OCC Bulletin 2026-13](https://www.occ.gov/news-issuances/bulletins/2026/bulletin-2026-13.html) — the same from the OCC, with a short summary and the exclusion of generative AI · language: English
- [Regulation B, § 1002.9, on the CFPB website](https://www.consumerfinance.gov/rules-policy/regulations/1002/9/) — the official text of the requirement to give specific reasons for refusal, with examples · language: English
- [CFPB withdrawn guidance](https://www.consumerfinance.gov/compliance/guidance/withdrawn-guidance/) — the list of withdrawn documents, including the one on refusals based on complex algorithms · language: English

## Related {#related}

- [US AI policy](page:reference/regulation/us-federal-and-state-ai-policy)
- [NIST AI Risk Management Framework](page:reference/regulation/nist-ai-rmf)
- [EU Artificial Intelligence Act (AI Act)](page:reference/regulation/eu-ai-act)
- [Responsible AI](page:responsible-ai)
