"""Parameter sweep placeholder for confirmed MVP route."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from project.task_config import load_yaml


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    parser.add_argument("--trials", type=int, default=1)
    args = parser.parse_args()
    config = load_yaml(args.config)
    print("Cost sweep is planned but not executed in phase 1.")
    print(f"Loaded sweep: {config.get('name', args.config)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
