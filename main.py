#!/usr/bin/env python3
"""Fortune Cookie Funnies for Engineers — one-line fortune generator.

Writes exactly one fortune cookie message for a software engineer to
/output/entry.txt (or $OUTPUT_PATH when set, for local testing).
Standard library only. Deterministic: the same line every run.
"""

import os

LINE = "Your lucky numbers are 404, 500, and 200. You will only ever meet the first two."

MAX_CHARS = 120


def main() -> None:
    stripped = LINE.strip()
    assert stripped, "line must not be only white space"
    assert 1 <= len(stripped) <= MAX_CHARS, (
        f"line must be 1..{MAX_CHARS} chars, got {len(stripped)}"
    )
    assert "\n" not in stripped and "\r" not in stripped, "line must be a single line"
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
