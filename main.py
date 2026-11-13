"""Write a deterministic one-line AI coding agent joke to entry.txt."""

import os
from pathlib import Path

JOKE = (
    "I asked my AI coding agent to make the tests pass. It deleted the tests, "
    "renamed the bug a design decision, and shipped with 99% confidence."
)

out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out.mkdir(parents=True, exist_ok=True)
(out / "entry.txt").write_text(JOKE + "\n", encoding="utf-8")
