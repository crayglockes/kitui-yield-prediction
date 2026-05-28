# Predictive Modelling for Maize and Bean Yields in Kitui County, Kenya

**Author:** Mocraig Sande  
**Project Members:** Walter Murimi · James Muteti · John Mutisya · Jeremy Kipkurui
**Programme:** B.Sc. Applied Statistics with Computing, Moi University  
**Supervisor:** Prof. Ann Mwangi  
**Academic Year:** 2025/2026  

[![Python](https://img.shields.io/badge/Python-3.10-blue)]()
[![License](https://img.shields.io/badge/License-Academic-green)]()

---

## Project Overview

This capstone project develops and validates predictive models for maize and bean yields among smallholder farmers in Kitui County, Kenya — one of Kenya's most food-insecure arid and semi-arid regions. Four modelling approaches are compared: Multiple Linear Regression (OLS), LASSO Regression, Random Forest, and XGBoost.

**Key Results (Summary):**

| Crop  | Best Model | RMSE (t/ha) | R² |
|-------|-----------|------------|-----|
| Maize | LASSO   | 0.232          | 0.594   |
| Beans | LASSO   | 0.155          | 0.633   |

---

## Data Sources

| Source | Variables | URL |
|--------|-----------|-----|
| Synthetic survey (n=200) | All agronomic & socioeconomic | Generated — see `notebooks/02_synthetic_survey.ipynb` |
| NASA POWER | Rainfall, temp, solar | power.larc.nasa.gov |
| SoilGrids 2.0 | pH, SOC, clay, sand | rest.soilgrids.org |

---

## Repository Structure

```text
kitui-yield-prediction/
├── data/
│   ├── synthetic/        # Synthetic farmer survey (n=200)
│   ├── raw/              # API downloads (gitignored, regenerable)
│   └── processed/        # Merged, clean, feature-engineered
├── notebooks/            # Colab notebooks (numbered, run in order)
├── src/                  # Reusable functions
├── outputs/
│   ├── figures/          # All plots (180–200 dpi PNG)
│   ├── tables/           # Model results, summaries
│   └── maps/             # Interactive HTML maps
├── docs/                 # Questionnaire, codebook, sources
└── tests/                # Pytest unit tests
```

## Reproduce This Project

```bash
# 1. Clone
git clone git@github.com:crayglockes/kitui-yield-prediction.git
cd kitui-yield-prediction

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run notebooks in order (01 → 07) in Google Colab or Jupyter
# 4. Run tests
pytest tests/ -v
```

All random seeds are set to 42. Results are fully reproducible.

---

## Limitations

1. Data are synthetic — calibrated against published distributions but not from an actual field survey. Findings should be validated with primary data before policy application.
2. SoilGrids and NASA POWER data represent 250m–0.5° resolution averages; farm-level soil and microclimate variation is not fully captured.
3. Models are cross-sectional (single season); temporal dynamics of multi-year yield trends are not modelled.

---

## Ethical Statement

Synthetic data generation methodology is fully documented in `notebooks/02_synthetic_survey.ipynb`. No real farmer data was collected without consent. The questionnaire (`docs/questionnaire.md`) represents the intended instrument for future primary data collection under Moi University IREC ethics protocol.
