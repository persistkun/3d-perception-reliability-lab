# 前沿笔记：BEV、Occupancy、World Models

状态：2026-04-29 创建中文模板。

目标：建立自动驾驶感知前沿框架，能解释为什么行业从 object-level 3D detection 往 scene-level representation 走。

## 核心理解框架

```text
3D Detection
  -> 预测 predefined classes 的 object-level boxes

BEV Perception
  -> 把多传感器信息统一到 bird's-eye-view 表示

3D Occupancy Prediction
  -> 预测 scene-level occupied/free/semantic voxel

4D / World Models
  -> 不只看当前帧，还预测未来动态，用于 planning 和 simulation
```

## 对比表

| 方向 | Input | Output | Strength | Limitation |
|---|---|---|---|---|
| 3D Detection | 待填 | 待填 | 待填 | 待填 |
| BEV Perception | 待填 | 待填 | 待填 | 待填 |
| 3D Occupancy | 待填 | 待填 | 待填 | 待填 |
| World Model | 待填 | 待填 | 待填 | 待填 |

## Paper Notes Checklist

- [ ] BEVDet
- [ ] BEVFusion
- [ ] TPVFormer
- [ ] OccNet
- [ ] UniAD
- [ ] SurroundOcc

## 一句话解释

- BEVFusion：待填。
- TPVFormer：待填。
- UniAD：待填。
