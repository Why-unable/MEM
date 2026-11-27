#!/usr/bin/env python3
"""Check that the human-facing docs match the current repository sources."""
from __future__ import annotations

import csv
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAPERS = ROOT / "data/agent-memory-2025/papers.json"
EDGES = ROOT / "data/agent-memory-2025/edges.json"
TIMELINE = ROOT / "data/agent-memory-2025/baseline-timeline.json"
TIMELINE_CSV = ROOT / "data/agent-memory-2025/baseline-timeline.csv"
TIMELINE_NOTE = ROOT / "vault/40_Maps/Agent Memory 2025+ Baseline Timeline.md"
ROUTE_NOTE = ROOT / "个人理解/路线分类.md"
VENUE_AUDIT = ROOT / "data/agent-memory-2025/VENUE_AUDIT.md"
EVIDENCE_DIR = ROOT / "vault/10_Papers/evidence"
PROPOSAL_DIR = ROOT / "开题报告"


def fail(message: str) -> None:
    raise SystemExit(f"docs-check failed: {message}")


def read(path: Path) -> str:
    if not path.exists():
        fail(f"missing file: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def require(text: str, needle: str, label: str) -> None:
    if needle not in text:
        fail(f"{label} does not contain {needle!r}")


def main() -> None:
    papers = json.loads(read(PAPERS))
    edges = json.loads(read(EDGES))
    timeline = json.loads(read(TIMELINE))
    paper_ids = {p["id"] for p in papers}
    paper_count = len(papers)
    edge_count = len(edges)
    venue_counts = Counter(p["venue_tier"] for p in papers)

    if len(paper_ids) != paper_count:
        fail("duplicate paper ids")

    # Canonical source coverage.
    timeline_rows = timeline.get("papers", [])
    timeline_ids = {r["paper_id"] for r in timeline_rows}
    if len(timeline_rows) != paper_count or timeline_ids != paper_ids:
        fail("baseline-timeline.json does not cover exactly the paper source")

    csv_rows = list(csv.DictReader(read(TIMELINE_CSV).splitlines()))
    if len(csv_rows) != paper_count:
        fail(f"baseline CSV has {len(csv_rows)} rows, expected {paper_count}")
    if {r["paper_id"] for r in csv_rows} != paper_ids:
        fail("baseline CSV ids do not match papers.json")
    if any(not r.get("tagline") for r in csv_rows):
        fail("baseline CSV contains empty tagline")

    # Every paper has a live evidence card and a generated paper note.
    evidence_status = {}
    for paper_id in sorted(paper_ids):
        evidence_path = EVIDENCE_DIR / f"{paper_id}-evidence.md"
        evidence_text = read(evidence_path)
        match = re.search(r"^status:\s*(\S+)\s*$", evidence_text, re.MULTILINE)
        if not match:
            fail(f"missing evidence status: {evidence_path.relative_to(ROOT)}")
        evidence_status[paper_id] = match.group(1)
        read(ROOT / f"vault/10_Papers/{paper_id}.md")
    not_checked = {pid: status for pid, status in evidence_status.items() if status not in {"evidence-checked", "verified"}}
    if not_checked:
        fail(f"non-checked evidence: {not_checked}")

    # Human-facing timeline and route map must link every paper and carry tags.
    timeline_note = read(TIMELINE_NOTE)
    timeline_links = re.findall(r"\[\[10_Papers/evidence/(.+?)-evidence\|", timeline_note)
    if len(timeline_links) != paper_count or set(timeline_links) != paper_ids:
        fail("timeline note does not contain exactly one evidence link per paper")

    route_note = read(ROUTE_NOTE)
    route_links = list(re.finditer(r"\[([^\]]+)\]\(\.\./vault/10_Papers/evidence/(.+?)-evidence\.md\)", route_note))
    route_ids = {m.group(2) for m in route_links}
    if route_ids != paper_ids:
        fail("route classification does not link all papers")
    if any(" · " not in m.group(1) for m in route_links):
        fail("route classification contains a paper link without a tagline")

    # Venue audit must be complete and its counts current.
    venue_text = read(VENUE_AUDIT)
    require(venue_text, f"| **Total** | **{paper_count}** |", "VENUE_AUDIT.md")
    for tier, count in venue_counts.items():
        require(venue_text, f"| {tier} | {count} |", "VENUE_AUDIT.md")
    for paper in papers:
        require(venue_text, paper["title"].replace("|", "\\|"), "VENUE_AUDIT.md")

    # Top-level status docs.
    readme = read(ROOT / "README.md")
    require(readme, f"收录论文：**{paper_count} 篇**", "README.md")
    require(readme, f"概念关系：**{edge_count} 条**", "README.md")
    require(readme, "docs/multi-machine-playbook.md", "README.md")
    require(readme, "Agent Memory 2025+ Baseline Timeline.md", "README.md")
    require(readme, "开题报告/README.md", "README.md")

    status = read(ROOT / "STATUS.md")
    require(status, "当前阶段：`v0.2.4", "STATUS.md")
    require(status, "research/agent-memory-evidence", "STATUS.md")
    require(status, f"论文：{paper_count}", "STATUS.md")
    require(status, f"关系：{edge_count}", "STATUS.md")
    require(status, f"全文证据卡：{paper_count}", "STATUS.md")

    roadmap = read(ROOT / "ROADMAP.md")
    require(roadmap, "v0.2.4", "ROADMAP.md")
    require(roadmap, f"{paper_count}/52" if paper_count == 52 else str(paper_count), "ROADMAP.md")
    require(roadmap, "docs/multi-machine-playbook.md", "ROADMAP.md")

    map_readme = read(ROOT / "maps/agent-memory-2025/README.md")
    require(map_readme, f"- {paper_count} papers", "maps/agent-memory-2025/README.md")
    require(map_readme, f"- {edge_count} conceptual edges", "maps/agent-memory-2025/README.md")
    require(map_readme, f"- {venue_counts['CCF-A']} CCF-A", "maps/agent-memory-2025/README.md")

    data_readme = read(ROOT / "data/agent-memory-2025/README.md")
    require(data_readme, f"主论文库，{paper_count} 篇", "data/agent-memory-2025/README.md")
    require(data_readme, f"概念关系，{edge_count} 条", "data/agent-memory-2025/README.md")
    require(data_readme, "baseline-timeline.json", "data/agent-memory-2025/README.md")

    evidence_readme = read(EVIDENCE_DIR / "README.md")
    require(evidence_readme, f"`evidence-checked`：{paper_count} 篇", "evidence/README.md")
    require(evidence_readme, "Baseline Timeline", "evidence/README.md")

    dashboard = read(ROOT / "vault/90_System/Dashboard.md")
    require(dashboard, f"{paper_count} 篇论文，{edge_count} 条概念关系", "vault Dashboard")
    require(dashboard, "Baseline Timeline", "vault Dashboard")

    # Proposal pack.
    proposal_files = [
        "README.md",
        "01_选题方法与方向评估.md",
        "02_国内开题报告写作规范.md",
        "03_备选方向A_自适应记忆路由研究设计.md",
        "04_开题报告初稿模板.md",
        "05_VikingMem后续研究与方向B设计.md",
        "06_备选方向A_开题报告模板.md",
        "07_下一步_导师讨论版.md",
    ]
    proposal_texts = {name: read(PROPOSAL_DIR / name) for name in proposal_files}
    primary_title = "面向知识更新的可追溯事件—实体记忆冲突消解与回滚方法研究"
    require(proposal_texts["README.md"], primary_title, "开题报告/README.md")
    require(proposal_texts["04_开题报告初稿模板.md"], primary_title, "开题报告/04_开题报告初稿模板.md")
    require(proposal_texts["05_VikingMem后续研究与方向B设计.md"], primary_title, "开题报告/05_VikingMem后续研究与方向B设计.md")
    require(proposal_texts["02_国内开题报告写作规范.md"], "学校/学院模板为准", "开题报告/02_国内开题报告写作规范.md")
    require(proposal_texts["04_开题报告初稿模板.md"], "一页研究设计画布", "开题报告/04_开题报告初稿模板.md")
    require(proposal_texts["07_下一步_导师讨论版.md"], "2 页的“导师讨论版研究方案”", "开题报告/07_下一步_导师讨论版.md")
    require(proposal_texts["07_下一步_导师讨论版.md"], "2–4 周行动清单", "开题报告/07_下一步_导师讨论版.md")

    playbook = read(ROOT / "docs/multi-machine-playbook.md")
    require(playbook, "research/agent-memory-evidence", "multi-machine playbook")
    require(playbook, "make docs-check", "multi-machine playbook")

    print(f"papers: {paper_count}")
    print(f"edges: {edge_count}")
    print("venue tiers: " + ", ".join(f"{k}={v}" for k, v in sorted(venue_counts.items())))
    print(f"evidence: {paper_count}/{paper_count}")
    print(f"timeline rows: {len(timeline_rows)}")
    print(f"timeline links: {len(timeline_links)}")
    print(f"route links: {len(route_links)}")
    print("proposal docs: OK")
    print("docs: OK")


if __name__ == "__main__":
    main()
