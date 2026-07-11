"""Video export placeholder."""

from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="outputs/raw_results")
    args = parser.parse_args()
    print(f"Video export awaits confirmed renderer and real trajectory data: {args.input}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

