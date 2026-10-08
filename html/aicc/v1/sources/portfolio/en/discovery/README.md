# Discovery catalog

The Discovery catalog holds the scenarios in which AI could help the Bank, by service area and capability: each with its problem, the Solution it suggests, and its leading indicators. The catalog feeds the Funnel: a scenario becomes an Initiative only when a function states a need for it and the Competence Center Lead enters it in the [Portfolio Backlog](../portfolio-backlog.md) as Proposed (Portfolio Management Model 5.2). A scenario is not an Initiative and has no state of the Portfolio Kanban.

The catalog is kept in this folder as Markdown records in both languages, one record for each page of the Discovery Catalog section of the Competence Center portal. The portal generator (`portal/tools/discovery.py`) renders the pages from the records; the records hold the content only, and the generator adds the interface labels, the layout, the links and the counts.

When a scenario is entered in the Funnel, the Initiative Brief names the scenario it comes from, by its URN, so that the link from the catalog to the Portfolio Backlog is kept.

## Records

The path of a record is the path of its page: `risk-control/credit-risk.md` is the page `discovery/risk-control/credit-risk/`, and `risk-control/index.md` is the page `discovery/risk-control/`. There are four kinds of record.

| Record | Holds |
| --- | --- |
| `index.md` | The overview of the catalog: one card for each area, with its group and its sub-groups of capabilities, and the peer frameworks. |
| `<area>/index.md` | An area: its problems by category, the cards of its capabilities and of its cycles, and the scenarios that belong to the area as a whole. |
| `<area>/<capability>.md` | A capability: its problems by category, and its sections with their scenarios. |
| `<area>/<cycles>.md`, `value-streams/index.md` | A set of flows (the cycles of an area, or the value streams): flow categories, and for each flow its description, problems, stages and scenarios. |

Every record starts with the title of its page as a level 1 heading and the introduction of the page as a paragraph.

## Identifiers

A problem category, a section, a flow category, a flow and a card carry their identifier at the end of their heading, as `{#identifier}`. The identifier is the fragment of the page address that leads to them (for a card, the name of the page it leads to); it does not change when a title changes.

A scenario and a flow carry their URN on their first labelled line. The URN identifies them across the catalog and outside it: the Regulatory Horizon and the Initiative Briefs refer to a scenario by its URN, and the stages of a flow belong to its URN. The last part of a scenario's URN is its fragment on its page (`#scenario-<last part>`), so it is unique within the page.

## Problems

Problems are listed under the heading `## Problems`. On an area or capability page they are grouped in categories, each a level 3 heading with its identifier followed by a table with the columns Lens and Problem; the first category is shown first on the page. The value streams have one table of problems without categories.

## Scenarios

A scenario is a heading (level 3, or level 4 within a flow) with the scenario title, then seven labelled lines and the table of its key results:

```markdown
### Counterparty Exposure Breach Notification Pack

- URN: urn:financial-services:scenario:risk-control/credit-risk/counterparty-exposure-analytics/counterparty-exposure-breach-pack
- Lens: Enablement
- Complexity: S
- Intent: The AI agent assembles the supervisory notification pack ...
- Problem to solve: A large-exposure breach triggers a mandatory notification ...
- Solution: The AI agent detects the limit breach ...
- OKR: The CRO reviews and approves an AI-assembled supervisory notification pack ...

| Dimension | Key result |
| --- | --- |
| Adoption | ... |
| Acceptance | ... |
| Cycle | ... |
```

The Lens is one of Insights, Automation, Enablement, Optimize and New opps; the Complexity is one of S, M, L and XL. The OKR line holds the objective, and the table holds the three key results in the order Adoption, Acceptance, Cycle.

## Sections and flows

In a capability record, each section is a level 2 heading with its identifier, followed by its introduction and its scenarios.

In a flow record, each flow category is a level 2 heading with its identifier. Each flow is a level 3 heading with its identifier, followed by two labelled lines (URN and Summary, the short description shown in the list), one or more paragraphs of description, the table of its problems (Lens, Problem), the table of its stages and its scenarios. The table of stages has the columns Key, Stage, Title, Description and Problem to solve, one row for each stage in the order of the flow; the Key identifies the stage on the page (`#stage-<flow>--<key>`), the Stage is its short name on the flow, and the other three columns are shown when a reader opens the stage.

## Cards

The overview of an area (`## Overview`) has one card for each capability and one for its cycles; the overview record has one card for each area. A card is a level 3 heading with the title of the page it leads to and that page's identifier, a labelled line with its Group, and a table:

- a card of capabilities or of sections has the columns Sub-group and Items, and Items lists, separated by commas, the identifiers of the sections of the capability (in an area record) or the names of the capability pages of the area (in the overview record);
- a card of flows has the columns Section, List name and Flows, and Flows lists the identifiers of the flows; the List name is the name of the list given to assistive technologies.

The generator checks that the title of a card is the title of the page it leads to, and that every listed section and flow exists; it takes the title of each listed item from its record. On an area page the first two cards stand in the top band, the third is the card of the cycles, and the rest follow below it. On the overview page each area has a fixed place, defined in the generator. The overview record ends with a level 2 heading that names the peer frameworks, and each peer framework is a level 3 heading followed by its description.

## Derived content and the interface

The records hold no counts, no breadcrumbs and no interface labels. The generator counts the scenarios of every section, flow, page and area, builds the breadcrumbs from the titles of the area records, and adds the labels of the page (such as the column names and the names of the scenario sections) in the language of the record. The labelled lines and the table headers of a record are written in the language of the record.

## Text

Each paragraph, labelled line and table row is one line; text is never wrapped. The only inline markup is `**strong**` and `*emphasis*`. A `|`, `*` or `\` that is part of the text is written with a backslash before it. The records contain no HTML: everything a page shows is either text of a record or derived from the records by the generator.

## Russian edition

The Russian records are in `portfolio/ru/discovery/` at the same paths. A Russian record mirrors its English record: the same headings with the same identifiers, the same URNs and the same tables with the same rows, with the text, the labelled lines and the table headers in Russian. Each Russian record starts with the translation pin of its English record, which names the English record and the SHA-256 of its bytes; when an English record changes, its Russian record is reviewed and its pin is renewed.

## Checks

After a change, run `python3 portal/tools/build.py` and `python3 portal/tools/check.py --idempotent`. The build fails on a record that does not follow this format, and the translation check fails when a Russian record no longer matches the English record it is pinned to.
