#!/usr/bin/env python3
"""Check served and downloaded guides for missing local files or stale manifests."""
import argparse
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
from urllib.parse import unquote, urlsplit
from zipfile import ZipFile


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.references = []

    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key in ("src", "href") and value:
                self.references.append(value)


def check_files(files):
    checked = 0
    for name, data in files.items():
        if not name.endswith(".html"):
            continue
        parser = Links()
        parser.feed(data.decode("utf-8"))
        for ref in parser.references:
            url = urlsplit(ref)
            if url.scheme or url.netloc or not url.path:
                continue
            target = (Path(name).parent / unquote(url.path)).as_posix()
            assert target in files, f"Missing local resource: {name} → {ref}"
            checked += 1
    manifest = json.loads(files["manifest.json"])
    for entry in manifest["files"]:
        data = files[entry["path"]]
        assert len(data) == entry["bytes"], entry["path"]
        assert hashlib.sha256(data).hexdigest() == entry["sha256"], entry["path"]
    return {"pages": sum(name.endswith(".html") for name in files), "references": checked,
            "hashes": len(manifest["files"])}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path)
    root = parser.parse_args().output
    served = {p.relative_to(root).as_posix(): p.read_bytes() for p in root.rglob("*") if p.is_file()}
    with ZipFile(root / "o-uiux-kit.zip") as archive:
        downloaded = {name: archive.read(name) for name in archive.namelist()}
    print(json.dumps({"served": check_files(served), "downloaded": check_files(downloaded)}, indent=2))
