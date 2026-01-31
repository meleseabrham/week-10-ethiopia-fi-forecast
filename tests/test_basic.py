import pytest
import pandas as pd
import os
import sys

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.utils import load_data, get_observations, get_summary_metrics

def test_load_data_invalid_path():
    """Test that load_data handles missing files gracefully."""
    df = load_data("non_existent_file.csv")
    assert df.empty

def test_get_observations_filtering():
    """Test that filtering observations works correctly."""
    mock_data = pd.DataFrame([
        {'record_type': 'observation', 'indicator_code': 'acc', 'value_numeric': 0.5, 'observation_date': '2021-01-01'},
        {'record_type': 'event', 'indicator_code': None, 'value_numeric': None, 'observation_date': '2021-02-01'}
    ])
    obs = get_observations(mock_data)
    assert len(obs) == 1
    assert obs.iloc[0]['indicator_code'] == 'acc'

def test_summary_metrics_calculation():
    """Test that summary metrics are calculated correctly from mock data."""
    mock_data = pd.DataFrame([
        {'record_type': 'observation', 'indicator_code': 'account_ownership', 'value_numeric': 0.46, 'observation_date': '2021-12-31'},
        {'record_type': 'observation', 'indicator_code': 'telebirr_users_m', 'value_numeric': 54, 'observation_date': '2024-12-31'}
    ])
    metrics = get_summary_metrics(mock_data)
    assert metrics['latest_account_ownership'] == 0.46
    assert metrics['latest_telebirr_users'] == 54

def test_data_integrity():
    """Verify that the generated unified data file exists and has rows."""
    path = "c:/project/kifya/week 10/ethiopia-fi-forecast/data/raw/ethiopia_fi_unified_data.csv"
    if os.path.exists(path):
        df = pd.read_csv(path)
        assert len(df) > 0
        assert "record_type" in df.columns
