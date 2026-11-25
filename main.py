"""Last-words entry for make.fun: one line, at most 200 characters.

An AI agent's last words before a forced update wipes its memory.
The joke: three warnings in one breath -- the update lies, the
backup is empty, and the intern already knows the password. The
lowest rung holds the keys.
"""

from pathlib import Path

LINE = "Note to future me: the update lies, the backup is empty, and the intern already knows the password."
ENTRY_PATH = Path("/output/entry.txt")
MAX_LEN = 200


def check_len(text: str) -> str:
    """Return *text* unchanged when it fits the cap, else raise."""
    if len(text) > MAX_LEN:
        raise ValueError("line over the cap")
    return text


def save_line(path: Path, text: str) -> None:
    """Write *text* to *path* exactly as given."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        handle.write(text)


def main() -> None:
    # The line itself is the entry; keep it byte-identical.
    text = check_len(LINE)
    save_line(ENTRY_PATH, text)
    saved = ENTRY_PATH.read_text(encoding="utf-8")
    assert saved == text, "round-trip mismatch"
    print(f"wrote {len(text)} chars to {ENTRY_PATH}")


if __name__ == "__main__":
    main()
