# AICC O! UI/UX kit verification

Checked version 0.1.1 on 2 October 2026 from the AICC checkout.

- `python3 obank-uiux/design-system/build.py --output obank-uiux/site` built nine pages (eight guide sections and the examples page), seven interactive patterns and 97 packaged files.
- `python3 obank-uiux/design-system/check_package.py obank-uiux/site` passed: 251 served references and 241 downloaded-kit references resolve; all 97 served and 95 downloaded file hashes match their manifests.
- All 108 entries in `ui-comps/manifest.json` resolve to local curated asset files.
- Browser verification passed 180 layout cases across light/dark, Russian/English shell and 1440/768/320px widths; 30 desktop automated accessibility cases had no violations. Catalogue, profile tabs, flow selection, form review, filters, search, theme/language, mobile navigation and downloads passed. Full results are in `verification-artifacts/verification.json` and `layout-accessibility.json`.

The guide's factual examples are fictional. Its checks establish guide behaviour, not adoption or functionality of another AICC portal. The Cloud LAB version C page was verified separately when accepted; its operational text remains illustrative for this design kit.
