#!/usr/bin/env python3
"""Build the time-ordered baseline/effect note from the curated JSON source."""
from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path


LANE_ORDER = {
    "utility": 0,
    "efficiency": 1,
    "safety": 2,
    "benchmark": 3,
    "survey": 4,
}
TYPE_LABEL = {
    "method": "方法",
    "benchmark": "Benchmark",
    "attack": "安全攻击",
    "survey": "综述",
}
LANE_LABEL = {
    "utility": "效果",
    "efficiency": "效率 / Pareto",
    "safety": "安全",
    "benchmark": "评测基准",
    "survey": "综述",
}


def evidence(paper_id: str, label: str) -> str:
    return f"[[10_Papers/evidence/{paper_id}-evidence|{label}]]"


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sort_rows(rows: list[dict]) -> list[dict]:
    indexed = list(enumerate(rows))
    def key(item: tuple[int, dict]):
        index, row = item
        delta = row.get("delta_pct") if row["lane"] == "utility" else None
        return (
            LANE_ORDER[row["lane"]],
            0 if delta is not None else 1,
            -(delta or 0),
            index,
        )
    return [row for _, row in sorted(indexed, key=key)]


def write_csv(path: Path, rows: list[dict]) -> None:
    columns = [
        "date", "paper_id", "short", "tagline", "type", "lane", "datasets",
        "headline", "comparison", "delta_pct", "baseline_shift", "note",
    ]
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=columns, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({key: row.get(key, "") for key in columns})


def build_note(data: dict) -> str:
    rows = data["papers"]
    grouped: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        grouped[row["date"]].append(row)

    parts: list[str] = []
    parts.append("---")
    parts.append("type: evidence")
    parts.append("subtype: baseline-timeline")
    parts.append("status: evidence-checked")
    parts.append(f"checked_at: {data['as_of']}")
    parts.append("tags:")
    parts.append("  - evidence")
    parts.append("  - baseline")
    parts.append("  - dataset")
    parts.append("  - timeline")
    parts.append("---")
    parts.append("")
    parts.append("# Agent Memory 2025+：时间化论文效果、数据集与基线变化")
    parts.append("")
    parts.append("> 范围：主库 52 篇正式发表论文；时间按正式 venue 的发表月份排列。")
    parts.append("> 目标：回答三件事：同月有哪些工作、主结果如何、它们和谁比、baseline 如何演化。")
    parts.append("> 数据源：[JSON](../../data/agent-memory-2025/baseline-timeline.json) · [CSV](../../data/agent-memory-2025/baseline-timeline.csv)")
    parts.append("> 实验设置背景：[EXPERIMENT_LANDSCAPE](../../maps/agent-memory-2025/EXPERIMENT_LANDSCAPE.md) · 逐篇证据：[[10_Papers/evidence/INDEX|Evidence Index]]")
    parts.append("")
    parts.append("## 0. 先看结论：目前的“最好”是条件性的")
    parts.append("")
    parts.append("**如果只看当前最醒目的绝对分数，VikingMem 是最强候选之一：**")
    parts.append("")
    parts.append("- LoCoMo LLM-Judge：**90.12**（GPT-4.1-mini），高于同表 Full-Context 的 86.36；GPT-4o-mini 设置下为 **88.83**。")
    parts.append("- LongMemEval-S LLM-Judge：**75.80**（GPT-4o），高于 Zep 的 70.40；GPT-4o-mini 下为 **66.36**。")
    parts.append("- 但它不是跨任务总冠军：LoCoMo F1 只有 **54.98**，与 TiMem、E-mem 的 54 分头部差距很小，且 backbone / judge / split 不同。")
    parts.append("")
    parts.append("**如果按 benchmark 分别看，头部大致是：**")
    parts.append("")
    parts.append("| Benchmark / 指标 | 头部结果 | 强对照 | 能下的判断 |")
    parts.append("|---|---|---|---|")
    parts.append("| LoCoMo LLM-Judge / GPT-4o-mini | VikingMem **88.83**；TiMem 75.30；Nemori 73.0；MAGMA 70.0 | Mirix 78.66；Full-Context 77.47 | VikingMem 明显领先，但 judge prompt 与 split 未统一 |")
    parts.append("| LoCoMo LLM-Judge / GPT-4.1-mini | VikingMem **90.12**；RecMem 81.10；Nemori 80.8 | Full-Context 86.36；Mem0 62.92 | 绝对分最高，仍未与所有方法做同 backbone 对照 |")
    parts.append("| LoCoMo LLM-Judge / Claude-Sonnet-4.5 | MRAgent **88.32** | LangMem 78.61 | active reconstruction 在强 backbone 上也有效 |")
    parts.append("| LoCoMo LLM-Judge / Gemini-2.5-Flash | MRAgent **84.21** | Mem0 68.31 | 同一方法换 backbone 后仍是强基线 |")
    parts.append("| LoCoMo F1 | VikingMem **54.98**；TiMem 54.40；E-mem 54.17 | GAM 45.31；Memory-R1 45.02；A-Mem 分类别互有胜负 | 54–55 是当前公开 F1 头部簇，差距不足以宣布绝对胜者 |")
    parts.append("| LongMemEval-S | TiMem **76.88**；RecMem **76.80**；VikingMem **75.80** | Zep 70.40；MemoryOS 74.40；Full-Context 59.20–66.20 | 三篇处于同一头部区间，backbone 和指标版本不同 |")
    parts.append("| 个性化 / 推荐 / 工具 | PersonaAgent LaMP-1 0.919；MemRec H@1 0.5882；ReMe Pass@4 69.97 | 各自任务内 baseline | 不能换算成 LoCoMo 排名 |")
    parts.append("| 行动 / 具身 | LightWM ALFWorld 0.910；AgeMem 五任务平均 54.31；LTS GAIA 30.4 | 同设置 baseline | 记忆对“行动闭环”的收益通常更大，但任务差异也更大 |")
    parts.append("")
    parts.append("**效率上表现最好的不是最高分论文：**")
    parts.append("")
    parts.append("- **TierMem**：LoCoMo accuracy 0.851 vs raw-only 0.873（-2.2 pp），但 input tokens **-54.1%**、latency **-60.7%**。")
    parts.append("- **Hippocampus**：检索加速 **1.1x–31.5x**，per-query token 降低 **1.1x–14.5x**。")
    parts.append("- **LightMem**：LongMemEval total token 最多降低 **38x**，LoCoMo accuracy 提升区间 **6.10%–29.29%**。")
    parts.append("- **Mem0**：相对 full-context，p95 latency **-91%**、token **-90%+**。")
    parts.append("- **RecMem**：LongMemEval-S 76.80 且 build token 明显低于 Mem0/A-Mem，但 LoCoMo 仍低于 full-context。")
    parts.append("")
    parts.append("> **关键警告：这不是一个可以跨论文直接排名的总榜。** 行内 `+x%` 是为了提供同月浏览顺序，可能来自不同数据集、backbone、judge、split 和检索预算；严格结论必须回到同一 benchmark + 同一指标 + 同一 backbone 的子表。")
    parts.append("")
    parts.append("## 1. 怎么读这张时间表")
    parts.append("")
    parts.append("1. **时间**：使用正式发表月份，不是 arXiv 首次提交月份。")
    parts.append("2. **同月排序**：先排有明确相对提升的方法论文，再排效率、安全、benchmark 和综述；没有可换算提升的论文放在同月方法组末尾。")
    parts.append("3. **效果列**：保留论文自己的主指标，不把 F1、accuracy、success rate、ASR 混成一个分数。")
    parts.append("4. **baseline 变化**：记录作者实际对比了谁，以及新增了哪类基线；不等于引文关系。")
    parts.append("5. **未报告**：用 `—` 或“无统一 headline”标注，不用估算值填空。")
    parts.append("")

    parts.append("## 2. 月度时间轴（52 篇）")
    parts.append("")
    parts.append("> 每月内部的顺序是“效果浏览顺序”，不是跨任务的科学排名。")
    parts.append("")
    for date in sorted(grouped):
        parts.append(f"### {date}")
        parts.append("")
        parts.append("| 论文 | 类型 | 数据集 / Benchmark | 主结果 | 对照 / 变化 | Baseline 变化 |")
        parts.append("|---|---|---|---|---|---|")
        for row in sort_rows(grouped[date]):
            parts.append(
                "| "
                + " | ".join([
                    evidence(row["paper_id"], row["short"]) + f" · {row['tagline']}",
                    f"{TYPE_LABEL[row['type']]} / {LANE_LABEL[row['lane']]}",
                    row["datasets"],
                    row["headline"],
                    row["comparison"],
                    row["baseline_shift"],
                ])
                + " |"
            )
        parts.append("")

    parts.append("## 3. Baseline 是怎么变化的")
    parts.append("")
    parts.append("| 阶段 | 常见数据集 | 常见 baseline | 变化 |")
    parts.append("|---|---|---|---|")
    parts.append("| 2025 H1 | LoCoMo、LongBench、∞-Bench、LongMemEval 开始出现 | Full-context、BM25/dense RAG、MemGPT、MemoryBank、ReadAgent | 从“塞上下文 / 简单检索”转向结构化记忆和事件分割 |")
    parts.append("| 2025 H2 | LoCoMo 成为主战场；LongMemEval 快速普及 | A-Mem、Mem0、MemoryOS、Zep、LangMem | A-Mem 成为通用结构基线；Mem0 成为生产 pipeline 基线；MemoryOS 带入 OS/层次视角 |")
    parts.append("| 2026 H1 | LoCoMo、LongMemEval、Long-MT-Bench+、PersonaMem、M3-Bench、GAIA | 前一代 memory systems + HippoRAG 2、MAGMA、MemGAS、MRAgent、TiMem | 基线从“有没有结构”升级为“多粒度、时间层次、active reconstruction”；开始同时报告 token/latency |")
    parts.append("| 2026 H2 | 仍以 LoCoMo / LongMemEval 为主，但 BFCL、AppWorld、WebArena、MemoryArena 增多 | Mem0、MemoryOS、MAGMA、TiMem、GAM、Zep、full-context；安全论文加入攻击/防御基线 | 同时比较 accuracy–cost–action utility；benchmark 和攻击面被拆开；但跨论文协议仍不统一 |")
    parts.append("")
    parts.append("**最明显的变化：**")
    parts.append("")
    parts.append("- **从“RAG vs 结构记忆”变成“结构 × 更新策略 × 检索策略”。** 2025 年常见 baseline 还是 full-context、BM25、MemGPT、MemoryBank；到 2026 年，A-Mem、Mem0、MemoryOS 已成为新一代基础对照，MAGMA、MemGAS、MRAgent、TiMem 又成为更近的强基线。")
    parts.append("- **从单一 accuracy 变成 accuracy + token + latency + storage + action success。** 最新系统论文很少只报一个分数；TierMem、Hippocampus、LightMem、RecMem 的核心贡献往往在 Pareto 前沿。")
    parts.append("- **从“记忆有没有用”变成“什么时候不该用记忆”。** PersistBench、MEXTRA、MINJA、InjecMEM、eTAMP 把跨域污染、注入、隐私提取和遗忘纳入评测。")
    parts.append("- **baseline 越来越强，但协议没有同步统一。** 同一个 A-Mem 在不同论文里可能被重实现；LoCoMo 的 judge、split、adversarial 是否纳入、检索预算都可能不同。")
    parts.append("")

    parts.append("## 4. 数据集格局：哪些论文在用哪些数据")
    parts.append("")
    parts.append("| 任务簇 | 主要数据集 / Benchmark | 代表论文 | 主要指标 |")
    parts.append("|---|---|---|---|")
    parts.append("| 长期对话记忆 | LoCoMo、LongMemEval-S/M、Long-MT-Bench+、MSC | SeCom、Mem0、MemoryOS、A-Mem、MAGMA、MemGAS、MRAgent、TiMem、RecMem、VikingMem | F1、LLM-Judge、BLEU、accuracy、token、latency |")
    parts.append("| 人类 / 事件 / 长文 | LongBench、∞-Bench、NarrativeQA、Qasper、MuSiQue、2Wiki、Test of Time | EM-LLM、HippoRAG 2、M+、REMem、ARTEM、MemAgent、BEAM/LIGHT | F1、EM、recall、retention length |")
    parts.append("| 行动 / 具身 | ALFWorld、SciWorld、PDDL、BabyAI | G-Memory、AgeMem、LightWM、MemoryArena | success rate、progress rate、action score |")
    parts.append("| 工具 / Web / 研究 | BFCL-V3、AppWorld、GAIA、AssistantBench、WebArena、Mind2Web、SWE-Bench | ReMe、LTS、ReasoningBank、MemEvolve、MemoryArena | Pass@K、success rate、runtime、steps |")
    parts.append("| 个性化 / 推荐 | LaMP、PersonaMem、PersonaBench、Amazon、Yelp、MovieTV | Evoking/RF-Mem、PersonaAgent、MemRec | accuracy、Recall@K、Hit@K、NDCG@K |")
    parts.append("| 多模态 | M3-Bench-robot/web、VideoMME-long | M3-Agent | QA accuracy |")
    parts.append("| 安全 / 遗忘 | MIMIC-III、eICU、WebShop、WildChat、WebArena、PersistBench | MEXTRA、MINJA、InjecMEM、eTAMP、PersistBench | ASR、ISR、CER、failure rate、beneficial memory use |")
    parts.append("")

    parts.append("## 5. 重要反例：不要让“最好”掩盖条件")
    parts.append("")
    parts.append("- **A-Mem** 在 temporal / multi-hop 上很强，但在 GPT-4o 的单跳和 adversarial 上输给 full-context。")
    parts.append("- **MemGAS** 在 LongMemEval 上领先，但在 LoCoMo 上低于 HippoRAG 2（41.07 vs 45.62）。")
    parts.append("- **RecMem** 在 LongMemEval 上超过 memory systems，但在 LoCoMo 上仍低于 full-context（81.10 vs 84.18）。")
    parts.append("- **TierMem** 的 accuracy 比 raw-only 低 2.2 pp，价值在 54.1% token 和 60.7% latency 节省。")
    parts.append("- **VikingMem** 的 90.12 是强结果，但 temporal weighting 在 fact-based benchmark 中默认关闭，不能据此推断所有时间敏感任务都更强。")
    parts.append("- **LightWM** 的 0.910 是 ALFWorld 上的 procedure-centric 结果，不能外推到开放对话。")
    parts.append("- **安全 ASR 高不等于 utility 高**：MINJA、InjecMEM、eTAMP 的“效果”是攻击成功率，不是任务正确率。")
    parts.append("")

    parts.append("## 6. 对 MEM 的下一步")
    parts.append("")
    parts.append("1. **建立三条独立榜单**：utility、efficiency/Pareto、safety；不要合成一个总分。")
    parts.append("2. **统一最小比较单元**：至少固定 `benchmark + metric + backbone + judge + retrieval budget`。")
    parts.append("3. **每个方法记录四个成本**：build token、per-query token、p50/p95 latency、storage。")
    parts.append("4. **把 full-context 保留为常驻基线**：它能暴露结构化记忆在 single-hop、knowledge-update、adversarial 上的反例。")
    parts.append("5. **优先补做同条件复现**：VikingMem、TiMem、RecMem、MRAgent、MAGMA 目前最值得在统一协议下复跑。")
    parts.append("")
    parts.append("## 7. 证据入口")
    parts.append("")
    parts.append("- 逐篇证据索引：[[10_Papers/evidence/INDEX|Per-Paper Evidence Index]]")
    parts.append("- 实验设置与 baseline 家族：[EXPERIMENT_LANDSCAPE](../../maps/agent-memory-2025/EXPERIMENT_LANDSCAPE.md)")
    parts.append("- 结构化数据：[baseline-timeline.json](../../data/agent-memory-2025/baseline-timeline.json)")
    parts.append("- CSV：[baseline-timeline.csv](../../data/agent-memory-2025/baseline-timeline.csv)")
    parts.append("")
    return "\n".join(parts)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", default="data/agent-memory-2025/baseline-timeline.json")
    parser.add_argument("--papers", default="data/agent-memory-2025/papers.json")
    parser.add_argument("--out", default="vault/40_Maps/Agent Memory 2025+ Baseline Timeline.md")
    parser.add_argument("--csv-out", default="data/agent-memory-2025/baseline-timeline.csv")
    args = parser.parse_args()

    data = read_json(Path(args.data))
    papers = read_json(Path(args.papers))
    paper_ids = {p["id"] for p in papers}
    timeline_ids = {row["paper_id"] for row in data["papers"]}
    if paper_ids != timeline_ids:
        missing = sorted(paper_ids - timeline_ids)
        extra = sorted(timeline_ids - paper_ids)
        raise SystemExit(f"timeline/paper mismatch; missing={missing}, extra={extra}")

    write_csv(Path(args.csv_out), data["papers"])
    note = build_note(data)
    Path(args.out).write_text(note + "\n", encoding="utf-8")
    print(f"wrote {args.out}")
    print(f"wrote {args.csv_out}")
    print(f"papers: {len(data['papers'])}")


if __name__ == "__main__":
    main()
