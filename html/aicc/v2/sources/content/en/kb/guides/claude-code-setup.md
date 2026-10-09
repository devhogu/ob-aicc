---
title: "Set up Claude Code for your project: CLAUDE.md, permissions, skills, hooks"
summary: What to put in CLAUDE.md and what to leave out, how to allow what's safe and block reading secrets, and when you need a skill, a subagent, a hook or a connection.
category: Claude Code
level: advanced
minutes: 8
order: 53
tags: claude code, claude.md, permissions, skills, hooks, subagents
source: Best practices for Claude Code
source_url: https://code.claude.com/docs/en/best-practices
source_hash: 0867f23886ad
---

After reading this guide, you will be able to turn `CLAUDE.md` into a short working note, set up permissions (what is fine without asking and what is never allowed), and choose how to cover repeated work: with a skill, a subagent, a hook or a connection.

A few minutes of setup make every following session noticeably better.

## CLAUDE.md, the project's short note {#claude-md}

Claude reads this file at the start of every session. `/init` creates the draft; refine it over time. For each line, ask yourself: “If I removed it, would Claude start making mistakes?” If not, delete it.

| Include | Leave out |
| --- | --- |
| Build and test commands that can't be guessed | Anything visible from the code |
| Style rules that differ from the usual | Well-known rules of the language |
| How to name branches and write PRs | Detailed API documentation (a link is better) |
| Architecture decisions, quirks of the environment | Information that changes often, long explanations |

An example fragment for a project in a regulated environment (replace the commands with your own):

```markdown
# Build and tests
- Build: ./gradlew build
- Tests for one module: ./gradlew :payments:test

# Rules
- Work only in the current branch; the developer commits and pushes
- Do not read or edit .env or the secrets/ directory
- Test data must be made up, with no real customer data
- Do not change database migrations without separate approval
```

If Claude keeps breaking a rule from the file, the file is most likely too long and the rule gets lost. Keep `CLAUDE.md` in git: it grows more valuable over time. Remember that `CLAUDE.md` is a request, not a guarantee: block what must never happen with permissions and hooks.

## Permissions {#permissions}

The permission mode sets the overall behavior (the modes are described in [How Claude Code works](page:kb/guides/claude-code-how-it-works#safety)). For sensitive code, choose Manual mode: every action goes through you.

Permission rules refine the mode for particular commands and files: `allow` covers safe, frequent things that need no asking (linter, tests), and `deny` covers what is never allowed. You can view and change the rules with the `/permissions` command or in a settings file: `~/.claude/settings.json` holds your personal ones, `.claude/settings.json` the shared project ones (kept in git). An example from the documentation:

```json
{
  "permissions": {
    "allow": [
      "Bash(npm run lint)",
      "Bash(npm run test *)"
    ],
    "deny": [
      "Read(./.env)",
      "Read(./.env.*)",
      "Read(./secrets/**)"
    ]
  }
}
```

- A read ban applies to Claude's built-in tools and to commands it recognizes, such as `cat`, but not to a program that opens files itself (a Python script, for example). For protection at the system level, turn on the isolated environment (sandbox) with the `/sandbox` command.
- Claude Code ignores the `.claudeignore` file; move its entries into `deny` rules.
- The safest option is to keep no real secrets in the working copy at all.

## What to choose for repeated work {#extend}

<div class="rai-cards rai-cards--4">
<article><h3>Skill</h3><p>Knowledge and procedures you need now and then: <code>.claude/skills/name/SKILL.md</code>. Claude loads it on its own or when you type <code>/name</code>. For details, see <a href="page:kb/guides/skills-complete-guide#code">Skills in Claude Code</a>.</p></article>
<article><h3>Subagent</h3><p>A separate worker with its own context and tools, a security reviewer for example: <code>.claude/agents/</code>. For details, see <a href="page:kb/guides/claude-code-subagents">Subagents</a>.</p></article>
<article><h3>Hook</h3><p>A command that runs every time, without exception: a check after an edit, a ban on writing to a folder. For details, see <a href="page:kb/guides/claude-code-hooks">Hooks</a>.</p></article>
<article><h3>Connections (MCP)</h3><p>Access to the task tracker, a database or documentation with the <code>claude mcp add</code> command, if the connection is approved. For details, see <a href="page:kb/guides/claude-code-mcp">MCP connections</a>.</p></article>
</div>

The rule of thumb: `CLAUDE.md` is for what is always needed, a skill for what is needed now and then, a hook for what must happen without fail.

## Safety {#safety}

`CLAUDE.md`, skills and project settings live in git and are read in every session, so they must contain no passwords, keys or tokens. Connect only approved tools and look at the changes (`git diff`) before you commit.

**Try this:** add a `deny` rule for files with secrets to the project's `.claude/settings.json`, open a new session and ask Claude to read `.env`: the request should be refused. Check the rules with the `/permissions` command.
