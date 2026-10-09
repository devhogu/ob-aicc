---
title: "Claude Code: how to save context and budget"
summary: Why usage grows in long sessions, and ten habits that cut it without losing quality.
category: Claude Code
level: basic
minutes: 5
order: 54
tags: claude code, costs, context, model, limits
source: Эффективное управление затратами (документация на русском)
source_en: Manage costs effectively
source_url: https://code.claude.com/docs/ru/costs
source_hash: 44d29c70448c
---

After reading this guide, you will be able to see where your context and usage limit go, and apply ten habits that cut usage without losing quality.

Every prompt in Claude Code sends the model the whole current conversation: your messages, the files it read, command output. The longer the session, the more each next question costs, even a short one. So saving almost always comes down to one thing: keeping the context small.

## How to see usage {#see}

- `/usage` shows the current session's usage. The dollar amount is an estimate: on a subscription it isn't what you are billed. On the Pro, Max, Team and Enterprise plans it also shows what share went to skills, subagents, plugins and MCP connections.
- `/context` shows what exactly is taking up the context.
- `/insights` gives a report on how you work and where you lose time.

## Ten habits {#habits}

<ol class="rai-principles">
<li><b><code>/clear</code> between tasks</b><span>Old context is paid for in every following message. Before clearing, use <code>/rename</code> so you can come back later.</span></li>
<li><b>The right model for the task</b><span>Sonnet for most tasks, Opus for complex architecture and reasoning. Switch with <code>/model</code>.</span></li>
<li><b>A specific prompt</b><span>“Add input validation to the login function in auth.ts” instead of “improve the code” means less needless reading.</span></li>
<li><b>A plan for anything complex</b><span>Plan mode prevents expensive rework when the direction turns out to be wrong.</span></li>
<li><b>Stop early</b><span>Press <code>Esc</code> as soon as Claude heads the wrong way; <code>/rewind</code> to go back.</span></li>
<li><b>A short CLAUDE.md</b><span>Up to 200 lines; put special procedures into skills, which load only when needed.</span></li>
<li><b>Hand noisy work to subagents</b><span>Let a subagent read logs, tests and documentation; only the conclusion comes back to the conversation.</span></li>
<li><b>Command line instead of MCP</b><span>If a system has a command-line tool (<code>gh</code>, <code>aws</code>, <code>gcloud</code>), it uses less context than an MCP connection; turn off connections you don't need in <code>/mcp</code>. On connections, see <a href="page:kb/guides/claude-code-mcp">MCP connections</a>.</span></li>
<li><b>Less thinking for simple things</b><span>For simple tasks you can lower the effort level with the <code>/effort</code> command.</span></li>
<li><b>The check in the prompt</b><span>Give the tests and the expected result up front, and Claude catches mistakes on its own, without extra rounds.</span></li>
</ol>

## Why usage grows in a long session {#why}

Long context, breaks (after a pause the cache expires and the history is processed again), scheduled tasks and subagents all send their own requests. `/compact` also costs a request, while `/clear` is free.

**Try this:** run `/context` and `/usage` at the start and at the end of your next task and compare; before a new task, use `/rename` and `/clear`.
