# Official G1 Box Baseline Run Log

## 2026-07-12

### Scope

- Upstream SUMO source copied to `third_party/sumo` from the local official Windows source tree with `.git` excluded.
- No `sudo` was used.
- No SUMO source, cost, object parameter, or low-level policy was modified.
- Baseline configuration: task `g1_box`, optimizer `cem`, one episode, default runner options.

### Setup and build

The expected files and directories were present after the copy, including `pyproject.toml`, `pixi.lock`, `g1_extensions`, `sumo/run_mpc`, the G1 box task, and its XML model.

`pixi` was installed at `/home/xuzhe/.pixi/bin/pixi` but was not on the Codex shell `PATH`, so commands used that absolute path. `pixi install` completed successfully. `pixi run build` also completed successfully, building both the G1 extension and the Judo MuJoCo rollout extension. Pixi emitted a non-fatal warning that the existing lock file uses format v6; the lock file was not changed.

The runner entry-point check succeeded:

```text
pixi run python -m sumo.run_mpc --help
```

### Baseline command

```text
pixi run python -m sumo.run_mpc --init-task=g1_box --init-optimizer=cem --num-episodes=1
```

The run downloaded missing mesh assets, started the Viser server at `http://localhost:8080`, and initialized episode 1. It then failed at progress `0/2001` during the first controller action update.

### Result

Status: **failed before completing an episode**.

The final exception was:

```text
File "judo/utils/mj_rollout_backend.py", line 77, in rollout
    assert controls.shape[-1] == nu
AssertionError
```

Failure classification: simulation/control-interface dimension mismatch between the controls passed to the Judo MuJoCo rollout backend and the model actuator dimension (`nu`). This was not a `sudo`, source-copy, dependency-installation, build, or visualization-startup failure.

Because the official baseline did not complete, no result artifact search was treated as evidence of a successful run. No source-level fix or configuration change was attempted.

### Correction attempt 1: select the registered rollout backend

Further diagnosis showed the following dimensions and registration metadata:

```text
registered_backend= mujoco_g1
task_nu= 3
model_nu= 29
mapped_shape= (2, 4, 17)
```

The G1 task correctly maps its compact 3-dimensional MPC controls to the 17-dimensional command consumed by the G1 rollout extension. However, `run_mpc.py` constructed Judo's `Controller` without passing the task's registered rollout backend name. Judo therefore selected its default plain `mujoco` backend, which requires raw controls matching the model's 29 actuators and produced the observed assertion.

The runner was minimally corrected to pass `task_dict[config.init_task].rollout_backend` when constructing the controller. For `g1_box`, this selects the already-registered `G1RolloutBackend`. No task cost, object parameter, model XML, policy, or training behavior was changed.

The next run passed the original control-dimension assertion but stopped while constructing the selected G1 backend:

```text
AttributeError: module 'g1_extensions' has no attribute 'G1Rollout'
```

### Correction attempt 2: load the native module under editable installation

Inspection showed that the compiled module existed and exported the required API:

```text
g1_extensions/_g1_extensions.cpython-313-x86_64-linux-gnu.so
native_attrs= G1Rollout, rollout, shutdown_thread_pool, sim, sim_g1
```

The editable scikit-build loader registered only `g1_extensions._g1_extensions` and synthesized `g1_extensions` as an empty namespace package. Consequently, the repository's `g1_extensions/__init__.py` was not executed, so neither its top-level native exports nor `G1_EXTENSIONS_POLICY_DIR` initialization were available.

The existing `require_g1_extensions()` loader was made compatible with this editable-install layout: if the top-level package lacks `G1Rollout`, it sets the same repository-local policy directory used by the package initializer and imports `g1_extensions._g1_extensions` directly. The compiled extension and existing official ONNX policy remain unchanged.

### Successful rerun

The unchanged baseline command completed successfully after the two interface/loading corrections:

```text
============================================================
Task: g1_box  Optimizer: cem
Episodes: 1  Length: 10.0s
Avg Reward: -7504.75  Success: 1/1  Failure: 0/1
============================================================
Results saved to: run_mpc/results/g1_box/trajectories.h5
```

The process exited with code 0 after completing all `2001/2001` simulation steps. The generated HDF5 file contains the expected run metadata and episode result:

```text
task=g1_box
optimizer=cem
num_episodes=1
episode_length_s=10.0
sim_dt=0.005
episode_0.success=True
episode_0.failure=False
episode_0.length=10.0
```

Recorded dataset shapes:

```text
qpos_traj       (501, 43)
rewards         (201,)
rollout_rewards (201, 16)
rollout_states  (201, 16, 501, 84)
time_traj       (501,)
```

Result artifact: `third_party/sumo/run_mpc/results/g1_box/trajectories.h5`.

### Packaging follow-up

Python compilation succeeded. The initial full `pytest -q` run reached one failure after 29 passes:

```text
FAILED tests/test_imports.py::test_g1_extensions_import
ImportError: cannot import name 'G1Rollout' from 'g1_extensions' (unknown location)
```

This directly tested the public import rather than SUMO's compatible loader. After the failure, the suite remained alive in native threads and was interrupted after 233.49 seconds to obtain its summary (`1 failed, 29 passed`).

The packaging root cause was that `g1_extensions/pyproject.toml` declares `wheel.packages = ["g1_extensions"]`, which expects the Python package initializer at `g1_extensions/g1_extensions/__init__.py` relative to that subproject. The existing initializer was one directory too high, so scikit-build's editable loader recorded no Python source modules. A standard package initializer was added at the declared location. It re-exports the same compiled native API and points `G1_EXTENSIONS_POLICY_DIR` to the unchanged existing policy directory.

`pixi install` alone did not refresh the already-installed editable metadata. A direct `uv pip --reinstall` attempt outside Pixi activation failed because CMake could not locate Eigen3. Running the reinstall inside Pixi activation succeeded, but the next `pixi run` synchronized the environment back to Pixi's prior package state. The managed fix was therefore:

```text
pixi reinstall g1-extensions
pixi run build
```

The package-specific Pixi reinstall refreshed the editable source mapping. Its isolated build temporarily linked the native module against an unavailable MuJoCo 3.10 library; the official `pixi run build` then correctly rebuilt and linked it against the environment's `libmujoco.so.3.6.0`. Public import verification and the previously failing test then passed:

```text
module_file=.../g1_extensions/g1_extensions/__init__.py
policy_dir=.../g1_extensions/policy
tests/test_imports.py::test_g1_extensions_import: 1 passed
```

### Final end-to-end verification

After all packaging and native-build corrections, the exact requested baseline command was run again without additional options. It completed all `2001/2001` steps and exited with code 0:

```text
Task: g1_box  Optimizer: cem
Episodes: 1  Length: 10.0s
Avg Reward: -7504.08  Success: 1/1  Failure: 0/1
Results saved to: run_mpc/results/g1_box/trajectories.h5
```

This final run overwrote the earlier HDF5 at the same expected result path. No cost, object parameter, XML model, low-level policy, or training procedure was changed during correction.
