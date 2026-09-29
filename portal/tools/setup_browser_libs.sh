#!/usr/bin/env bash
# Install Playwright's Chromium system libraries WITHOUT root, into a local prefix.
# Needed on hosts (e.g. this sandboxed container) where `playwright install-deps`
# cannot run because there is no root / "no new privileges" is set.
#
# Downloads the exact apt packages Playwright reports and extracts them under
# portal/.tools/pw-syslibs/ (git-ignored). Use tools/with-browser-env.sh to run
# Playwright against them. Re-run after `playwright install` changes the browser.
set -euo pipefail
cd "$(dirname "$0")/../.."                       # repo root
VENV=portal/.venv/bin/python
PREFIX=portal/.tools/pw-syslibs
TMP=$(mktemp -d)

echo "Resolving Chromium system dependencies..."
{ "$VENV" -m playwright install-deps --dry-run chromium 2>&1 || true; } | grep '^  ' | tr -d ' ' | sort -u > "$TMP/pkgs.txt"
echo "  $(wc -l < "$TMP/pkgs.txt") packages"

echo "Downloading (no root)..."
( cd "$TMP" && apt-get download $(cat pkgs.txt) )

echo "Extracting into $PREFIX ..."
rm -rf "$PREFIX"; mkdir -p "$PREFIX"
for f in "$TMP"/*.deb; do dpkg-deb -x "$f" "$PREFIX"; done
rm -rf "$TMP"

# Headless Chromium needs a working fontconfig or it aborts (SkFontMgr ... Not implemented).
# Point fontconfig at the fonts we extracted and a writable cache, then build the cache.
ABS="$(cd "$PREFIX" && pwd)"
mkdir -p "$ABS/var/cache/fontconfig"
cat > "$ABS/etc/fonts/portal.conf" <<EOF
<?xml version="1.0"?>
<!DOCTYPE fontconfig SYSTEM "fonts.dtd">
<fontconfig>
  <dir>$ABS/usr/share/fonts</dir>
  <cachedir>$ABS/var/cache/fontconfig</cachedir>
  <include ignore_missing="yes">$ABS/etc/fonts/conf.d</include>
  <config></config>
</fontconfig>
EOF
LD_LIBRARY_PATH="$ABS/usr/lib/x86_64-linux-gnu:$ABS/lib/x86_64-linux-gnu:$ABS/usr/lib" \
  FONTCONFIG_FILE="$ABS/etc/fonts/portal.conf" \
  "$ABS/usr/bin/fc-cache" -f >/dev/null 2>&1 || echo "  (fc-cache warning; continuing)"

echo "Done. $(du -sh "$PREFIX" | cut -f1) in $PREFIX"
echo "Run Playwright via: portal/tools/with-browser-env.sh portal/.venv/bin/python <script>"
