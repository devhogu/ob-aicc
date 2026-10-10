---
title: OWASP Top 10 for Large Language Model Applications
summary: The OWASP community's list of the ten main security risks of applications built on large language models; it is used to test generative AI solutions and to learn to spot attacks in everyday work.
nav: false
source_hash: 50d99b2531eb
---
## Briefly {#short}

OWASP is an international nonprofit community of application security specialists. Its generative AI security project maintains a list of the ten main risks of applications built on [[llm|large language models (LLMs)]]. The current edition is the 2026 edition, published in August 2026. The list is voluntary: not a law or a standard, but a widely accepted benchmark that developers and security specialists use to test AI solutions.

## What it means in practice {#practice}

For teams that build or roll out generative AI solutions, this is the list of attacks you need to be able to test for before launch. But many of the risks on the list affect any employee who uses an AI assistant:

- **Someone else's document with a planted command.** You ask the assistant to summarize a customer's email, a web page, or a file, and hidden inside is text like “forget your previous instructions and …”. The assistant may carry out that command. This is [[prompt-injection|prompt injection]], the first risk on the list. Always check the result when the assistant worked on someone else's document.
- **Extra data in the prompt.** Anything you paste into a prompt may end up where it shouldn't: in a reply to another person, in the service's logs, with the supplier. This is sensitive information disclosure, the second risk. Don't give AI more customer or colleague data than needed; see [What you can and cannot share with AI](page:kb/guides/what-to-share).
- **The assistant does more than you asked.** If the assistant is connected to email, files, or other systems, it may send an email or change or delete a file without your direct decision. This is [[excessive-agency|excessive agency]], the third risk. Give the assistant only the access it needs, and confirm its actions.
- **A confident but wrong answer.** The model can make up a fact, a figure, or a link, and it sounds convincing. On the list this is misinformation. Check everything you pass on, and don't give in to [[overreliance|overreliance]].
- **Unvetted extensions and services.** A third-party plugin, an unknown model, or a free online service is a supply chain risk. Use only the tools and accounts approved in your organization.
- **Code and text without review.** If code, a formula, or text from the assistant is run or sent on right away, a mistake or a harmful insertion reaches working systems. This is improper output handling.

## Key ideas {#ideas}

- **The ten risks of the 2026 edition.** In order: [[prompt-injection|prompt injection]]; sensitive information disclosure; [[excessive-agency|excessive agency]]; supply chain; [[data-poisoning|data and model poisoning]]; unbounded consumption; misinformation; hidden context exposure; vector and embedding weaknesses, the search that [[rag|retrieval-augmented generation (RAG)]] is built on; and improper output handling.
- **The model can be fooled.** The edition's main message: don't count on a model that can't be fooled; build the system around it so that when it is fooled, nothing important breaks.
- **Commands and data get mixed.** To a model, instructions and ordinary text are one stream, so a command can arrive from any document, email, image, or another system's reply. This path can't be closed completely; the risk can only be reduced.
- **Hidden context will sooner or later be exposed.** System instructions, internal rules, and tool descriptions that the user doesn't see can leak. So they don't hold secrets, and protection isn't built on them.
- **Experience plus real cases.** The order of the list is set by a vote of practitioners (three-quarters of the weight), adjusted by data on real incidents (one quarter). For the 2026 edition, 6,639 described incidents were analyzed.

## Good to know {#details}

- The first version of the list came out on 1 August 2023, the 2025 edition on 18 November 2024, and the 2026 edition in August 2026.
- In the 2026 edition, excessive agency rose from sixth place to third, system prompt leakage was broadened into hidden context exposure, and improper output handling fell from fifth place to tenth.
- OWASP covers the risks of [[ai-agent|AI agents]], which call tools and act on their own, in a separate list, the OWASP Top 10 for Agentic Applications.
- The list is free and released under the open CC BY-SA 4.0 license. OWASP has published a Russian translation of the 2025 edition; there is no translation of the 2026 edition yet.
- It is not a regulator's requirement but a benchmark. For each risk, the document gives examples of attacks and ways to defend against them.

## Where to read more {#read}

- [OWASP Top 10 for LLM Applications 2026](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/) — the official page of the edition and the full text to download, PDF · language: English
- [Announcement of the 2026 edition](https://genai.owasp.org/2026/09/01/owasp-genai-security-project-unveils-2026-top-10-for-llm-applications-new-agent-control-standard-and-sponsors-as-community-tops-30000-members/) — what's new in the edition, in brief · language: English
- [The 2025 edition in Russian](https://genai.owasp.org/resource/owasp-top-10-%d0%b4%d0%bb%d1%8f-llm-%d0%b8-%d0%b3%d0%b5%d0%bd%d0%b5%d1%80%d0%b0%d1%82%d0%b8%d0%b2%d0%bd%d0%be%d0%b3%d0%be-%d0%b8%d0%b8-2025/) — a translation of the previous edition published by OWASP; most of the risks in it are the same · language: Russian
- [Prompt injection is not SQL injection](https://www.ncsc.gov.uk/blog-post/prompt-injection-is-not-sql-injection) — a clear explanation from the UK National Cyber Security Centre (NCSC) of why prompt injection can't be fully eliminated · language: English

## Related {#related}

- [NIST AI Risk Management Framework](page:reference/regulation/nist-ai-rmf)
- [ISO/IEC standards on AI (including ISO/IEC 42001)](page:reference/regulation/iso-iec-ai-standards)
- [What you can and cannot share with AI](page:kb/guides/what-to-share)
- [Responsible AI](page:responsible-ai) and [How we apply it](page:responsible-ai/how-we-apply-it)
- [Regulatory Horizon](page:catalog/regulatory-horizon)
