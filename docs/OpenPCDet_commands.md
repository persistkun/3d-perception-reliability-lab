# OpenPCDet Commands

Status: placeholder created on 2026-04-29.

Goal: collect reproducible commands for smoke tests, training, evaluation, result inspection, and paper artifact refresh.

## Environment

TODO: fill exact conda environment, CUDA version, PyTorch version, and OpenPCDet commit.

```powershell
conda activate <env>
cd C:\AV2_Scenario_Mining\OpenPCDet
```

## Smoke Test Pattern

Use small subsets or batch size 1 before launching long jobs.

```powershell
python tools/test.py --cfg_file <config.yaml> --ckpt <checkpoint.pth> --batch_size 1
```

## Evaluation Pattern

```powershell
python tools/test.py --cfg_file <config.yaml> --ckpt <checkpoint.pth> --batch_size <N> --eval_all
```

## Training Pattern

```powershell
python tools/train.py --cfg_file <config.yaml> --batch_size <N> --epochs <E>
```

## Current AV2 Reliability Project Commands

Refresh paper-facing artifacts from the repository root:

```powershell
python scripts\generate_method_overview_figure.py
python scripts\generate_posthoc_calibration_figure.py
python scripts\generate_lowlr_seed_stability_figure.py
python scripts\generate_hard_class_figure.py
python scripts\generate_wacv_group_analysis.py
python scripts\generate_wacv_reliability_figures.py
python scripts\generate_reliability_tradeoff_summary_figure.py
python scripts\selective_risk_detection.py
python scripts\check_paper_integrity.py
```

Selected-baseline selective risk figure:

```powershell
python scripts\selective_risk_detection.py --model-preset si1_selected_baseline --sample-interval 1 --out-json reports\selective_risk_detection_si1_selected_baseline_summary.json --out-csv reports\selective_risk_detection_si1_selected_baseline_summary.csv --out-curves reports\selective_risk_detection_si1_selected_baseline_curves.csv --out-md PAPER\SELECTIVE_RISK_DETECTION_SI1_SELECTED_BASELINE.md --out-figure figures\selective_risk_detection_si1_selected_baseline.png
```

## Result Paths

Selected baseline:

```text
OpenPCDet/output/argo2_models/cbgs_voxel01_voxelnext/si1_baseline_epoch34_eval/eval/epoch_34/val/si1/result.pkl
```

Paper evidence:

```text
PAPER/PAPER_NUMBER_LINEAGE.md
reports/posthoc_calibration_baseline_epoch34_si1.csv
reports/selective_risk_detection_si1_selected_baseline_summary.csv
figures/selective_risk_detection_si1_selected_baseline.png
```

## Daily Command Log

| Date | Command | Output path | Result | Next action |
|---|---|---|---|---|
| 2026-04-29 | Created command sheet | `docs/OpenPCDet_commands.md` | Skeleton ready | Fill exact train/eval commands |
