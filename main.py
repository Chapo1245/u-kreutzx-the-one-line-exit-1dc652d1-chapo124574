#!/usr/bin/env python3
"""The One-Line Exit — writes one funny resignation letter to /output/entry.txt.

The entry is a single fixed line, chosen by hand: a resignation letter
whose joke lands in one twist. The program is fully deterministic — it
writes the same bytes on every run. Standard library only.
"""

import os

LINE = "Dear Sir, I resign: after three years of 'we're a family here,' I have finally been disowned."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The gate allows 1 to 140 characters; this line is 93. Fail loudly
    # rather than writing an entry the gate would refuse.
    if not 1 <= len(LINE) <= 140 or LINE != LINE.strip() or "\n" in LINE:
        raise SystemExit("entry line does not satisfy the 1-140 char single-line gate")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE + "\n")


if __name__ == "__main__":
    main()
