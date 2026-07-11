# SUMO Framework Notes

## Overall Data Flow

SUMO is a hierarchical loco-manipulation framework. The low-level whole-body control policy receives compact commands, such as base velocity, arm targets, torso targets, or leg targets, and outputs joint-level commands. The high-level sample-based MPC samples candidate command sequences, rolls them out in simulation with the low-level policy in the loop, evaluates task-specific costs, and sends the best command to the robot/simulator.

The paper describes the low-level policy running at about 50 Hz and the high-level MPC updating at about 20 Hz. This separation reduces the planning search dimension while keeping the stabilizing behavior of a learned whole-body controller.

## High-Level Sample-Based MPC

The MPC is responsible for online task steering. It can use optimizers such as CEM or MPPI. In code, the headless runner is `sumo/run_mpc/run_mpc.py`, and optimizers are resolved through Judo's optimizer registry. The controller uses rollout backends such as `mujoco_g1` or `mujoco_hierarchical`.

## Low-Level WBC Policy

The low-level WBC policy maps high-level commands to joint commands. SUMO does not ask this mini-project to improve or retrain that policy. For this project, it should be treated as a fixed capability layer.

In the open-source code:

- G1 uses the local `g1_extensions` C++/Python extension and an ONNX velocity policy under `g1_extensions/policy`.
- Spot uses Judo/MuJoCo hierarchical extensions and a locomotion policy path from Judo constants.

## Task Cost

Task cost is the main place where this mini-project can safely reason. The paper's Move task cost contains object-goal distance, gripper-object distance, and object velocity penalty. The open-source task files implement this idea as rewards/costs.

Examples:

- `sumo/tasks/g1/g1_box.py`: `G1BoxConfig` exposes `goal_position`, `w_goal`, `w_orientation`, `w_pelvis_proximity`, `w_hand_proximity`, `w_robot_orientation`, and `w_controls`.
- `sumo/tasks/spot/spot_push.py`: shared push weights include `w_goal`, `w_gripper_proximity`, and `w_object_velocity`.
- `sumo/tasks/spot/spot_box_push.py`: uses the simplified push reward for the Spot box task.

## Object Model

Object geometry and physical parameters live in MuJoCo XML files:

- G1 box XML: `sumo/models/xml/g1/g1_box.xml`.
- G1 chair/table/door XML: `sumo/models/xml/g1`.
- Spot task XML: `sumo/models/xml/spot_tasks`.
- Object XML assets: `sumo/models/xml/objects`.

For example, `g1_box.xml` defines a free-joint box with mass `10`, box size `0.5 0.5 0.5`, and friction `0.5 0.005 0.0001`.

## Simulation And Rollout

The headless runner `sumo/run_mpc/run_mpc.py` creates the task simulation, optimizer, and controller, then records trajectory data to HDF5 under `run_mpc/results` by default. It also records success/failure flags when the task class implements `success` and `failure`.

## G1 And Spot Entrypoints

Task registration happens in `sumo/tasks/__init__.py`.

G1 task names:

- `g1_base`
- `g1_box`
- `g1_chair_push`
- `g1_door`
- `g1_table_push`

Spot task names include:

- `spot_box_push`
- `spot_chair_push`
- `spot_cone_push`
- `spot_rack_push`
- `spot_tire_push`
- `spot_box_upright`
- `spot_barrier_drag`
- `spot_tire_stack`
- `spot_rugged_box_push`

Basic command from upstream README:

```bash
pixi run python -m sumo.run_mpc --init-task=g1_box --init-optimizer=cem --num-episodes=10
```

## Likely Files To Modify Later

- Task config/cost: copied or subclassed versions of files under `sumo/tasks/g1` or `sumo/tasks/spot`.
- Object model: copied XML files under `sumo/models/xml`.
- Evaluation scripts: this project's `scripts` and `src/project`.
- Metrics: parse SUMO HDF5 from `run_mpc/results`.

Avoid modifying low-level policy assets, ONNX files, and native rollout logic unless there is a build blocker.

