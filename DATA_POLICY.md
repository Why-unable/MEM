# Data Policy

## 1. 可以提交

- 论文元数据（标题、作者、年份、venue、DOI、官方 URL）
- 官方摘要
- 个人撰写的论文笔记与综合
- 概念关系
- 研究问题、决策、日志
- 脚本、schema、CI、配置模板

## 2. 不提交

- 版权 PDF
- Zotero `zotero.sqlite` / `fulltext.sqlite` / storage 附件
- API keys、token、cookie
- 个人 Zotero 私有导出（除非明确审查）
- 机器特定路径配置
- `.DS_Store`
- Obsidian workspace 状态

## 3. 大文件

默认不用 Git LFS。若未来需要提交自有数据：

- 先开 ADR
- 使用 Git LFS
- 记录许可证与来源
- 不要把第三方 PDF 当自有数据

## 4. 隐私

- 不提交个人在读论文的敏感批注，除非用户明确同意。
- Zotero 本地 API key 只放本机 `.env` 或凭据管理器。
- 私人 vault 路径可以出现在 `config/mem.config.json`，若仓库公开应迁移到 `config/mem.config.example.json`。

## 5. 版权

论文摘要与元数据用于研究索引。PDF 不进入仓库。引用原文时保持最小必要范围并附来源。

## 6. 数据生命周期

```text
检索候选
→ 00_Inbox
→ 核验
→ papers.json
→ 生成论文笔记
→ 主题综合
→ 研究问题
→ 实验/写作
```

## 7. 多机同步

每台机器只维护：

- 自己的 `.env`
- 自己的 Obsidian workspace
- 自己的 Zotero 数据库

共享：

- 论文元数据
- 笔记
- 关系
- 决策
- 研究日志
