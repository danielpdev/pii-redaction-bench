# Design record

## Decision

The baseline returns typed character spans. Redaction validates non-overlapping bounds. Evaluation uses exact span matches and reports false positives and misses, including known unsupported classes.

## Failure model

Exact offsets, no ticket-number false positive, rejected overlapping spans and no partial credit for an incorrect boundary. Known name and obfuscated-email misses remain in the report.

## Tradeoffs

Regex support is intentionally limited to formatted emails and one phone pattern. This is not certified anonymization and must not be used as a privacy guarantee. All examples are synthetic.

## Next change to defend in review

Add a local NER model and independently labeled multilingual data; compare recall and over-redaction.

## Reproducibility

`uv.lock` pins Python dependencies; the web lockfile pins the React build where present. Model-backed evaluations use a separately installed local service. Dataset examples are synthetic and intentionally small. Reported timing is a local observation, not a throughput SLA. Run `make test` after changing state transitions and `make eval` after changing decisions. Keep inference quality separate from deterministic invariant checks.
