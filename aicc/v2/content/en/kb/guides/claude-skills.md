---
title: "Skills: teach Claude your procedure"
summary: What a skill is, how it differs from a project and a connector, and how to find the first procedure in your work that is worth writing down as a skill.
category: Claude
level: basic
minutes: 6
order: 42
tags: claude, skills, procedure, automation, project, connectors
source: Claude 101 · Introduction to agent skills
source_url: https://academy.claude.com/courses/claude-101
source_hash: ee5217d94bae
---

This guide is for those who already work with Claude in conversations and projects and notice that they keep explaining the same thing to it over and over. By the end you will be able to tell a skill from a project and a connector, and you will find the first procedure in your work that is worth writing down as a skill.

A **skill** is a written-down procedure: exactly how to do a particular piece of work. For example, “how to format an internal memo using our template” or “how to check a contract against a list of requirements”. Claude applies a skill on its own when it sees that the skill fits the task; you can also call the procedure by hand, by its name.

## Skill, project, or connector? {#vs}

All three save you from repeating yourself, but they solve different problems.

<div class="rai-cards rai-cards--3">
<article><h3>Project</h3><p>About the <b>topic</b>: standing documents and rules for one area of work, for example “Quarterly reporting”. It applies only in that project's conversations.</p></article>
<article><h3>Skill</h3><p>About the <b>method</b>: one procedure that Claude applies in any conversation and project, for example “format a table to the finance department's standard”.</p></article>
<article><h3>Connector</h3><p>About <b>access</b>: it lets Claude into a work system, such as email, calendar, or file storage. A connector opens the door; a skill teaches what to do inside.</p></article>
</div>

They work well together: the “Reporting” project holds the procedures, the “format a table to the standard” skill sets the format, and a connector to the file storage lets Claude fetch the latest data export. Connectors and skills work only if your organization has turned them on.

## What a skill is made of {#parts}

A skill is a folder whose main file is called `SKILL.md`. It contains three things: a short name, a description of when to apply the skill, and the steps themselves. Next to it you can put a template and a sample of finished work, and for complex cases small programs (scripts); a first skill doesn't need them.

Until a skill is needed, Claude sees only its name and description. It reads the full text when it decides to apply the skill, so skills don't clutter every conversation. You don't have to write the file by hand: Claude can draft a skill from your description. How to do that is shown in the [complete guide](page:kb/guides/skills-complete-guide#create-in-chat).

## How to write a good skill {#write}

1. **One procedure.** “Summary of meeting minutes”, not “everything about meetings”.
2. **A clear description of when to apply it.** Claude uses it to decide whether the skill fits the task.
3. **Steps in order.** What to take as input, what to do, what to produce as output.
4. **A sample result.** At least one example of finished work.
5. **A check at the end.** For example: “list what needs to be clarified with the author”.

## Try it now {#try}

Find a candidate for a skill. Think of an instruction you have already pasted into several conversations with Claude: how to format a memo, a contract checklist, the structure of a weekly summary. Write its name in one line and decide, using the cards above: is it a topic (project), a method (skill), or access to a system (connector)? If it's a method, that's your first skill.

We collect skills that are useful to many people in a shared [[skill-library|skill library]]; [tell us](page:services/how-to-engage) about yours.

For details, see the guide [Claude skills: the complete guide](page:kb/guides/skills-complete-guide).
