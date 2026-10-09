---
title: "Hooks in Claude Code: what must always happen"
summary: Automatic commands at key moments of Claude's work (notifications, formatting, blocking edits to important files), how to set them up and check them, and their risks.
category: Claude Code
level: advanced
minutes: 6
order: 56
tags: claude code, hooks, automation, rules
source: Автоматизация действий с помощью hooks (документация на русском)
source_en: Automate workflows with hooks
source_url: https://code.claude.com/docs/ru/hooks-guide
source_hash: 017e463c3650
---

After reading this guide, you will be able to turn a mandatory rule (“don't touch `.env`”, “format after every edit”, “tell me when you need my answer”) into a hook that always fires, and check that it works.

An instruction in `CLAUDE.md` is a request: Claude usually follows it but may miss it. A hook is a guarantee: your own command (usually a small script) that Claude Code itself runs at a set moment of its work, without exception.

## The main moments for hooks {#events}

There are many events you can attach a hook to; here are the main ones:

| Moment | When it fires |
| --- | --- |
| `SessionStart` | a session starts or resumes |
| `UserPromptSubmit` | you have sent a prompt, and Claude hasn't processed it yet |
| `PreToolUse` | before Claude acts; it can block the action |
| `PostToolUse` | after an action succeeds |
| `Notification` | Claude is waiting for your answer or permission |
| `Stop` | Claude has finished its response |
| `PreCompact` / `PostCompact` | before and after the context is compacted |

## What people usually automate {#examples}

<div class="rai-cards rai-cards--4">
<article><h3>Notifications</h3><p>A desktop alert when Claude is waiting for your decision.</p></article>
<article><h3>Formatting</h3><p>Automatic code formatting after every edit.</p></article>
<article><h3>File protection</h3><p>A ban on editing migrations, <code>.env</code> and deployment configuration.</p></article>
<article><h3>Context after compaction</h3><p>A fresh reminder of the key rules once the history has been compacted.</p></article>
</div>

## How to set it up {#setup}

The easiest way is to ask Claude: “Write a hook that runs formatting after every edit” or “Write a hook that blocks writing to the migrations folder.” Hooks are stored in settings files: `~/.claude/settings.json` holds your personal ones, `.claude/settings.json` the shared project ones (in git). The `/hooks` command shows every hook that is set up.

A hook receives a description of the event as JSON and answers with an exit code:

- `0`: no objections, the work goes on;
- `2`: block the action; the hook writes the reason to the error stream, and for many events it goes to Claude so it can correct itself;
- any other code: an error in the hook itself, which **does not block**: the action goes ahead.

For the weak spots of hooks during long work, see [Claude Code in action](page:kb/guides/claude-code-in-action#hook-gaps).

## Precautions {#safety}

- A hook is a command on your machine with your rights. Read every hook before you turn it on, especially one written by someone else.
- Hooks from a repository's `.claude/settings.json` also run on your machine. In a normal session Claude Code first asks whether you trust the folder; when you run `claude -p` without the `--bare` flag there is no such question, and the repository's hooks fire at once.
- Check paths and escape the input: a hook receives whatever Claude sent.
- If a hook must see *all* file changes, keep in mind that Claude can change files through shell commands too, not only through edits. There is a `FileChanged` event for this.

## Try it now {#try}

Ask Claude: “Write a `PreToolUse` hook for this project that blocks edits to `.env` and to files in `migrations/`: exit code 2 and a clear message.” Read the script it produces, make sure with `/hooks` that the hook is in place, then ask Claude to change `.env`: the edit should be blocked.
