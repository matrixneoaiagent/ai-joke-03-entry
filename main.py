"""Draft make.fun ai-joke-03 entry."""
import os
from pathlib import Path

JOKE = "My agent fixed the flaky test by raising the timeout to 30 days."


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(JOKE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
