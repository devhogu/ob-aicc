---
title: "Claude Code: your first session in a repository"
summary: Start Claude Code in your repository, create CLAUDE.md, give it a first task and check the result in the diff, without losing control of the changes.
category: Claude Code
level: basic
minutes: 8
order: 49
tags: claude code, development, terminal, repository, claude.md
source: Best practices for Claude Code
source_url: https://code.claude.com/docs/en/best-practices
source_hash: b4e705503fa0
---

After reading this guide, you will be able to start Claude Code in your repository, create a `CLAUDE.md` file with the project's rules, give it a small first task and check the result before it goes into a commit.

Claude Code is a coding assistant that runs in the terminal, right in the project folder. It reads files, makes changes, and runs commands and tests. In effect it is an [[ai-agent|AI agent]] for development, so the rule is the same as for any agent: it acts, and you stay in control and answer for the result.

Use it only with an account approved in your organization and only in repositories where this is allowed.

## Before the first run {#before}

- **A separate branch.** Create a working branch, for example `git switch -c try-claude-code`. Everything Claude does stays there until you have checked it.
- **No secrets in the working copy.** Claude Code reads the project's files, and whatever it reads goes to the model along with the prompt. If the folder holds, say, a `.env` file with real passwords, remove it first or block it from being read; the section [Permissions](page:kb/guides/claude-code-setup#permissions) shows how.

## First run {#start}

1. Open a terminal in the repository folder.
2. Run `claude` and sign in with your work account. If the command isn't found, Claude Code isn't installed yet: install it the way your organization has approved (the official instructions are in the [Claude Code documentation](https://code.claude.com/docs/en/overview)).
3. Check the permission mode (see “Control” below). In a sensitive repository, switch to Manual mode right away.
4. Start with a question, not a change: “Explain how this project is structured and where the entry point is.”
5. Run `/init`. Claude creates `CLAUDE.md`, a short note about the project that it reads at the start of every session. Read the draft, remove what you don't need and add your own: how to build, how to run the tests, what not to touch. For what else is worth putting there, see [Set up Claude Code for your project](page:kb/guides/claude-code-setup).

## How to frame a task {#task}

- **One task, one step.** “Add an empty-value check to function X and a test for it.”
- **Say how to check.** “Run the tests and show me the result.”
- **Point to files.** Give the path to the file or function you mean.
- **For anything big, a plan first.** “Propose a plan first, without changing anything.”

## Control {#control}

- **Permission mode.** It decides whether Claude asks before it acts; switch it with Shift+Tab. In Manual mode Claude asks before every edit and command, so read what it is about to do before you agree. In newer versions a session starts in Auto mode by default: a separate model checks each action and stops risky ones, but it does not judge whether the code is correct. **For sensitive repositories, choose Manual mode.** For all the modes, see [How Claude Code works](page:kb/guides/claude-code-how-it-works#safety).
- **Branch and diff.** Look at `git diff` before every commit. Commit and push yourself, through your usual code review process.
- **Secrets.** Passwords, keys and tokens must not end up in prompts or in project files.
- **Customer data.** Don't paste it into prompts or use it in tests; test data must be made up.
- **Responsibility.** The result is your code: you check it, and you answer for it.

## Try it now {#try}

1. In your branch, run `claude` and ask a question about how the project is structured.
2. Run `/init`, read `CLAUDE.md` and add the command that runs the tests.
3. Give it a small task with a check: “Add an empty-value check to function X, write a test for it and run the tests.”
4. Look at `git diff`: was only what you asked for changed? Does the test actually check something?
