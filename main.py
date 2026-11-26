#!/usr/bin/env python3
"""The Printer Apology — a one-line apology from an office printer.

Writes a single funny apology line to /output/entry.txt (max 120 chars).
"""

import os

ENTRY = (
    "Sorry I jammed on your deadline, ate the good paper, "
    "and blamed the Wi-Fi. In my defence, you feed me like a shredder."
)


def main() -> None:
    # Gate: one line, 1-120 chars, not only whitespace.
    line = ENTRY.strip()
    assert 1 <= len(line) <= 120, f"entry is {len(line)} chars"
    assert "\n" not in line, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
