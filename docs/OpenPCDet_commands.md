# OpenPCDet 命令速查表

状态：2026-04-29 创建中文模板。

目标：收集可复现命令，包括 smoke test、training、evaluation、result inspection、paper artifact refresh。

## 环境

待填：填写 conda environment、CUDA version、PyTorch version、OpenPCDet commit。

```powershell
conda activate <env>
cd C:\AV2_Scenario_Mining\OpenPCDet
```

## Smoke Test 模板

长时间训练前，先用小 subset 或 batch size 1 快速验证。

```powershell
python tools/test.py --cfg_file <config.yaml> --ckpt <checkpoint.pth> --batch_size 1
```

## Evaluation 模板

```powershell
python tools/test.py --cfg_file <config.yaml> --ckpt <checkpoint.pth> --batch_size <N> --eval_all
```

## Training 模板

```powershell
python tools/train.py --cfg_file <config.yaml> --batch_size <N> --epochs <E>
```

## 当前 AV2 reliability 项目命令

从 WACV 仓库根目录刷新 paper-facing artifacts：

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

Selected-baseline selective risk figure：

```powershell
python scripts\selective_risk_detection.py --model-preset si1_selected_baseline --sample-interval 1 --out-json reports\selective_risk_detection_si1_selected_baseline_summary.json --out-csv reports\selective_risk_detection_si1_selected_baseline_summary.csv --out-curves reports\selective_risk_detection_si1_selected_baseline_curves.csv --out-md PAPER\SELECTIVE_RISK_DETECTION_SI1_SELECTED_BASELINE.md --out-figure figures\selective_risk_detection_si1_selected_baseline.png
```

## 结果路径

Selected baseline：

```text
OpenPCDet/output/argo2_models/cbgs_voxel01_voxelnext/si1_baseline_epoch34_eval/eval/epoch_34/val/si1/result.pkl
```

Paper evidence：

```text
PAPER/PAPER_NUMBER_LINEAGE.md
reports/posthoc_calibration_baseline_epoch34_si1.csv
reports/selective_risk_detection_si1_selected_baseline_summary.csv
figures/selective_risk_detection_si1_selected_baseline.png
```

## 每日命令记录

| 日期 | 命令 | 输出路径 | 结果 | 下一步 |
|---|---|---|---|---|
| 2026-04-29 | 创建命令表 | `docs/OpenPCDet_commands.md` | 模板已建立 | 填写精确 train/eval 命令 |
