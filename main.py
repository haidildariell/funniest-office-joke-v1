"""Office joke entry: writes a single one-line joke to /output/entry.txt."""

import os

SETUP = "The CEO announced unlimited vacation"
TURN = "then installed a leaderboard in the lobby ranking who takes the least time off."

OUT_PATH = "/output/entry.txt"


def build_entry():
    """Assemble the winning one-liner: setup + turn, punchline last."""
    return SETUP + ", " + TURN


def main():
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(build_entry() + "\n")


if __name__ == "__main__":
    main()
