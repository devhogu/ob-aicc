---
title: "Show an example"
summary: Examples are the most reliable way to set the tone, format, and structure of an answer. How many you need, what they should be like, and how to put them into a prompt.
category: Prompting Claude
level: basic
minutes: 4
order: 22
tags: prompt, examples, sample, few-shot, format
source: Лучшие практики составления подсказок
source_en: Prompting best practices
source_url: https://platform.claude.com/docs/ru/build-with-claude/prompt-engineering/claude-prompting-best-practices
source_hash: 7e8b133e9b24
---

A style is hard to describe in words and easy to show. This guide is about setting the tone and format of an answer with ready-made samples. By the end, you will be able to give Claude your best emails or summaries and get new text in the same style.

## What examples should be like {#good}

<div class="rai-cards rai-cards--3">
<article><h3>Relevant</h3><p>Close to your real task: the same kind of documents, the same reader.</p></article>
<article><h3>Varied</h3><p>Different from one another, so Claude doesn't pick up an accidental detail such as the same length or the same opening.</p></article>
<article><h3>Set apart</h3><p>Marked as examples so they aren't mistaken for instructions: “Example 1: … Example 2: …” or &lt;example&gt; tags.</p></article>
</div>

**Three to five** examples work best. You can ask Claude to assess your examples — whether they are varied enough — or to come up with a few more along the same lines.

## What it looks like {#how}

Below, each example is wrapped in an `<example>` … `</example>` tag. A tag is just a word in angle brackets: it shows Claude where an example starts and ends. For more on tags, see the guide [Role and structure](page:kb/guides/prompt-structure). The answers in the example are illustrative.

```
Reply to the customer in the same style as in the examples.

<example>
Question: Can I close my card in the app?
Answer: Yes. Open the card → “Settings” → “Close card”. We'll transfer the remaining balance to your account.
</example>
<example>
Question: Why didn't my payment go through?
Answer: Usually it's the card limit. Check the limit under “Card” → “Limits”. If you haven't reached it, write to us and we'll sort it out.
</example>

Customer question: {question}
```

Replace `{question}` with the customer's real question — without their name, account number, or other personal data.

## Try it now {#try}

1. Find three of your own emails that worked well: for example, replies to customer requests or emails to colleagues in another department.
2. Remove names, account numbers, phone numbers, and anything else that can't be shared (see [What you can and cannot share with AI](page:kb/guides/what-to-share)).
3. Paste them in as “Example 1”, “Example 2”, “Example 3” and ask: “Write an email about … in the same style.”
4. Compare the result with what you get without examples.
