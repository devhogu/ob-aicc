#!/usr/bin/env python3
# START_MODULE_CONTRACT
#   PURPOSE: Assemble the walkable end-to-end pack of v1: the folder edition of the site, which carries the source documents, and a zip for sharing.
#   SCOPE: Writes only the output folder (default portal/published) and the zip beside it; reads the built html/aicc/v1 and the source folders.
#   DEPENDS: export_portable
#   LINKS: M-PORTABLE-EXPORT, C-HUB-V2
# END_MODULE_CONTRACT
#
# START_MODULE_MAP
#   pack - export the folder edition, add the sources and their index, write the zip
# END_MODULE_MAP
"""Pack v1 end to end: open aicc.html in the folder, or share the zip."""
import argparse
import hashlib
from pathlib import Path
import zipfile

import export_portable

ROOT = Path(__file__).resolve().parents[2]
TOP = 'aicc-v1'


# START_CONTRACT: pack
#   PURPOSE: Export the folder edition of v1 with its source documents and write the zip.
#   INPUTS: { source: Path - built v1 site; output: Path - pack folder; archive: Path - zip file }
#   OUTPUTS: { dict - file counts and the zip checksum }
#   SIDE_EFFECTS: Replaces the output folder and the zip.
# END_CONTRACT: pack
def pack(source, output, archive):
    export_portable.export(source, output)
    listing = sorted(p for p in (output / 'sources').rglob('*') if p.is_file())
    archive.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) as bundle:
        for path in sorted(p for p in output.rglob('*') if p.is_file()):
            bundle.write(path, Path(TOP) / path.relative_to(output))
    return {'site_files': sum(1 for p in output.rglob('*') if p.is_file()) - len(listing), 'source_files': len(listing),
            'zip': str(archive), 'zip_bytes': archive.stat().st_size, 'zip_sha256': hashlib.sha256(archive.read_bytes()).hexdigest()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, default=ROOT / 'html/aicc/v1')
    parser.add_argument('--output', type=Path, default=ROOT / 'portal/published')
    parser.add_argument('--zip', type=Path, default=ROOT / 'portal/aicc-v1.zip')
    args = parser.parse_args()
    for key, value in pack(args.source, args.output, args.zip).items():
        print(f'{key}: {value}')


if __name__ == '__main__':
    main()
