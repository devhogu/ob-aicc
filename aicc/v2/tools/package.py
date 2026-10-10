# START_MODULE_CONTRACT
#   PURPOSE: Pack the Hub (version 2) for offline use in three packages - bilingual, Russian and English: the built site, which opens straight from files, and the full source it is built from.
#   SCOPE: Reads html/aicc/v2 (a fresh build) and aicc/v2; writes one folder and one zip per package under the chosen output folder. No network, no rebuild.
#   DEPENDS: M-PORTAL-SOURCE
#   LINKS: C-HUB-V2, C-HUB-V2-EN, M-PORTABLE-EXPORT
# END_MODULE_CONTRACT
#
# START_MODULE_MAP
#   PACKAGES - the packages: name, editions, the edition it opens on, the README language
#   pack - write one package folder and its zip
#   single_edition - turn a copied site into one edition: the other edition and the language switch go
#   main - write the packages asked for (all by default)
# END_MODULE_MAP
"""Pack the Hub v2: aicc-v2-hub (both editions), aicc-v2-hub-ru, aicc-v2-hub-en - each the site plus the full source, as a folder and a zip."""
import argparse
import re
import shutil
import subprocess
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SITE = ROOT / 'html' / 'aicc' / 'v2'
SRC = ROOT / 'aicc' / 'v2'
SKIP = shutil.ignore_patterns('__pycache__', '*.pyc', '.pytest_cache')
PACKAGES = {
    'aicc-v2-hub': {'editions': ('ru', 'en'), 'home': 'ru', 'readme': ('ru', 'en')},
    'aicc-v2-hub-ru': {'editions': ('ru',), 'home': 'ru', 'readme': ('ru',)},
    'aicc-v2-hub-en': {'editions': ('en',), 'home': 'en', 'readme': ('en',)},
}
TITLE = {'ru': 'Хаб Компетенций по AI', 'en': 'AI Competence Hub'}

README = {'ru': """Хаб Компетенций по AI — {what} (версия 2)
Сборка из коммита {commit}.

КАК ОТКРЫТЬ
Откройте файл index.html в этой папке в браузере.
Сайт работает прямо из файлов, без сервера и без интернета: поиск, вкладки,
карты обучения и отметки о пройденных шагах работают в браузере.
Держите папку site целиком: страницы ссылаются на свои стили и скрипты.

ЧТО ВНУТРИ
site/                   готовый сайт: {editions}, стили, скрипты, иконки
site/sources/           исходные файлы, опубликованные вместе с сайтом
source/aicc/v2/         полный исходный код Хаба (обе редакции):
  content/ru, content/en   страницы (Markdown): русский источник и английский перевод
  cards/                карточки проектов (портфель)
  vocabulary/           словарь терминов
  reference/            Справочник: регуляторы, ресурсы, обучение Anthropic
  learning/             карты обучения и дорожная карта
  catalog/              каталог сценариев (pages — русский, pages-en — английский)
  i18n/                 английские термины, правила стиля, строки интерфейса, записи о переводе
  calendar.json         календарь PI и итераций
  site.json, site.css, site.js, ui/   настройки, стили, скрипты, набор интерфейса
  tools/                сборка, проверка, упаковка
  tests/                тесты
source/portal/.cache/mermaid-hub/   уже нарисованные схемы: пересборка обходится без браузера

КАК ПЕРЕСОБРАТЬ
Нужен Python 3 с пакетами markdown-it-py и PyYAML. Новые или изменённые схемы
рисуются через Node и Chromium (tools/render-mermaid.js); без изменений в схемах они не нужны.
  cd source
  python3 aicc/v2/tools/build.py                 # результат: source/html/aicc/v2 (обе редакции)
  python3 aicc/v2/tools/check.py --idempotent    # ссылки, якоря, словарь, соответствие редакций
  python3 -m unittest discover -s aicc/v2/tests
""", 'en': """AI Competence Hub — {what} (version 2)
Built from commit {commit}.

HOW TO OPEN
Open index.html in this folder in a browser.
The site works straight from the files, with no server and no internet: search, tabs,
learning maps and the steps you tick off all work in the browser.
Keep the site folder together: the pages refer to their own styles and scripts.

WHAT IS INSIDE
site/                   the finished site: {editions}, styles, scripts, icons
site/sources/           the source files published with the site
source/aicc/v2/         the full source of the Hub (both editions):
  content/ru, content/en   pages (Markdown): the Russian source and its English translation
  cards/                project cards (the portfolio)
  vocabulary/           the vocabulary
  reference/            Reference: regulators, resources, Anthropic learning
  learning/             learning maps and the roadmap
  catalog/              the Discovery Catalog (pages: Russian, pages-en: English)
  i18n/                 English terms, style rules, interface strings, translation records
  calendar.json         the PI and iteration calendar
  site.json, site.css, site.js, ui/   settings, styles, scripts, interface kit
  tools/                build, check, packaging
  tests/                tests
source/portal/.cache/mermaid-hub/   diagrams already drawn: a rebuild needs no browser

HOW TO REBUILD
You need Python 3 with markdown-it-py and PyYAML. New or changed diagrams are drawn
with Node and Chromium (tools/render-mermaid.js); without diagram changes they are not needed.
  cd source
  python3 aicc/v2/tools/build.py                 # output: source/html/aicc/v2 (both editions)
  python3 aicc/v2/tools/check.py --idempotent    # links, anchors, vocabulary, edition parity
  python3 -m unittest discover -s aicc/v2/tests
"""}
WHAT = {'ru': {('ru', 'en'): 'русская и английская редакции', ('ru',): 'русская редакция', ('en',): 'английская редакция'},
        'en': {('ru', 'en'): 'Russian and English editions', ('ru',): 'Russian edition', ('en',): 'English edition'}}
EDITIONS = {'ru': {('ru', 'en'): 'страницы ru/ и en/ с переключателем языка', ('ru',): 'страницы ru/', ('en',): 'страницы en/'},
            'en': {('ru', 'en'): 'pages in ru/ and en/ with a language switch', ('ru',): 'pages in ru/', ('en',): 'pages in en/'}}
SWITCH = re.compile(r'<a class="lang-switch"[^>]*>[^<]*</a>')


def single_edition(site, keep):
    """A copied site reduced to one edition: the other editions' pages, scripts and listings go, and so does the switch to them."""
    for lang in ('ru', 'en'):
        if lang == keep:
            continue
        shutil.rmtree(site / lang, ignore_errors=True)
        for name in (f'search-{lang}.js', f'i18n-{lang}.js'):
            (site / 'assets' / name).unlink(missing_ok=True)
        (site / 'sources' / ('index.html' if lang == 'ru' else f'index-{lang}.html')).unlink(missing_ok=True)
    for page in (site / keep).rglob('*.html'):
        text = page.read_text(encoding='utf-8')
        if 'lang-switch' in text:
            page.write_text(SWITCH.sub('', text), encoding='utf-8')
    if keep != 'ru':  # the site's own entry opens the kept edition; its source listing becomes the main one
        (site / 'index.html').write_text(
            f'<!doctype html><html lang="{keep}"><head><meta charset="utf-8"><meta http-equiv="refresh" content="0; url={keep}/index.html">'
            f'<script>location.replace("{keep}/index.html"+location.hash)</script>'
            f'<title>{TITLE[keep]}</title></head><body><main><h1><a href="{keep}/index.html">{TITLE[keep]}</a></h1></main></body></html>\n', encoding='utf-8')
        listing = site / 'sources' / f'index-{keep}.html'
        if listing.exists():
            listing.replace(site / 'sources' / 'index.html')


# START_CONTRACT: pack
#   PURPOSE: Write <out>/<name>/ (site/, source/aicc/v2/, source/portal/.cache/mermaid-hub/, index.html, README.txt) and <out>/<name>.zip.
#   INPUTS: { name: str - a key of PACKAGES; out: Path; commit: str }
#   OUTPUTS: { (Path, Path) - the folder and the zip }
#   SIDE_EFFECTS: Replaces the package folder and zip of the same name in the output folder.
# END_CONTRACT: pack
def pack(name, out, commit):
    spec = PACKAGES[name]
    folder = out / name
    shutil.rmtree(folder, ignore_errors=True)
    shutil.copytree(SITE, folder / 'site', ignore=SKIP)
    if len(spec['editions']) == 1:
        single_edition(folder / 'site', spec['editions'][0])
    shutil.copytree(SRC, folder / 'source' / 'aicc' / 'v2', ignore=SKIP)
    cache = ROOT / 'portal' / '.cache' / 'mermaid-hub'  # the diagrams already drawn, so the source rebuilds without a browser
    if cache.is_dir():
        shutil.copytree(cache, folder / 'source' / 'portal' / '.cache' / 'mermaid-hub')
    home = spec['home']
    (folder / 'index.html').write_text(
        f'<!doctype html><html lang="{home}"><head><meta charset="utf-8"><meta http-equiv="refresh" content="0; url=site/{home}/index.html">'
        f'<script>location.replace("site/{home}/index.html")</script>'
        f'<title>{TITLE[home]}</title></head><body><p><a href="site/{home}/index.html">{TITLE[home]}</a></p></body></html>\n', encoding='utf-8')
    key = spec['editions']
    readme = '\n\n'.join(README[lang].format(commit=commit, what=WHAT[lang][key], editions=EDITIONS[lang][key]) for lang in spec['readme'])
    (folder / 'README.txt').write_text(readme, encoding='utf-8')
    archive = out / f'{name}.zip'
    archive.unlink(missing_ok=True)
    with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) as z:
        for path in sorted(folder.rglob('*')):
            if path.is_file():
                z.write(path, path.relative_to(out).as_posix())
    return folder, archive


# START_CONTRACT: main
#   PURPOSE: Write the packages asked for, by default all three, from the current build.
#   INPUTS: { --out: folder (default: portal/published); --only: package names }
#   OUTPUTS: { None; prints the paths and sizes }
#   SIDE_EFFECTS: Replaces the named package folders and zips.
# END_CONTRACT: main
def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', default=str(ROOT / 'portal' / 'published'))
    parser.add_argument('--only', nargs='*', choices=sorted(PACKAGES), default=sorted(PACKAGES))
    args = parser.parse_args()
    out = Path(args.out).resolve()
    out.mkdir(parents=True, exist_ok=True)
    if not (SITE / 'ru' / 'index.html').exists():
        raise SystemExit(f'no built site in {SITE}: run aicc/v2/tools/build.py first')
    commit = subprocess.run(['git', 'rev-parse', '--short', 'HEAD'], cwd=ROOT, capture_output=True, text=True).stdout.strip() or 'unknown'
    for name in args.only:
        folder, archive = pack(name, out, commit)
        files = sum(1 for p in folder.rglob('*') if p.is_file())
        print(f'{folder} ({files} files) · {archive.name} ({archive.stat().st_size / 1e6:.1f} MB), from {commit}')


if __name__ == '__main__':
    main()
