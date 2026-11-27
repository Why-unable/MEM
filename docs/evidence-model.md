# Evidence Model

MEM 的证据层是 **一篇论文一个 evidence 文件**：

```text
vault/10_Papers/evidence/<paper-id>-evidence.md
```

自动生成的 `vault/10_Papers/<paper-id>.md` 只包含元数据、摘要和地图关系，不是证据卡。

## 为什么 1:1

- 主线综合不能替代论文级证据。
- 任何 claim 必须能追溯回具体论文、页码或表格。
- 多机协作时，单篇 evidence 文件比一个超大主线性文档更容易合并。
- 论文更新/撤稿/venue 修正时，只需要改对应 evidence 文件。

## 状态

| 状态 | 含义 |
|---|---|
| `queued` | 入口存在，尚未读全文 |
| `metadata-only` | 只核对 metadata/摘要 |
| `full-text-scan` | 已读方法/实验/局限，但未做页码级证据卡 |
| `evidence-checked` | 有页码级关键数字、局限、成本和 RQ 关系 |
| `verified` | 人工复核过来源、数字和引用 |

`queued` 不是“已完成证据”。不允许把摘要或主线综合标成 `evidence-checked`。

## 最低内容

1. 一句话定位
2. 研究问题
3. 记忆单元 / 数据结构
4. 写入、组织、检索、更新、遗忘
5. 训练方式（若适用）
6. 数据集、backbone、baseline、指标
7. 关键数字（带页码/表号）
8. 主要结论
9. 局限
10. 与主线其他论文的关系
11. 对 RQ1/RQ3 的意义
12. 可复用点
13. 成本：build / query / latency / storage
14. 待核对
15. 来源

## 索引

```bash
python3 scripts/build_evidence_index.py
```

生成：

```text
vault/10_Papers/evidence/INDEX.md
```

首次为缺失论文创建 queued 入口：

```bash
python3 scripts/build_evidence_index.py --create-missing
```

## 规则

- 不猜 DOI、venue、作者、数字。
- 关键数字必须回 PDF。
- 不同论文的指标不可直接横比。
- LLM-Judge 分数不是绝对正确率。
- 作者原话与分析判断必须分开。
- 不确定的内容进入“待核对”，不要伪装成结论。
