#!/usr/bin/env python3
"""Validate individual Russian sources against their English comparison files and report calque markers.

Usage: python3 check_one.py charter/ru/documents/business-model.md portal/content/ru/services/catalog.md
Runs the same structural validation as the build (front matter, numbered sections and clauses, tables)
for each file, then prints the scan markers that remain in it.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / 'portal' / 'tools'))
sys.path.insert(0, str(HERE))

from localization import Sources, canonical_path  # noqa: E402
import scan  # noqa: E402


def main(paths):
    sources = Sources(ROOT, 'ru')
    report = scan.scan()['files']
    failed = False
    for name in paths:
        rel = Path(name).resolve().relative_to(ROOT).as_posix() if Path(name).exists() else name
        try:
            if rel.endswith('.md') and '/ru/' in rel and not rel.endswith('translation-en-ru-map.md'):
                selected = sources.resolve(canonical_path(rel))
                if selected.language != 'ru':
                    raise ValueError('not selected as a reviewed Russian source')
            status = 'OK'
        except Exception as error:  # report every file, then fail
            status = 'FAIL: %s' % error
            failed = True
        markers = report.get(rel, {})
        print('%s  %s' % (rel, status))
        if markers:
            print('   rejected forms: %s' % (markers.get('rejected') or 'none'))
            print('   latin words: %s %s' % (markers.get('latin'), markers.get('latin_sample')))
            print('   capitalised terms (heuristic): %s' % markers.get('capitalised_terms'))
    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
