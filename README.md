# Ethiopia Financial Inclusion Forecasting System

## Business Need
You are a Data Scientist at Selam Analytics, a financial technology consulting firm specializing in emerging markets. Selam Analytics has been engaged by a consortium of stakeholders to develop a financial inclusion forecasting system.

The consortium wants to understand:
1. What drives financial inclusion in Ethiopia?
2. How do events like product launches, policy changes, and infrastructure investments affect inclusion outcomes?
3. How did financial inclusion rates change in 2025 and how will it look like in the coming years - 2026 and 2027?

## Project Goal
Build a forecasting system that predicts Ethiopia's progress on two core dimensions of financial inclusion:
- **Access**: Account Ownership Rate
- **Usage**: Digital Payment Adoption Rate

## Unified Schema Definition
The project uses a unified dataset structure (`ethiopia_fi_unified_data.csv`) to handle multiple record types consistently:
- **Observation**: Actual measured values (e.g., % account ownership).
- **Event**: Discrete milestones (e.g., policy launch, product market entry).
- **Target**: Official policy goals (e.g., 70% inclusion by 2025).
- **Impact Link**: Modeled relationships linking events to indicators via `parent_id`.

## Directory Structure
- `data/`: Raw and processed data
- `notebooks/`: Jupyter notebooks for analysis
- `src/`: Source code modules
- `dashboard/`: Interactive dashboard (Streamlit)
- `models/`: Trained models
- `reports/`: Generated analysis reports
- `tests/`: Unit tests

## Completed Tasks

### Task 1: Data Exploration and Enrichment
**Objective**: Understand the starter dataset and enrich it with additional data relative to the forecasting task.
- **Enriched Dataset**: Added historical Findex data (2011-2024), mobile money user stats (Telebirr, M-Pesa), and key policy events.
- **Outputs**:
  - `data/raw/ethiopia_fi_unified_data.csv`: Unified schema containing observations, events, and targets.
  - `data_enrichment_log.md`: Detailed log of all added data sources and values.
  - `notebooks/01-task1-data-exploration.ipynb`: Initial data profiling and understanding.

### Task 2: Exploratory Data Analysis (EDA)
**Objective**: Analyze the data to understand patterns and factors influencing financial inclusion.
- **Key Insights**:
  - **Account Ownership vs Usage**: Significant gap between account ownership (49%) and active usage, despite massive mobile money registration numbers.
  - **Gender Gap**: Persistent gap with Men (57%) significantly outperforming Women (42%) in account ownership.
  - **Event Impact**: Visualized timeline showing correlation between Telebirr launch (2021) and subsequent user base growth, though formal account inclusion lags.
  - **Urban/Rural Divide**: Financial inclusion remains heavily skewed towards urban centers (73% vs 43%).
- **Outputs**:
  - `notebooks/02-task2-eda.ipynb`: Comprehensive EDA with visualizations.
  - `reports/task2_insights.md`: Summary of 5 key strategic insights.
  - `reports/figures/`: Generated plots (Access Trajectory, Data Coverage, Event Timeline).

### Task 3: Event Impact Modeling
**Objective**: Quantify how events (Policies, Product Launches) affect key indicators.
- **Key Findings**: modeled the "Access vs Usage" disconnect. Confirmed that while Mobile Money (Telebirr) launch drives massive immediate Usage (Mag 0.9, Lag 0), it has a much smaller, lagged effect on Formal Account Ownership (Mag 0.2, Lag 24).
- **Outputs**:
  - `notebooks/03-task3-impact-modeling.ipynb`: Validation of impact hypotheses.
  - `reports/task3_methodology.md`: Documentation of the Event-Indicator Association Matrix.
  - `data/raw/ethiopia_fi_unified_data.csv`: Updated with validated Impact Links.

### Task 4: Forecasting Access and Usage
**Objective**: Project key indicators for 2025-2027 with uncertainty quantification.
- **Key Findings**: Forecasting a "Status Quo" growth to **52% Account Ownership by 2025**, missing the 70% NFIS-II target. Optimistic scenario reaches **62% by 2027**.
- **Outputs**:
  - `notebooks/04-task4-forecasting.ipynb`: Logistic growth models and scenario generation.
  - `reports/task4_forecast_results.md`: Detailed forecast tables and policy recommendations.

### Task 5: Dashboard Development
**Objective**: Interactive visualization of insights and forecasts.
- **Features**:
  - **Executive Overview**: Real-time metrics and target gap analysis.
  - **Trends**: Deep dive into Gender Gap and Mobile Money growth.
  - **Forecast Simulator**: Interactive slider to adjust growth parameters (k) and policy boosts.
  - **Projections**: Official scenario tables and answers to consortium questions.
- **Outputs**:
  - `dashboard/app.py`: Full Streamlit application code.

## Setup & Running
1. Install dependencies: `python -m streamlit run dashboard/app.py`
2. **Run Dashboard**:
   ```bash
   streamlit run dashboard/app.py
   ```
3. Run Tests: `pytest`
