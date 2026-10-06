"""After the import: keep what repeats a title equal to that title (RUNBOOK.md step 7).

- The browser title and the last breadcrumb follow the page title; a breadcrumb link follows the title
  of the page it points to. The token `service.eyebrow` stays: both builders replace it with the
  name of their site.
- A link label on an area page or the overview that equalled the section or page title it points to in
  the baseline is set to the new title.
- The accessible name of a problems tab follows its visible label.
"""
import argparse
import html
import os
import re


def plain(markup):
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', markup))).strip()


def titles(text):
    """Page title and section titles by anchor."""
    head = re.search(r'<h1 class="page-header__title">(.*?)</h1>', text, re.S)
    found = {'': plain(head[1]) if head else ''}
    for match in re.finditer(r'<section class="l3-section" id="([^"]+)">.*?<h2 class="l3-section__title">(.*?)</h2>', text, re.S):
        found[match[1]] = plain(match[2])
    for match in re.finditer(r'<details class="flow-detail" id="([^"]+)">.*?<(h[23])[^>]*class="flow-detail__title[^"]*"[^>]*>(.*?)</\2>', text, re.S):
        found[match[1]] = plain(match[3])
    return found


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--root', required=True)
    parser.add_argument('--baseline', required=True)
    args = parser.parse_args()
    pages = sorted(os.path.join(d, f) for d, _, fs in os.walk(args.root) for f in fs if f == 'index.html' and '/assets' not in d)
    new = {os.path.relpath(p, args.root): titles(open(p).read()) for p in pages}
    old = {rel: titles(open(os.path.join(args.baseline, rel)).read()) for rel in new}
    counts = {'titles': 0, 'breadcrumbs': 0, 'labels': 0, 'tab names': 0}
    for path in pages:
        rel = os.path.relpath(path, args.root)
        text = source = open(path).read()
        own = new[rel]['']
        if rel != 'index.html' and own:
            text, n = re.subn(r'(<title>)(.*?)(</title>)', lambda m: m[1] + m[2].replace(html.escape(old[rel][''], quote=False), html.escape(own, quote=False)) + m[3], text, count=1, flags=re.S)
            text = re.sub(r'(<span class="breadcrumb__current"[^>]*>)(.*?)(</span>)', lambda m: m[1] + html.escape(own, quote=False) + m[3], text, count=1, flags=re.S)

        def renamed(href, shown):
            """The new title of the link target, if the label repeated the old one."""
            target, _, anchor = href.partition('#')
            target_rel = os.path.normpath(os.path.join(os.path.dirname(rel), target)) if target else rel
            was, now = old.get(target_rel, {}).get(anchor, ''), new.get(target_rel, {}).get(anchor, '')
            return now if was and now and shown.lower() == was.lower() and shown != now else ''

        def link(match):
            attrs, label = match[1], match[2]
            href = re.search(r'href="([^"]+)"', attrs)[1]
            lead = label.split('<span', 1)[0]
            now = renamed(href, plain(lead))
            if not now:
                return match[0]
            counts['breadcrumbs' if 'breadcrumb__link' in attrs else 'labels'] += 1
            return f'<a{attrs}>' + lead.replace(lead.strip(), html.escape(now, quote=False), 1) + label[len(lead):] + '</a>'
        text = re.sub(r'<a((?=[^>]*class="[^"]*(?:card-link|breadcrumb__link))[^>]*href="[^"]+"[^>]*)>(.*?)</a>', link, text, flags=re.S)

        def box(match):
            """An area or sub-area box: its heading and the accessible name of its link follow the target title."""
            article = match[0]
            target = re.search(r'<a class="card__click-target" href="([^"]+)"[^>]*aria-label="([^"]*)"', article)
            head = re.search(r'(<h[23] class="card__title[^"]*">)(.*?)(<span class="card__count"|</h[23]>)', article, re.S)
            if not target or not head:
                return article
            now = renamed(target[1], plain(head[2]))
            if not now:
                return article
            counts['labels'] += 1
            article = article.replace(head[0], head[1] + head[2].replace(head[2].strip(), html.escape(now, quote=False), 1) + head[3], 1)
            return article.replace(target[0], target[0].replace(f'aria-label="{target[2]}"', 'aria-label="' + html.escape(now) + '"'), 1)
        text = re.sub(r'<article class="card[^"]*">.*?</article>', box, text, flags=re.S)

        labels = {m[1]: m[2].strip() for m in re.finditer(r'<label\s+class="problems-tab-label"\s+for="([^"]+)"[^>]*>(.*?)</label>', text, re.S)}

        def tab(match):
            want = labels.get(match[1])
            if want and match[3] != want:
                counts['tab names'] += 1
                return match[0].replace(f'aria-label="{match[3]}"', f'aria-label="{want}"')
            return match[0]
        text = re.sub(r'<input\s+type="radio"\s+class="problems-tab-input"\s+name="problems-tabs"\s+id="([^"]+)"(.*?)aria-label="([^"]*)"\s*>', tab, text, flags=re.S)
        if text != source:
            counts['titles'] += re.search(r'<title>.*?</title>', text, re.S)[0] != re.search(r'<title>.*?</title>', source, re.S)[0]
            open(path, 'w').write(text)
    print(counts)


if __name__ == '__main__':
    main()
