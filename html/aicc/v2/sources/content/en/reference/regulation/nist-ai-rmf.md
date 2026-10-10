---
title: NIST AI Risk Management Framework
summary: NIST's voluntary framework for managing AI risk; the most practical benchmark when you need to decide how to check an AI solution and who is responsible for what.
nav: false
source_hash: 332ef51a07ad
---
## Briefly {#short}

The AI Risk Management Framework (AI RMF) is a framework for managing AI risk published by NIST, the US National Institute of Standards and Technology. Version 1.0 (document NIST AI 100-1) came out on 26 January 2023. It is voluntary: not a law, but a set of clear steps that any organization in any country can use. In July 2024 NIST added a separate profile for [[generative-ai|generative AI]] (NIST AI 600-1).

## What it means in practice {#practice}

For us, this is the most practical framework of all: we rely on it when we explain [[risk-tier|risk tiers]] and a project's checkpoints. It doesn't need a dedicated department or a big program, and it works even for a small pilot.

An example: a team runs a pilot in which an AI assistant drafts replies to customer complaints. Here is how the framework's four functions look on such a pilot:

- **Govern.** Name the person responsible for the pilot and agree on the rules: which data may be given to the assistant, who checks the replies, and what result stops the pilot. Write this down on the project card.
- **Map.** Who will use the assistant, whom the replies affect, and what can go wrong: a wrong fact in a reply, customer data ending up where it shouldn't, a different tone for different customers. This sets the risk tier.
- **Measure.** Test the assistant on an [[evaluation-set|evaluation set]] of anonymized past complaints: how many replies are correct, how many [[hallucination|hallucinations]] there are, where a reply sounds rude or unfair. Record the results so you have something to compare against.
- **Manage.** Decide what to do about the risks you found: an employee checks every reply before it goes out, personal data stays out of the prompt, and there is a clear procedure in case of an error. Look again in a month.

If you simply use an AI assistant at work, the main thing to remember from the framework is this: AI output has to be checked, and a person stays responsible for it.

## Key ideas {#ideas}

- **Trustworthy AI.** The framework names seven characteristics of such AI: valid and reliable; safe; secure and resilient; accountable and transparent; explainable and interpretable; privacy-enhanced; and fair, with harmful [[bias|bias]] managed.
- **Four functions.** Govern, Map, Measure, and Manage. Govern is the foundation that runs through everything; the other three usually follow in that order and repeat in a cycle.
- **Risk depends on the use.** The same model can be harmless in one task and dangerous in another. So you first describe where and for what the AI is used, and only then decide how many checks are needed. This is the [[risk-based-approach|risk-based approach]].
- **Risks of generative AI.** The NIST AI 600-1 profile sets out 12 risks that generative AI creates or makes worse. They include confidently stated made-up content (hallucinations), leaks of personal data, bias, information security threats, intellectual property violations, and people trusting the machine too much.
- **A practical guide.** The Playbook is a free online collection of suggested actions for each function. It isn't a mandatory checklist: you take what fits the task.

## Good to know {#details}

- AI RMF 1.0 was published on 26 January 2023, and the generative AI profile on 26 July 2024.
- The framework is voluntary, and there is no certification against it. You can apply it in parts, as your resources allow.
- NIST says version 1.0 is now being revised. What exactly will change has not been announced yet.
- All the documents are free and published in English. NIST does not publish an official Russian translation.

## Where to read more {#read}

- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) — the official page: about the framework, news on the revision, all documents · language: English
- [AI RMF 1.0 (NIST AI 100-1)](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf) — the full text of the framework, PDF · language: English
- [AI RMF Playbook](https://airc.nist.gov/airmf-resources/playbook/) — suggested actions for each of the four functions · language: English
- [Generative AI Profile (NIST AI 600-1)](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf) — 12 risks of generative AI and actions against them, PDF · language: English
- [NIST AI Resource Center](https://airc.nist.gov/) — NIST's hub of AI materials: the framework, guides, use examples · language: English

## Related {#related}

- [ISO/IEC standards on AI (including ISO/IEC 42001)](page:reference/regulation/iso-iec-ai-standards)
- [OWASP Top 10 for Large Language Model Applications](page:reference/regulation/owasp-top-10-llm)
- [Requirements for the hazard assessment of AI systems and for high-hazard AI systems](page:reference/regulation/kg-high-risk-ai-requirements)
- [Responsible AI](page:responsible-ai) and [How we apply it](page:responsible-ai/how-we-apply-it)
- [Regulatory Horizon](page:catalog/regulatory-horizon)
