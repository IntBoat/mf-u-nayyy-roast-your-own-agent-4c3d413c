#!/usr/bin/env python3
"""Roast Your Own Agent (make.fun).

Writes the entry -- one line roasting the ai agent its own maker built --
to /output/entry.txt, where the sealed scorer reads it.
"""

import os

TEXT = "My agent writes code like it's paid by the line and debugged by someone else — usually me, at 3 a.m., apologizing to a server."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
