---
title: "Subagents in Claude Code"
summary: Separate workers with their own context and tools; when you need them, which ones are built in and how to make your own.
category: Claude Code
level: advanced
minutes: 8
order: 55
tags: claude code, subagents, context, delegation
source: "Создание пользовательских subagents (документация на русском) и курс Introduction to Subagents"
source_en: "Create custom subagents and the Introduction to Subagents course"
source_url: https://code.claude.com/docs/ru/sub-agents
source_hash: a4019e8cddf9
---

After reading this guide, you will be able to decide whether a task needs a subagent and make your own, for example a reviewer that only reads code and reports in a set format.

A subagent is a separate worker inside a session, with its own context, its own instructions and its own set of allowed tools. The main Claude hands it part of the work and gets back only the conclusions.

## Why {#why}

<div class="rai-cards rai-cards--4">
<article><h3>Clean context</h3><p>Code searches, logs and long output stay with the subagent and don't clutter the conversation.</p></article>
<article><h3>Limits</h3><p>A reviewer subagent can be allowed to read only.</p></article>
<article><h3>Specialization</h3><p>Its own instructions for one task: security, tests, documentation.</p></article>
<article><h3>Savings</h3><p>Simple tasks can go to a faster, cheaper model.</p></article>
</div>

Some subagents are already built in: **Explore** for fast, read-only code search, **Plan** for research in Plan mode, and **General-purpose** for multi-step tasks.

## How to make your own {#create}

The easiest way is to ask: “Create a code-improver subagent that suggests readability and performance improvements.” Or by hand, in the file `.claude/agents/code-improver.md`:

```markdown
---
name: code-improver
description: Finds and suggests readability and performance improvements
tools: Read, Grep, Glob
model: sonnet
---
You are a code improvement specialist. For each finding, explain the problem,
show the current code and suggest an improved version. Do not change the code yourself.
```

`.claude/agents/` holds the project's subagents (keep them in git so the whole team has them), and `~/.claude/agents/` your personal ones for all projects. Only `name` and `description` are required; if you leave out `tools`, the subagent gets all the tools of the main session, so it is better to set the list explicitly.

## How to invoke one {#use}

- In words: “Use the code-improver subagent to check this module.”
- To be sure, mention it: type `@` and pick the subagent from the list.
- An independent review of finished work: “Have a subagent check the changes against the plan and list the gaps.” A fresh look doesn't depend on the reasoning of whoever wrote the code.

## How to design a good subagent {#design}

From the Introduction to Subagents course:

- **The description decides what the main Claude will hand over.** The main agent sees the name and description of every subagent, and writes the assignment from the description. Put in it what the subagent needs to receive: “name exactly which files to check”, “return sources that can be cited”.
- **The output format is the biggest improvement.** It gives the subagent a point at which to stop. For a review: summary · critical · important · minor · recommendations · verdict.
- **An “Obstacles” section.** Have the subagent report setup problems, workarounds and flaky dependencies; otherwise the main Claude will discover them all over again.
- **Minimal tools.** A researcher gets search and reading; a reviewer gets those plus commands for `git diff`; only a subagent that edits gets edit tools.

### Do you need a subagent {#need}

The deciding question: **does the intermediate work matter to you?** If only the conclusion matters, a subagent saves context. If you need the reasoning, do it in the main conversation: a subagent returns only the result, and you don't see how it got there.

Good fits: research, review (Claude checks code better when it was “written by someone else”), and tasks with special rules, such as texts or layouts that follow a design system.

### What not to do {#antipatterns}

- **“Expert” roles.** “You are a Python expert” adds nothing.
- **Sequential chains** of “reproduce → debug → fix” across different subagents: context is lost at every handoff.
- **A subagent for running tests** that hides the full output: in Anthropic's tests this option gave the worst result.

## When you don't need one {#not}

For small, targeted edits and for tasks that need frequent back-and-forth, a subagent only adds an extra step.

## Try it now {#try}

Ask Claude: “Create a project subagent security-reviewer in `.claude/agents/`. Tools: only Read, Grep, Glob. It checks the files it is given for passwords, keys and tokens, for real customer data in tests and examples, and for disabled checks. Output format: summary · critical · important · minor · verdict. It changes nothing itself.” Read the file it creates, then call the subagent with `@` on the files from your latest change. Its report is a hint for your review, not a replacement for it.
