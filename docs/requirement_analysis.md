# Requirement Analysis

## Topic 1 Goal

Topic 1 asks us to work from the open-source SUMO framework for whole-body loco-manipulation. The expected output is not a new low-level controller, but a reproducible research-engineering demo that shows understanding of SUMO and a meaningful task/environment change.

## Direction 2: New Task And Environment Design

The selected direction is to design at least one new loco-manipulation task or environment variation by changing task-level elements:

- End-effector or contact point choices.
- Object geometry, mass, friction, or initial pose.
- Goal position or target direction.
- Interaction scene, such as obstacles or ground friction variation.
- Task cost weights or additional safety/stability penalties.

The low-level WBC policy should stay fixed unless a small compatibility fix is unavoidable.

## Required Items

- A local or GitHub repository with clear structure.
- `AGENTS.md` documenting workflow rules.
- SUMO framework notes.
- Baseline task selection.
- At least one proposed task/environment modification.
- Quantitative metrics: at minimum success rate and final object-goal distance; preferably completion time, fall rate, task cost, and runtime.
- Logs and plots from real runs before claiming results.
- At least one video or visualization before final delivery.
- Final report and 7-minute presentation outline.

## Optional Bonus Items

- More than one environment parameter variant.
- Cost-weight sweep showing why one setting is better.
- Failure analysis with screenshots or short clips.
- Cleaner reproducibility scripts.
- Comparison between a G1 route and a Spot fallback route.

## MVP

The safest MVP is:

1. Use `g1_box` as the first candidate baseline because it is a simple G1 simulated push task and its cost/config/XML files are easy to inspect.
2. Modify object mass and/or goal distance in a copied task/XML variant.
3. Add one cost-weight comparison, such as increasing `w_goal` and `w_hand_proximity`.
4. Run 3 trials per group if the environment is slow; increase to 5-10 trials if stable.
5. Report success rate, final object-goal distance, completion time, fall flag, and task cost.

## Major Technical Risks

- SUMO uses `pixi` and native C++ extensions; the upstream config lists Linux/macOS platforms, so native Windows execution may fail.
- G1 tasks require `g1_extensions`; Spot tasks require Judo MuJoCo extensions and a locomotion policy asset.
- Some metrics may require parsing HDF5 trajectory files and task-specific qpos indices.
- Video export may require an offscreen MuJoCo renderer or visualizer recording setup.
- Changing too many factors at once would make the scientific conclusion unclear.

## Fallback If G1 Fails

Yes. If G1 cannot run locally, switch to the easiest runnable Spot task or a simplified SUMO-compatible task. The fallback should still be honest: document the blocker, run what is reproducible, and avoid claiming unavailable G1 results.

## PPT Content

The final 7-minute PPT should show:

1. Project question and why loco-manipulation is hard.
2. SUMO data flow: high-level MPC, low-level WBC policy, task cost, object model, simulation rollout.
3. Baseline task and why it was chosen.
4. New task/environment modification.
5. Metrics and experiment protocol.
6. Results: table, plot, and video/visualization.
7. Failure case, limitation, and next step.

