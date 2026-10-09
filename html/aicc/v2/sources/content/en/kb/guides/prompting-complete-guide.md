---
title: "How to write prompts for Claude: the complete guide"
summary: Everything about briefing Claude — clarity, context, examples, structure, long documents, format, thinking modes, accuracy, templates, and checking — based on Anthropic's current recommendations, with examples from our work.
category: Prompting Claude
level: deep
minutes: 35
order: 2
featured: true
layout: course
tags: prompt, prompting, prompt engineering, examples, xml, format, hallucinations, template
source: Лучшие практики составления подсказок — документация платформы Claude
source_en: Prompting best practices — Claude Platform documentation
source_url: https://platform.claude.com/docs/ru/build-with-claude/prompt-engineering/claude-prompting-best-practices
source_hash: 8e2178de698a
---

A good [[prompt|prompt]] isn't a magic formula but a well-defined task: the way you would explain it to a smart new employee. This guide brings together everything Anthropic currently recommends for its models and puts it in terms of our work — emails, reports, spreadsheets, contracts, and summaries.

**Who it's for and what it gives you.** For those who have already mastered individual techniques and want to write prompts for recurring and complex tasks. By the end, you will be able to build a complex prompt from a skeleton, save it as a template, and improve it by testing it on 5–10 of your own past examples.

The nine tabs go from simple to complex. Tabs 1–7 sum up the techniques from the short guides in this series, starting with [How to brief the assistant](page:kb/guides/writing-a-task). What's new is in tab 8, “Templates, chains, and improving a prompt”, and tab 9, “The skeleton of a complex prompt”: start with them if you have already been through the short guides.

Anthropic's documentation gives its examples in English; here they are adapted and supplemented with our own. You can also write prompts in Russian: Claude replies in the language you write in.

## The basics: clear, specific, and why {#clear}

Anthropic advises thinking of Claude as a **brilliant but new employee**: it can do a lot, but it doesn't know your norms, your habits, or what “goes without saying.”

### The colleague test {#golden}

Show your prompt to a colleague who knows nothing about the task and ask them to do it. If they get confused, so will Claude.

### Say directly what you need {#direct}

| Weaker | Stronger |
| --- | --- |
| “Write an email about the project delay” | “Write an email to our corporate client: the integration is delayed by two weeks because of a security review; the new deadline is 15 November. Calm tone, apologetic without overdoing it. Up to 150 words.” |
| “Do a sales analysis” | “Compare sales by product for September and August. I need the three biggest changes and their likely causes. A table and five lines of conclusions for my manager.” |

- Specify the **format and constraints**: length, structure, language.
- If order or completeness matters, give **the steps as a numbered list**.
- If you want more than the minimum — detailed, creative — **ask for it explicitly**: the model won't do more than you asked.

### Three things worth describing {#describe}

The AI Fluency course names three aspects of describing a task:

<div class="rai-cards rai-cards--3">
<article><h3>What to get</h3><p>The result, the format, the reader, the style: “a one-page internal memo for the chief financial officer.”</p></article>
<article><h3>How to approach it</h3><p>The order of work: “first copy out the figures from the report, then compare them with the plan, then draw conclusions.”</p></article>
<article><h3>How to behave</h3><p>The role of your counterpart: “be critical, look for weak spots”, “answer briefly”, “ask questions if anything is missing.”</p></article>
</div>

### Explain why {#why}

A reason works better than a prohibition: Claude understands the point and carries it over to similar cases on its own.

| Weaker | Stronger |
| --- | --- |
| “No abbreviations” | “This text will be read by a customer who doesn't know our internal terms, so write without abbreviations or acronyms.” |

A handy form from Anthropic's documentation:

```
I'm working on [the bigger task] for [whom].
They need [what the result will give them].
With that in mind: [the request].
```

## Examples: show, don't describe {#examples}

Examples are **one of the most reliable ways** to set the format, tone, and structure of an answer. A style is hard to describe in words and easy to show.

<div class="rai-cards rai-cards--3">
<article><h3>Relevant</h3><p>Close to the real task: the same kind of documents, the same reader, the same difficulty.</p></article>
<article><h3>Varied</h3><p>Different from one another, including edge cases — otherwise Claude picks up an accidental detail: the same length, the same opening.</p></article>
<article><h3>Set apart</h3><p>Clearly marked as examples so they aren't mistaken for instructions: “Example 1:” or &lt;example&gt; tags.</p></article>
</div>

- **How many:** **three to five** examples work best.
- **A positive example beats a prohibition.** Showing how to do it works better than listing how not to.
- **Ask for help:** Claude can assess whether your examples are varied enough, or come up with a few more along the same lines.

```
Reply to the customer in the same style as in the examples.

<examples>
<example>
Question: Can I close my card in the app?
Answer: Yes. Open the card → “Settings” → “Close card”. We'll transfer the remaining balance to your account.
</example>
<example>
Question: Why didn't my payment go through?
Answer: Most often it's because of the card limit. Check it under “Card” → “Limits”. If you haven't reached the limit, write to us and we'll sort it out.
</example>
</examples>

Customer question: {question}
```

The simplest source of examples is your own good work: two or three emails, summaries, or replies that turned out well.

## Structure: role, data, instructions {#structure}

When instructions, documents, examples, and the question are mixed together in a prompt, the model may take part of a document for an instruction. Two habits help.

### Role {#role}

One sentence at the start focuses the tone and knowledge: “You are a credit risk analyst. Explain things briefly and without jargon.” It also helps to name the audience: “…for branch staff who aren't familiar with the methodology.” Current models usually don't need long role “backstories”: one or two sentences are enough.

### Labeled boxes for data {#tags}

Wrap each part of the prompt in a clear tag — XML tags, that is, words in angle brackets. It's like labeling boxes when you move.

```
<instructions>
Compare the two contracts and list the differences in payment terms.
Answer as a table: clause, contract A, contract B, why it matters for us.
</instructions>

<documents>
  <document index="1">
    <source>Contract A, 2026 edition</source>
    <document_content>…text…</document_content>
  </document>
  <document index="2">
    <source>Contract B</source>
    <document_content>…text…</document_content>
  </document>
</documents>
```

- Tag names should be clear and the same from prompt to prompt.
- Nest tags when the parts are naturally nested.
- Refer to the tags in your instructions: “based on document 1.”

Tags aren't required syntax: a simple request doesn't need them. They help when a prompt has many parts.

### It's also about security {#safety}

If a document came from outside — an email, a web page, a customer's file — it may contain text that looks like a command. An explicit boundary between “here is my request” and “here is the pasted document” reduces the risk of [[prompt-injection|prompt injection]].

## Long documents {#long}

Claude reads very long texts: an annual report, a set of contracts, a dozen internal procedures. Three techniques from Anthropic's documentation make the answer more accurate.

<ol class="rai-flow">
<li><b>Documents at the top</b><span>all the materials first, with the question and instructions at the very end</span></li>
<li><b>Each with a tag</b><span>with a title and a source, as in the example above</span></li>
<li><b>Quotes first</b><span>then an answer based only on them</span></li>
</ol>

- **The question at the end:** in Anthropic's tests this improves answer quality by up to **30%**, especially when there are several documents.
- **Quotes first:** “First, copy out word for word the passages that relate to the question. Then answer based only on them.” Claude focuses on what matters, and you check the answer against the quotes — this is what [[grounding|grounding]] means.
- **Give files meaningful names:** Claude will understand “Report_Q3_2026.pdf” better than “document1.pdf”.

## Format, length, and the scope of the task {#format}

### Say what to do, not what not to do {#positive}

| Weaker | Stronger |
| --- | --- |
| “Don't use lists” | “Write in flowing prose, in paragraphs” |
| “Don't make it long” | “No more than five sentences” |
| “No introductions” | “Get straight to the point; the first sentence is the conclusion” |

### The style of the prompt sets the style of the answer {#match}

If the prompt is all bullets and highlighting, the answer will most likely be the same. If you want calm business prose, write the prompt that way.

### Length {#length}

Current Claude models answer fairly briefly and may skip a closing summary. If you need a detailed analysis, ask for it. If you need something very short, set a limit: “up to 100 words.” A good rule from the documentation: **the result first**, then the details; and **clarity matters more than brevity** — shorten by choosing what to include, not by writing like a telegram.

### Action or advice: the verb decides {#verb}

“Can you suggest how to improve this email?” gets you advice. “Rewrite this email” gets you a new email. Choose the verb that matches what you need.

### The scope of the task {#scope}

- Current models follow instructions **literally**. If you want a rule to apply to the whole document, say so: “apply this to all sections, not just the first one.”
- If you want only ideas, say so: “give me options and stop”; otherwise Claude may start doing the work right away.
- Don't write “MUST” and “CRITICALLY IMPORTANT” in capitals: new models already pay close attention to instructions, and pressure leads to overcorrection.

### If the format has to be strict {#strict}

For recurring tasks, give an answer template with tags or fields — for example, “for each competitor: strengths, weaknesses, our response in 30 words.” A template plus an example is the most reliable way to get the same kind of result every time.

## Thinking and modes of work {#thinking}

Current Claude models **decide for themselves when and how much to think**. On the newest models thinking is always on, and the effort level sets how deep it goes.

### The effort level in the app {#effort}

| Level | When |
| --- | --- |
| Low, Medium | routine work: translating, rephrasing, short answers; saves your usage limit |
| High | the best balance for most tasks |
| Xhigh, Max | complex calculations, in-depth document analysis, multi-step planning |

The effort level controls how deeply the model thinks before answering. You choose the model and the level next to the send button; which ones are available to you depends on your plan and your organization's settings. Raise the level for calculations, detailed document analysis, and complex planning — this is more reliable than coaxing the model to “think harder” in the text of the prompt.

### How to ask it to think {#how-think}

- A short general instruction — “think carefully before you answer” — usually works better than a step-by-step reasoning plan.
- **Don't ask for the reasoning to be written out** in a separate block: on new models such a request may be declined, and the thinking happens anyway.
- **Self-check:** “Before you finish, check your answer against these criteria: …” is a useful last line for a prompt.

### Search, thinking, or research {#modes}

<div class="rai-cards rai-cards--3">
<article><h3>Web search</h3><p>A simple factual question where freshness matters: an exchange rate, a news item, a current rule.</p></article>
<article><h3>Thinking</h3><p>Complex reasoning that doesn't need fresh data: a calculation, a review of a contract, the logic of a decision.</p></article>
<article><h3>Research</h3><p>A report drawing on five or more sources: a market overview, a comparison of regulators' approaches.</p></article>
</div>

If your organization has turned search off, work with the documents you provide yourself.

## Accuracy: fewer made-up answers {#accuracy}

A model always tries to answer, even when it doesn't know the answer. That's how a [[hallucination|hallucination]] happens. You can't rule it out completely, but you can greatly reduce it.

<ol class="rai-principles">
<li><b>Allow it to say “I don't know”</b><span>“If the report doesn't have enough data for a conclusion, say so — ‘not enough data’ — and don't fill in the gaps.”</span></li>
<li><b>Limit the sources</b><span>“Answer only from the attached documents, not from general knowledge.”</span></li>
<li><b>Quotes first</b><span>“Copy out the passages word for word; if there are none, write ‘no relevant quotes’. Base the analysis only on the quotes you copied out.”</span></li>
<li><b>Check against the sources</b><span>“For each statement, find a supporting quote. If you can't find one, remove the statement and mark the spot.”</span></li>
<li><b>Confidence and source</b><span>“For each conclusion, give the source and say how confident you are.”</span></li>
<li><b>Fresh facts through search</b><span>Fees, requirements, rates, and rules change. If search is turned on: “Use search to check anything that might have changed — what's allowed, what's required, what it costs — even if you're sure.”</span></li>
<li><b>Two runs</b><span>Ask the same prompt twice in new conversations. Where the answers differ, something is probably made up.</span></li>
</ol>

These techniques reduce errors but don't replace checking: check for yourself any figures, dates, names, and references that will go to a customer, a manager, or a regulator. For details, see [How to check AI output](page:kb/guides/checking-results).

### Careful quoting {#quoting}

In summaries the model sometimes carries phrases over from the source without quotation marks. If it matters to tell a quote from a paraphrase (for example, in materials for compliance), say so directly and show an example of the correct formatting.

## Templates, chains, and improving a prompt {#iterate}

### A template with variables {#template}

A template is a saved prompt for a task that comes up every week or month. It has a **fixed part** — the role, the rules, the format — and **variables**: what changes each time, such as the document, the period, or the topic. Save the fixed part and fill in the variables each time inside tags, so it's clear where they start and end. In the example below the variables are in curly braces.

```
You are preparing a brief summary for a manager.
<report>{REPORT TEXT}</report>
<period>{PERIOD}</period>
Write the summary using this template: the three main changes, the risks, what to propose.
```

Another example is a weekly summary of customer requests: “You are a contact center analyst. Here is an anonymized export of the week's customer requests in &lt;data&gt;. Group them by topic, show the five most frequent, and compare with the previous week in &lt;previous&gt;. If a topic can't be determined, put the request under ‘Other’ and don't guess.”

It's convenient to save such a template in a [project](page:kb/guides/claude-projects) or turn it into a [skill](page:kb/guides/skills-complete-guide).

### A chain: draft → review → revise {#chain}

A big task is better split into steps, where each one is a separate prompt with one goal. The main pattern from the documentation is self-correction:

<ol class="rai-flow">
<li><b>Draft</b><span>“write a summary from the data”</span></li>
<li><b>Review</b><span>“here is the summary and the source data: find errors and unsupported statements”</span></li>
<li><b>Revise</b><span>“fix the summary based on the comments”</span></li>
</ol>

A tip for reviews: ask it to find **everything**, and pick out what matters in a separate step. If you ask for “only serious problems” right away, the model will take you literally, report less, and may miss something you need.

### How to improve a prompt {#improve}

1. **Define what “good” means** — specifically and verifiably: “a five-column table, every figure with a source”, not “a quality summary.”
2. **Collect 5–10 examples** of your past work on this task.
3. **Run the prompt** on these examples and compare the results with how you would have done it.
4. **Refine** the prompt based on the differences you find. Start simple and add techniques only when needed.
5. **Ask Claude for help:** “Here is my prompt and what I got. How can I improve the prompt so the result looks like this: …” — a simple and powerful technique.

Your first prompt is the start of a conversation, not a final request: refining as you go is normal.

### Try it now: a template for your own task {#try}

1. Choose a task you do every week: a summary, a report, meeting minutes, checking documents against a checklist.
2. Write a prompt following the skeleton in tab 9 and mark the variables in curly braces.
3. Take 5–10 past cases of this task — without personal data — and run the template on them.
4. Compare the results with what you did at the time, note the differences, and adjust the template.

## The skeleton of a complex prompt {#skeleton}

For a serious task — an analysis, a report, a recurring process — it helps to follow the skeleton from Anthropic's tutorial.

<ol class="rai-principles">
<li><b>Role and context</b><span>Who you are and what this work is for.</span></li>
<li><b>Tone</b><span>How to speak to the reader.</span></li>
<li><b>Task and rules</b><span>What to do, what matters, what to do if there's no answer.</span></li>
<li><b>Examples</b><span>One to five samples of a good result.</span></li>
<li><b>Data</b><span>Documents and input information, in tags.</span></li>
<li><b>The request itself</b><span>Near the end, after the data.</span></li>
<li><b>Answer format</b><span>Structure, length, order.</span></li>
</ol>

First get a good result with the full skeleton, then remove what isn't needed.

### A complete example {#full-example}

```
You are a financial analyst preparing material for the Management Board.
Write in business language, without jargon: the readers are not finance specialists.

Task: prepare a one-page summary based on the quarterly report.
If there isn't enough data for a conclusion, say so and don't fill in the gaps.
Take figures only from the report; for each one, give the section it comes from.

<example>
Revenue grew by 12% (section 2.1) thanks to retail lending…
</example>

<report>
{QUARTERLY REPORT TEXT}
</report>

Write the summary: 1) the three main changes in the quarter; 2) two risks;
3) what to propose to the Board. Each point is 2–3 sentences.
Before you finish, check that every figure has a section reference.
```

### Where to learn more {#learn}

- Anthropic's interactive prompting tutorial: nine chapters with exercises, from the structure of a prompt to complex tasks; it includes an exercise for financial services. The tutorial was written for earlier models: where the two differ, follow this guide.
- The Claude 101 and AI Fluency courses: the lessons “Getting better results” and “Effective prompting techniques”.
- All the links are in the Reference section: [Anthropic learning](page:reference/anthropic).
