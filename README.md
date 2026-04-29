# 3D Perception Reliability Lab

> LiDAR 3D object detection · OpenPCDet baselines · Argoverse 2 · calibration · uncertainty · selective risk · subgroup reliability

Wang Changkun | XMUM AI Year 1

## 我能为实验室做什么

- 跑通并整理 OpenPCDet 3D perception baseline。
- 处理 Argoverse 2 这类大规模点云数据和 LiDAR detection 输出。
- 不只看 mAP，还能分析 detector reliability：calibration、Brier score、risk-coverage curve、runtime trade-off、subgroup failure。
- 把实验结果整理成可复现的表格、图、论文笔记和失败案例分析。
- 能讨论 3D detection 到 BEV、occupancy prediction、world model 的前沿趋势。

## 当前主项目

**When Should a 3D Detector Doubt Itself? Calibration, Uncertainty, and Reliability on Argoverse 2**

这个仓库是我的 3D perception 科研助理作品集。当前最强的资产是一个基于 OpenPCDet / VoxelNeXt 风格 pipeline 的 Argoverse 2 LiDAR 3D detection reliability audit。

## 当前结果快照

| Model | Dataset / split | mAP | AvgR | Internal ECE | Brier | FPS |
|---|---|---:|---:|---:|---:|---:|
| VoxelNeXt epoch34 selected | AV2 full SI=1 validation | 0.1397 | 0.1800 | 0.0624 | 0.1665 | 15.75 |
| VoxelNeXt epoch50 prior | AV2 full SI=1 validation | 0.1237 | 0.1658 | 0.0631 | 0.1637 | 16.45 |
| Low-LR SI=1 | AV2 full SI=1 validation | 0.1234 | 0.1515 | 0.0631 | 0.1535 | 16.42 |
| MC-Dropout T=5 SI=1 | AV2 full SI=1 validation | 0.0897 | 0.1113 | 0.0452 | 0.1592 | 3.62 |

Post-hoc diagnostic calibration 把 selected baseline 的 ECE 从 `0.1043` 降到 `0.0078`，classwise affine-logit calibration 可到 `0.0071`。

## 冲刺地图

- [8 周冲刺总计划](SPRINT_8W_RESEARCH_ASSISTANT.md)
- [Day 0 初始盘点](docs/SPRINT_DAY0_STATUS.md)
- [OpenPCDet 源码地图](docs/OpenPCDet_code_map.md)
- [OpenPCDet 命令速查表](docs/OpenPCDet_commands.md)
- [AV2 数据集笔记](docs/AV2_dataset_notes.md)
- [Reliability analysis notebook 占位](notebooks/03_calibration_and_selective_risk.ipynb)
- [BEV / occupancy / world model 前沿笔记](docs/frontier_notes_occupancy_bev_worldmodel.md)

## 仓库结构

```text
3d-perception-reliability-lab/
├── README.md              # GitHub 首页，放最能展示实力的成果
├── docs/                  # 日常技术笔记和实验说明
├── notebooks/             # 分析 notebook
├── scripts/               # 可复用脚本
├── paper-notes/           # 每篇论文一份笔记
└── figures/               # 后续放图、GIF、结果可视化
```

## 每日节奏

每天按 2 小时推进：

- 40 分钟输入：论文、文档、视频或源码。
- 60 分钟输出：笔记、代码、表格或图。
- 20 分钟 GitHub 收尾：commit + push。

最低标准：每天改一个文件，留下一个有用产物。

## 下一批每日产物

- 填 `docs/OpenPCDet_code_map.md`。
- 填 `docs/OpenPCDet_commands.md`。
- 给 README 加第一张干净的 visualization 或 qualitative montage。
- 读 Dr. Goh 的 NeuroMerging 后，完善套磁邮件草稿。
