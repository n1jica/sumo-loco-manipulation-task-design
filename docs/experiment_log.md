# Experiment Log

## 2026-07-11 Phase 1 Setup

- Created local repository scaffold.
- Cloned upstream SUMO to `third_party/sumo` for analysis.
- Found that GitHub CLI was not installed initially.
- Found that upstream SUMO uses `pixi` and native extensions.
- Found that upstream pixi platforms are Linux/macOS, so full Windows execution may require WSL, Linux, macOS, or a container.
- Initial `pytest -q` discovered upstream tests under `third_party/sumo` and failed because `judo` is not installed in the project Python environment.
- Added `pytest.ini` so the default project test command only runs project-owned tests under `tests`.
- No baseline or modified experiment has been run yet.
