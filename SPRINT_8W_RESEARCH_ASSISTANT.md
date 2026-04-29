# 8 周冲刺：3D Perception Research Assistant

Wang Changkun | XMUM AI Year 1 | 目标时间：2026 年 8-9 月联系顶尖实验室

核心定位：

> 3D Perception Baseline Engineer + Reliability Analyst

这个仓库从 2026-04-29 开始作为冲刺工作台使用。

## 总原则

- 这不是“我在学习”的仓库，而是“我每天交付一点科研资产”的仓库。
- 每天至少留下一个产物：代码、图、笔记、commit、实验表、邮件草稿、可复现命令都可以。
- WACV 论文仓库继续放论文和实验原始资产；这个仓库只放对外展示、学习路线、作品集材料。
- 技术名词保持英文，比如 OpenPCDet、CenterPoint、ECE、Brier score、risk-coverage。

## 每天执行模板

| 时间块 | 时间 | 当天产物 |
|---|---:|---|
| 论文 / 课程 | 1h | 论文笔记或概念总结 |
| 代码 / 实验 | 2h | 脚本、命令、log、结果 |
| 笔记 / 文档 | 1h | Markdown、表格、图说明 |
| GitHub / 申请材料 | 1h | commit、README 更新、CV bullet、邮件草稿 |

## 第 1 阶段：第 1-2 周，OpenPCDet 地基

目标：让别人相信我是“会用 OpenPCDet 干活的人”。

要掌握：

- OpenPCDet repo 结构：datasets、models、tools。
- `tools/train.py` 和 `tools/test.py` 的参数。
- Dataset config 和 model config 的关键字段。
- checkpoint 加载和 evaluation 流程。
- prediction dict 里的 boxes、scores、labels。
- AV2、nuScenes、KITTI 的数据目录结构。
- batch size 1 smoke test。
- log、TensorBoard、W&B、`result.pkl` 怎么看。

任务：

- [ ] 跑通或整理 CenterPoint baseline。
- [ ] 记录 W&B 或其他日志方式。
- [ ] 整理 AV2 到 OpenPCDet 的转换和 coordinate alignment。
- [ ] 整理 AV2 baseline 结果和输出路径。

产出：

- [ ] `docs/OpenPCDet_code_map.md`
- [ ] `docs/OpenPCDet_commands.md`
- [ ] `docs/AV2_dataset_notes.md`
- [ ] 一份可复现 eval log / 结果数字表。

验收：

- [ ] 有一个清楚的 baseline 数字。
- [ ] AV2 conversion 路径讲得清楚。
- [ ] README 或 docs 里有精确命令和结果路径。

## 第 2 阶段：第 3 周，PointPillars + Visualization

目标：能 3 分钟讲清 PointPillars，并做出好看的点云可视化。

任务：

- [ ] 读 PointPillars Section 3 和 Fig. 2。
- [ ] 找到 OpenPCDet 的 `pointpillar.yaml` 并注释关键字段。
- [ ] 写 Open3D visualization 脚本，把 3D boxes 叠到点云上。
- [ ] 生成 GIF 或 MP4 放进 README。
- [ ] 收集 3 个 failure cases：远距离、遮挡、稀疏点云。

产出：

- [ ] `docs/PointPillars_explained.md`
- [ ] `figures/3d_visualization.gif` 或 MP4
- [ ] failure case 截图和分析。

验收：

- [ ] 能解释为什么 PointPillars 快。
- [ ] 能解释 pillar 和 voxel 的区别。
- [ ] README 第一屏有视觉成果。

## 第 3 阶段：第 4 周，CenterPoint + Data Augmentation

目标：从“会跑 baseline”升级到“懂 detector 设计思路”。

任务：

- [ ] 跟 `center_head.py`，理解 heatmap target 怎么生成。
- [ ] 整理 anchor-based vs center-based detection。
- [ ] 实现一个简单 Gaussian noise point-cloud augmentation。
- [ ] 画 AV2 class distribution。
- [ ] 画 AV2 distance distribution。

产出：

- [ ] `docs/CenterPoint_vs_PointPillars.md`
- [ ] `docs/data_augmentation_notes.md`
- [ ] `figures/class_distribution.png`
- [ ] `figures/distance_distribution.png`

验收：

- [ ] 能解释 anchor-based vs center-based。
- [ ] augmentation pipeline 跑通。
- [ ] 有 before/after 对比日志或图。

## 第 4 阶段：第 5 周，Reliability Analysis

目标：形成差异化能力。别人只会说 mAP，我要能说 detector 什么时候不可信。

核心问题：

> When does a 3D detector know that it should not be trusted?

任务：

- [ ] 整理 `scripts/calibration_metrics.py`。
- [ ] 整理 `scripts/risk_coverage.py`。
- [ ] 完成 `notebooks/03_calibration_and_selective_risk.ipynb`。
- [ ] 画 reliability diagram。
- [ ] 画 risk-coverage curve。
- [ ] 做 class、distance、VRU、小目标/long-tail subgroup analysis。

产出：

- [ ] `scripts/calibration_metrics.py`
- [ ] `scripts/risk_coverage.py`
- [ ] `notebooks/03_calibration_and_selective_risk.ipynb`
- [ ] `figures/reliability_diagram.png`
- [ ] `figures/risk_coverage_curve.png`
- [ ] grouped ECE/Brier 表格。

验收：

- [ ] ECE 和 Brier 脚本能从 saved detections 运行。
- [ ] reliability diagram 存在。
- [ ] risk-coverage curve 存在。
- [ ] 能解释 calibration 为什么比单看 mAP 更接近真实部署风险。

## 第 5 阶段：第 6 周，前沿视野：BEV / Occupancy / World Model

目标：顶尖实验室问前沿方向时不露怯。

阅读清单：

- [ ] PointPillars
- [ ] CenterPoint
- [ ] BEVDet
- [ ] BEVFusion
- [ ] TPVFormer
- [ ] OccNet
- [ ] UniAD
- [ ] SurroundOcc
- [ ] Calibration: Guo et al.

任务：

- [ ] 每篇核心论文写 100 字笔记。
- [ ] 如果可行，跑一次 TPVFormer inference demo。
- [ ] 如果可行，跑一次 3D occupancy inference demo。
- [ ] 做 Detection vs BEV vs Occupancy vs World Model 对比表。

产出：

- [ ] `docs/frontier_notes_occupancy_bev_worldmodel.md`
- [ ] `paper-notes/TPVFormer.md`
- [ ] `paper-notes/BEVFusion.md`
- [ ] `paper-notes/OccNet.md`
- [ ] `paper-notes/UniAD.md`
- [ ] TPVFormer 或 occupancy 可视化截图。

验收：

- [ ] 能一句话解释 TPVFormer、BEVFusion、UniAD。
- [ ] 能解释为什么自动驾驶感知从 3D detection 走向 occupancy。

## 第 6 阶段：第 7 周，GitHub 作品集

目标：让博士生点进 GitHub 3 秒内觉得这个学弟能干活。

README 第一屏必须有：

- 清楚定位。
- 关键 baseline metrics。
- 可视化 GIF 或图。
- 我能立刻为实验室做什么。
- reliability analysis 和 paper notes 链接。

任务：

- [ ] 整理仓库结构。
- [ ] 给 README 加 GIF 和 result table。
- [ ] 更新一页 CV。
- [ ] 加具体数字：mAP、FPS、数据规模、ECE、Brier、AUROC。

验收：

- [ ] README 第一屏有图和数字。
- [ ] CV 有强的 3D perception reliability 项目经历。

## 第 7 阶段：第 8 周，精准套磁

目标：发 20 封精准 research email，不群发。

优先目标：

- [ ] XMUM AI faculty：Dr. Goh、Prof. Zhang、Dr. Ashwaq、Dr. Hakim、Dr. Chua、Dr. Shaidah。
- [ ] Shanghai AI Lab / OpenDriveLab。
- [ ] Shenzhen IDEA。
- [ ] Tsinghua MARS Lab 博士生。
- [ ] SJTU MVIG Lab 博士生。
- [ ] BAAI。
- [ ] NTU AutoDriving Lab。
- [ ] A*STAR。
- [ ] HKUST / HKU CV groups。

邮件规则：

- [ ] 第一段必须提对方具体论文或项目。
- [ ] 放 GitHub 和一页 CV。
- [ ] 具体说明自己能干什么：baseline experiments、ablation、point-cloud data processing、failure analysis、reliability evaluation。
- [ ] 7 天后礼貌 follow-up 一次。

追踪表：

| Target | Person | Paper / project hook | Date sent | Follow-up | Reply | Next action |
|---|---|---|---|---|---|---|
| XMUM | Dr. Goh Sim Kuan | NeuroMerging / AI4Brain |  |  |  |  |
| XMUM | Prof. Zhang Yingqian | Reliable AI / CV / AI security |  |  |  |  |

## 当前最佳自我介绍

> I work on reliable 3D perception: OpenPCDet baselines, LiDAR detection evaluation, confidence calibration, risk-coverage analysis, and subgroup failure analysis.

不要只说自己做 autonomous driving。更宽的桥是：

> trustworthy AI, reliable perception, calibration, uncertainty, risk-aware evaluation, and real-world model failure analysis.

## 眼前下一步

- [ ] 填 `docs/OpenPCDet_code_map.md`。
- [ ] 填 `docs/OpenPCDet_commands.md`。
- [ ] 从 WACV/AV2 论文仓库提取已存在的 baseline metrics。
- [ ] 读 NeuroMerging 摘要后完善 Dr. Goh 邮件。
