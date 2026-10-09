---
title: "Claude Code: everyday recipes"
summary: Ready-made sequences of prompts to understand code, fix a bug, refactor, write tests, open a PR, and work with documentation and images.
category: Claude Code
level: basic
minutes: 7
order: 51
tags: claude code, workflows, debugging, tests, refactoring, pr
source: Распространённые рабочие процессы (документация на русском)
source_en: Common workflows
source_url: https://code.claude.com/docs/ru/common-workflows
source_hash: 7546f7fadc7b
---

After this guide you will be able to take a ready-made recipe (understand someone else's code, fix a bug, write tests, prepare a PR) and work through it in your own repository.

Each recipe is a chain of prompts: start with a broad question and narrow it down. You can write the prompts in Russian.

<div class="rai-cards rai-cards--3">
<article><h3>Understand someone else's code</h3><p>“Give me an overview of this project” → “what are the main architecture decisions?” → “where are the key data models?” → “how does authorization work?”. Ask for a glossary of the project's terms.</p></article>
<article><h3>Find the right place</h3><p>“Find the files that handle user login” → “how are they connected?” → “trace the login from the interface to the database”.</p></article>
<article><h3>Fix a bug</h3><p>Give the command that reproduces the bug and the error text → ask for several possible fixes → apply the one you choose → check it.</p></article>
<article><h3>Refactor code</h3><p>“Find deprecated API calls” → “suggest how to rewrite utils.js” → “rewrite it, keeping the behavior” → “run the tests”. In small steps.</p></article>
<article><h3>Tests</h3><p>“Which functions aren't covered by tests?” → “add tests” → “add edge cases” → “run them and fix the failures”. Claude will follow the style of your existing tests. Test data must be made up only.</p></article>
<article><h3>Pull request (PR)</h3><p>“Summarize my changes” → “create a PR” → “expand the description”. Before you submit, ask it to name the risks. This doesn't replace review by a colleague.</p></article>
<article><h3>Documentation</h3><p>“Find functions without comments” → “add documentation” → “improve it with examples” → “check it against our standard”.</p></article>
<article><h3>Images</h3><p>Paste a screenshot of an error, a mockup or a diagram: “what's wrong here?”, “build the layout from this mockup”. The screenshot must contain no customer data.</p></article>
<article><h3>Not just code</h3><p>Claude Code works in any folder (notes, documentation, sets of markdown files) to search, edit and reorganize.</p></article>
</div>

## Try it now: tests for one module {#try}

1. “Which functions in `path/to/module` aren't covered by tests?”
2. “Write tests for them in the style of the existing ones. Use made-up data only. Don't change the module's code.”
3. “Run the tests and show the output.”
4. Look at `git diff` yourself: only test files were changed, they contain no real data, and no existing check has been weakened.

## Useful tricks {#tricks}

- `@path/to/file` includes a file in the prompt right away; `@folder` shows its structure.
- `claude --continue` picks up yesterday's work; `/rename` gives the session a clear name.
- `claude --worktree name` opens a second session on its own branch, so the edits don't get in each other's way.
- `claude --permission-mode plan` or Shift+Tab: plan first, then edit.
- “Have a subagent find out how token refresh works”: the subagent explores in its own context, and the main conversation stays uncluttered. For details, see [Subagents in Claude Code](page:kb/guides/claude-code-subagents).
- `git log --oneline -20 | claude -p "summarize the recent commits"` runs Claude in scripts, with no dialog. Note that without the `--bare` flag such a run executes the hooks and MCP connections set up in the repository and doesn't ask whether you trust the folder. Don't run it like this in someone else's or an unchecked repository; details are in [Claude Code in action](page:kb/guides/claude-code-in-action#headless).

When you run Claude from a script or on a schedule, word the prompt especially clearly, including what counts as success and where the result should go: Claude can't come back to you with questions.
