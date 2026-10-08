# AI Competence Hub (version 2)

Source of the Hub site. It is self-contained: its own interface kit copy (`ui/`), its own build and check tools, its own content. Russian is the source language; English will be translated later.

- `content/ru/` the pages (Markdown with a front matter of `title`, `summary`, `order`)
- `vocabulary/terms-*.yaml` the terms; a page writes `[[funnel]]` or `[[funnel|воронки]]` and the site shows «воронка (funnel)» linked to the vocabulary
- `cards/` the project cards (later)
- `site.json` names, sections, messages and the wording the check refuses

```
python3 aicc/v2/tools/build.py                # html/aicc/v2
python3 aicc/v2/tools/check.py --idempotent   # rebuild, compare, check links, ids, chip, wording
python3 -m unittest discover -s aicc/v2/tests
```

Every address names its file (`.../index.html`), so the built folder also opens straight from a file manager.
