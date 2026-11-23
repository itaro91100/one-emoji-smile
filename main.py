"""One Emoji, One Smile — entry for make.fun.

The whole entry is a single warm emoji. This program keeps that emoji
as one constant, checks that it really is exactly one emoji character,
and writes it — alone, with no words around it — to the output file
the grader reads.
"""

import os
import sys
import unicodedata

# The entry: a smiling face with hearts. Warmth, affection and a smile
# in one character — nothing else is sent.
CHOSEN_EMOJI = "\U0001F970"


def is_single_emoji(text):
    """True only when `text` is exactly one emoji character.

    A single code point in the Symbol, other category, living above
    the basic punctuation range, with no whitespace and no joiner:
    that is one whole emoji and nothing else.
    """
    if len(text) != 1:
        return False
    if text.isspace():
        return False
    if unicodedata.category(text) != "So":
        return False
    return ord(text) >= 0x1F000


def main():
    if not is_single_emoji(CHOSEN_EMOJI):
        print("entry is not exactly one emoji", file=sys.stderr)
        return 1
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(CHOSEN_EMOJI)
    sys.stdout.write(CHOSEN_EMOJI)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
