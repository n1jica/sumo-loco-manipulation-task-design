"""General project utilities."""

from pathlib import Path


def repo_root() -> Path:
    """Return the project repository root."""
    return Path(__file__).resolve().parents[2]

