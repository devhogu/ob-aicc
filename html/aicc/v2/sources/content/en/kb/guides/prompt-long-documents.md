---
title: "Long documents: text first, question last"
summary: Three techniques for working with large documents — the order of the parts of a prompt, a tag for each document, and quotes before the answer — plus a ready prompt for comparing two contracts.
category: Prompting Claude
level: basic
minutes: 5
order: 25
tags: prompt, documents, long context, quotes, contract
source: Лучшие практики составления подсказок
source_en: Prompting best practices
source_url: https://platform.claude.com/docs/ru/build-with-claude/prompt-engineering/claude-prompting-best-practices
source_hash: 8355f0692905
---

Claude can read a very long text: an annual report, a contract, a dozen internal procedures at once. But details get lost easily in a long text — for people and for the model alike. This guide is about three techniques that will let you ask questions about large documents and check the answer against quotes.

<ol class="rai-flow">
<li><b>Documents at the top</b><span>all the text first, with the question and instructions at the end</span></li>
<li><b>Each in its own tag</b><span>with a title and a source</span></li>
<li><b>Quotes first</b><span>then an answer based on them</span></li>
</ol>

Share internal documents and contracts only with a service approved for them, and without personal data — see [What you can and cannot share with AI](page:kb/guides/what-to-share).

## Documents at the top, question at the bottom {#order}

Put long materials at the start of the prompt and the question at the very end. According to Anthropic, putting the question at the end noticeably improves the answer, especially when there are several documents.

## Each document gets its own tag {#tags}

You already know tags from the guide [Role and structure](page:kb/guides/prompt-structure). With several documents, it helps to give each one a number (`index`), a source (`<source>`), and the text (`<document_content>`):

```
<documents>
  <document index="1">
    <source>Lending procedure, 2026 edition</source>
    <document_content>…</document_content>
  </document>
  <document index="2">
    <source>Credit committee minutes</source>
    <document_content>…</document_content>
  </document>
</documents>

Which terms in the minutes are inconsistent with the procedure?
```

If you attach files rather than paste text, give them clear names: Claude will understand “Lending_procedure_2026.pdf” better than “document1.pdf”.

## Quotes first {#quotes}

Ask: “First, copy out word for word the passages that relate to the question, then answer based only on them.” This way Claude focuses on what matters and makes up less, and you can easily check the answer against the quotes. This approach is called [[grounding|grounding]]: every statement can be found in the document.

## Try it now: compare two contracts {#try}

Take two similar contracts, or two versions of the same contract, that may be shared with your work account. Paste them in and add at the end:

```
Compare the payment terms and the parties' liability in documents 1 and 2.
First, copy out word-for-word quotes from each document that relate to these terms.
Then, based only on the quotes, make a table: term, document 1, document 2, the difference.
If one of the documents doesn't have a term, say so.
```

Check two or three rows of the table against the contracts themselves: do the quotes match the text?
