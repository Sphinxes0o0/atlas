# AGENT.md — Atlas Exercise Science Wiki

> 运动科学知识库维护手册。LLM agent 根据此文件维护 wiki。
> 从 pyramid（通用技术知识库）拆分而来，专注运动科学/运动健康领域。

---

## 领域

运动科学 (Exercise Science)：运动生理学、训练方法、跑步专项、营养补剂、生物力学、可穿戴技术、人群专项研究。

**核心来源：** relay-neuron 仓库的运动科学文献分析。

---

## 目录结构

```
atlas/
├── wiki/                     # Obsidian Vault
│   ├── entities/             # 概念页面（按子域组织）
│   │   └── exercise-science/
│   │       ├── physiology/   # 运动生理学
│   │       ├── training/     # 训练方法
│   │       ├── running/      # 跑步专项
│   │       ├── nutrition/    # 营养
│   │       ├── supplements/  # 补剂（姜黄素/辅酶Q10）
│   │       ├── biomechanics/ # 生物力学
│   │       ├── technology/   # 可穿戴技术
│   │       ├── population/   # 人群专项
│   │       ├── obesity/      # 肥胖与代谢
│   │       ├── health/       # 运动健康
│   │       └── recovery/     # 恢复
│   ├── sources/              # 源文档摘要
│   ├── attachments/          # 图片/附件
│   └── temporal/journal/     # 日记
│
├── AGENT.md                  # 本文件
└── index.md                  # 全局导航
```

---

## 页面类型规范

### Entity 页面

```yaml
---
type: entity
tags: [exercise-science, <subdomain>]
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: [source-name]
---
```

### Source 页面

```yaml
---
type: source
source-type: github | pdf | web
title: "标题"
created: YYYY-MM-DD
summary: "一句话总结"
---
```

### Index 页面（模块导航）

```yaml
---
type: index
tags: [exercise-science, <subdomain>]
created: YYYY-MM-DD
---
```

---

## Ingest 工作流

1. 用户将新来源放入 relay-neuron 或指定 PDF/网页
2. LLM 读取来源内容
3. 在 `wiki/sources/` 创建摘要页
4. 在 `wiki/entities/exercise-science/<subdomain>/` 创建或更新实体页
5. 更新对应 `*-index.md` 模块导航
6. 更新 `wiki/home.md` 全局首页
7. 追加 `wiki/log.md`

---

## 命名规范

- Entity: `wiki/entities/exercise-science/<subdomain>/<slug>.md`
- Source: `wiki/sources/<source-name>.md`
- Index: `wiki/<subdomain>-index.md`

---

## 交叉引用

- 每个 entity 页面至少 2 条 [[wikilinks]] 指向其他 entity
- 相关 entity 互链
- 禁止仅靠 index 串联的星形结构

---

## Obsidian 配套

- Vault 根目录：`wiki/`
- 插件推荐：Templater, Dataview, QuickAdd

---

## 理念

> "LLM 负责总结、交叉引用、保持一致。人负责筛选来源、提出好问题、思考意义。"
>
> Atlas — 解剖学寰椎（支撑身体）、图集（知识汇编）、阿特拉斯神（力量象征）。
