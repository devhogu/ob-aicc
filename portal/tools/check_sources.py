#!/usr/bin/env python3
"""Verify pinned English sources and all Russian translation metadata."""
import hashlib
import json
from pathlib import Path

from localization import validate_translations

ROOT = Path(__file__).resolve().parents[2]


def english_fields(value):
    if isinstance(value, list):
        return [english_fields(item) for item in value]
    if isinstance(value, dict):
        if value and set(value) <= {'en', 'ru', 'ky'}:
            return english_fields(value['en'])
        return {key: english_fields(item) for key, item in value.items()}
    return value


def check(root=ROOT):
    manifest = json.loads((root / 'portal/translation-source.json').read_text())
    for entry in manifest['files']:
        path = root / entry['path']
        raw = path.read_bytes()
        if entry['hash_basis'] == 'english_projection':
            raw = json.dumps(english_fields(json.loads(raw)), ensure_ascii=False,
                             sort_keys=True, separators=(',', ':')).encode('utf-8')
        if hashlib.sha256(raw).hexdigest() != entry['sha256']:
            raise ValueError(f'{entry["path"]}: changed since the pinned English source; reconcile the source baseline')
    expected = set()
    for area in ('charter', 'registry', 'portfolio', 'portal/content'):
        expected.update(path.relative_to(root).as_posix() for path in (root / area / 'en').rglob('*.md'))
    listed = {entry['path'] for entry in manifest['files'] if entry['path'].endswith('.md')}
    if expected != listed:
        raise ValueError(f'English source inventory differs: {sorted(expected ^ listed)}')
    counts = validate_translations(root)
    print(f'English source hashes: {len(manifest["files"])} verified; reviewed Russian translations: {counts["reviewed"]}.')


if __name__ == '__main__':
    check()
