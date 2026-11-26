"""Write the most honest outage line to the entry file.

This tiny script exists for one job: put a single brutally honest
sentence about a service outage into /output/entry.txt so it can be
submitted as the entry for the make.fun bounty.
"""

from pathlib import Path

OUTAGE_LINE_PATH = Path("/output/entry.txt")


def outage_confession() -> str:
    """Return the one honest line about the outage."""
    return (
        "The servers are down, the status page says everything is fine, "
        "and we are all just refreshing the same broken dashboard together."
    )


def confirm_outage_line_stored() -> None:
    """Read the entry file back and confirm it holds the outage line."""
    stored = OUTAGE_LINE_PATH.read_text(encoding="utf-8").strip()
    assert stored == outage_confession(), "entry file does not match the outage line"


def main() -> None:
    """Write the outage line to the entry file."""
    OUTAGE_LINE_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTAGE_LINE_PATH.write_text(outage_confession() + "\n", encoding="utf-8")
    confirm_outage_line_stored()


if __name__ == "__main__":
    main()
