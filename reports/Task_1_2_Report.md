# Project Report: Ethiopia Financial Inclusion Forecasting System
**Prepared by:** Selam Analytics Data Science Team  
**Date:** January 31, 2026  
**Status:** Task 1 & 2 Complete

---

## 1. Understanding and Defining the Business Objective

Ethiopia is currently experiencing an unprecedented digital financial transformation. The explosive growth of **Telebirr** (reaching 54 million users since 2021) and the 2023 entry of **M-Pesa** have fundamentally shifted the landscape. However, Global Findex data reveals a paradox: while mobile money registrations are soaring, the formal **Account Ownership Rate** (Access) grew by only 3 percentage points between 2021 and 2024.

### 1.1 Consortium Goals
Selam Analytics has been engaged by a consortium (including the National Bank of Ethiopia, development finance institutions, and mobile money operators) to resolve this complexity. The primary objectives are:
*   **Predictive Forecasting:** Projecting Ethiopia's progress on **Access** (Account Ownership) and **Usage** (Digital Payment Adoption) for the 2025–2027 period.
*   **Driver Analysis:** Identifying the catalytic events—launches, policies, or infrastructure investments—that move these indicators.
*   **Strategic Decision Support:** Providing timely data to inform the National Financial Inclusion Strategy (NFIS-II) goal of 70% inclusion by 2025.

---

## 2. Discussion of Completed Work and Initial Analysis

### 2.1 Task 1: Data Exploration and Enrichment
The foundation of this system is a **Unified Schema** designed to ingest heterogeneous data types into a single analytical pipeline:

*   **Observation:** Measured historical data points (e.g., Findex 49% ownership).
*   **Event:** Discrete regulatory or market changes (e.g., Safaricom market entry).
*   **Impact Link:** Relationship coefficients mapping how an event (like Telebirr launch) flows through to an indicator (Usage) with a specific lag.
*   **Target:** Policy benchmarks (e.g., NBE’s 70% inclusion goal).

**Enrichment:** We enriched the starter set with historical Findex data (2011-2024), real-time operator subscriber counts (Telebirr/M-Pesa), and regional/gender-disaggregated data. This allows for a multi-dimensional view of the "unbanked" population.

**Data Quality Assessment:**
*   **Strength:** High confidence in historical Findex markers and official operator reports.
*   **Gap:** Limited recent granularity on regional (rural vs. urban) "active" usage compared to "registration" numbers.

### 2.2 Task 2: Exploratory Data Analysis (EDA)
Our analysis identified 5 critical insights derived from the data:

1.  **The Slowdown Paradox (2021-2024):** Despite massive Telebirr growth, net account ownership grew only **+3pp**. Visualization of the trajectory shows a flattening curve, suggesting registration does not always equate to a "New-to-Bank" event.
2.  **The Gender Gap:** Women (42%) significantly lag behind Men (57%) in account access. This gap remained persistent across the 2017–2024 period, identifying a core area for policy intervention.
3.  **Urban/Rural Divide:** Financial inclusion is urban-centric (73% vs 43%). The vast majority of the "unbanked" or "under-banked" reside in rural areas where infrastructure acts as a barrier.
4.  **Registered vs. Active Usage:** There is a significant gap between the 54M registered Telebirr accounts and the ~35% digital payment adoption rate. This suggests a large portion of accounts are used for single purposes or remain dormant.
5.  **Event-Indicator Correlation:** Timeline analysis shows that the 2021 Safaricom license award and Telebirr launch were the primary catalysts for infrastructure growth (Usage), but the "Access" needle is harder to move than "Usage" once a user is in the system.

---

## 3. Next Steps and Key Areas of Focus

### 3.1 Task 3: Event Impact Modeling
We will build an **Event-Indicator Association Matrix**. This phase will involve:
*   Correlation testing between the Safaricom entry and mobile money account spikes.
*   Modeling logic to quantify the "Successiveness" of product launches on inclusion rates.
*   **Hypothesis:** Regulatory milestones (like Allowing Non-Banks to offer mobile money) have a higher long-term impact on *Access* than single product launches.

### 3.2 Task 4: Forecasting (2025-2027)
Using the association matrix and historical trends, we will:
*   Generate baseline forecasts for 2025-2027.
*   **Scenario Analysis:** Model "Optimistic" (High adoption of interoperability) vs "Conservative" scenarios.
*   Quantify uncertainty using confidence intervals derived from the variability of Findex history.

### 3.3 Task 5: Dashboard Development
Final findings will be presented via an interactive Streamlit dashboard, featuring:
*   Real-time "What-If" sliders to adjust policy impacts.
*   Visual maps of regional inclusion disparities.
*   Forecasting charts overlaid with confidence bands.

---

## 4. Conclusion
The initial phases have successfully structured the data and identified the critical growth gaps in Ethiopia's financial inclusion journey. While "Usage" is accelerating due to market liberalization, "Access" requires targeted interventions for women and rural populations. The upcoming modeling phase will quantify exactly how much policy changes can shift these metrics.
