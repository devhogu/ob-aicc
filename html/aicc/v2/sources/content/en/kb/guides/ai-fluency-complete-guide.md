---
title: "AI Fluency: the complete guide"
summary: The AI Fluency course in our own words. Three ways to work with AI, the four 4D skills and their components, the description–discernment loop, six techniques for setting a task, responsibility, and your personal rules for working with AI.
category: Getting started
level: deep
minutes: 30
order: 5
featured: true
layout: course
tags: ai fluency, 4d, delegation, description, discernment, diligence, literacy, personal policy
source: "AI Fluency: Framework and Foundations — Claude Academy"
source_url: https://academy.claude.com/courses/ai-fluency-framework-foundations
source_hash: d22258676510
---

This guide is for people who already work with an assistant and have read the short version, [Four skills for working with AI (4D)](page:kb/guides/ai-fluency-4d). By the end, you will be able to choose one of three ways of working with AI for your task, run the description–discernment loop, and write down your personal rules for working with AI.

This is a retelling of the AI Fluency course, which Anthropic also uses to train its own staff; the framework was developed by Rick Dakan and Joseph Feller. The course isn't about “the ten best prompts” (advice like that goes out of date quickly) but about skills that last: working with AI **effectively, efficiently, ethically, and safely**. It asks you to stop treating AI as “next-level spell check” and to learn to **think together with it**.

Each tab below is a separate topic, and almost every one has an exercise; you can read them in order or pick and choose. About 30 minutes for everything.

## Three ways to work with AI {#modes}

<div class="rai-cards rai-cards--3">
<article><h3>Automation</h3><p>AI carries out a specific assignment following instructions: a summary, an email, a translation. Good when the result is clear in advance; bad when you yourself don't know what you want. <i>Example: shorten meeting minutes to five points.</i></p></article>
<article><h3>Augmentation</h3><p>AI is a thinking partner: the solution isn't obvious, and you need room to try things. AI doesn't do the work for you; it helps you do it better. <i>Example: think through how to explain a new document-checking procedure to your department.</i></p></article>
<article><h3>Agency</h3><p>AI acts on your behalf: it sorts incoming work, prepares drafts, answers others. You set its knowledge and behavior rather than each action: more director than scriptwriter. <i>Example: every week it drafts a summary from a folder of reports, and you check it.</i></p></article>
</div>

No one way is better than the others, and you can combine them in a single project. How to choose:

- **The result is clear in advance and easy to check:** automation.
- **You don't yet know the best solution yourself:** augmentation.
- **The same work recurs, and you are ready to set it up and check it regularly:** agency. This is the way that carries the most responsibility: decide in advance where a person checks the result and can stop the work, and use only tools approved in your organization.

**Try this.** Write down three of your tasks for this week and decide which way suits each. If a task fits none of them, it may be better done without AI.

## The four 4D skills {#4d}

| Skill | Question | Components |
| --- | --- | --- |
| **Delegation** | What do I do, and what does AI do? | understanding the task · understanding the tool · dividing the work |
| **Description** | How do I explain it clearly? | what to get · how to approach it · how to behave |
| **Discernment** | Is the result any good? | the result · the process · the AI's behavior |
| **Diligence** | Am I working responsibly? | creation · transparency · using the result |

In the short guide these skills are also glossed in everyday words: what to hand over, how to explain it, judging the result, owning the result. They are the same four skills.

Most work with AI consists of short “describe → evaluate” loops. Delegation sets where these loops are needed, and diligence sets the bounds they run within.

**Try this.** Talk with Claude for 5–10 minutes about a topic you know well, for example a procedure you run every day, leaving out internal details. Where does it strengthen your thinking? Where did you have to correct it? Where did your expertise help you evaluate the answer?

## How generative AI works {#basics}

- [[generative-ai|Generative AI]] **creates something new** (text, tables, code) rather than only classifying: a spam filter sorts emails, while a language model writes them.
- A model is trained in two stages: first to predict the continuation of text on huge amounts of data, then to be helpful, honest and harmless with the help of human feedback.
- The model **doesn't pull a ready answer from a database**; it writes it afresh every time.
- The [[context-window|context window]] is its working memory: the prompts, answers and materials of the conversation.

### Strengths and limitations {#limits}

<div class="rai-cards rai-cards--2">
<article><h3>Strengths</h3><p>Versatility in language tasks without extra training; keeps the thread of a conversation; can work with search, files and apps, if these are turned on in your work account; speed, scale, pattern recognition.</p></article>
<article><h3>Limitations</h3><p>Doesn't know about events after its training; is confidently wrong ([[hallucination|hallucinations]]); loses earlier material when the context overflows; answers don't repeat exactly; complex multi-step reasoning; no access to your internal data until you give it.</p></article>
</div>

People bring critical thinking, judgment, creativity and ethical oversight. For more, see [What AI can and cannot do](page:kb/guides/ai-capabilities-limitations).

## Delegation {#delegation}

Delegation rests not on AI but on **your own expertise**: “the strongest AI users are experts in their field first, and experts in delegation second”.

<ol class="rai-principles">
<li><b>Understand the task</b><span>What is the goal, what does success look like, what work leads to it? Parts of the work can be laborious, uncertain, short of data or in need of judgment.</span></li>
<li><b>Understand the tool</b><span>Different systems are strong at different things: speed, depth, accuracy, creativity. This knowledge comes with practice. Take your organization's constraints into account too: budget, regulatory requirements, approved services.</span></li>
<li><b>Divide the work</b><span>What to automate, where to think together, what to leave to a person, and what can be given to an agent: an AI that carries out the steps of a task on its own.</span></li>
</ol>

“The goal is not to automate everything.”

**Exercise.** Take a project of about an hour, for example preparing a monthly briefing from an Excel report. Ask Claude to keep asking you questions until a picture of success takes shape. Break the project into tasks and decide for each: what is yours, what is AI's, what you do together. Do this as a conversation: you may see what Claude doesn't, and the other way round.

## Description {#description}

Description is more than a [[prompt|prompt]]: it also means being able to get a conversation out of a dead end, and to create “an environment for thinking”. “AI is neither a database nor a vending machine.”

<div class="rai-cards rai-cards--3">
<article><h3>What to get</h3><p>Context, format, audience, style. “AI doesn't read minds”: “cook dinner” versus a recipe.</p></article>
<article><h3>How to approach it</h3><p>A general direction, step-by-step instructions or a “here's how I do it” example; which data, in what order, by what method.</p></article>
<article><h3>How to behave</h3><p>Narrow down or explore? Argue or follow? In detail or briefly? Explain or just answer?</p></article>
</div>

### Six techniques {#techniques}

<ol class="rai-principles">
<li><b>Give context</b><span>“Tell me about this regulation” versus “below is the text of a new regulation; pick out three changes for the lending department, one sentence each; I'm preparing a five-minute update for the morning meeting, and the audience is experienced loan officers”.</span></li>
<li><b>Show examples</b><span>Try without them first; if you need them, use varied ones that cover the options.</span></li>
<li><b>Set constraints</b><span>Format, length, language, layout.</span></li>
<li><b>Break it into steps</b><span>Especially when the task varies and your experience matters.</span></li>
<li><b>Ask it to think first</b><span>Reasoning comes before the answer, not after. It also shows you where AI goes off track.</span></li>
<li><b>Set a role and tone</b><span>“You are an experienced mentor; explain this to a contact center newcomer in plain words”, “look at the text as a compliance specialist would”.</span></li>
</ol>

**The secret weapon** is to ask AI to improve your prompt. If it isn't working: add specifics, give an example, break it into steps, ask for three options, change the format, ask “how sure are you?”, start a new conversation.

Common mistakes: expecting AI to read your mind; mixing unrelated tasks in one prompt; describing success vaguely; not giving feedback. For everything about prompts, see [How to write prompts for Claude](page:kb/guides/prompting-complete-guide).

**Exercise: bad prompts.** Write to Claude: “Give me five bad prompts for my work tasks: an internal memo, a reply to a customer complaint, a meeting summary. I'll fix them, and you rate my fixes.” After five minutes, swap roles: you write bad prompts and Claude fixes them. Look at what it adds: those are the missing parts of a good description.

## Discernment {#discernment}

Discernment is the flip side of description, and your quality control system. It requires knowledge of the subject and an understanding of AI's typical weaknesses.

<div class="rai-cards rai-cards--3">
<article><h3>The result</h3><p>Is it accurate? Suitable for the audience? Coherent? Does it meet the requirements? Does it add value?</p></article>
<article><h3>The process</h3><p>Logical errors, lapses of attention, unnecessary steps, getting stuck on one interpretation, returning to ideas already rejected.</p></article>
<article><h3>The AI's behavior</h3><p>Too many questions? Too brief? Does it take feedback? Does this style of communication suit you?</p></article>
</div>

### How to give feedback {#feedback}

What's wrong → why → a concrete suggestion → adjust the instructions. Sometimes the right answer is to **reconsider the delegation**: the wrong tool or the wrong approach.

### The description–discernment loop {#loop}

<ol class="rai-flow rai-flow--4">
<li><b>Describe</b><span>the task, the approach, the behavior</span></li>
<li><b>Evaluate</b><span>the result, the process, the behavior</span></li>
<li><b>Refine</b><span>the description based on the evaluation</span></li>
<li><b>Integrate</b><span>add your own expertise, make the decision and take responsibility for the result</span></li>
</ol>

**Exercise: expert evaluation.** Ask for three explanations of a topic in which you are an expert, for example how your department's process works; evaluate them against the three kinds of discernment, separate the strong points from the weak ones, and improve them together with Claude.

## Diligence {#diligence}

The first three skills are mostly about effectiveness; diligence is about ethics and safety. It's like driving: what matters is not only getting there, but also following the rules and thinking of others.

<div class="rai-cards rai-cards--3">
<article><h3>Creation</h3><p>How the system was trained, who owns the data, who will get access to it, whether your organization's policy allows it. Example: before sharing confidential data, check the service's policy and your organization's permissions.</p></article>
<article><h3>Transparency</h3><p>Who should know about AI's role, when, and in how much detail to say so. Example: in a team proposal, mark which parts were done with AI.</p></article>
<article><h3>Using the result</h3><p>You are responsible for what is published, not AI: facts, bias, rights of use. Example: a report prepared with AI is checked against the same standards as one prepared without it.</p></article>
</div>

**Exercise: an AI contribution statement.** For a piece of your work, for example an internal memo, write a short statement: which parts were done with AI, how they were checked, who is responsible for the result. For each of the three kinds of diligence, ask yourself a few check questions.

What you may share with AI here: [What you can and cannot share with AI](page:kb/guides/what-to-share); how to check: [How to check AI output](page:kb/guides/checking-results).

## Your personal rules for working with AI {#policy}

The course's final exercise is a **personal AI policy**: one page of your own rules. Everyone who works with Claude regularly should write one and discuss it with their manager. If your organization has its own rules, your personal rules add to them; they don't replace them.

The policy brings together what you already know: [what you can share with AI](page:kb/guides/what-to-share), [how to check the result](page:kb/guides/checking-results) and the four 4D skills. Five sections:

<ol class="rai-principles">
<li><b>When and how I use AI</b><span>Which tasks yes, which tasks no.</span></li>
<li><b>Limits for confidential material</b><span>What I never share, and with which services.</span></li>
<li><b>Quality control</b><span>How and how thoroughly I check the result, depending on who it goes to.</span></li>
<li><b>Ethical dilemmas</b><span>How I resolve borderline cases and whom I turn to.</span></li>
<li><b>Disclosing AI's part</b><span>A template, and the cases where detailed disclosure is needed.</span></li>
</ol>

A sample draft you can rewrite for yourself:

- **I use AI for** drafting emails, meeting summaries, rewording texts and working through anonymized tables. **I don't use it for** decisions about customers or final legal wording.
- **I never share** personal data of customers and colleagues, banking secrecy or passwords. I work only in a work account approved in my organization.
- **I check:** for myself, I read and assess; for my manager, I check figures and facts against the source; for a customer, a full check against the list and a second person if in doubt.
- **Borderline cases** I discuss with my manager before acting.
- **I disclose AI's part** with a short phrase, for example “Draft prepared with the help of AI, checked by me”, and in more detail where the reader expects it.

**Try this.** Write your rules on one page under these five sections and discuss them with your manager.

### How to keep growing {#grow}

- Rate yourself on each skill and each way of working: beginner, developing, confident.
- Build a personal library of 5–10 prompt templates that worked well.
- Practice description and discernment through games: riddles, “20 questions”, a story told together. Skills grow faster through play.

Fluency in working with AI grows with practice; it doesn't appear all at once. And AI is not a magic wand.
