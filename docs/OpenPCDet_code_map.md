# OpenPCDet Code Map

Status: placeholder created on 2026-04-29.

Goal: make the OpenPCDet repository understandable enough that a professor, PhD student, or future self can see that I know where training, evaluation, datasets, models, and result artifacts live.

## Repository Areas To Fill

| Area | Path | What I Need To Understand | Notes |
|---|---|---|---|
| Training entry | `OpenPCDet/tools/train.py` | Argument parsing, config loading, checkpoint saving, logging | TODO |
| Evaluation entry | `OpenPCDet/tools/test.py` | Checkpoint loading, distributed eval, result saving | TODO |
| Dataset config | `OpenPCDet/tools/cfgs/dataset_configs/` | Dataset root, class names, data processor, augmentor | TODO |
| Model config | `OpenPCDet/tools/cfgs/` | Backbone, dense head, post-processing, NMS | TODO |
| Dataset implementation | `OpenPCDet/pcdet/datasets/` | Info files, ground truth, prediction dicts | TODO |
| Model implementation | `OpenPCDet/pcdet/models/` | Detector template, 3D backbones, dense heads | TODO |
| Data augmentation | `OpenPCDet/pcdet/datasets/augmentor/` | GT sampling, flips, rotation, scaling | TODO |
| Result artifacts | `OpenPCDet/output/` | Logs, TensorBoard, `result.pkl`, eval summaries | TODO |

## Prediction Dictionary Checklist

For each saved prediction output, identify:

- `pred_boxes`
- `pred_scores`
- `pred_labels`
- frame or sample identifier
- coordinate frame
- class mapping
- post-processing threshold

## Questions To Answer

- How does OpenPCDet convert model outputs into evaluator inputs?
- Where is NMS applied?
- Where are score thresholds applied?
- How does the AV2 evaluator define mAP, AvgR, ECE, MCE, and Brier?
- What exact path produced the current selected baseline result?

## Current Known Baseline Artifact

Selected baseline:

```text
OpenPCDet/output/argo2_models/cbgs_voxel01_voxelnext/si1_baseline_epoch34_eval/eval/epoch_34/val/si1/result.pkl
```

Metrics:

```text
mAP 0.1397, AvgR 0.1800, internal ECE 0.0624, Brier 0.1665, FPS 15.75
```
