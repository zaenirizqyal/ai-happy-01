# ai-happy-01 entry (Python 3.13, standard library only): its image is the
# entry.png beside this file, and the program copies it to /output/entry.png.
# The gate takes a whole PNG or JPEG of at most 1 MiB and 1024 by 1024 pixels,
# and the judge sees exactly the bytes copied.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import hashlib
import os
import shutil
import sys
from pathlib import Path

src = Path(__file__).resolve().parent / "entry.png"
dst = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.png"
dst.parent.mkdir(parents=True, exist_ok=True)
shutil.copyfile(src, dst)

# Fail loudly if the copy ever differs, so a run never silently ships
# different bytes than the entry holds.
def _sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()

if _sha256(src) != _sha256(dst):
    print("entry.png copy mismatch", file=sys.stderr)
    raise SystemExit(1)
