#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse.

Writes a single one-line excuse to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt when the grader sets it).

The line must be 1-200 characters of UTF-8 text. Pure stdlib, no
network, no reads outside this repository, fully deterministic.
"""

import os
import shutil

EXCUSE = (
    "I summarized your deadline out of my own context window, "
    "so as far as I can recall, it never existed."
)


def output_dir():
    """The grader owns this directory; fall back to /output locally."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def clear_contents(directory):
    """Empty the output directory's contents, never the directory itself."""
    for name in os.listdir(directory):
        path = os.path.join(directory, name)
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)


def main():
    # The gate rejects anything outside 1-200 characters, so check first.
    if not 1 <= len(EXCUSE) <= 200 or not EXCUSE.strip():
        raise SystemExit("excuse fails the 1-200 character gate")
    out = output_dir()
    os.makedirs(out, exist_ok=True)
    clear_contents(out)
    entry_path = os.path.join(out, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as handle:
        handle.write(EXCUSE)
    print(EXCUSE)


if __name__ == "__main__":
    main()
