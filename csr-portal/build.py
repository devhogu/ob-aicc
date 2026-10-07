#!/usr/bin/env python3
"""Build a bilingual O!-styled CSR trial from the retained proposal pages."""
from __future__ import annotations

from html import escape, unescape
from pathlib import Path
import json
import re
import shutil

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "portfolio"
OUTPUT = ROOT / "html/csr"
KIT = ROOT / "obank-uiux/site"
HERE = Path(__file__).resolve().parent
MARKER = ".csr-o-uiux-output"
PROCESS_ID = {
    "en": "en-business-use-case-process-integration-map",
    "ru": "ru-business-use-case-карта-встраивания-в-процесс",
}

WORDS = {
    "en": {
        "skip": "Skip to content", "scope": "Project proposal · conceptual explorer",
        "menu": "Sections", "start": "Executive orientation", "theme": "Light theme",
        "map_eyebrow": "Proposed customer-case workflow", "map_title": "From contact to recorded outcome",
        "map_intro": "Eight stages describe the proposed handling path. Each pairs service work with the assistance this project would introduce. Quality and improvement form a feedback loop after the case outcome; the path is not a claim about current Bank practice.",
        "focus": "Expand map", "scroll": "Scrollable proposed case-resolution workflow",
        "swipe": "Scroll within the map to see all eight stages.", "table": "Scrollable proposal table",
        "work": "Service work", "assist": "Proposed assistance", "owner": "Accountable process role",
        "detail": "Selected stage", "source": "Read the process integration map", "loop": "Learning loop",
        "loop_intro": "After closure, quality review uses recurring patterns to inform a separate improvement backlog.",
    },
    "ru": {
        "skip": "Перейти к содержимому", "scope": "Проектное предложение · концептуальный обзор",
        "menu": "Разделы", "start": "Вводный обзор", "theme": "Светлая тема",
        "map_eyebrow": "Предлагаемый процесс обслуживания", "map_title": "От обращения до зафиксированного результата",
        "map_intro": "Восемь этапов описывают предлагаемый путь обработки обращения. Для каждого показана работа команды и помощь, которую должен добавить проект. Контроль качества и улучшение образуют обратную связь после результата; схема не утверждает, что Банк уже работает именно так.",
        "focus": "Развернуть схему", "scroll": "Прокручиваемая схема предлагаемого разрешения обращения",
        "swipe": "Прокрутите схему, чтобы увидеть все восемь этапов.", "table": "Прокручиваемая таблица предложения",
        "work": "Работа команды", "assist": "Предлагаемая помощь", "owner": "Ответственная роль",
        "detail": "Выбранный этап", "source": "Читать карту встраивания в процесс", "loop": "Цикл улучшения",
        "loop_intro": "После закрытия контроль качества собирает повторяющиеся причины для отдельного плана улучшений.",
    },
}


def text_only(value: str) -> str:
    return " ".join(unescape(re.sub(r"<[^>]+>", " ", value)).split())


def source_steps(content: str, lang: str) -> list[tuple[str, str, str, str]]:
    marker = f'id="{PROCESS_ID[lang]}"'
    if marker not in content:
        raise ValueError(f"Missing process-integration source for {lang}")
    section = content.split(marker, 1)[1].split("</table>", 1)[0]
    body = section.split("<tbody>", 1)[1].split("</tbody>", 1)[0]
    rows = [tuple(text_only(cell) for cell in re.findall(r"<td[^>]*>(.*?)</td>", row, re.S))
            for row in re.findall(r"<tr[^>]*>(.*?)</tr>", body, re.S)]
    if len(rows) != 9 or any(len(row) != 4 for row in rows):
        raise ValueError(f"Expected nine four-column process steps for {lang}, got {len(rows)}")
    return rows  # type: ignore[return-value]


def heading_ids(content: str) -> list[str]:
    ids = re.findall(r'<(?:h[2-5]|section)\b[^>]*\bid="([^"]+)"', content)
    if len(ids) < 90:
        raise ValueError(f"Expected the retained proposal headings, got {len(ids)}")
    return ids


def case_map(lang: str, steps: list[tuple[str, str, str, str]]) -> str:
    w = WORDS[lang]
    cards = "".join(
        f'<li><button type="button" data-csr-step="{i}" aria-pressed="false" '
        f'data-work="{escape(work, quote=True)}" data-assist="{escape(assist, quote=True)}" '
        f'data-owner="{escape(owner, quote=True)}"><span class="csr-step-number">{i + 1:02}</span>'
        f'<strong>{escape(title)}</strong><small>{escape(work)}</small></button></li>'
        for i, (title, work, assist, owner) in enumerate(steps[:8])
    )
    first = steps[0]
    feedback = steps[8]
    return f'''<section class="csr-case-map" id="{lang}-case-map" aria-labelledby="csr-map-title">
  <div class="csr-map-heading"><div><p class="eyebrow">{escape(w['map_eyebrow'])}</p>
    <h2 id="csr-map-title">{escape(w['map_title'])}</h2><p>{escape(w['map_intro'])}</p></div>
    <button id="csr-map-focus" type="button" aria-pressed="false">{escape(w['focus'])}</button></div>
  <p class="csr-scroll-hint">{escape(w['swipe'])}</p>
  <div class="csr-map-scroll" role="region" tabindex="0" aria-label="{escape(w['scroll'])}"><ol class="csr-map-track">{cards}</ol></div>
  <div class="csr-map-inspector" aria-live="polite"><div><p class="eyebrow">{escape(w['detail'])}</p>
    <h3 id="csr-step-title">{escape(first[0])}</h3><dl>
      <div><dt>{escape(w['work'])}</dt><dd id="csr-step-work">{escape(first[1])}</dd></div>
      <div><dt>{escape(w['assist'])}</dt><dd id="csr-step-assist">{escape(first[2])}</dd></div>
    <div><dt>{escape(w['owner'])}</dt><dd id="csr-step-owner">{escape(first[3])}</dd></div>
    </dl></div><a href="#{PROCESS_ID[lang]}">{escape(w['source'])} →</a></div>
  <div class="csr-feedback"><span aria-hidden="true">↺</span><div><strong>{escape(w['loop'])}: {escape(feedback[0])}</strong>
    <p>{escape(w['loop_intro'])} {escape(feedback[2])}</p></div></div>
</section>'''


def transform(content: str, lang: str, hash_map: dict[str, str]) -> str:
    w = WORDS[lang]
    steps = source_steps(content, lang)
    content = re.sub(r'<header class="topbar">.*?</header>', '', content, count=1, flags=re.S)
    # The source's intersection-ratio observer mislabels very long sections at their start.
    nav_start = content.index("      var panels = Array.from(document.querySelectorAll('[data-document]'));")
    nav_end = content.index("      window.addEventListener('keydown'", nav_start)
    content = content[:nav_start] + content[nav_end:]
    content = content.replace('<details class="nav-doc" open>', '<details class="nav-doc">')
    content = content.replace('<body data-language=', '<body class="csr-portal" data-language=', 1)
    content = content.replace('<main class="content">', '<main class="content" id="csr-main">', 1)
    content = content.replace('<div class="table-wrap">', f'<div class="table-wrap" data-csr-table-label="{escape(w["table"], quote=True)}">')
    content = re.sub(r'(<p class="lede">.*?</p>)', lambda m: m.group(1) + '\n' + case_map(lang, steps), content, count=1, flags=re.S)
    language = ('<span class="language-button" aria-current="true">ENG</span><a class="language-button" data-csr-language href="../ru/index.html" lang="ru">РУС</a>'
                if lang == "en" else
                '<a class="language-button" data-csr-language href="../en/index.html" lang="en">ENG</a><span class="language-button" aria-current="true">РУС</span>')
    header = f'''<a class="o-skip" href="#csr-main">{escape(w['skip'])}</a>
<header class="csr-header o-header"><a class="o-identity" href="#{lang}-start"><img src="../assets/o-mark.svg" width="34" height="38" alt=""><span>CSR · Customer Service Resolution</span></a>
  <span class="csr-header-scope">{escape(w['scope'])}</span>
  <div class="csr-header-tools"><button class="menu-button" id="menu-button" type="button" aria-controls="sidebar" aria-expanded="false">{escape(w['menu'])}</button>
    <span class="csr-current" id="current-section">{escape(w['start'])}</span>
    <span class="language-selector" role="group" aria-label="{'Document language' if lang == 'en' else 'Язык документа'}">{language}</span>
    <button id="csr-theme" type="button">{escape(w['theme'])}</button></div></header>'''
    content = content.replace('<body class="csr-portal" data-language="' + lang + '">',
                              '<body class="csr-portal" data-language="' + lang + '">\n' + header, 1)
    styles = ''.join(f'<link rel="stylesheet" href="../assets/{name}">\n' for name in
                     ("fonts.css", "tokens.css", "workspace.css", "csr.css"))
    early = '<script>try{document.documentElement.dataset.theme=localStorage.getItem("obank-csr-theme")==="light"?"light":"dark"}catch{document.documentElement.dataset.theme="dark"}</script>\n'
    mapping = json.dumps(hash_map, ensure_ascii=False).replace('</', '<\\/')
    content = content.replace('</head>', early + styles + f'<script id="csr-hash-map" type="application/json">{mapping}</script>\n</head>', 1)
    content = content.replace('</body>', '<script src="../assets/csr.js" defer></script>\n</body>', 1)
    return re.sub(r'[ \t]+(?=\r?$)', '', content, flags=re.M)


def build() -> None:
    if not (SOURCE / "en/projects/service-resolution/workbook.html").is_file() or not KIT.is_dir():
        raise SystemExit("CSR source or O! UI/UX kit is missing")
    if OUTPUT.exists():
        if not (OUTPUT / MARKER).is_file():
            raise SystemExit("Refusing to replace a non-generated html/csr directory")
        shutil.rmtree(OUTPUT)
    OUTPUT.mkdir(parents=True)
    (OUTPUT / MARKER).write_text("Generated by csr-portal/build.py from portfolio/{en,ru}/projects/service-resolution/workbook.html\n")
    assets = OUTPUT / "assets"
    assets.mkdir()
    for name in ("fonts.css", "tokens.css", "workspace.css"):
        shutil.copyfile(KIT / name, assets / name)
    for name in ("csr.css", "csr.js"):
        shutil.copyfile(HERE / "assets" / name, assets / name)
    shutil.copyfile(KIT / "assets/logos/o-mark.svg", assets / "o-mark.svg")
    shutil.copytree(KIT / "assets/fonts", assets / "assets/fonts")
    sources = {lang: (SOURCE / lang / "projects/service-resolution/workbook.html").read_text() for lang in ("ru", "en")}
    ru_ids, en_ids = heading_ids(sources["ru"]), heading_ids(sources["en"])
    if len(ru_ids) != len(en_ids):
        raise ValueError("Russian and English document structures differ")
    maps = {"ru": dict(zip(ru_ids, en_ids)), "en": dict(zip(en_ids, ru_ids))}
    for lang in ("ru", "en"):
        output = OUTPUT / lang / "index.html"
        output.parent.mkdir()
        output.write_text(transform(sources[lang], lang, maps[lang]))
    (OUTPUT / "index.html").write_text('<!doctype html><html lang="ru"><meta charset="utf-8"><meta http-equiv="refresh" content="0;url=ru/index.html"><title>CSR</title><a href="ru/index.html">Открыть CSR</a></html>\n')
    print(f"Built bilingual CSR site in {OUTPUT}")


if __name__ == "__main__":
    build()
