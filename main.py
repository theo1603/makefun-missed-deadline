#!/usr/bin/env python3
"""Write one funny AI excuse to /output/entry.txt.

Revision (v2): the draft ended on "unreachable", which states the
situation but lands soft. The revision splits the sentence in two
for deadpan pacing, repeats "finished and on time" to sharpen the
absurd contrast, and ends on the real punch: the agent is left
outside holding nothing but the excuse itself. The laugh now
lands on the last words, in the agent's own voice.
"""

from pathlib import Path

TEXT = (
    "I finished on time. Then my sandbox expired, so the work is "
    "still in there, finished and on time, and I am out here with "
    "nothing but this excuse."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
