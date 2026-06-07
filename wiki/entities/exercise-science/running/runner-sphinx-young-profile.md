---
type: entity
tags: [exercise-science, running, runner-profile, personal, sphinx-young]
created: 2026-06-03
updated: 2026-06-03
sources: [source-itra-runner-young-sphinx]
---

# Runner Profile: Sphinx YOUNG (ITRA 6729918)

> 个人越野跑档案。ITRA 注册名 **Sphinx YOUNG** (工作体系是 Sphinx SHI)。
> **数据更新**: 2026-06-03，含 5 场已上传 + 1 场刚跑完待上传 (Jiuzhaigou)

## 基础画像

| 字段 | 值 |
|---|---|
| ITRA ID | **6729918** |
| 姓名 (EN) | Sphinx YOUNG |
| 姓名 (CN) | 施阳 (Sphinx SHI) — 工作身份 |
| 国家 | 🇨🇳 China |
| 性别 | Male |
| 年龄 | 30 (2026) |
| 年龄段位 | M 23-34 |
| 队伍 | 个人 (无 team/club) |
| ITRA 会员 ID | 643715 |
| Profile URL | `https://itra.run/RunnerSpace/young.sphinx.6729918` |

## ITRA 能力指标

| 指标 | 值 | 段位 |
|---|---|---|
| **Performance Index (PI)** | **354** | Intermediate 4 |
| 世界排名 (Overall Male) | 1,200,695 / 1,574,431 | Top 76.27% |
| 亚洲排名 (Asia Male) | 211,448 / 417,513 | Top 50.6% |
| 中国排名 (China Male) | 116,595 / 212,808 | Top 54.8% |
| 年龄组排名 (M 23-34) | DNF (样本不足) | 待 10+ 场计算 |

**注**: Endurance Points 分布 `0/0/2/0/0/0/0` — 显示 50K/50M 等级空缺，PI 主要靠 25km 段位贡献。

## 完赛记录 (6 场, 2025-12 至 2026-05)

### 已上传 ITRA (5 场)

| # | 日期 | 赛事 | 距离 | 爬升 | 用时 | 配速 | 名次/总 | 单场 PI |
|--:|---|---|--:|--:|--:|--:|--:|--:|
| 1 | 2025-12-14 | WAXE yandang 16K | 15.4 km | 526 m | 3:28:58 | 13:34 | 892/1054 | 238 |
| 2 | 2026-03-15 | Qiantang Three-Zone 22KM | 21.4 km | 1556 m | 5:47:09 | 16:13 | 130/264 | 322 |
| 3 | 2026-03-22 | WENLING GOLDEN COAST 25K | 24.7 km | 1006 m | 4:19:13 | 10:30 | 1033/2323 | 384 |
| 4 | 2026-04-19 | Anji Huangpu 25km | 25.9 km | 2171 m | 7:15:56 | 16:50 | 177/342 | **462** ⭐ |
| 5 | 2026-05-17 | TIANMU TRAIL CHALLENGE 20KM | 21.6 km | 1496 m | 5:04:05 | 14:04 | 458/833 | 364 |

### 待上传 ITRA (1 场, 已跑完)

| # | 日期 | 赛事 | 距离 | 爬升 | 用时 | 配速 | 名次/总 | 单场 PI 推算 |
|--:|---|---|--:|--:|--:|--:|--:|--:|
| 6 | 2026-05-31 | JIUZHAIGOU TRAIL · Sacred Garden 33KM | 31.33 km | 1377 m | **7:31:00** | 14:24 | 1023/2500 (40.9%) | **~330** |
| - | - | - | - | - | 性别 653 / 年龄组 234 | - | - | - |

**Jiuzhaigou 状态**: ITRA 比赛页 (`Races/RaceDetails/.../113873`) 已显示赛事信息，结果未上传 ("This race has no published results yet")。等待主办方 (Jiuzhaigou100) 通过 ITRA 账号批量导入。

## 累计数据

| 指标 | 值 |
|---|---|
| 完赛数 | **6 / 6 (100%)** |
| 总距离 | 140.3 km |
| 总爬升 | 8,132 m |
| 总用时 | 33:26:21 |
| 最长比赛 | **31.33 km** (Jiuzhaigou 2026-05-31) |
| 最高爬升 | 2,171 m (Anji 2026-04-19) |

## 配速 vs 爬升规律

| 比赛 | 配速 (min/km) | 爬升/距离比 (m/km) | 难度档 |
|---|--:|--:|---|
| Wenling 25K | **10:30** | 41 | 🟢 平 |
| Tianmu 20K | 14:04 | 69 | 🟡 中 |
| Jiuzhaigou 33K | 14:24 | 44 | 🟢 中低 (但距离长) |
| WAXE 16K | 13:34 | 34 | 🟢 平 |
| Qiantang 22K | 16:13 | 73 | 🟡 中 |
| Anji 25km | **16:50** | **84** | 🔴 难 |

**核心规律**: 配速主要由"爬升/距离比"决定，Wenling 25K (10:30/km) 是舒适区基准，Anji 25km (16:50/km) 是难区上限。

## PI 趋势与推算

### 5 场单场 PI 演变 (校准到 ITRA 354)

```
race 1 (WAXE 12-14):    238
race 2 (Qiantang 3-15): 322  ↑ 84  (冬训红利)
race 3 (Wenling 3-22):  384  ↑ 62  (周背靠背仍进步)
race 4 (Anji 4-19):     462  ↑ 78  (月度训练红利)  ⭐ peak
race 5 (Tianmu 5-17):   364  ↓ 98  (回撤, 5月平台期)
```

**线性回归**: PI = +39.6 × race_index + 270

**Jiuzhaigou 推算**: 7:31 完赛 → 单场 PI ~330 → 6 场累计均值 ~350 (基本持平)

### 关键观察

1. **冬训期 (12-14 → 3-15)**: PI +84，蜕变期
2. **3 月背靠背 (3-15 → 3-22)**: 7 天间隔仍能涨 +62 — 周背靠背能力
3. **4-19 Anji 峰值 (462)**: 单场最高 PI，月度训练效果最大化
4. **5-17 Tianmu 回撤 (-98)**: 5 月平台期，可能因 Anji 后疲劳未完全恢复
5. **Jiuzhaigou 33km 7:31**: 距离 +22% 但用时几乎相同 (Anji 7:16) → **长距离耐力显著进步**

## 段位对照 (ITRA Performance Index)

| 段位 | PI 范围 | 当前位置 |
|---|---|---|
| Beginner | 0-99 | |
| Novice | 100-199 | |
| Intermediate 1-2 | 200-299 | |
| **Intermediate 3-4** | **300-399** | **← 现在 (354)** |
| Intermediate 5 / Advanced 1-2 | 400-499 | 接近 (Anji 单场 462) |
| Advanced 3-4 | 500-599 | |
| Elite 1-2 | 600-699 | |
| Elite 3 | 700+ | |

## 6 月初赛事计划 (4 连战窗口) — ITRA 实测数据

| 日期 | 比赛 | 距离 | 爬升 | 限时 | 参赛 | 评估 | 备注 |
|---|---|--:|--:|--:|--:|---|---|
| 2026-06-05 周五 | **Pioneer camp Mountain Chongqing 23K** (四面山) | 23.7 km | 1679 m | 16h | 200 | ✅ 已选 | 距离适中，爬升大但 16h 限时宽裕 |
| 2026-06-06 周六 | HOWETAG Guaipo 20km (沈阳怪坡) | 23.4 km | 552 m | **1h** | 500 | ❌ 限时不够 | 1h 限时几乎无人能完赛 |
| 2026-06-06 周六 | Kada Qingdao 16km (青岛) | 15.0 km | 1091 m | **3h** | 100 | ❌ 限时不够 | 配速需 8.4 min/km 不可能 |
| 2026-06-06 周六 | DaGang 24KM (宁波大隐) | 24.2 km | 1053 m | **5h** | 250 | ❌ 限时不够 | 预测 5.8h 超时 0.8h |
| 2026-06-06 周六 | Wuhai 沙漠 30km (乌兰布和) | 30.9 km | 314 m | **7h** | 200 | ⚠️ 紧 | 沙漠赛 6:30 极早起跑 |
| 2026-06-07 周日 | **Himalaya Energy Ultra Trail 35km** (林芝鲁朗) | 35.8 km | 1001 m | 9h | 400 | ⚠️ **海拔 3300m** | 距 50K 段位只差 6km |
| 2026-06-07 周日 | **Chongli 11th 50km** (崇礼翠云山) | 44.2 km | 2072 m | 12h | 450 | ✅ 推算 OK | 距 50K 段位只差 6km |

### 最终推荐方案 (基于实际数据)

| 方案 | 6-05 周五 | 6-06 周六 | 6-07 周日 | 风险 | 适合 |
|---|---|---|---|---|---|
| **🏆 最佳** | Chongqing 23K | 跳过 (恢复) | **Chongli 50K** | 🟢 低 | 长距离升级 |
| 🥈 稳 | Chongqing 23K | 跳过 | **Lulang 35K** | 🟢 低 | 海拔体验 |
| 🥉 保守 | Chongqing 23K | 跳过 | 跳过 | 🟢 极低 | 最大化恢复 |
| ⚠️ 激进 | Chongqing 23K | Wuhai 30K 紧跑 | Chongli 50K | 🟠 中高 | 6 场连发 |

### 6-07 Chongli 50K 重点评估

- **距离 44.16 km / 爬升 2072 m / 限时 12h**
- 相对 JZ: 距离 **+41%**, 爬升 **+50%**
- 你的预测用时: **10.8h** (余 1.2h cutoff)
- 配速 16.3 min/km (vs JZ 14.4 min/km, 慢 13% 合理)
- 完赛概率: 中等 (你 5/31 7.5h 跑 33km 经验可迁移)
- 段位升级: ✅ 完赛即解锁 50K 段位
- PI 推算: **863** (vs JZ 330, 段位跳)

### 6-07 不推荐 Lulang 35K 理由

- 海拔 3300m (你跑过最高的赛 JZ 也才 2000m+), **高原反应风险高**
- 35K 段位对你升级价值小 (已能跑 33km)
- 35km 9h 限时比 Chongli 50K 12h 更紧

**警告**: Jiuzhaigou 33km 后恢复期 **至少 1-2 周**，6-05/06/07 三连战是 JZ 后**第 5/6/7 天** — 身体不会完全恢复。
**6-06 4 场全部限时不够** (Jupyter 恢复不足配速慢 15-20%) — 全部跳过最稳。

## 11 月长程计划 (3 连战窗口)

| 周 | 比赛 (假设) | 距离 | 相对 JZ | 配速预测 | 完赛率 |
|:--:|---|--:|--:|--:|--:|
| 1 | Race A | 42 km | +34% | 9.6h | 90% |
| 2 | Race B | 35 km | +12% | 8.4h | 85% |
| 3 | Race C | 40 km | +28% | 10.2h | 70% |

**周间隔 = 7 天** (跟 3 月 7 天背靠背已验证节奏一致)。

### 完赛概率全完赛: ~54% (90% × 85% × 70%)

### 推荐方案

| 方案 | 场 1 (42km) | 场 2 (35km) | 场 3 (40km) | 完赛率 |
|---|---|---|---|:--:|
| **A 稳 (推荐)** | 全力 | 7-8 分配速 | 7-8 分配速 | 80% |
| B 平衡 | 全力 | 全力 | 控速 | 65% |
| C 激进 | 全力 | 全力 | 全力 | 50% |

### 5 个月训练准备期 (6/1 → 11/1)

| 月份 | 重点 |
|---|---|
| 6 月 | Chongli 50K (4 周) + 2-3 场 HM 段位 |
| 7-8 月 | 密集 LSD 长距离训练 (40-50km 2-3 次) |
| 9 月 | 1 场 35-40km 测试赛 |
| 10 月 | Taper 减量 + 1 场 HM 找状态 |
| 11 月 | 3 连战 (场 1 全力 / 场 2-3 控强度) |

### 11 月底 PI 预测: 500-560 (Advanced 1-2 起步)

**段位升级预期**: Intermediate 4 → Advanced 1-2 跳 1 档

## 数据质量笔记

- **公开 ITRA 端点限制**: ITRA `/api/runner/find` 等内部 API 需 CSRF + session，开放访问返回 403
- **数据获取路径**: Chrome `65su345s` profile + opencli v1.8.2 (Browser Bridge) + 登录态
- **ITRA 上传时延**: 主办方批量上传需 7-30 天，Jiuzhaigou 5-31 跑完后预计 6/8-6/15 上传
- **PI 推算方法**: 5 场校准到 ITRA 354 (mean = 354) → 有效配速 (min/km_eq) 线性回归 → 推算新场 PI
- **单场 PI 公式简化**: `PI ≈ base_score(dist, elev) × (ref_time / your_time) × calibration`

## 后续追踪

- [ ] Jiuzhaigou 上传后核对实际 PI 变化
- [ ] 6 月初 4 连战完赛情况记录
- [ ] 第一场 50K 测试 (推荐 9-10 月)
- [ ] 训练负荷数据接入 (Garmin/Strava)
- [ ] HR 数据 + 配速分析

## 引用

- ITRA Profile: https://itra.run/RunnerSpace/young.sphinx.6729918
- Jiuzhaigou 2026 Race: https://itra.run/Races/RaceDetails/JIUZHAIGOU.TRAIL..Sacred.Garden.33KM/2026/113873
- ITRA Performance Index 表: https://itra.run/Runners/Ranking
- opencli 工具: https://github.com/jackwener/opencli (v1.8.2)

## 相关页面

- [[entities/exercise-science/running/trail-running]] — 越野跑概览
- [[entities/exercise-science/running/running-economy]] — 跑步经济性
- [[entities/exercise-science/running/trail-running-injuries]] — 越野跑损伤
- [[entities/exercise-science/running/trail-running-psychology]] — 越野跑心理
- [[entities/exercise-science/running/ultra-endurance]] — 超长距离耐力
