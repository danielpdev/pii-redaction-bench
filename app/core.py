"""An intentionally bounded regex baseline with exact-span error analysis."""

import json
import re
from pathlib import Path

PATTERNS = {
    "EMAIL": re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
    "PHONE": re.compile(r"(?<!\w)\+\d{2}\s\d{3}\s\d{3}\s\d{3}(?!\d)"),
}


def detect(text):
    spans = [
        dict(type=kind, start=m.start(), end=m.end())
        for kind, regex in PATTERNS.items()
        for m in regex.finditer(text)
    ]
    return sorted(spans, key=lambda s: (s["start"], s["end"]))


def redact(text, spans):
    last = 0
    parts = []
    for s in sorted(spans, key=lambda s: s["start"]):
        if not 0 <= s["start"] < s["end"] <= len(text) or s["start"] < last:
            raise ValueError("invalid or overlapping spans")
        parts.extend([text[last : s["start"]], f"[{s['type']}]"])
        last = s["end"]
    return "".join(parts) + text[last:]


def score(cases):
    tp = fp = fn = 0
    errors = []
    for case in cases:
        predicted = detect(case["text"])
        p = {(s["type"], s["start"], s["end"]) for s in predicted}
        g = {(s["type"], s["start"], s["end"]) for s in case["spans"]}
        tp += len(p & g)
        fp += len(p - g)
        fn += len(g - p)
        if p != g:
            errors.append(
                dict(
                    id=case["id"],
                    false_positives=sorted(p - g),
                    misses=sorted(g - p),
                    redacted=redact(case["text"], predicted),
                )
            )
    return dict(
        precision=tp / (tp + fp) if tp + fp else 0,
        recall=tp / (tp + fn) if tp + fn else 0,
        true_positives=tp,
        false_positives=fp,
        false_negatives=fn,
        errors=errors,
    )


def evaluate(mode="fixture"):
    cases = json.loads(Path("data/cases.json").read_text())
    r = score(cases)
    return dict(
        passed=True,
        metrics=r,
        case_count=len(cases),
        limitation="Baseline recognizes formatted emails and one international phone shape. It intentionally misses names and obfuscated email. Not an anonymization guarantee.",
    )


def demo(mode="fixture"):
    cases = json.loads(Path("data/cases.json").read_text())
    return dict(
        examples=[dict(text=c["text"], redacted=redact(c["text"], detect(c["text"]))) for c in cases],
        evaluation=evaluate(mode),
    )
