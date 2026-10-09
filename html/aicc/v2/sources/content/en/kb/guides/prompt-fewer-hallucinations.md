---
title: "How to reduce made-up answers"
summary: Seven techniques that noticeably reduce the model's confident errors — from allowing it to say “I don't know” to checking against quotes and running the prompt twice.
category: Prompting Claude
level: basic
minutes: 5
order: 27
tags: prompt, hallucinations, made-up answers, checking, accuracy
source: Лучшие практики составления подсказок
source_en: Prompting best practices
source_url: https://platform.claude.com/docs/ru/build-with-claude/prompt-engineering/claude-prompting-best-practices
source_hash: 38ad4c88c7be
---

A model always tries to answer, even when it doesn't know the answer. That's how a [[hallucination|hallucination]] happens: a smooth, confident, but made-up fact, figure, or reference. You can't rule it out completely, but you can greatly reduce it. After this guide you'll be able to add techniques to your prompt that make the answer verifiable and honest where the data runs short.

## Seven techniques {#tips}

<ol class="rai-principles">
<li><b>Allow it to say “I don't know”</b><span>“If the documents don't contain the answer, say so — ‘not enough data’ — and don't fill in the gaps.”</span></li>
<li><b>Limit the sources</b><span>“Answer only from the attached documents” rather than “from your own knowledge.”</span></li>
<li><b>Quotes first</b><span>“Copy out word for word the passages that relate to the question; if there are none, write ‘no relevant quotes’. Answer only from the quotes you copied out.”</span></li>
<li><b>A source and confidence level for each conclusion</b><span>“After each conclusion, say which document and section it comes from and how confident you are.”</span></li>
<li><b>Self-check</b><span>“Reread your answer: which statements aren't backed by quotes? Remove them or flag them.”</span></li>
<li><b>Fresh facts through search</b><span>Fees, requirements, rates, and rules change. If web search is turned on in your work account: “Use search to check anything that might have changed, even if you're sure.” If search is turned off, provide the current documents yourself.</span></li>
<li><b>Two runs</b><span>Ask the same prompt twice in new conversations. Where the answers differ, something is probably made up.</span></li>
</ol>

You don't need all seven at once. Start with the first three: they're easy to add to any question about a document.

## Try it now {#try}

Take a document that may be shared with your work account — for example, a new internal policy or regulation. Paste it in and ask a question whose answer you know:

```
<document>
…text of the policy…
</document>

Answer the question: from what date does the new procedure apply, and who does it affect?
Answer only from the document above.
First, copy out the word-for-word quotes you're relying on.
If the document doesn't contain the answer, write “the document doesn't say” and don't fill in the gaps.
```

Then ask a question whose answer is definitely not in the document. A good answer is “the document doesn't say”, not a plausible invention. Find the quotes from the first answer in the document itself.

## What you still need to check yourself {#you}

These techniques reduce errors but don't replace checking. Always check figures, dates, names, clause numbers, and references against the source — especially if the result is going to a customer, a manager, or a regulator. For more, see the guide [How to check AI output](page:kb/guides/checking-results).
