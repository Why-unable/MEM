---
type: evidence
paper_id: memgas
title: "From Single to Multi-Granularity: Toward Long-Term Memory Association and Selection of Conversational Agents"
status: evidence-checked
checked_at: 2026-11-26
source_pdf: "data/agent-memory-2025/pdfs/memgas.pdf"
source_version: "ICLR 2026 conference paper; OpenReview i2yIvZARnG"
pages_checked: "1-10, 22-23"
tags:
  - evidence
  - mainline-a
  - agent-memory
  - multi-granularity
---

# MemGAS 证据卡

## 结论先行

- MemGAS 的核心是 **多粒度记忆 + 自适应粒度选择**：同一条对话同时保留 session、turn、summary、keyword 四种粒度。
- 它不是简单地“多存几种表示”，而是用 GMM 建立跨记忆关联，用 entropy router 选择当前 query 最适合的粒度，再用 PPR 做图检索。
- 在 LongMemEval 上它明显优于 full-history 和 A-Mem；但在 LoCoMo 的 LLM-Judge 上仍低于 HippoRAG 2，说明“多粒度”不是 universal win。

## 研究问题与定位

现有长期对话记忆系统通常使用单一粒度：要么按 session/chunk 检索，要么按 turn 检索。单一粒度的问题是：

- 细粒度（turn）保留细节但噪声多；
- 粗粒度（session/summary）覆盖完整但可能丢失关键事实；
- 固定粒度无法适配不同 query。

MemGAS 的目标是让系统在 query 到来时动态选择“应该看多细”。

## 方法拆解

### 多粒度记忆单元

每条 session 被表示为：

```text
M_i = { S_i, T_i, U_i, K_i }
```

- `S_i`：session 原文
- `T_i`：turn 级对话
- `U_i`：LLM 生成的 session summary
- `K_i`：LLM 生成的关键词

来源：PDF p.3，Eq. 1-2。

### 关联构建

- 对每个粒度分别编码为 dense vector。
- 新记忆与历史记忆在每个粒度上计算相似度。
- 用 Gaussian Mixture Model 把相似度向量聚类为 accept / reject 两个集合。
- accept set 形成新记忆与历史记忆之间的关联边。

来源：PDF p.4，Section 2.2。

### 自适应路由

对每个粒度 `g`：

1. 计算 query 与所有记忆的相似度分布。
2. 计算该分布的 Shannon entropy。
3. 用 inverse entropy 归一化得到粒度权重：

```text
w_g = (1/H_g) / sum_g'(1/H_g')
```

4. 低熵（更确定）的粒度获得更高权重。

来源：PDF p.4-5，Eq. 3-4。

### 检索与过滤

- 用 router 权重初始化每个粒度节点的 relevance score。
- 在 multi-granularity association graph 上运行 Personalized PageRank。
- 取 top-k 节点作为候选上下文。
- 用 LLM 做 redundancy filtering，去掉重复或无关内容。

来源：PDF p.5，Section 2.4。

## 存储与使用

- **怎么存**：同一条对话同时保留四种粒度：整段 session、逐轮 turn、session 摘要、关键词。它不是四份独立记忆，而是同一记忆的四种看法。
- **怎么连**：新记忆加入时，系统判断哪些历史记忆与它相关，并把相关粒度连接起来，形成多粒度关联图。
- **怎么用**：query 先判断自己更需要细节还是概括，再决定四种粒度的使用比例；然后沿关联图扩散，取回相关记忆，最后过滤重复和噪声。
- **怎么更新**：新 session 会生成新的多粒度记录，并与历史记录建立关联；旧记录本身不被重写。

**一句话**：MemGAS 存的是“同一记忆的多种粗细版本”；检索是“先选粒度，再沿关联找证据”。

### 一个端到端例子（示意）

场景：用户在多轮对话中持续提到自己完成的在线课程。

**存储**

- session 1：用户说“我在 Coursera 完成了两门课”。
- 同一段记忆还保留：逐轮原话、session 摘要、关键词“Coursera、在线课程”。
- session 2：用户后来说“我又在 edX 完成了三门课”。

**连接**

- session 2 加入时，系统发现它与 session 1 都在谈“在线课程完成情况”。
- 两个 session 的摘要、关键词和原始对话会建立多粒度关联。
- 旧记录不被改写，只是与新记录连起来。

**更新**

- 新 session 生成新的四粒度记忆：整段 session、逐轮对话、摘要、关键词。
- 新记忆与相关的历史 session 建立关联。
- 以后新增课程记录也按同样方式追加和连接。

**检索**

query：“我一共完成了多少门在线课程？”

- 系统判断：这个问题更需要“摘要/整段”而不是某一轮原话。
- 从 session 1 和 session 2 的摘要/整段中取证据。
- 沿关联图把两段记忆都找出来，过滤重复内容。
- 组合得到答案：2 + 3 = 5 门。

**这个例子说明**：MemGAS 不是只存一份摘要，也不是只存逐轮对话；它把同一段经历保留成多种粗细，检索时先决定看多细，再把相关记忆连起来。


## 实验与关键数字

### 设置

- 4 个 benchmark：LoCoMo、Long-MT-Bench+、LongMemEval-s、LongMemEval-m。
- Generator：GPT-4o-mini。
- 检索 backbone：Contriever（baseline 对比中统一）。
- 指标：GPT4o-as-Judge、F1、BLEU-4、ROUGE、BERTScore、Recall@k、NDCG@k。
- Training-free。

### QA 结果（GPT4o-J）

| Benchmark | Full History | A-Mem | HippoRAG 2 | MemGAS |
|---|---:|---:|---:|---:|
| LongMemEval-s | 50.60 | 55.60 | 57.60 | **60.20** |
| LongMemEval-m | 12.20 | — | — | **45.40** |
| LoCoMo | 33.43 | 40.81 | **45.62** | 41.07 |
| LongMTBench+ | 67.44 | 65.73 | — | **69.44** |

来源：PDF p.7, Table 1。

重要反例：**LoCoMo 上 MemGAS 的 GPT4o-J 低于 HippoRAG 2**（41.07 vs 45.62），说明多粒度关联并非在所有 benchmark 上都占优。

### 检索结果

| Benchmark | 方法 | Recall@3 | NDCG@3 |
|---|---|---:|---:|
| LongMemEval-s | HippoRAG 2 | 75.53 | 85.44 |
| LongMemEval-s | **MemGAS** | **78.51** | **86.83** |
| LoCoMo | HippoRAG 2 | 56.60 | 58.37 |
| LoCoMo | **MemGAS** | **57.30** | **58.76** |

来源：PDF p.8, Table 2。

### 成本

LongMemEval-s：

- MemGAS：8,829 tokens/query，2.55 秒/query。
- Full History：103,137 tokens/query，9.39 秒/query。
- A-Mem：9,018 tokens/query，2.59 秒/query。
- HippoRAG 2：8,530 tokens/query，4.51 秒/query。

来源：PDF p.7, Table 1。

记忆构建成本（LongMemEval-s，PDF p.23, Table 10）：

- MemGAS 输入 52.9M tokens（100%）。
- HippoRAG 2 输入 111.1M tokens（210%）。
- RAPTOR 输入 62.6M tokens（118%）。
- SeCom 输入 106.2M tokens（200%）。
- RecurSum 输入 58.3M tokens（110%）。

额外内存（PDF p.23, Table 11）：

- Raw memory：266MB。
- Summary memory：16.2MB。
- Keyword memory：10.8MB。
- 总额外约 27MB，约为 raw memory 的 10%。

### 消融（LongMemEval-s）

| 配置 | GPT4o-J | F1 | R@3 |
|---|---:|---:|---:|
| MemGAS | **60.20** | **20.38** | **78.51** |
| w/o GMM | 57.20 | 19.49 | 76.38 |
| w/o PPR | 56.60 | 19.76 | 75.96 |
| w/o Memory Association | 56.80 | 17.69 | 74.89 |
| w/o Router | 56.60 | 18.88 | 75.53 |
| w/o All | 55.40 | 13.78 | 71.06 |

来源：PDF p.8, Table 3。

模块额外延迟很小：QA 延迟最多增加 0.0191 秒，检索延迟最多增加 0.0079 秒；LLM API 调用占端到端延迟 98% 以上。

## 成本分析

- **报告成本**：构建 52.9M input / 5.2M output tokens；8,829 tokens/query；2.55s/query；额外约 27MB 内存。
- **横向对比**：full-history 为 103,137 tokens / 9.39s；A-Mem 为 9,018 / 2.59s；HippoRAG 2 为 8,530 / 4.51s。
- **成本位置**：构建重、查询轻；按 token 粗略估算，约 560 次查询后才开始回本。
- **对比判断**：适合长历史、多次查询；短对话或一次性查询不划算，且 LoCoMo 上成本优势没有转化为 judge 优势。

## 真正的新意

1. **同一记忆的多粒度表示**：不是在不同系统间切换粒度，而是在同一个记忆库里同时维护四种粒度。
2. **entropy-based router**：用 query 对各粒度匹配分布的不确定性来选择粒度，而不是固定 top-k。
3. **GMM 关联构建**：把“新记忆是否与旧记忆相关”变成概率聚类问题，而不是单一阈值。
4. **PPR + LLM filter**：图传播负责召回，LLM 负责去噪，分工清晰。

## 局限与威胁

- 论文没有独立的 Limitations 章节；以下是分析判断，不是作者原话。
- **依赖 LLM 生成 summary / keywords**：元数据质量会直接影响路由器。
- **GMM / entropy / PPR 都有超参数**：不同数据集可能需要重新校准。
- **LoCoMo 上不如 HippoRAG 2**：说明多粒度不是 universal improvement，benchmark 和 judge 选择会改变结论。
- **构建成本不低**：52.9M input tokens；虽然低于 HippoRAG 2，但仍是显著成本。
- **没有显式遗忘/删除/权限机制**：LLM filter 是查询时过滤，不是记忆治理。
- **评测主要是对话记忆**：未覆盖多 agent 共享、工具使用、多模态。

## 与主线 A 其他论文的关系

- **A-Mem**：A-Mem 是单一粒度的原子笔记；MemGAS 把“粒度”本身变成可选择对象。
- **MAGMA**：MAGMA 选择“关系类型”，MemGAS 选择“记忆粒度”；两者是正交维度。
- **G-Memory**：G-Memory 的层次是组织层（insight/query/interaction），MemGAS 的层次是语义粒度（session/turn/summary/keyword）。
- **MRAgent**：MemGAS 仍是单轮 router + PPR；MRAgent 把检索变成多轮 active reconstruction。

## 对 RQ1 的意义

MemGAS 提供了“结构”的另一种定义：**结构不只是图关系，也包括粒度层级**。

- 支持：在 LongMemEval 上，多粒度结构显著优于 full-history 和 A-Mem，且 token 成本低一个数量级。
- 反例：LoCoMo 上 HippoRAG 2 更高，说明“更多结构”不一定更好；任务/评测差异可能比架构差异更大。
- 对 RQ1 的启示：比较结构记忆 vs 长上下文时，必须把 **粒度选择** 作为独立变量，否则会把“多粒度”误当成“图结构”的收益。

## 可复用点

- session / turn / summary / keyword 四粒度 schema。
- GMM accept/reject 关联构建。
- inverse entropy router。
- PPR + top-k + LLM redundancy filter。
- 构建 token、查询 token、额外 RAM、延迟四类成本报告。
- 用 “w/o GMM / PPR / MA / Router” 做模块级消融。

## 待核对

- [ ] 核对 LongMemEval-m 中 A-Mem / HippoRAG 2 缺失值的原因。
- [ ] 核对 LoCoMo 上 MemGAS 低于 HippoRAG 2 的具体分类差异。
- [ ] 检查代码仓库与论文版本是否一致。
- [ ] 评估 GMM 聚类的稳定性与初始化敏感性。

## 来源

- 本地 PDF：`data/agent-memory-2025/pdfs/memgas.pdf`
- OpenReview：https://openreview.net/forum?id=i2yIvZARnG
- ICLR Proceedings PDF：https://proceedings.iclr.cc/paper_files/paper/2026/file/93e444b4a1a64815631c3c74977ee200-Paper-Conference.pdf
- arXiv：https://arxiv.org/abs/2505.19549
