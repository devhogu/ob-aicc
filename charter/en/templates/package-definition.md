```yaml
id: AICC-TPL-14-EN
title: Package Definition
status: active
revision: 1.1
created: 2026-10-03
revised: 2026-10-07
```

# Package Definition

**Template.** Copy for each Package when a service category foresees it or an Engagement leaves it. The Owner completes it while the Package is produced and keeps it current while the Package is available, and the Competence Center Lead keeps it in the Portfolio (Business Model 4.4). It describes the Package: what it is, what it contains, and how a function re-deploys it. It carries no figures of the Bank, no data, and no code. Keep it short, in one form.

| Field | Entry |
| --- | --- |
| Identifier | PKG-[nnn] |
| Title | [title] |
| Kind | [method / kit / engine / catalog of automations / template set] |
| Service area and category | [service area; service category (Business Model 4.5)] |
| Status | [planned / in preparation / available / withdrawn; the status of the Package, not a state of an item] |
| Owner | [the Solution Engineer or the Competence Center Lead who keeps it] |
| Produced by | [the Engagement or the Initiative that left it: INI-nnn, AGR-nnn] |
| Used by | [the functions, and the Solutions that use it: SOL-nnn] |
| Needs to re-deploy | [what a function shall provide: a corpus, a data source, a template set, an owner, an environment] |
| Risk Tier of its uses | [the Risk Tier that a use of it normally carries, and what raises it; each use takes its own Risk Tier in its Solution Definition (AI Policy 3)] |
| Where it is kept | [the repository or the folder, and the version] |
| Date of last change | [date] |

## 1. What it is and what problem it answers

[What the Package does and does not do, and the routine work or problem of a function that it answers.]

## 2. What it contains

[The parts of the Package: the methods, Templates, components, automations, or rules that it holds, each by reference.]

## 3. How a function re-deploys it

[The prerequisites that the function provides, the steps of the re-deployment in order, and who helps: the Owner, a Solution Engineer, or the Competence Center Lead.]

## 4. Limits and risks

[The data classes that it may touch, and what it shall not be used for. The providers and the platforms that it depends on. The check or the validation that a use of it needs (Solution Lifecycle Model 7.1).]

## 5. History

[The Engagements and the Initiatives that produced or changed it, and the lessons from its uses.]

| Date | Engagement or Initiative | Change |
| --- | --- | --- |
| [date] | [INI-nnn, AGR-nnn] | [what was produced or changed] |
