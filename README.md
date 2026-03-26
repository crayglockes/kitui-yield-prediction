# Predictive Modelling for Maize and Bean Yields in Kitui County, Kenya

**Author:** Your Full Name · Reg. No: Your Reg No  
**Programme:** B.Sc. Applied Statistics with Computing, Moi University  
**Supervisor:** Supervisor Name  
**Academic Year:** 2024/2025  

## Project Overview
This capstone project develops and validates predictive models for maize and bean
yields among smallholder farmers in Kitui County, Kenya.
Four models are compared: OLS, LASSO, Random Forest, and XGBoost.

## Repository Structure
- `data/` — raw, processed and synthetic datasets
- `notebooks/` — Colab notebooks (run in order 01→07)
- `src/` — reusable Python functions
- `outputs/` — figures, tables, maps, reports
- `docs/` — questionnaire, codebook, data dictionary
- `tests/` — pytest unit tests

## Reproduce
```bash
git clone https://github.com/crayglockes/kitui-yield-prediction.git
cd kitui-yield-prediction
pip install -r requirements.txt
```
All random seeds set to 42.
