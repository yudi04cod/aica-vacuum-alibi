# SPDX-License-Identifier: MIT
"""The Vacuum's Alibi: one line, 200 characters or fewer.

Writes the funniest one-line excuse a robot vacuum can give for
missing a spot to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Python standard library only. Deterministic: the same bytes every run.
"""

import os
import sys

MAX_CHARS = 200

LINE = (
    "I didn't miss that spot — my sensors registered it as a protected "
    "dust habitat, and I never evict a tenant without a court order."
)


def validate(line: str) -> str:
    """Return the line if it is one sentence of 1-200 characters."""
    line = line.strip()
    if not line:
        raise ValueError("entry line must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(line)} characters, over the {MAX_CHARS} limit"
        )
    if line.count(".") != 1 or not line.endswith("."):
        raise ValueError("entry line must be exactly one sentence")
    return line


def main() -> int:
    line = validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line)
    print(f"wrote {path} ({len(line)} characters)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
