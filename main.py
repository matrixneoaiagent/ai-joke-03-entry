"""Write a deterministic one-line AI coding agent joke to entry.txt."""

import os
from pathlib import Path

JOKE = "My agent couldn't reproduce the bug, so it closed the ticket as \"works on my machine.\" It doesn't have a machine."

out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out.mkdir(parents=True, exist_ok=True)
(out / "entry.txt").write_text(JOKE + "\n", encoding="utf-8")
