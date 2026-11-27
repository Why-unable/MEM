#!/usr/bin/env python3
"""Build an Obsidian-ready research map from MEM paper metadata.

Stdlib only. The input schema is intentionally small:
- papers.json: list of paper records
- edges.json: list of {from,to,type,label} conceptual edges
"""
from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

CATEGORY_LABELS = {
    "architecture": "记忆架构",
    "training": "记忆策略与训练",
    "system": "系统与效率",
    "episodic": "情景记忆",
    "consolidation": "记忆整合",
    "personalization": "个性化记忆",
    "multimodal": "多模态记忆",
    "procedural": "程序性记忆",
    "multiagent": "多智能体记忆",
    "evaluation": "评测与基准",
    "safety": "安全与隐私",
    "application": "应用",
    "survey": "综述与框架",
}
CATEGORY_ORDER = list(CATEGORY_LABELS)
COLORS = {
    "architecture": "1",
    "training": "2",
    "system": "3",
    "episodic": "4",
    "consolidation": "5",
    "personalization": "6",
    "multimodal": "1",
    "procedural": "2",
    "multiagent": "3",
    "evaluation": "4",
    "safety": "6",
    "application": "5",
    "survey": "5",
}


def q(value: Any) -> str:
    """YAML-safe scalar using JSON quoting."""
    return json.dumps("" if value is None else str(value), ensure_ascii=False)


def slug(value: str) -> str:
    value = re.sub(r"[^a-zA-Z0-9\u4e00-\u9fff._-]+", "-", value).strip("-")
    return value or "untitled"


def yaml_tags(obj: dict[str, Any]) -> str:
    lines = ["---"]
    for key, value in obj.items():
        if isinstance(value, list):
            lines.append(f"{key}:")
            for item in value:
                lines.append(f"  - {q(item)}")
        elif value is None:
            lines.append(f"{key}: null")
        else:
            lines.append(f"{key}: {q(value)}")
    lines.append("---")
    return "\n".join(lines)


def load_inputs(papers_path: Path, edges_path: Path) -> tuple[list[dict], list[dict]]:
    papers = json.loads(papers_path.read_text(encoding="utf-8"))
    edges = json.loads(edges_path.read_text(encoding="utf-8"))
    ids = {p["id"] for p in papers}
    missing = [(e.get("from"), e.get("to")) for e in edges if e.get("from") not in ids or e.get("to") not in ids]
    if missing:
        raise SystemExit(f"Edges refer to unknown papers: {missing}")
    return papers, edges


def paper_url(p: dict) -> str:
    return p.get("openreview_url") or p.get("pdf_url") or ""


def write_paper_notes(vault: Path, papers: list[dict], edges: list[dict], topic: str) -> dict[str, str]:
    paper_dir = vault / "10_Papers"
    paper_dir.mkdir(parents=True, exist_ok=True)
    by_id = {p["id"]: p for p in papers}
    out_edges = defaultdict(list)
    in_edges = defaultdict(list)
    for e in edges:
        out_edges[e["from"]].append(e)
        in_edges[e["to"]].append(e)
    paths: dict[str, str] = {}
    for p in papers:
        pid = p["id"]
        rel = f"10_Papers/{pid}.md"
        paths[pid] = rel
        tags = [
            "paper",
            f"topic/{slug(topic)}",
            f"category/{p['category']}",
            f"tier/{p['venue_tier']}",
            "priority/core" if p.get("priority") == 1 else "priority/supporting",
        ]
        meta = {
            "id": pid,
            "type": "paper",
            "title": p["title"],
            "year": p.get("year"),
            "venue": p.get("venue_short"),
            "venue_tier": p.get("venue_tier"),
            "category": p.get("category"),
            "authors": p.get("authors", []),
            "doi": p.get("DOI"),
            "arxiv": p.get("arXiv"),
            "openreview": p.get("openreview_url"),
            "pdf": p.get("pdf_url"),
            "status": p.get("status", "published"),
            "tags": tags,
        }
        connections = []
        for e in out_edges.get(pid, []):
            other = by_id[e["to"]]
            connections.append(f"- {e['type']} → [[10_Papers/{e['to']}|{other['title']}]]：{e['label']}")
        for e in in_edges.get(pid, []):
            other = by_id[e["from"]]
            connections.append(f"- {e['type']} ← [[10_Papers/{e['from']}|{other['title']}]]：{e['label']}")
        connection_text = "\n".join(connections) if connections else "- 暂无显式关系，等待后续补边。"
        body = f"""{yaml_tags(meta)}
# {p['title']}

> **一句话定位**：{p.get('role_zh', '')}

## 元数据

- **Venue**：{p.get('venue_short') or p.get('venue')}（{p.get('venue_tier')}）
- **年份**：{p.get('year')}
- **作者**：{', '.join(p.get('authors', []))}
- **PDF**：[打开 PDF]({p.get('pdf_url')})
- **OpenReview / Proceedings**：[查看记录]({p.get('openreview_url')})

## 摘要

{p.get('abstract', '')}

## 在研究地图中的位置

- **类别**：{CATEGORY_LABELS.get(p.get('category'), p.get('category'))}
- **角色**：{p.get('role_zh', '')}
- **优先级**：{'核心' if p.get('priority') == 1 else '支撑/扩展'}

## 关系

{connection_text}

## 我的阅读问题

1. 它把记忆的哪个环节作为核心：写入、组织、检索、整合、遗忘，还是评测？
2. 它和 [[20_Topics/{topic}]] 中的哪条研究线索最接近？
3. 它的实验能否迁移到我的研究问题？需要哪些数据或基线？

## 可扩展笔记

- 关键方法：
- 关键实验：
- 局限：
- 可复用点：
- 与 Zotero 条目：
"""
        (paper_dir / f"{pid}.md").write_text(body, encoding="utf-8")
    return paths


def write_topic(vault: Path, papers: list[dict], topic: str) -> str:
    topic_dir = vault / "20_Topics"
    topic_dir.mkdir(parents=True, exist_ok=True)
    rel = f"20_Topics/{topic}.md"
    by_cat = defaultdict(list)
    for p in papers:
        by_cat[p["category"]].append(p)
    sections = []
    for cat in CATEGORY_ORDER:
        if cat not in by_cat:
            continue
        sections.append(f"## {CATEGORY_LABELS[cat]}\n")
        bullets = []
        for p in sorted(by_cat[cat], key=lambda x: (x.get("priority", 9), x["year"] or 0, x["title"])):
            bullets.append(f"- [[10_Papers/{p['id']}|{p['title']}]] — {p['venue_short']} — {p['role_zh']}")
        sections.append("\n".join(bullets))
        sections.append("")
    counts = Counter(p["category"] for p in papers)
    tier_counts = Counter(p["venue_tier"] for p in papers)
    body = f"""---
type: topic
topic: {q(topic)}
paper_count: {len(papers)}
updated: 2026-11-19
tags:
  - topic
  - agent-memory
---

# {topic}

## 范围

- 时间：2025-01-01 至 2026-11-19
- 对象：LLM/agent 的长期记忆、episodic memory、memory policy、记忆整合、记忆评测与安全
- 发表要求：优先 CCF-A/顶会正式发表；ICLR、COLM、MLSys 等顶级但非 CCF-A 的 venue 单独标注
- 收录：{len(papers)} 篇

## 统计

- 类别分布：{', '.join(f'{CATEGORY_LABELS[c]} {n}' for c, n in counts.most_common())}
- Venue 层级：{', '.join(f'{k} {v}' for k, v in tier_counts.most_common())}

## 深度综合

完整的研究综合、争议、空白和阅读顺序见：

- [[40_Maps/{topic} Synthesis]]

## 快速阅读路径

1. 先读 [[10_Papers/amem|A-Mem]]、[[10_Papers/gmemory|G-Memory]]、[[10_Papers/longmemeval|LongMemEval]] 建立问题框架。
2. 再读 [[10_Papers/memoryr1|Memory-R1]]、[[10_Papers/memagent|MemAgent]]、[[10_Papers/memeolve|MemEvolve]] 看“记忆策略学习”路线。
3. 接着读 [[10_Papers/recmem|RecMem]]、[[10_Papers/timem|TiMem]]、[[10_Papers/tiermem|TierMem]] 看记忆整合与压缩。
4. 最后读 [[10_Papers/injection|Memory Injection]]、[[10_Papers/privacy|Privacy Risks]]、[[10_Papers/poisononce|Poison Once]] 看安全边界。

{"\n\n".join(sections)}
## 关键研究缺口

- **统一评测**：LongMemEval、MemBench、Minerva、PersistBench 各自强调不同能力，仍缺少跨任务、跨模态的统一协议。
- **记忆策略学习**：Memory-R1、MemAgent、MemEvolve 代表 RL/进化路线，但训练成本、稳定性和可迁移性仍未解决。
- **遗忘与隐私**：PersistBench 关注“何时忘”，隐私/注入工作关注“不能忘什么”，两者还没有形成统一的记忆治理框架。
- **多智能体共享记忆**：G-Memory、Learning to Share 是起点，但共享粒度、权限和冲突解决仍是空白。
- **从记忆到能力**：程序性记忆与经验复用（Remember Me, Refine Me）可能比“检索更多历史”更接近真正的终身学习。

## 说明

本页是**概念地图**，边表示研究主题之间的继承、扩展、对照或应用关系，不等同于逐条引文关系。每篇论文的正式 venue、PDF 与源记录见论文笔记。
"""
    (topic_dir / f"{topic}.md").write_text(body, encoding="utf-8")
    return rel


def write_mermaid(papers: list[dict], edges: list[dict]) -> str:
    by_id = {p["id"]: p for p in papers}
    lines = ["```mermaid", "flowchart LR"]
    for cat in CATEGORY_ORDER:
        items = [p for p in papers if p["category"] == cat]
        if not items:
            continue
        lines.append(f"  subgraph {cat}[{CATEGORY_LABELS[cat]}]")
        for p in items:
            label = p["title"].replace('"', "'").replace("\n", " ")
            if len(label) > 42:
                label = label[:39] + "..."
            lines.append(f'    {p["id"]}["{label}"]')
        lines.append("  end")
    for e in edges:
        lines.append(f'  {e["from"]} -->|{e["type"]}| {e["to"]}')
    lines.append("```")
    return "\n".join(lines)


def write_map_markdown(out: Path, papers: list[dict], edges: list[dict], topic: str) -> None:
    lines = [
        f"# {topic} · Research Map",
        "",
        f"- 论文数：{len(papers)}",
        f"- 关系数：{len(edges)}",
        "- 范围：2025-01-01 至 2026-11-19",
        "- 说明：边为概念关系，不等同于逐条引文。",
        "",
        "## 全景图",
        "",
        write_mermaid(papers, edges),
        "",
        "## 论文清单",
        "",
        "| ID | 论文 | Venue | 层级 | 类别 | 定位 |",
        "|---|---|---|---|---|---|",
    ]
    for p in sorted(papers, key=lambda x: (CATEGORY_ORDER.index(x["category"]), x.get("priority", 9), x["year"] or 0)):
        lines.append(
            f"| `{p['id']}` | {p['title']} | {p['venue_short']} | {p['venue_tier']} | "
            f"{CATEGORY_LABELS.get(p['category'], p['category'])} | {p['role_zh']} |"
        )
    lines += [
        "",
        "## 关系边",
        "",
        "| From | 类型 | To | 解释 |",
        "|---|---|---|---|",
    ]
    by_id = {p["id"]: p for p in papers}
    for e in edges:
        lines.append(f"| {by_id[e['from']]['title']} | {e['type']} | {by_id[e['to']]['title']} | {e['label']} |")
    lines += [
        "",
        "## 维护规则",
        "",
        "- 新增论文先写入 `data/agent-memory-2025/papers.json`。",
        "- 新增关系先写入 `data/agent-memory-2025/edges.json`。",
        "- 然后运行 `python3 scripts/build_research_map.py --papers ... --edges ... --vault ... --out ...`。",
    ]
    (out / "research-map.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_canvas(vault: Path, out: Path, papers: list[dict], edges: list[dict], topic: str) -> None:
    by_id = {p["id"]: p for p in papers}
    cat_x = {cat: i * 520 for i, cat in enumerate(CATEGORY_ORDER)}
    cat_y = defaultdict(int)
    nodes = []
    for cat in CATEGORY_ORDER:
        items = sorted([p for p in papers if p["category"] == cat], key=lambda x: (x.get("priority", 9), x["year"] or 0, x["title"]))
        for p in items:
            y = cat_y[cat]
            cat_y[cat] += 220
            nodes.append({
                "id": p["id"],
                "type": "file",
                "file": f"10_Papers/{p['id']}.md",
                "x": cat_x[cat],
                "y": y,
                "width": 420,
                "height": 150,
                "color": COLORS.get(cat, "1"),
            })
    canvas_edges = []
    for i, e in enumerate(edges):
        canvas_edges.append({
            "id": f"edge-{i}",
            "fromNode": e["from"],
            "fromSide": "right",
            "toNode": e["to"],
            "toSide": "left",
            "label": f"{e['type']}: {e['label']}",
            "color": "4",
        })
    canvas = {"nodes": nodes, "edges": canvas_edges}
    (out / "research-map.canvas").write_text(json.dumps(canvas, ensure_ascii=False, indent=2), encoding="utf-8")
    # Put a second copy inside the Obsidian vault, where Canvas is normally opened.
    (vault / "40_Maps" / f"{topic}.canvas").write_text(json.dumps(canvas, ensure_ascii=False, indent=2), encoding="utf-8")


def write_csv(out: Path, papers: list[dict]) -> None:
    fields = ["id", "title", "year", "venue_short", "venue_tier", "category", "priority", "role_zh", "DOI", "arXiv", "openreview_url", "pdf_url"]
    with (out / "papers.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore", lineterminator="\n")
        w.writeheader()
        for p in papers:
            w.writerow(p)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--papers", required=True)
    ap.add_argument("--edges", required=True)
    ap.add_argument("--vault", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--topic", default="Agent Memory 2025+")
    args = ap.parse_args()
    papers_path, edges_path = Path(args.papers), Path(args.edges)
    vault, out = Path(args.vault), Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    vault.mkdir(parents=True, exist_ok=True)
    papers, edges = load_inputs(papers_path, edges_path)
    write_paper_notes(vault, papers, edges, args.topic)
    write_topic(vault, papers, args.topic)
    write_mermaid(papers, edges)
    write_map_markdown(out, papers, edges, args.topic)
    write_canvas(vault, out, papers, edges, args.topic)
    write_csv(out, papers)
    synthesis = out / "SYNTHESIS.md"
    if synthesis.exists():
        (vault / "40_Maps" / f"{args.topic} Synthesis.md").write_text(synthesis.read_text(encoding="utf-8"), encoding="utf-8")
    (out / "research-map.json").write_text(json.dumps({
        "topic": args.topic,
        "scope": {"from": "2025-01-01", "to": "2026-11-19"},
        "paper_count": len(papers),
        "edge_count": len(edges),
        "papers": papers,
        "edges": edges,
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Built {len(papers)} papers, {len(edges)} edges")
    print(f"Vault: {vault}")
    print(f"Output: {out}")


if __name__ == "__main__":
    main()
