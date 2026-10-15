import pytest
from ml_service.domain import classify

def test_classification_is_deterministic():
    assert classify(2500, 2).score == 50
    assert classify(2500, 2).category == "medium"

def test_high_risk_threshold():
    assert classify(4000, 2).category == "high"

@pytest.mark.parametrize("amount", [-1, float("nan"), float("inf")])
def test_bad_amounts_fail(amount):
    with pytest.raises(ValueError, match="finite, nonnegative"):
        classify(amount, 0)

def test_invalid_past_due_fails():
    with pytest.raises(ValueError, match="nonnegative integer"):
        classify(20.0, -1)
