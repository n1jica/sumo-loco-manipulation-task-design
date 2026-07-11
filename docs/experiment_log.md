# Experiment Log

## 2026-07-11 Phase 1 Setup

- Created local repository scaffold.
- Cloned upstream SUMO to `third_party/sumo` for analysis at commit `4cea4e4e229ac075219ba3a3919c8e6e5f84f228`.
- Found that GitHub CLI was not installed initially.
- Found that upstream SUMO uses `pixi` and native extensions.
- Found that upstream pixi platforms are Linux/macOS, so full Windows execution may require WSL, Linux, macOS, or a container.
- Initial `pytest -q` discovered upstream tests under `third_party/sumo` and failed because `judo` is not installed in the project Python environment.
- Added `pytest.ini` so the default project test command only runs project-owned tests under `tests`.
- No baseline or modified experiment has been run yet.

## 2026-07-12 00:10 环境配置记录

### 命令

```powershell
Get-Location
Get-ChildItem -Force
git status --short --branch
git remote -v
Test-Path AGENTS.md
Test-Path README.md
Test-Path docs\environment_setup.md
Test-Path docs\experiment_log.md
Test-Path third_party
Test-Path scripts\setup_check.py
wsl -l -v
wsl pwd
wsl uname -a
```

### 现象

当前目录确认为项目仓库：

```text
C:\Users\xuzhe\Desktop\sumo\sumo-loco-manipulation-task-design
```

仓库处于 `main` 分支并跟踪远程：

```text
origin https://github.com/n1jica/sumo-loco-manipulation-task-design.git
```

项目必需文件中只有 `docs/environment_setup.md` 起初不存在，已创建。`wsl` 命令返回 Windows Subsystem for Linux 未安装发行版的提示，并建议执行 `wsl.exe --install`。

### 初步判断

错误类型：Linux / WSL2 环境缺失。

可能原因：当前 Windows 主机没有安装或初始化 WSL2 Linux 发行版，因此无法执行用户要求的 Linux 环境检查、pixi 安装、SUMO build、pytest 或 baseline run。

### 修复尝试

未尝试自动安装 WSL2。WSL2 安装会改变系统环境，且可能需要管理员权限和重启，应由用户确认后执行。

### 结果

需要人工确认。当前阶段停止在环境检查失败点；未执行 `pixi install`、`pixi run build`、SUMO pytest 或 baseline episode。
