# Task 3: Event Impact Modeling Methodology

## 1. Objective
To quantify the relationship between discrete events (Product Launches, Policies) and continuous financial inclusion indicators (Account Ownership, Usage) for the purpose of forecasting.

## 2. Methodology: Event-Indicator Matrix
We utilize an **Association Matrix** approach where each Event $E$ exerts a pressure on Indicator $I$ defined by:

$$ \Delta I_t = \sum (Magnitude_{E} \times Decay(t - T_E)) $$

Where:
*   **Magnitude**: A coefficient (0.0 - 1.0) representing the potential lift.
*   **Lag/Decay**: The time profile of the impact (Immediate step-change vs. linear ramp vs. S-curve).

### Hypothesized Impacts (The "Priors")
Based on our literature review and expert consultation (simulated), we established the following priors:

| Event | Indicator | Impact | Magnitude | Lag | Rationale |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Telebirr Launch** | Mobile Money Users | Positive | **0.9** (High) | 0 Mo | Direct product adoption. |
| **Telebirr Launch** | Acc. Ownership | Positive | **0.2** (Low) | 24 Mo | Conversion to formal banking is slow; "Walled Garden" effect. |
| **M-Pesa Launch** | Acc. Ownership | Positive | **0.1** (Low) | 18 Mo | Increased competition drives marginal inclusion. |
| **NFIS-II Strategy** | Acc. Ownership | Positive | **0.4** (Med) | 36 Mo | Policy changes take years to trickle down to rural infra. |

## 3. Validation Results (Telebirr Case Study)
We tested the model against the 2021-2024 period:
*   **Predicted**: Sharp rise in usage, flat/slow rise in account ownership.
*   **Observed**: Telebirr users hit 54M, but Account Ownership only grew +3pp (46% -> 49%).
*   **Conclusion**: The model's distinction between "Usage Impact" and "Access Impact" is valid. We must be careful **not** to forecast 1:1 conversion from Mobile Wallets to Bank Accounts.

## 4. Assumptions & Uncertainties
*   **Assumption**: Impact magnitudes are additive (linear superposition). In reality, diminishing returns likely exist.
*   **Uncertainty**: The "Active" rate of new mobile money users is unknown. If 90% are inactive, the true impact on inclusion is lower than modeled.
*   **External Factors**: We assume no major macroeconomic shocks (inflation, instability) that would reverse trends, though these are constant risks in the region.
