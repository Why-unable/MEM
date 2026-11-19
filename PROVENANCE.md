# Provenance and Evidence Rules

## 1. 来源优先级

1. 官方 proceedings：OpenReview、ACL Anthology、AAAI OJS、PMLR、MLSys
2. 出版商 DOI：ACM、IEEE、Springer、Elsevier
3. Crossref
4. OpenAlex
5. Semantic Scholar
6. arXiv / 预印本
7. 个人笔记 / 模型总结

低优先级来源不能覆盖高优先级来源。

## 2. 每篇论文必须核验

- 标题
- 作者
- 年份
- venue
- 正式记录或官方 PDF
- DOI / arXiv / OpenReview / ACL Anthology / AAAI ID

## 3. 证据等级

| 等级 | 含义 |
|---|---|
| A | 官方 proceedings / DOI + 原文关键页 |
| B | 官方 PDF + 摘要 |
| C | 二次数据库记录 |
| D | 模型总结或未核验笔记 |

主地图默认至少 B；核心 claim 应达到 A。

## 4. 关系边

边类型：

- `extends`：明确扩展
- `related`：主题相关，但未必有引用关系
- `contrasts`：结论或假设冲突
- `applies`：方法/系统被应用
- `evaluates`：评测工作关系
- `evaluated-by`：被评测
- `risk`：安全/隐私风险
- `inspired-by`：明确影响

如果不知道关系类型，使用 `related`，不要伪造 `extends` 或 citation edge。

## 5. 模型推断

凡是模型生成但没有原文证据的内容，必须标记：

```text
status: inferred
confidence: low | medium | high
verified_by: human | official-source | none
```

## 6. 预印本

仅 arXiv 的工作进入：

```text
data/<topic>/preprints-excluded.md
```

确认正式发表后，补 venue/DOI 再进入主库。

## 7. 更新记录

每次大规模新增/修改论文或关系，需要更新：

- `CHANGELOG.md`（系统/仓库变化）
- `research-log/YYYY-MM-DD-*.md`（研究过程）
- `VENUE_AUDIT.md`（venue 核验）
