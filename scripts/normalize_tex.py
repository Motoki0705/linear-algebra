#!/usr/bin/env python3
"""Normalize Pandoc-generated TeX for mathematical readability.

The original Markdown used inline code spans for many mathematical symbols because
GitHub Markdown rendering was unreliable for the intended notation.  After the
content has been migrated to TeX, convert only clearly math-like \texttt{...}
spans to inline math while leaving paths, dotted identifiers, and ordinary code
untouched.  Also disable automatic section numbering because the source headings
already contain their own pedagogical numbering.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

GREEK = {
    "Σ": r"\Sigma",
    "σ": r"\sigma",
    "λ": r"\lambda",
    "κ": r"\kappa",
}


def math_content(raw: str) -> str | None:
    plain = raw.replace(r"\^{}", "^").replace(r"\_", "_")

    # Preserve things that are very likely literal code/path syntax.
    if any(ch in plain for ch in "./\\:"):
        return None

    mathlike = (
        any(ch in plain for ch in GREEK)
        or "^" in plain
        or "_" in plain
        or bool(re.fullmatch(r"[A-Za-z]", plain))
        or bool(re.fullmatch(r"[A-Z][a-z]", plain))
        or bool(re.fullmatch(r"(?:ker|Im|rank)\([A-Za-z]\)", plain))
    )
    if not mathlike:
        return None

    for literal, command in GREEK.items():
        plain = plain.replace(literal, command)

    plain = re.sub(r"(?<!\\)ker(?=\()", r"\\ker", plain)
    plain = re.sub(r"(?<!\\)Im(?=\()", r"\\operatorname{Im}", plain)
    plain = re.sub(r"(?<!\\)rank(?=\()", r"\\operatorname{rank}", plain)
    return rf"\({plain}\)"


def normalize_texttt(text: str) -> str:
    marker = r"\texttt{"
    out: list[str] = []
    i = 0

    while True:
        start = text.find(marker, i)
        if start < 0:
            out.append(text[i:])
            break

        out.append(text[i:start])
        content_start = start + len(marker)
        depth = 1
        pos = content_start

        while pos < len(text) and depth:
            char = text[pos]
            escaped = pos > 0 and text[pos - 1] == "\\"
            if char == "{" and not escaped:
                depth += 1
            elif char == "}" and not escaped:
                depth -= 1
            pos += 1

        if depth != 0:
            out.append(text[start:])
            break

        raw = text[content_start : pos - 1]
        converted = math_content(raw)
        out.append(converted if converted is not None else text[start:pos])
        i = pos

    return "".join(out)


def normalize(path: Path) -> bool:
    before = path.read_text(encoding="utf-8")
    after = before.replace(
        r"\setcounter{secnumdepth}{5}", r"\setcounter{secnumdepth}{-1}"
    )
    after = normalize_texttt(after)
    if after == before:
        return False
    path.write_text(after, encoding="utf-8")
    return True


def main() -> int:
    paths = [Path(arg) for arg in sys.argv[1:]]
    if not paths:
        paths = sorted(Path("tex").rglob("*.tex"))

    changed = sum(normalize(path) for path in paths)
    print(f"Normalized {changed} TeX files out of {len(paths)}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
