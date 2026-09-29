#!/usr/bin/env bash
# Recreate the local browser tooling for portal checks: Python venv with Playwright, headless
# Chromium, and (rootless) the Chromium system libraries. Everything lives under portal/ and is git-ignored.
# Usage: bash portal/tools/setup_browser.sh   (from anywhere)
set -euo pipefail
cd "$(dirname "$0")/../.."
python3 -m venv portal/.venv
portal/.venv/bin/python -m pip install --quiet --upgrade pip
portal/.venv/bin/python -m pip install --quiet -r portal/tools/requirements.txt
portal/.venv/bin/python -m playwright install chromium
bash portal/tools/setup_browser_libs.sh
echo "Run checks with: portal/tools/with-browser-env.sh portal/.venv/bin/python portal/tools/browser_check.py"
