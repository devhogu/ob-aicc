---
title: "Let it think: thinking and effort level"
summary: Current Claude models decide for themselves when and how much to think. How to help them on complex tasks, when to raise the effort level, and what you no longer need to do.
category: Prompting Claude
level: basic
minutes: 4
order: 26
tags: prompt, reasoning, thinking, effort level, analysis
source: Лучшие практики составления подсказок
source_en: Prompting best practices
source_url: https://platform.claude.com/docs/ru/build-with-claude/prompt-engineering/claude-prompting-best-practices
source_hash: 502a57ea7e39
---

Someone who blurts out an answer to a hard question gets it wrong more often than someone who thinks first. It's the same with a model. This guide is about letting Claude think where it's needed: afterwards you'll be able to choose the effort level for a task and briefly ask for careful work.

Current Claude models **decide for themselves when and how much to think** before answering, and on the newest models thinking is always on. Your job is to signal how complex the task is.

## How to help on a complex task {#how}

- **Raise the effort level.** The effort level is a setting that controls how deeply the model thinks before answering. In the app you choose it next to the send button: High for most tasks, Xhigh and Max for calculations, in-depth document analysis, and multi-step planning. This is more reliable than any coaxing in the text of the prompt.
- **A short instruction beats a plan.** “Think carefully before you answer” usually works better than reasoning steps you spell out yourself.
- **If the order of work matters**, describe it as a process: “first copy out the contract terms, then compare them with the regulation, then draw a conclusion.”
- **A self-check at the end:** “Before you finish, check your answer against these criteria: all the amounts add up, and every conclusion cites a clause of the document.”

Which models and levels you have depends on your plan and your organization's settings. If your work account doesn't have this menu, use the techniques in the other points.

## What not to do anymore {#avoid}

- Don't ask for the reasoning to be written out in a separate block: on new models such a request may be declined, and the thinking happens anyway.
- Don't write “think step by step” for simple tasks — translating, shortening, rephrasing: it only slows the answer down and uses up your usage limit.

## When you need it {#when}

<div class="rai-cards rai-cards--3">
<article><h3>Raise the effort</h3><p>Calculations, comparing several documents, “if — then” conditions, finding errors, analyzing causes. For example: reconcile a report with an export and explain the discrepancies.</p></article>
<article><h3>Lower is fine</h3><p>Translating, shortening, rephrasing, simple reference questions. For example: shorten an email to five points.</p></article>
<article><h3>Bonus</h3><p>You can see how Claude reached its conclusion — an error in the reasoning is easier to find than one in a finished answer.</p></article>
</div>

## Try it now {#try}

Take a task with a calculation or a comparison — for example, checking an internal memo against a six-point checklist. Send the same prompt at the normal and at a raised effort level, with the line “Before you finish, check your answer against each point of the checklist.” Compare which answer is more accurate.

For more, see the “Thinking and modes of work” tab of the [complete guide to prompting](page:kb/guides/prompting-complete-guide#thinking).
