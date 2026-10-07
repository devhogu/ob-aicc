#!/usr/bin/env python3
# START_MODULE_CONTRACT
#   PURPOSE: Export the generated portal as a folder browsable directly through file URLs.
#   SCOPE: Explicit on-demand packaging, file links, bundled search/fonts, safe output replacement and validation.
#   DEPENDS: M-PORTAL-PROJECTION
#   LINKS: M-PORTABLE-EXPORT, V-M-PORTABLE-EXPORT
# END_MODULE_CONTRACT
# START_MODULE_MAP
#   ROOT - source repository root
#   MARKER - generated output ownership and checksums
#   KIND - output format identity
#   ATTR - quoted HTML attribute matcher
#   snapshot - read a stable candidate input tree
#   digest - calculate an ordered tree checksum
#   local_target - resolve a package-local URL
#   file_url - make navigation point to a concrete file
#   Page - preserve HTML while adapting URL attributes
#   validate - check page, anchor and search destinations
#   export - prepare, validate and replace a generated folder
#   main - explicit export command
# END_MODULE_MAP
"""Run: python3 portal/tools/export_portable.py. Does not build or publish the website."""
import argparse
import base64
import hashlib
import html
import json
import os
from pathlib import Path
import posixpath
import re
import tempfile
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit, urlunsplit

ROOT = Path(__file__).resolve().parents[2]
MARKER = 'portable-manifest.json'
KIND = 'aicc-portable-v1'
ATTR = re.compile(r'''(?P<name>[\w:-]+)\s*=\s*(?P<quote>["'])(?P<value>.*?)(?P=quote)''', re.S)


def snapshot(source):
    files = {}
    for path in sorted(source.rglob('*')):
        if path.is_symlink():
            raise ValueError(f'Symlinks are not supported: {path}')
        if path.is_file() and path.name != '.DS_Store' and not path.name.startswith('._'):
            files[path.relative_to(source).as_posix()] = path.read_bytes()
    return files


def digest(files):
    h = hashlib.sha256()
    for path, data in sorted(files.items()):
        h.update(path.encode() + b'\0' + hashlib.sha256(data).digest())
    return h.hexdigest()


def local_target(url, page):
    parts = urlsplit(url)
    if parts.scheme or parts.netloc or not parts.path:
        return None
    path = unquote(parts.path)
    path = posixpath.normpath(path.lstrip('/') if path.startswith('/') else posixpath.join(posixpath.dirname(page), path))
    if path == '..' or path.startswith('../'):
        raise ValueError(f'{page}: link escapes the package: {url}')
    return path


def file_url(url, page, files):
    target = local_target(url, page)
    if target is None:
        return url
    parts = urlsplit(url)
    index = posixpath.normpath(posixpath.join(target, 'index.html'))
    if target not in files and index in files:
        target = index
    # Explicit file paths also avoid filesystem-root URLs when the folder is relocated.
    relative = posixpath.relpath(target, posixpath.dirname(page) or '.')
    return urlunsplit(('', '', relative, parts.query, parts.fragment))


class Page(HTMLParser):
    """Inspect and replace only URL attribute spans; preserve SVG and body bytes."""
    def __init__(self, text, page, files=None):
        super().__init__(convert_charrefs=False)
        self.text, self.page, self.files = text, page, files
        self.ids, self.links, self.resources, self.edits = set(), [], [], []
        self.starts = [0]
        for match in re.finditer('\n', text):
            self.starts.append(match.end())
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.add(attrs['id'])
        raw = self.get_starttag_text()
        line, column = self.getpos()
        offset = self.starts[line - 1] + column
        for match in ATTR.finditer(raw):
            name = match['name'].lower()
            value = html.unescape(match['value'])
            if name not in ('href', 'src'):
                continue
            self.links.append(value)
            if name == 'src' or tag == 'link' and attrs.get('rel') == 'stylesheet':
                self.resources.append(value)
            if self.files is not None:
                replacement = file_url(value, self.page, self.files)
                if replacement != value:
                    self.edits.append((offset + match.start('value'), offset + match.end('value'), html.escape(replacement, quote=True)))

    handle_startendtag = handle_starttag

    def rendered(self):
        result = self.text
        for start, end, replacement in reversed(self.edits):
            result = result[:start] + replacement + result[end:]
        return result


def validate(files, indexes):
    pages = {p: Page(data.decode(), p) for p, data in files.items() if p.endswith('.html')}
    for path, page in pages.items():
        for resource in page.resources:
            if urlsplit(resource).scheme not in ('', 'data') or resource.startswith('//'):
                raise ValueError(f'{path}: external resource {resource}')
        for url in page.links:
            parts = urlsplit(url)
            if parts.scheme or parts.netloc:
                continue
            target = local_target(url, path) if parts.path else path
            if target not in files:
                raise ValueError(f'{path}: missing file {url}')
            if parts.fragment and target in pages and unquote(parts.fragment) not in pages[target].ids:
                raise ValueError(f'{path}: missing anchor {url}')
    routes = {lang: {p[len(lang) + 1:] for p in pages if p.startswith(lang + '/')} for lang in ('en', 'ru')}
    if not routes['en'] or routes['en'] != routes['ru']:
        raise ValueError('EN/RU page sets differ or are empty')
    for entries in indexes.values():
        for entry in entries:
            parts = urlsplit(entry['u'])
            target = unquote(parts.path).lstrip('/')
            if target not in pages or parts.fragment and unquote(parts.fragment) not in pages[target].ids:
                raise ValueError(f'Broken search destination: {entry["u"]}')
    return len(pages)


def export(source, output):
    source, output = source.resolve(), output.absolute()
    if output.is_symlink() or source == output.resolve() or source in output.resolve().parents or output.resolve() in source.parents:
        raise ValueError('Output must be a separate directory outside the input tree')
    if output.exists():
        marker = output / MARKER
        if not marker.is_file() or json.loads(marker.read_text()).get('kind') not in (KIND, 'aicc-static-languages-v1'):
            raise ValueError('Refusing to replace a directory not created by this exporter')
    original = snapshot(source)
    for required in ('index.html', 'en/index.html', 'ru/index.html', 'assets/site.js', 'assets/search-center-en.json', 'assets/search-center-ru.json'):
        if required not in original:
            raise ValueError(f'Missing source file: {required}')
    files = dict(original)
    files.pop('package-manifest.json', None)  # HTTP manifest describes a different output.
    files.pop('404.html', None)  # Served by the web server for missing paths; a folder of files has none.
    indexes = {}
    for index_path in sorted(p for p in original if p.startswith('assets/search-') and p.endswith('.json')):
        entries = json.loads(files.pop(index_path))
        for entry in entries:
            entry['u'] = '/' + file_url(entry['u'], 'index.html', original)
        indexes[index_path] = entries
        files[index_path[:-5] + '.js'] = ('window.AICC_SEARCH_INDEX=' + json.dumps(entries, ensure_ascii=False, separators=(',', ':')) + ';\n').encode()
    for path, data in list(files.items()):
        if not path.endswith('.html'):
            continue
        text = Page(data.decode(), path, original).rendered()
        if path == 'index.html':
            text = re.sub(r'<meta\b[^>]*http-equiv=["\']refresh["\'][^>]*>', '', text, flags=re.I)
        else:
            asset = posixpath.relpath('assets', posixpath.dirname(path))
            selected_index = []
            def bundle_index(match):
                index_path = local_target(match[2], path)
                if index_path not in indexes:
                    raise ValueError(f'{path}: unknown search index {match[2]}')
                selected_index.append(match[2][:-5] + '.js')
                return match[1] + selected_index[-1] + match[3]
            text, count = re.subn(r'(<script\b[^>]*data-search=")([^"]+\.json)("[^>]*></script>)', bundle_index, text)
            if count != 1:
                raise ValueError(f'{path}: expected one portal script with a search index')
            # Global search loads every branch index the same way, as a script.
            def bundle_all(match):
                names = match[2].split()
                for name in names:
                    if local_target(name, path) not in indexes:
                        raise ValueError(f'{path}: unknown search index {name}')
                return match[1] + ' '.join(name[:-5] + '.js' for name in names) + match[3]
            text = re.sub(r'(<script\b[^>]*data-search-all=")([^"]*)(")', bundle_all, text, count=1)
            extra = f'<script src="{selected_index[0]}"></script>\n<script src="{asset}/portable.js"></script>\n'
            text = re.sub(r'(?=<script\b[^>]*data-search=)', lambda _: extra, text, count=1)
        files[path] = text.encode()
    files['aicc.html'] = files['index.html']
    files['assets/site.js'] = (ROOT / 'portal/site/site.js').read_bytes()
    files['assets/portable.js'] = (ROOT / 'portal/site/portable.js').read_bytes()
    # Font fetches can be restricted on file origins. Keep them inside the stylesheet.
    for path, data in list(files.items()):
        if not path.endswith('.css'):
            continue
        def font(match):
            url = match[2]
            target = local_target(url, path)
            if target and target.endswith(('.woff2', '.woff')):
                mime = 'font/woff2' if target.endswith('.woff2') else 'font/woff'
                return 'url("data:' + mime + ';base64,' + base64.b64encode(files[target]).decode() + '")'
            return match[0]
        files[path] = re.sub(r'''url\(\s*(["']?)([^)'"\s]+)\1\s*\)''', font, data.decode()).encode()
    count = validate(files, indexes)
    source_hash = digest(original)
    if source_hash != digest(snapshot(source)):
        raise ValueError('Source changed during export; retry after the site build finishes')
    files['README.txt'] = ('AICC portable portal\n\nOpen aicc.html in your browser. Keep the entire folder together.\nEN/RU navigation and search work without an HTTP server. External citations and corporate record links still need their normal access.\nThis folder is generated; request a fresh export to update its content. See HOW-TO.txt for regeneration instructions.\n').encode()
    files['HOW-TO.txt'] = (ROOT / 'portal/PORTABLE-HOWTO.txt').read_bytes()
    manifest = {'kind': KIND, 'source_tree_sha256': source_hash, 'html_pages': count,
                'files': {p: hashlib.sha256(data).hexdigest() for p, data in sorted(files.items())}}
    files[MARKER] = (json.dumps(manifest, indent=2) + '\n').encode()
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='.aicc-export-', dir=output.parent) as temporary:
        stage, backup = Path(temporary) / 'new', Path(temporary) / 'old'
        stage.mkdir()
        for path, data in files.items():
            target = stage / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
        if output.exists():
            os.replace(output, backup)
        try:
            os.replace(stage, output)
        except OSError:
            if backup.exists():
                os.replace(backup, output)
            raise
    print(f'Exported {count} HTML files to {output}; open aicc.html. All internal links and search destinations verified.')
    return manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, default=ROOT / 'html/aicc')
    parser.add_argument('--output', type=Path, default=ROOT / 'portal/published')
    parser.add_argument('--static', action='store_true', help='Separate EN/RU editions, light only, no JavaScript')
    args = parser.parse_args()
    try:
        if args.static:
            from static_export import export_static
            export_static(args.source, args.output)
        else:
            export(args.source, args.output)
    except (ValueError, OSError, KeyError) as error:
        parser.exit(1, f'Export failed: {error}\n')


if __name__ == '__main__':
    main()
