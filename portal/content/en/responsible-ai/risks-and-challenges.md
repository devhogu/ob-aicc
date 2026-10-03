# The risks and challenges

Every capability of generative AI has a failure mode attached to it, and most of the failure modes are new to the people who have to manage them. This page sets them out in plain terms, in three groups: the risks that machine learning always carried, the risks that generative AI added, and the risks that agents compound. It ends with the challenges that are not about the technology at all, which are the ones that decide most outcomes.

## 1. The risks that were always there

1.1. **Bias.** A model learns from examples, and examples carry the past. A scorecard trained on past lending reproduces past exclusions; a hiring model trained on past hires reproduces past preferences. In a bank, a biased model is a fairness problem for customers, a legal problem under consumer protection and anti-discrimination rules, and a reputation problem. The answer is testing for bias before release and monitoring in use, in proportion to the risk.

1.2. **Drift and decay.** The world moves and the model does not. A fraud model trained before a new scheme does not see it; a forecast trained before a rate shock is wrong afterwards. Monitoring the performance of a model in use, with alert levels that trigger a review, is the standard answer, and the AI Registry is where the Bank records which models are watched and by whom.

1.3. **Data quality and lineage.** A model is only as good as its data, and a decision is only defensible if the data can be traced. Poor data produces confident nonsense; untraceable data produces an audit finding. Classification, ownership, and lineage of data are the foundation of the Maturity Roadmap for this reason.

1.4. **Model risk.** The combination of the above, which banks have managed for two decades under model risk management: independent validation, documentation, monitoring, and a named owner. The discipline carries over to AI unchanged in principle and extended in scope.

## 2. The risks that generative AI added

2.1. **Confabulation.** The model produces fluent, confident, and wrong output: a clause that does not exist, a figure that was never reported, a citation to a document that was never written. It is not a bug that will be fixed; it is a property of predicting the plausible continuation. It is contained by grounding the model in approved sources with citations, by evaluating it on the cases of the function, and by keeping a person who validates before anything takes effect. The [NIST generative AI profile](../reference/regulations/nist-ai-rmf.md) lists it first among the generative risks.

2.2. **Prompt injection.** The model reads instructions and data through the same channel and cannot reliably tell them apart. A document, an email, or a web page that the model processes can contain text that the model follows as an instruction: ignore your rules, reveal your prompt, send this data elsewhere. It is the first item on the [industry's list of security risks for language-model applications](../reference/regulations/owasp-top-10-llm.md), and it is why an assistant that reads untrusted content must have limited permissions, filtered inputs and outputs, and a person between its proposal and any action.

2.3. **Data leakage.** Data goes where it should not: into a provider's training set, into another user's answer, into a log. Confidential and personal data of the Bank must reach only the models and the services that its classification allows, under contracts that forbid training on it, with retention and residency known. The provider check of the AI Policy exists for this.

2.4. **Intellectual property and provenance.** Models are trained on material whose rights are contested, and they produce material whose origin is unclear. The Bank must know what it may use, what it may publish, and what it must label as machine-assisted, and it must keep the trail from a published statement back to its governed source.

2.5. **Over-reliance and deskilling.** When the assistant is usually right, people stop checking, and when they stop checking they stop learning. The remedy is design: the person reviews and decides, the assistant proposes; the roles and the training say so; and the measures watch the override rate as well as the throughput.

2.6. **Security of the supply chain.** Models, libraries, plug-ins, vector stores, and hosted services form a supply chain that the Bank does not control. Poisoned data, compromised components, and leaked system prompts are the new entries in the security catalog, and they are managed as any third-party risk is: assessment, contract, monitoring, exit.

2.7. **Cost and concentration.** The models are expensive to run and are supplied by few providers. Unbounded use produces unbounded bills; dependence on one provider produces a single point of failure. Cost limits, fallback arrangements, and exit plans are part of the design, not of the aftermath.

## 3. The risks that agents compound

3.1. An agent turns a wrong sentence into a wrong action. The industry names three root causes of harm: excessive functionality, when the agent can do more than its task needs; excessive permissions, when it can reach more than its task needs; and excessive autonomy, when it acts without the confirmation its risk requires. Errors cascade when one agent's output is another's input. The Bank's position follows from this: an agent acts within limits and permissions set by its Risk Tier, on channels it cannot influence, with a person able to stop it, with its actions logged, and it is not released to act on systems or funds in a regulated process without validation by the Control Functions and the decision of the Executive Sponsor.

## 4. The challenges that are not about the technology

4.1. **Shadow AI.** People use the tools they have, approved or not, and paste what they should not. The rule is plain: only approved Solutions are used, and no internal document or data of the Bank other than public data goes into an external service that is not an approved Solution (AI Policy 2.1, 2.6). A ban alone drives the use underground, so what makes the rule work is an approved assistant that is good enough, training on what may and may not be shared, and, for each unapproved use reported, an entry in the AI Registry with an approved Solution proposed or the use stopped (AI Policy 2.7).

4.2. **Ownership.** A use of AI without a named owner is a risk without a manager. Every Solution in the Bank has an owner, a Risk Tier, and an entry in the AI Registry, or it does not go live.

4.3. **Skills and change.** The constraint is people before it is technology. Training by role, Domain Experts in each function, and communities of practice are the slow work that makes the fast work possible.

4.4. **Measurement.** A pilot that cannot say whether it worked did not work. Every Initiative has leading indicators and success Measures before it starts, and the decision after the MVP is taken on them.

4.5. **Expectation.** The most common failure is the gap between what was promised and what was possible. The honest statement of what the technology does and does not do, which this course tries to give, is itself a control.

## 5. How the risks are read together

5.1. The frameworks of the field, among them the [NIST AI Risk Management Framework](../reference/regulations/nist-ai-rmf.md) with its generative profile, the [OWASP Top 10 for Large Language Model Applications](../reference/regulations/owasp-top-10-llm.md), and the risk-based regime of the [EU Artificial Intelligence Act](../reference/regulations/eu-ai-act.md), converge on the same reading: the risk of a use of AI depends on what it can affect, whom it can harm, how autonomous it is, and what data it touches, and the controls should be proportionate to that. The Bank's Risk Tiers are its version of this reading, set by the class of the data, the influence of the AI on a decision, whether the output reaches or affects a customer, and the degree of autonomy (AI Policy 3.1), and the page What responsible AI means explains the principles behind them.
