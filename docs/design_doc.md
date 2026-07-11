# Design Doc

## Baseline Choice

Primary candidate baseline: `g1_box`.

Reason:

- It is one of the paper's G1 simulation tasks.
- The code is compact and readable.
- The object XML exposes mass, size, and friction clearly.
- The task config exposes useful cost weights.
- It avoids real robot deployment and avoids WBC retraining.

Fallback baseline: `spot_box_push` if the G1 native extension path fails and Spot dependencies are easier to build in the final environment.

## Planned Modification

Recommended route: G1 box push with object mass and goal distance perturbation, followed by a small cost-weight adjustment.

Baseline:

- `g1_box`
- Original box mass: `10`
- Original box size: `0.5 0.5 0.5`
- Original friction: `0.5 0.005 0.0001`
- Original major weights: `w_goal=50`, `w_hand_proximity=10`, `w_controls=3`

Modified task:

- Increase box mass, for example 10 kg to 15 kg.
- Increase target distance by about 30 percent.
- Compare original cost weights against a higher goal/hand-proximity setting.

## Hypothesis

Increasing mass and goal distance should make the task harder, increasing final object-goal error and reducing success rate. Increasing the goal and hand-proximity weights may recover part of the performance by pushing the MPC to prioritize object progress and contact maintenance.

## Metrics

- `success_rate`: ratio of trials satisfying task success condition.
- `final_object_goal_distance`: XY distance from final object position to goal.
- `completion_time`: first time success is reached, or episode time limit if not reached.
- `fall_rate` or `fall_flag`: robot fall condition.
- `task_cost`: final or accumulated reward/cost from SUMO.
- `runtime` or `planning_time`: wall-clock runtime if easy to collect.

## Visualization

Minimum acceptable visualization:

- One baseline trajectory plot and one modified-task trajectory plot, showing object position and goal.

Preferred:

- One short rendered video for baseline and one for modified task, exported from MuJoCo or captured from SUMO visualizer.

## Minimum Success Criteria

The MVP is successful when:

1. Baseline and modified configs are reproducible.
2. At least 3 trials per group are run.
3. Logs exist under `outputs/logs`.
4. At least one figure exists under `outputs/figures`.
5. At least one video or trajectory visualization exists under `outputs/videos`.
6. The report honestly explains any build or simulation limitations.

## Candidate Routes

### Route A: G1 Box Mass + Goal Distance

Risk: medium, because G1 native extensions must build.

Workload: low to medium.

Display value: high. The change is easy to explain and directly linked to physical control difficulty.

### Route B: G1 Box Cost Weight Sweep Only

Risk: lower after G1 runs, because it may avoid XML edits.

Workload: low.

Display value: medium. It demonstrates SUMO's test-time cost flexibility but is less visually distinct.

### Route C: Spot Box Push Friction/Mass Variant

Risk: medium to high, because Spot needs Judo MuJoCo hierarchical extensions and policy assets.

Workload: medium.

Display value: high if it runs, because Spot tasks are visually rich and close to the paper's real-world demonstrations.

## Recommendation

Start with Route A. If native G1 execution is blocked on Windows, document the blocker and choose either WSL/Linux execution or Route B/C depending on which SUMO backend can be built fastest.

