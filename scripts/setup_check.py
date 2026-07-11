"""Check whether the first-stage project scaffold is present."""

from pathlib import Path


REQUIRED_PATHS = [
    "AGENTS.md",
    "README.md",
    "configs/baseline/g1_box.yaml",
    "configs/experiments/g1_box_heavy_goal.yaml",
    "docs/requirement_analysis.md",
    "docs/sumo_framework_notes.md",
    "docs/design_doc.md",
    "src/project/metrics.py",
]


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    missing = [path for path in REQUIRED_PATHS if not (root / path).exists()]
    if missing:
        print("Missing required paths:")
        for path in missing:
            print(f"- {path}")
        return 1
    sumo_path = root / "third_party" / "sumo"
    print("Project scaffold OK.")
    print(f"SUMO clone present: {sumo_path.exists()} ({sumo_path})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

