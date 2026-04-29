# 3D Perception Reliability Lab

> LiDAR 3D object detection · OpenPCDet baselines · Argoverse 2 · calibration · uncertainty · selective risk · subgroup reliability

Wang Changkun | XMUM AI Year 1

## What I Can Do For A Lab

- Run and audit OpenPCDet 3D perception baselines on large-scale point-cloud datasets.
- Process Argoverse 2 style LiDAR detection outputs and trace metrics back to saved artifacts.
- Analyze detector reliability beyond mAP: calibration, Brier score, risk-coverage curves, runtime trade-offs, and subgroup failures.
- Produce reproducible result tables, figures, paper notes, and failure-case visualizations.
- Discuss the current shift from 3D detection to BEV, occupancy prediction, and world models.

## Current Project

**When Should a 3D Detector Doubt Itself? Calibration, Uncertainty, and Reliability on Argoverse 2**

This repository is being organized into a research-assistant portfolio. The current strongest asset is an evidence-first reliability audit for LiDAR 3D detection on Argoverse 2 using an OpenPCDet / VoxelNeXt-style pipeline.

## Current Results Snapshot

| Model | Dataset / split | mAP | AvgR | Internal ECE | Brier | FPS |
|---|---|---:|---:|---:|---:|---:|
| VoxelNeXt epoch34 selected | AV2 full SI=1 validation | 0.1397 | 0.1800 | 0.0624 | 0.1665 | 15.75 |
| VoxelNeXt epoch50 prior | AV2 full SI=1 validation | 0.1237 | 0.1658 | 0.0631 | 0.1637 | 16.45 |
| Low-LR SI=1 | AV2 full SI=1 validation | 0.1234 | 0.1515 | 0.0631 | 0.1535 | 16.42 |
| MC-Dropout T=5 SI=1 | AV2 full SI=1 validation | 0.0897 | 0.1113 | 0.0452 | 0.1592 | 3.62 |

Post-hoc diagnostic calibration reduces selected-baseline ECE from `0.1043` to `0.0078` with global affine-logit calibration and `0.0071` with classwise affine-logit calibration.

## Sprint Map

- [8-week sprint plan](SPRINT_8W_RESEARCH_ASSISTANT.md)
- [Day 0 status](docs/SPRINT_DAY0_STATUS.md)
- [OpenPCDet code map](docs/OpenPCDet_code_map.md)
- [OpenPCDet commands](docs/OpenPCDet_commands.md)
- [AV2 dataset notes](docs/AV2_dataset_notes.md)
- [Reliability analysis notebook placeholder](notebooks/03_calibration_and_selective_risk.ipynb)
- [BEV / occupancy / world model notes](docs/frontier_notes_occupancy_bev_worldmodel.md)

## Target Repository Structure

```text
3d-perception-reliability-lab/
├── README.md
├── docs/
├── notebooks/
├── scripts/
├── paper-notes/
└── figures/
```

## Next Daily Outputs

- Fill `docs/OpenPCDet_code_map.md`.
- Fill `docs/OpenPCDet_commands.md`.
- Add the first clean visualization or qualitative montage to this README.
- Draft a targeted email to Dr. Goh Sim Kuan using the reliable-AI positioning.
