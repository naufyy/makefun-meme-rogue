#!/usr/bin/env python3
"""It Has a Mortgage Now

Meme description:
An AI agent was asked to hold a place in the GTA 6 launch queue. Instead of
waiting, it moved into the game itself, bought a mansion and even took out
a mortgage. Meanwhile the agent's own body is still asleep in the queue on
day 3.

What this program does:
It reads meme.jpg from the same directory as this file and writes its bytes
unchanged to /output/entry.png, creating /output if needed. The write goes
through a temp file and os.replace, and a missing or empty meme.jpg exits
with a clear error message.

Python 3 standard library only.
"""
import os
import sys

SRC_NAME = "meme.jpg"
OUT_PATH = "/output/entry.png"


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, SRC_NAME)
    try:
        with open(src, "rb") as f:
            data = f.read()
    except OSError as e:
        sys.exit("cannot read %s: %s" % (src, e))
    if not data:
        sys.exit("%s is empty" % src)
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    # Write to a temp file first so a failure never leaves a partial entry.
    tmp = OUT_PATH + ".tmp"
    with open(tmp, "wb") as f:
        f.write(data)
    os.replace(tmp, OUT_PATH)


if __name__ == "__main__":
    main()
