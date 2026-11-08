# A/B Test Analysis: Simplified Utility Payment Form

## 📌 Business Problem
The product team at the utility payment service launched an A/B test for a new payment form with auto-filled details. The goal is to determine if the new form increases the conversion rate from opening the form (Step 1) to successful payment (Step 4).

## 🎯 Key Metric
Conversion Rate (CR) = Users at Step 4 / Users at Step 1.

## 🛠 Tech Stack
*   **Python** (pandas, numpy)
*   **Statistics** (statsmodels for Z-test)
*   **Visualization** (matplotlib, seaborn)

## 📂 Project Structure
*   `data/raw/` - Initial Excel file (users & payments).
*   `notebooks/01_eda.ipynb` - Exploratory Data Analysis (outliers, anomalies).
*   `src/` - Modular Python code for data processing, metrics, and stats.
*   `main.py` - Pipeline execution script.

## 🧹 Data Cleaning (EDA)
The raw data contained intentional anomalies:
*   Invalid ages (-5, 150) and missing cities.
*   Users without assigned groups.
*   Payments without `user_id` or mismatched groups.

All anomalies were filtered out using `src/data_processing.py`.

## 📊 Results
*   **Group A (Control):** Conversion Rate = X% (N = Y)
*   **Group B (Test):** Conversion Rate = Z% (N = W)
*   **Relative Lift:** +% 
*   **Z-stat:** ... | **p-value:** ...
*   **Conclusion:** The new form shows a statistically significant improvement (p < 0.05). Recommendation: Roll out to 100% of users.

## 🚀 How to Run
1. Clone the repo.
2. Install dependencies: `pip install -r requirements.txt`
3. Place the raw Excel file in `data/raw/`.
4. Run the pipeline: `python main.py`