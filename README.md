# civil-lab-data-analysis

Python notebooks and scripts for analyzing civil engineering laboratory data — concrete strength, soil mechanics, and materials testing. Developed alongside my Master's studies in Civil & Environmental Engineering at **Technische Hochschule Deggendorf**.

## Goals

- Provide clean, reproducible analysis pipelines for typical civil engineering lab experiments.
- Practice Python data analysis on real engineering problems (numpy, pandas, matplotlib, scipy).
- Build a reusable toolbox for upcoming master thesis and coursework projects.

## Planned modules

| Module | Topic | Status |
|---|---|---|
| `concrete/` | Compressive strength tests (DIN EN 12390-3), cube vs. cylinder conversion | Planned |
| `soil/` | Sieve analysis, Atterberg limits, Proctor compaction | Planned |
| `corrosion/` | KKS (kathodischer Korrosionsschutz) potential measurements | Planned |
| `rehabilitation/` | Carbonation depth & chloride profiles for existing structures | Planned |

## Tech stack

- Python 3.11+
- Jupyter Lab
- pandas, numpy, scipy, matplotlib, seaborn

## Getting started

```bash
git clone https://github.com/koosha77/civil-lab-data-analysis.git
cd civil-lab-data-analysis
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter lab
```

## Standards & references

- DIN EN 12390 — Testing hardened concrete
- DIN 18196 — Soil classification
- HOAI / DIN 276 — German construction cost framework (context for rehab studies)

## License

MIT — see [LICENSE](LICENSE).
