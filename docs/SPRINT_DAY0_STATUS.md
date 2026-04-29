# Sprint Day 0 初始盘点

日期：2026-04-29

这个文件记录：8 周冲刺里哪些东西已经从 WACV/AV2 项目继承过来了，哪些还需要整理成干净的作品集材料。

## 当前已有的强资产

WACV 论文仓库里已经有一个 paper-grade reliability 项目：

```text
When Should a 3D Detector Doubt Itself?
Calibration, Uncertainty, and Reliability on Argoverse 2
```

当前最强 detector-quality baseline：

| Model | Dataset / split | mAP | AvgR | Internal ECE | Brier | FPS |
|---|---|---:|---:|---:|---:|---:|
| VoxelNeXt epoch34 selected | AV2 full SI=1 validation | 0.1397 | 0.1800 | 0.0624 | 0.1665 | 15.75 |
| VoxelNeXt epoch50 prior | AV2 full SI=1 validation | 0.1237 | 0.1658 | 0.0631 | 0.1637 | 16.45 |
| Low-LR SI=1 | AV2 full SI=1 validation | 0.1234 | 0.1515 | 0.0631 | 0.1535 | 16.42 |
| MC-Dropout T=5 SI=1 | AV2 full SI=1 validation | 0.0897 | 0.1113 | 0.0452 | 0.1592 | 3.62 |

Post-hoc calibration：

| Setting | Diagnostic ECE |
|---|---:|
| Identity / uncalibrated | 0.1043 |
| Global affine-logit calibration | 0.0078 |
| Classwise affine-logit calibration | 0.0071 |

关键理解：

- MC-Dropout 改善 internal ECE，但伤害 mAP 和 FPS。
- Held-out score calibration 保留检测结果，同时给出最强 reliability correction。
- VRU 和 subgroup reliability 是安全风险里不能被 global metrics 掩盖的部分。

## 和本冲刺相关的已有脚本

Reliability 和 calibration：

- `scripts/posthoc_calibration_search.py`
- `scripts/selective_risk_detection.py`
- `scripts/distance_aware_calibration_experiment.py`
- `scripts/group_aware_risk_calibration_experiment.py`
- `scripts/generate_wacv_reliability_figures.py`
- `scripts/generate_wacv_group_analysis.py`

Paper 和 reproducibility：

- `README_WACV_REPRODUCIBILITY.md`
- `PAPER/PAPER_NUMBER_LINEAGE.md`
- `scripts/check_paper_integrity.py`
- `scripts/refresh_paper_artifacts.ps1`

Qualitative visualization：

- `scripts/mine_qualitative_cases.py`
- `scripts/make_qualitative_storyboard.py`
- `scripts/make_qualitative_montage.py`
- `figures/qualitative/`

## 当前缺口

WACV 项目作为论文很强，但还没有被整理成“别人一眼看懂的科研助理作品集”。

高优先级缺口：

- [ ] GitHub README 第一屏：一句定位、图、结果表。
- [ ] `docs/OpenPCDet_code_map.md`
- [ ] `docs/OpenPCDet_commands.md`
- [ ] `docs/AV2_dataset_notes.md`
- [ ] 一个干净 visualization GIF 或 montage。
- [ ] 一页 CV bullet。
- [ ] Dr. Goh 套磁邮件。
- [ ] 一份说明：AV2 reliability 项目如何连接 XMUM AI 老师方向。

低优先级或可选缺口：

- [ ] nuScenes CenterPoint baseline。
- [ ] PointPillars reproduction。
- [ ] TPVFormer 或 occupancy inference demo。

## 更新后的策略

不要从零开始。

现在采用两条线：

1. 作品集包装：把已有 WACV/AV2 reliability work 整理成 GitHub-facing portfolio。
2. 能力拓宽：补 PointPillars、CenterPoint、BEV/Occupancy 笔记和可选 demo。

## 当前最佳自我介绍

> I am a first-year AI student at XMUM working on reliable 3D perception. I have built an Argoverse 2 / OpenPCDet reliability audit around VoxelNeXt, covering baseline evaluation, calibration, MC-Dropout uncertainty, selective risk detection, runtime trade-offs, and subgroup reliability. I can contribute to a lab by running baselines, processing point-cloud data, auditing detector failures, and turning saved detection outputs into reliability evidence.

## 下一步

- [ ] 填 `docs/OpenPCDet_commands.md`。
- [ ] 填 `docs/OpenPCDet_code_map.md`。
- [ ] 写 README 第一屏草稿。
