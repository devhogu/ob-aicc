---
title: "Be clear and explain why"
summary: The colleague test — the key check for any prompt — and why one sentence on what the result is for improves the answer more than ten prohibitions.
category: Prompting Claude
level: basic
minutes: 4
order: 21
tags: prompt, clarity, context, colleague test
source: Лучшие практики составления подсказок
source_en: Prompting best practices
source_url: https://platform.claude.com/docs/ru/build-with-claude/prompt-engineering/claude-prompting-best-practices
source_hash: 30e5f75ad8cd
---

This guide is about two habits that improve almost any [[prompt|prompt]]: checking it with the “colleague test” and explaining what the result is for. By the end, you will be able to find what's missing from your prompt in a minute and add it.

Think of Claude as a very capable but new employee: it can do a lot, but it doesn't know your rules, your habits, or what “goes without saying.”

## The colleague test {#golden}

Before you send a prompt, imagine handing the same text to a colleague from another department who knows nothing about the task. Would they understand what to do, for whom, and in what form? If they would be lost, so will Claude.

## Say it directly {#direct}

- Say what result you need and in what form.
- If order or completeness matters, list the steps as a numbered list.
- If you need more detail or more than the bare minimum, ask for it: the model won't do more than you asked.

| Weaker | Stronger |
| --- | --- |
| “Make a sales summary” | “Write a summary of September sales for my manager: three key findings, a table by product, one page. Note anything in the data worth double-checking.” |
| “Summarize the minutes” | “Here are the notes from our department meeting. Write up the minutes: decisions, tasks with owners and deadlines, open questions. If a task has no deadline, write ‘no deadline given’.” |

## Explain why {#why}

A reason works better than a prohibition. Claude understands the point and applies it on its own to similar cases you didn't think of.

| Weaker | Stronger |
| --- | --- |
| “No abbreviations!” | “This text will be read by a customer who doesn't know our internal terms, so write without abbreviations or acronyms.” |
| “Keep it short” | “My manager will read this summary on a phone between meetings, so put the main point in the first two lines.” |

## Try it now {#try}

Take a prompt that got a weak answer. Check it with the colleague test and add one line: who the result is for and why it's needed. Send it in a new conversation and compare the answers.
