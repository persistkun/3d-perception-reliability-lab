# 8-Week Sprint: 3D Perception Research Assistant

Wang Changkun | XMUM AI Year 1 | Target window: August-September 2026 top labs

Core positioning:

> 3D Perception Baseline Engineer + Reliability Analyst

Working rule for this thread:

- This document is the active sprint memory from 2026-04-29 onward.
- The goal is not passive learning. The goal is weekly deliverables that can be shown to professors, PhD students, and research labs.
- Every workday should leave at least one artifact: code, figure, note, commit, result table, email draft, or reproducible command.

## Daily Template

| Block | Time | Output |
|---|---:|---|
| Paper / course | 1h | Notes or summary |
| Code / experiment | 2h | Script, command, log, or result |
| Notes / documentation | 1h | Markdown, table, or figure explanation |
| GitHub / application material | 1h | Commit, README update, CV bullet, or email draft |

## Stage 1: Weeks 1-2, OpenPCDet Foundation

Goal: become credible as someone who can run and audit OpenPCDet baselines.

Key skills:

- OpenPCDet repo map: datasets, models, tools.
- `tools/train.py` and `tools/test.py` CLI arguments.
- Dataset config and model config fields.
- Checkpoint loading and evaluation flow.
- Prediction dictionaries: boxes, scores, labels.
- AV2, nuScenes, and KITTI data layout.
- Fast batch-size-1 smoke tests.
- Logs, TensorBoard, W&B, and `result.pkl`.

Tasks:

- [ ] Run CenterPoint on nuScenes or a small/smoke subset.
- [ ] Add or document W&B logging for loss and mAP curves.
- [ ] Document AV2 to OpenPCDet conversion and coordinate alignment.
- [ ] Run or summarize AV2 CenterPoint baseline and competition-style output.

Deliverables:

- [ ] `docs/OpenPCDet_code_map.md`
- [ ] `docs/OpenPCDet_commands.md`
- [ ] `docs/AV2_dataset_notes.md`
- [ ] Reproducible eval log screenshot or copied metrics table.

Acceptance:

- [ ] A CenterPoint baseline number exists.
- [ ] The AV2 conversion path is documented and reproducible.
- [ ] README or notes show exact commands and result paths.

## Stage 2: Week 3, PointPillars + Visualization

Goal: explain PointPillars clearly and produce visual evidence for a research portfolio.

Tasks:

- [ ] Read PointPillars Section 3 and Fig. 2.
- [ ] Locate OpenPCDet `pointpillar.yaml` and annotate key fields.
- [ ] Build an Open3D visualization script for 3D boxes over point clouds.
- [ ] Generate GIF or MP4 for README.
- [ ] Collect at least 3 failure cases: far range, occlusion, sparse points.

Deliverables:

- [ ] `docs/PointPillars_explained.md`
- [ ] `figures/3d_visualization.gif` or MP4
- [ ] Failure-case screenshots and explanations.

Acceptance:

- [ ] Can explain why PointPillars is fast.
- [ ] Can explain pillar vs voxel.
- [ ] README first screen has a strong visualization.

## Stage 3: Week 4, CenterPoint + Data Augmentation

Goal: move from running baselines to understanding detector design.

Tasks:

- [ ] Trace `center_head.py` and explain heatmap target generation.
- [ ] Document anchor-based vs center-based detection.
- [ ] Implement a simple Gaussian-noise point-cloud augmentation.
- [ ] Plot AV2 class distribution.
- [ ] Plot AV2 distance distribution.

Deliverables:

- [ ] `docs/CenterPoint_vs_PointPillars.md`
- [ ] `docs/data_augmentation_notes.md`
- [ ] `figures/class_distribution.png`
- [ ] `figures/distance_distribution.png`
- [ ] Commented or documented CenterPoint head notes.

Acceptance:

- [ ] Can explain anchor-based vs center-based detection.
- [ ] Augmentation pipeline runs.
- [ ] W&B or logs show before/after comparison.

## Stage 4: Week 5, Reliability Analysis

Goal: turn the portfolio into a differentiated research contribution.

Core question:

> When does a 3D detector know that it should not be trusted?

Tasks:

- [ ] Implement or clean `scripts/calibration_metrics.py`.
- [ ] Implement or clean `scripts/risk_coverage.py`.
- [ ] Prepare `notebooks/03_calibration_and_selective_risk.ipynb`.
- [ ] Plot reliability diagram.
- [ ] Plot risk-coverage curve.
- [ ] Run subgroup analysis by class, distance, VRU, and small/long-tail objects.

Deliverables:

- [ ] `scripts/calibration_metrics.py`
- [ ] `scripts/risk_coverage.py`
- [ ] `notebooks/03_calibration_and_selective_risk.ipynb`
- [ ] `figures/reliability_diagram.png`
- [ ] `figures/risk_coverage_curve.png`
- [ ] Grouped ECE/Brier table.

Acceptance:

- [ ] ECE and Brier scripts run from saved detection results.
- [ ] Reliability diagram exists.
- [ ] Risk-coverage curve exists.
- [ ] Can explain why calibration matters beyond mAP.

## Stage 5: Week 6, Frontier: Occupancy / BEV / World Model

Goal: be able to discuss current autonomous-driving perception trends.

Reading list:

- [ ] PointPillars
- [ ] CenterPoint
- [ ] BEVDet
- [ ] BEVFusion
- [ ] TPVFormer
- [ ] OccNet
- [ ] UniAD
- [ ] SurroundOcc
- [ ] Calibration: Guo et al.

Tasks:

- [ ] Write 100-word notes for each core paper.
- [ ] Run or document TPVFormer inference demo if feasible.
- [ ] Run or document one 3D occupancy open-source inference demo if feasible.
- [ ] Create a comparison table: Detection vs BEV vs Occupancy vs World Model.

Deliverables:

- [ ] `docs/frontier_notes_occupancy_bev_worldmodel.md`
- [ ] `paper-notes/TPVFormer.md`
- [ ] `paper-notes/BEVFusion.md`
- [ ] `paper-notes/OccNet.md`
- [ ] `paper-notes/UniAD.md`
- [ ] TPVFormer or occupancy visualization screenshot.

Acceptance:

- [ ] Can explain TPVFormer, BEVFusion, and UniAD in one sentence each.
- [ ] Can explain why perception is moving from 3D detection to occupancy.

## Stage 6: Week 7, GitHub Portfolio

Goal: make the GitHub repository useful within 3 seconds.

Target structure:

```text
3d-perception-reliability-lab/
├── README.md
├── docs/
├── notebooks/
├── scripts/
├── paper-notes/
└── figures/
```

README first screen must show:

- Strong visualization GIF.
- Concrete baseline metrics.
- What the student can immediately do for a lab.
- Links to reliability analysis and paper notes.

Tasks:

- [ ] Organize all files into the target structure.
- [ ] Add GIF and result table to README.
- [ ] Update one-page CV.
- [ ] Add concrete numbers: mAP, FPS, data scale, ECE, Brier, AUROC.

Acceptance:

- [ ] README first screen has visuals and numbers.
- [ ] CV has a strong 3D perception reliability project entry.

## Stage 7: Week 8, Targeted Outreach

Goal: send 20 precise research emails, not generic mass email.

Priority targets:

- [ ] XMUM AI faculty: Dr. Goh, Prof. Zhang, Dr. Ashwaq, Dr. Hakim, Dr. Chua, Dr. Shaidah.
- [ ] Shanghai AI Lab / OpenDriveLab.
- [ ] Shenzhen IDEA.
- [ ] Tsinghua MARS Lab PhD students.
- [ ] SJTU MVIG Lab PhD students.
- [ ] BAAI.
- [ ] NTU AutoDriving Lab.
- [ ] A*STAR.
- [ ] HKUST / HKU CV groups.

Email rule:

- [ ] First paragraph must mention a specific paper or project by the recipient.
- [ ] Include GitHub and one-page resume.
- [ ] Keep the ask concrete: baseline experiments, ablation, point-cloud data processing, failure analysis, reliability evaluation.
- [ ] Follow up once after 7 days.

Tracking table:

| Target | Person | Paper / project hook | Date sent | Follow-up | Reply | Next action |
|---|---|---|---|---|---|---|
| XMUM | Dr. Goh Sim Kuan | NeuroMerging / AI4Brain |  |  |  |  |
| XMUM | Prof. Zhang Yingqian | Reliable AI / CV / AI security |  |  |  |  |

## Current Highest-Value Positioning

Use this phrase when introducing the project:

> I work on reliable 3D perception: OpenPCDet baselines, LiDAR detection evaluation, confidence calibration, risk-coverage analysis, and subgroup failure analysis.

Do not describe the project only as autonomous driving. The broader bridge is:

> trustworthy AI, reliable perception, calibration, uncertainty, risk-aware evaluation, and real-world model failure analysis.

## Immediate Next Actions

- [ ] Create `docs/OpenPCDet_code_map.md`.
- [ ] Create `docs/OpenPCDet_commands.md`.
- [ ] Inspect existing AV2/WACV files to reuse prior results instead of duplicating work.
- [ ] Extract current best baseline metrics from existing project artifacts.
- [ ] Draft Dr. Goh outreach email after reading NeuroMerging abstract and project list.
