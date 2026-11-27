#!/usr/bin/env python3
"""Build a per-paper evidence index and create missing evidence stubs.

The evidence directory is the per-paper evidence layer. This script does not
invent evidence: missing files are created with `status: queued` and a checklist.
Existing evidence files are never overwritten.
"""
from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

MAINLINE = {
    "architecture": "A",
    "training": "B",
    "system": "C",
    "episodic": "D",
    "consolidation": "D",
    "personalization": "E",
    "multimodal": "E",
    "procedural": "E",
    "application": "E",
    "multiagent": "E",
    "evaluation": "F",
    "safety": "G",
    "survey": "X",
}
MAINLINE_TITLE = {
    "A": "Memory Architecture",
    "B": "Memory Policy",
    "C": "Systems and Efficiency",
    "D": "Episodic Memory and Consolidation",
    "E": "Personalization, Multimodal and Procedural",
    "F": "Evaluation",
    "G": "Safety and Privacy",
    "X": "Cross-cutting",
}
STATUS_ORDER = ["queued", "metadata-only", "full-text-scan", "evidence-checked", "verified"]


def evidence_path(evidence_dir: Path, paper_id: str) -> Path:
    return evidence_dir / f"{paper_id}-evidence.md"


def existing_status(path: Path) -> str:
    if not path.exists():
        return "missing"
    text = path.read_text(encoding="utf-8")
    m = re.search(r"^status:\s*[\"']?([^\"'\n]+)", text, re.MULTILINE)
    return m.group(1).strip() if m else "unmarked"


def stub(paper: dict, mainline: str) -> str:
    authors = ", ".join(paper.get("authors", []))
    pdf = paper.get("pdf_url") or ""
    record = paper.get("openreview_url") or ""
    doi = paper.get("DOI") or "null"
    arxiv = paper.get("arXiv") or "null"
    return f'''---
type: evidence
paper_id: "{paper['id']}"
title: {json.dumps(paper['title'], ensure_ascii=False)}
status: queued
checked_at: null
source_pdf: ""
source_version: ""
pages_checked: []
mainline: "{mainline}"
tags:
  - evidence
  - mainline-{mainline.lower()}
---

# {paper['title']} — Evidence

> Status: **queued**. 这是逐篇 evidence 的入口，不是已完成的证据卡。
> 不要把下面的摘要当作已验证结论；关键数字必须回全文和页码核对。

## 元数据

- **Venue**：{paper.get('venue_short') or paper.get('venue')}（{paper.get('venue_tier')}）
- **年份**：{paper.get('year')}
- **作者**：{authors}
- **DOI**：{doi}
- **arXiv**：{arxiv}
- **PDF**：{pdf}
- **正式记录**：{record}
- **主库角色**：{paper.get('role_zh', '')}

## 官方摘要

{paper.get('abstract', '')}

## 待提取（全文核对）

- [ ] 研究问题与一句话定位
- [ ] 记忆单元 / 数据结构
- [ ] 写入、组织、检索、更新、遗忘机制
- [ ] 训练方式与监督信号（若适用）
- [ ] 数据集、backbone、baseline、指标
- [ ] 关键数字（必须标 PDF 页码或表格）
- [ ] 主要结论
- [ ] 局限与威胁
- [ ] 与主线 {mainline} 其他论文的关系
- [ ] 对 RQ1 / RQ3 的意义
- [ ] 可复用点
- [ ] 成本：build / query / latency / storage
- [ ] 待核对项

## 来源

- 主库记录：`data/agent-memory-2025/papers.json`
- PDF：{pdf}
- 正式记录：{record}
'''


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--papers", default="data/agent-memory-2025/papers.json")
    ap.add_argument("--evidence-dir", default="vault/10_Papers/evidence")
    ap.add_argument("--out", default="vault/10_Papers/evidence/INDEX.md")
    ap.add_argument("--create-missing", action="store_true")
    args = ap.parse_args()

    papers = json.loads(Path(args.papers).read_text(encoding="utf-8"))
    evidence_dir = Path(args.evidence_dir)
    evidence_dir.mkdir(parents=True, exist_ok=True)

    rows = []
    created = []
    for p in papers:
        mainline = MAINLINE.get(p.get("category", ""), "X")
        path = evidence_path(evidence_dir, p["id"])
        if not path.exists() and args.create_missing:
            path.write_text(stub(p, mainline), encoding="utf-8")
            created.append(path.name)
        rows.append({
            "id": p["id"],
            "title": p["title"],
            "venue": p.get("venue_short") or p.get("venue", ""),
            "tier": p.get("venue_tier", ""),
            "mainline": mainline,
            "status": existing_status(path),
            "file": path.name,
        })

    counts = Counter(r["status"] for r in rows)
    by_main = defaultdict(list)
    for r in rows:
        by_main[r["mainline"]].append(r)

    lines = [
        "# Per-Paper Evidence Index",
        "",
        "> 每篇主库论文都应对应一个 `<paper-id>-evidence.md`。",
        "> 状态为 `queued` 的文件只是入口，不是已验证证据。",
        "",
        "## 覆盖",
        "",
        f"- 主库论文：{len(rows)}",
        f"- 已有独立 evidence 文件：{sum(1 for r in rows if r['status'] != 'missing')}",
        f"- 已完成页码级证据卡：{counts.get('evidence-checked', 0) + counts.get('verified', 0)}",
        "",
        "```text",
    ]
    for s in STATUS_ORDER:
        lines.append(f"{s}: {counts.get(s, 0)}")
    lines += ["```", ""]

    if created:
        lines += [f"> 本次创建了 {len(created)} 个 queued 入口。", ""]

    for mainline in ["A", "B", "C", "D", "E", "F", "G", "X"]:
        items = by_main.get(mainline, [])
        if not items:
            continue
        lines += [
            f"## Mainline {mainline} · {MAINLINE_TITLE[mainline]}",
            "",
            "| Paper | Venue | Status | Evidence |",
            "|---|---|---|---|",
        ]
        for r in sorted(items, key=lambda x: (x["status"] != "evidence-checked", x["id"])):
            link = f"[{r['id']}]({r['file']})"
            lines.append(f"| {r['title']} | {r['venue']} | `{r['status']}` | {link} |")
        lines.append("")

    lines += [
        "## 状态定义",
        "",
        "- `queued`：入口存在，尚未读全文。",
        "- `metadata-only`：只核对了 metadata/摘要。",
        "- `full-text-scan`：已读方法/实验/局限，但未做页码级证据卡。",
        "- `evidence-checked`：有页码级关键数字、局限、成本与 RQ 关系。",
        "- `verified`：人工复核过来源、数字和引用。",
    ]
    Path(args.out).write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"papers: {len(rows)}, created: {len(created)}, index: {args.out}")
    if created:
        print("created:", ", ".join(created))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
