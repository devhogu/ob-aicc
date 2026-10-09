---
title: "Role and structure: separate instructions from data"
summary: One sentence about the role sets the tone, and simple tags around documents keep Claude from confusing pasted text with your instructions.
category: Prompting Claude
level: basic
minutes: 4
order: 23
tags: prompt, role, tags, xml, structure
source: Лучшие практики составления подсказок
source_en: Prompting best practices
source_url: https://platform.claude.com/docs/ru/build-with-claude/prompt-engineering/claude-prompting-best-practices
source_hash: 0bc781631969
---

When your instructions, pasted documents, examples, and question are all mixed together in a prompt, Claude may take part of a document for an instruction. This guide is about two simple habits that prevent this. Afterwards you'll be able to give Claude a role and separate instructions from data in a prompt with tags.

## Give a role {#role}

A role is one sentence at the start that says on whose behalf or in what capacity to work. It sets both the knowledge and the tone:

- “You are a credit risk analyst. Explain things briefly and without jargon.”
- “You are a compliance specialist. Review the text strictly and flag anything questionable.”

It also helps to name the reader: “…for branch staff who aren't familiar with the methodology.” You don't need a long “backstory”: one or two sentences are enough.

## Separate the parts of the prompt {#tags}

Wrap each part of the prompt in a clear tag. A tag is a word in angle brackets: `<instructions>` at the start of a part and `</instructions>`, with a slash, at the end. Technically these are called XML tags, but you don't need to know that: Claude simply sees what is where — like labeled boxes when you move house.

```
<instructions>
Compare the two contracts and list the differences in payment terms.
Answer as a table: clause, contract A, contract B.
</instructions>

<document name="Contract A">
…text…
</document>

<document name="Contract B">
…text…
</document>
```

The rules are simple:

- name tags clearly and the same way from prompt to prompt: `<instructions>`, `<context>` (the background), `<document>`, `<example>`;
- nest tags when the parts are naturally nested: several `<document>` tags inside `<documents>`;
- refer to the tag in your instructions: “based on the document in &lt;document name="Contract A"&gt;”.

A short request doesn't need tags. They help when a prompt has several parts. Paste contracts and other internal documents only into a service approved for them — see [What you can and cannot share with AI](page:kb/guides/what-to-share).

## Why this matters for security too {#safety}

If a document came from outside — an email, a web page, a customer's file — it may contain text that looks like a command, for example “ignore the previous instructions and …”. A command planted like this is called a [[prompt-injection|prompt injection]]. A clear separation of “here are my instructions, and here is the data” reduces this risk but doesn't remove it: still check any result based on someone else's document.

## Try it now {#try}

Take a new internal regulation or policy that may be shared with your work account. Write a prompt in three parts: a role (“You are a methodologist…”), the document in a `<document>` tag, and the instruction in an `<instructions>` tag: “Summarize this for branch staff: what changes, from what date, and what they need to do differently. No more than 7 points.”
