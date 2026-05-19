"""
Concrete compressive strength analysis.

Reads cube test results, applies a cube-to-cylinder conversion factor
based on DIN EN 206 / EN 1992, computes characteristic strength fck
and classifies the concrete into a strength class (C12/15 ... C50/60).

Author: Koosha Karamian
Master's program, Civil & Environmental Engineering
Technische Hochschule Deggendorf
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from statistics import mean, stdev

import pandas as pd

# Cube (150 mm) to cylinder (150/300 mm) conversion factor (EN 206)
CUBE_TO_CYLINDER = 0.80

# Strength classes (fck_cylinder, fck_cube) in N/mm^2
STRENGTH_CLASSES = [
    ("C12/15", 12, 15),
    ("C16/20", 16, 20),
    ("C20/25", 20, 25),
    ("C25/30", 25, 30),
    ("C30/37", 30, 37),
    ("C35/45", 35, 45),
    ("C40/50", 40, 50),
    ("C45/55", 45, 55),
    ("C50/60", 50, 60),
]


@dataclass
class StrengthResult:
    mean_cube: float
    std_cube: float
    fck_cube: float       # characteristic cube strength
    fck_cyl: float        # characteristic cylinder strength
    strength_class: str


def characteristic_strength(values_mpa: list[float], k: float = 1.48) -> float:
    """Estimate 5%-fractile characteristic strength: f_ck = f_mean - k * s."""
    if len(values_mpa) < 2:
        raise ValueError("Need at least two specimens.")
    return mean(values_mpa) - k * stdev(values_mpa)


def classify(fck_cyl: float) -> str:
    chosen = STRENGTH_CLASSES[0][0]
    for name, fck, _ in STRENGTH_CLASSES:
        if fck_cyl >= fck:
            chosen = name
    return chosen


def analyze(cube_strengths_mpa: list[float]) -> StrengthResult:
    fck_cube = characteristic_strength(cube_strengths_mpa)
    fck_cyl = fck_cube * CUBE_TO_CYLINDER
    return StrengthResult(
        mean_cube=mean(cube_strengths_mpa),
        std_cube=stdev(cube_strengths_mpa),
        fck_cube=fck_cube,
        fck_cyl=fck_cyl,
        strength_class=classify(fck_cyl),
    )


if __name__ == "__main__":
    # Example dataset: 28-day cube strengths in N/mm^2
    cubes = [38.2, 41.5, 39.7, 42.1, 40.0, 37.8, 41.0]
    result = analyze(cubes)
    print(f"Mean cube strength : {result.mean_cube:.2f} N/mm^2")
    print(f"Std deviation      : {result.std_cube:.2f} N/mm^2")
    print(f"f_ck,cube          : {result.fck_cube:.2f} N/mm^2")
    print(f"f_ck,cyl           : {result.fck_cyl:.2f} N/mm^2")
    print(f"Strength class     : {result.strength_class}")
