---
title: AI terms in plain words
summary: The AI terms you need most if you don't work with AI every day: kinds of systems, building and using them, kinds of failure, working with risk.
order: 20
related: reference/vocabulary, responsible-ai, responsible-ai/how-we-apply-it
source_hash: cb7642effa06
---

This page explains, in plain words, the technology terms that come up in the Responsible AI section. The terms for how the Hub works are collected in the general [vocabulary](page:reference/vocabulary).

## Kinds of systems {#systems}

| Term | What it means |
| --- | --- |
| Artificial intelligence, AI | A machine system that, from its input data, produces a prediction, content, a recommendation, or a decision to achieve given goals. This is the definition the OECD and the EU use |
| Model | A pattern found during training: a function that turns input data into a result. A scorecard and a language model are both models |
| [[machine-learning|Machine learning]] | A way to build a model from examples instead of writing its rules by hand |
| [[llm|Large language model (LLM)]] | A model trained on very large amounts of text to predict the next fragment; the basis of generative AI for working with language |
| [[generative-ai|Generative AI]] | AI that creates content, such as text, images, or code, rather than only a prediction or a class |
| Assistant | An application that helps the user with answers, suggestions, or drafts but doesn't take actions in systems itself |
| [[ai-agent|AI agent]] | A system in which the model works out the steps toward a goal itself and acts through tools: it gets data, calls services, fills in forms |

## Building and using {#building}

| Term | What it means |
| --- | --- |
| [[fine-tuning|Fine-tuning]] | Additional training of an existing model on data for a specific task |
| [[prompt|Prompt]] | The instructions and context the model receives at the moment of use; a system prompt is a standing instruction from the developer |
| [[context-window|Context window]] | The amount of text the model takes into account at once; it doesn't see whatever doesn't fit |
| [[token|Token]] | A unit of text for a language model: a word or part of one; costs and limits are counted in tokens |
| [[rag|Retrieval-augmented generation (RAG)]] | At the moment of the question, the model receives relevant fragments of verified documents and answers from them, with references |
| [[grounding|Grounding]] | Tying the model's answers to verified sources so that they can be double-checked |
| [[evaluation-set|Evaluation set]] | Real cases with expected results; the solution is checked against them before launch and after every noticeable change |
| [[guardrails|Guardrails]] | Rules, filters, and restrictions around the model: what it may respond to and which actions it is allowed to take |
| [[human-in-the-loop|Human in the loop]] | An employee reviews every result before it is used |
| [[human-on-the-loop|Human on the loop]] | A person watches the system and can step in and stop it |
| [[model-gateway|Model gateway]] | A single point of access to models: request routing, cost tracking, logs, data protection |

## Kinds of failure {#failures}

| Term | What it means |
| --- | --- |
| [[hallucination|Hallucination]] | A smooth, confident, and wrong result: a fact, figure, or source reference that doesn't exist |
| [[bias|Bias]] | Systematic unfairness in results, learned from the data or built in during design |
| [[model-drift|Drift]] | A model's quality declining as reality drifts further from the data it was trained on |
| [[prompt-injection|Prompt injection]] | Text in the input that the model carries out as an instruction: typed directly by a user or hidden in a document or web page |
| [[jailbreak|Jailbreak]] | A specially crafted prompt that makes the model forget its guardrails |
| [[data-leakage|Data leakage]] | Data ends up where it shouldn't be: with the vendor, in an answer to another user, in a log |
| [[data-poisoning|Data poisoning]] | Deliberately corrupting the data a model learns from, or the documents it takes information from |
| [[excessive-agency|Excessive agency]] | An AI agent has more functions, access rights, or autonomy than its task needs |
| [[overreliance|Over-reliance]] | People accept results without double-checking them, because the system is usually right |

## Working with risk {#risk}

| Term | What it means |
| --- | --- |
| [[responsible-ai|Responsible AI]] | Principles and practices that let whoever uses AI answer for its results; more on the [Responsible AI](page:responsible-ai#principles) page |
| [[risk-tier|Risk tier]] | An assessment of how serious the consequences of a mistake by an AI solution would be; it is set by the data, the influence on decisions, whether results reach customers, and autonomy |
| [[risk-based-approach|Risk-based approach]] | Controls are proportionate to the risk; this is the basis of the EU Artificial Intelligence Act (AI Act), the NIST AI Risk Management Framework, and the risk tiers in our projects |
| [[high-risk-ai|High-risk AI]] | In the AI Act, the uses listed in it, including credit scoring of individuals, that must meet the full set of requirements |
| [[model-risk-management|Model risk management]] | The long-standing practice of validating, documenting, and monitoring models with an assigned owner; working with AI extends it to new systems |
| [[independent-review|Independent review]] | Review of a solution by a person who didn't take part in building it; in the medium and high tiers, together with risk, security, and legal specialists |
| [[explainability|Explainability]] | The ability to explain why a system produced a given result, in a way that the explanation can be relied on |
| [[impact-assessment|Impact assessment]] | An assessment of how a higher-risk use will affect people and their rights; it is done before launch |
| [[model-card|Model card]] | A short description of a model or system: what it is, what it's for, how it was tested, where it shouldn't be used |
| [[ai-literacy|AI literacy]] | Understanding what AI can and can't do; everyone who uses it needs it |
| [[ai-incident|AI incident]] | An event in which a use of AI causes or could cause harm, including harm that was prevented |
| [[shadow-ai|Shadow AI]] | AI tools used at work in place of the tools meant for that kind of data |

## Financial services {#fintech}

| Term | What it means |
| --- | --- |
| [[kyc|Know your customer (KYC)]] | Establishing a customer's identity and assessing the risk linked to them, at onboarding and throughout the relationship |
| [[liveness-check|Liveness check]] | Checking that the document is presented by a person who is actually there, not by a photo or recording of them |
| [[alternative-data|Alternative data]] | Data other than credit history used to assess a customer: transaction, mobile, behavioral; it raises questions of fairness and consent |
| [[real-time-scoring|Real-time scoring]] | A score the model gives right during a transaction, for example in fraud detection |
