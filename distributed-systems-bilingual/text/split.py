#!/usr/bin/env python3
"""把 full.txt 按章切分到 chapters/chNN.txt，并去掉水印行。"""
import os
import re
import pathlib

HERE = pathlib.Path(__file__).parent

CHAPTER_STARTS = [
    (1, "01-introduction"),
    (2, "02-architectures"),
    (3, "03-processes"),
    (4, "04-communication"),
    (5, "05-coordination"),
    (6, "06-naming"),
    (7, "07-consistency-and-replication"),
    (8, "08-fault-tolerance"),
    (9, "09-security"),
]

WATERMARK = re.compile(r"downloaded by gwenlita52299@gmail\.com")
RUNNING = re.compile(r"^\s*(DS 4\.03|)\s*$")


def main() -> None:
    text = (HERE / "full.txt").read_text(encoding="utf-8", errors="replace")

    # 找到每个章开头的行号（两个数字单独成行那种）
    lines = text.splitlines()
    marks = []
    for i, ln in enumerate(lines):
        if re.fullmatch(r"\s*0[1-9]\s*", ln):
            marks.append(i)
    marks = marks[: len(CHAPTER_STARTS)]

    outdir = HERE / "chapters"
    outdir.mkdir(exist_ok=True)

    for idx, (num, slug) in enumerate(CHAPTER_STARTS):
        start = marks[idx]
        end = marks[idx + 1] if idx + 1 < len(marks) else len(lines)
        chunk = lines[start:end]
        cleaned = []
        for ln in chunk:
            if WATERMARK.search(ln):
                continue
            cleaned.append(ln.rstrip())
        (outdir / f"ch{num:02d}.txt").write_text("\n".join(cleaned), encoding="utf-8")
        print(f"ch{num:02d} -> {slug}: {len(cleaned)} lines")


if __name__ == "__main__":
    main()
