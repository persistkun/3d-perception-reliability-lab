"""Calibration metrics 入口。

用途：以后把 ECE、Brier score、reliability diagram 的计算整理成一个干净、
适合展示的脚本。当前 WACV 论文级实现仍在原论文仓库的
`posthoc_calibration_search.py` 等脚本里。
"""

from __future__ import annotations


def expected_calibration_error() -> None:
    """待填: 实现 saved prediction 上的 ECE 计算。"""
    raise NotImplementedError("第 4 阶段填写：reliability analysis。")


def brier_score() -> None:
    """待填: 实现 matched detection outputs 的 Brier score。"""
    raise NotImplementedError("第 4 阶段填写：reliability analysis。")


if __name__ == "__main__":
    print(
        "作品集占位脚本：当前论文级 calibration 实现在 "
        "`posthoc_calibration_search.py`。"
    )
