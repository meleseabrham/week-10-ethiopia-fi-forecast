import pandas as pd
import os

# Define the schema columns
columns = [
    "record_type", "pillar", "indicator", "indicator_code", "value_numeric",
    "observation_date", "source_name", "source_url", "confidence",
    "category", "parent_id", "related_indicator", "impact_direction",
    "impact_magnitude", "lag_months", "evidence_basis",
    "original_text", "collected_by", "collection_date", "notes"
]

data = []

# Helper to add observation
def add_obs(pillar, indicator, code, value, date, source, url=""):
    data.append({
        "record_type": "observation",
        "pillar": pillar,
        "indicator": indicator,
        "indicator_code": code,
        "value_numeric": value,
        "observation_date": date,
        "source_name": source,
        "source_url": url,
        "confidence": "High",
        "collected_by": "System Init",
        "collection_date": "2026-01-29"
    })

# Helper to add event
def add_event(category, name, date, source):
    data.append({
        "record_type": "event",
        "category": category,
        "indicator": name, # using indicator col for event name
        "observation_date": date,
        "source_name": source,
        "confidence": "High",
        "collected_by": "System Init",
        "collection_date": "2026-01-29"
    })

# Helper to add target
def add_target(pillar, indicator, code, value, date, source):
    data.append({
        "record_type": "target",
        "pillar": pillar,
        "indicator": indicator,
        "indicator_code": code,
        "value_numeric": value,
        "observation_date": date,
        "source_name": source,
        "confidence": "High",
        "collected_by": "System Init",
        "collection_date": "2026-01-29"
    })

# --- Historical Access Data (Global Findex / NBE) ---
add_obs("Access", "Account Ownership", "account_ownership", 0.14, "2011-12-31", "Global Findex")
add_obs("Access", "Account Ownership", "account_ownership", 0.22, "2014-12-31", "Global Findex")
add_obs("Access", "Account Ownership", "account_ownership", 0.35, "2017-12-31", "Global Findex")
add_obs("Access", "Account Ownership", "account_ownership", 0.46, "2021-12-31", "Global Findex")
add_obs("Access", "Account Ownership", "account_ownership", 0.49, "2024-12-31", "Global Findex 2024")

# --- Usage Data (2024) ---
add_obs("Usage", "Mobile Money Account Ownership", "mobile_money_ownership", 0.0945, "2024-12-31", "Global Findex 2024")
add_obs("Usage", "Made or received digital payment", "digital_payment_adoption", 0.35, "2024-12-31", "Official Report")
add_obs("Usage", "Used account to receive wages", "receive_wages", 0.15, "2024-12-31", "Official Report")

# --- Enriched Data (Search Results) ---
# Gender Gap
add_obs("Access", "Account Ownership (Men)", "account_ownership_men", 0.57, "2024-12-31", "Shega/Findex Analysis", "https://shega.co/post/ethiopias-financial-inclusion-finding-from-global-findex-2025/")
add_obs("Access", "Account Ownership (Women)", "account_ownership_women", 0.42, "2024-12-31", "Shega/Findex Analysis", "https://shega.co/post/ethiopias-financial-inclusion-finding-from-global-findex-2025/")

# Urban/Rural
add_obs("Access", "Account Ownership (Urban)", "account_ownership_urban", 0.732, "2024-12-31", "RSIS International", "https://www.rsisinternational.org")
add_obs("Access", "Account Ownership (Rural)", "account_ownership_rural", 0.433, "2024-12-31", "RSIS International", "https://www.rsisinternational.org")

# Telebirr Users
add_obs("Infrastructure", "Telebirr Users (Million)", "telebirr_users_m", 54, "2024-12-31", "Ethio Telecom", "https://stockmarket.et")
add_obs("Infrastructure", "Telebirr Users (Million)", "telebirr_users_m", 55, "2025-06-30", "Ethio Telecom Projection", "https://stockmarket.et")
add_obs("Infrastructure", "Telebirr Users (Million)", "telebirr_users_m", 88, "2026-06-30", "Ethio Telecom Forecast", "https://techpoint.africa")

# M-Pesa Users
add_obs("Infrastructure", "M-Pesa Active Users (Million)", "mpesa_users_m", 10, "2025-07-31", "Safaricom Ethiopia", "https://safaricom.co.ke")

# --- Events ---
add_event("product_launch", "Telebirr Launch", "2021-05-11", "Ethio Telecom")
add_event("product_launch", "M-Pesa Ethiopia Launch", "2023-08-16", "Safaricom")
add_event("policy", "NFIS-II Strategy Launch", "2021-01-01", "NBE")
add_event("policy", "Ethio Telecom Next Horizon Strategy", "2025-07-01", "Ethio Telecom")

# --- Targets ---
add_target("Access", "Account Ownership Target (NFIS-II)", "account_ownership_target", 0.70, "2025-12-31", "NBE")

# --- Impact Links (Simplified for now) ---
# --- Impact Links (Validated in Task 3) ---
impact_strategies = [
    # Telebirr Impacts
    {"parent_id": "Telebirr Launch", "related_indicator": "account_ownership", "dir": "Positive", "mag": 0.2, "lag": 24, "type": "observation", "note": "Slow conversion to formal accounts"},
    {"parent_id": "Telebirr Launch", "related_indicator": "telebirr_users_m", "dir": "Positive", "mag": 0.9, "lag": 0, "type": "observation", "note": "Direct adoption"},
    
    # M-Pesa Impacts
    {"parent_id": "M-Pesa Ethiopia Launch", "related_indicator": "account_ownership", "dir": "Positive", "mag": 0.1, "lag": 18, "type": "observation", "note": "Competition effect"},
    {"parent_id": "M-Pesa Ethiopia Launch", "related_indicator": "mpesa_users_m", "dir": "Positive", "mag": 0.8, "lag": 0, "type": "observation", "note": "Direct adoption"},
    
    # Policy Impacts
    {"parent_id": "NFIS-II Strategy Launch", "related_indicator": "account_ownership", "dir": "Positive", "mag": 0.4, "lag": 36, "type": "target", "note": "Long term policy effect on rural infra"}
]

for imp in impact_strategies:
    data.append({
        "record_type": "impact_link",
        "parent_id": imp["parent_id"],
        "related_indicator": imp["related_indicator"],
        "impact_direction": imp["dir"],
        "impact_magnitude": imp["mag"],
        "lag_months": imp["lag"],
        "confidence": "Medium",
        "evidence_basis": "Task 3 Modeling",
        "notes": imp["note"],
        "collected_by": "Task 3 Model",
        "collection_date": "2026-01-31"
    })


try:
    df = pd.DataFrame(data, columns=columns)
    output_path = "c:/project/kifya/week 10/ethiopia-fi-forecast/data/raw/ethiopia_fi_unified_data.csv"
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    df.to_csv(output_path, index=False)
    print(f"Successfully created {output_path} with {len(df)} records.")
except Exception as e:
    print(f"CRITICAL ERROR during data initialization: {e}")
    exit(1)
