#!/usr/bin/env bash
# Run a command with the local Playwright browser libraries on the loader path.
# Usage: portal/tools/with-browser-env.sh portal/.venv/bin/python portal/tools/check_style_lab.py
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
PREFIX="$ROOT/portal/.tools/pw-syslibs"
if [ ! -d "$PREFIX" ]; then
  echo "Browser libs missing. Run: portal/tools/setup_browser_libs.sh" >&2
  exit 1
fi
export LD_LIBRARY_PATH="$PREFIX/usr/lib/x86_64-linux-gnu:$PREFIX/lib/x86_64-linux-gnu:$PREFIX/usr/lib${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
export FONTCONFIG_PATH="$PREFIX/etc/fonts"
export FONTCONFIG_FILE="$PREFIX/etc/fonts/portal.conf"
exec "$@"
