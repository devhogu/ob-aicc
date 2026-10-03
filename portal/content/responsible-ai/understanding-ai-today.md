# Understanding AI today

Artificial intelligence is not one thing. It is a family of techniques that let a computer do work that used to need human judgment: recognizing, predicting, ranking, generating, and now acting. The techniques differ in how they are built, in what they are good at, and in how they fail, and the difference matters for anyone who decides whether and where to use them. This page explains the family in plain terms, with banking examples, as the first step of a short course on the subject.

## 1. From rules to learning

1.1. The first generation of automation was rules: a person writes the logic, and the computer applies it the same way every time. A rule is exact, explainable, and brittle: it does only what it was told, and it breaks when the world changes. Most of the systems of a bank are still rules, and rightly so.

1.2. Machine learning changed the direction. Instead of writing the rule, a person gives the computer examples, and the computer finds the pattern that fits them. A credit scorecard learned from past loans, a fraud model learned from past transactions, a forecast learned from past sales: each is a model, and each predicts a number or a class from the data it is given. A model is only as good as its examples, it carries the biases of its examples, and it degrades as the world drifts away from them. This is why banks built model risk management: independent validation, documentation, monitoring, and a named owner for every model.

1.3. Machine learning of this kind is specific: one model, one task, trained on the data of that task. It is powerful where the task is well defined and the data is plentiful, and it is the backbone of credit, fraud, pricing, and collections in banks today.

## 2. Generative AI

2.1. Generative AI is the step that changed the public conversation. Large language models are trained on very large bodies of text, and later images, audio, and code, to do one thing: predict what comes next. Done at scale, that one ability produces systems that write, summarize, translate, answer questions, draft code, and hold a conversation in natural language, without being built for any one of those tasks. The same model serves the lawyer, the accountant, the engineer, and the customer service agent.

2.2. Three properties follow from how these models work, and they explain both the opportunity and the risk. First, the model is general: it is not trained on the task of the function, so it must be given the context, the documents, the rules, and the examples of that task at the moment of use. Second, the model is probabilistic: it produces the most plausible continuation, which is usually right and sometimes confidently wrong; the industry calls the wrong case a hallucination or a confabulation. Third, the model does not know what it does not know: it has no built-in sense of its own confidence, of the date, or of the boundary between an instruction and a piece of data.

2.3. The practical consequence is that generative AI is used well as an assistant on governed material, with a person who decides, and used badly as an oracle. The techniques that make it reliable are known and are the daily work of AICC: retrieval over approved sources with citations, so that the model answers from the documents of the Bank and not from its memory; prompting and instructions that bound the task; evaluation sets that measure how often it is right on the cases of the function; and human validation sized to the risk.

## 3. Agents

3.1. The newest step gives the model tools: it can read a system, call a service, fill a form, run a script, and chain those actions toward a goal. An AI system that plans and acts in this way is called an agent. An agent can take a customer request from intake to a drafted resolution, assemble a report from several sources, or run a test suite and fix what fails. It is where the largest productivity gains are expected and where the risks compound, because an error is no longer a wrong sentence but a wrong action.

3.2. The industry's answer is bounded autonomy: an agent acts within limits and permissions set by the risk of the task, on channels it cannot influence, with a person able to stop it, and with every action logged and reversible where it can be. The Bank's Maturity Roadmap places agents at its fifth level for this reason: they stand on the governance, the knowledge, and the platform built at the levels before.

## 4. What is the same and what is new

| | Rules | Machine learning | Generative AI | Agents |
| --- | --- | --- | --- | --- |
| How it is built | A person writes the logic | Learned from examples of one task | Trained on vast general data, adapted at use | A generative model with tools and a goal |
| What it is good at | Exact, repeatable decisions | Prediction and classification on plentiful data | Language, knowledge, drafting, code, conversation | Multi-step work across systems |
| How it fails | Does not handle the unforeseen | Bias, drift, overfitting | Confabulation, injection, leakage, over-reliance | Wrong actions, cascading errors, excessive agency |
| Who is accountable | The owner of the rule | The model owner, under validation | The owner of the use, under a Risk Tier | The owner of the use, under tighter limits |
| Banking examples | Payment limits, eligibility checks | Scorecards, fraud models, forecasts | Knowledge assistants, document drafting, case summaries | Case resolution, report assembly, operations runbooks |
| Fintech examples | Transaction limits and velocity rules | Real-time fraud scoring, thin-file credit scoring, liveness and document checks | Chat-first service, onboarding assistance, dispute drafting | End-to-end case resolution under limited authority, reconciliation of partner interfaces |

4.1. What is the same across the family: accountability stays with a named person, the quality of the data decides the quality of the result, and a model is validated by someone other than its builder. What is new with generative AI and agents: the general model that must be given its context, the probabilistic output that must be checked, the natural-language interface that opens new attacks, and the autonomy that must be bounded.

## 5. Where the Bank stands

5.1. The Bank uses all four. Its rules run its systems; its models run its credit and fraud decisions under model risk management; generative AI enters through assistants on governed knowledge and through the automation of routine work; agents come later, within limits. The Statement of Intent sets the direction, the AI Policy sets the rules of use, and the pages that follow explain the opportunities, the fintech context, the risks, and what responsible use means.
