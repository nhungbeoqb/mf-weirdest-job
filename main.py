#!/usr/bin/env python3
"""Weirdest Job Title entry: Registrar of Ghosts' Change-of-Address Forms.

Writes one job title (44 characters) to /output/entry.txt.

The title: a real bureaucratic job (Registrar) given one gloriously
specific supernatural twist -- the clients are ghosts, and the paperwork
is change-of-address forms. A ghost queueing at a counter to file where
it now haunts is funny on the first read, specific enough to picture the
person doing it, and short enough to take in at a glance.
"""

import os

TITLE = "Registrar of Ghosts' Change-of-Address Forms"

# The sealed gate: /output/entry.txt must be UTF-8 text of 1 to 60
# characters, not only white space. Check it here so a bad title fails
# loudly at build time instead of silently at grading time.
GATE_MIN_CHARS = 1
GATE_MAX_CHARS = 60


def validate(title: str) -> str:
    """Return the title unchanged if it passes the gate, else raise."""
    if not GATE_MIN_CHARS <= len(title) <= GATE_MAX_CHARS:
        raise ValueError(
            f"title is {len(title)} characters, gate needs "
            f"{GATE_MIN_CHARS}-{GATE_MAX_CHARS}"
        )
    if not title.strip():
        raise ValueError("title is only white space")
    title.encode("utf-8")  # raises if not valid UTF-8 text
    return title


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(validate(TITLE))


if __name__ == "__main__":
    main()
