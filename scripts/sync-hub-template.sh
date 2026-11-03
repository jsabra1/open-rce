#!/bin/sh
# Make jsabra1/rce-hub-template match engine/skills/rcx/assets/hub-template/.
# Usage: scripts/sync-hub-template.sh   (run from the open-rce root; needs gh login)
set -eu
SRC="$(cd "$(dirname "$0")/.." && pwd)/engine/skills/rcx/assets/hub-template"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
gh repo clone jsabra1/rce-hub-template "$TMP/t" -- -q
rsync -a --delete --exclude .git "$SRC/" "$TMP/t/"
cd "$TMP/t"
if [ -z "$(git status --porcelain)" ]; then echo "Template already matches."; exit 0; fi
git status --short
git add -A
git commit -q -m "Sync starter hub from open-rce $(git -C "$SRC" describe --tags --always 2>/dev/null || echo main)"
git push -q
echo "Template updated."
