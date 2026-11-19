# 方案 A 安装与使用

方案 A 的目标是：**轻量、可控、可审计地建立个人论文研究地图**。

## 组成

1. **Scholar Literature Maps**：文献发现与分组。
2. **Research Nexus 思路**：Obsidian 中的 paper/topic/idea/journal 节点。
3. **OpenAlex MCP / Local Citation Network**：引文和作者数据。
4. **MEM 自己的脚本**：把论文元数据变成笔记、Canvas 和 research map。
5. **Zotero**：书目与 PDF 附件。

## 1. 打开 Obsidian Vault

用 Obsidian 打开：

```text
$MEM_ROOT/vault
```

建议先打开：

- `vault/90_System/Dashboard.md`
- `vault/20_Topics/Agent Memory 2025+.md`
- `vault/40_Maps/Agent Memory 2025+.canvas`

## 2. 安装外部工具（可选）

```bash
cd $MEM_ROOT
bash scripts/bootstrap_scheme_a.sh
```

脚本会把外部工具克隆到 `.tools/`，不修改你的全局 Codex 配置。

## 3. 使用 Scholar Literature Maps 的流程

对一个新主题：

1. 写下范围：对象、方法、时间、排除项。
2. 先将中文问题转成英文检索概念。
3. 先搜核心文献，再做受控邻域扩展。
4. 按“奠基 / 综述 / 方法 / 数据集 / 争议 / 最新进展”分组。
5. 只把可核验论文写入 `data/<topic>/papers.json`。
6. 运行校验和构建脚本。

## 4. 使用 Research Nexus 的流程

推荐节点类型：

- `paper`：一篇论文
- `topic`：一个研究主题
- `idea`：一个研究想法
- `journal`：研究日志

推荐关系类型：

- `related-to`
- `supports`
- `contradicts`
- `extends`
- `inspired-by`
- `summarized-by`

本仓库的 `scripts/build_research_map.py` 会生成符合这个结构的 Markdown 笔记和 Canvas。

## 5. 新增一个主题

```text
data/<topic>/
  papers.json
  edges.json
  queries.md
maps/<topic>/
  research-map.md
  research-map.json
  research-map.canvas
  papers.csv
```

然后运行：

```bash
python3 scripts/validate_mem.py \
  --papers data/<topic>/papers.json \
  --edges data/<topic>/edges.json

python3 scripts/build_research_map.py \
  --papers data/<topic>/papers.json \
  --edges data/<topic>/edges.json \
  --vault vault \
  --out maps/<topic> \
  --topic '<Topic Name>'
```

## 6. 当前案例

`Agent Memory 2025+` 已经包含：

- 36 篇正式发表论文
- 17 篇 CCF-A
- 8 篇 ICLR
- 6 篇 ACL Findings
- 3 篇 COLM
- 1 篇 MLSys
- 1 篇 ECAI
- 47 条概念关系

## 7. 下一步

- 绑定你的实际 Obsidian Vault 路径。
- 绑定 Zotero collection。
- 把 36 篇论文导入 Zotero。
- 逐篇补“关键方法 / 关键实验 / 局限 / 可复用点”。
- 从地图缺口生成 3–5 个研究问题。
