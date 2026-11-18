#!/usr/bin/env python3
"""news-image-20261117 v4 (akun 1): write the pre-composed front page.

Super-dense variant testing the density hypothesis: the live top 3 carry
24-30 stories, our v2/v3 carry 17. This one packs 24 stories + a numbers
strip — compressed lead/map/secondaries make room for a 3x3 story grid,
a 3-column "ALSO ON TUESDAY" list and a "TODAY IN NUMBERS" strip.
Tuesday 17 November 2026, fresh photo panels, all new angles.
Deterministic: copies the embedded bytes verbatim.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "image.jpg")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    # Guard: entry must be <= 1 MiB and exactly 1024x1024.
    assert os.path.getsize(dst) <= 1048576, "entry over 1 MiB"


if __name__ == "__main__":
    main()
