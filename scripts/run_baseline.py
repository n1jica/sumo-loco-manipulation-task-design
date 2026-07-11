"""Baseline runner wrapper.

This wrapper documents the intended SUMO command and prevents accidental claims
before SUMO is built in the local environment.
"""

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
    args = parser.parse_args()
    config = load_yaml(args.config)
    root = Path(__file__).resolve().parents[1]
    sumo_dir = root / "third_party" / "sumo"
    task = config.get("sumo_task", "g1_box")
    optimizer = config.get("optimizer", "cem")
    trials = config.get("trials", 3)
    print("Baseline config loaded.")
    print(f"Task: {task}, optimizer: {optimizer}, trials: {trials}")
    print("Run this after SUMO is installed and native extensions are built:")
    print(f"cd {sumo_dir}")
    print(f"pixi run python -m sumo.run_mpc --init-task={task} --init-optimizer={optimizer} --num-episodes={trials} --no-visualize")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
