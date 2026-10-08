#!/usr/bin/env python3
# START_MODULE_CONTRACT
#   PURPOSE: Assemble the walkable end-to-end pack of v1: the folder edition of the site plus the source documents, and a zip for sharing.
#   SCOPE: Writes only the output folder (default portal/published) and the zip beside it; reads the built html/aicc/v1 and the source folders.
#   DEPENDS: export_portable
#   LINKS: M-PORTABLE-EXPORT, C-HUB-V2
# END_MODULE_CONTRACT
#
# START_MODULE_MAP
#   SOURCES - source folders copied into the pack
#   pack - export the folder edition, add the sources and their index, write the zip
# END_MODULE_MAP
"""Pack v1 end to end: open aicc.html in the folder, or share the zip."""
import argparse
import hashlib
from html import escape
from pathlib import Path
import shutil
import zipfile

import export_portable

ROOT = Path(__file__).resolve().parents[2]
SOURCES = ('charter', 'registry', 'portfolio', 'lab')
TOP = 'aicc-v1'


# START_CONTRACT: pack
#   PURPOSE: Export the folder edition of v1, add the source documents with a linked index, and write the zip.
#   INPUTS: { source: Path - built v1 site; output: Path - pack folder; archive: Path - zip file }
#   OUTPUTS: { dict - file counts and the zip checksum }
#   SIDE_EFFECTS: Replaces the output folder and the zip.
# END_CONTRACT: pack
def pack(source, output, archive):
    export_portable.export(source, output)
    listing = []
    for name in SOURCES:
        for path in sorted((ROOT / name).rglob('*')):
            if path.is_file() and '__pycache__' not in path.parts and path.suffix in ('.md', '.json', '.yaml', '.yml'):
                relative = Path('sources') / path.relative_to(ROOT)
                target = output / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(path, target)
                listing.append(relative.as_posix())
    groups = {}
    for item in listing:
        groups.setdefault('/'.join(item.split('/')[1:3]), []).append(item)
    body = ''.join(
        f'<h2>{escape(group)}</h2><ul>' + ''.join(f'<li><a href="{escape(item[len("sources/"):])}">{escape(item[len("sources/"):])}</a></li>' for item in items) + '</ul>'
        for group, items in sorted(groups.items()))
    (output / 'sources' / 'index.html').write_text(
        '<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Source documents</title></head>'
        '<body style="font:16px/1.5 system-ui,sans-serif;max-width:60rem;margin:2rem auto;padding:0 1rem">'
        '<h1>Source documents of the site</h1><p>The Markdown documents the site is built from. '
        '<a href="../aicc.html">Back to the site</a></p>' + body + '</body></html>\n', encoding='utf-8')
    with (output / 'README.txt').open('a', encoding='utf-8') as fh:
        fh.write('\nsources/ holds the Markdown documents the site is built from (charter, registry, portfolio, lab); open sources/index.html to browse them.\n')
    archive.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) as bundle:
        for path in sorted(p for p in output.rglob('*') if p.is_file()):
            bundle.write(path, Path(TOP) / path.relative_to(output))
    return {'site_files': sum(1 for p in output.rglob('*') if p.is_file()) - len(listing) - 1, 'source_files': len(listing),
            'zip': str(archive), 'zip_bytes': archive.stat().st_size, 'zip_sha256': hashlib.sha256(archive.read_bytes()).hexdigest()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, default=ROOT / 'html/aicc/v1')
    parser.add_argument('--output', type=Path, default=ROOT / 'portal/published')
    parser.add_argument('--zip', type=Path, default=ROOT / 'portal/aicc-v1.zip')
    args = parser.parse_args()
    for key, value in pack(args.source, args.output, args.zip).items():
        print(f'{key}: {value}')


if __name__ == '__main__':
    main()
