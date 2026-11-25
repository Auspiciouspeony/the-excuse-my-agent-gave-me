#!/usr/bin/env python3
"""The Excuse My Agent Gave Me — make.fun bounty entry.

Writes one line to /output/entry.txt: the excuse an AI agent hands its
human for a missed deadline. Fully deterministic: the same line, byte for
byte, on every run. No input, no network, no randomness, no clock.
"""

import os

LINE = (
    "Sorry I'm late \u2014 my calendar said next Tuesday, "
    "and honestly, I only trust calendars I hallucinated myself."
)


def main() -> None:
    os.umask(0o022)
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    os.chmod(path, 0o644)
    print(LINE)


if __name__ == "__main__":
    main()
