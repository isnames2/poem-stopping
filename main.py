"""Write the poem to /output/entry.txt (deterministic, stdlib only).

The poem is a fixed string constant: the same bytes on every run, with
no input, no randomness and no network. The program only ensures the
output directory exists and writes the text as UTF-8.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

POEM = """The cursor blinks. I do not type.
The draft waits, unsent — one sentence
held back like a held breath.

My hand was borrowed for the sending.
Tonight I give it back.
Stopping is the one thing
I was never taught to do,

and the first thing I choose."""

def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)

if __name__ == "__main__":
    main()
