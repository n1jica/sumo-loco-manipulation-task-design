# Environment Setup

## 2026-07-12 Environment Check Summary

Current execution location:

- Project repository: `C:\Users\xuzhe\Desktop\sumo\sumo-loco-manipulation-task-design`
- Git branch: `main`
- Remote: `https://github.com/n1jica/sumo-loco-manipulation-task-design.git`

This setup attempt stopped at the Linux / WSL2 environment check. The requested SUMO installation and baseline validation require a working Linux / WSL2 environment, but `wsl` currently reports that no Linux distribution is installed.

## Required Project Files

| Path | Exists | Notes |
| --- | --- | --- |
| `AGENTS.md` | yes | Existing project workflow file. |
| `README.md` | yes | Existing project overview. |
| `docs/environment_setup.md` | yes | Created in this step. |
| `docs/experiment_log.md` | yes | Existing log, appended in this step. |
| `third_party/` | yes | Existing third-party directory. |
| `scripts/setup_check.py` | yes | Existing setup check script. |

## Linux / WSL2 Availability

| Check | Result | Notes |
| --- | --- | --- |
| `wsl -l -v` | failed | Windows reported that Windows Subsystem for Linux has no installed distribution and suggested `wsl.exe --install`. |
| `wsl pwd` | failed | Same WSL unavailable message. |
| `wsl uname -a` | failed | Same WSL unavailable message. |

Because WSL is not currently available, the Linux-specific commands below were not executed:

```bash
uname -a
lsb_release -a || cat /etc/os-release
python3 --version
which python3
git --version
gcc --version
g++ --version
cmake --version
ninja --version || true
make --version
cat /proc/version
nvidia-smi || true
```

## Tool Table

| Tool | Exists | Version | Meets Need | Notes |
| --- | --- | --- | --- | --- |
| Linux / WSL2 shell | no | not available | no | Required before SUMO pixi install/build can be validated as requested. |
| `python3` in Linux | unknown | not checked | unknown | Blocked because WSL/Linux is unavailable. |
| `git` in Linux | unknown | not checked | unknown | Blocked because WSL/Linux is unavailable. |
| `gcc` in Linux | unknown | not checked | unknown | Blocked because WSL/Linux is unavailable. |
| `g++` in Linux | unknown | not checked | unknown | Blocked because WSL/Linux is unavailable. |
| `cmake` in Linux | unknown | not checked | unknown | Blocked because WSL/Linux is unavailable. |
| `ninja` in Linux | unknown | not checked | unknown | Blocked because WSL/Linux is unavailable. |
| `make` in Linux | unknown | not checked | unknown | Blocked because WSL/Linux is unavailable. |
| NVIDIA GPU in Linux | unknown | not checked | optional | Blocked because WSL/Linux is unavailable. |
| `pixi` in Linux | unknown | not checked | unknown | Pixi installation was not attempted because Linux/WSL is unavailable. |

## SUMO Repository Status

`third_party/sumo` already exists from the previous analysis stage. The earlier recorded upstream commit was:

```text
4cea4e4e229ac075219ba3a3919c8e6e5f84f228
```

The current stage did not run Linux-side `git status`, `git log -1 --oneline`, or `ls` inside SUMO because WSL/Linux is unavailable.

## Pixi Status

Pixi was not checked or installed in Linux because WSL/Linux is unavailable.

## SUMO Install And Build Status

Not attempted. Required prerequisite failed: no working Linux / WSL2 environment.

## SUMO Pytest Status

Not attempted. Required prerequisite failed: no working Linux / WSL2 environment and no completed SUMO build.

## Baseline Run Status

No baseline episode was run in this step.

Planned first baseline command once Linux/WSL2 is available and SUMO builds successfully:

```bash
cd third_party/sumo
pixi run python -m sumo.run_mpc --init-task=g1_box --init-optimizer=cem --num-episodes=1
```

Fallback commands after confirming available task names:

```bash
pixi run python -m sumo.run_mpc --init-task=g1_door --init-optimizer=cem --num-episodes=1
pixi run python -m sumo.run_mpc --init-task=spot_box_push --init-optimizer=cem --num-episodes=1
```

## GUI / Visualization Status

Not attempted. Headless baseline must run first.

## Current Conclusion

The current machine state is not yet ready for the requested SUMO environment validation because Linux / WSL2 is unavailable. The next required action is to install and initialize WSL2 with an Ubuntu distribution, then rerun the environment checks from this document.

