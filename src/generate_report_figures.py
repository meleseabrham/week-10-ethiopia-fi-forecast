import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Ensure figure directory exists
os.makedirs('reports/figures', exist_ok=True)

# Load data
df = pd.read_csv('data/raw/ethiopia_fi_unified_data.csv')
obs = df[df['record_type'] == 'observation']

# --- 1. Urban vs Rural Plot ---
urban = obs[obs['indicator_code'] == 'account_ownership_urban']
rural = obs[obs['indicator_code'] == 'account_ownership_rural']

if not urban.empty and not rural.empty:
    plt.figure(figsize=(8, 5))
    categories = ['Urban', 'Rural']
    values = [urban.iloc[-1]['value_numeric'], rural.iloc[-1]['value_numeric']]
    sns.barplot(x=categories, y=values, palette='coolwarm')
    plt.title('The Geographic Divide: Account Ownership (2024)')
    plt.ylabel('Ownership Rate')
    plt.ylim(0, 1)
    for i, v in enumerate(values):
        plt.text(i, v + 0.02, f"{v*100:.1f}%", ha='center', fontweight='bold')
    plt.savefig('reports/figures/eda_urban_rural_divide.png')
    plt.close()

# --- 2. Usage Patterns (Digital Payments vs Wages) ---
usage = obs[obs['indicator_code'] == 'digital_payment_adoption']
wages = obs[obs['indicator_code'] == 'receive_wages']

if not usage.empty and not wages.empty:
    plt.figure(figsize=(8, 5))
    patterns = ['Digital Payments Made/Received', 'Wages Received Digitally']
    vals = [usage.iloc[-1]['value_numeric'], wages.iloc[-1]['value_numeric']]
    sns.barplot(x=patterns, y=vals, palette='viridis')
    plt.title('Usage Patterns: Transactional vs. Institutional')
    plt.ylabel('Adoption Rate')
    plt.ylim(0, 0.5)
    for i, v in enumerate(vals):
        plt.text(i, v + 0.01, f"{v*100:.1f}%", ha='center', fontweight='bold')
    plt.savefig('reports/figures/eda_usage_patterns.png')
    plt.close()

print("New figures saved to reports/figures/")
