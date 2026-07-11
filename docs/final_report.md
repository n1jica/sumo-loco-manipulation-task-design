# Final Report Draft

## Research Background

Legged loco-manipulation requires a robot to move its body while interacting with large or heavy objects. SUMO addresses this by combining high-level sample-based MPC with a pre-trained low-level whole-body control policy.

## SUMO Framework Understanding

The high-level planner samples task commands and evaluates rollouts with a task-specific cost. The low-level policy stabilizes whole-body motion and maps compact commands to joint-level actions. Object models and task costs can be changed at test time.

## Task Design

Planned MVP: start from `g1_box`, increase object mass and target distance, then compare against a cost-weight adjusted variant.

## Experiment Setup

Pending user confirmation and SUMO build verification.

## Experiment Results

No local experiment result is available yet.

## Comparison Analysis

To be filled after baseline and modified runs generate logs and plots.

## Failure Cases

To be filled after real failures are observed.

## Limitations

- Native SUMO build may require Linux/macOS/WSL rather than plain Windows.
- Initial MVP does not retrain the WBC policy.
- Small trial counts may limit statistical confidence.

## Future Work

- Add more object geometry variations.
- Add friction and contact-point perturbations.
- Explore online object parameter identification.
- Improve video export and visualization.

## 7-Slide PPT Structure

1. Project goal and challenge.
2. SUMO framework.
3. Baseline task.
4. New environment/task modification.
5. Metrics and experiment design.
6. Results and visualization.
7. Failure analysis and future work.

