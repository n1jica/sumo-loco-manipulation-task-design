from project.metrics import TrialMetrics, success_rate


def test_success_rate() -> None:
    records = [
        TrialMetrics(task="g1_box", trial=0, success=True),
        TrialMetrics(task="g1_box", trial=1, success=False),
    ]
    assert success_rate(records) == 0.5

