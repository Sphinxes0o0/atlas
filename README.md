# Atlas — 运动科学知识库

Atlas 统一维护 Relay Neuron 的原始研究资料与 Obsidian 知识库。

## 阅读入口

- [知识库首页](wiki/home.md)：按领域浏览概念、来源摘要和主题索引。
- [研究资料目录](raw/github/relay-neuron/research/README.md)：浏览原始研究文档。
- [研究任务清单](raw/github/relay-neuron/RESEARCH_MASTER_LIST.md)：查看研究任务与完成情况。
- [Relay Neuron 介绍](raw/github/relay-neuron/README.md)。
- [维护指南](CLAUDE.md)。

## 目录与维护

- `raw/github/relay-neuron/`：Relay Neuron 原始资料及其配套配置。后续研究直接在此维护，无需再向独立仓库同步。
- `wiki/`：概念页面、来源摘要、交叉引用与导航；在 Obsidian 中将此目录作为 Vault 打开。
- `scripts/`：资料导入、覆盖率和知识库健康检查工具。

原始资料更新后，按维护指南同步相关知识库摘要与概念页。资料导入不代表已重新验证文献，也不会自动更新既有摘要。

```sh
python3 scripts/atlas_health.py
python3 scripts/ingest_relay_neuron.py --dry-run --batch raw/github/relay-neuron/research/
```

## 仓库合并记录

2026-11-15 将 Relay Neuron 的 `main` 合入 Atlas，并以双父提交保留两边 `main` 可达的提交历史。原始资料沿用已有目录，避免重复副本；原仓库保持可访问。

- Atlas 合并前版本：`5611edbecf78d58a35cdf9d6ea02470a99729319`
- Relay Neuron 导入版本：`8374267146558e82b4177352f344fe8eb08d6ec4`

本次新增 45 个文件、更新 58 个文件，3,097 个相同文件保持原样。Atlas 已有的 5 个额外文件继续保留（4 个配套资源和 1 个导入测试样例）。已有知识库页面和摘要保留，后续可单独开展内容复核。

此次合并涵盖 `main` 分支的文件和提交历史；其他分支、Issues、Discussions 及仓库设置不属于本次文件合并范围。
