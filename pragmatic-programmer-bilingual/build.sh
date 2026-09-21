#!/usr/bin/env bash
# 编译中英对照本（XeLaTeX 需要跑两遍以生成目录/交叉引用）
set -euo pipefail
export PATH="/Library/TeX/texbin:$PATH"

JOB="main"
ENGINE="xelatex"
FLAGS="-interaction=nonstopmode -halt-on-error -synctex=1"

cd "$(dirname "$0")"

mkdir -p build
$ENGINE $FLAGS -output-directory=build "$JOB.tex"
$ENGINE $FLAGS -output-directory=build "$JOB.tex"

cp -f "build/$JOB.pdf" "./$JOB.pdf" 2>/dev/null || true
echo "OK -> $JOB.pdf"
