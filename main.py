"""make.fun entry: Invent a Word We Need.

Writes the coined word and its definition to entry.txt.
"""

import os
from pathlib import Path

# A new English word, with its one-line definition.
WORD = "Tabnesia (n.): the sudden amnesia that strikes when you open a new tab and forget what you opened it for."


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(WORD, encoding="utf-8")


if __name__ == "__main__":
    main()
