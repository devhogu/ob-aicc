---
title: "Claude Tag: Claude in your team's Slack"
summary: How Claude works as an agent in shared Slack channels. Where to give it work, how to steer it, channel memory and rules, answers without a mention, scheduled tasks, safety, and what a leader should decide before a pilot. Only for organizations where Claude Tag is available.
category: Claude Tag
level: basic
minutes: 10
order: 46
layout: course
tags: claude tag, slack, channels, team, memory, routines
source: "Introduction to Claude Tag — Claude Academy, документация Claude Tag"
source_en: "Introduction to Claude Tag — Claude Academy, Claude Tag documentation"
source_url: https://academy.claude.com/courses/introduction-to-claude-tag
source_hash: 9b01e40961de
---

This guide is for a leader who is deciding whether the team needs an agent in a shared channel, and for the members of such channels. By the end, you will understand how the agent works in shared channels, whose permissions it uses, what happens to the data, and what to decide before a pilot.

<p class="pf-tip"><b>Is it available to you?</b> Claude Tag works only in Slack and only on the Team and Enterprise plans, and is currently in public beta. It isn't available to organizations with <span class="en">Zero Data Retention</span> (ZDR), customer-managed encryption keys (CMEK) or a HIPAA configuration. If your organization doesn't use Slack or Claude Tag isn't turned on, read this guide as background for now: its habits will be useful for any team agent.</p>

Claude Tag is Claude in your team's Slack workspace. You write <code>@Claude</code> and the task, and the answer arrives in a thread. Claude first reads the channel, including messages from before it was added, works with the connected tools and keeps working after you've closed your laptop. To add it to a channel: <code>/invite @Claude</code>.

Three habits from Anthropic's course: **work with Claude as you would with a colleague, work where the team works, extend trust gradually.**

## Where to give it work {#where}

| Where | On whose behalf | Memory | When |
| --- | --- | --- | --- |
| Direct messages | yours, with your connections (email, calendar, files) | visible only to you | personal tasks; check before sending, since everything goes out in your name |
| Public channel | under **its own** account with the channel's tools | channel notes | team work: the best choice by default |
| Private channel | its own account, within the channel's bounds | channel notes only | “the member list is the access list; keep it short” |

The rule: ask where you would ask a colleague. If several places fit, choose a **public channel**: colleagues build on the work, corrections benefit everyone, and setup is done once.

### Important: permissions {#rights}

In team tools Claude acts under its own account, and **any member of the channel** can use its permissions: if the account can change tickets, anyone can ask it to. Your personal connections work in a channel only for your own requests and after you confirm.

**Check.** Ask in the channel “@Claude, what do you have access to here?”, then request one real record and check it against the source.

## How to set a task {#request}

<ol class="rai-principles">
<li><b>The goal and why</b><span>Think about the result, not the steps.</span></li>
<li><b>Inputs and an example</b><span>What to use, and what a good result looks like.</span></li>
<li><b>How to check</b><span>A rubric, links to sources, separating “verified” from “inferred”.</span></li>
<li><b>Priorities</b><span>Which decisions Claude should bring back to you.</span></li>
<li><b>The form of the result</b><span>A message, a table, a document.</span></li>
</ol>

For complex tasks, ask for a plan first. Claude shows its progress in a single checklist message. To correct it, **reply in the thread** rather than editing your original message. Check the result more thoroughly the higher the stakes.

## Channel memory and rules {#memory}

- **Memory** is Claude's notes: “@Claude, remember for this channel: …”, “what do you remember about…”, “forget the note about…”.
- **Channel instructions** are rules on the channel's settings page. They take priority over memory, but they are **not a hard lock**: restrictions are enforced by settings and permissions, not by text.

| Symptom | Cause |
| --- | --- |
| shallow answers | the tools it needs are missing |
| answers things it shouldn't | the channel's role isn't set |
| the same mistake again | nobody said “remember for this channel” |
| stays silent | not turned on in the channel |

## Answers without a mention and standing duties {#proactive}

One channel, one kind of work: that way Claude becomes a specialist in it. Turn on “Respond automatically” and describe in one line what to answer and what to stay out of: a support channel, help on internal rules, a project channel. To turn it off for a thread: <code>!mute</code>.

A **standing duty** is something Claude keeps running for days and weeks: it coordinates, takes responsibility for the result, provides continuity when people change. It brings decisions on deadlines, scope and trade-offs to people, for example in a batch twice a week.

## Scheduled tasks {#routines}

In one message, describe what to read, what to look for, what to post, when, and what to do in edge cases, for example “if nothing needs attention, post nothing”. Treat the first post as a draft, and make corrections by replying in the thread. To list them: <code>!routines</code>. A task belongs to the channel and keeps running even if its author has left.

## Safety {#safety}

- Each thread runs in its own isolated environment; outbound traffic is blocked by default; actions are taken from service accounts.
- **Restrictions written in a task steer Claude but don't prohibit anything**: enforce restrictions outside the conversation, with permissions and settings.
- Editing or deleting messages in Slack doesn't remove them from the record on Anthropic's side.
- During the beta there is no automatic retention period for conversations and memory; the organization's own retention period doesn't apply to Claude Tag.
- An administrator can't see conversations with Claude but can see analytics and activity.

**What a leader should decide before a pilot.**

1. Whether your function needs Claude Tag at all: for a regulated department, the data risk owner decides, taking into account the retention rules above. In the course's example of rolling out Claude Tag, it was turned off for the regulated department (see [Rolling out Claude in an organization](page:kb/guides/deploying-claude-enterprise#new-product)).
2. Which channels to invite it to and who is in them: anything Claude's account can do in a channel, any member can ask for.
3. Which tools and permissions to give the channel's account: start with read-only access.
4. Who is responsible for the channel instructions and the scheduled tasks.

## Nine team habits {#habits}

1. Don't explain again what is already in the channel.
2. Check the result against the source.
3. Keep the work in the channel, not in direct messages.
4. Save corrections to the channel's memory.
5. One kind of work per channel.
6. Set rules for answers without a mention.
7. Turn weekly work into a scheduled task.
8. Every request comes with a goal, sources and a check.
9. One standing duty, with clear decisions that come back to people.

For how people and agents work together on a team, see [People and agents on one team](page:kb/guides/human-agent-teams).
