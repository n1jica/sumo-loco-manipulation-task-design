# Third-Party Dependencies

Clone SUMO here for local analysis and experiments:

```bash
git clone https://github.com/rai-opensource/sumo.git third_party/sumo
```

This project ignores `third_party/sumo` in git to avoid accidentally vendoring upstream research code. If a stable upstream version is needed later, use a git submodule or record the exact commit hash in `docs/experiment_log.md`.

