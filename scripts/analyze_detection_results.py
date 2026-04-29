"""Detection result 分析入口。

用途：以后用这个脚本读取 OpenPCDet 的 `result.pkl`，统计预测框、分数、
类别、frame id 等信息。当前只是作品集占位文件，真正实现可以后续逐步补。
"""

from __future__ import annotations


def summarize_result_pickle() -> None:
    """待填: 读取并总结 `result.pkl` 里的 boxes、scores、labels、frame ids。"""
    raise NotImplementedError("第 1 阶段填写：result.pkl inspection。")


if __name__ == "__main__":
    print("作品集占位脚本：后续用于 OpenPCDet result.pkl inspection。")
