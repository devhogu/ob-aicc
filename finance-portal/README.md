# Financial Services O! workspace trial

This builds the retained 152-page bilingual framework from `html-alt/financial-services/` into `html/financial-services/`. The original routes, cards, desktop grid relationships, CSS-controlled tabs, disclosures and flow-stage modals remain in place. A shared O! header, local fonts and token-level styling supply the common visual language; narrow grids stack to keep their content readable.

```sh
python3 finance-portal/build.py
python3 -m http.server 8906 --bind 0.0.0.0 --directory html/financial-services
```

The generated root opens Russian; every page has an Overview link and a direct counterpart-language link. The original `service.eyebrow` breadcrumb placeholder is rendered as the localized Financial Services label. The source corpus remains a conceptual framework, not a verified current O!Bank architecture. `html/financial-services/` is generated output; edit shared presentation in `finance-portal/assets/` and the retained corpus in `html-alt/financial-services/`.

[Full walkthrough and evidence](verification.md) cover all pages, links, controls and responsive layouts. Run the maintained checks with `portal/tools/with-browser-env.sh portal/.venv/bin/python finance-portal/quality_audit.py geometry`, then `interactions`, `links` and `modals`. The `links` pass clicks every anchor and takes several minutes.
