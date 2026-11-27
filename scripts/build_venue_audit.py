#!/usr/bin/env python3
"""Regenerate the topic venue audit from the paper source of truth."""
from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path

TIER_ORDER = ["CCF-A", "Top-ICLR", "Top-COLM", "Top-MLSys", "ACL-Findings", "CCF-B"]
TIER_NOTE = {
    "CCF-A": "CCF-A 主会/期刊。",
    "Top-ICLR": "ICLR 为顶级会议，但在旧 CCF 目录中不标为 CCF-A。",
    "Top-COLM": "COLM 为顶级会议，但在旧 CCF 目录中不标为 CCF-A。",
    "Top-MLSys": "MLSys 为顶级系统会议，但在旧 CCF 目录中不标为 CCF-A。",
    "ACL-Findings": "ACL Findings 为高质量 Findings track，不是 ACL 主会。",
    "CCF-B": "明确标注为非 CCF-A 的高质量 venue。",
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--papers", default="data/agent-memory-2025/papers.json")
    parser.add_argument("--out", default="data/agent-memory-2025/VENUE_AUDIT.md")
    args = parser.parse_args()

    papers = json.loads(Path(args.papers).read_text(encoding="utf-8"))
    grouped: dict[str, list[dict]] = defaultdict(list)
    for paper in papers:
        grouped[paper["venue_tier"]].append(paper)

    tiers = [tier for tier in TIER_ORDER if tier in grouped]
    tiers += sorted(set(grouped) - set(tiers))

    parts = [
        "# Venue Audit — Agent Memory 2025+",
        "",
        "> 本文件由 `scripts/build_venue_audit.py` 从 `papers.json` 生成。",
        "> 主库只收录正式发表论文；venue tier 是检索与地图分层，不等同于论文质量总分。",
        "",
        "## Summary",
        "",
        "| Tier | Papers |",
        "|---|---:|",
    ]
    for tier in tiers:
        parts.append(f"| {tier} | {len(grouped[tier])} |")
    parts.append(f"| **Total** | **{len(papers)}** |")
    parts.append("")

    for tier in tiers:
        rows = sorted(grouped[tier], key=lambda p: (p.get("year", 0), p["title"].lower()))
        parts.append(f"## {tier} ({len(rows)})")
        parts.append("")
        parts.append("| 论文 | Venue | 官方记录 | PDF |")
        parts.append("|---|---|---|---|")
        for paper in rows:
            record = paper.get("openreview_url") or paper.get("pdf_url") or ""
            pdf = paper.get("pdf_url") or paper.get("openreview_url") or ""
            record_cell = f"[record]({record})" if record else "—"
            pdf_cell = f"[PDF]({pdf})" if pdf else "—"
            title = paper["title"].replace("|", "\\|")
            parts.append(f"| {title} | {paper['venue_short']} | {record_cell} | {pdf_cell} |")
        parts.append("")

    parts.extend([
        "## Notes",
        "",
        "- venue 计数由 `papers.json` 动态生成，README/STATUS 中的总数应与本文件一致。",
        "- 正式记录优先使用官方 proceedings、出版商 DOI 或 OpenReview。",
        "- 仅 arXiv 的工作不进入本审计文件，见 `preprints-excluded.md`。",
    ])
    Path(args.out).write_text("\n".join(parts) + "\n", encoding="utf-8")
    print(f"wrote {args.out}")
    print(f"papers: {len(papers)}; tiers: {', '.join(f'{t}={len(grouped[t])}' for t in tiers)}")


if __name__ == "__main__":
    main()
