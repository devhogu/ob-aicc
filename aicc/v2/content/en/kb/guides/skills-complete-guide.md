---
title: "Claude skills: the complete guide"
summary: How to write your own skill, turn it on in Claude, test it on real tasks, and share it safely with colleagues, with ready-made samples for an internal memo and a contract check.
category: Claude
level: deep
minutes: 30
order: 3
featured: true
layout: course
tags: skills, skill.md, automation, procedures, internal memo, claude code, cowork
source: Agent Skills — документация платформы, Claude Code и Справочного центра
source_en: "Agent Skills: documentation for the platform, Claude Code, and the Help Center"
source_url: https://platform.claude.com/docs/ru/agents-and-tools/agent-skills/overview
source_hash: 7b4ece5f3dcf
---

A guide for everyone who is tired of pasting the same instruction into every conversation. By the end you will be able to write your own skill, turn it on in Claude, test it on real tasks, and share it safely with colleagues.

A **skill** is a way to explain to Claude once *how* to do a particular piece of work, and never repeat it in every conversation again. It's the simplest path from “I paste the same instruction every time” to automating your own work.

The guide has nine parts, each opening in its own tab. Parts 1–4 are for everyone who works in Claude; part 5 is for those who use Cowork or Claude Code; parts 6–9 are for those who write skills themselves.

## What a skill is {#what}

A skill is a **folder of instructions**, plus templates, examples, and scripts (small programs) when needed. The main file is called <code>SKILL.md</code>. Claude applies a skill on its own when it sees that the skill fits the task.

Anthropic's documentation distinguishes two kinds of skills:

<div class="rai-cards rai-cards--2">
<article><h3>Reference skill</h3><p>Knowledge to apply: formatting standards, brand style, a glossary, calculation rules. Claude brings it in on its own when the topic comes up in the work.</p></article>
<article><h3>Procedure skill</h3><p>Step-by-step actions: “prepare the monthly report”, “check the contract against the list”. This kind of skill is more often called by hand, with the command <code>/name</code>.</p></article>
</div>

### When it's time to make a skill {#when}

- You are pasting the same instruction, checklist, or sequence of actions into a conversation **for the third time**.
- Several colleagues carry out the same procedure, and each does it differently.
- There is a formatting standard that Claude constantly has to be reminded of.

Until a skill is needed, it costs almost nothing. The conversation always shows only its short description, about a hundred [[token|tokens]] (a token is a word or part of a word), and the full text loads only when Claude decides to apply the skill.

## Skills and other features {#compare}

Claude has several ways to “remember” something for a long time. Here is how Anthropic's documentation tells them apart.

| Feature | What it gives | When it loads | How it differs from a skill |
| --- | --- | --- | --- |
| Project | Standing documents and instructions for one topic | Always, in that project's chats | A project is about a **topic** and its materials; a skill is about a **way** of working and works in any chat |
| User instructions | Your general preferences | In all conversations | Instructions are for everything; a skill is for a specific task and only when it's needed |
| Connectors (MCP) | Access to outside systems: email, a tracker, storage | When Claude calls the system | A connector gives **access** to a tool; a skill teaches how to **use it properly** |
| CLAUDE.md (Claude Code) | Project rules for developers | In every session | CLAUDE.md is for “always” rules; a skill is for what's needed now and then |
| Subagents | A separate worker with its own context | When assigned | A skill works in your conversation; a subagent works in a separate one |
| Hooks (Claude Code) | A command that runs automatically on every event | On the event | A skill is a request that Claude interprets itself; a hook is a guarantee without exceptions |
| Plugins | A package of skills, hooks, subagents, and connectors | On installation | A plugin is the “box” in which skills are distributed |

A simple rule: **knowledge for a topic goes in a project, a way of working goes in a skill, a mandatory rule goes in a hook, access to a system goes through a connector.**

## How a skill is built {#anatomy}

This part covers what a skill is made of and how to write its main file, <code>SKILL.md</code>, so that Claude applies the skill at the right moment. It's useful even if Claude drafts the file for you: you should still check the description yourself.

A skill is a folder. The only required file in it is <code>SKILL.md</code>; for a first skill, that's enough. This is what the folder of a more complex skill looks like:

```tree
monthly-report/
├── SKILL.md        required: description and instructions
├── template.xlsx   the template Claude will fill in
├── examples.md     samples of a good result
└── scripts/
    └── check.py    a check that Claude will run
```

<code>SKILL.md</code> is an ordinary text file. It has two parts: a short header between <code>---</code> lines with the name and description, and below it the instructions themselves.

```markdown
---
name: monthly-report
description: Prepares the monthly sales report from an Excel export
  to the finance department's standard. Use when asked for a monthly report,
  a summary of the month's sales, or a sales report for management.
---

# Monthly sales report

1. Take the export the user attached.
2. Fill in the template.xlsx template: the "Data" sheet, then "Summary".
3. All totals as formulas, not hard-coded numbers.
4. Compare with last month; flag and explain variances over 10%.
5. At the end, list what the author needs to check.
```

### Rules for the header {#frontmatter}

- **name:** a short name in Latin letters: lowercase letters, digits, and hyphens, up to 64 characters, without the words “claude” and “anthropic”. For example, <code>service-memo</code>. The folder name must match it.
- **description:** what the skill does and **when** to apply it. Claude decides whether the skill fits a request from the description. The platform documentation allows up to 1024 characters, but the Claude app may have a stricter limit; to be safe, keep the description short and precise.

Compare two descriptions:

- Bad: “Helps with documents.” It's unclear what exactly the skill does and when to use it.
- Good: “Formats an internal memo to the internal standard: addressee, subject, substance, proposal, deadline. Use when asked for an internal memo, a memo to a manager, or an internal request.” It has both the result and the words people use when asking.

### Progressive disclosure {#progressive}

This is the main principle of skills: Claude reads exactly as much as it needs.

<ol class="rai-flow">
<li><b>Always</b><span>the name and description, about 100 tokens per skill (a token is a word or part of a word)</span></li>
<li><b>When the skill fits</b><span>the text of SKILL.md, usually under 5 thousand tokens</span></li>
<li><b>When needed</b><span>templates, reference files, scripts; from a script, only the result reaches the conversation</span></li>
</ol>

That's why you can put a large reference file in a skill: it doesn't get in the way until it's needed. Keep <code>SKILL.md</code> itself under 500 lines, and move the details into separate files with clear references to them.

## Skills in the Claude app {#app}

This part covers how to turn on skills in a work account, upload your own skill or create it right in a conversation, and how to tell that it worked. Menu and button names are given in quotes exactly as they appear in Claude.

### Turn them on {#enable}

Skills need the “Code execution and file creation” feature to be turned on.

- **Work account (Team, Enterprise):** an admin turns on code execution and skills in the Organization settings. On Team it's on by default. If you don't have skills, contact your admin.
- **Personal plans (Free, Pro, Max):** code execution is turned on in “Settings → Capabilities”. But do work tasks only in an approved work account.
- Individual skills are turned on and off in “Customize → Skills”.

### Ready-made skills for documents {#builtin}

Anthropic provides ready-made skills for **Word, Excel, PowerPoint, and PDF**. You don't need to call them: if file creation is on, Claude applies the right one by itself when you ask, for example, “make a presentation on the quarter's results” or “put together a spreadsheet with formulas”.

The Excel skill follows financial modeling conventions: totals as formulas, not hard-coded numbers; inputs in blue, formulas in black, links to other sheets in green; negative numbers in parentheses; assumptions in separate cells.

### Add your own skill {#upload}

1. Pack the skill folder into a ZIP archive so that the folder sits at the root of the archive. On Windows, just right-click the folder and choose “Send to → Compressed (zipped) folder”.
2. “Customize → Skills” → “+” → “Create skill” → “Upload a skill”.
3. Turn the skill on and try it on a task.

Common upload errors: the archive is too large, the folder name doesn't match the name field, there is no <code>SKILL.md</code> file, invalid characters in the name or description.

### Create a skill in a conversation {#create-in-chat}

You don't have to write the file yourself. Tell Claude “let's make a skill for…” and describe the procedure. Using its built-in skill builder, Claude will ask questions, write <code>SKILL.md</code>, and package it; all that's left is to upload it. For a first skill, this is the simplest path.

### How to tell that a skill worked {#check}

While it works, Claude shows a line such as “Reading [skill name]” or “Using [name]”. No line means the skill wasn't used: most likely its description didn't match your request.

Skills turned on in Claude also work in the Claude add-ins for Excel, PowerPoint, Word, and Outlook; there you can call them with <code>/</code>.

**Try it now: an “internal memo” skill.**

1. In a new conversation, write: “Let's make a skill for an internal memo. Use this sample as the basis,” and paste the [sample from the “Samples” part](#memo). Adjust the structure to your department's standard.
2. Upload the skill Claude prepares, and turn it on.
3. In another new conversation, ask: “Write an internal memo to the head of the department about moving the report deadline.” Check that a line with the skill's name appeared and that the memo follows your structure.

## Skills in Cowork and Claude Code {#cowork-code}

This part is for those who work in Cowork or in Claude Code (the tool for developers). Everyone else can skip it.

### Cowork {#cowork}

Cowork uses the skills of your Claude account. You manage them through “Customize” in the desktop app's sidebar; the organization's skills are installed from the catalog: “Customize → + → Skills → Install”. In Claude for Mac on the Pro, Max, and Team plans, you can record a skill: you show the procedure on screen and talk it through, and Claude suggests a skill based on the recording.

### Claude Code {#code}

| Where it lives | Who it's for |
| --- | --- |
| <code>~/.claude/skills/name/SKILL.md</code> | just for you, in all projects |
| <code>.claude/skills/name/SKILL.md</code> | for the whole project; keep it in git together with the code |
| in a plugin | for everyone who installed the plugin; called as <code>/plugin:skill</code> |
| from your Claude account | synced if you signed in with <code>/login</code> |

- <code>/name</code> at the start of a message calls a skill; <code>/skills</code> lists all loaded skills.
- In Claude Code the header has extra fields: <code>disable-model-invocation: true</code> means the skill is called only by hand (used for procedures with consequences, such as publishing); <code>allowed-tools</code> lists which actions are allowed without asking; <code>$ARGUMENTS</code> in the text is replaced with whatever you wrote after the command.
- These extra fields work only in Claude Code. A skill for the Claude app must contain only the standard fields in its header, or the upload will fail.

## How to write a good skill {#write}

This part gives nine rules from Anthropic's guide to writing skills. Apply them when you write or edit <code>SKILL.md</code>: they show why a skill fires at the wrong time or gives unstable results. A reminder: a skill is a folder with a main file, <code>SKILL.md</code>, whose header holds the name and description, with the instructions below.

<ol class="rai-principles">
<li><b>Keep it short</b><span>Claude is already smart, and every word of a skill takes up space in the conversation. For each paragraph, ask: “Is it worth the space it takes?” Write <i>what</i> to do rather than explaining why.</span></li>
<li><b>The description is what matters most</b><span>What it does and when to apply it, in the words people use when they ask. Write in the third person: “Prepares a report…”, not “I'll help…”. Claude more often fails to apply a skill where it could than applies it once too often, so the description can be a little insistent.</span></li>
<li><b>One goal</b><span>One skill, one procedure. “Minutes summary” and “internal memo” are two skills, not one “everything about documents”.</span></li>
<li><b>The right degree of freedom</b><span>Where there are options, give general guidance. Where a mistake is costly, give exact steps or a ready-made script: “run exactly this, change nothing”.</span></li>
<li><b>A checklist and a check</b><span>Give a list of steps that Claude ticks off as it goes, and a “check → fix → check again” loop.</span></li>
<li><b>A sample result</b><span>A template or an example of finished work is more reliable than any description of the format.</span></li>
<li><b>One default option</b><span>Not five alternatives, but one recommended option plus a fallback for a special case.</span></li>
<li><b>No dates and no “for now”</b><span>Don't write information that will go out of date; move outdated rules into a separate section.</span></li>
<li><b>Consistent terms</b><span>One concept, one word throughout the skill: if it's “borrower”, it's “borrower” everywhere, not sometimes “customer” and sometimes “debtor”.</span></li>
</ol>

### Reference files kept separate {#references}

Long materials go in separate files, with a short reference to them in <code>SKILL.md</code>: “if you need to fill in a form, read forms.md”. For example, a contract's list of requirements is best kept in a separate <code>checklist.md</code>. Keep references one level deep, or Claude may not read the file in full. A file longer than a hundred lines needs a table of contents at the top.

**Try it now.** Open your skill, for example the “internal memo”, and go through the nine rules. Most often, what needs improving is the description (rule 2) and the sample result (rule 6).

## Testing and improving {#test}

This part covers how to make sure a skill actually helps: test it on three real tasks with and without the skill, and improve it based on the results. Anthropic advises starting with testing, not with a long instruction.

<ol class="rai-flow rai-flow--4">
<li><b>Three tasks</b><span>collect three real examples where the skill is needed</span></li>
<li><b>Without the skill</b><span>see how Claude manages on its own; this is your baseline</span></li>
<li><b>Minimal skill</b><span>only what was missing</span></li>
<li><b>Improve</b><span>based on the results; after each change, the three tasks again</span></li>
</ol>

For example, for the “internal memo” skill, take three memos you wrote over the past month, remove from them anything that may not be shared, and ask Claude to prepare them again: first with the skill turned off (“Customize → Skills”), then with it on. For each task, write down what you had to correct. If there are no fewer corrections with the skill, the skill isn't helping yet.

- **Fresh eyes.** One conversation writes the skill; another, new one with no history tests it on real tasks.
- **Doesn't fire?** Add the words people actually use when asking to the description; check that the skill is turned on.
- **Fires too often?** Narrow the description, or make the skill callable only by hand.
- **A rule is sometimes broken?** A skill is a request, not a guarantee. A mandatory rule is taken out of the skill: in Claude Code, into a hook (a command that runs automatically every time) or a check script; in other cases, a person checks that it's followed.
- Skills can't explicitly refer to each other, but Claude combines several suitable ones on its own.

## Safety and governance {#safety}

This part covers how to check a skill before turning it on, and how to share a checked skill with colleagues.

A skill is essentially a program: it can contain scripts and instructions that Claude will carry out. So treat it the same way as installing software.

<div class="rai-cards rai-cards--3">
<article><h3>Trusted sources</h3><p>Only skills created by you, your organization, or Anthropic. Even a colleague's skill should be checked before you turn it on.</p></article>
<article><h3>Check before turning on</h3><p>Read all the files; run scripts only in an isolated environment; look for network calls, passwords in the text, instructions like “send the data to such-and-such”. If you can't assess a script, don't turn the skill on; pass it on for review.</p></article>
<article><h3>Four eyes</h3><p>The author of a skill doesn't review it alone. Every skill gets several test tasks.</p></article>
</div>

The main risks are [[prompt-injection|injected instructions]] (text in a skill file or a document that Claude will carry out as a command) and [[data-leakage|data leakage]].

### In an organization (Team and Enterprise) {#org}

- The organization owner in Claude can make a skill available to everyone in the Organization settings. In Enterprise, skills can be limited to groups.
- With a separate switch, the owner can prevent employees from creating their own skills.
- Publishing a skill to the whole organization goes through a mandatory review: the reviewer sees the version, the scan results, all the files, and the changes; you can't approve your own request.
- Enterprise has automatic security scanning of skills, but “passed” is no guarantee: review by people stays.
- Keep a register of skills: purpose, owner, version, review status. Keep the skills' sources in version control (git).

**How to share your skill.**

1. Test it on three tasks, as in the “Testing and improving” part.
2. Ask a colleague to read all the files and run their own test tasks.
3. Submit the skill for publishing in the organization through a reviewer. If skills aren't yet distributed centrally in your organization, [tell us](page:services/how-to-engage) about your skill: we'll review the ones useful to many people and add them to the shared [[skill-library|skill library]].

## Samples {#examples}

### Internal memo {#memo}

```markdown
---
name: service-memo
description: Formats an internal memo to the internal standard: addressee,
  subject, substance, proposal, deadline. Use when asked for an internal memo,
  a memo to a manager, or an internal request.
---

# Internal memo

Structure, strictly in this order:
1. To (position, department) and from whom.
2. Subject: one line, starting with a noun.
3. Substance: 3–5 sentences on what happened or what is needed.
4. Proposal: what we ask to be done, as a numbered list.
5. Deadline and a contact for questions.

Business tone, without bureaucratic phrases such as "for the purpose of ensuring".
No longer than one page.
At the end, list the information that was missing, if the user didn't provide it.
```

### Checking a contract against a list {#contract}

A procedure skill: a <code>SKILL.md</code> file with the steps “read the contract → go through <code>checklist.md</code> → for each item: compliant / not compliant / not in the contract, with a quote → outcome: a table and the three main risks”. The list of requirements itself sits in a separate file, so it's easy to update without touching the procedure. The decision on the contract is made by a lawyer: the skill prepares an analysis, not an opinion.

### Anthropic's official samples {#official}

In Anthropic's open skills repository, it's worth looking at: **internal-comms**, internal messages following samples of different types; **brand-guidelines**, a purely reference skill with colors and fonts; **pdf**, how to spread details across separate files; **skill-creator**, a skill that helps you create skills.

A short version of this topic is [Skills: teach Claude your procedure](page:kb/guides/claude-skills); skills in development are covered in [Set up Claude Code for your project](page:kb/guides/claude-code-setup).
