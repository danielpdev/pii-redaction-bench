# Demo walkthrough

## Start

```bash
make setup
make demo
make test
make eval
```

## What to show

The baseline returns typed character spans. Redaction validates non-overlapping bounds. Evaluation uses exact span matches and reports false positives and misses, including known unsupported classes.

## Failure case to discuss

Exact offsets, no ticket-number false positive, rejected overlapping spans and no partial credit for an incorrect boundary. Known name and obfuscated-email misses remain in the report.

## Evidence

Open the JSON evaluation report alongside the implementation. Distinguish synthetic fixture outputs, synthetic trace timing, actual elapsed evaluation time, and local model inference. Do not present a tiny test set as a production benchmark.

## Closing tradeoff

Regex support is intentionally limited to formatted emails and one phone pattern. This is not certified anonymization and must not be used as a privacy guarantee. All examples are synthetic.

The repository's `docs/demo.webm` or `docs/demo.mp4`, when present, records the demonstration. A terminal replay is also available for focused projects as `docs/demo.cast`.
