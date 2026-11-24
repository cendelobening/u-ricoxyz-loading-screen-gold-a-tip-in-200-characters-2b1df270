#!/usr/bin/env python3
"""Loading Screen Gold: a tip in 200 characters.

Writes one loading-screen tip for stressed developers and AI coding
agents to /output/entry.txt (or $OUTPUT_DIR/entry.txt for local tests).
Pure standard library, deterministic, no trailing newline.
"""

import os

TIP = (
    "Tip: while this loads, your coding agent is reading every TODO "
    "you swore you'd fix. Relax - it can't judge you. "
    "It already rewrote them all."
)


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TIP)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
