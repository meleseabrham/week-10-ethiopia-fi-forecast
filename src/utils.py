import pandas as pd
import os
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    """
    Loads the unified dataset with error handling.
    """
    if not os.path.exists(file_path):
        st.error(f"Data file not found at: {file_path}")
        return pd.DataFrame()
    
    try:
        df = pd.read_csv(file_path)
        # Convert date column if it exists
        if 'observation_date' in df.columns:
            df['observation_date'] = pd.to_datetime(df['observation_date'])
        return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()

def get_observations(df, indicator_code=None):
    """
    Filters the dataset for observations, optionally by indicator code.
    """
    if df.empty:
        return df
    
    obs = df[df['record_type'] == 'observation']
    if indicator_code:
        obs = obs[obs['indicator_code'] == indicator_code]
    return obs.sort_values('observation_date')

def get_events(df):
    """
    Filters the dataset for events.
    """
    if df.empty:
        return df
    return df[df['record_type'] == 'event'].sort_values('observation_date')

@st.cache_data
def get_summary_metrics(df):
    """
    Calculates key metrics for the dashboard.
    """
    if df.empty:
        return {}
    
    # Latest account ownership
    acc = get_observations(df, 'account_ownership')
    latest_acc = acc.iloc[-1]['value_numeric'] if not acc.empty else 0
    
    # Latest Telebirr users
    telebirr = get_observations(df, 'telebirr_users_m')
    latest_telebirr = telebirr.iloc[-1]['value_numeric'] if not telebirr.empty else 0
    
    return {
        "latest_account_ownership": latest_acc,
        "latest_telebirr_users": latest_telebirr
    }
