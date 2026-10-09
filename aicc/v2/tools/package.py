# START_MODULE_CONTRACT
#   PURPOSE: Pack the Hub (version 2, Russian edition) for offline use: the built site, which opens straight from files, and the full source it is built from.
#   SCOPE: Reads html/aicc/v2 (a fresh build) and aicc/v2; writes one folder and one zip under the chosen output folder. No network, no rebuild.
#   DEPENDS: M-HUB-V2-BUILD
#   LINKS: C-HUB-V2
# END_MODULE_CONTRACT
#
# START_MODULE_MAP
#   main - copy the site and the source into <out>/aicc-v2-hub-ru/, write the README, zip it
# END_MODULE_MAP
"""Pack the Hub v2 Russian edition: site + full source, as a folder and a zip."""
import argparse
import shutil
import subprocess
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SITE = ROOT / 'html' / 'aicc' / 'v2'
SRC = ROOT / 'aicc' / 'v2'
NAME = 'aicc-v2-hub-ru'
SKIP = shutil.ignore_patterns('__pycache__', '*.pyc', '.pytest_cache')

README = """Хаб Компетенций по AI — русская редакция (версия 2)
Сборка из коммита {commit}.

КАК ОТКРЫТЬ
Откройте файл index.html в этой папке (или site/ru/index.html) в браузере.
Сайт работает прямо из файлов, без сервера и без интернета: поиск, вкладки,
карты обучения и отметки о пройденных шагах работают в браузере.
Держите папку site целиком: страницы ссылаются на свои стили и скрипты.

ЧТО ВНУТРИ
site/                   готовый сайт: страницы HTML, стили, скрипты, иконки
site/sources/           исходные файлы, опубликованные вместе с сайтом
source/aicc/v2/         полный исходный код Хаба:
  content/ru/           страницы (Markdown)
  cards/                карточки проектов (портфель)
  vocabulary/           словарь терминов
  reference/            Справочник: регуляторы, ресурсы, обучение Anthropic
  learning/             карты обучения и дорожная карта
  catalog/              каталог сценариев
  calendar.json         календарь PI и итераций
  site.json, site.css, site.js, ui/   настройки, стили, скрипты, набор интерфейса
  tools/                сборка, проверка, упаковка
  tests/                тесты
source/portal/.cache/mermaid-hub/   уже нарисованные схемы: пересборка обходится без браузера

КАК ПЕРЕСОБРАТЬ
Нужен Python 3 с пакетами markdown-it-py и PyYAML. Новые или изменённые схемы
рисуются через Node и Chromium (tools/render-mermaid.js); без изменений в схемах они не нужны.
  cd source
  python3 aicc/v2/tools/build.py                 # результат: source/html/aicc/v2
  python3 aicc/v2/tools/check.py --idempotent    # проверка ссылок, якорей, словаря
  python3 -m unittest discover -s aicc/v2/tests
"""


# START_CONTRACT: main
#   PURPOSE: Write <out>/aicc-v2-hub-ru/ (site/, source/aicc/v2/, index.html, README.txt) and <out>/aicc-v2-hub-ru.zip.
#   INPUTS: { --out: folder for the package (default: portal/published) }
#   OUTPUTS: { None; prints the paths and sizes }
#   SIDE_EFFECTS: Replaces the package folder and zip of the same name in the output folder.
# END_CONTRACT: main
def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', default=str(ROOT / 'portal' / 'published'))
    out = Path(parser.parse_args().out).resolve()
    if not (SITE / 'ru' / 'index.html').exists():
        raise SystemExit(f'no built site in {SITE}: run aicc/v2/tools/build.py first')
    commit = subprocess.run(['git', 'rev-parse', '--short', 'HEAD'], cwd=ROOT, capture_output=True, text=True).stdout.strip() or 'unknown'
    pack = out / NAME
    shutil.rmtree(pack, ignore_errors=True)
    shutil.copytree(SITE, pack / 'site', ignore=SKIP)
    shutil.copytree(SRC, pack / 'source' / 'aicc' / 'v2', ignore=SKIP)
    # the diagrams already drawn, so the source rebuilds without a browser (tools/diagrams.py reads this cache first)
    cache = ROOT / 'portal' / '.cache' / 'mermaid-hub'
    if cache.is_dir():
        shutil.copytree(cache, pack / 'source' / 'portal' / '.cache' / 'mermaid-hub')
    (pack / 'index.html').write_text(
        '<!doctype html><html lang="ru"><head><meta charset="utf-8"><meta http-equiv="refresh" content="0; url=site/ru/index.html">'
        '<title>Хаб Компетенций по AI</title></head><body><p><a href="site/ru/index.html">Хаб Компетенций по AI — открыть</a></p></body></html>\n',
        encoding='utf-8')
    (pack / 'README.txt').write_text(README.format(commit=commit), encoding='utf-8')
    archive = out / f'{NAME}.zip'
    archive.unlink(missing_ok=True)
    with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) as z:
        for path in sorted(pack.rglob('*')):
            if path.is_file():
                z.write(path, path.relative_to(out).as_posix())
    files = sum(1 for p in pack.rglob('*') if p.is_file())
    print(f'{pack} ({files} files)\n{archive} ({archive.stat().st_size / 1e6:.1f} MB), from {commit}')


if __name__ == '__main__':
    main()
