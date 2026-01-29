import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Ethiopia FI Forecast", layout="wide")

st.title("Ethiopia Financial Inclusion Forecasting System")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Overview", "Data Analysis", "Forecasts"])

if page == "Overview":
    st.write("## Overview")
    st.write("Analysis of financial inclusion trends in Ethiopia, focusing on Account Ownership and Digital Payment Adoption.")
    
    st.info("Data loading not implemented yet.")

elif page == "Data Analysis":
    st.write("## Data Analysis")
    st.write("Exploratory Data Analysis will help understand the drivers of financial inclusion.")

elif page == "Forecasts":
    st.write("## Forecasts")
    st.write("Projections for 2025-2027.")
