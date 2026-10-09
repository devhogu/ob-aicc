---
title: "A big task as a chain of prompts"
summary: Why complex work is better split into several steps, each with its own prompt, how to pass the result from step to step, and how the “draft — review — revise” chain works.
category: Prompting Claude
level: advanced
minutes: 5
order: 28
tags: prompt, chain, steps, self-check, complex tasks
source: Лучшие практики составления подсказок
source_en: Prompting best practices
source_url: https://platform.claude.com/docs/ru/build-with-claude/prompt-engineering/claude-prompting-best-practices
source_hash: 044fb81a6a0d
---

One huge prompt — “read, analyze, write a report, and check it” — often gives a mediocre result: the model spreads itself too thin. It's better to split the work into steps, where each step is a separate prompt with one goal. Such a sequence is called a prompt chain. By the end, you will be able to split your big task into a chain and check the result at each step.

## The main chain: draft — review — revise {#draft}

It works for almost any text: a summary, an internal memo, a reply to a complaint.

<ol class="rai-flow">
<li><b>Draft</b><span>“Write a summary from the data below”</span></li>
<li><b>Review</b><span>“Here is the summary and the source data: find errors and unsupported statements”</span></li>
<li><b>Revise</b><span>“Fix the summary based on the comments”</span></li>
</ol>

At the review step, ask it to find **everything**, and pick out what matters separately. If you ask for “only serious problems” right away, the model will take you literally, report less, and may miss something you need.

## A chain for analyzing documents {#analysis}

When you first need to make sense of the materials, add steps at the start:

<ol class="rai-flow rai-flow--4">
<li><b>Extract</b><span>copy the facts and figures you need out of the documents</span></li>
<li><b>Analyze</b><span>compare, find deviations, draw conclusions</span></li>
<li><b>Write</b><span>a summary or an email based on the conclusions</span></li>
<li><b>Check</b><span>compare the text with the facts from step 1</span></li>
</ol>

## Why it works {#why}

- **Accuracy.** At each step the model is busy with one thing.
- **Transparency.** You can see at which step an error appeared, which makes it easier to fix.
- **Repeatability.** A chain that works can be saved and run again: that's already close to [automation](page:kb/guides/automate-a-routine-task).

## How to pass the result on {#pass}

Paste the result of the previous step into the next prompt in a separate tag, for example `<facts>…</facts>`, and say directly what to do with it: “Using the facts in &lt;facts&gt;, write a summary…”.

## Self-check as a separate step {#review}

The last step is a review: “Here is the summary and here are the source facts. Find discrepancies and unsupported statements.” A fresh look at a finished text catches errors that slip by during writing. A review by the model doesn't replace yours: still check the figures and facts in the final text yourself.

## Try it now {#try}

Prepare a draft reply to a customer complaint — without the customer's name, account number, or other personal data.

1. **Draft:** “I work in the customer complaints department. Here is the gist of the complaint and what we found out. Draft a polite reply to the customer, 6–8 sentences, with no promises beyond what we found out.”
2. **Review:** “Here is the reply and the source facts. Find every place where the reply promises more than the facts support, or sounds harsh or unclear.”
3. **Revise:** “Fix the reply based on these comments.”

Compare the final version with the draft from the first step.
