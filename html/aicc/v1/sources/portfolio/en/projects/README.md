# Projects

The register of the projects. A project is the delivery of one Initiative: its documents, from the Initiative Brief and the scoping through the Solution design, the controls and the readiness for release. The state of the Initiative is in the [Portfolio Backlog](../portfolio-backlog.md), and the state of its Capabilities and Features is in the [Program Backlog](../program-backlog.md); the project documents do not hold a state of their own.

| Project | Initiative | State of the Initiative | Documents |
| --- | --- | --- | --- |
| service-resolution | INI-013 Customer Intelligence–Enabled Service Resolution | As in the Portfolio Backlog | [service-resolution/](service-resolution/start.md) |

A project folder is opened when an Initiative needs documents beyond its Initiative Brief, and it is named with a short key. Each document of the project is one Markdown file in each language, with the same file name, headings, identifiers, tables, and diagrams in both: `start.md` (the overview), `charter.md`, `journeys.md` and one file for each journey, `governance.md`, `how-it-works.md`, `controls.md`, `technical-design.md`, `journey-profiles.md`, and `it-readiness.md`.

How a document is written:

- The front matter names the document (`key`) and its menu label (`label`); the overview also carries the line above its title (`eyebrow`), its summary (`lede`), and its short facts (`pills`).
- A heading that other pages link to carries its identifier at the end, `## Hypothesis {#charter-hypothesis}`, and a link to it is written `[text](#charter-hypothesis)`. The language prefix is added when the site is built.
- A table cell that holds only `<` is merged into the cell on its left.
- A diagram is a `mermaid` code block that starts with `%% id:` and `%% caption:` lines.
- On the overview, a list after `<!-- flow -->` is shown as the value flow, and a list of `- [Title](#document): description` after `<!-- cards -->` is shown as cards.
