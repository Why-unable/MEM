# 2026-11-27 — 时间化 baseline 与研究效果整理

- 执行者：Codex
- 范围：`Agent Memory 2025+` 主库 52 篇正式发表论文
- 目标：按正式发表月份整理主结果、数据集、对比基线和 baseline 变化

## 完成

- 新增 `data/agent-memory-2025/baseline-timeline.json`：52 篇的精选主结果、数据集、baseline 与变化。
- 新增 `data/agent-memory-2025/baseline-timeline.csv`：便于筛选和二次分析。
- 新增 `scripts/build_baseline_timeline.py`：从 JSON 生成 Obsidian 笔记与 CSV。
- 新增 `vault/40_Maps/Agent Memory 2025+ Baseline Timeline.md`。
- 在 `maps/agent-memory-2025/EXPERIMENT_LANDSCAPE.md` 和 README 中增加入口。
- 将生成器接入 `make check`。

## 核心判断

- 绝对分数最高候选：VikingMem，LoCoMo LLM-Judge 90.12（GPT-4.1-mini）。
- LongMemEval-S 头部：TiMem 76.88、RecMem 76.80、VikingMem 75.80，backbone 与协议不同。
- LoCoMo F1 头部：VikingMem 54.98、TiMem 54.40、E-mem 54.17，差距较小。
- 效率/Pareto 代表：TierMem、Hippocampus、LightMem、Mem0、RecMem。
- 重要反例：A-Mem、MemGAS、RecMem、TierMem 都显示结果依赖任务或成本条件。

## 被否决的方向

- 不构造跨 benchmark 的统一总分：F1、accuracy、success rate、ASR、latency 不是同一量纲。
- 不把所有论文硬塞进一个绝对排行榜：backbone、judge、split、检索预算没有统一。
- 不用摘要级数字补齐缺失项：没有可核对主结果的论文标为“无统一 headline”。

## 未解决问题

- 需要把 LoCoMo / LongMemEval 的统一 backbone、judge、split 和检索预算写成最小实验协议。
- 需要复核部分未逐行抄录的 Table 2/3 数字。
- 需要补做 VikingMem、TiMem、RecMem、MRAgent、MAGMA 的同条件复现。
- 安全、效率和 utility 应保持三条独立榜单。

## 下一步

优先建立“同 benchmark + 同指标 + 同 backbone”的可比子表，再讨论跨论文 SOTA。
