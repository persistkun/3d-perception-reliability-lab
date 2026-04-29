# AV2 数据集笔记

状态：2026-04-29 创建中文模板。

目标：整理 Argoverse 2 的数据目录、转换假设、coordinate frame、class mapping，以及 reliability 项目用到的 evaluation artifacts。

## Dataset 范围

当前项目：Argoverse 2 LiDAR 3D detection reliability audit。

当前重要 split：

```text
Full prepared validation, sample interval 1
```

Selected baseline result：

```text
VoxelNeXt epoch34 selected:
mAP 0.1397, AvgR 0.1800, internal ECE 0.0624, Brier 0.1665, FPS 15.75
```

## 需要填写的内容

- [ ] Raw AV2 directory layout。
- [ ] OpenPCDet prepared data directory layout。
- [ ] Info file 名称和 sample 数量。
- [ ] Class list 和 class mapping。
- [ ] Coordinate system notes。
- [ ] Box convention notes。
- [ ] Diagnostic scripts 使用的 matching rule。
- [ ] OpenPCDet internal ECE 和 diagnostic post-hoc ECE 的区别。

## Diagnostic Matching Rule

当前 supplement 中的设置：

- score threshold：`> 0.3`
- matching：2m center-distance
- assignment：class-consistent greedy matching

## 常见 failure modes

- far-range detections
- vulnerable road users
- sparse point clouds
- long-tail classes
- high-confidence false positives
- missed small objects
