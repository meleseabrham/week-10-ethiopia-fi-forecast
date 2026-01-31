import streamlit as st
import pandas as pd
import sys
import os
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Add src to path to import utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.utils import load_data, get_observations, get_summary_metrics, get_events

# --- Page Config ---
st.set_page_config(
    page_title="Ethiopia Financial Inclusion Forecast",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS Styling ---
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stMetric {
        background-color: white;
        padding: 15px;
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .metric-container { display: flex; justify-content: space-between; gap: 20px; }
    h1, h2, h3 { color: #2c3e50; }
    .insight-box {
        background-color: #e8f4fd;
        padding: 20px;
        border-radius: 5px;
        border-left: 5px solid #2196f3;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --- Load Data ---
DATA_PATH = os.path.join(os.path.dirname(__file__), "../data/raw/ethiopia_fi_unified_data.csv")
df = load_data(DATA_PATH)

# --- Sidebar ---
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/thumb/7/71/Flag_of_Ethiopia.svg/2560px-Flag_of_Ethiopia.svg.png", width=100)
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Executive Overview", "Trends & Analysis", "Forecast Simulator", "Inclusion Projections"])

st.sidebar.write("---")
st.sidebar.info("**Selam Analytics**\nTask 5: Final Dashboard\nv1.0.0")

# --- Helper: Logistic Model for Sidebar ---
def logistic_forecast(t, t0=2020, L=0.85, k=0.5):
    return L / (1 + np.exp(-k * (t - t0)))

# --- Page 1: Executive Overview ---
if page == "Executive Overview":
    st.title("🇪🇹 Ethiopia Financial Inclusion Dashboard")
    st.markdown("### Strategic Overview of Access (Account Ownership) & Usage (Digital Payments)")
    
    # Metrics
    if not df.empty:
        metrics = get_summary_metrics(df)
        
        # Latest Calculations
        acc_own = metrics.get('latest_account_ownership', 0)
        telebirr = metrics.get('latest_telebirr_users', 0)
        target_gap = 0.70 - acc_own
        
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Account Ownership", f"{acc_own*100:.1f}%", "+3.0% (3yr)", delta_color="normal")
        col2.metric("Target Gap (2025)", f"{target_gap*100:.1f}pp", "Off Track", delta_color="inverse")
        col3.metric("Mobile Money Users", f"{telebirr}M", "+54M (3yr)")
        col4.metric("Digital Payment Usage", "35%", "High Growth")
    
    st.write("---")
    
    # Key Insight Box
    st.markdown("""
        <div class="insight-box">
        <h4>🚨 Key Strategic Insight</h4>
        <p>While <b>Usage</b> is booming (driven by Telebirr/M-Pesa), <b>Formal Access</b> is lagging. 
        Forecasts indicate we will reach ~52% Account Ownership by 2025, missing the 70% NFIS-II target unless policy shifts redefine 'Inclusion'.</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Quick Plot: Trajectory
    st.subheader("Trajectory vs Target")
    acc_obs = get_observations(df, 'account_ownership')
    
    if not acc_obs.empty:
        fig, ax = plt.subplots(figsize=(10, 4))
        # History
        sns.lineplot(data=acc_obs, x='observation_date', y='value_numeric', marker='o', ax=ax, label='Historical', color='#1f77b4', linewidth=2.5)
        # Target
        plt.axhline(0.70, color='red', linestyle='--', label='NFIS-II Target (70%)')
        plt.text(acc_obs['observation_date'].iloc[0], 0.71, " Target", color='red')
        
        ax.set_ylim(0, 0.8)
        ax.set_title("Account Ownership: History vs Goal")
        st.pyplot(fig)


# --- Page 2: Trends ---
elif page == "Trends & Analysis":
    st.title("📊 Historical Trends & Drivers")
    
    tab1, tab2 = st.tabs(["Account Ownership", "Infrastructure Enablers"])
    
    with tab1:
        st.subheader("Gender & Regional Gaps")
        col1, col2 = st.columns(2)
        
        # Gender Gap
        acc_men = get_observations(df, 'account_ownership_men')
        acc_women = get_observations(df, 'account_ownership_women')
        
        if not acc_men.empty and not acc_women.empty:
            fig_g, ax_g = plt.subplots()
            ax_g.bar(['Men', 'Women'], [acc_men.iloc[-1]['value_numeric'], acc_women.iloc[-1]['value_numeric']], color=['#3498db', '#e74c3c'])
            ax_g.set_title("Gender Gap (2024)")
            ax_g.set_ylim(0, 0.7)
            col1.pyplot(fig_g)
        
        # Urban Rural
        col2.write("**Urban vs Rural Divide**")
        col2.progress(73, text="Urban Inclusion: 73%")
        col2.progress(43, text="Rural Inclusion: 43%")
        col2.caption("Significant infrastructure barrier in rural regions.")

    with tab2:
        st.subheader("The Rise of Mobile Money")
        tb = get_observations(df, 'telebirr_users_m')
        if not tb.empty:
            fig, ax = plt.subplots(figsize=(10, 5))
            sns.lineplot(data=tb, x='observation_date', y='value_numeric', marker='s', color='orange', linewidth=3, ax=ax)
            ax.set_title("Telebirr User Base Growth (Millions)")
            ax.set_ylabel("Users (Millions)")
            st.pyplot(fig)


# --- Page 3: Forecast Simulator ---
elif page == "Forecast Simulator":
    st.title("🔮 Interactive Forecast Model (2025-2027)")
    
    col1, col2 = st.columns([1, 3])
    
    with col1:
        st.markdown("### Model Parameters")
        k_param = st.slider("Growth Rate (k)", 0.1, 1.0, 0.5, 0.05, help="Speed of adoption curve.")
        saturation = st.slider("Market Ceiling (L)", 0.6, 1.0, 0.85, 0.05, help="Max potential population reachable.")
        policy_boost = st.checkbox("Apply NFIS-II Policy Boost?", value=False)
        
    with col2:
        # Generate dynamic forecast
        years = np.arange(2011, 2028)
        forecast_vals = logistic_forecast(years, k=k_param, L=saturation)
        
        if policy_boost:
            # Add simple linear boost post-2024
            boost = np.array([0.015 * (y - 2024) if y > 2024 else 0 for y in years])
            forecast_vals += boost
            
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Historical Data
        acc_obs = get_observations(df, 'account_ownership')
        acc_obs['year'] = pd.to_datetime(acc_obs['observation_date']).dt.year
        ax.scatter(acc_obs['year'], acc_obs['value_numeric'], color='black', s=100, label='Historical Data', zorder=5)
        
        # Forecast
        ax.plot(years, forecast_vals, color='green', linestyle='--', linewidth=3, label='Forecast Scenario')
        
        # Target
        ax.axhline(0.70, color='red', linestyle=':', label='2025 Target')
        
        ax.set_ylim(0, 1.0)
        ax.set_title(f"Dynamic Forecast (k={k_param}, Ceiling={saturation})")
        ax.legend()
        ax.grid(True, alpha=0.3)
        st.pyplot(fig)
        
        val_2025 = forecast_vals[years == 2025][0]
        st.metric("Predicted 2025 Ownership", f"{val_2025*100:.1f}%")


# --- Page 4: Inclusion Projections (Consortium View) ---
elif page == "Inclusion Projections":
    st.title("📑 Official Inclusion Projections")
    
    st.write("### Progress Towards Goals")
    
    # Scenario Table
    scenarios = pd.DataFrame({
        "Year": [2025, 2026, 2027],
        "Conservative (Status Quo)": ["52.3%", "55.1%", "58.0%"],
        "Optimistic (Policy Success)": ["53.8%", "58.1%", "62.5%"],
        "Target": ["70%", "N/A", "N/A"]
    })
    st.table(scenarios)
    
    st.subheader("Consortium Questions Answered")
    st.markdown("""
    1.  **What drives inclusion?** Currently, **Mobile Money (Usage)** is the driver, but it is not converting efficiently to **Account Ownership (Access)**.
    2.  **How do events affect outcomes?** Product launches (Telebirr) scale usage instantly, but policy changes (NFIS) take 24-36 months to impact formal access.
    3.  **Will we hit the 2025 target?** Highly unlikely (forecast ~52%). Recommendation: Reclassify 'Level 2' verified mobile wallets as 'Accounts' to bridge the gap.
    """)
    
    # Download
    csv = df.to_csv(index=False)
    st.download_button("Download Unified Dataset (CSV)", data=csv, file_name="ethiopia_fi_forecast_data.csv", mime="text/csv")
