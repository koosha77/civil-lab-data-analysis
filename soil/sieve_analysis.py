"""
Sieve analysis for soil samples.

Computes the percentage passing each sieve, the characteristic
diameters D10, D30, D60, and derives the coefficients of uniformity
Cu and curvature Cc, following DIN EN ISO 17892-4 / DIN 18123.

Author: Koosha Karamian, THD Deggendorf
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass
class GradationResult:
    d10: float
    d30: float
    d60: float
    cu: float
    cc: float
    classification: str


def percent_passing(sieve_mm: list[float], retained_g: list[float]) -> list[float]:
    total = sum(retained_g)
    cumulative = 0.0
    passing = []
    for r in retained_g:
        cumulative += r
        passing.append(100.0 * (1.0 - cumulative / total))
    return passing


def interp_d(sieve_mm: list[float], passing_pct: list[float], target: float) -> float:
    order = np.argsort(passing_pct)
    p = np.array(passing_pct)[order]
    s = np.log10(np.array(sieve_mm)[order])
    return float(10 ** np.interp(target, p, s))


def classify(cu: float, cc: float) -> str:
    if cu >= 6 and 1 <= cc <= 3:
        return "Well graded (W)"
    return "Poorly / gap graded (P)"


def analyze(sieve_mm: list[float], retained_g: list[float]) -> GradationResult:
    passing = percent_passing(sieve_mm, retained_g)
    d10 = interp_d(sieve_mm, passing, 10)
    d30 = interp_d(sieve_mm, passing, 30)
    d60 = interp_d(sieve_mm, passing, 60)
    cu = d60 / d10
    cc = (d30 ** 2) / (d10 * d60)
    return GradationResult(d10, d30, d60, cu, cc, classify(cu, cc))


if __name__ == "__main__":
    sieves   = [16.0, 8.0, 4.0, 2.0, 1.0, 0.5, 0.25, 0.125, 0.063]
    retained = [ 5.0, 25.0, 60.0, 90.0, 70.0, 50.0, 40.0, 30.0, 20.0]
    res = analyze(sieves, retained)
    print(f"D10 = {res.d10:.3f} mm")
    print(f"D30 = {res.d30:.3f} mm")
    print(f"D60 = {res.d60:.3f} mm")
    print(f"Cu  = {res.cu:.2f}")
    print(f"Cc  = {res.cc:.2f}")
    print(f"Gradation: {res.classification}")
