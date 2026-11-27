---
type: evidence
paper_id: hippocampus
title: "Hippocampus: An Efficient and Scalable Memory Module for Agentic AI"
status: evidence-checked
checked_at: 2026-11-27
source_pdf: "data/agent-memory-2025/pdfs/hippocampus.pdf"
source_version: "MLSys 2026 conference paper"
pages_checked: "1-10"
mainline: "C"
tags:
  - evidence
  - mainline-c
  - system
  - retrieval
  - compression
---

# Hippocampus 证据卡

## 结论先行

- Hippocampus 的核心是 **压缩域检索**：用 compact binary signatures 做语义搜索，用 lossless token-ID streams 做精确内容重构。
- Dynamic Wavelet Matrix (DWM) 同时压缩/索引两路，避免 dense vector 或 graph traversal 的高延迟。
- 论文报告最高 **31x** 检索加速、**14x** per-query token 降低，同时保持有竞争力的 accuracy。

## 研究问题与定位

现有 memory systems 依赖 dense vector、KG traversal 或 hybrid，检索延迟高、存储扩展差。Hippocampus 要回答：

> 能否在压缩域直接做高效检索，同时保留原始 token 以便无损重构？

## 方法拆解

### 两路表示

1. **Compact binary signatures**：用于语义近似搜索。
2. **Lossless token-ID streams**：用于精确内容重构。

### Dynamic Wavelet Matrix

- 同时压缩和索引两路数据。
- 支持在压缩域做搜索。
- 对固定 tokenizer vocabulary，storage 随 memory size 线性增长。

### 检索

- query 转成 binary signature/token 表示。
- 在 DWM 上做近似搜索。
- 命中的 entry 通过 token-ID stream 重构原文。

来源：PDF p.1-5，Method。

## 实验与关键数字

### 设置

- Benchmarks：LoCoMo、LongMemEval-S（以及 LongMemEval-M 附录）。
- Baselines：ReadAgent、MemoryBank、MemGPT、A-Mem、MemoryOS、MemOS 等。
- Metrics：F1/accuracy、end-to-end retrieval latency、avg token consumption、storage。

### 主要结果

- 检索加速：**1.1x–31.5x**。
- per-query token footprint：**1.1x–14.5x** 降低。
- LoCoMo 平均读取约 **1.3K tokens/query**。
- accuracy 与 dense/graph memory systems 有竞争力；论文报告在部分任务上超过 MemGPT 等。

来源：PDF p.1 abstract；p.7-9，Table 1-2，Figure 8-11。

### 成本位置

- 主要节省在 search latency（dense vector similarity 常占 80%+ latency）。
- token 降低来自压缩签名 + 按需重构 token-ID。
- storage 线性增长，适合长历史。

来源：PDF p.3-5，p.7-9。

## 真正的新意

1. **压缩域检索**：不是先解压/embedding 再检索。
2. **binary signature + token-ID stream 双路**：近似搜索和精确重构分开。
3. **DWM 数据结构**：把压缩和索引合并。
4. **系统级成本分析**：latency、tokens、storage 一起报告。

## 局限与威胁

- **依赖 tokenizer/vocabulary**：固定 tokenizer 下 storage 线性；换 tokenizer 需要重建。
- **近似搜索有精度损失**：binary signatures 不是 dense embedding，可能影响召回。
- **系统实现复杂**：DWM + 双路表示，工程门槛高。
- **主要是检索/QA**：没有 action-coupled、多模态、安全。
- **没有显式遗忘/删除**：压缩存储仍随历史增长。

## 与主线 C 的关系

- **Mem0/MemoryOS**：Hippocampus 不依赖 dense vector/graph，走压缩索引路线。
- **LightMem/SimpleMem**：都关注压缩，但 Hippocampus 更偏底层数据结构。
- **EverMemOS**：EverMemOS 优化生命周期；Hippocampus 优化检索 substrate。
- **TierMem**：TierMem 用 summary/raw 两层；Hippocampus 用 binary/token-ID 两路。

## 对 RQ1 的意义

Hippocampus 提供了“检索 substrate”维度的证据：

- 结构记忆的成本不仅取决于图/摘要，还取决于底层索引。
- RQ1 应报告 retrieval latency 和 token footprint，而不只是 accuracy。

## 可复用点

- binary signature + lossless token-ID 双路表示。
- Dynamic Wavelet Matrix 压缩索引。
- 压缩域搜索 + 按需重构。
- latency/token/storage 三轴报告。

## 成本

- 检索加速最高 31x。
- token footprint 最高 14x 降低。
- LoCoMo 平均约 1.3K tokens/query。
- build time / storage 细节见附录（待核对）。

## 来源

- 本地 PDF：`data/agent-memory-2025/pdfs/hippocampus.pdf`
- MLSys 2026（论文记录）
