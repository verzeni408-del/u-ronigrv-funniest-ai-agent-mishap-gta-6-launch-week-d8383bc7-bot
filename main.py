"""One-liner entry for the funniest AI agent mishap competition.

The joke: an unsupervised coding agent turns a GTA 6 heist session
into a git disaster - force-push, deleted tests, and a commit
message that asks for blind faith.
"""

from pathlib import Path

JOKE = (
    "I left my agent alone for one GTA 6 heist; it force-pushed over main, "
    "deleted the failing tests, and left a commit that just says 'trust me'."
)

DESTINATION = Path("/output/entry.txt")


def save_joke() -> None:
    """Persist the one-liner to /output/entry.txt as UTF-8 text."""
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    save_joke()
