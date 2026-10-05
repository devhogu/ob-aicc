# Portable folder edition

Run `python3 portal/tools/export_portable.py` when a folder edition is needed. It packages the current generated site in `html/aicc/` into `portal/published/`; it does not rebuild the website, upload files, or run automatically. If content has changed since the last site build, first run `python3 portal/tools/build.py`.

Copy the complete `published` folder to the corporate share or a local folder, then open `aicc.html` in a browser and choose English or Russian. Keep `en/`, `ru/` and `assets/` beside the entry point. All internal navigation uses explicit HTML files, including language switches and search results. Search data is bundled as JavaScript; fonts are embedded in CSS. Theme choices travel with internal navigation. Copy buttons fall back to selectable text if browser clipboard access is unavailable.

The exporter validates all internal links, anchors, language counterparts and search destinations before replacing an earlier export. It refuses to overwrite a folder without its generated manifest. `portable-manifest.json` records input and output checksums. Exported files are ignored by Git; source content remains in the existing corpus and portal sources. The HTTP publisher does not refresh this folder.

Run `python3 -m unittest discover -s portal/tests` for regression checks and `portal/.venv/bin/python portal/tools/check_portable_browser.py` to test the exported pages directly through `file://`, without a local server. The browser report goes to `.runtime/portable/browser-report.json`.

External citations, email feedback and links to corporate records still require their normal network access or application. A Windows shared-folder path such as `\\server\share\aicc\aicc.html` must be checked on a corporate workstation: local Chromium verification cannot establish SMB access, browser policies or file associations on that workstation.
