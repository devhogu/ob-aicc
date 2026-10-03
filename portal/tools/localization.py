"""Canonical English sources and reviewed language views of the same content."""
# START_MODULE_CONTRACT
# PURPOSE: Select a reviewed translation or an explicitly identified English fallback.
# SCOPE: Source identity, freshness, structural validation, and paired table extraction.
# DEPENDS: none
# LINKS: M-PORTAL-LOCALIZATION, V-M-PORTAL-LOCALIZATION
# END_MODULE_CONTRACT
# START_MODULE_MAP
# LANGUAGES - supported source language codes
# ROOTS - language-specific source areas
# front_matter - read the corpus's flat YAML metadata fence
# canonical_path - map a language source path to its English identity
# Source - selected text with its real language and canonical identity
# Sources - resolve and validate source files for one requested language
# validate_translations - validate the entire Russian source tree
# END_MODULE_MAP
import hashlib
import re
from dataclasses import dataclass
from pathlib import Path

LANGUAGES = ('en', 'ru')
ROOTS = ('charter', 'registry', 'portfolio', 'portal/content')


def front_matter(text):
    match = re.match(r'```yaml\n(.*?)```', text, re.S)
    if not match:
        return {}
    return dict((key.strip(), value.strip()) for line in match[1].splitlines()
                if ':' in line for key, value in [line.split(':', 1)])


def canonical_path(path):
    for root in ROOTS:
        for lang in LANGUAGES:
            prefix = f'{root}/{lang}/'
            if path.startswith(prefix):
                return f'{root}/en/' + path[len(prefix):]
    return path


def _tables(text):
    tables, current = [], []
    fenced = False
    for line in text.splitlines() + ['']:
        if line.startswith('```'):
            fenced = not fenced
        if not fenced and line.startswith('|'):
            current.append([x.strip() for x in re.split(r'(?<!\\)\|', line.strip().strip('|'))])
        elif current:
            tables.append(current)
            current = []
    return tables


@dataclass(frozen=True)
class Source:
    canonical: str
    path: str
    language: str
    text: str
    metadata: dict


class Sources:
    def __init__(self, root, language):
        if language not in LANGUAGES:
            raise ValueError(f'Unsupported language: {language}')
        self.root = Path(root)
        self.language = language
        self.cache = {}

    def resolve(self, path):
        canonical = canonical_path(path)
        if canonical in self.cache:
            return self.cache[canonical]
        original = self.root / canonical
        raw = original.read_bytes()
        text = raw.decode('utf-8')
        meta = front_matter(text)
        source = Source(canonical, canonical, 'en', text, meta)
        translated = canonical
        for root in ROOTS:
            prefix = f'{root}/en/'
            if canonical.startswith(prefix):
                translated = f'{root}/{self.language}/' + canonical[len(prefix):]
                break
        candidate = self.root / translated
        if translated != canonical and candidate.is_file():
            translated_text = candidate.read_text(encoding='utf-8')
            translated_meta = front_matter(translated_text)
            status = translated_meta.get('translation_status', 'draft')
            if status not in ('draft', 'reviewed'):
                raise ValueError(f'{translated}: unknown translation_status {status}')
            if status == 'reviewed':
                required = {'source': canonical, 'source_sha256': hashlib.sha256(raw).hexdigest()}
                if meta.get('revision'):
                    required['source_revision'] = meta['revision']
                if meta.get('id'):
                    required['id'] = re.sub(r'-EN$', '-' + self.language.upper(), meta['id'])
                    required['status'] = meta['status']
                for key, value in required.items():
                    if translated_meta.get(key) != value:
                        raise ValueError(f'{translated}: {key} does not match the English source; review required')
                # Stable clause numbers and tables are the structural contract used by routes and projections.
                for pattern in (r'^#{2,6} (\d+(?:\.\d+)*)\.', r'^(\d+(?:\.\d+)+)\.\s'):
                    if re.findall(pattern, text, re.M) != re.findall(pattern, translated_text, re.M):
                        raise ValueError(f'{translated}: numbered sections or clauses differ from the English source')
                original_tables, translated_tables = _tables(text), _tables(translated_text)
                shapes = lambda tables: [[len(row) for row in table] for table in tables]
                if shapes(original_tables) != shapes(translated_tables):
                    raise ValueError(f'{translated}: table structure differs from the English source')
                # Record identities and dated facts stay shared across translated views.
                if canonical.startswith(('registry/en/', 'portfolio/en/')):
                    pattern = r'\b(?:[A-Z]{2,5}-\d[\w-]*|\d{4}-\d{2}-\d{2})\b'
                    strip_meta = lambda s: re.sub(r'^```yaml\n.*?```\s*', '', s, count=1, flags=re.S)
                    if sorted(re.findall(pattern, strip_meta(text))) != sorted(re.findall(pattern, strip_meta(translated_text))):
                        raise ValueError(f'{translated}: record identifiers or dates differ from the canonical record')
                source = Source(canonical, translated, self.language, translated_text, translated_meta)
        self.cache[canonical] = source
        return source

    def text(self, path):
        return self.resolve(path).text

    def table(self, path, header_start, canonical_keys=()):
        """Use English column identities and table position, with translated cell text.

        Canonical key columns keep stable lookup identities (e.g. Role). Display
        translations are available under _localized_<key> without changing callers.
        """
        canonical = canonical_path(path)
        original = (self.root / canonical).read_text(encoding='utf-8')
        source = self.resolve(canonical)
        english_tables, selected_tables = _tables(original), _tables(source.text)
        headers = [x.strip() for x in header_start.strip().strip('|').split('|')]
        for index, table in enumerate(english_tables):
            if table[0][:len(headers)] == headers:
                result = []
                for en_row, row in zip(table[2:], selected_tables[index][2:]):
                    record = dict(zip(table[0], row))
                    record['_labels'] = dict(zip(table[0], selected_tables[index][0]))
                    original_record = dict(zip(table[0], en_row))
                    for key in canonical_keys:
                        record['_localized_' + key] = record[key]
                        record[key] = original_record[key]
                    result.append(record)
                return result
        return []


def validate_translations(root):
    """Validate every translation, including records not projected into the portal."""
    root = Path(root)
    sources = Sources(root, 'ru')
    counts = {'reviewed': 0, 'draft': 0}
    for area in ROOTS:
        for path in sorted((root / area / 'ru').rglob('*.md')):
            relative = path.relative_to(root).as_posix()
            canonical = canonical_path(relative)
            if not (root / canonical).is_file():
                if path == root / area / 'ru' / 'README.md':
                    continue  # translation-workspace introduction, not corpus content
                raise ValueError(f'{relative}: no canonical English source')
            selected = sources.resolve(canonical)
            counts['reviewed' if selected.language == 'ru' else 'draft'] += 1
    return counts
