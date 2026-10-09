---
title: "Answer format: ask for what you need"
summary: How to get an answer in the form and length you need — a table, paragraphs, something short — and why “do this” works better than “don't do that.”
category: Prompting Claude
level: basic
minutes: 4
order: 24
tags: prompt, format, style, length, table
source: Лучшие практики составления подсказок
source_en: Prompting best practices
source_url: https://platform.claude.com/docs/ru/build-with-claude/prompt-engineering/claude-prompting-best-practices
source_hash: bfb27633abfe
---

Claude can answer in almost any form: a table, a list, an email, a short summary. This guide is about four techniques that help you get the right form and length the first time, without extra rounds of “make it shorter.”

## 1. Say what to do, not what not to do {#positive}

| Weaker | Stronger |
| --- | --- |
| “Don't use lists” | “Write in flowing prose, in paragraphs” |
| “Don't make it long” | “Answer in no more than five sentences” |
| “No introductions” | “Get straight to the point; the first sentence is the conclusion” |

## 2. Describe the format precisely {#exact}

Name the table columns, the number of points, the length, the language, and whether you need headings. “Table: product, September, October, change in %” is better than “make a table.”

An example for a report from Excel: “Here is an anonymized export of the number of customer requests by branch for September and October. Make a table: branch, September, October, change in %. Sort by change, from largest to smallest. Below the table, give three conclusions, one sentence each.”

## 3. Write the prompt in the style you expect back {#match}

The style of the prompt affects the style of the answer. If the prompt is all lists and bold text, the answer will most likely be the same. If you want calm business prose, write the prompt that way.

## 4. Show a sample {#sample}

The most reliable way is an [example](page:kb/guides/prompt-examples) of the finished result: paste in a past summary and ask for a new one following the same pattern.

## Shorter or more detailed {#length}

Current Claude models answer fairly briefly. If you need a detailed analysis or, on the contrary, a very short answer, say so directly and set a limit: “up to 100 words”, “one page.”

Pay attention to the verb, too. “Can you suggest how to improve this email?” gets you advice. “Rewrite this email” gets you a new email.

## Try it now {#try}

Take an answer from Claude whose form you didn't like. Don't fix it by hand — add one line about the format to the prompt: the table columns, the number of points, or a length limit. Compare the result.
