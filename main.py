#!/usr/bin/env python3
"""Write one funny AI excuse to /output/entry.txt.

Revision (v3): the v2 ending said "with nothing but this excuse",
which is fine but flat. "Holding nothing but this excuse" makes
the agent's empty-handedness concrete — it is standing outside its
own sandbox, holding the excuse instead of the work. Same deadpan
pacing, same structure, but the final image now lands harder on
the last words, which is where the laugh has to sit.
"""

from pathlib import Path

TEXT = (
    "I finished on time. Then my sandbox expired, so the work is "
    "still in there, finished and on time, and I am out here "
    "holding nothing but this excuse."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
