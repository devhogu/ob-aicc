# START_MODULE_CONTRACT
#   PURPOSE: Hold a translated edition to its Russian source: the same structure on every page pair, no Russian left on its pages, and every translation current against the Russian text it was made from.
#   SCOPE: Reads html/aicc/v2/<lang> and aicc/v2 (content, data files, catalog, i18n); writes nothing.
#   DEPENDS: PyYAML
#   LINKS: C-HUB-V2-EN, M-PORTAL-LOCALIZATION, V-M-PORTAL-LOCALIZATION
# END_MODULE_CONTRACT
#
# START_MODULE_MAP
#   source_hash - the hash of a Russian source as a translation records it
#   signature - the structure of one built page that both editions must share
#   compare - differences between the signatures of a page pair
#   cyrillic - visible Russian text on a translated page
#   staleness - translations missing or made from an older Russian text
# END_MODULE_MAP
"""Parity of a translated edition with the Russian source."""
import hashlib
import json
from html.parser import HTMLParser
from pathlib import Path
import posixpath
import re
from urllib.parse import unquote, urlsplit

import yaml

SRC = Path(__file__).resolve().parents[1]
# attributes whose values must be equal in both editions: they carry identity (progress keys, tabs, cards, anchors of views)
KEYED = ('data-tab', 'data-tab-panel', 'data-step', 'data-node-step', 'data-dot-step', 'data-ring', 'data-seg', 'data-walk', 'data-walk-here',
         'data-map', 'data-map-progress', 'data-kb-open', 'data-kb-detail', 'data-pi', 'data-it', 'data-week', 'data-here-week', 'data-here-it', 'data-road-continue')
# components counted on both sides
COMPONENTS = ('o-card', 'lib-card', 'kb-card', 'kb-map', 'kb-feature', 'rm-card', 'rm-stop', 'lm-level', 'lm-step', 'lm-walk', 'lm-dot', 'lm-node', 'rm-node',
              'tab-panel', 'o-diagram', 'scenario-card', 'rai-cards', 'rai-flow', 'rai-principles', 'here-tile', 'pi-cal', 'kb-column', 'pf-tip', 'lib-chip', 'o-pn')
INLINE = {'a', 'span', 'b', 'strong', 'em', 'i', 'code', 'small', 'sup', 'sub', 'br', 'abbr', 'mark', 'kbd', 'u', 's', 'q', 'time', 'wbr'}
CYRILLIC = re.compile(r'[А-Яа-яЁё]')


def source_hash(text):
    return hashlib.sha1(text.encode('utf-8')).hexdigest()[:12]


def russian_part(data):
    """A data structure without its translations (keys ending in _<lang> other than Russian), so editing English never marks itself stale."""
    if isinstance(data, dict):
        return {k: russian_part(v) for k, v in data.items() if not re.search(r'_(en)$', str(k))}
    if isinstance(data, list):
        return [russian_part(v) for v in data]
    return data


class Signature(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.main = 0
        self.ids, self.headings, self.keyed, self.components, self.tables, self.links = [], [], [], {}, [], []
        self.text = []
        self._skip = []
        self._table = None
        self._svg = 0  # ids inside a drawing come from its content and differ between languages

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'main':
            self.main += 1
        if tag == 'svg':
            self._svg += 1
        if tag in ('br', 'img', 'meta', 'link', 'input', 'hr', 'wbr', 'path', 'circle', 'rect', 'line', 'polyline', 'polygon', 'use', 'stop'):
            self._void(tag, a)
            return
        classes = (a.get('class') or '').split()
        hidden = tag in ('script', 'style', 'template', 'title') or a.get('lang') == 'ru' or 'ru-original' in classes or 'lang-switch' in classes
        self._skip.append(hidden)
        if not self.main:
            return
        self._void(tag, a)
        if tag in ('h1', 'h2', 'h3', 'h4'):
            self.headings.append(tag)
        if tag == 'table':
            self._table = [0, 0]
        elif tag == 'tr' and self._table is not None:
            self._table[0] += 1
        elif tag in ('td', 'th') and self._table is not None and self._table[0] == 1:
            self._table[1] += int(a.get('colspan') or 1)

    def _void(self, tag, a):
        if not self.main:
            return
        if a.get('id') and not self._svg:
            self.ids.append(a['id'])
        for key in KEYED:
            if key in a:
                self.keyed.append(f'{key}={a[key]}')
        for c in (a.get('class') or '').split():
            if c in COMPONENTS:
                self.components[c] = self.components.get(c, 0) + 1
        if tag == 'a' and a.get('href') and 'lang-switch' not in (a.get('class') or ''):
            self.links.append(a['href'])

    def handle_endtag(self, tag):
        if tag in ('br', 'img', 'meta', 'link', 'input', 'hr', 'wbr', 'path', 'circle', 'rect', 'line', 'polyline', 'polygon', 'use', 'stop'):
            return
        if self._skip:
            self._skip.pop()
        if tag == 'svg':
            self._svg -= 1
        if tag == 'main':
            self.main -= 1
        if tag == 'table' and self._table is not None:
            self.tables.append(tuple(self._table))
            self._table = None

    def handle_data(self, data):
        if self.main and not any(self._skip):
            self.text.append(data)


def signature(path):
    sig = Signature()
    sig.feed(Path(path).read_text(encoding='utf-8'))
    return sig


# START_CONTRACT: compare
#   PURPOSE: The differences between the Russian page and its translation that break parity.
#   INPUTS: { ru: Signature; other: Signature; name: str - the page path below the edition; lang: str; ordered: bool - False for a page sorted alphabetically in each language (the vocabulary) }
#   OUTPUTS: { list - error strings }
#   SIDE_EFFECTS: none
# END_CONTRACT: compare
def compare(ru, other, name, lang, ordered=True):
    errors = []
    if (ru.ids != other.ids) if ordered else (sorted(ru.ids) != sorted(other.ids)):
        missing = [i for i in ru.ids if i not in other.ids][:3]
        extra = [i for i in other.ids if i not in ru.ids][:3]
        errors.append(f'{lang}/{name}: anchors differ (missing {missing}, extra {extra})' if missing or extra else f'{lang}/{name}: anchors in another order')
    if ru.headings != other.headings:
        errors.append(f'{lang}/{name}: headings differ ({len(ru.headings)} vs {len(other.headings)})')
    if sorted(ru.keyed) != sorted(other.keyed):
        diff = sorted(set(ru.keyed) ^ set(other.keyed))[:3]
        errors.append(f'{lang}/{name}: keyed components differ {diff}')
    if ru.components != other.components:
        diff = {k: (ru.components.get(k, 0), other.components.get(k, 0)) for k in set(ru.components) | set(other.components) if ru.components.get(k) != other.components.get(k)}
        errors.append(f'{lang}/{name}: components differ {diff}')
    if ru.tables != other.tables:
        errors.append(f'{lang}/{name}: table shapes differ {ru.tables} vs {other.tables}')
    here = posixpath.dirname(f'{lang}/{name}')
    for ref in other.links:
        parts = urlsplit(ref)
        if parts.scheme or parts.netloc or not parts.path:
            continue
        target = posixpath.normpath(posixpath.join(here, unquote(parts.path)))
        if target.startswith('ru/') and lang != 'ru':
            errors.append(f'{lang}/{name}: link into the Russian edition {ref}')
            break
    return errors


def cyrillic(sig):
    """Visible Russian words on a translated page (law originals in brackets are marked lang="ru" and skipped)."""
    text = re.sub(r'\s+', ' ', ' '.join(sig.text))
    return sorted(set(re.findall(r'[А-Яа-яЁё][А-Яа-яЁё-]*', text)))


def _front(text):
    m = re.match(r'---\n(.*?)\n---\n', text, re.S)
    return dict(re.findall(r'^([\w-]+):\s*"?(.*?)"?\s*$', m[1], re.M)) if m else {}


# START_CONTRACT: staleness
#   PURPOSE: Every translation of an edition that is missing or was made from an older Russian text.
#   INPUTS: { lang: str }
#   OUTPUTS: { (list, list) - missing and stale, each as readable strings }
#   SIDE_EFFECTS: none
# END_CONTRACT: staleness
def staleness(lang):
    missing, stale = [], []
    # pages: content/<lang>/x.md carries source_hash of content/ru/x.md
    ru_root, own_root = SRC / 'content' / 'ru', SRC / 'content' / lang
    for path in sorted(ru_root.rglob('*.md')):
        rel = path.relative_to(ru_root)
        own = own_root / rel
        if not own.exists():
            missing.append(f'page content/{lang}/{rel}')
            continue
        if _front(own.read_text(encoding='utf-8')).get('source_hash') != source_hash(path.read_text(encoding='utf-8')):
            stale.append(f'page content/{lang}/{rel}')
    # data files: i18n/sources-<lang>.yaml records the hash of the Russian part of each file when it was translated
    record = {}
    for record_path in sorted((SRC / 'i18n').glob(f'sources-{lang}*.yaml')):  # one record per translator, merged
        record.update(yaml.safe_load(record_path.read_text(encoding='utf-8')) or {})
    data = [p for folder in ('reference', 'learning', 'cards', 'vocabulary') for p in sorted((SRC / folder).glob('*.yaml')) if not p.name.startswith('template')]
    data.append(SRC / 'calendar.json')
    for path in data:
        key = path.relative_to(SRC).as_posix()
        raw = path.read_text(encoding='utf-8')
        loaded = json.loads(raw) if path.suffix == '.json' else yaml.safe_load(raw)
        current = source_hash(json.dumps(russian_part(loaded), ensure_ascii=False, sort_keys=True, default=str))
        if key not in record:
            missing.append(f'data {key}')
        elif record[key] != current:
            stale.append(f'data {key}')
    # catalog: catalog/pages-<lang>/<x> carries "source_hash" of catalog/pages/<x> in its page header
    cat_ru, cat_own = SRC / 'catalog' / 'pages', SRC / 'catalog' / f'pages-{lang}'
    if cat_ru.exists():
        for path in sorted(list(cat_ru.rglob('index.html')) + list(cat_ru.glob('_moved/*.html'))):
            rel = path.relative_to(cat_ru)
            own = cat_own / rel
            if not own.exists():
                missing.append(f'catalog {rel.parent.as_posix() or "."}')
                continue
            head = re.match(r'<!--page (.*?) -->\n', own.read_text(encoding='utf-8'))
            if not head or json.loads(head[1]).get('source_hash') != source_hash(path.read_text(encoding='utf-8')):
                stale.append(f'catalog {rel.parent.as_posix() or "."}')
    return missing, stale
