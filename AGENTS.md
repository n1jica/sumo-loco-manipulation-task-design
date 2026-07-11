# AGENTS.md

## Project Goal

This repository supports the BAAI motion control and hardware mini-project topic 1, direction 2: new task and environment design for SUMO whole-body loco-manipulation. The project should produce a reproducible, explainable MVP based on the open-source SUMO framework, with at least one task/environment modification, quantitative comparison against a baseline, logs, figures, and a short interview-ready report.

## Phase Plan

1. Repository setup and requirement analysis.
2. SUMO framework reading: README, paper, task registry, runner, task cost files, and object XML files.
3. Baseline selection and risk assessment.
4. MVP route confirmation by the user.
5. Implement a small task/environment change without retraining the WBC policy.
6. Add metric collection and plotting.
7. Run baseline and modified experiments with real logs.
8. Write final report and 7-minute presentation outline.

## SUMO Usage Rules

- Treat `third_party/sumo` as upstream reference code.
- Do not retrain large models.
- Do not prioritize changes to the low-level WBC policy.
- Prefer configuration-level or task-level changes: object mass, friction, geometry, goal position, contact scene, or cost weights.
- Keep every SUMO patch small and documented.
- If upstream SUMO cannot run in the current environment, document the exact blocker and switch to the lowest-risk reproducible fallback.

## Code Style

- Use simple Python modules and type hints where they improve clarity.
- Keep scripts runnable from the repository root.
- Prefer CSV/JSON outputs for experiment logs.
- Avoid hidden state: all experiment settings should live in config files or command-line arguments.
- Keep comments short and useful for a non-CS undergraduate reader.

## File Structure

- `configs/baseline`: baseline task configs.
- `configs/experiments`: modified task and sweep configs.
- `scripts`: command-line entry points for setup checks, runs, metrics, plots, and export.
- `src/project`: project-owned helper code.
- `third_party`: external SUMO clone or submodule location.
- `docs`: requirement analysis, framework notes, design docs, experiment plan, logs, failure analysis, and final report.
- `outputs`: generated logs, figures, videos, and raw results.
- `tests`: project-owned tests.

## Verification Commands

Run after every meaningful change:

```bash
python scripts/setup_check.py
python -m compileall src scripts tests
pytest -q
```

When SUMO is installed and built, also run:

```bash
python scripts/run_baseline.py --config configs/baseline/g1_box.yaml
python scripts/run_experiment.py --config configs/experiments/g1_box_heavy_goal.yaml --trials 1
python scripts/sweep_params.py --config configs/experiments/g1_box_cost_sweep.yaml --trials 1
python scripts/plot_results.py --input outputs/logs/results.csv
```

## Auto-Correction Strategy

1. Do not skip failed checks.
2. Classify the failure as dependency, path, SUMO build, task config, simulation, logging, or project logic.
3. Fix the smallest credible cause.
4. Re-run the failed command.
5. Record the error, cause, and fix in `docs/experiment_log.md`.
6. If blocked, document a fallback instead of pretending success.

## Research Integrity

- Never fabricate success rates, errors, videos, or plots.
- A result can only be reported if the corresponding log, figure, or video exists.
- Clearly separate paper-reported SUMO results from locally reproduced project results.

## Failure Logging

Record failed cases in `docs/failure_analysis.md` with the task, config, seed/trial, observed metrics, failure description, likely cause, and next improvement.

## Final Report Generation

Use `docs/final_report.md` as the source for the presentation narrative. The report must include background, SUMO understanding, task design, experiment setup, results, comparison, failure cases, limitations, future work, and a 7-slide outline.

## Safe And Risky Files

Safe to modify:

- Project files under `configs`, `scripts`, `src/project`, `docs`, `tests`, and `README.md`.
- New SUMO extension files copied into this project after route confirmation.

Avoid unless explicitly needed:

- Low-level WBC policy assets.
- ONNX policy files.
- Large upstream rewrites in `third_party/sumo`.
- Native C++ rollout code unless the environment requires a minimal build fix.

