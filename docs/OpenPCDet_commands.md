# OpenPCDet 命令速查表

状态：2026-04-29 创建中文模板。

目标：收集可复现命令，包括 smoke test、training、evaluation、result inspection、paper artifact refresh。

## 环境

Linux (tested on Ubuntu 14.04/16.04/18.04/20.04/21.04)
Linux（已在 Ubuntu 14.04/16.04/18.04/20.04/21.04 上测试）
• Python 3.6+
• PyTorch 1.1 or higher (tested on PyTorch 1.1, 1,3, 1,5~1.10)
PyTorch 1.1 或更高版本（已在 PyTorch 1.1、1.3、1.5~1.10 上测试）
• CUDA 9.0 or higher (PyTorch 1.3+ needs CUDA 9.2+)
CUDA 9.0 或更高版本（PyTorch 1.3+ 需要 CUDA 9.2+）
• spconv v1.0 (commit 8da6f96) or spconv v1.2 or spconv v2.x
spconv v1.0 (commit 8da6f96) 或 spconv v1.2 或 spconv v2.x

```powershell
git clone https://github.com/open-mmlab/OpenPCDet.git克隆仓库
python setup.py develop安装,让系统认识防止报错
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
python test.py --cfg_file ${CONFIG_FILE} --batch_size ${BATCH_SIZE} --ckpt ${CKPT}
# 测试/评估命令（通用）
python test.py --cfg_file [配置文件路径] --batch_size [批次大小] --ckpt [权重路径]

# nuScenes CenterPoint 评估示例
python test.py --cfg_file tools/cfgs/nuscenes_models/cbgs_pp_centerpoint.yaml --batch_size 1 --ckpt ../output/xxx/last_checkpoint.pth

# AV2 CenterPoint 评估示例
python test.py --cfg_file tools/cfgs/argo2_models/cbgs_pp_centerpoint_argo2.yaml --batch_size 1 --ckpt ../output/xxx/last_checkpoint.pth
#筛出最优的但是时间会倍数增长,只用在最后评估
python test.py --cfg_file ${CONFIG_FILE} --batch_size ${BATCH_SIZE} --eval_all
#多gpu分布式
sh scripts/dist_test.sh ${NUM_GPUS} \
    --cfg_file ${CONFIG_FILE} --batch_size ${BATCH_SIZE}

# or

sh scripts/slurm_test_mgpu.sh ${PARTITION} ${NUM_GPUS} \
    --cfg_file ${CONFIG_FILE} --batch_size ${BATCH_SIZE}
后者为显卡集群
 学校超算、实验室集群、大厂算力平台专用
 
## 当前 AV2 reliability 项目命令
'''
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
## 今天学到的参数解释

| 参数 | 作用 | 我自己的理解 |
|---|---|---|
| `--cfg_file` | 指定 config 文件 | 决定用哪个 dataset、model、训练/评估设置 |
| `--ckpt` | 指定 checkpoint | eval 时加载训练好的 `.pth` 权重 |
| `--batch_size` | batch size | 显存不够就调小，smoke test 可以用 1,比如我的本地电脑 |
| `--eval_all` | 评估多个 checkpoint | 用来扫 checkpoint，找表现最好的 epoch，但耗时更长 |
| `--epochs` | 训练 epoch 数 | 控制训练轮数 |
| `--save_interval` | 保存 checkpoint 的间隔 | 控制保存 checkpoint 的频率,为了防止训练丢失还是尽量每个epoch都要保存 |
| `--eval` | 是否评估 | 默认是评估，训练时可以不评估 python test.py --cfg xxx.yaml --eval result.pkl直接计算指标了,不再进行评估几分钟,Python test.py 默认也会eval|
| `--save_to_file` | 是否保存结果到文件 | 默认是保存，训练时可以不保存 |
| `--out_dir` | 输出目录 | 默认是 `output`，训练时可以指定 |
| `--out_csv` | 输出 csv 文件 | 默认是 `result.csv`，训练时可以指定CSV = 纯文本表格文件，专门存实验指标、数值结果，科研必备。 |
## 每日命令记录

| 日期 | 命令 | 输出路径 | 结果 | 下一步 |
|---|---|---|---|---|
| 2026-04-29 | | 2026-04-29 | 整理 OpenPCDet train/test/eval 命令 | `docs/OpenPCDet_commands.md` | 已理解 `train.py`、`test.py`、`--cfg_file`、`--ckpt`、`--eval_all`  | 模板已建立 | 填写精确 train/eval 命令 |
4.29 学习了openPCDet的流程,数据预处理以及评估训练的指令,一些参数的意义,指令怎么写,csv是什么,分布式的指令有两种