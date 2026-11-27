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
- `vault/40_Maps/Agent Memory 2025+ Baseline Timeline.md`
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

`Agent Memory 2025+` 当前包含：

- 52 篇正式发表论文
- 86 条概念关系
- 27 篇 CCF-A
- 12 篇 Top-ICLR
- 7 篇 ACL Findings
- 3 篇 Top-COLM
- 1 篇 Top-MLSys
- 2 篇 CCF-B
- 52/52 逐篇 `evidence-checked`
- 52 篇时间化 baseline 记录
- 4 个 Zotero collection，52 条书目 + 52 条 importer notes

核心入口：

```text
vault/90_System/Dashboard.md
vault/20_Topics/Agent Memory 2025+.md
vault/20_Topics/Mainline Overview.md
vault/10_Papers/evidence/INDEX.md
vault/40_Maps/Agent Memory 2025+ Baseline Timeline.md
maps/agent-memory-2025/EXPERIMENT_LANDSCAPE.md
个人理解/路线分类.md
```

## 7. 多机部署

第二台机器按以下顺序接手：

```bash
git clone git@github.com:Why-unable/MEM.git
cd MEM
git fetch origin
git switch research/agent-memory-evidence
make check
```

然后：

1. 打开本机 `MEM/vault/` 到 Obsidian。
2. 确认 Zotero 52 条书目，不重复导入已有 batch。
3. 阅读 `docs/multi-machine-playbook.md` 与 `CONTRIBUTING.md`。
4. 运行 `make docs-check` 验收文档与数据一致。

## 8. 下一步

- 建立 `CLAIMS.md`：claim–evidence–confidence。
- 建立 RQ1 统一实验协议。
- 对 52 张 evidence 做 `verified` 人工抽查。
- 迁移 per-paper 数据分片，降低多机冲突。
- 回填 Zotero item key 与合法可获得的本机 PDF 附件。
