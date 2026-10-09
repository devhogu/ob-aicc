---
title: "People and agents on one team"
summary: How to move from “everyone has their own assistant” to a team where people and AI agents work together. Three properties of a team agent, four principles, five readiness questions and a plan for the first two weeks.
category: For leaders
level: basic
minutes: 12
order: 7
layout: course
tags: agents, team, collaboration, roles, trust, pilot, north star
source: "Building Effective Human-Agent Teams — Claude Academy"
source_url: https://academy.claude.com/courses/building-effective-human-agent-teams
source_hash: efb90d5e6d0b
---

A guide for leaders and members of teams where Claude is already used individually. It retells Anthropic's course on how people and agents work together. After it, you will be able to assess your team's readiness with five questions, plan the first two weeks of a pilot, and bring an agent into the work so that trust in it grows step by step.

An [[ai-agent|AI agent]] is an AI that doesn't just answer in a conversation but carries out multi-step work on its own with the help of tools: it reads files, searches systems, prepares documents. Cowork, for example, works this way. A personal assistant speeds up one person, but the knowledge stays in that person's conversations. The next step is **an agent as a member of the team**.

## Why work together {#why}

When everyone has their own assistant, four people ask similar questions and get slightly different answers: that is **parallel work, not teamwork**. In a shared space (a shared channel or a shared project) a question is asked once, everyone reads and builds on the answer, and what is written becomes team knowledge that a newcomer can read on their very first day.

The faster a team grows, the harder scattered context hits the quality of the agents' work.

**Exercise.** Write down three questions your team asks every week, for example “what's the procedure for this operation”, “where's the current form”, “what changed in the rules”. Who else asks them? What breaks when the answers differ? What would one shared agent change?

## A tool or a teammate {#teammate}

An ordinary assistant works on your behalf and knows what you know. A team agent **works under its own name**, and the team itself decides what it has access to. Three essential properties:

<div class="rai-cards rai-cards--3">
<article><h3>Its own account</h3><p>Its own permissions and tools, not the manager's login. And a clear history of its work, which lets you tune the agent over time.</p></article>
<article><h3>Shared memory</h3><p>It remembers goals and decisions between conversations, so you don't have to explain the context again every time.</p></article>
<article><h3>Shared context</h3><p>It sees the team's spaces: decisions, changes, agreements.</p></article>
</div>

An example from the course of why its own account matters: an agent working under a manager's login opens the billing folder. “It can open everything the manager can. Nobody decided that.” For a financial organization this is a ready illustration of the principle of **least privilege**: the agent has exactly the access its work needs.

**Check.** Does your tool work under its own name? Does it remember goals between conversations? Does it see the team's shared spaces?

## Four principles of a strong team {#principles}

<ol class="rai-principles">
<li><b>Clear roles</b><span>One list of work for people and agents; each piece of work has one owner.</span></li>
<li><b>A written goal</b><span>A “North Star”: one measurable team goal in one sentence. People set it and pin it where the agent will read it.</span></li>
<li><b>The right access to information</b><span>“If it isn't written down and accessible, it doesn't exist.” An agent without access works superficially, guesses or makes mistakes.</span></li>
<li><b>Gradual trust</b><span>Independence in proportion to proven reliability, extended deliberately and separately for each type of task.</span></li>
</ol>

Teams with agents work faster, and that is exactly why misalignment and mistakes cost more.

### Three modes of owning the work {#modes}

| Mode | Example from the course | Risk |
| --- | --- | --- |
| People do it | the “launch / don't launch” decision | slow, but judgment stays with people |
| The agent drafts, a person decides | replies to customers, feedback analysis | the draft can “anchor” the decision, so a person accepts it without thinking it through |
| The agent on its own | the morning summary | the cost of a mistake must be low |

The rhythm of handing over work: **the agent drafts → a person decides and refines → the agent releases the final version.**

Lessons from the course's simulation, in which a team worked with agents:

- An agent that answered users on its own promised a fix date that nobody had agreed.
- An agent announced the launch decision on its own, and the post had to be taken down.
- Even a **draft** “we're launching” recommendation, published in the morning, made half the team consider the question settled.
- And manual checking where there is nothing left to catch is a signal that it's time to give the agent more independence.

**Judgment on important decisions and external promises stay with people.** In a bank this means, for example, a decision on a customer's application or a reply to an outside organization.

## Is the organization ready {#readiness}

Five readiness questions. Go through them with your team: everyone rates each item from 1 to 5, then discuss where the ratings differed.

1. Is information open and searchable, or is it in personal documents and correspondence?
2. Is it written down who owns what, including agents?
3. Does every member, including agents, have the tools to do the work?
4. Can the agent's key work be checked before a person sees it: against a rubric (a list of criteria for “done”), with a test or by a second agent?
5. Is there a written goal?

Start with the weakest item: one change per area, each change with an owner and a success criterion, a plan for two weeks. If all the ratings are high, double-check and start with a minimal pilot: one space, one agent, one visible piece of work.

## Plan for the first two weeks {#start}

“Start soon, but start small.”

<ol class="rai-principles">
<li><b>One space, 3–5 people, one agent</b><span>Ideally a team with high trust.</span></li>
<li><b>Open by default</b><span>A decision made in a meeting or in private messages is posted in the shared space the same day.</span></li>
<li><b>A list of work</b><span>The agent proposes, people decide; each piece of work has one owner.</span></li>
<li><b>The goal is written down and pinned</b><span>Where the agent will read it.</span></li>
<li><b>One visible piece of the agent's work</b><span>For example, a morning summary for the team; for the first few days a person checks it.</span></li>
<li><b>A rubric for “what done means”</b><span>A short list of criteria for each task. Nothing builds trust faster.</span></li>
<li><b>Trust, step by step</b><span>After several successes in a row, extend the agent's independence on that task.</span></li>
<li><b>Explained it twice? Write it down</b><span>As an instruction or a <a href="page:kb/guides/skills-complete-guide">skill</a>.</span></li>
<li><b>A weekly retro</b><span>A short review of “what worked, what to change”, with people and agents; the agents save the conclusions for other agents.</span></li>
</ol>

“Most of these habits helped teams long before agents, but with agents, skipping them has become more costly.”

Tools for a team agent are Claude Tag (Claude in Slack; see [Claude Tag](page:kb/guides/claude-tag)) or managed agents on the Claude platform. Use them only if they are approved in your organization. Until you have a team agent, many of these habits can be started in a shared Claude project the team uses: a written goal, one owner for each piece of work, a “done” rubric. How the organization should make decisions about access and risk: [Rolling out Claude in an organization](page:kb/guides/deploying-claude-enterprise).
