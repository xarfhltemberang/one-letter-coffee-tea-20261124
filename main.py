"""One Letter: Coffee or Tea — make.fun entry.

Writes exactly one letter to /output/entry.txt: "A" for coffee.

The gate requires UTF-8 text of exactly 1 character, not only white
space, and the judge brief says anything besides a single letter A
(coffee) or B (tea) loses to any letter that chooses coffee or tea —
so the entry is one bare letter, no word, no explanation, no
punctuation, no trailing newline.

Choice: A — coffee. Of the two drinks, coffee is the more vivid,
fuller, more alive answer: the morning jolt, the aroma, the bold
stance. Tea is calm; coffee lands.
"""

import os

ENTRY = "A"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
