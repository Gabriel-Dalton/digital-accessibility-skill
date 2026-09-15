#!/usr/bin/env bash
# Builds digital-accessibility.skill (a zip archive) from the digital-accessibility/ folder.
set -euo pipefail
cd "$(dirname "$0")/.."
out="digital-accessibility.skill"
rm -f "$out"
python - "$out" <<'PY'
import sys, zipfile, pathlib
out = sys.argv[1]
root = pathlib.Path("digital-accessibility")
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    for p in sorted(root.rglob("*")):
        if p.is_file():
            z.write(p, p.as_posix())
print(f"wrote {out}")
PY
