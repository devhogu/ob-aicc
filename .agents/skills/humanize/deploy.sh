#!/bin/sh
# humanize 1.10.4: deploy into a repository (idempotent). Usage: ./deploy.sh /path/to/repo [options]
# Options: --providers claude,codex  --vale auto|download|system|skip  --dry-run   (see: ./deploy.sh --help)
# Guides: docs/DEPLOY.md (deploy, update, remove), docs/ACCEPTANCE.md (verify and accept), docs/USAGE.md (use)
# Environment: HUMANIZE_PYTHON selects the Python (3.9+); see docs/DEPENDENCIES.md.
set -eu
DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd -P)
ok() { "$1" -c 'import sys; sys.exit(0 if sys.version_info >= (3, 9) else 1)' >/dev/null 2>&1; }
PY=${HUMANIZE_PYTHON:-}
if [ -n "$PY" ]; then
  ok "$PY" || { echo "humanize: HUMANIZE_PYTHON=$PY is not Python 3.9+" >&2; exit 1; }
else
  for c in python3 python3.14 python3.13 python3.12 python3.11 python3.10 python3.9 \
           /opt/homebrew/bin/python3 /usr/local/bin/python3 /usr/bin/python3; do
    if command -v "$c" >/dev/null 2>&1 && ok "$c"; then PY=$(command -v "$c"); break; fi
  done
  [ -n "$PY" ] || { echo "humanize: Python 3.9+ not found; install it or set HUMANIZE_PYTHON" >&2; exit 1; }
fi
export PYTHONUTF8=1 PYTHONDONTWRITEBYTECODE=1
PYTHONPATH="$DIR${PYTHONPATH:+:$PYTHONPATH}" exec "$PY" -m humanize deploy "$@"
