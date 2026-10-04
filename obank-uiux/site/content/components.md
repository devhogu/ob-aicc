# Components and interaction rules

## Buttons and menus

Use a primary filled action for the main next step and neutral secondary actions nearby. Links navigate; buttons act. Destructive actions need clear wording and proportional confirmation. Disabled actions should explain their unavailable condition where useful. Loading must retain the control's label/context and avoid duplicate submission.

Menus collect related commands. Use a native select for a choice when it serves the task. For a custom command menu, implement keyboard opening, item navigation, Escape and focus return. A disclosure for navigation links is simpler than pretending it is a command menu.

## Forms

Every field has a persistent label. Put instructions before an error occurs and specific errors next to the affected field. Mark required fields clearly; retain entered values after validation. A form-wide error summary links to the fields when several fail. Success feedback should explain what happened and where the result lives.

Do not use placeholder text as the only label. Distinguish saved, submitted and locally previewed. The form example in this guide previews data only.

## Cards, profiles and tables

Cards summarize selectable subjects; a profile is a coherent reading document. Keep identity, purpose, scope and qualification together. Prefer facts or relationship rows where comparison matters. Tables need header cells, meaningful sort controls and a visible result count. Search/filter changes must distinguish no matches from no records.

Show a metric with subject, unit and period. Unknown is not zero. A status badge includes text; colours do not establish business meaning. Read-only values should not resemble editable inputs.

## Tabs and disclosures

Use tabs for alternate views of one subject, with accessible panel relationships and keyboard navigation. Use disclosures for optional detail. A disclosure's summary must tell the reader what will expand. Neither pattern should hide essential qualifications needed to understand the visible result.

## Feedback and state coverage

| State | Required treatment |
| --- | --- |
| Loading | Explain what is loading; reserve the content region; expose busy state where useful |
| No records yet | Explain what is absent and the relevant next step |
| No search matches | Retain the query and offer reset/change search |
| Partial / unknown | Show available content plus its missing scope or evidence |
| Error | Describe the failed action and useful recovery, retaining entered context |
| Success | Confirm the actual outcome; avoid claiming a backend save in a local example |
| Unavailable / read-only | Explain the condition without implying unknown permissions |

Avoid infinite decorative spinners and fabricated progress percentages. Respect reduced motion. A runtime service issue, a data-loading failure and a knowledge gap are different states.

## Diagrams and comparison

Connections carry labels and direction where meaningful. Keep composition, association and sequential flow visually distinct. Selection can use magenta; ordinary lines stay neutral. Provide a text/list equivalent for essential meaning and a keyboard path to node details. Zoom, pan and fullscreen controls require real behaviour and accessible names.

Choose the visual by the question, not by the available diagram library:

| View | Meaning and minimum explanation |
| --- | --- |
| Relationship graph | Typed, labelled connections between bounded subjects; direction only where the relationship defines it. Start from a selected subject and offer a relationship list. |
| Composition or capability tree | A chosen grouping with expandable children. Shared subjects keep one identity; cross-links are not duplicated as new facts. |
| Matrix | Named row and column meanings, a defined cell meaning and a visible symbol for unknown or empty. A blank cell does not silently mean “none.” |
| Journey or process flow | Goal, actors, stages, optional branches and handoffs. Arrows claim sequence or movement only when supported by the underlying content. |
| Metric or comparison | Subject, unit, period, reporting basis and qualifiers stay visible; align comparisons on the same basis. |

The [Cloud LAB map](content/cloud-lab.md) is one concrete stage-by-concern example. Its columns, cards and concern accents are specific to that page. Every visual needs a readable list or table for its essential meaning, and an exported view must retain scope and qualifications.

Comparison views preserve each column's subject, scope and period. Differences need explanation, not only highlighted cells. On narrow screens use a labelled scroll region or a stacked equivalent.
