# START_MODULE_CONTRACT
#   PURPOSE: Write the language entry /{lang}/ as a forward to the Center, which is where the site opens.
#   SCOPE: One redirect page per language; no content of its own.
#   DEPENDS: M-PORTAL-SOURCE
#   LINKS: M-PORTAL-NEIGHBOURS, V-M-PORTAL-NEIGHBOURS
# END_MODULE_CONTRACT
# START_MODULE_MAP
#   build - write both language entries
# END_MODULE_MAP
"""The entry at /{lang}/: it forwards to the Center."""
from pathlib import Path

import workspace


def build(output):
    output = Path(output)
    for lang in ('en', 'ru'):
        target = workspace.relative(f'/{lang}/', workspace.route(lang, 'center'))
        title = workspace.messages(lang)['site_name']
        page = (f'<!doctype html>\n<html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">'
                f'<meta http-equiv="refresh" content="0; url={target}"><link rel="canonical" href="{target}">'
                f'<title>{title}</title><script>location.replace("{target}"+location.hash)</script></head>'
                f'<body><h1><a href="{target}">{title}</a></h1></body></html>\n')
        entry = output / lang / 'index.html'
        entry.parent.mkdir(parents=True, exist_ok=True)
        entry.write_text(page, encoding='utf-8')
    return 2
