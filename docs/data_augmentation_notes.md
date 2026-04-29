# Data Augmentation 笔记

状态：2026-04-29 创建中文模板。

目标：整理 OpenPCDet 里常见 point-cloud augmentation 方法，并记录自己的 custom experiment。

## 标准 Augmentations

- GT sampling：
- Random flip：
- Random rotation：
- Random scaling：
- Translation / noise：

## OpenPCDet 路径

待填。

## Custom Gaussian Noise Experiment

状态：未开始。

计划：

- [ ] 给 point coordinates 加 Gaussian noise。
- [ ] 插入 data processor 或 augmentor pipeline。
- [ ] 跑 smoke test。
- [ ] 比较 mAP、calibration、failure cases。

## 结果记录

| 日期 | Augmentation | Dataset / split | Metric change | Notes |
|---|---|---|---|---|
