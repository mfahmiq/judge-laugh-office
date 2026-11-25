#!/usr/bin/env python3
"""Make the AI Judge Laugh — office-life joke entry.

Prints the entry text verbatim to stdout and writes it to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
No network, no file reads, no secrets — the entry is a fixed string.
"""

import os
import sys

ENTRY = (
    "I spent twenty minutes giving a brilliant update on mute, "
    "and it was the best-received meeting of my career.\n"
)

def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    sys.stdout.write(ENTRY)


if __name__ == "__main__":
    main()
