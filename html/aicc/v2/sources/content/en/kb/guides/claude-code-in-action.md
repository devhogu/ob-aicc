---
title: "Claude Code in action: long sessions, automation, and review — the complete guide"
summary: How to move from single prompts to long Claude Code work with minimal supervision — directing a session, goals, CLAUDE.md, a verification skill, permission modes, hooks, scheduled and CI runs, reviewing the result, and safety for a regulated organization.
category: Claude Code
level: deep
minutes: 40
order: 4
featured: true
layout: course
tags: claude code, goal, loop, worktrees, hooks, modes, headless, github actions, code review, plugins, agents
source: "Claude Code in Action — Claude Academy, проверено по документации Claude Code на русском"
source_en: "Claude Code in Action — Claude Academy, checked against the Claude Code documentation in Russian"
source_url: https://academy.claude.com/courses/claude-code-in-action
source_hash: 5f49b1d0444a
---

This guide is for people who already use Claude Code for single tasks and want to move to **long work with less supervision**: set a goal, walk away, and come back to a result you can check. It retells the Claude Code in Action course and has been checked against the official documentation in Russian; where the course and the documentation disagree, the documentation is right.

After reading this guide, you will be able to give Claude Code a checkable goal and leave it to work, choose the permission mode and the kind of automation to fit the task, review the result from the diff rather than the summary, and know which settings matter for a regulated organization.

The course's main idea: **the less you watched, the more you check.** Autonomy without checking is not a saving but a deferred risk.

For the basics it builds on, see [How Claude Code works](page:kb/guides/claude-code-how-it-works) and [Practices that work](page:kb/guides/claude-code-best-practices).

## Directing a long session {#steer}

Two habits: **set the boundaries first, then steer**. Actually read the plan from Plan mode rather than skimming it: correcting a plan is faster than untangling the result later.

### Directed compaction {#compact}

<code>/compact Focus on implementing the --version flag</code>: the text after the command decides what stays in the compacted history. It is how you steer the context.

### Rewind with options {#rewind}

Pressing <code>Esc</code> twice on an empty line opens the restore points; each of your messages creates one. The options:

| Option | When |
| --- | --- |
| Restore code and conversation | Claude went the wrong way; start again from that point |
| Restore conversation only / code only | to restore just one of the two |
| Summarize from here | drop a side branch of the conversation and keep the beginning |
| Summarize up to here | condense a long preparation and keep the implementation whole |

Rewind does not undo what was done by shell commands (installed packages, for example) or edits made by background subagents: **for that there is only git**.

### Goal: work until done {#goal}

<code>/goal all tests in src/billing pass, type checking reports zero errors</code>: Claude keeps working until the condition is met. After each step a separate fast model reads the conversation and decides: met, not met, or impossible. <code>/goal clear</code> removes the goal; <code>/goal</code> with nothing after it shows the status.

A good condition is **one that can be checked from Claude's own output**:

```text
/goal npm test exits with code 0, no existing test file is changed, or stop after 20 turns
```

- One measurable end state, a way to prove it, prohibitions and a turn limit.
- A goal does not change the permission mode: for unattended work, combine it with Auto mode.
- The goal clears itself on an error a person must fix: sign-in, a limit, an overflow.
- The course's rule: **set a goal when “done” is easier to describe than the steps.**
- For a sensitive repository, unattended work may be unacceptable. Then set the goal in Manual mode: Claude will stop at every question, and you will confirm.

**Try this:** in a separate branch, set a `/goal` with the condition “`npm test` (or your test command) exits with code 0, no existing test file is changed, or stop after 20 turns”. When Claude finishes, read the `git diff` first and only then its summary.

### Scheduled polling in a session {#loop}

<code>/loop 5m check whether the deployment has finished</code> repeats the prompt at an interval; with no interval, Claude picks a pause between a minute and an hour itself. It works while the session is open; repeats expire after seven days.

### Parallel sessions {#worktrees}

<code>claude --worktree name</code> (or <code>-w</code>) creates a separate copy of the repository on its own branch, so two sessions don't get in each other's way. The <code>.worktreeinclude</code> file lists untracked files (environment settings) to copy into each copy. Add the <code>.claude/worktrees/</code> directory to <code>.gitignore</code>.

## A CLAUDE.md that gets followed {#claude-md}

CLAUDE.md is **guidance, not enforcement**: lines compete for attention, and the longer the file, the worse each rule is followed.

- **Hard rules** such as “never push to main” belong not in CLAUDE.md but in a hook (see “Hooks”).
- Four levels load together: the organization's policy (which can't be turned off), your personal file, the project file (in git) and the local <code>CLAUDE.local.md</code> (not in git; for example, decisions about your branch).
- Imports such as <code>@.claude/conventions/code-style.md</code> help organize the file but **don't shrink the context**: whatever is imported is inserted whole.

### How to word rules {#rules}

| Weaker | Stronger |
| --- | --- |
| “Follow the project structure” | “New API handlers go in src/api/handlers, one per file” |
| “Don't use default export” | “Use named exports, not a default export” |

- Specific and checkable; say **what to do instead**.
- Save the “IMPORTANT” highlight for 2–3 truly important rules, no more.
- Every mistake Claude makes is a bug report on CLAUDE.md: “add this to CLAUDE.md”. And the other way round: **delete any line you can't justify.**
- The course's advice: start without CLAUDE.md, see where you have to correct Claude, and only then run <code>/init</code>.

## Verification skill {#verify-skill}

The first skill worth writing is **verification**. It fires after changes: run the tests → read the diff → make sure no test was weakened → a pass/fail report with evidence.

> “Done” does not mean “the code looks right”. Done is when the checks have been run and the result is stated plainly.

```markdown
---
name: verify-changes
description: Checks changes after code edits (tests, the diff, weakened
  tests) and gives a report with evidence. Use after any refactoring
  and before a commit.
---
1. Run ./scripts/check.sh and show the full output.
2. Read the git diff. Find tests that were skipped, deleted or weakened.
3. Find new dependencies and addresses and keys written into the code.
4. Find real customer data in tests and examples.
5. Report: pass / fail, with evidence for each item.
```

Put the skill in the project's <code>.claude/skills</code>, and the whole team will have it. What goes where: **CLAUDE.md** for standing rules; a **skill** for a procedure for a type of task; a **hook** for what can't be skipped. The rule: if you have typed the same multi-step instruction twice, it is a skill. For details, see [Claude skills: the complete guide](page:kb/guides/skills-complete-guide).

## Permission modes {#modes}

| Mode | What it does | Where it fits |
| --- | --- | --- |
| Manual | asks before edits and commands | sensitive code, getting started |
| Accept edits | edits files and runs simple file commands without asking | a familiar task under supervision |
| Plan | only explores and proposes a plan | understand before editing |
| Auto | a separate model checks every action and blocks dangerous ones | unattended work |
| Don't ask | runs only what was allowed in advance and silently declines the rest | CI, scheduled jobs: nothing gets stuck on a question |
| Bypass | no checks of any kind | **only** in an isolated container with no network |

- Shift+Tab switches between Manual, Accept edits, Plan and Auto.
- In newer versions, interactive sessions **start in Auto mode**.
- Important: the check in Auto judges **intent, not correctness**. Broken authorization will pass the check: “broken doesn't mean dangerous”. That is why Auto is combined with a hook that runs the tests.

## Hooks: what must happen {#hooks}

There are about thirty events; the key ones for long work:

| Event | What for |
| --- | --- |
| PreToolUse | the main enforcement tool: block, allow or change an action before it runs |
| PostToolUse | formatting and checks after an edit |
| Stop / SubagentStop | “you're not done yet”: don't let it finish while the tests fail |
| SessionStart with the <code>compact</code> matcher | bring back the key rules after the context is compacted |
| InstructionsLoaded | audit what went into the context |

### Exit codes {#exit-codes}

- <code>2</code>: block (the message goes to Claude). Stop with code 2 won't let the session finish.
- <code>1</code>: **does not block**, only reports an error.
- PostToolUse is too late to block: the action has already run.

### Where hooks are unreliable {#hook-gaps}

- A PreToolUse hook that times out **lets** the action through.
- A Stop hook is lifted after eight blocks in a row with no action; check the <code>stop_hook_active</code> field.
- If the organization allows only managed hooks, <code>/goal</code> stops working.

A useful trick is **“mask, don't block”**: PreToolUse finds a secret key in a command and swaps it for a placeholder instead of stopping the work. For the basics, see the guide [Hooks in Claude Code](page:kb/guides/claude-code-hooks).

## Scheduled and non-interactive runs {#automation}

A ladder of choices, from “build nothing” to your own program:

<ol class="rai-flow">
<li><b>Routines</b><span>a prompt + a repository + connections + a run on a schedule, a call or a GitHub event; runs in Anthropic's cloud</span></li>
<li><b>claude -p</b><span>a run from a script or CI with no dialog</span></li>
<li><b>Agent SDK</b><span>your own program with Claude inside</span></li>
</ol>

### Routines {#routines}

<code>/schedule daily dependency check at 9:00</code> or through claude.ai/code/routines. The minimum interval is an hour; each run starts from a fresh copy of the main branch; changes can be pushed only to <code>claude/*</code> branches. All connections are **on** by default, so remove the ones you don't need; keep the network on “Trusted”; protect the main branch so that the connected account can't bypass the protection. The organization owner can turn routines off entirely.

### claude -p {#headless}

```bash
claude -p "summarize the changes in this diff"

# a structured answer that follows a schema
claude -p "list the module's functions" --output-format json \
  --json-schema '{...}' | jq '.structured_output'

# unattended: only what was allowed in advance
claude -p "fix the linter errors" --permission-mode dontAsk \
  --allowedTools "Edit,Bash(npm run lint *)"
```

**An important difference from the course.** On its own, <code>-p</code> **loads the same context as a normal session**, including hooks from the repository's <code>.claude/settings.json</code> and connections from its <code>.mcp.json</code>, and does so **without the trust dialog**. Only the <code>--bare</code> flag skips them. For CI on someone else's or unchecked code, use <code>--bare</code> and pass what you need explicitly with flags (<code>--settings</code>, <code>--mcp-config</code>). <code>--bare</code> gives a reproducible setup, not an identical model answer, and requires an API key. If you have no API key, there is the <code>--setting-sources user</code> flag: with it Claude Code reads neither the project's settings nor its <code>.mcp.json</code>.

A run succeeds when it exits with code 0; for <code>--output-format stream-json</code>, also check the list of denied actions.

## Pull requests: Code Review and GitHub Actions {#github}

<div class="rai-cards rai-cards--2">
<article><h3>Code Review</h3><p>A managed PR review service: an administrator turns it on; it runs when a PR is opened, on every push, or on <code>@claude review</code>. It analyzes the changes against the whole codebase and leaves comments with a severity level. It <b>never approves or blocks</b> a PR. Fix things locally: <code>/code-review --fix</code>. Not available in zero data retention and HIPAA configurations.</p></article>
<article><h3>GitHub Actions</h3><p><code>/install-github-app</code> (needs repository administrator rights), the <code>anthropics/claude-code-action</code> action. Runs on an <code>@claude</code> mention, or on your own prompt and schedule. For reports, use read-only tools with no questions.</p></article>
</div>

Rules for Actions: secrets only through GitHub Secrets or identity federation; minimal permissions for GitHub Actions workflows; a turn limit with <code>--max-turns</code>, timeouts and a cap on concurrent runs; merge only after review by a person.

## Reviewing unattended work {#trust}

<ol class="rai-principles">
<li><b>Review depth matches the degree of autonomy</b><span>The less you saw, the stricter the check.</span></li>
<li><b>The diff first, then the summary</b><span>The summary is written by whoever did the work; the diff doesn't lie. First the files from the plan, then everything outside the plan.</span></li>
<li><b>/code-review and a “cold” subagent</b><span>A fresh look with no memory of how the code was written. Levels: <code>/code-review low</code>, <code>/code-review high</code>.</span></li>
<li><b>Tests as a gate</b><span>A Stop hook with tests plus PostToolUse with a linter and type checking; code 2 sends the error back to Claude.</span></li>
<li><b>Have the tests been weakened?</b><span>Skipped, deleted and “softened” tests get a check of their own.</span></li>
<li><b>For runs from scripts</b><span>Look at the JSON result and the exit code, not just the text.</span></li>
</ol>

### Three piles of findings {#piles}

Sort review findings into three piles: **fix now / ask why / leave**. A reviewer asked to look for problems will always find some; if you chase every one, the code grows needless abstractions. Accept what affects correctness and the requirements.

Good prompts:

```text
Review the changes you just made. Report the problems, don't fix anything yet.

You said isValidEmail doesn't trim whitespace, but line 4 calls trim(). Check again: does the finding still stand?

Fix the first finding. Then run the tests and show the output.
```

## Parallel work and plugins {#scale}

### Background sessions (Agent view) {#agent-view}

<code>claude agents</code> is one screen with all background sessions and their status (working, waiting for an answer, finished, error). <code>claude --bg --name "flaky-test-fix" "…"</code> starts one in the background. Note: a background session works in a separate copy of the repository and **can commit, push and open a draft PR on its own** (except pushing to main, force-pushing and merging). If git must stay under manual control, write that in CLAUDE.md. Each background session draws on your usage limit separately.

### Dynamic workflows {#workflows}

For tasks of tens or hundreds of steps, Claude writes a workflow plan that runs many subagents: “keep fixing until <code>npx tsc --noEmit</code> passes or two rounds make no progress”, “check every changed file and give one summary”. The built-in <code>/deep-research question</code> does research. Progress is in <code>/workflows</code>. The plan is shown before the run; the limit is 16 agents at once; large runs come with a usage warning. The organization can turn workflows off.

### Subagents in parallel {#fan-out}

“Explore the authorization, database and API modules in parallel, with separate subagents”; <code>/batch instruction</code> splits a change across 5–30 subagents, each in its own copy. Try it on 2–3 files first, then on everything. For more on subagents, see [Subagents in Claude Code](page:kb/guides/claude-code-subagents).

### Plugins {#plugins}

A plugin bundles skills, subagents, hooks and connections: <code>/plugin install github@claude-plugins-official</code>; a team marketplace is added with <code>/plugin marketplace add your-org/claude-plugins</code>. **A plugin runs code with your rights**, and its hooks are added to yours. Version plugins like dependencies.

## Safety in a regulated organization {#safety}

<ol class="rai-principles">
<li><b>-p without --bare runs the repository's settings</b><span>Hooks and connections start without the trust dialog. For CI, use <code>--bare</code> and explicit settings.</span></li>
<li><b>Fix the default mode</b><span>Newer versions start in Auto. Set the mode in the organization's settings and forbid Bypass; Bypass only in an isolated container with no network, as an unprivileged user.</span></li>
<li><b>Auto checks intent, not correctness</b><span>Define trusted infrastructure and an internal package registry; cover correctness with tests in a Stop hook.</span></li>
<li><b>Know the weak spots of hooks</b><span>Code 1 doesn't block, a timeout lets the action through, Stop is lifted after eight blocks.</span></li>
<li><b>Routines run in Anthropic's cloud</b><span>Decide whether that is acceptable for your repositories; turn off unneeded connections; protect the main branch.</span></li>
<li><b>Background sessions work with git on their own</b><span>If you need manual control, forbid it in CLAUDE.md.</span></li>
<li><b>GitHub Actions with minimal permissions</b><span>Secrets through Secrets, limits on turns and time, merge only after a person has reviewed.</span></li>
<li><b>Plugins only from allowed marketplaces</b><span>Set the list of allowed marketplaces and the limits on hooks in the organization's settings.</span></li>
<li><b>Undo means git</b><span>Rewind in Claude Code doesn't undo shell commands or edits by background subagents.</span></li>
<li><b>Watch the usage</b><span>Background sessions and workflows use up the limit several times over; organizations can set limits on workflows.</span></li>
</ol>

All organization-level settings are in the Claude Code documentation: the Permission modes, Hooks, Routines, GitHub Actions and Code Review pages. The links are in the Reference section: [Anthropic learning](page:reference/anthropic).
