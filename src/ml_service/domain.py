"""Deterministic domain rules: intentionally NOT an ML model."""

import math
from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class Decision:
    score: int
    category: str


def classify(amount: float, past_due_count: int) -> Decision:
    """Return a deterministic risk tier, with explicit input validation.

    This is a deliberately simple Phase-0 placeholder, not a trained model.
    """
    if not math.isfinite(amount) or amount < 0:
        raise ValueError("amount must be a finite, nonnegative number")
    if (
        isinstance(past_due_count, bool)
        or not isinstance(past_due_count, int)
        or past_due_count < 0
    ):
        raise ValueError("past_due_count must be a nonnegative integer")
    score = min(60, int(amount // 1000) * 5) + min(40, past_due_count * 20)
    category = "high" if score >= 60 else "medium" if score >= 30 else "low"
    return Decision(score=score, category=category)


def as_payload(decision: Decision) -> dict[str, int | str]:
    return asdict(decision)
