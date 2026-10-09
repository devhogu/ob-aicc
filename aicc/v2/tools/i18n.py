# START_MODULE_CONTRACT
#   PURPOSE: The edition language of a build and its words: interface strings, plurals, months and localized data fields, Russian being the source.
#   SCOPE: Holds the current language for one edition's build; reads aicc/v2/i18n/ui-<lang>*.yaml. Russian text passes through unchanged, so the Russian edition is byte-identical to a build without this module.
#   DEPENDS: PyYAML
#   LINKS: C-HUB-V2-EN, M-PORTAL-LOCALIZATION
# END_MODULE_CONTRACT
#
# START_MODULE_MAP
#   SOURCE - the source language ('ru')
#   use - set the edition language for the build that follows
#   lang - the current edition language
#   T - an interface string in the edition language, formatted with named values
#   P - the plural form of a word for a count
#   loc - a data field in the edition language (field_<lang> beside field)
#   table - the whole translation table of the edition (for the page script)
#   missing - Russian strings that had no translation in this build
# END_MODULE_MAP
"""Edition language: T('Русская строка {n}', n=3) gives the edition's text; Russian passes through."""
from pathlib import Path

import yaml

SOURCE = 'ru'
HERE = Path(__file__).resolve().parents[1] / 'i18n'
_state = {'lang': SOURCE}
_tables = {}
_missing = set()


def use(language):
    _state['lang'] = language


def lang():
    return _state['lang']


def table(language=None):
    """Russian string -> edition string, merged from every i18n/ui-<lang>*.yaml."""
    language = language or lang()
    if language not in _tables:
        merged = {}
        for path in sorted(HERE.glob(f'ui-{language}*.yaml')):
            for key, value in (yaml.safe_load(path.read_text(encoding='utf-8')) or {}).items():
                merged[str(key)] = str(value)
        _tables[language] = merged
    return _tables[language]


# START_CONTRACT: T
#   PURPOSE: An interface string in the edition language. The Russian string is its own key; values are put in with str.format.
#   INPUTS: { text: str - the Russian string; context: str - optional, picks the table entry 'text|context' when there is one; values: named values for {placeholders} }
#   OUTPUTS: { str - the edition's string; the Russian one when the edition is Russian or has no translation (recorded as missing) }
#   SIDE_EFFECTS: Records a missing translation.
# END_CONTRACT: T
def T(text, context=None, **values):
    if lang() != SOURCE:
        found = table().get(f'{text}|{context}') if context else None  # a word that reads differently in one place: 'Готово к старту|point'
        found = found if found is not None else table().get(text)
        if found is None:
            _missing.add(text)
        else:
            text = found
    return text.format(**values) if values else text


def P(n, forms):
    """forms: the three Russian forms (one, few, many); in another edition the table gives 'one|other' under 'one|few|many'."""
    if lang() == SOURCE:
        n10, n100 = abs(n) % 10, abs(n) % 100
        return forms[0] if n10 == 1 and n100 != 11 else forms[1] if 2 <= n10 <= 4 and not 12 <= n100 <= 14 else forms[2]
    key = '|'.join(forms)
    found = table().get(key)
    if found is None:
        _missing.add(key)
        return forms[2]
    one, _, other = found.partition('|')
    return one if abs(n) == 1 else (other or one)


def loc(obj, field):
    """A data field in the edition language: obj[field + '_' + lang] beside the Russian obj[field]."""
    if lang() != SOURCE:
        value = obj.get(f'{field}_{lang()}')
        if value not in (None, ''):
            return value
        if obj.get(field) not in (None, ''):
            _missing.add(f'{field}: {str(obj.get(field))[:60]}')
    return obj.get(field)


def missing():
    return sorted(_missing)
