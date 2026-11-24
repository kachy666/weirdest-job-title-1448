#!/usr/bin/env python3
"""Weirdest Job Title: Blind Judge Showdown — round 1 entry.

Prints exactly one job title, 60 characters or fewer, and nothing else.
"""

TITLE = "Sommelier for Gas Station Slushies"


def main() -> None:
    assert "\n" not in TITLE, "title must be a single line"
    assert len(TITLE) <= 60, f"title is {len(TITLE)} chars, over the 60-char limit"
    print(TITLE)


if __name__ == "__main__":
    main()
