import pytest

def add(x, y):
    return x + y

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

# ── tests/test_pipeline.py ───────────────────────────────────
# Run with: !pytest tests/ -v

import pytest
import pandas as pd
import numpy as np
import sys, os
sys.path.insert(0, '/content/drive/MyDrive/kitui-yield-prediction')

BASE_DIR = '/content/drive/MyDrive/kitui-yield-prediction'

class TestSyntheticData:
    """Tests for synthetic survey dataset."""

    @pytest.fixture(autouse=True)
    def load_data(self):
        self.df = pd.read_csv(f'{BASE_DIR}/data/synthetic/synthetic_survey_n200.csv')

    def test_row_count(self):
        assert len(self.df) == 200, f"Expected 200, got {len(self.df)}"

    def test_no_duplicate_ids(self):
        assert self.df["farmer_id"].nunique() == 200

    def test_maize_yield_range(self):
        assert self.df["maize_yield_tha"].min() >= 0.05
        assert self.df["maize_yield_tha"].max() <= 4.0

    def test_bean_yield_range(self):
        assert self.df["bean_yield_tha"].min() >= 0.01
        assert self.df["bean_yield_tha"].max() <= 2.5

    def test_binary_columns(self):
        for col in ["seed_type","irrigation","extension_access","farmer_group","gender"]:
            unique_vals = set(self.df[col].unique())
            assert unique_vals.issubset({0, 1}), f"{col} has non-binary values: {unique_vals}"

    def test_fertiliser_zero_inflation(self):
        zero_pct = (self.df["fert_rate_kgha"] == 0).mean()
        assert 0.30 <= zero_pct <= 0.60, \
            f"Zero fertiliser % = {zero_pct:.1%}; expected 30–60%"

    def test_subcounty_coverage(self):
        assert self.df["subcounty"].nunique() == 5

    def test_lat_lon_in_kitui(self):
        assert self.df["lat"].between(-1.35, -0.40).all(), "Latitude out of Kitui range"
        assert self.df["lon"].between(37.75, 38.65).all(), "Longitude out of Kitui range"

    def test_no_missing_key_columns(self):
        key_cols = ["maize_yield_tha","bean_yield_tha","chirps_rain_mm","ndvi_mean"]
        for col in key_cols:
            assert self.df[col].isnull().sum() == 0, f"{col} has missing values"


class TestMergedData:
    """Tests for merged and engineered dataset."""

    @pytest.fixture(autouse=True)
    def load_data(self):
        self.df = pd.read_csv(f'{BASE_DIR}/data/processed/merged_clean.csv')

    def test_row_count_preserved(self):
        assert len(self.df) == 200

    def test_engineered_features_exist(self):
        for feat in ["management_index","climate_stress","planting_optimal",
                     "soil_fertility_score","rain_adequacy"]:
            assert feat in self.df.columns, f"Missing engineered feature: {feat}"

    def test_management_index_range(self):
        assert self.df["management_index"].between(0, 1).all()

    def test_climate_stress_range(self):
        assert self.df["climate_stress"].between(0, 1).all()

    def test_no_duplicate_columns(self):
        assert len(self.df.columns) == len(set(self.df.columns)), \
            "Duplicate column names detected"
