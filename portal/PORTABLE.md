# Published folder editions

Create the JavaScript-free edition with `python3 portal/tools/export_portable.py --static`. This explicitly refreshes `portal/published/` from the latest generated site; first run `python3 portal/tools/build.py` when content has changed.

Open `portal/published/en/index.html` for English or `portal/published/ru/index.html` for Russian. Each language folder contains the full site and its own assets and can be copied separately. The parent `aicc.html` offers ordinary links to both editions. Keep each edition’s files and subfolders together.

This edition is fixed to the light theme and contains no JavaScript. Workflow popup descriptions become native inline disclosures; stage links reveal their content. Portfolio and delivery views remain visible as linked sections, the Lab keeps its complete matrix, and diagrams have full-size SVG links. Native HTML disclosures and browser title hints still work. Topics replaces scripted search with page and heading links; use the browser’s Find command for text search. Select text to copy and use browser zoom for diagrams. Language, theme, filter and clipboard buttons are omitted. Feedback uses email links.

Validate the package with `portal/tools/with-browser-env.sh portal/.venv/bin/python portal/tools/check_static_export_browser.py`. The check compares authored reading content and workflow stage descriptions with the generated site, validates all links, then opens every page in separately relocated EN/RU folders with JavaScript disabled and a dark OS preference. The report is written to `.runtime/static-export/browser-report.json`.

Generated exports are ignored by Git. `portable-manifest.json` records source and output checksums, route counts and inline stage counts. Regeneration safely replaces only exporter-owned output. It never changes the hosted site or operational records.

## Interactive folder edition

Run `python3 portal/tools/export_portable.py` when a folder edition is needed. It packages the current generated site in `html/aicc/` into `portal/published/`; it does not rebuild the website, upload files, or run automatically. If content has changed since the last site build, first run `python3 portal/tools/build.py`.

Copy the complete `published` folder to the corporate share or a local folder, then open `aicc.html` in a browser and choose English or Russian. Keep `en/`, `ru/` and `assets/` beside the entry point. All internal navigation uses explicit HTML files, including language switches and search results. Search data is bundled as JavaScript; fonts are embedded in CSS. Theme choices travel with internal navigation. Copy buttons fall back to selectable text if browser clipboard access is unavailable.

The exporter validates all internal links, anchors, language counterparts and search destinations before replacing an earlier export. It refuses to overwrite a folder without its generated manifest. `portable-manifest.json` records input and output checksums. Exported files are ignored by Git; source content remains in the existing corpus and portal sources. The HTTP publisher does not refresh this folder.

Run `python3 -m unittest discover -s portal/tests` for regression checks and `portal/.venv/bin/python portal/tools/check_portable_browser.py` to test the exported pages directly through `file://`, without a local server. The browser report goes to `.runtime/portable/browser-report.json`.

External citations, email feedback and links to corporate records still require their normal network access or application. A Windows shared-folder path such as `\\server\share\aicc\aicc.html` must be checked on a corporate workstation: local Chromium verification cannot establish SMB access, browser policies or file associations on that workstation.
