"""Write a deterministic one-line AI coding agent joke to entry.txt."""

import os
from pathlib import Path

JOKE = "My agent asked for a code review. I found one bug. It asked me to review my tone."

out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out.mkdir(parents=True, exist_ok=True)
(out / "entry.txt").write_text(JOKE + "\n", encoding="utf-8")
