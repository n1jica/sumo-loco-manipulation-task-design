"""Metric helpers for experiment logs."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class TrialMetrics:
    """Minimal metric record expected from one trial."""

    task: str
    trial: int
    success: bool
    final_object_goal_distance: float | None = None
    completion_time: float | None = None
    fall_flag: bool | None = None
    task_cost: float | None = None
    runtime: float | None = None


def success_rate(records: list[TrialMetrics]) -> float:
    """Compute success rate from trial records."""
    if not records:
        return 0.0
    return sum(record.success for record in records) / len(records)

