import pytest
from app.core import detect, redact, score, evaluate


def test_exact_spans_and_no_ticket_false_positive():
    text = "Email a@example.test; ticket 123456."
    s = detect(text)
    assert len(s) == 1 and text[s[0]["start"] : s[0]["end"]] == "a@example.test"
    assert redact(text, s) == "Email [EMAIL]; ticket 123456."


def test_known_misses_are_reported():
    r = evaluate()["metrics"]
    assert r["recall"] < 1 and r["false_negatives"] == 2


def test_overlap_rejected():
    with pytest.raises(ValueError):
        redact("abcdef", [{"type": "X", "start": 0, "end": 3}, {"type": "Y", "start": 2, "end": 4}])


def test_exact_span_not_partial_credit():
    r = score([{"id": "a", "text": "a@example.test", "spans": [{"type": "EMAIL", "start": 0, "end": 3}]}])
    assert r["true_positives"] == 0 and r["false_positives"] == 1 and r["false_negatives"] == 1
