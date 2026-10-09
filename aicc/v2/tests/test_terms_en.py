"""English term list (aicc/v2/i18n/terms-en.yaml): complete over the vocabulary, one English per Russian term, no forbidden wording."""
from pathlib import Path
import re
import unittest

import yaml

V2 = Path(__file__).resolve().parents[1]
TERMS_EN = V2 / 'i18n' / 'terms-en.yaml'
STYLE_EN = V2 / 'i18n' / 'style-en.md'


def load(path):
    return yaml.safe_load(path.read_text(encoding='utf-8'))


def vocabulary():
    return [t for path in sorted((V2 / 'vocabulary').glob('*.yaml')) for t in load(path)]


def renderings(data):
    """Every English rendering in the list, with where it sits."""
    out = [(f'terms/{t["id"]}', t.get('en')) for t in data['terms']]
    for group, items in data['names'].items():
        for item in items:
            out.append((f'names/{group}/{item["ru"]}', item.get('en')))
            for extra in ('en_short', 'hint_en'):
                if extra in item:
                    out.append((f'names/{group}/{item["ru"]}/{extra}', item[extra]))
    out += [(f'phrases/{p["ru"]}', p.get('en')) for p in data['phrases']]
    out += [(f'plurals/{p["ru"][0]}', form) for p in data['plurals'] for form in p['en']]
    out += [(f'laws/{law["id"]}', law.get('en')) for law in data['laws']]
    return out


class TermList(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = load(TERMS_EN)
        cls.vocab = vocabulary()

    def test_every_vocabulary_id_has_one_entry_with_its_russian_term(self):
        terms = {}
        for t in self.data['terms']:
            self.assertNotIn(t['id'], terms, f'{t["id"]} is listed twice')
            terms[t['id']] = t
        for v in self.vocab:
            self.assertIn(v['id'], terms, f'vocabulary id {v["id"]} is missing from terms')
            self.assertEqual(terms[v['id']]['ru'], v['ru'], f'{v["id"]}: ru differs from the vocabulary')
        self.assertEqual(set(terms), {v['id'] for v in self.vocab}, 'terms lists an id the vocabulary does not have')

    def test_different_russian_terms_never_share_an_english_rendering(self):
        seen = {}
        for t in self.data['terms']:
            key = t['en'].strip().lower()
            self.assertNotIn(key, seen, f'{t["id"]} and {seen.get(key)} both render as "{t["en"]}"')
            seen[key] = t['id']

    def test_names_are_one_to_one_within_each_group(self):
        for group, items in self.data['names'].items():
            ru, en = {}, {}
            for item in items:
                self.assertNotIn(item['ru'], ru, f'names/{group}: {item["ru"]} is listed twice')
                ru[item['ru']] = item['en']
                if 'alias_of' in item:
                    self.assertEqual(ru.get(item['alias_of']), item['en'], f'names/{group}: {item["ru"]} must match its alias')
                    continue
                self.assertNotIn(item['en'].lower(), en, f'names/{group}: {item["ru"]} and {en.get(item["en"].lower())} share "{item["en"]}"')
                en[item['en'].lower()] = item['ru']

    def test_each_phrase_has_one_fixed_rendering_and_there_are_enough(self):
        ru = [p['ru'] for p in self.data['phrases']]
        self.assertEqual(len(ru), len(set(ru)), 'a Russian phrase is listed twice')
        self.assertGreaterEqual(len(ru), 80)
        messages = load(V2 / 'site.json')['messages']['ru']
        keyed = {p['key']: p for p in self.data['phrases'] if 'key' in p}
        for key, text in messages.items():
            self.assertIn(key, keyed, f'site message {key} has no English phrase')
            self.assertEqual(keyed[key]['ru'], text, f'site message {key}: ru differs from site.json')

    def test_placeholders_survive_translation(self):
        for p in self.data['phrases']:
            self.assertEqual(sorted(re.findall(r'\{\w*\}', p['ru'])), sorted(re.findall(r'\{\w*\}', p['en'])), p['ru'])

    def test_no_rendering_is_empty(self):
        for where, en in renderings(self.data):
            self.assertTrue(isinstance(en, str) and en.strip(), f'{where}: empty English')

    def test_no_rendering_uses_forbidden_english(self):
        forbidden = [w.lower() for w in self.data['forbidden_en']]
        patterns = [re.compile(p) for p in self.data.get('forbidden_patterns_en', [])]
        for where, en in renderings(self.data):
            for word in forbidden:
                self.assertNotIn(word, en.lower(), f'{where}: "{en}" uses forbidden "{word}"')
            for pattern in patterns:
                self.assertIsNone(pattern.search(en), f'{where}: "{en}" matches {pattern.pattern}')

    def test_forbidden_english_covers_the_site_list(self):
        forbidden = {w.lower() for w in self.data['forbidden_en']}
        for latin in ('Executive Sponsor', 'Domain Owner', 'Steering', 'DR-2026', 'v1', 'O!Bank', 'Obank'):
            self.assertIn(latin.lower(), forbidden)
        site = load(V2 / 'site.json')
        self.assertEqual(self.data['forbidden_patterns_en'], site['forbidden_patterns'])

    def test_every_act_has_an_english_title_and_unofficial_titles_keep_the_russian(self):
        laws = {law['id']: law for law in self.data['laws']}
        for act in load(V2 / 'reference' / 'acts.yaml'):
            self.assertIn(act['id'], laws, f'act {act["id"]} has no entry in laws')
            self.assertEqual(laws[act['id']]['ru_original'], act['title'], f'{act["id"]}: ru_original differs from acts.yaml')
        for law in laws.values():
            self.assertIn(law['type'], ('act', 'body', 'topic'), law['id'])
            self.assertIsInstance(law['official'], bool, law['id'])
            self.assertTrue(law.get('ru_original'), f'{law["id"]}: the Russian original is required')

    def test_the_hub_names_and_the_style_rules_are_stated(self):
        hub = {n['key']: n['en'] for n in self.data['names']['hub']}
        self.assertEqual((hub['title'], hub['middle'], hub['short']), ('AI Competence Hub', 'Competence Hub', 'Hub'))
        style = STYLE_EN.read_text(encoding='utf-8')
        for needed in ('American spelling', 'AI Competence Hub', 'Competence Hub', 'forbidden', 'official English title', 'plain'):
            self.assertIn(needed, style)


if __name__ == '__main__':
    unittest.main()
