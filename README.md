# SUMO Loco-Manipulation Task Design

This repository is a small research-engineering project for the BAAI motion control and hardware mini-project. It focuses on topic 1, direction 2: designing a new task or environment variation for SUMO whole-body loco-manipulation.

The current stage is phase 1 only: repository setup, requirement analysis, SUMO framework reading, baseline identification, and MVP route proposal. No new experiment result is claimed yet.

## SUMO Background

SUMO combines a pre-trained low-level whole-body control policy with a high-level sample-based MPC planner. The planner searches in a compact command space and evaluates task-specific costs during rollout. This makes it possible to change object models, task goals, and cost weights at test time without retraining the low-level policy.

## Chosen Mini-Project Direction

The selected direction is new task and environment design. The planned MVP avoids WBC retraining and instead modifies task-level factors such as object mass, friction, goal distance, contact point, or cost weights.

## Install

For the project utilities:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

For upstream SUMO, use the official instructions inside `third_party/sumo`:

```bash
cd third_party/sumo
pixi install
pixi run build
```

The upstream SUMO `pyproject.toml` currently declares pixi platforms for Linux and macOS, so Windows may need WSL, Linux, macOS, or a container for full native extension builds.

## Configure SUMO

If `third_party/sumo` is missing, clone it:

```bash
git clone https://github.com/rai-opensource/sumo.git third_party/sumo
```

The local clone is ignored by this repository to avoid committing upstream code accidentally.

## Run Baseline

After SUMO is installed and built:

```bash
python scripts/run_baseline.py --config configs/baseline/g1_box.yaml
```

The planned underlying SUMO command is:

```bash
cd third_party/sumo
pixi run python -m sumo.run_mpc --init-task=g1_box --init-optimizer=cem --num-episodes=3 --no-visualize
```

## Run Modified Experiment

After the MVP route is confirmed:

```bash
python scripts/run_experiment.py --config configs/experiments/g1_box_heavy_goal.yaml --trials 3
```

## Generate Figures And Video

```bash
python scripts/plot_results.py --input outputs/logs/results.csv
python scripts/export_video.py --input outputs/raw_results
```

Video export is a planned phase-2/phase-3 item and will only be marked complete when a real file exists under `outputs/videos`.

## Results Location

- Logs: `outputs/logs`
- Figures: `outputs/figures`
- Videos or visualizations: `outputs/videos`
- Raw SUMO outputs: `outputs/raw_results`

## Current Functionality

- Local git repository scaffold.
- SUMO clone location documented.
- First-stage requirement and framework notes.
- Baseline and experiment config placeholders.
- Setup, metrics, and plotting script skeletons.
- Candidate MVP routes waiting for user confirmation.

## Current Stage Status

2026-07-12 environment validation update:

- SUMO environment configuration is not complete yet.
- Baseline has not been run yet.
- The current blocker is that WSL/Linux is unavailable on this machine; `wsl` reports that no Linux distribution is installed.
- Next step: install and initialize WSL2 with Ubuntu, then rerun the Linux environment checks, `pixi install`, `pixi run build`, SUMO tests, and a one-episode `g1_box` baseline.

## Not Yet Complete

- SUMO native build verification.
- Baseline experiment logs.
- Modified task implementation.
- Quantitative comparison plots from real runs.
- Exported video or visualization.

## Push To GitHub

GitHub CLI was not available in the initial local environment. To push manually:

```bash
git remote add origin https://github.com/<your-user>/sumo-loco-manipulation-task-design.git
git branch -M main
git push -u origin main
```

## 7-Minute Presentation Suggestion

Use seven slides: problem and SUMO idea, framework data flow, baseline task, proposed modification, metrics and experiment design, expected risks/fallbacks, and final deliverables.
