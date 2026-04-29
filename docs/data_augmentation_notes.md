# Data Augmentation Notes

Status: placeholder created on 2026-04-29.

Goal: document common point-cloud augmentation methods in OpenPCDet and record any custom experiments.

## Standard Augmentations

- GT sampling:
- Random flip:
- Random rotation:
- Random scaling:
- Translation / noise:

## OpenPCDet Paths

TODO.

## Custom Gaussian Noise Experiment

Status: not started.

Plan:

- [ ] Add Gaussian noise to point coordinates.
- [ ] Insert into data processor or augmentor pipeline.
- [ ] Run smoke test.
- [ ] Compare mAP, calibration, and failure cases.

## Results Log

| Date | Augmentation | Dataset / split | Metric change | Notes |
|---|---|---|---|---|
