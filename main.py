"""One Word From Your Ex — make.fun one-word bounty entry.

Writes a single word to /output/entry.txt, byte-exact, no trailing
newline. Standard library only, fully deterministic.
"""

from pathlib import Path

WORD = "Almost"


def main() -> None:
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_bytes(WORD.encode("utf-8"))


if __name__ == "__main__":
    main()
