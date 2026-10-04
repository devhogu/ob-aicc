# STS trial verification

2 October 2026. The generated static package is a design trial based on `html-alt/sts/en/`; it does not assert that the conceptual STS model is the current O!Bank service inventory or operating assignment.

From the AICC repository root:

```sh
python3 sts-portal/build.py
portal/tools/with-browser-env.sh portal/.venv/bin/python sts-portal/verify.py
```

The browser run passed all eight pages across dark/light themes and 1440, 768, 390 and 320 px widths: 64 layout cases, no page overflow, external requests, HTTP errors or JavaScript errors. It also passed five interaction suites for the lifecycle map and deep links, map focus, theme persistence, reference keyboard tabs, the three prototype inspectors and mobile navigation. Source headings remain in order after the new framing headings. The machine-readable result is in [verification/report.json](verification/report.json).

An axe-core pass on the eight pages in both themes found zero WCAG 2 A/AA and 2.1 AA violations in 16 cases. Visual inspection covered desktop light/dark and mobile layouts. Wide prototype diagrams scroll within their own region on mobile, with a visible scroll hint and keyboard focus. The source remains English-only; this trial does not provide bilingual content or a production data model.
