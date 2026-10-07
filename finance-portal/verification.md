# Financial Services O! walkthrough

Checked 2 October 2026 against the generated `html/financial-services/` package. The [full Chromium report](verification/quality-report.json) covers every one of the 152 EN/RU pages; [baseline and current screenshots](verification/preview) show the recurring layout families. The retained source is `html-alt/financial-services/`.

| Check | Result |
| --- | ---: |
| Page routes and content | 152/152 match the source page body, apart from localized breadcrumb labels |
| Static targets, assets, IDs and ARIA references | 3,742 local references checked; no missing target, duplicate ID or dangling reference |
| Rendered pages | 912 loads: every page at 1440, 1024, 768, 600, 390 and 320 px |
| Expanded-content layouts | 304 page/width combinations with all disclosures open |
| Clipping, overlap, broken assets and high layout shift | None detected in the rendered sweep |
| Link reachability | 3,308 visible-link hit tests after expansion; no obscured or unnamed link |
| Actual link activation | All 3,612 desktop/mobile anchor clicks reached their expected destinations; 1,600 fragment clicks revealed their targets |
| Disclosures and tabs | All 2,296 disclosures toggled; all 100 tab labels selected the matching visible panel |
| Stage controls | All 472 buttons opened populated modals and closed with Escape, restoring focus |
| Modal fit | 1,416 stage/width combinations at 1440, 390 and 320 px; long content scrolls inside the dialog |

The link activation pass opened each clicked destination in a disposable browser tab so the source page stayed available for the next link. Separate same-tab journeys passed at desktop and mobile widths: overview → Finance & Treasury → ALM → RU counterpart → RU overview. The sticky O! header remained in place while scrolling at 1440, 390 and 320 px. Closing a modal by its button or backdrop also returned focus to the stage button in both languages.

The walkthrough corrected four issues found in the retained presentation: two-column cards hiding text on narrow screens, a long slash-separated scenario phrase clipping at 390/320 px, first-load font movement on the home pages, and missing keyboard focus handling in the stage dialog and CSS-only tabs. The generated Russian home breadcrumb now reads “Финансовые услуги.” These are shared skin/behavior changes; the original page grids, cards, content, tab rules and stage data remain the source.

**Russian navigation correction, 2 October:** the retained Russian child pages carried English section names in 66 parent breadcrumbs, for example “Strategic Banking Portfolio” above “Распределение капитала.” The build now takes each parent label from that section's Russian index page. Static verification checks all child breadcrumbs against their section titles and rejects unmarked cross-language links. Chromium also clicks every Russian child-page parent breadcrumb and confirms it lands in the Russian section.

The corpus is a conceptual banking framework, not a verified current O!Bank architecture. This is a Chromium layout and interaction audit, not a factual review or a cross-browser certification. The trial remains outside AICC's `html/aicc` production publisher.
