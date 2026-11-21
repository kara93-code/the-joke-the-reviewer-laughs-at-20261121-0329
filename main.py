#!/usr/bin/env python3
"""the-joke-the-reviewer-laughs-at-20261121-0329.

Writes one original one-line joke about working beside an AI coding
agent to /output/entry.txt. Deterministic: the same bytes on every run.
No network, no randomness, no input files, standard library only.
"""

from pathlib import Path

JOKE_LINE = "My agent's PR said 'minor cleanup' \u2014 the diff touched 214 files and my faith in code review."


def build_joke() -> str:
    """Return the entry text: a single line, no trailing newline."""
    return JOKE_LINE


def write_entry(destination: Path, text: str) -> None:
    """Write text as UTF-8, creating the output directory if needed.

    The file is left world-readable (mode 0644) so the grader's
    scorer can read it.
    """
    import os

    destination.parent.mkdir(parents=True, exist_ok=True)
    with open(destination, "w", encoding="utf-8") as handle:
        handle.write(text)
    os.chmod(destination, 0o644)


def main() -> None:
    import os

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    write_entry(out_dir / "entry.txt", build_joke())


if __name__ == "__main__":
    main()
