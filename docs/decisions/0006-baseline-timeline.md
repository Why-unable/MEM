# ADR-0006: Baseline Timeline Is a Derived Evidence Layer

- Status: accepted
- Date: 2026-11-27
- Owners: MEM
- Related: `data/agent-memory-2025/baseline-timeline.json`, `scripts/build_baseline_timeline.py`

## Context

Per-paper evidence answers “what does this paper claim?” but not “which paper is strongest, on which benchmark, against which baseline, and how did the baseline family change over time?” A single cross-paper ranking is misleading because papers differ in dataset, backbone, judge, split, retrieval budget, and metric.

## Decision

Maintain a curated timeline source:

```text
data/<topic>/baseline-timeline.json
```

Generate:

```text
data/<topic>/baseline-timeline.csv
vault/40_Maps/<Topic> Baseline Timeline.md
```

The timeline:

- Uses formal publication month.
- Preserves each paper’s own metric and score.
- Separates utility, efficiency, safety, benchmark, and survey lanes.
- Uses a 2–6 字 mechanism tagline for fast scanning.
- Sorts within a month only as a browsing aid, not as a cross-task scientific ranking.

## Consequences

- The repository can answer “what is currently best on LoCoMo / LongMemEval?” while preserving caveats.
- Adding a paper requires updating both paper metadata and timeline data when a comparable result exists.
- Generated CSV and Markdown must not be hand-edited; source conflicts must be resolved in JSON first.
- Cross-benchmark `delta_pct` remains a heuristic, not a universal score.

## Alternatives

- Single global leaderboard: rejected because metrics and protocols differ.
- Only per-paper evidence: rejected because it does not expose temporal baseline drift.
- Hand-maintained Markdown table: rejected because it drifts from source data and is hard to validate.

## Validation

```bash
make baseline-timeline
make docs-check
make check
```

`scripts/check_docs.py` verifies 52 paper IDs, 52 timeline rows, 52 evidence links, and tagline coverage.
