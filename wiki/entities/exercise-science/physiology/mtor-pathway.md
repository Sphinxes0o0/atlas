---
type: entity
tags: [exercise-science, protein-synthesis, cell-signaling]
created: 2026-05-20
updated: 2026-05-28
sources: [relay-neuron-physiology, relay-neuron-mtor-pathway]
---

# mTOR Pathway (mTOR 信号通路)

## Definition

哺乳动物雷帕霉素靶蛋白 (mTOR) 是 PI3K 相关激酶家族成员，是蛋白质合成的主要调控因子，作为细胞生长的中央枢纽整合营养、能量和生长因子信号。

## Structure

| 复合物 | 组成 | 功能 |
|-------|------|-----|
| mTORC1 | mTOR + Raptor + mLST8 | 蛋白质合成调控（核心） |
| mTORC2 | mTOR + Rictor + mLST8 | 细胞存活、代谢 |

## Activation Cascade

```
氨基酸 (亮氨酸) → mTORC1 → S6K1 → 蛋白质合成
                        ↓
                  4E-BP1 磷酸化
                        ↓
                  eIF4E 释放 → 翻译启动
```

## Key Findings

- **亮氨酸核心作用**: ~2-3g/餐 达到最大 [[entities/exercise-science/physiology/mps-muscle-protein-synthesis]] 刺激
- **运动后时间进程**:
  - 运动后 1-4 小时: mTOR、S6K1、4E-BP1 磷酸化增加
  - 运动后 24-48 小时: MPS 持续升高
  - 运动后 72 小时: 恢复至基线
- **阻力训练 vs 有氧训练**:
  - 阻力训练: 显著激活 mTORC1 (Ser2448, S6K1 Thr389)
  - 有氧训练: 激活 AMPK，抑制 mTORC1
  - 这一差异是 [[entities/exercise-science/physiology/concurrent-training]] 协调效应的核心机制

### 新机制发现 (2026-05)

- **GATOR2复合物**: 氨基酸充足时激活mTORC1，GCN2在氨基酸缺乏时抑制mTORC1
- **Sestrin2和CASTOR1**: 亮氨酸和精氨酸的直接感受器，与GATOR2相互作用解除对mTORC1的抑制
- **ILF3**: 新发现的mTORC1正调控因子，形成复合物促进mTORC1信号
- **FBXO2**: F-box蛋白，通过调节GATOR2组分影响mTORC1激活

## Anabolic Resistance

老年人或特定人群对合成代谢刺激响应减弱：
- mTOR 通路信号下调
- [[entities/exercise-science/physiology/satellite-cells]] 活性降低
- 肌肉蛋白分解 (MPB) 增加
- 需要更高蛋白质剂量或亮氨酸富集

## 过度激活风险

- **胰岛素抵抗**: 持续mTORC1激活通过S6K1反馈抑制IRS-1磷酸化
- **神经退行性疾病**: 过度mTORC1与阿尔茨海默病相关
- **昼夜节律破坏**: 夜间光照和深夜进食抑制褪黑素，干扰mTORC1正常节律
- **肿瘤促进**: mTORC1过度激活促进细胞生长和血管生成
- **代谢综合征**: 高糖饮食+频繁进食→持续mTORC1激活→代谢失调

## Related

- [[entities/exercise-science/physiology/mps-muscle-protein-synthesis]]
- [[entities/exercise-science/physiology/muscle-hypertrophy]]
- [[entities/exercise-science/physiology/concurrent-training]]
