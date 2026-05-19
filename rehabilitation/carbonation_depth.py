"""
Carbonation depth prediction for existing concrete structures.

Uses the classical square-root-of-time model:

    x_c(t) = K * sqrt(t)

where x_c is the carbonation depth [mm], t is the age [years]
and K [mm/sqrt(year)] is a material- and environment-dependent
coefficient. Indicative K values for exposure classes (XC1 ... XC4)
are provided below for educational use only.

Author: Koosha Karamian, THD Deggendorf
"""

from __future__ import annotations

import math
from dataclasses import dataclass

# Indicative K values [mm / sqrt(year)] for ordinary Portland cement concrete
# (very rough, for teaching examples only — not for design)
K_VALUES_MM_PER_SQRT_YEAR = {
    "XC1": 1.5,   # dry or permanently wet
    "XC2": 3.0,   # wet, rarely dry
    "XC3": 4.0,   # moderate humidity
    "XC4": 5.0,   # cyclic wet and dry
}


@dataclass
class CarbonationCheck:
    age_years: float
    cover_mm: float
    depth_mm: float
    margin_mm: float
    rebar_safe: bool


def depth(age_years: float, k: float) -> float:
    return k * math.sqrt(age_years)


def time_to_reach_cover(cover_mm: float, k: float) -> float:
    return (cover_mm / k) ** 2


def check(age_years: float, cover_mm: float, exposure: str) -> CarbonationCheck:
    k = K_VALUES_MM_PER_SQRT_YEAR[exposure.upper()]
    d = depth(age_years, k)
    margin = cover_mm - d
    return CarbonationCheck(age_years, cover_mm, d, margin, margin > 0)


if __name__ == "__main__":
    # Example: 35-year-old parking deck, 25 mm cover, XC4 exposure
    r = check(age_years=35, cover_mm=25, exposure="XC4")
    print(f"Carbonation depth at {r.age_years} yr : {r.depth_mm:.1f} mm")
    print(f"Concrete cover                : {r.cover_mm:.1f} mm")
    print(f"Remaining margin              : {r.margin_mm:+.1f} mm")
    print("Rebar still passive" if r.rebar_safe else "Likely depassivated — inspect!")
