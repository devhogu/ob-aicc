# AI terms explained

The vocabulary of the field, in plain terms, for the reader of this course. The Vocabulary of the charter defines the terms that the documents use as rules; this page explains the terms of the technology that the documents assume. Where a term is both, the charter's definition prevails.

## 1. Kinds of system

| Term | Meaning |
| --- | --- |
| Artificial intelligence (AI) | A machine-based system that, for a given set of objectives, infers from the input it receives how to produce outputs such as predictions, content, recommendations, or decisions that can influence environments; the definition the OECD and the EU use |
| Machine learning | A way of building a model from examples instead of writing its rules; the model finds the pattern that fits the examples and applies it to new cases |
| Model | The learned pattern itself: a function from inputs to outputs, with parameters set by training. A scorecard, a fraud detector, and a language model are all models |
| Large language model (LLM) | A model trained on very large bodies of text to predict the next token; the basis of generative AI for language |
| Generative AI | AI that produces content, text, images, code, audio, rather than only a prediction or a class |
| Foundation model, general-purpose model | A large model trained for general capability and adapted to many tasks; the EU AI Act calls it a general-purpose AI model |
| Agent, agentic AI | A system in which a model plans and acts toward a goal with tools: it reads, calls services, fills forms, runs code, and chains steps |
| Assistant, copilot | An AI application that helps a person with a task, proposing and drafting, with the person deciding |

## 2. How they are built and used

| Term | Meaning |
| --- | --- |
| Training | The process that sets the parameters of a model from data |
| Fine-tuning | Further training of an existing model on the data of a task or an organization |
| Prompt | The instructions and the context given to a model at the moment of use; a system prompt is the standing instruction set by the builder |
| Context window | How much text a model can take into account at once; what is outside it, the model does not see |
| Token | The unit a language model reads and writes, a word or a part of one; costs and limits are counted in tokens |
| Retrieval-augmented generation (RAG) | Giving the model the relevant passages of approved documents at the moment of the question, so that it answers from them and cites them, instead of from its memory |
| Embedding, vector store | A numeric representation of text that lets a system find the passages most relevant to a question; the store that holds them |
| Grounding | Tying the model's answers to approved sources, so that they can be checked |
| Evaluation, evaluation set | Measuring how well a model or an application performs on a set of cases with known good answers; the set is built with the people who know the work |
| Benchmark | A standard evaluation used to compare models; useful for choosing, not sufficient for approving a use |
| Guardrails | The rules, filters, and limits placed around a model: what it may answer, what it may not, what it may do |
| Human in the loop, human on the loop | A person validates each output before it takes effect; or a person oversees the system and can intervene and stop it |
| Model gateway | A single controlled access point to models, with routing, cost control, logging, and data protection policy |
| Tool gateway | Permissioned access from an AI system to systems and services, with limits per tool |

## 3. How they fail

| Term | Meaning |
| --- | --- |
| Hallucination, confabulation | Fluent, confident, and wrong output: a fact, a figure, a citation that does not exist |
| Bias | Systematic unfairness in outputs, learned from the data or built into the design |
| Drift | The decline of a model's performance as the world moves away from the data it was trained on |
| Prompt injection | Text in the input that the model follows as an instruction against the intent of its builder; direct when the user writes it, indirect when it hides in a document or a page the model reads |
| Data leakage | Data reaching a place it should not: a provider's training set, another user's answer, a log |
| Jailbreak | Input crafted to make a model ignore its guardrails |
| Data poisoning | Corrupting the data a model learns from, or the documents it retrieves, to change its behavior |
| Excessive agency | An agent with more functionality, permissions, or autonomy than its task needs |
| Over-reliance | People accepting outputs without checking because the system is usually right |
| Model collapse | Degradation of models trained increasingly on machine-generated content |

## 4. How they are governed

| Term | Meaning |
| --- | --- |
| Responsible AI, trustworthy AI | The principles and practices by which an organization remains answerable for its use of AI; see What responsible AI means |
| Risk Tier | The Bank's classification of a use of AI by what it affects, whom it can harm, its autonomy, and its data, which sets the controls that apply; the term of the AI Policy |
| Risk-based approach | Controls proportionate to risk; the principle of the [EU AI Act](../reference/regulations/eu-ai-act.md), the [NIST framework](../reference/regulations/nist-ai-rmf.md), and the Bank's Risk Tiers |
| High-risk AI | In the [EU AI Act](../reference/regulations/eu-ai-act.md), the uses it lists, among them credit scoring of natural persons, which carry the full set of duties |
| AI Registry | The Bank's record of each Solution, model, and agent, with owner, scope, data access, and Risk Tier; the term of the Statement of Intent |
| Model risk management | The discipline of validating, documenting, and monitoring models, with a named owner; the banking practice that AI governance extends |
| Validation, independent validation | The judgment of a model or a Solution by a person who did not build it, before use and periodically |
| Explainability | The ability to state why a system produced an output in terms the person affected, the regulator, or the auditor can act on |
| Transparency | Telling people that they interact with AI and how it is used |
| Impact assessment | An assessment, before a higher-risk use, of its effect on the people concerned and the rights at stake |
| Model card, system card | A standard document that states what a model or a system is, what it is for, how it was tested, and where it should not be used |
| AI literacy | The understanding of what AI does and does not do that everyone who uses it should have; a duty under the [EU AI Act](../reference/regulations/eu-ai-act.md) and a training requirement of the Bank |
| Open banking | The sharing of account data and payment initiation with licensed third parties through interfaces, with the customer's consent |
| Embedded finance | Financial services offered inside a non-financial product or application, through a partner bank |
| Regtech | Technology, including AI, applied to compliance work: screening, monitoring, reporting, regulatory change |
| Alternative data | Data other than a credit history used to assess a customer: transactions, mobile and behavioral data, with the fairness and consent duties that follow |
| Liveness check | The test that the person presenting an identity document is present and alive, not a photo or a recording |
| Real-time scoring | A model's decision within the time of the transaction or the interaction, as in fraud and payments |
