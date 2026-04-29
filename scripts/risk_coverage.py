"""Risk-coverage analysis 入口。

用途：以后把 selective risk / risk-coverage curve 做成一个干净的作品集脚本。
当前 WACV 论文级实现仍在原论文仓库的 `selective_risk_detection.py`。
"""

from __future__ import annotations


def compute_risk_coverage_curve() -> None:
    """待填: 从 saved detections 计算 risk-coverage curve。"""
    raise NotImplementedError("第 4 阶段填写：selective risk analysis。")


if __name__ == "__main__":
    print(
        "作品集占位脚本：当前论文级 selective-risk 实现在 "
        "`selective_risk_detection.py`。"
    )
