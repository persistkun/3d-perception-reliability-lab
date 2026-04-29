# Sprint Day 0 Status

Date: 2026-04-29

This file records which parts of the 8-week sprint already exist in the current repository and which parts still need to be built into a clean portfolio.

## Current Strong Assets

The repository already contains a paper-grade reliability project:

```text
When Should a 3D Detector Doubt Itself?
Calibration, Uncertainty, and Reliability on Argoverse 2
```

Current best detector-quality baseline from `WACV_PROJECT_MEMORY_DO_NOT_DRIFT.md`:

| Model | Dataset / split | mAP | AvgR | Internal ECE | Brier | FPS |
|---|---|---:|---:|---:|---:|---:|
| VoxelNeXt epoch34 selected | AV2 full SI=1 validation | 0.1397 | 0.1800 | 0.0624 | 0.1665 | 15.75 |
| VoxelNeXt epoch50 prior | AV2 full SI=1 validation | 0.1237 | 0.1658 | 0.0631 | 0.1637 | 16.45 |
| Low-LR SI=1 | AV2 full SI=1 validation | 0.1234 | 0.1515 | 0.0631 | 0.1535 | 16.42 |
| MC-Dropout T=5 SI=1 | AV2 full SI=1 validation | 0.0897 | 0.1113 | 0.0452 | 0.1592 | 3.62 |

Post-hoc calibration result:

| Setting | Diagnostic ECE |
|---|---:|
| Identity / uncalibrated | 0.1043 |
| Global affine-logit calibration | 0.0078 |
| Classwise affine-logit calibration | 0.0071 |

Key interpretation:

- MC-Dropout improves internal ECE but hurts detection quality and runtime.
- Held-out score calibration preserves detections and gives the strongest reliability correction.
- VRU and subgroup reliability remain important failure modes.

## Existing Scripts Relevant to Sprint

Reliability and calibration:

- `scripts/posthoc_calibration_search.py`
- `scripts/selective_risk_detection.py`
- `scripts/distance_aware_calibration_experiment.py`
- `scripts/group_aware_risk_calibration_experiment.py`
- `scripts/generate_wacv_reliability_figures.py`
- `scripts/generate_wacv_group_analysis.py`

Paper and reproducibility:

- `README_WACV_REPRODUCIBILITY.md`
- `PAPER/PAPER_NUMBER_LINEAGE.md`
- `scripts/check_paper_integrity.py`
- `scripts/refresh_paper_artifacts.ps1`

Qualitative visualization:

- `scripts/mine_qualitative_cases.py`
- `scripts/make_qualitative_storyboard.py`
- `scripts/make_qualitative_montage.py`
- `figures/qualitative/`

## Sprint Gaps

The current project is strong as a paper, but not yet packaged as a first-screen research-assistant portfolio.

High-priority gaps:

- [ ] A public-facing README with one clear positioning line, visual, and metrics table.
- [ ] `docs/OpenPCDet_code_map.md`
- [ ] `docs/OpenPCDet_commands.md`
- [ ] `docs/AV2_dataset_notes.md`
- [ ] A clean visual demo GIF or compact montage for GitHub first screen.
- [ ] A one-page CV bullet set.
- [ ] A targeted email draft for Dr. Goh Sim Kuan.
- [ ] A bridge note explaining how this AV2 reliability project maps to XMUM AI faculty interests.

Lower-priority or optional gaps:

- [ ] nuScenes CenterPoint baseline if compute/time allows.
- [ ] PointPillars reproduction if needed for broader baseline credibility.
- [ ] TPVFormer or occupancy inference demo.

## Updated Strategy

Do not restart from scratch.

The sprint should now use a two-track strategy:

1. Portfolio packaging:
   Convert existing WACV/AV2 reliability work into a clean GitHub-facing research assistant portfolio.

2. Skill broadening:
   Add PointPillars, CenterPoint, BEV/Occupancy notes, and optional demos only where they improve credibility for external labs.

## Current Best Self-Introduction

Use this version:

> I am a first-year AI student at XMUM working on reliable 3D perception. I have built an Argoverse 2 / OpenPCDet reliability audit around VoxelNeXt, covering baseline evaluation, calibration, MC-Dropout uncertainty, selective risk detection, runtime trade-offs, and subgroup reliability. I can contribute to a lab by running baselines, processing point-cloud data, auditing detector failures, and turning saved detection outputs into reliability evidence.

## Next Concrete Step

Create the first two portfolio docs:

- `docs/OpenPCDet_commands.md`
- `docs/OpenPCDet_code_map.md`

Then create a README first-screen draft.
