---
title: Responsible AI
summary: A short course in six parts: the kinds of AI, what AI offers, where it helps in financial services, how it goes wrong, what using it responsibly means, and how we do it.
order: 0
layout: course
related: responsible-ai/how-we-apply-it, responsible-ai/ai-terms-explained, hub/values, process/profiles
source_hash: d5d74b5baab2
---

<p class="lede">AI already works in financial services: in scoring, in fraud detection, in assistants for staff. It speeds work up, but it makes its own kind of mistakes, and in finance a model's mistake means an honest customer turned down, fraud missed, or data sent where it shouldn't go. That's why, after asking “What does AI give us?”, we always ask a second question: “How will we answer for its results?”</p>

[[responsible-ai|Responsible AI]] is a simple idea: whoever uses AI is responsible for what the AI does and organizes the work so that they can stand behind the result. You can read the six short parts below in order or jump to any of them.

## AI today {#today}

Artificial intelligence isn't one technology but a family of methods. They work differently, are good at different things, and go wrong in different ways.

<div class="rai-kinds">
<article><small>1</small><h3>Rules</h3><p class="rai-how">A developer writes down the logic</p><dl><dt>Good at</dt><dd>Precise, repeatable decisions</dd><dt>Typical failures</dt><dd>Can't cope with the unexpected</dd><dt>Example</dt><dd>Payment limits</dd></dl></article>
<article><small>2</small><h3>Machine learning</h3><p class="rai-how">A model learns from examples of one task</p><dl><dt>Good at</dt><dd>Prediction and classification when there is plenty of data</dd><dt>Typical failures</dt><dd>Bias, drift</dd><dt>Example</dt><dd>Scoring, fraud detection</dd></dl></article>
<article><small>3</small><h3>Generative AI</h3><p class="rai-how">A general-purpose model that is given the context of a task</p><dl><dt>Good at</dt><dd>Language, knowledge, texts, code, dialogue</dd><dt>Typical failures</dt><dd>Confident mistakes, attacks through text, leaks</dd><dt>Example</dt><dd>A knowledge base assistant</dd></dl></article>
<article><small>4</small><h3>AI agents</h3><p class="rai-how">A model with tools that works out the steps itself</p><dl><dt>Good at</dt><dd>Multi-step work across several systems</dd><dt>Typical failures</dt><dd>Wrong actions, cascading errors</dd><dt>Example</dt><dd>Handling requests, preparing reports</dd></dl></article>
</div>

What all four have in common: a specific person is responsible for how it's used, the data sets the quality of the result, and the model is checked by someone other than its creator. What's new with generative AI and agents: the model has to be given context, its output has to be checked, language opens the door to new attacks, and its autonomy has to be limited.

The practical conclusion: generative AI is good as an assistant that works with verified material while a person makes the decision, and poor as an infallible source of answers.

## What AI offers {#value}

Three capabilities have become available and cheap at the same time.

<div class="rai-cards rai-cards--3">
<article><h3>Language</h3><p>Reading, writing, summarizing, and translating in working languages, well enough for real work.</p></article>
<article><h3>Knowledge</h3><p>Answering questions from a body of documents, citing the source.</p></article>
<article><h3>Code</h3><p>Writing, explaining, testing, and fixing programs.</p></article>
</div>

Earlier automation replaced a whole task and needed long projects. AI helps where automating never paid off: in the thousand small acts of reading, cross-checking, and preparing texts that make up a working day.

<ol class="rai-flow">
<li><b>AI prepares</b><span>a draft, a summary, a selection of material, an option for a decision</span></li>
<li><b>A person decides</b><span>checks, approves, signs</span></li>
<li><b>Routine goes away</b><span>time goes to judgment and talking to people, not to collecting and retyping</span></li>
</ol>

Value more often comes from many small uses across all departments, on a shared platform and with trained people, than from a few big bets. The place to start is where the benefit is higher and the risk lower: assistants built on verified knowledge, then automating routine work with a person checking it.

## AI in finance {#finance}

Where AI already helps, and what exactly it does.

<div class="rai-cards rai-cards--3 rai-cards--areas">
<article><h3>Customer service</h3><p>Gives the employee hints during a conversation, prepares summaries and draft replies, answers in chat from the knowledge base.</p></article>
<article><h3>Customer onboarding</h3><p>Reads documents, checks that a live person is in front of the camera, and hands unusual cases to an employee.</p></article>
<article><h3>Fraud prevention</h3><p>Scores transactions in real time, spots patterns across accounts and devices, and prepares material for investigations.</p></article>
<article><h3>Lending</h3><p>Assesses customers with no credit history using [[alternative-data|alternative data]], suggests limits, and monitors repayment.</p></article>
<article><h3>Operations</h3><p>Extracts data from documents and works through reconciliation breaks, payment exceptions, disputes, and refunds.</p></article>
<article><h3>Compliance</h3><p>Gathers material for investigations, screens against sanctions lists, and works through false positives.</p></article>
<article><h3>Finance and reporting</h3><p>Prepares draft reports from reconciled data and commentary on variances, with the source of every figure cited.</p></article>
<article><h3>Knowledge</h3><p>Turns rules, procedures, and product terms into a knowledge base for answering questions with references.</p></article>
<article><h3>Technology</h3><p>Helps write and review code, creates tests, explains legacy code, and analyzes incidents.</p></article>
</div>

Customers come mainly through mobile channels and speak Kyrgyz and Russian. That makes assistants for staff, and a knowledge base used to answer customers, especially useful. Credit decisions involving AI, and agents that talk to customers or carry out transactions, come later, once the data, the platform, and the people are ready for them.

## How AI goes wrong {#risks}

Risks build up in layers: the old ones haven't gone away, generative AI has added new ones, and agents amplify the consequences. And some difficulties aren't about technology at all.

<div class="rai-risks">
<section><h3>Always there</h3><ul>
<li><b>[[bias|Bias]]</b><span>The model repeats the past: old refusals, old preferences.</span><em>Testing before launch, watching results by group</em></li>
<li><b>[[model-drift|Drift]]</b><span>The world changes but the model doesn't: it can't see a new fraud scheme.</span><em>Quality monitoring, a threshold written down in advance</em></li>
<li><b>Bad data</b><span>Bad data produces confident nonsense.</span><em>A clear source and data class</em></li>
</ul></section>
<section><h3>Added by generative AI</h3><ul>
<li><b>[[hallucination|Hallucination]]</b><span>A smooth, confident, and wrong answer.</span><em>Answers from sources with references, human review</em></li>
<li><b>[[prompt-injection|Prompt injection]]</b><span>Text in an email or document that the model carries out as a command.</span><em>Narrow permissions, filters, a person before any action</em></li>
<li><b>[[data-leakage|Data leakage]]</b><span>Data ends up with the vendor, another user, or in a log.</span><em>Services matched to the data class, a contract that rules out training on our data</em></li>
<li><b>[[overreliance|Over-reliance]]</b><span>People stop double-checking the assistant and lose the skill.</span><em>AI suggests, a person decides</em></li>
</ul></section>
<section><h3>Amplified by AI agents</h3><ul>
<li><b>[[excessive-agency|Excessive agency]]</b><span>A mistake becomes an action, not just a sentence.</span><em>Only the permissions needed, every step logged, the ability to stop and undo</em></li>
<li><b>Vendors and costs</b><span>A chain of services outside our control, bills without limits.</span><em>Cost limits, a fallback option</em></li>
</ul></section>
<section><h3>Not about technology</h3><ul>
<li><b>[[shadow-ai|Shadow AI]]</b><span>Work data goes out to external services.</span><em>A good internal assistant and clear rules</em></li>
<li><b>No one is responsible</b><span>A use with no owner is a risk that no one manages.</span><em>Every solution has a [[business-owner|business owner]]</em></li>
<li><b>No way to measure</b><span>A pilot no one can call a success or a failure.</span><em>Success measures are written down before the start</em></li>
<li><b>Inflated expectations</b><span>A gap between what was promised and what's possible.</span><em>Be honest about what AI can and can't do</em></li>
</ul></section>
</div>

The risk of a use depends on what it affects, whom it could harm, how independently it acts, and what data it works with. Safeguards are scaled to match, which is why every solution has a [[risk-tier|risk tier]].

## Principles {#principles}

International principles and regulators' requirements, including the [Kyrgyz Republic's requirements for AI systems](page:reference/regulation), come together in seven points. They are also our [principles of use](page:hub/values).

<ol class="rai-principles">
<li><b>Accountability</b><span>A specific person, the business owner, is responsible for every solution that uses AI. Bought-in AI is treated the same as our own.</span></li>
<li><b>Fairness</b><span>AI doesn't discriminate against customers or employees; it is tested before release and monitored in use.</span></li>
<li><b>Transparency and [[explainability|explainability]]</b><span>People know they are dealing with AI, and the result can be explained.</span></li>
<li><b>Data protection</b><span>AI gets only the data it needs and stores it as the rules require.</span></li>
<li><b>Security and reliability</b><span>AI is tested and protected against typical attacks; important services have a fallback option.</span></li>
<li><b>A person decides</b><span>A person can stop the AI or undo its action; a customer can ask for a decision to be reviewed.</span></li>
<li><b>Proportionate checks</b><span>How deep the checks go depends on the risk tier; they can't be skipped.</span></li>
</ol>

Four common misconceptions:

<div class="rai-cards rai-cards--4 rai-myths">
<article><h3>“It slows us down”</h3><p>The opposite: teams that know the risk tier and what to check from the start move faster and don't grind to a halt after the first incident.</p></article>
<article><h3>“It's about the model”</h3><p>More often, harm comes from how the model is used, on what data, and who works with it.</p></article>
<article><h3>“Approved, so we're done”</h3><p>A solution stays under watch for as long as it runs: both the world and the model change.</p></article>
<article><h3>“It's someone else's job”</h3><p>The solution's owner is responsible; someone who didn't build it checks it; every user knows the rules.</p></article>
</div>

## How we apply it {#apply}

Every project goes through the same four steps, each as deep as its risk tier calls for.

<ol class="rai-flow rai-flow--4">
<li><b>Risk tier</b><span>set at the start: what the solution affects and whom it could harm</span></li>
<li><b>Human in the loop</b><span>decide where a person checks the AI's output and where they can stop it</span></li>
<li><b>Checks along the path</b><span>at checkpoints, not by a single committee at the end</span></li>
<li><b>Monitoring</b><span>of quality in use; in an incident, stop, analyze, fix</span></li>
</ol>

For details, see [How we apply it](page:responsible-ai/how-we-apply-it); for unfamiliar words, see [AI terms in plain words](page:responsible-ai/ai-terms-explained).
