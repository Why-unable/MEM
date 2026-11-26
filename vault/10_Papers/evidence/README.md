# Evidence Notes

本目录存放**基于论文全文**的证据卡，不放摘要级读书笔记。

## 为什么单独放

`vault/10_Papers/<paper-id>.md` 由 `scripts/build_research_map.py` 生成，重建时会覆盖。证据卡是人工/AI 阅读后的研究资产，不能放在生成文件里。

## 当前覆盖

- `amem-evidence.md`
- `gmemory-evidence.md`
- `magma-evidence.md`
- `memgas-evidence.md`
- `reconstructed-evidence.md`

## 证据卡最低要求

每张卡至少包含：

1. 结论先行
2. 研究问题与定位
3. 方法拆解：写入 / 组织 / 检索 / 更新 / 遗忘
4. 实验设置与关键数字
5. 真正的新意
6. 局限与威胁
7. 与主线其他论文的关系
8. 对 RQ1/RQ3 的意义
9. 可复用点
10. 待核对
11. 来源与页码

## 证据规则

- 关键数字必须标 PDF 页码或表格编号。
- 区分作者原话与分析判断。
- 正式论文与 arXiv 版本必须注明。
- 不同论文的指标不可直接横比。
- LLM-Judge 分数不能当作绝对正确率。
- 不确定的元数据写入“待核对”，不要猜。

## 命名

```text
<paper-id>-evidence.md
```

## 入口

- 主线综合：[[20_Topics/Mainline A - Memory Architecture]]
- 主题页：[[20_Topics/Agent Memory 2025+]]
