# START_MODULE_CONTRACT
#   PURPOSE: Write the package root above the frozen v1 site: the chooser page and a redirect for every former page address.
#   SCOPE: Files directly under the package root (index.html, {lang}/**) only; never touches the version folders.
#   DEPENDS: none
#   LINKS: M-AICC-PORTAL, C-HUB-V2
# END_MODULE_CONTRACT
#
# START_MODULE_MAP
#   build - write the chooser and the redirects; return the number of files written
# END_MODULE_MAP
import os
import shutil


def _page(target, title, body=''):
    return (f'<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">'
            f'<meta http-equiv="refresh" content="0; url={target}"><link rel="canonical" href="{target}">'
            f'<title>{title}</title><script>location.replace("{target}"+location.hash)</script></head>'
            f'<body style="font:16px/1.5 system-ui,sans-serif;margin:3rem"><p><a href="{target}">{title}</a></p>{body}</body></html>\n')


# START_CONTRACT: build
#   PURPOSE: Chooser at the package root that forwards to the default version, plus a redirect page at every former address.
#   INPUTS: { package: str - package root; version: str - default version folder; langs: list - language folders }
#   OUTPUTS: { int - files written }
#   SIDE_EFFECTS: Replaces {lang}/ folders and index.html under the package root.
# END_CONTRACT: build
def build(package, version, langs):
    count = 0
    shutil.rmtree(os.path.join(package, 'assets'), ignore_errors=True)
    for lang in langs:
        shutil.rmtree(os.path.join(package, lang), ignore_errors=True)
        base = os.path.join(package, version, lang)
        for folder, _, files in os.walk(base):
            if 'index.html' not in files:
                continue
            rel = os.path.relpath(folder, base).replace(os.sep, '/')
            rel = '' if rel == '.' else rel + '/'
            depth = rel.count('/') + 1
            target = '../' * depth + f'{version}/{lang}/{rel}'
            out = os.path.join(package, lang, rel)
            os.makedirs(out, exist_ok=True)
            with open(os.path.join(out, 'index.html'), 'w', encoding='utf-8') as fh:
                fh.write(_page(target, 'AI Competence Center'))
            count += 1
    with open(os.path.join(package, 'index.html'), 'w', encoding='utf-8') as fh:
        fh.write(_page(f'{version}/', 'AI Competence Center', f'<ul><li><a href="{version}/">Version 1</a></li></ul>'))
    return count + 1
