# Cloud LAB: flow-first O! workspace

This recipe records the accepted **version C** of AICC's Cloud LAB page. It combines the O! workspace shell with the original page's visible flow map. The page itself is `html/cloudlab/index.html`; its active CSS and JavaScript are in `html/cloudlab/assets/`. It is a concrete reference, not a template whose Cloud LAB content belongs in every portal.

## Choose the view by meaning

| Meaning to convey | Suitable visual | Reader should infer |
| --- | --- | --- |
| Ordered work across concerns | Stage-by-concern map | Progresses left to right through named stages; rows show contributions by concern |
| A set of abilities | Capability strip | The operating model has these abilities; the strip alone does not prove temporal order |
| A recurring cycle | Loop | Output feeds the next cycle; the return arrow has a stated meaning |
| Two interacting systems | Paired relationship view | Distinct responsibilities and the connection between them |
| Details, qualifications and guardrails | Text sections after the visual | Full wording, limits and context that a compact map cannot hold |

Do not turn a classification into a flow by adding arrows. A map's order is a claim: state whether it is a typical pathway, required sequence or merely a reading order. In Cloud LAB the six columns indicate stage order. Cards within a cell **do not** assert individual dependencies.

## Page anatomy

1. Keep the O! identity and page scope in a compact, sticky top header. Keep a named theme control there only if both themes are implemented. Use `--header-height` and anchored section `scroll-margin-top` so the header never covers destinations.
2. Put stable section navigation in the left rail. Show the selected section. At narrow widths collapse the rail into a labelled disclosure. On a dense map page the central canvas gets the full remaining width; omit a permanent right rail.
3. Explain the page's purpose in one short paragraph, then show the primary diagram early. The map should be visible without crossing several prose sections.
4. Give the diagram a labelled, keyboard-focusable scroll region when it genuinely needs two dimensions. Only that region scrolls sideways; the document does not overflow. Offer a map-focus control on wide screens that hides navigation and can restore it.
5. Follow the map with a short inspector for the selected activity and a link to that stage's notes. Keep full stage descriptions, other conceptual diagrams and guardrails after the map.

Cloud LAB uses six stages by five concerns and 41 selectable activity cards. These numbers came from its source material. Choose axes and density from each new subject; do not copy these counts as a site standard.

## Map interactions

Each activity card in the trial is a real button. Selection sets `aria-pressed` and updates a nearby inspector with the full activity name, description, stage and concern. The trial's static cards do not have durable record IDs; assign stable IDs when building a data-driven map so selection, links and content updates can follow the same activity. A selected card needs a visible non-colour cue and a clear focus ring. The map-focus button also reports its pressed state. Keep activity names visible; truncation may be used only when the full wording is recoverable by the inspector and keyboard.

Stage notes use matching IDs so a reader can move from the compact map to detail. A text pathway or structured stage list should expose the same essential information when the visual is hard to scan. Preserve the distinction between a stage, a concern, an activity and a dependency; they are different concepts.

## Visual language and reusable source

Use the shared O! semantic tokens and the **TT Norms Pro + Golos Text** pair. The O! mark is the global identity. Provider marks identify a subject, not a new theme. The header can carry the burgundy-to-near-black treatment; the working canvas stays quiet and opaque. A single accent per concern helps orientation, but labels and position carry the meaning. Use restrained borders and spacing rather than a card around every paragraph.

The current page demonstrates the implementation split:

| AICC file | Role |
| --- | --- |
| `html/cloudlab/index.html` | Semantic page structure and Cloud LAB-specific content |
| `html/cloudlab/assets/base.css`, `palette.css`, `tokens.css`, `fonts.css` | Base presentation and shared visual values |
| `html/cloudlab/assets/workspace.css`, `reframed.css` | O! shell and stage-detail presentation |
| `html/cloudlab/assets/converged.css`, `converged.js` | Sticky layout, map focus, selection and inspector |
| `html/cloudlab/assets/reframed.js` | Theme control and page navigation |

For a new site, start with the generated shared guide CSS and its [foundations](content/foundations.md), [layout](content/layout.md) and [component rules](content/components.md). Reuse the Cloud LAB **composition and interaction rules** only where the subject has an actual ordered flow. Keep content and IDs in the consuming application; do not hard-code Cloud LAB's activities as shared components.

## Review a new application of this pattern

- Can a reader tell what flows, what is grouped, and what is only related?
- Can the primary map be read and selected by keyboard, with visible focus and full labels available?
- Does the map remain usable at 320px through its local scroll region, without horizontal page overflow?
- Do sticky elements leave anchor destinations and selected details visible?
- Do light/dark presentation, Russian/English wording or a clearly labelled language fallback preserve hierarchy and meaning?
- Are map content and claims supplied by the consuming product, with uncertain or illustrative statements labelled there?

The supplied Cloud LAB page is an accepted visual and interaction trial. Its activity text is an example of that project; this style guide does not validate those operational claims.
