#!/usr/bin/env python3
"""Split the extracted PDF text into per-chapter files.

Boundaries are 1-indexed line numbers located by heading grep on full.txt.
The repeated watermark line is stripped.
"""
import re
from pathlib import Path

HERE = Path(__file__).parent
SRC = HERE / "full.txt"
OUT = HERE / "chapters"
OUT.mkdir(exist_ok=True)

BOUNDARIES = [
    ("00-front-matter", 1),
    ("01-a-pragmatic-philosophy", 717),
    ("02-a-pragmatic-approach", 1626),
    ("03-the-basic-tools", 3558),
    ("04-pragmatic-paranoia", 5151),
    ("05-bend-or-break", 6505),
    ("06-while-you-are-coding", 7995),
    ("07-before-the-project", 9307),
    ("08-pragmatic-projects", 10211),
]

WATERMARK = re.compile(r"^Prepared exclusively for Zach\s*$")
BLANK_RUN = re.compile(r"\n{3,}")


def clean(text: str) -> str:
    lines = [ln for ln in text.splitlines() if not WATERMARK.match(ln)]
    return BLANK_RUN.sub("\n\n", "\n".join(lines)).strip() + "\n"


def main() -> None:
    lines = SRC.read_text(encoding="utf-8", errors="replace").splitlines(keepends=True)
    total = len(lines)
    spans = []
    for i, (name, start) in enumerate(BOUNDARIES):
        end = BOUNDARIES[i + 1][1] - 1 if i + 1 < len(BOUNDARIES) else total
        spans.append((name, start, end))
    for name, start, end in spans:
        chunk = "".join(lines[start - 1:end])
        (OUT / f"{name}.txt").write_text(clean(chunk), encoding="utf-8")
        print(f"{name:<28} lines {start:>6}-{end:<6} ({end - start + 1:>5} lines)")


if __name__ == "__main__":
    main()
