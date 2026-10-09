---
title: "How Claude Code works"
summary: The agentic loop, tools, what Claude sees, sessions and context, undoing changes and permission modes, all on one page.
category: Claude Code
level: basic
minutes: 6
order: 50
tags: claude code, agentic loop, tools, modes, context
source: Как работает Claude Code (документация на русском)
source_en: How Claude Code works
source_url: https://code.claude.com/docs/ru/how-claude-code-works
source_hash: 31270d63bca1
---

After this guide you will be able to explain what Claude Code does between your prompt and its answer, which tools it uses, what it sees, how sessions work, and how permission modes decide what it may do without your consent.

Claude Code is not a chat that gives coding tips but an assistant that acts on its own: it reads files, edits them and runs commands. Although it was built for development, you can hand it almost anything done from the command line: documentation, builds, searching through files.

## The agentic loop {#loop}

The work goes round a loop of three steps, called the agentic loop:

<ol class="rai-flow">
<li><b>Gather context</b><span>find and read the files it needs, understand the task</span></li>
<li><b>Take action</b><span>edit code, run commands and tests</span></li>
<li><b>Verify</b><span>look at the result and repeat if needed</span></li>
</ol>

The loop adapts to the task: a question may need only reading, a bug fix several rounds. You are part of the loop: you can interrupt (`Esc`) and redirect it at any moment.

Hence the main advice: **delegate, don't dictate.** Give context and a goal as you would to a capable colleague, saying which files matter and what counts as done; Claude will work out the rest.

## Tools {#tools}

Files (read, edit, create), search (by name and by content), execution (commands, tests, git), the web (documentation, search), and code intelligence from your editor when the plugins are installed.

On top of that you can add extensions, each with its own guide:

- **skills**: ready-made instructions for a type of task;
- **MCP connections**: access to outside systems such as a tracker, a database or documentation;
- **hooks**: your own commands that run automatically at set moments;
- **subagents**: separate workers with their own context.

## What Claude sees {#access}

Your project, your terminal (anything you can run yourself), the git state, the `CLAUDE.md` file, auto memory (notes Claude saves on its own between sessions), and the extensions you have set up.

Everything Claude has read goes to the model as part of the prompt. So secrets and customer data must not sit anywhere it can look.

## Sessions and context {#sessions}

Everything Claude has seen during a session (your messages, the files it read, command output) is kept in its working memory, the [[context-window|context window]]. It is limited, and that explains most of the advice in the following guides.

- Each session starts with a clean context; put standing rules in `CLAUDE.md`.
- `claude --continue` continues the last session; `claude --resume` lets you pick one from a list.
- When the context fills up, Claude compacts the history, and detailed instructions from early on may be lost. `/context` shows what is taking up space.

## Safety {#safety}

<div class="rai-cards rai-cards--2">
<article><h3>Undo</h3><p>Before every edit Claude saves a snapshot of the file. Press <code>Esc</code> twice to go back. What was done by shell commands, and outside actions such as databases, APIs and deployment, can't be undone this way: for those you have only git and your own care.</p></article>
<article><h3>Permission modes</h3><p>Switch them with Shift+Tab: <b>Auto</b>: a checking model blocks anything risky (in newer versions a session starts in it); <b>Manual</b>: asks before edits and commands; <b>Accept edits</b>: edits files without asking; <b>Plan</b>: only explores and proposes a plan. For sensitive code, use <b>Manual</b>.</p></article>
</div>

There are also modes for runs with no person present; they are described in [Claude Code in action](page:kb/guides/claude-code-in-action#modes).

Not sure how to do something? Ask Claude Code itself: “how do I set up hooks?” It answers from its own documentation. `/init` creates `CLAUDE.md`, and `/doctor` checks the installation.

**Try this:** press Shift+Tab a few times and watch the mode change; ask a question about the project and run `/context` to see how much space is already taken.
