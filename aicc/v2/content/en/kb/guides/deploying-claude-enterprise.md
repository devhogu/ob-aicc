---
title: "Rolling out Claude in an organization: five decisions — the complete guide"
summary: How a leader and the owner of an organization in Claude can make the five decisions that shape a rollout (structure, access, governance, spend and visibility), and what position a regulated department needs.
category: For leaders
level: deep
minutes: 35
order: 6
featured: true
layout: course
tags: rollout, enterprise, administration, groups, access, spend, audit, data retention, regulation
source: "Deploying Claude Enterprise with Confidence — Claude Academy, проверено по Справочному центру Claude"
source_en: "Deploying Claude Enterprise with Confidence — Claude Academy, checked against the Claude Help Center"
source_url: https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence
source_hash: c9f7fdf66a5f
---

This guide is for people who decide **how** Claude will be brought into the organization: the owners of the organization in Claude (the main administrators of its account), IT, information security, finance and heads of departments. It retells Anthropic's course on rolling out Claude Enterprise and has been checked against the Help Center.

By the end, you will be able to go through the five rollout decisions (structure, access, governance, spend, visibility), understand what position a regulated department needs, and read adoption signals. For a head of department the most important parts are “Access”, “Spend”, “Adoption signals” and “Regulated department”: they show what to ask for in your pilot and what to agree with IT, security and the budget owner.

The course teaches not which buttons to press but **judgment**: which decisions to make, in what order, and who makes them. The course's running example is a fintech company with five departments, one of which operates under financial regulation. In a bank the whole organization operates under regulation, so read the “Regulated department” part with particular care.

## The frame: five decisions in order {#frame}

<ol class="rai-flow">
<li><b>Structure</b><span>organizations, groups, identities</span></li>
<li><b>Access</b><span>which capabilities and connectors for which groups</span></li>
<li><b>Governance</b><span>skills, plugins, projects, instructions</span></li>
<li><b>Spend</b><span>limits, models, how to raise them</span></li>
<li><b>Visibility</b><span>logging, retention, audit, adoption signals</span></li>
</ol>

The order is strict: each decision sets the bounds for the next, and visibility measures the result of all four.

### Four settings that are hard to undo {#irreversible}

- **<span class="en">Domain claiming</span>**: the organization confirms that an email domain belongs to it, and accounts on the corporate email domain come under its management. This is irreversible.
- **The number of organizations**: merging or splitting means reconnecting every employee affected.
- **Mapping directory groups to roles**: which groups from the corporate employee directory get which roles in Claude. A change immediately changes access for everyone it affects.
- **Data retention period**: you can change it, but what was deleted under a short period can't be brought back.

### The rollout objective {#objective}

One objective for the whole organization, in two halves: **what success looks like** and **which constraints must not be broken**. In the course's example: “all five departments use Claude daily by the end of the quarter, without a single security escalation from the regulated department”. And a rule: if a choice speeds up the rollout but risks such an escalation, take the slower path.

## Owners and preparation {#owners}

“A decision without an owner is one of the fastest ways to stall a rollout.” The owner is chosen by responsibility, not by job title.

| Decision | Who usually decides |
| --- | --- |
| Structure | the owner of the organization in Claude, the user directory team, IT |
| Access | the owner, team leads; connectors with write access are signed off by the data risk owner |
| Governance | the owner, the adoption team, security |
| Spend | the owner and whoever controls the budget |
| Visibility | the owner and the data risk owner (security, legal, compliance) |

Two decisions usually go beyond IT: **spend** goes to the budget owner, **visibility** to the data risk owner.

### Required preparation {#prereq}

<ol class="rai-principles">
<li><b>Two owners, assigned directly</b><span>Before single sign-on is set up, as insurance against losing access. The primary owner is kept out of day-to-day administration.</span></li>
<li><b>Single sign-on enforced</b><span>Employees sign in to Claude only through their corporate account; the organization's user directory is connected.</span></li>
<li><b>Automatic user provisioning</b><span>Employees and their groups come from the directory.</span></li>
<li><b>Domain verified and claimed, last</b><span>After everything else. There are 30 days for personal accounts on the corporate domain to move over; warn employees in advance.</span></li>
</ol>

Give each administrator the least powerful role that is enough for their work.

## Structure: one organization, well-designed groups {#structure}

**By default, one organization.** Splitting is worth it only if there is a separate contract with Anthropic; user directories that can't be merged; or data that a regulator or contract requires to be **demonstrably** isolated, and only after compliance has confirmed that the organization boundary meets that requirement. Separate limits or a stricter regime for one department are handled with groups, not a new organization.

### Groups {#groups}

Almost all settings are tied to groups, not to people. If you want a setting “just for these three people”, you need another group.

- **The union rule:** if a person is in several groups, their permissions add up; a narrow group can't take away what a broad one grants.
- That is why a hard boundary needs **a separate group whose members are not in the broad one**.
- A typical choice is a mixed scheme: groups by department plus separate groups for regulated functions.

## Access: capabilities and connectors {#access}

### Capabilities {#surfaces}

Chat, Cowork, Claude Code, Claude in Office: each group has its own set. Two levels decide: the organization switch (the ceiling) and the role's permissions. A default model can be set for the organization and for a role.

- Options: broad first, specialized as needed; a pilot, then expansion; in phases after review.
- In the course's example, the regulated department **got Claude Code only once session logging was ready**.
- Adding a capability is cheap; taking it away is expensive, because people's work breaks.

### Connectors {#connectors}

Three levels of permission: the organization turns a connector on, a role receives it, an employee connects their own account. Claude gets the employee's permissions in that system.

- **Read-only by default**, and only for the groups whose work lives in that system.
- Write access comes in phases and **with the data risk owner's sign-off**. For each write operation: always allow, ask, or block.
- Announce every connector at launch; requests for new ones go to the access owner.

## Governance: skills, plugins, projects {#governance}

The risk is sprawl: dozens of nearly identical skills, unchecked procedures that everyone assumes were checked, projects with sensitive data open to the whole organization.

| Position | How it works | When |
| --- | --- | --- |
| Create freely, share after review | sharing within groups is on, publishing goes through a reviewer | most organizations |
| Centralized | sharing is off, only the owner distributes skills | a strict environment |
| Fully open | everything is on | rarely |

- For regulated groups: **approval first**, use after.
- The organization's shared instructions are two or three lines on style and rules: they apply in every conversation.
- You can loosen the policy at any time; tightening it doesn't remove what has already been published, so that will need reviewing.

For skills and how to review them in detail, see [Claude skills: the complete guide](page:kb/guides/skills-complete-guide).

## Spend: limits and levers {#spend}

Three levels of limits: the organization ceiling, a limit per group member, personal exceptions. If a person is in two groups, a setting decides which limit applies, the higher or the lower.

- A limit that has been reached is a pause, not a failure: the employee sends a request to raise it. The organization owners approve it, but someone else controls the budget, so **define the escalation procedure in advance**.
- If you don't know the usage profile, start with a strict limit and recalculate from the first month's data, rather than raising it in small steps.
- If exceptions multiply, those people need their own group.
- Chat uses little; Claude Code and Cowork use more per task.

### Levers that don't change limits {#levers}

- **The default model and effort level** affect spend more than most limit changes. An example from the course: a department hit its limit because the most powerful model was doing routine summaries; the default model was lowered, and the same volume of work fit within the old limit.
- Organization instructions: short answers, only the files needed, a high effort level only when it is really needed.
- Skills and projects for reuse.

Review spend monthly, and more often at the start. **For a regulated group, a separate review with its own owners.**

## Visibility: logging, retention, audit {#visibility}

**Set it up before people get access.** A period without logging is a period for which there will be no record: turning it on retroactively doesn't work.

- **Compliance API**: programmatic access through which the organization exports conversation and file content and audit events into its own systems; the primary owner turns it on. Whether it meets a specific regulatory requirement is for legal and compliance to decide. The feed goes into the existing security review process **with an assigned reader**: “a log that nobody reads is not a control”.
- **Audit logs**: metadata only, without the text of prompts.
- **Retention period**: indefinite by default; the minimum custom period is 30 days; the setting covers the whole organization. Shortening the period means erasing history, so agree on the period once and in advance.
- **<span class="en">Inference hooks</span>** (beta, Enterprise): every prompt goes to the organization's security server before it is answered, for example to protect against data leaks.

What isn't in the course but is in the Help Center: a custom retention period **does not apply** to Claude Tag, Claude Design, managed agents or the cloud features of Claude Code; the Compliance API doesn't cover Claude Code cloud sessions or access through cloud providers. Take this into account in your assessment.

## Adoption signals {#adoption}

This part covers how to tell from a few simple indicators whether Claude is taking hold in a department, and where to look for the cause if it isn't. It is useful for a leader running a pilot or a rollout in their own area.

Reach (how many people use it) and depth (how intensively) are [[leading-indicator|leading indicators]]: they show up earlier than a measurable result. They are **a diagnostic, not a target**: as soon as a signal becomes a quota, people start working for the number rather than the result.

| Signal | If it's low, look at |
| --- | --- |
| Active users by group | access and awareness |
| Coming back every week | training and expectations |
| Conversations per person | whether the capabilities and connectors fit the work |
| Skills and projects in use | the governance position |
| Connector usage | the set of connectors |

The pace goal is concrete: “every group with access comes back weekly for eight weeks”, not “good adoption soon”. An example from the course: a department was stuck at 10% because its staff hadn't been trained, and the cure was training, not settings.

**Try it now.** Choose two signals from the table for your department and write a pace goal in one sentence, as in the example above. Agree with the owner of the organization in Claude on who will send you these signals for your group and how often. A low signal is a reason to talk with the team about the cause, not to hand down a quota.

## Regulated department: one position {#regulated}

For a regulated function the course proposes **one agreed position, not five exceptions**:

<ol class="rai-principles">
<li><b>A separate group</b><span>Its members are not in the broad groups, so the union rule adds nothing.</span></li>
<li><b>The same capabilities, except development</b><span>Claude Code only once session logging is ready.</span></li>
<li><b>Read-only connectors</b><span>All others are off for the group.</span></li>
<li><b>Approval first</b><span>Skills and plugins after review.</span></li>
<li><b>The normal limit, with every increase reviewed</b><span>With a separate budget owner.</span></li>
<li><b>Retention period set by regulatory requirements</b><span>For the whole organization, with the Compliance API and an assigned reader.</span></li>
</ol>

“If the whole organization is regulated, this set is your baseline configuration.”

The course's final steps: confirm the four hard-to-undo settings (or hand them to an owner with a decision date); for each open question, write down what is blocking it, what is needed to unblock it and the decision date, since “an owner's name on its own is not a plan”; then launch group by group in the order structure → access → governance → spend → turning on logging → launch.

### When a new product appears {#new-product}

Three questions for any new capability: **who should get it? what will pass through it? does it change the risk** (a new class of data, a new degree of independence, new people)? If any answer is “yes”, go to the data risk owner. In the course's example, Claude Tag (Claude in Slack) was turned off for the regulated department, and the risk owner signed off on that decision.

For how people and agents work together within teams, see [People and agents on one team](page:kb/guides/human-agent-teams). Links to the course and the Help Center are in the Reference section: [Anthropic learning](page:reference/anthropic).
