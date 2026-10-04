# CSR trial verification

2 October 2026. From the AICC repository root:

```sh
python3 csr-portal/build.py
portal/tools/with-browser-env.sh portal/.venv/bin/python csr-portal/verify.py
portal/tools/with-browser-env.sh portal/.venv/bin/python csr-portal/audit.py
```

The browser run passed Russian and English pages in dark and light themes at 1440, 768, 390 and 320 px: 16 layout cases, no document overflow, external requests, HTTP errors or JavaScript errors. Interactions checked: stage-to-inspector selection and URL state, map focus and restoration, language switch to the corresponding section, theme persistence, keyboard-open/zoom/Escape/focus restoration in the diagram viewer, and mobile navigation. The machine-readable result is [verification/report.json](verification/report.json).

The deeper [headless audit](verification/audit.json) compared the rendered wording of all 18 document sections with the retained source and checked all 268 original anchor links (198 distinct targets). It physically clicked all 198 left-navigation links on desktop and the 18 document overview links on mobile. It opened and closed all 68 embedded diagrams on desktop and again on mobile, checking SVG restoration, focus and the visible Close control. All checks passed. The audit found an active-navigation defect in the first build: the previous document could remain highlighted at a long section boundary. The generated page now selects the section by its actual scroll position and jumps immediately through the large document.

An axe-core run on both languages in both themes at desktop and 390 px found zero WCAG 2 A/AA and 2.1 AA violations across eight cases. Wide diagrams and tables retain local scrolling; the proposal's SVG diagrams use a light canvas in both themes to preserve their embedded text and colour rules.

This is a restyled **project proposal** and conceptual workflow. It neither confirms current Bank practice nor selects a pilot journey, appoints owners or approves a system design. The shared shell and map are presentation code; source wording continues to come from the retained bilingual pages.
