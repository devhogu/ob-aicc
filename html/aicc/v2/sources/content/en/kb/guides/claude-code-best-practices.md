---
title: "Claude Code: practices that work"
summary: The essentials of Anthropic's recommendations (give a way to verify, plan first, precise context, a clean session) and five common mistakes.
category: Claude Code
level: advanced
minutes: 8
order: 52
tags: claude code, practices, context, plan, verification
source: Best practices for Claude Code
source_url: https://code.claude.com/docs/en/best-practices
source_hash: d703a660b882
---

After this guide you will be able to give Claude a way to check its own work, run a complex task through a plan and keep the session clean: three habits that the quality of almost any work in Claude Code depends on.

Almost all the advice on Claude Code follows from one limit: the [[context-window|context window]] fills up fast, with every message, every file read and every command output. The fuller it gets, the more often the model forgets early instructions and makes mistakes. Context is the main resource you have to manage.

## 1. Give it a way to verify the work {#verify}

Claude stops when the work *looks* finished. Give it a check that answers yes or no: tests, a build, a linter, a screenshot to compare against. Then it carries the work through to a result on its own.

| Weaker | Stronger |
| --- | --- |
| “write an email check” | “write validateEmail; examples: user@example.com is valid, user@.com is invalid; run the tests after implementing it” |
| “the build is failing” | “the build fails with this error: […]. Fix the cause rather than suppressing the error, and check that the build passes” |

Ask it to show evidence: the test output, the command and its result. And check for yourself that Claude hasn't weakened existing tests to make them pass.

## 2. Explore first, then plan, then code {#plan}

Plan mode (switched with Shift+Tab) lets Claude read and answer without changing anything. The order: explore the code → make a plan → implement → commit. Small things like a typo don't need a plan: if you can describe the change in one sentence, just ask for it. For changes to sensitive code a plan is doubly useful: you can discuss the approach with a colleague before the first edit appears.

## 3. Precise context in the prompt {#context}

Name the file, the scenario and how to check; point to similar code as a model; describe the symptom, the likely location and what “fixed” means. You can reference files with `@` and paste screenshots straight into the prompt.

## 4. Keep the session clean {#session}

- `Esc` stops Claude so you can correct course; `Esc Esc` or `/rewind` goes back to an earlier point.
- `/clear` between unrelated tasks.
- Corrected it twice and it's still wrong? `/clear` and a new, more precise prompt is almost always better than a long session full of corrections.
- Hand large investigations to subagents: they read files in their own context and bring back only the conclusions. For details, see [Subagents in Claude Code](page:kb/guides/claude-code-subagents).

## Five common mistakes {#mistakes}

<div class="rai-cards rai-cards--3">
<article><h3>The “everything” session</h3><p>Different tasks in one conversation clutter the context. The cure is <code>/clear</code>.</p></article>
<article><h3>Going round in corrections</h3><p>After two failed corrections, start with a clean slate and a better prompt.</p></article>
<article><h3>A bloated CLAUDE.md</h3><p>When the file is too long, important rules get lost. Cut it down.</p></article>
<article><h3>Trusted, not checked</h3><p>Plausible code with no check of the edge cases. No check, no release.</p></article>
<article><h3>Endless exploration</h3><p>“Explore everything” with no limits eats the context. Narrow the task or give it to a subagent.</p></article>
</div>

## Try it now {#try}

Take the next task from your tracker. Start in Plan mode, read the plan and correct it. Then ask Claude to implement it and run the tests, showing the output. If after two corrections the result is still wrong, `/clear` and write a new, more precise prompt.

Project setup (`CLAUDE.md`, permissions, skills, hooks) is in the guide [Set up Claude Code for your project](page:kb/guides/claude-code-setup).
