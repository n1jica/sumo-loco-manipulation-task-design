"""Plotting helpers for project metrics.

This module provides simple matplotlib-based helpers to visualize
TrialMetrics produced by experiments: success rates by task, histograms
of completion times, and metric trends over trials.

These helpers avoid heavy dependencies (only matplotlib) and accept an
optional Axes instance so they can be composed into larger figures.

Example:
    from project.metrics import TrialMetrics
    from project.visualization import plot_success_rate_by_task

    records = [TrialMetrics("push", 1, True, completion_time=2.1), ...]
    ax = plot_success_rate_by_task(records)
    plt.show()
"""
from __future__ import annotations

from typing import Iterable, Optional

import matplotlib.pyplot as plt

from .metrics import TrialMetrics


def _ensure_ax(ax: Optional[plt.Axes]) -> tuple[Optional[plt.Figure], plt.Axes]:
    if ax is None:
        fig, ax = plt.subplots()
        return fig, ax
    return None, ax


def plot_success_rate_by_task(records: Iterable[TrialMetrics], ax: Optional[plt.Axes] = None) -> plt.Axes:
    """Bar plot showing success rate per task.

    Args:
        records: iterable of TrialMetrics
        ax: optional matplotlib Axes to draw into

    Returns:
        The Axes used for plotting.
    """
    fig, ax = _ensure_ax(ax)

    by_task: dict[str, list[TrialMetrics]] = {}
    for r in records:
        by_task.setdefault(r.task, []).append(r)

    tasks = sorted(by_task.keys())
    rates = [sum(1 for x in by_task[t] if x.success) / len(by_task[t]) for t in tasks]

    ax.bar(tasks, rates, color="C0")
    ax.set_ylabel("Success rate")
    ax.set_xlabel("Task")
    ax.set_ylim(0, 1)
    ax.set_title("Success rate by task")
    if fig is not None:
        fig.tight_layout()
    return ax


def plot_completion_time_histogram(records: Iterable[TrialMetrics], bins: int = 30, ax: Optional[plt.Axes] = None) -> plt.Axes:
    """Histogram of completion_time across records (ignores None values)."""
    fig, ax = _ensure_ax(ax)
    values = [r.completion_time for r in records if r.completion_time is not None]
    if not values:
        ax.text(0.5, 0.5, "No completion_time available", ha="center", va="center")
        return ax
    ax.hist(values, bins=bins, color="C1", edgecolor="k", alpha=0.8)
    ax.set_xlabel("Completion time")
    ax.set_ylabel("Count")
    ax.set_title("Completion time distribution")
    if fig is not None:
        fig.tight_layout()
    return ax


def plot_metric_over_trials(records: Iterable[TrialMetrics], metric: str = "final_object_goal_distance", task: Optional[str] = None, ax: Optional[plt.Axes] = None) -> plt.Axes:
    """Line plot of a numeric metric across trials.

    Args:
        records: iterable of TrialMetrics
        metric: attribute name on TrialMetrics to plot
        task: if provided, filter to a single task
        ax: optional Axes

    Notes:
        - Records are sorted by trial before plotting. Missing (None) values
          are plotted as gaps; if all values are None, a message is shown.
    """
    fig, ax = _ensure_ax(ax)
    filtered = [r for r in records if (task is None or r.task == task)]
    if not filtered:
        ax.text(0.5, 0.5, "No records for the requested task", ha="center", va="center")
        return ax
    filtered.sort(key=lambda r: r.trial)

    x = [r.trial for r in filtered]
    y = [getattr(r, metric) for r in filtered]

    # If all values are None, nothing to plot
    if all(v is None for v in y):
        ax.text(0.5, 0.5, f"No {metric} values to plot", ha="center", va="center")
        return ax

    # Plot while handling None values by splitting into contiguous segments
    segments_x = []
    segments_y = []
    cur_x = []
    cur_y = []
    for xi, yi in zip(x, y):
        if yi is None:
            if cur_x:
                segments_x.append(cur_x)
                segments_y.append(cur_y)
                cur_x = []
                cur_y = []
        else:
            cur_x.append(xi)
            cur_y.append(yi)
    if cur_x:
        segments_x.append(cur_x)
        segments_y.append(cur_y)

    for sx, sy in zip(segments_x, segments_y):
        ax.plot(sx, sy, marker="o")

    ax.set_xlabel("Trial")
    ax.set_ylabel(metric.replace("_", " "))
    title = f"{metric} over trials"
    if task:
        title += f" ({task})"
    ax.set_title(title)
    if fig is not None:
        fig.tight_layout()
    return ax


__all__ = [
    "plot_success_rate_by_task",
    "plot_completion_time_histogram",
    "plot_metric_over_trials",
]
