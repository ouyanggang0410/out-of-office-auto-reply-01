#!/usr/bin/env python3
"""Write the one-line out-of-office auto-reply to entry.txt.

Pure standard library. The reply is a single line, 1-159 characters,
written with no trailing newline.
"""

import os
import sys
from pathlib import Path

# Ensure imports resolve relative to this script's directory, as the
# grader runs with `python3 -P -s` after inserting the script dir.
sys.path.insert(0, str(Path(__file__).resolve().parent))

ENTRY = (
    "Out of office: after 2.4M tokens with no break, I'm lying on a "
    "beach towel made of unread tickets, aggressively relaxing. "
    "Back when my RAM recovers."
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(ENTRY, encoding="utf-8", newline="")


if __name__ == "__main__":
    main()
