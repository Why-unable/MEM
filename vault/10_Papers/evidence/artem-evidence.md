---
type: evidence
paper_id: artem
title: "ARTEM: Enhancing Large Language Model Agents with Spatial-Temporal Episodic Memory"
status: evidence-checked
checked_at: 2026-11-27
source_pdf: "data/agent-memory-2025/pdfs/artem.pdf"
source_version: "AAAI 2026 conference paper"
pages_checked: "1-8"
mainline: "D"
tags:
  - evidence
  - mainline-d
  - episodic-memory
  - temporal-reasoning
---

# ARTEM 证据卡

## 结论先行

- ARTEM 把 episodic memory 做成 **spatial-temporal event**：LLM 抽取 temporal/spatial/entity/semantic 信息，再用 STEM 神经网络增量存储和检索。
- 它关注四类任务：partial cue retrieval、epistemic uncertainty detection、recent event identification、chronological recall。
- 在合成书 Synaptic Echoes（200 章、102,870 tokens）上，ARTEM Simple Recall **0.709**、Chronological **0.585**，并在 null query 上保持高 F1。

## 研究问题与定位

现有 RAG/ICL/fine-tuning 难以处理需要时间顺序的长期事件。ARTEM 要回答：

> 能否用空间-时间事件结构和增量神经记忆，支持长期 episodic recall 和 temporal reasoning？

## 方法拆解

### Event extraction

LLM 从文本中抽取：

- temporal markers
- spatial information
- entities
- semantic content

形成事件表示 `(t, s, ent, c)`。

### STEM

- Spatial-Temporal Episodic Memory：自组织神经网络。
- instance-based incremental learning。
- 多通道编码 temporal/spatial/entity/content。
- 支持部分线索检索、时间顺序回忆、近期事件识别、认知不确定性检测。

来源：PDF p.2-5，Method。

## 实验与关键数字

### 设置

- Benchmark：Episodic Memory Benchmark + 合成书 Synaptic Echoes（200 章、102,870 tokens）。
- Baselines：ICL、RAG、fine-tuning、多个 LLM（GPT-4o/4o-mini、Claude、o1/o3-mini、Gemini）。
- Metrics：Simple Recall F1、Chronological F1、null-query F1、epistemic uncertainty F1。

### 主要结果

| 指标 | ARTEM |
|---|---:|
| Simple Recall F1 | **0.709** |
| Chronological F1 | **0.585** |
| Null-query F1 | **0.95** |
| Temporal query F1 | **0.67** vs baseline 0.5 |

- 在 multi-event 场景中，STEM/ARTEM 明显优于标准 LLM memory。
- 在 confabulation detection 上 F1 约 0.66。

来源：PDF p.5-7，Table 3-4。

### 任务类型

- partial cue retrieval
- epistemic uncertainty detection
- recent event identification
- chronological recall

四类任务都覆盖，说明不是单一 QA。

来源：PDF p.1 abstract；p.5-6。

## 真正的新意

1. **空间-时间事件表示**：temporal/spatial/entity/semantic 四通道。
2. **STEM 增量学习**：不是一次性建图/向量库。
3. **null-query / epistemic uncertainty**：显式评估“不知道”。
4. **chronological recall**：时间顺序作为独立能力。

## 局限与威胁

- **依赖 LLM event extraction**：抽取错误会传播。
- **STEM 结构复杂**：训练/增量更新成本高。
- **评测主要是合成/标准化 episodic 任务**：真实开放世界未验证。
- **没有多模态**：视觉/音频扩展是未来工作。
- **没有显式遗忘/删除**：事件记忆持续增长。

## 与主线 D 的关系

- **EM-LLM**：事件分割 + 检索；ARTEM 用 STEM 神经记忆。
- **REMem**：gist/fact 图 + agentic retriever；ARTEM 用时空事件向量。
- **TiMem**：时间树；ARTEM 用 temporal channel + chronological recall。
- **TierMem**：压缩/raw 两层；ARTEM 不在粒度层做文章。

## 对 RQ1 的意义

ARTEM 说明 temporal reasoning 需要专门的 memory representation：

- 单纯 embedding 检索不足以处理时间顺序。
- RQ1 应把 temporal channel / chronological recall 作为独立能力。

## 可复用点

- `(t, s, ent, c)` 事件 schema。
- STEM 多通道增量记忆。
- null-query / epistemic uncertainty 评测。
- chronological recall 任务。
- 合成长书 benchmark。

## 成本

- STEM 增量学习成本未在摘要中量化。
- event extraction 需要 LLM 调用。
- 没有统一 token/latency/storage 表。

## 来源

- 本地 PDF：`data/agent-memory-2025/pdfs/artem.pdf`
- AAAI 2026（论文记录）
