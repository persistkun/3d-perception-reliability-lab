# AV2 Dataset Notes

Status: placeholder created on 2026-04-29.

Goal: document Argoverse 2 data layout, conversion assumptions, coordinate frames, class mapping, and evaluation artifacts used in the reliability project.

## Dataset Scope

Current project: Argoverse 2 LiDAR 3D detection reliability audit.

Important split currently used:

```text
Full prepared validation, sample interval 1
```

Selected baseline result:

```text
VoxelNeXt epoch34 selected:
mAP 0.1397, AvgR 0.1800, internal ECE 0.0624, Brier 0.1665, FPS 15.75
```

## Items To Fill

- [ ] Raw AV2 directory layout.
- [ ] OpenPCDet prepared data directory layout.
- [ ] Info file names and sample counts.
- [ ] Class list and class mapping.
- [ ] Coordinate system notes.
- [ ] Box convention notes.
- [ ] Matching rule used by diagnostic scripts.
- [ ] Difference between OpenPCDet internal ECE and diagnostic post-hoc ECE.

## Diagnostic Matching Rule

Current supplement notes:

- score threshold: `> 0.3`
- matching: 2m center-distance
- assignment: class-consistent greedy matching

## Common Failure Modes To Track

- far-range detections
- vulnerable road users
- sparse point clouds
- long-tail classes
- high-confidence false positives
- missed small objects
