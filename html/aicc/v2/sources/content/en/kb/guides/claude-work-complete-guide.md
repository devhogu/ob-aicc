---
title: "Working in Claude: projects, documents, Office, and Cowork — complete guide"
summary: How to work with Claude every day. Projects from creation to upkeep, files and creating Word, Excel, PowerPoint, and PDF documents, Claude inside Office, connectors, Cowork with your folders and scheduled tasks, data safety, and ready-made scenarios by role.
category: Claude
level: deep
minutes: 50
order: 1
featured: true
layout: course
tags: claude, projects, files, word, excel, powerpoint, outlook, office, cowork, artifacts, connectors, scheduling, safety
source: Справочный центр Claude, документация Claude для Office и курсы Claude 101 и Introduction to Claude Cowork
source_en: Claude Help Center, Claude for Office documentation, and the Claude 101 and Introduction to Claude Cowork courses
source_url: https://support.claude.com/ru/articles/13345190
source_hash: 8ee03fc103c4
---

This guide is for employees who want to work with Claude every day, from the first conversation to tasks that Claude runs on its own on a schedule. Each tab is a separate topic, and you can start reading anywhere. The guide is based on the Claude Help Center, the Claude for Office documentation, and the Claude 101 and Introduction to Claude Cowork courses, as of October 2026.

<div class="rai-cards rai-cards--3">
<article><h3>Chat: think together</h3><p>A conversation: talk something through, go over a document, write a draft, get a finished file. For recurring work, use <b>projects</b>.</p></article>
<article><h3>Cowork: hand it over</h3><p>Claude works with your files, folders, apps, and browser itself, carries out a multi-step task, and delivers a finished result.</p></article>
<article><h3>Office: right in the document</h3><p>Claude in Excel, Word, PowerPoint, and Outlook: it edits the open file in place and keeps its formatting.</p></article>
</div>

What's available depends on your plan and on what your organization's admin has turned on. Work only in an approved work account; if something is missing, [write to us](page:services/how-to-engage). What you can and cannot share with Claude is covered in the [data checklist](page:kb/guides/what-to-share).

## Where to start {#start}

This tab helps you find the buttons you need in Claude and set it up for yourself in five minutes.

### Interface language {#language}

In this guide, button and menu names are given in quotes exactly as they appear in Claude, for example “Settings → Capabilities”. **You can also talk to Claude in Russian**: it replies in the language you write in.

### Where things are {#where}

- **New conversation:** the button at the top left. Every conversation starts from a blank page.
- **Projects:** “Projects” in the left panel, or at claude.ai/projects.
- **Model and effort level:** the menu next to the send button. The effort level sets how much Claude thinks before answering. For routine work, “Low” or “Medium”; for most tasks, “High”; for complex analysis, “Xhigh” or “Max”. On the newer models, thinking is always on.
- **“+” in the message box:** attach files, turn on “Research” and “Connectors”, turn off memory for this conversation.
- **Standing instructions:** “Settings → Instructions for Claude”: your instructions for all conversations, such as who you are and how to format answers. For example: “I'm a credit operations specialist. Write in Russian, in a formal business style, conclusion first, then the details.”

### Memory and private conversations {#memory}

Memory is what Claude remembers about you and your work between conversations.

- On team plans, memory is off by default: the organization owner turns it on, and then each employee turns it on for themselves in “Settings → Memory”. That is also where you can see and correct what Claude has remembered.
- The ghost icon starts a **private conversation**: it isn't saved to history or memory. On team plans, such conversations are still subject to the organization's retention and export rules.

## Projects {#projects}

This tab is for those who have already built a first project or are about to. By the end you will be able to write good project instructions, keep the project's documents in order, and share the project with colleagues.

A project is a workspace with its own conversation history, its own documents, and its own instructions. Claude takes everything in the project into account in every conversation inside it. A short introduction is in the guide [Projects in Claude](page:kb/guides/claude-projects).

<ol class="rai-flow rai-flow--4">
<li><b>Create</b><span>one topic, one project</span></li>
<li><b>Knowledge</b><span>documents to rely on</span></li>
<li><b>Instructions</b><span>role, way of working, tone, requirements</span></li>
<li><b>Work and maintain</b><span>conversations, shared access, updates</span></li>
</ol>

### 1. Create {#create}

1. “Projects → + New Project”: the button at the top right.
2. The name and description are for people: **Claude doesn't see them**, so put everything important in the instructions.
3. On team plans, choose the visibility: “Keep it private” (only you) or “Share with your broader organization” (the whole organization), if your admin allows it.

Several narrow projects are better than one “everything for work”: “Replies to customer requests”, “Quarterly reporting”, “Checking supply contracts”.

### 2. Add knowledge {#knowledge}

Project knowledge is the documents Claude relies on in every conversation in the project. On the right of the project page, click “+” and upload documents.

- Up to **30 MB per file**; the number of files isn't limited, but the total must fit in the model's [[context-window|context window]].
- On paid plans, when there is a lot of knowledge, Claude turns on search across the project documents by itself; this increases capacity about tenfold without loss of quality.
- **Give files clear names:** “Lending_procedure_2026.pdf”, not “document1.pdf”. Claude finds its way by the names.
- Add complete, current versions; drafts and outdated material aren't needed.
- Name the specific document in your questions: “according to the lending procedure, section 4”.
- Google Docs can be added as a link if Google Drive is connected.

### 3. Write instructions {#instructions}

“Set project instructions” → text → “Save instructions”. Good instructions contain four things: context (who you are and what the project is for), the way of working, the tone, and mandatory requirements. Take the sample below and adapt it to your task.

```text
Context: a project for contact center specialists. We answer customer questions about cards and payments.

Way of working: first look for the answer in the project documents. If it isn't there, say so and offer to pass the question to a senior specialist.

Tone: polite, simple, no internal jargon. 5–7 sentences.

Mandatory: never promise deadlines or decisions that aren't in the procedure. Don't ask the customer for the full card number or codes.
```

```text
Context: a finance department project for preparing the monthly budget execution summary.

Way of working: 1) take the actuals and the plan from the attached export; 2) calculate the variances; 3) explain variances over 5% using the departments' comments; 4) write the summary.

Format: one page. First the three main conclusions, then a table, then the risks. Every figure comes with a reference to the sheet and row of the export.
```

If you correct Claude with the same remark from one conversation to the next, add it to the instructions. For how to word things, see [How to write prompts for Claude: the complete guide](page:kb/guides/prompting-complete-guide).

### 4. Work in the project {#work}

- Each task is a new conversation inside the project: all of them see the knowledge and the instructions.
- **Conversations in one project don't see each other**: whatever should be shared goes into knowledge. If memory is on, the project has its own memory, separate from your other conversations.
- A good conversation outside the project can be moved into it: the menu next to the conversation name → “Add to project”.

### 5. Share (Team and Enterprise) {#share}

A shared project gives the whole group the same documents and rules: for example, all contact center specialists have the same knowledge base of answers.

1. “Share project”, to the right of the name.
2. Add colleagues by name or email; you can paste a whole list of addresses at once.
3. Permissions: “Can view” sees the knowledge and instructions and can work in the project, but can't change them; “Can edit” can change the instructions, the knowledge, and the members.

Your conversations inside a shared project stay **yours**: colleagues don't see them unless you share them yourself. Give edit rights to those responsible for the project's documents; viewing is enough for everyone else.

### 6. Maintain {#maintain}

- “Star” pins a project you need to the top.
- Review the documents regularly: if a procedure changes, replace the file, or Claude will answer from the old one.
- “Archive” puts away a project that is no longer relevant and keeps its permissions; “Delete” removes it completely.

**Try it now.** Open your project and rewrite its instructions in four parts: context, way of working, tone, mandatory requirements. Ask the same question as before and compare the answers. If the project would help your colleagues, share it with them for viewing.

## Files and documents in a conversation {#files}

This tab covers which files you can attach to a conversation and how Claude reads them.

### What you can attach {#upload}

“+” → “Add files or photos”, or drag a file into the window, or paste an image from the clipboard.

| What | Limits |
| --- | --- |
| PDF, DOCX, XLSX, CSV, TXT, HTML, ODT, RTF, JSON | up to 20 files per conversation |
| JPEG, PNG, GIF, WebP images | up to 8000×8000 pixels; 1000×1000 or more works best |
| PDF up to 100 pages | Claude sees both the text and the images with charts |
| PDF of 101–1000 pages | text only |

- For large files, go by **30 MB**: different Help Center articles give different limits, and 30 MB is a safe boundary.
- From Word and other non-PDF files, Claude takes only the text; images inside aren't read.
- When you refer to a PDF page, give the number your viewer shows, not the one printed on the page.
- A large document is better split into parts.

Before you attach a file, recall [what you can and cannot share with AI](page:kb/guides/what-to-share).

## Creating Word, Excel, PowerPoint, and PDF files {#create-files}

This tab is for everyone who prepares reports, summaries, and presentations. By the end you will be able to ask Claude to make a finished file (an Excel spreadsheet with formulas, a Word document, a presentation, or a PDF) and download it.

Claude can not only read but also **create real files**: Excel spreadsheets with formulas and charts, Word documents, PowerPoint presentations, PDFs.

### Turn it on {#enable-files}

- **Free, Pro, Max:** “Settings → Capabilities → Code execution and file creation”.
- **Team, Enterprise:** on by default; an admin can turn it off.

### How to ask {#ask-files}

Be specific: describe the structure, the content, and the formatting.

<div class="rai-cards rai-cards--2">
<article><h3>Excel</h3><p>“From this export, make a table of customer requests by week: topics, counts, totals, and each topic's share, using formulas.” “Move all the data from this PDF into Excel and build a summary chart.”</p></article>
<article><h3>Data report</h3><p>“From this CSV export, make the department's weekly report: trends, three conclusions, recommendations.”</p></article>
<article><h3>Word</h3><p>“Explain this Excel table in a Word internal memo, with comments on each indicator.”</p></article>
<article><h3>PowerPoint</h3><p>“Turn this document into an 8-slide presentation for the management board.”</p></article>
</div>

You can also chain them: export → financial model → internal memo → presentation. Finished files download with a button and stay available as long as the conversation is open; you can also save them to Google Drive.

- In Excel, Claude puts in **formulas, not hard-coded numbers**; check how the formulas link up.
- Creating files uses up your plan's limit faster than a plain conversation.
- Files and websites from outside may contain [[prompt-injection|hidden commands]] for Claude: watch what it does, and stop the work if you see an unexpected call to outside resources.

**Try it now.** Take an export you work with every week and remove names, account numbers, and other customer data from it. Attach it and write: “Make an Excel spreadsheet: data on the first sheet, totals by category using formulas on the second, a chart on the third. List the formulas you used.” Download the file and check two or three formulas by hand.

### Artifacts {#artifacts}

An artifact is something Claude creates for you that you can share: a document, slides, a design, a dashboard, a small tool. It opens in a panel next to the conversation.

- **Templates:** documents (Docs), slides (Slides), and design (Design) on all plans; dashboards and animation on higher plans.
- **Edit:** ask Claude, edit right in the artifact, or select text → “Edit with Claude”.
- **Export:** documents to Word, PDF, Google Docs; slides to PowerPoint, PDF, Google Slides.
- **Share:** by default an artifact is private; on team plans, only within the organization. Permissions: view, comment, edit.
- An artifact can store data: before entering anything confidential, check whether it uses shared storage.
- Ask for a finished result right away: “make a one-page document from the quarter's results”, not “write some text about the results”.

## Claude in Excel, Word, PowerPoint, and Outlook {#office}

This tab is for those who work in Office all day. By the end you will be able to ask Claude to explain, fix, or add to a file you already have open, without copying it into a separate conversation.

The Claude for Microsoft 365 add-in is a Claude panel inside the Office apps. Claude works with the **open file** and edits it in place, keeping its formatting. Plans: Pro, Max, Team, Enterprise. Excel, Word, and PowerPoint are generally available; Outlook is in beta. If your Office doesn't have the add-in, see “How to install” below. Before you start, read “Important for data” at the end of the tab: the add-ins don't leave the usual audit trail.

<div class="rai-cards rai-cards--2">
<article><h3>Excel</h3><p>Explains any figure with cell references; changes an assumption and recalculates the dependent formulas; finds the cause of #REF! and #DIV/0!; builds a model or fills in a template; pivot tables, filters, conditional formatting. Warns you before overwriting data.</p></article>
<article><h3>Word</h3><p>Answers questions about the document with references to sections; rewrites a selected passage while keeping styles and numbering; makes edits as tracked changes that you accept or reject; works through a counterparty's comments and edits.</p></article>
<article><h3>PowerPoint</h3><p>Uses your corporate template, with its layouts, fonts, and colors; fixes one slide without touching the rest; builds a presentation from a description; turns bullet points into a diagram or an editable chart.</p></article>
<article><h3>Outlook (beta)</h3><p>Sorts your inbox into “needs me”, “Claude can handle it”, and “noise”; drafts replies in your style; boils a long thread down to decisions and open questions. <b>It doesn't send anything itself</b>: all replies stay as drafts.</p></article>
</div>

### Sample prompts {#office-prompts}

- Excel: “Explain how the total in cell C42 is calculated.” “Set the discount rate to 8% and update the dependent calculations.” “Find the source of the #REF! error on the summary sheet.”
- Word: “Find all provisions on data retention periods.” “Rewrite section 3 more simply, with the edits as tracked changes.” “Briefly summarize what the counterparty changed.”
- PowerPoint: “Add an executive summary slide in a single-column layout.” “Build a bar chart for the first to fourth quarters.”
- Outlook: “What needs my attention?” “Draft replies to everything you can handle.”

**Try it now.** Open your weekly report in Excel, open the Claude panel, and ask: “Explain how the total on this sheet is calculated, with cell references.” Compare the answer with what you know about the file.

### Working across several apps {#across}

If you turn on “Let Claude work across files” in each add-in, Claude links the open files: “take the actuals from the Q3 sheet, compare them with the plan, write comments on the variances in column F, and make three slides from this for the quarterly review.” It works only with open files. On team plans, an admin turns this feature on.

### What the add-ins can't do, and where to be careful {#office-limits}

- Excel: doesn't work with macros, VBA, or data tables; doesn't support perpetual-license Excel 2016 and 2019, iPad, or Android.
- Outlook: Exchange Online in Microsoft 365 only; admin consent is required.
- Not recommended without a human check: final materials for customers, calculations that matter for audit, documents for counterparties and courts. The add-in doesn't replace legal or financial judgment.

### How to install {#office-install}

On your own: Microsoft AppSource → “Claude for Microsoft 365” → “Get it now” → turn on the add-in in the Office app and sign in with your Claude work account. In an organization, the add-in is usually deployed by the Microsoft 365 admin; if you don't have it, contact IT. Standing instructions for Excel are set in the add-in itself: “Settings → Instructions”.

### Important for data {#office-data}

The add-ins have their own retention rules: conversation history is stored **locally in the browser** and isn't synced, data on Anthropic's side is deleted within 30 days, and **the organization's retention periods don't apply to the add-ins, and they don't appear in audit logs** (in Enterprise with the Compliance API turned on, they do, in beta). For materials that need an audit trail, take this into account in advance.

## Connectors and research {#connectors}

This tab is for those who have to gather information from email, the calendar, and shared folders. By the end you will be able to ask Claude to find what you need in your work systems and to choose between web search, thinking, and research.

### Connectors {#connect}

A connector gives Claude access to your work systems with your own permissions: it sees only what you see. Without a connector, you copy emails and files into the conversation yourself; with one, Claude finds them on its own.

- **Microsoft 365:** search and analysis across SharePoint, OneDrive, Outlook email and calendar, and Teams. Requires a work account; in an organization, an admin turns it on first. “Write” actions, such as sending emails or changing files, only if the admin has allowed them. A useful habit: “draft a reply to the supplier, but don't send it”.
- **Google Workspace:** Gmail, Calendar, Google Drive. By default, Claude checks with you before each email it sends.
- Where to manage them: “Customize → Connectors”, or “+” in the message box → “Connectors”.
- On team plans there is search across the organization's sources (“Ask Your Org”): a ready-made project that searches the connected systems and shows only what the employee has access to.

Sample prompts when a connector is on:

- “What's on my calendar this week, and which meetings do I need to prepare materials for?”
- “Find emails from the last two weeks about the new reporting procedure and put them in a list: who is asking for what, and by when.”
- “Find the latest version of the refunds procedure in the department's shared folder and tell me what changed in it.”

**Try it now.** If you have a connector to your email or calendar turned on, ask the first question from the list above and check the answer against your calendar. If you have no connectors, ask IT whether they are approved in your organization; there's no need to turn them on by a workaround.

### Search, thinking, or research {#research}

<div class="rai-cards rai-cards--3">
<article><h3>Web search</h3><p>A quick fact where freshness matters.</p></article>
<article><h3>Thinking</h3><p>Complex reasoning without fresh data: a calculation, a close reading of a document.</p></article>
<article><h3>Research</h3><p>A report drawn from many sources, with links: “+” → “Research”. Takes several minutes.</p></article>
</div>

Check links from web search and research the same way as any answer: open the source and make sure it says exactly that.

## Cowork: hand work to Claude {#cowork}

This tab is for those who already understand [when you need Cowork](page:kb/guides/claude-cowork) and want to hand it a real task. By the end you will be able to set up Cowork, run a task from handover to review, set standing context, and schedule a task.

“Chat is for thinking together with Claude. Cowork is for handing it work.” In Cowork, Claude gets access to the folder you choose, the connected apps, and the browser; it makes a plan, carries it out step by step, and delivers a finished result. It's the same approach as in Claude Code, Claude's tool for programmers, but without the command line.

**When to use Cowork:** a task of several steps that takes time, ends with a concrete result, and needs several sources or tools. For a one-off question, a plain conversation is enough; for editing one open file, use the Office add-in.

### Set up {#cowork-setup}

1. You need a paid plan and the Claude desktop app (macOS or Windows) from claude.com/download. In an organization, an admin turns Cowork on.
2. **Choose a working folder:** one folder for one piece of work, not “Documents” and not the whole drive. The folder gives Claude the right both to read and to write.
3. Add the connectors you need.

### Run a task {#cowork-run}

In the message box, choose “Cowork”, describe the task, look at Claude's plan, and start. Tasks can run in the cloud and keep going even when your laptop is closed; work with local files and the browser needs the app to be open.

### Permission modes {#cowork-modes}

The permission mode sets whether Claude asks for your approval before each action.

| Mode | What happens | When |
| --- | --- | --- |
| Manual | Claude asks before acting | the default; new tasks and important data |
| Auto | each action is checked for safety and anything dangerous is blocked; uses more of your limit | familiar tasks; in an organization, if the admin allows it |
| Skip | Claude acts without asking | only when you fully trust every action |

Deleting files **always** needs your explicit permission. Run your first tasks in Manual mode.

### The task cycle {#cowork-loop}

<ol class="rai-flow rai-flow--4">
<li><b>Hand it over</b><span>what to deliver (format, length), from what (folders, channels, dates), which details to keep in mind</span></li>
<li><b>Answer the questions</b><span>Claude will ask for details, usually with ready-made options</span></li>
<li><b>Steer as it goes</b><span>correcting course is better than redoing it from scratch</span></li>
<li><b>Check the result</b><span>check it against the sources; made-up dates, names, and quotes are a red flag</span></li>
</ol>

An example handover: “From the ‘Department reports’ folder, put together the budget execution summary for September: a table of actuals vs. plan by department, variances over 5% with explanations from the comments, one page in Word. Keep in mind that three new branches opened in the third quarter.”

**Try it now.** Create a new folder and put copies of three to five documents that may be shared into it: for example, department reports for a month or meeting minutes. Choose this folder in Cowork, Manual mode, and hand it over: “From the documents in this folder, put together a one-page summary in Word: the main points of each document, general conclusions, open questions. Say which file each point comes from.” Look at the plan, answer Claude's questions, and check the summary against the documents.

### Standing context {#cowork-context}

Standing context is what Claude knows about you and your work in every task, without explaining it again. Add it gradually, not all on the first day.

- **Global instructions:** “Settings → Cowork → Global instructions”: your role, organization, abbreviations and terms, the format of results, preferences such as “start with the recommendations”. A correction you repeat time after time is a candidate for the global instructions.
- **Folder instructions:** context for a specific piece of work; Claude can add to them itself.
- **Cowork projects:** “+” next to “Projects”, starting from scratch, from an existing folder, or from a chat project. A project holds instructions, scheduled tasks, context, and its own memory.

### Skills and plugins {#cowork-skills}

- **A skill** is a written-down procedure: exactly how to do a particular piece of work. Ask: “I want to make a skill for [process]. Ask me what you need to know.” For details, see [Claude skills: the complete guide](page:kb/guides/skills-complete-guide).
- **A plugin** is a set of skills for a whole line of work, together with connectors. Anthropic has plugins for finance (variance analysis, financial models, investment memos, quarterly reports), for lawyers, and for sales. “Customize → Plugins” → install; <code>/setup-claude</code> will ask you questions and recommend suitable ones. Plugins can run programs with your permissions: use only those from trusted sources and approved in your organization.

### Browser {#cowork-browser}

The Claude extension for Chrome and the desktop app's built-in browser are for systems that have no connector: internal portals, dashboards. You must already be signed in to the site, since Claude doesn't sign in for you; by default it asks before sensitive actions.

### Scheduled tasks {#cowork-schedule}

A scheduled task is a handover that Cowork carries out by itself at a set time: every morning, every Friday, on weekdays. It suits regular work that you have already done in Cowork by hand more than once and whose result you know how to check.

Type <code>/schedule</code> in a task or choose “Scheduled → New task”. You can set it up together with Claude (it will ask questions) or by hand: name, handover, permission mode, frequency (hourly, daily, weekly, on weekdays), folder. If the task works with files on your computer or with the browser, the Claude app must be open at that time.

Good scheduled tasks: a morning summary of email and calendar, a weekly report, regular monitoring of regulator news, sorting incoming files. **At first, let the result be a draft**, not a sent email.

An example weekly task: “Every Friday at 15:00, use the ‘Weekly report’ folder to put together a draft of the department's weekly report in Word: what was done, figures from the tables in the folder, problems, plans for next week. Save the file to the same folder. Don't send anything.”

## Safety and data {#safety}

Everyone should read this tab before working in Cowork, with the Office add-ins, or with connectors. By the end you will know where work with Claude leaves no audit trail and which tasks Cowork and the add-ins aren't suited for.

An audit trail is a record of who did what and when, which the organization keeps and can check. In regulated processes it may be mandatory. The general rules on data are in the checklist [What you can and cannot share with AI](page:kb/guides/what-to-share).

### What Anthropic says about work plans {#business-data}

- In the commercial products (Claude for Work), your prompts and answers are **not used to train models** by default. The exception is when you send feedback yourself (thumbs up or down): then the conversation may be kept for up to five years. An admin can turn ratings off.
- In Team and Enterprise, the organization controls the data, and Anthropic acts as a data processor, processing it on the organization's behalf. A deleted conversation disappears from history at once and from the servers within 30 days.

### Where there is no audit trail {#audit-gaps}

- **Local Cowork sessions** keep their history on the employee's computer: standard retention periods don't apply to them, and an admin can't manage or delete them centrally.
- **The Office add-ins** don't appear in audit logs and don't inherit the organization's retention periods (except Enterprise with the Compliance API).

### When Cowork and the add-ins aren't suitable {#not-for}

- Regulated processes where an audit trail is mandatory.
- Actions with serious consequences: sending legal documents, public statements, payments.
- Sensitive personal data outside the boundaries approved by IT.

If you're not sure whether a task is suitable, don't start; ask your manager or [write to us](page:services/how-to-engage).

### Anthropic's ten rules for Cowork {#cowork-rules}

<ol class="rai-principles">
<li><b>Don't give access to files with confidential data</b><span>A separate working folder, not “Documents” or “Desktop”.</span></li>
<li><b>Watch tasks, not just commands</b><span>Look at the plan and the progress in the progress tab.</span></li>
<li><b>Be careful with scheduled tasks</b><span>Drafts first.</span></li>
<li><b>Match oversight to importance</b><span>The higher the stakes, the stricter the mode and the check.</span></li>
<li><b>Be careful with computer use</b><span>It's in beta, and Claude acts on your screen.</span></li>
<li><b>Trusted sites only</b><span>Limit the browser to verified sources.</span></li>
<li><b>Take special care with unfamiliar connectors and plugins</b><span>Approved ones only.</span></li>
<li><b>Pay attention to data moving between apps</b><span>What from one system may end up in another.</span></li>
<li><b>Cloud sessions can reach your computer</b><span>Understand what they have access to.</span></li>
<li><b>Report anything suspicious right away</b><span>Stop the task and write to IT.</span></li>
</ol>

Three more habits from the course: keep backups out of Claude's reach; try new procedures on copies; word destructive instructions precisely, since “delete” and “update” can be understood in different ways. You are responsible for every action Claude takes on your instructions.

## Scenarios by role {#roles}

This tab is for those who want Claude to be useful not only to them but to the whole department. Pick the scenario for your role, try it yourself, and suggest it to your colleagues.

<div class="rai-cards rai-cards--2">
<article><h3>Finance: variance analysis</h3><p><b>Where:</b> Excel or Cowork. “Take the actuals from the ‘September’ sheet, compare them with the plan, write comments on variances over 5% in column F, then make three slides for management.”</p></article>
<article><h3>Finance: forecast and scenarios</h3><p><b>Where:</b> Cowork, possibly monthly on a schedule. “Load the actuals into the model, extend it by four quarters, calculate the base, optimistic, and pessimistic scenarios, list the assumptions you changed, and write a one-page memo.”</p></article>
<article><h3>Finance: making sense of someone else's spreadsheet</h3><p><b>Where:</b> Excel. “Explain how this model is built and where the total on the ‘Summary’ sheet comes from; find hard-coded numbers instead of formulas.”</p></article>
<article><h3>Compliance and lawyers: contract edits</h3><p><b>Where:</b> Word. “Briefly summarize what the counterparty changed, and flag changes to the liability terms and deadlines.” The lawyer makes the assessment.</p></article>
<article><h3>Compliance: checking against a list</h3><p><b>Where:</b> a project or a skill. The document is checked against your checklist: compliant / not compliant / not in the document, with a quote.</p></article>
<article><h3>Compliance: summary of a new regulation</h3><p><b>Where:</b> a conversation or a project. “Summarize this regulation for the department's staff: what changes, from what date, which of our processes are affected. Give the article number for each point.” A specialist checks the conclusions.</p></article>
<article><h3>Contact center: reply to a complaint</h3><p><b>Where:</b> a project with procedures and sample replies. Paste the gist of the complaint without the customer's name, account number, or other data: “Write a polite reply according to the procedure, without promising deadlines that aren't in the procedure.” The employee sends the reply.</p></article>
<article><h3>Lending: changes to a procedure</h3><p><b>Where:</b> a conversation or Word. “Compare the old and new versions of the lending procedure and make a table: section, what it was, what it is now, what this changes for the specialist.”</p></article>
<article><h3>HR: onboarding a newcomer</h3><p><b>Where:</b> a project. “From the project documents, put together a guide for a new employee of the department: the first week, whom to go to with what, the main procedures.”</p></article>
<article><h3>Operations: minutes and tasks</h3><p><b>Where:</b> chat or Cowork. “From the meeting transcript, write the minutes: decisions, tasks, owners, deadlines.”</p></article>
<article><h3>Back office: reconciling exports</h3><p><b>Where:</b> Excel or Cowork. “Compare two anonymized exports for the same day and list the rows that are in one and not the other, and the rows with different amounts.” An employee works through the discrepancies.</p></article>
<article><h3>Manager: preparing for the week</h3><p><b>Where:</b> Cowork on a schedule, with a connector to email and calendar. “Every Monday at 8:00, a summary of the week's meetings and the emails waiting for my reply.” A draft only.</p></article>
</div>

### How to introduce a scenario in your department {#roles-adopt}

1. Pick one scenario that saves time for you specifically, and run it yourself three or four times on real data that may be shared.
2. Write down what worked: the prompt, the project instructions, how you check the result.
3. Show your colleagues and share the project or the prompt. Agree on who checks the result before it goes further.
4. After two or three weeks, take stock: how much time you saved and which mistakes the check caught.

Want to introduce a scenario like this in your department? [Tell us about it](page:services/how-to-engage): that way the task comes to us as [[run-rate|run-rate work]].

All links to courses and documentation are in the Reference section: [Anthropic learning](page:reference/anthropic).
