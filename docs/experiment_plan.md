# Experiment Plan

## Baseline Task

`g1_box` with upstream object and cost settings.

## Modified Task

Candidate: heavier G1 box plus longer target distance, with optional cost-weight adjustment.

## Hypothesis

The heavier/longer-distance task should reduce performance. A cost-weight adjustment should recover some goal-reaching performance if the MPC can still find stable contact-rich behavior.

## Experimental Variables

- Object mass.
- Goal position or goal distance.
- `w_goal`.
- `w_hand_proximity`.

## Controlled Variables

- Low-level WBC policy.
- Optimizer type.
- Episode length.
- Number of trials per group.
- Initial robot pose unless explicitly part of the experiment.

## Metrics

- Success rate.
- Final object-goal distance.
- Completion time.
- Fall flag/rate.
- Task cost.
- Runtime/planning time if available.

## Expected Results

Baseline should perform best. The heavier/longer-distance variant should be harder. The tuned cost variant may improve final distance or success rate but could increase instability or control cost.

## Risks And Fallbacks

- If G1 build fails, use WSL/Linux or switch to a runnable Spot/simple task.
- If videos are hard to export, use trajectory visualizations first.
- If 10 trials are slow, run 3 trials per group and document the limitation.

