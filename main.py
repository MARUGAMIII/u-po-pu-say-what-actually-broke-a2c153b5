#!/usr/bin/env python3
"""Say What Actually Broke entry.

Writes a single original line of software error copy (at most 200
characters) to /output/entry.txt. The line tells the brutal truth about
a failed save -- the disk ran out of space mid-write -- and says what
to do next, in a way a real product could ship in an error dialog.
"""

import os

LINE = (
    "Your disk is full. We saved what fit and threw the rest away, "
    "so your file now ends mid-sentence. Free up space and save again."
)


def main() -> None:
    if not 1 <= len(LINE) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(LINE)}")
    if not LINE.isascii():
        raise ValueError("entry must be ASCII only")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
