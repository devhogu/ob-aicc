"""Audit the preserved history and verified candidate, before or after archival."""
import hashlib
import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET

BUNDLE = Path(__file__).resolve().parent
ROOT = BUNDLE.parents[3]
CHANGES = ROOT / '.grace/changes'


def digest(data):
    return hashlib.sha256(data).hexdigest()


def check():
    inventory = json.loads((BUNDLE / 'closure-inventory.json').read_text())
    errors = []
    for item in inventory['changes']:
        name, status = item['change'], item['disposition']
        archived = CHANGES / 'archive' / name
        if not archived.is_dir() or (CHANGES / 'active' / name).exists():
            errors.append(name + ': not archived')
            continue
        for relative, expected in item['original_files'].items():
            actual = relative
            invalid_original = name == 'C-RU-NATURAL-ALIGNMENT' and relative == 'plan.xml'
            if invalid_original:
                actual = 'plan.original.xml.txt'
            path = archived / actual
            if not path.is_file():
                errors.append(str(path) + ': missing historical file')
                continue
            data = path.read_bytes()
            if relative in ('spec.xml', 'plan.xml') and not invalid_original:
                document = ET.fromstring(data)
                if document.get('status') != status:
                    errors.append(name + ': wrong terminal status')
                text = data.decode()
                if status == 'superseded':
                    replacement = '\n    <Replacement>C-BASELINE-CLOSURE</Replacement>'
                    if replacement not in text:
                        errors.append(name + ': missing explicit replacement')
                    text = text.replace(replacement, '', 1)
                original_status = 'draft' if name == 'C-PORTAL-CHARTER' else 'approved'
                text = re.sub(r'status="' + status + '"', 'status="' + original_status + '"', text, count=1)
                data = text.encode()
            if digest(data) != expected:
                errors.append(name + '/' + relative + ': historical content changed')
        if not (archived / 'closeout.md').is_file():
            errors.append(name + ': missing closeout')
        if status == 'applied':
            gate = json.loads((archived / 'closeout-grace.json').read_text())
            if gate.get('assertionMode') != 'final' or not gate.get('commandsEnabled') or gate['summary']['errors']:
                errors.append(name + ': final gate did not pass')
    previous = CHANGES / 'archive/C-BASELINE-CLOSURE'
    for filename in ('spec.xml', 'plan.xml'):
        document = ET.parse(previous / filename).getroot()
        if document.get('status') != 'superseded' or document.findtext('.//Replacement') != 'C-BASELINE-CLOSURE-FINAL':
            errors.append('First reconciliation plan lacks its replacement')
    for relative, expected in json.loads((BUNDLE / 'protected-sources.json').read_text()).items():
        path = ROOT / relative
        if not path.is_file() or digest(path.read_bytes()) != expected:
            errors.append(relative + ': protected current source changed')
    evidence = json.loads((BUNDLE / 'verification-evidence.json').read_text())
    generated = {p.relative_to(ROOT / 'html/aicc').as_posix(): digest(p.read_bytes()) for p in (ROOT / 'html/aicc').rglob('*') if p.is_file()}
    if generated != evidence['generated_files']:
        errors.append('Generated site differs from verified candidate')
    for name in ('neighbours', 'portable'):
        report = evidence['browser'][name]
        if name == 'neighbours' and report['errors']:
            errors.append('Neighbour browser errors')
        if name == 'portable' and report['status'] != 'passed':
            errors.append('Portable browser did not pass')
    remaining = sorted(p.name for p in (CHANGES / 'active').glob('C-*') if p.name != BUNDLE.name)
    if remaining:
        errors.append('Unexpected active changes: ' + ', '.join(remaining))
    print(json.dumps({'prior_changes': len(inventory['changes']), 'protected_sources': len(json.loads((BUNDLE / 'protected-sources.json').read_text())), 'generated_files': len(generated), 'errors': errors}, indent=2))
    return bool(errors)


if __name__ == '__main__':
    raise SystemExit(check())
