"""Writes the entry — one line, a single line of text no longer than
200 characters — to entry.txt in the output directory.

The line is a fixed constant in this file; nothing is read from the
environment apart from the output directory.
"""

import os

LINE = "Sorry I missed the deadline — I've been waiting three days for your approval, which I now realize never came, because I never asked for it."

MIN_CHARS = 1
MAX_CHARS = 200
OUTPUT_FILENAME = "entry.txt"
OUTPUT_DIR = "/output"


def main():
    text = LINE.strip()
    if "\n" in text or "\r" in text:
        raise ValueError("line must be a single line of text")
    if len(text) > MAX_CHARS:
        raise ValueError(f"line is {len(text)} chars (max {MAX_CHARS})")
    if len(text) < MIN_CHARS:
        raise ValueError(f"line is {len(text)} chars (min {MIN_CHARS})")
    if not text.strip():
        raise ValueError("line is empty")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", OUTPUT_DIR)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, OUTPUT_FILENAME)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    # The grader collects the output as a different user.
    os.chmod(path, 0o644)
    print(f"wrote {path} ({len(text)} chars)")


if __name__ == "__main__":
    main()
