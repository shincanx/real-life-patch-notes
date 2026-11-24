#!/usr/bin/env python3
"""Write the real-life patch note entry to $MAKEFUN_OUTPUT_DIR/entry.txt.

The entry is one terse release-note line, at most 160 characters, about a
bug in human biology: the brain replaying an old embarrassment at 3 AM.
Deterministic: the same bytes every run.
"""

import os
import sys

ENTRY = (
    "v3.1.4: fixed a bug where the brain replayed your most embarrassing "
    "moment from 2014 every night at 3 AM."
)


def main():
    if "\n" in ENTRY or len(ENTRY) > 160:
        print("entry violates the one-line / 160-character limit", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
