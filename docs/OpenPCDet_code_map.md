# OpenPCDet 源码地图

状态：2026-04-29 创建中文模板。

目标：把 OpenPCDet 的结构整理到别人能看懂，也让自己以后快速回忆训练、评估、dataset、model、result artifact 都在哪里。

## 需要逐步填的区域

| 区域 | 路径 | 我要弄懂什么 | 笔记 |
|---|---|---|---|
| 训练入口 | `OpenPCDet/tools/train.py` | 参数解析、config 加载、checkpoint 保存、logging | 待填 |
| 评估入口 | `OpenPCDet/tools/test.py` | checkpoint 加载、distributed eval、result 保存 | 待填 |
| Dataset config | `OpenPCDet/tools/cfgs/dataset_configs/` | dataset root、class names、data processor、augmentor | 待填 |
| Model config | `OpenPCDet/tools/cfgs/` | backbone、dense head、post-processing、NMS | 待填 |
| Dataset 实现 | `OpenPCDet/pcdet/datasets/` | info files、ground truth、prediction dicts | 待填 |
| Model 实现 | `OpenPCDet/pcdet/models/` | detector template、3D backbones、dense heads | 待填 |
| Data augmentation | `OpenPCDet/pcdet/datasets/augmentor/` | GT sampling、flip、rotation、scaling | 待填 |
| Result artifacts | `OpenPCDet/output/` | logs、TensorBoard、`result.pkl`、eval summaries | 待填 |

## Prediction Dictionary 检查清单

每次读 saved prediction output 时，确认这些东西：

- `pred_boxes`
- `pred_scores`
- `pred_labels`
- frame 或 sample identifier
- coordinate frame
- class mapping
- post-processing threshold

## 需要回答的问题

- OpenPCDet 怎么把 model outputs 转成 evaluator inputs？
- NMS 在哪里做？
- score threshold 在哪里生效？
- AV2 evaluator 怎么定义 mAP、AvgR、ECE、MCE、Brier？
- 当前 selected baseline 是哪个路径产出的？

## 当前已知 baseline artifact

Selected baseline：

```text
OpenPCDet/output/argo2_models/cbgs_voxel01_voxelnext/si1_baseline_epoch34_eval/eval/epoch_34/val/si1/result.pkl
```

Metrics：

```text
mAP 0.1397, AvgR 0.1800, internal ECE 0.0624, Brier 0.1665, FPS 15.75
```
