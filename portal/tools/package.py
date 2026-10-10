# START_MODULE_CONTRACT
#   PURPOSE: Write the package root above the frozen v1 site: the chooser page and a redirect for every former page address.
#   SCOPE: Files directly under the package root (index.html, {lang}/**) only; never touches the version folders.
#   DEPENDS: none
#   LINKS: M-AICC-PORTAL, C-HUB-V2
# END_MODULE_CONTRACT
#
# START_MODULE_MAP
#   SOURCES - source folders published inside a version
#   publish_sources - copy the source documents into a version folder with a linked index
#   build - write the chooser and the redirects; return the number of files written
# END_MODULE_MAP
import os
import shutil
from html import escape
from pathlib import Path


def _page(target, title, body='', lang='en'):
    return (f'<!doctype html>\n<html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">'
            f'<meta http-equiv="refresh" content="0; url={target}"><link rel="canonical" href="{target}">'
            f'<title>{title}</title><script>location.replace("{target}"+location.hash)</script></head>'
            f'<body style="font:16px/1.5 system-ui,sans-serif;margin:3rem"><p><a href="{target}">{title}</a></p>{body}</body></html>\n')


# START_CONTRACT: build
#   PURPOSE: The package root forwards straight to the home page (the Hub, version 2, in Russian) with no choice shown, plus a redirect page at every former address of version 1.
#   INPUTS: { package: str - package root; version: str - the version the former addresses belong to; langs: list - language folders; home: str - where the root forwards }
#   OUTPUTS: { int - files written }
#   SIDE_EFFECTS: Replaces {lang}/ folders and index.html under the package root.
# END_CONTRACT: build
def build(package, version, langs, home='v2/ru/index.html'):
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
        fh.write(_page(home, 'Хаб Компетенций по AI', lang='ru'))  # no choice to make: the Hub opens in Russian, English is one click away on every page
    return count + 1


SOURCES = ('charter', 'registry', 'portfolio', 'lab')


# START_CONTRACT: publish_sources
#   PURPOSE: Copy the Markdown source documents of a version into its folder and write a linked index, so the version can be read without the repository.
#   INPUTS: { root: str - repository root; version_dir: str - the built version folder }
#   OUTPUTS: { int - files written }
#   SIDE_EFFECTS: Replaces version_dir/sources.
# END_CONTRACT: publish_sources
def publish_sources(root, version_dir):
    target_root = Path(version_dir) / 'sources'
    shutil.rmtree(target_root, ignore_errors=True)
    listing = []
    for name in SOURCES:
        for path in sorted((Path(root) / name).rglob('*')):
            if path.is_file() and '__pycache__' not in path.parts and path.suffix in ('.md', '.json', '.yaml', '.yml'):
                relative = path.relative_to(root)
                target = target_root / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(path, target)
                listing.append(relative.as_posix())
    groups = {}
    for item in listing:
        groups.setdefault('/'.join(item.split('/')[:2]), []).append(item)
    body = ''.join(f'<h2>{escape(group)}</h2><ul>' + ''.join(f'<li><a href="{escape(item)}">{escape(item)}</a></li>' for item in items) + '</ul>'
                   for group, items in sorted(groups.items()))
    (target_root / 'index.html').write_text(
        '<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Source documents</title></head>'
        '<body style="font:16px/1.5 system-ui,sans-serif;max-width:60rem;margin:2rem auto;padding:0 1rem">'
        '<h1>Source documents of the site</h1><p>The Markdown documents the site is built from. <a href="../ru/center/">Back to the site</a></p>'
        + body + '</body></html>\n', encoding='utf-8')
    return len(listing) + 1
