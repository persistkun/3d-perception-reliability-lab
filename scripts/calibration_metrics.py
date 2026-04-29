"""Calibration metric entry point for the 3D perception portfolio.

This file is intentionally lightweight for now. The paper-grade calibration
experiments currently live in `posthoc_calibration_search.py` and related WACV
scripts. This module will become the clean portfolio-facing interface for ECE,
Brier score, and reliability-diagram inputs.
"""

from __future__ import annotations


def expected_calibration_error() -> None:
    """TODO: implement a clean saved-prediction ECE calculation."""
    raise NotImplementedError("Fill during Stage 4: reliability analysis.")


def brier_score() -> None:
    """TODO: implement Brier score for matched detection outputs."""
    raise NotImplementedError("Fill during Stage 4: reliability analysis.")


if __name__ == "__main__":
    print(
        "Portfolio placeholder. See scripts/posthoc_calibration_search.py "
        "for the current paper-grade calibration implementation."
    )
