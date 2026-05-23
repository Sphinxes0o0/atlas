---
type: entity
tags: [exercise-science, hrv, monitoring, wearable, recovery]
created: 2026-05-23
sources: [relay-neuron-technology]
---

# HRV Monitoring (心率变异性监测)

## Definition

HRV 监测是利用可穿戴设备（心率带、智能手表、胸带）测量并分析心率变异性，用于评估恢复状态和训练适应。

## Key Points

- **测量方式**: 胸带（最准）、智能手表、光学传感器
- **关键指标**: RMSSD（副交感功能）、SDNN（整体变异度）、LF/HF（交感/副交感平衡）
- **晨脉测量**: 晨起静息 HRV 最有参考价值
- **趋势分析**: 周平均与个人基线比较

详见: [[entities/exercise-science/physiology/heart-rate-variability]]

## Devices

| 设备类型 | 精准度 | 便利性 | 代表产品 |
|----------|--------|--------|----------|
| 心率带 | 最高 | 中等 | Polar H10 |
| 胸带 | 最高 | 中等 | Whoop |
| 智能手表 | 中等 | 高 | Apple Watch, Garmin |
| 指尖传感器 | 高 | 中 | Oura（指环）|

## Training Application

HRV 引导训练（HRV-guided training）：

1. **每日测量**: 晨起测量 3-5 分钟
2. **判断标准**: RMSSD 比基线高/低多少
3. **训练决策**: 高则加量，低则减量

| HRV vs 基线 | 训练建议 |
|-------------|----------|
| >20% | 可加量训练 |
| ±10% | 维持当前计划 |
| 10-20%↓ | 减量 20-30% |
| >20%↓ | 休息或主动恢复 |

## Wearable Technology

现代可穿戴设备集成 HRV 监测：

- **Whoop**: 持续监测 + 恢复评分
- **Oura Ring**: 睡眠 HRV + 体温
- **Garmin**: 腕部光学 HRV + Body Battery

详见: [[entities/exercise-science/technology/wearable-devices]]

## Related

- [[entities/exercise-science/physiology/heart-rate-variability]]
- [[entities/exercise-science/technology/wearable-devices]]
- [[entities/exercise-science/physiology/overtraining-syndrome]]
