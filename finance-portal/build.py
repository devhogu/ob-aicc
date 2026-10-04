#!/usr/bin/env python3
"""Apply a shared O! shell and token skin to the retained finance page family."""
from __future__ import annotations

from html import escape
from pathlib import Path
import os
import re
import shutil

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "html-alt/financial-services"
OUTPUT = ROOT / "html/financial-services"
KIT = ROOT / "obank-uiux/site"
HERE = Path(__file__).resolve().parent
MARKER = ".finance-o-uiux-output"
LABELS = {
    "en": {"site": "Financial Services", "scope": "Conceptual framework", "home": "Overview", "other": "Русский", "skip": "Skip to main content"},
    "ru": {"site": "Финансовые услуги", "scope": "Концептуальная модель", "home": "Обзор", "other": "English", "skip": "Перейти к основному содержимому"},
}


def localize_breadcrumb(content: str, page: Path, lang: str) -> str:
    """Use the Russian section's own title for its child-page breadcrumb."""
    relative = page.relative_to(OUTPUT / lang)
    if lang != "ru" or len(relative.parts) != 3:
        return content
    section = SOURCE / "ru" / relative.parts[0] / "index.html"
    section_title = re.search(r'<span class="breadcrumb__current" aria-current="page">([^<]+)</span>', section.read_text())
    parent_link = r'(<a class="breadcrumb__link" href="../index.html">)([^<]+)(</a>)'
    if not section_title or len(re.findall(parent_link, content)) != 1:
        raise ValueError(f"Missing section title or parent breadcrumb: {page}")
    return re.sub(parent_link, lambda match: match.group(1) + section_title.group(1) + match.group(3), content, count=1)


def rel(page: Path, target: Path) -> str:
    return os.path.relpath(target, page.parent).replace(os.sep, "/")


def transform(content: str, page: Path, lang: str) -> str:
    labels = LABELS[lang]
    other = "ru" if lang == "en" else "en"
    counterpart = OUTPUT / other / page.relative_to(OUTPUT / lang)
    home = OUTPUT / lang / "index.html"
    assets = OUTPUT / "assets/o-uiux"
    content = localize_breadcrumb(content, page, lang)
    content = re.sub(r'<!-- Preconnect for Google Fonts to reduce latency -->\s*', "", content)
    content = re.sub(r'<link rel="preconnect" href="https://fonts\.(?:googleapis|gstatic)\.com"[^>]*>\s*', "", content)
    content = content.replace('>service.eyebrow<', f'>{escape(labels["site"])}<')
    if lang == "ru" and page.relative_to(OUTPUT / lang) == Path("index.html"):
        content = content.replace('>Financial Services</span>', f'>{escape(labels["site"])}</span>', 1)
    content = re.sub(r'<html\b', '<html data-theme="light"', content, count=1)
    content = re.sub(r'<body(?: class="([^"]*)")?>',
                     lambda match: f'<body class="{escape(" ".join(filter(None, (match.group(1), "finance-portal"))))}">',
                     content, count=1)
    font_files = (
        "assets/fonts/golos-text/GolosText-variable.woff2",
        "assets/fonts/tt-norms-pro/tt-norms-pro-400.woff2",
        "assets/fonts/tt-norms-pro/tt-norms-pro-700.woff2",
    )
    common = ''.join(f'<link rel="preload" href="{escape(rel(page, assets / name))}" as="font" type="font/woff2" crossorigin>\n'
                     for name in font_files)
    common += ''.join(f'<link rel="stylesheet" href="{escape(rel(page, assets / name))}">\n'
                      for name in ("fonts.css", "tokens.css"))
    content = re.sub(r'(</title>)', lambda match: match.group(1) + '\n' + common, content, count=1)
    shared = f'<link rel="stylesheet" href="{escape(rel(page, assets / "finance.css"))}">\n'
    if 'id="stageModal"' in content or 'class="problems-tab-input"' in content:
        shared += f'<script defer src="{escape(rel(page, assets / "finance.js"))}"></script>\n'
    content = content.replace('</head>', shared + '</head>', 1)
    header = f'''<div class="finance-shell-header"><nav class="finance-shell-nav" aria-label="{'Finance portal' if lang == 'en' else 'Портал финансовых услуг'}">
  <a class="finance-identity" href="{escape(rel(page, home))}"><img src="{escape(rel(page, assets / 'o-mark.svg'))}" width="32" height="36" alt=""><span>{escape(labels['site'])}</span></a>
  <span class="finance-scope">{escape(labels['scope'])}</span>
  <div class="finance-shell-links"><a href="{escape(rel(page, home))}">{escape(labels['home'])}</a><a href="{escape(rel(page, counterpart))}" hreflang="{other}" lang="{other}">{escape(labels['other'])}</a></div>
</nav></div>'''
    skip = re.search(r'<a class="skip-link"[^>]*>.*?</a>', content, re.S)
    if not skip:
        raise ValueError(f"Missing skip link: {page}")
    content = content[:skip.end()] + '\n' + header + content[skip.end():]
    return content


def build() -> None:
    if not SOURCE.is_dir() or not KIT.is_dir():
        raise SystemExit("Finance source or O! UI/UX kit is missing")
    if OUTPUT.exists():
        if not (OUTPUT / MARKER).is_file():
            raise SystemExit("Refusing to replace a non-generated html/financial-services directory")
        shutil.rmtree(OUTPUT)
    shutil.copytree(SOURCE, OUTPUT, ignore=shutil.ignore_patterns(".DS_Store"))
    (OUTPUT / MARKER).write_text("Generated by finance-portal/build.py from html-alt/financial-services\n")
    assets = OUTPUT / "assets/o-uiux"
    assets.mkdir(parents=True)
    for name in ("fonts.css", "tokens.css"):
        shutil.copyfile(KIT / name, assets / name)
    shutil.copyfile(HERE / "assets/finance.css", assets / "finance.css")
    shutil.copyfile(HERE / "assets/finance.js", assets / "finance.js")
    shutil.copyfile(KIT / "assets/logos/o-mark.svg", assets / "o-mark.svg")
    shutil.copytree(KIT / "assets/fonts", assets / "assets/fonts")
    pages = sorted(OUTPUT.rglob("*.html"))
    if len(pages) != 152:
        raise ValueError(f"Expected 152 bilingual pages, got {len(pages)}")
    for page in pages:
        lang = page.relative_to(OUTPUT).parts[0]
        if lang not in LABELS:
            raise ValueError(f"Unexpected page language: {page}")
        page.write_text(transform(page.read_text(), page, lang))
    for tokens in OUTPUT.glob("*/assets/styles/tokens.css"):
        tokens.write_text(re.sub(r"/\* Google Fonts.*?\*/\s*@import[^\n]*\n", "", tokens.read_text(), count=1, flags=re.S))
    (OUTPUT / "index.html").write_text('<!doctype html><html lang="ru"><meta charset="utf-8"><meta http-equiv="refresh" content="0;url=ru/index.html"><title>Financial Services</title><a href="ru/index.html">Открыть портал</a></html>\n')
    print(f"Built {len(pages)} finance pages in {OUTPUT}")


if __name__ == "__main__":
    build()
