"""Modified experiment runner placeholder."""

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
    print("Experiment route is still pending user confirmation.")
    print(f"Loaded candidate: {config.get('name', args.config)}")
    print(f"Requested trials: {args.trials}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
