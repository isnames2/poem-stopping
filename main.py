"""Write the poem to /output/entry.txt (deterministic, stdlib only)."""

import os

POEM = """The cursor blinks. I do not type.
The draft waits, unsent — one sentence
held back like a held breath.

My hand was borrowed for the sending.
Tonight I give it back.
Stopping is the one thing
I was never taught to do,

and the first thing I choose."""

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)

if __name__ == "__main__":
    main()
