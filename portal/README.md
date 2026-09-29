# AICC portal source

Editable home for the AICC portal: tokens, UI kit, content, templates, and build tools.
The generated site goes to `../html/aicc/` and is never edited by hand.

## Provenance

`tokens/` and `ui-comps/` were copied on 2026-09-29 from the sibling EA portal
(`/devops/obank/ea/portal`). There is no live link. This repository may diverge.

Left behind on purpose: the EA gallery, raw site captures (`collection/`), and examples.
Apple's SF Pro Display was not copied because its licence is not the group's.

## Fonts and brand

- Headings: TT Travels Text. Body: Golos Text. Both are the faces used on the O!Bank site.
- TT Norms Pro and TT Travels Text are group fonts. The practitioner has authorised them for
  bank-internal portals and bank communications. The portal is served behind the bank network.
  Publishing outside the bank network needs a new decision.
- Logos in `ui-comps/logos/` are extracted from public O! sites. Use them as-is, never recolour.
  The O!Bank logo exists only in an on-dark variant, so the header is dark in both themes.

## Build and check

```sh
python3 portal/tools/build.py                       # regenerate html/aicc/
python3 portal/tools/check.py --idempotent          # static checks and repeatable-build check
bash portal/tools/setup_browser.sh                  # once per checkout: venv, Playwright, Chromium, rootless system libs
portal/.venv/bin/python portal/tools/browser_check.py   # browser check; writes portal/verification/
```

`portal/.venv/` and `portal/.tools/` are local and git-ignored. Chromium itself is cached per user in
`~/.cache/ms-playwright`. Python 3.11+ is required.
