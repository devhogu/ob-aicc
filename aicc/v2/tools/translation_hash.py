#!/usr/bin/env python3
# START_MODULE_CONTRACT
#   PURPOSE: Print the hash a translation records for its Russian source, so a translator can mark the translation current.
#   SCOPE: Reads one Russian source file; writes nothing.
#   DEPENDS: M-PORTAL-LOCALIZATION
#   LINKS: C-HUB-V2-EN
# END_MODULE_CONTRACT
#
# START_MODULE_MAP
#   main - print the source hash of each file given
# END_MODULE_MAP
"""python3 aicc/v2/tools/translation_hash.py <Russian file> ... : pages and catalog pages hash the whole file; data files (.yaml, .json) hash their Russian part only."""
import json
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import parity  # noqa: E402


def main(paths):
    for name in paths:
        path = Path(name)
        raw = path.read_text(encoding='utf-8')
        if path.suffix in ('.yaml', '.yml', '.json'):
            data = json.loads(raw) if path.suffix == '.json' else yaml.safe_load(raw)
            value = parity.source_hash(json.dumps(parity.russian_part(data), ensure_ascii=False, sort_keys=True, default=str))
        else:
            value = parity.source_hash(raw)
        print(f'{value}  {name}')


if __name__ == '__main__':
    main(sys.argv[1:])
