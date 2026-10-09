---
title: What AI can and cannot do
summary: Four properties of language models (how they write, what they know, what they remember, and how they follow instructions), why an assistant can be confidently wrong, and where it needs your documents.
category: Getting started
level: start
minutes: 6
order: 12
tags: capabilities, limitations, models, knowledge, context
source: AI Capabilities and Limitations
source_url: https://academy.claude.com/courses/ai-capabilities-and-limitations
source_hash: 8bbce329738c
---

This guide is for people who have already tried an assistant and want to understand why it sometimes does brilliantly and sometimes gets things confidently wrong. By the end, you will be able to explain to a colleague where such mistakes come from and when the assistant needs your documents.

Inside an assistant there is a **language model**: a program trained on a huge amount of text to write coherent text. You don't need the technical details: four properties are enough to explain both its strength and its mistakes.

<div class="rai-cards rai-cards--4">
<article><h3>1. It writes piece by piece</h3><p>The model builds its answer one small piece of text at a time, each time choosing the most likely continuation. That is why it does familiar things brilliantly and can smoothly write something untrue.</p></article>
<article><h3>2. It knows what it has seen often</h3><p>It is strong on common topics and weak on anything rare, new, highly specialized or disputed. It knows nothing of what happened after its training.</p></article>
<article><h3>3. It remembers only the conversation</h3><p>Its working memory is the [[context-window|context window]]: everything in the current conversation. In long texts, details can quietly slip out of its attention.</p></article>
<article><h3>4. It follows concrete instructions</h3><p>It reliably carries out short, concrete, checkable instructions. Abstract ones it interprets in its own way, or follows to the letter rather than in spirit.</p></article>
</div>

## Why the model is confidently wrong {#why}

The model doesn't look up the answer in a database of facts; it writes the most plausible continuation. If it doesn't know the fact it needs, a plausible invention looks just as confident as the truth. This is a [[hallucination|hallucination]], and it is why answers need [checking](page:kb/guides/checking-results).

## Where AI is strong {#strong}

Shortening, retelling, rewording, translating, formatting to a template, breaking a text into parts, comparing two documents, sketching options. Anything the world has done many times over.

## Where to be careful {#careful}

- **Your internal rules and anything new.** The model doesn't know, or knows only roughly, your organization's procedures, tariffs and product terms, new regulations from the regulator and local specifics. Give it the document itself (one you are allowed to share) and have it answer from that. For recent public news you can turn on search, if it is available in your work account.
- **Figures and facts.** A made-up figure looks just as confident as a real one, so check against the source.
- **Long material.** Paste the document first and ask your question after it, at the end of the prompt. Ask for quotes.
- **Vague instructions.** “Make it good” is bad; “five points, one sentence each” is good.

## Typical model “habits” {#habits}

Models tend to agree with you, write longer than needed, play it safe and sound more certain than they are. It helps to say so directly: “If I'm wrong, push back”, “keep it short”, “if you're not sure, say so”.

When an answer is strange, ask yourself: is it a gap in knowledge, a lapse of memory, a misread instruction, or just a “smooth continuation”? The answer will tell you what to fix in the prompt.

## Try it now {#try}

Ask the assistant about an internal procedure you know well, for example how an internal memo gets approved, first without a document. Then paste the text of the procedure (if it may be shared) and ask the same question. Compare the answers: where did the model make things up, and where did it answer from the document?
