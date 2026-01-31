import streamlit as st
import pandas as pd
import sys
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Add src to path to import utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.utils import load_data, get_observations, get_summary_metrics, get_events

st.set_page_config(page_title="Ethiopia FI Forecast", layout="wide")

# Custom CSS for premium look
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🇪🇹 Ethiopia Financial Inclusion Forecasting System")

# Data loading
DATA_PATH = os.path.join(os.path.dirname(__file__), "../data/raw/ethiopia_fi_unified_data.csv")
df = load_data(DATA_PATH)

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Overview", "Analysis Insights", "Forecast Modeling"])

if page == "Overview":
    st.write("## Strategic Dashboard Overview")
    
    if not df.empty:
        metrics = get_summary_metrics(df)
        col1, col2, col3 = st.columns(3)
        
        col1.metric("Account Ownership (2024)", f"{metrics['latest_account_ownership']*100:.1f}%", "+3.0%")
        col2.metric("Mobile Money Users", f"{metrics['latest_telebirr_users']}M", "Booming")
        col3.metric("Digital Payments", "35%", "Emerging")

        st.write("---")
        
        # Quick Plot
        st.write("### Account Ownership Trajectory")
        obs_acc = get_observations(df, 'account_ownership')
        if not obs_acc.empty:
            fig, ax = plt.subplots(figsize=(10, 4))
            sns.lineplot(data=obs_acc, x='observation_date', y='value_numeric', marker='o', ax=ax, color='#1f77b4', linewidth=3)
            ax.set_title("Historical Growth (2011-2024)", fontweight='bold')
            ax.set_ylabel("Ownership Rate")
            ax.set_ylim(0, 0.6)
            st.pyplot(fig)
    else:
        st.warning("Data not available. Please ensure data/raw/ethiopia_fi_unified_data.csv exists.")

elif page == "Analysis Insights":
    st.write("## Exploratory Data Analysis Insights")
    st.markdown("""
    - **Slowdown Phenomenon:** Significant lag between user registration (54M) and actual bank account growth.
    - **Gender Gap:** 15% disparity between male and female ownership.
    - **Urban Bias:** 73% urban vs 43% rural inclusion.
    """)
    
    if not df.empty:
        with st.expander("View Raw Observations"):
            st.dataframe(df[df['record_type']=='observation'].head(10))

elif page == "Forecast Modeling":
    st.write("## Forecasting 2025-2027")
    st.info("Task 3 & 4: Predictive modeling in progress. Stay tuned for Event-Impact simulation.")
    st.write("### Policy Scenario Simulator (Preview)")
    impact = st.slider("Select Policy Impact Magnitude", 0.0, 1.0, 0.5)
    st.write(f"Adjusted forecast based on {impact} impact coefficient.")
