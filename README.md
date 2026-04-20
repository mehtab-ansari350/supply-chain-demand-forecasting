# Supply Chain Demand Forecasting & Analytics

 ![Dashboard](dashboard/dashboard.png)

---

##  Project Overview

This project delivers an **end-to-end supply chain forecasting pipeline** to predict future monthly sales and support data-driven decision-making.

It combines **SQL-based data engineering**, **time series modeling**, and **business intelligence dashboards** to simulate a real-world analytics workflow used in enterprise environments.

---

##  Business Problem

Accurate demand forecasting is critical for:

* Inventory optimization
* Reducing stockouts and overstocking
* Improving supply chain efficiency

This project aims to:

* Forecast future demand
* Compare multiple forecasting techniques
* Provide actionable insights through dashboards

---

##  Data Source

The project uses a **retail transactional dataset** representing historical sales activity across multiple time periods.

### 🔹 Raw Data

* Transaction-level sales records
* Includes attributes such as:

  * Order date
  * Sales amount
  * Product-level details

### 🔹 Data Processing Flow

* Raw data stored in structured format
* SQL transformations applied:

  * Monthly aggregation
  * Moving averages
  * Growth percentage
* Processed dataset exported for modeling

---

##  Processed Dataset

The final dataset used for modeling is **monthly aggregated sales data**.

### 🔹 Key Features

* **year** → Year of transaction
* **month** → Month of transaction
* **total_sales** → Total revenue for the month

Stored at:

```
data/aggregated/monthly_sales.csv
```

---

##  End-to-End Pipeline

### 1. Data Engineering (SQL)

* Raw transactional data processed using SQL
* Key transformations:

  * Monthly sales aggregation
  * Moving averages (3-month)
  * Growth percentage calculation
* Output stored for modeling

---

### 2. Data Processing (Python)

* Data cleaning and transformation using modular scripts
* Time series preparation:

  * Datetime indexing
  * Sorting and validation
  * Feature readiness for models

---

### 3. Modeling

#### 🔹 ARIMA Model

* Configuration: (1,1,2)
* Statistical time series model
* Captures trend and seasonality efficiently

#### 🔹 LSTM Model

* Deep learning approach
* Sequence length: 3
* Captures temporal dependencies

---

### 4. Model Evaluation

| Model | RMSE    |
| ----- | ------- |
| ARIMA | ~12.01M |
| LSTM  | ~17.47M |

**Key Insight:**
ARIMA outperforms LSTM due to structured and relatively small dataset.

---

### 5. Forecasting

* Generated next **12 months sales forecast**
* Saved outputs for business and visualization

---

### 6. Business Intelligence Dashboard (Power BI)

The dashboard provides:

* Actual vs Predicted comparison
* Future sales forecast
* Monthly sales trend
* Model performance comparison (RMSE)
* Final model selection insight

**Final Decision:**
ARIMA selected as production model based on lower RMSE

---

##  Tech Stack

### Programming & Libraries

* Python (Pandas, NumPy)
* Scikit-learn (Evaluation metrics)
* Statsmodels (ARIMA)
* TensorFlow / Keras (LSTM)

### Data Engineering

* SQL (PostgreSQL)

### Visualization

* Power BI

---

##  Project Structure

```
supply_chain_forecasting/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── aggregated/
│
├── notebooks/
│   ├── 01_eda.ipynb
│   └── 02_feature_engineering.ipynb
│
├── src/
│   ├── data_processing/
│   │   ├── clean_data.py
│   │   └── transform_data.py
│   │
│   ├── models/
│   │   ├── arima_model.py
│   │   ├── lstm_model.py
│   │   └── evaluate.py
│   │
│   ├── sql/
│   │   ├── create_tables.sql
│   │   ├── transformations.sql
│   │   └── aggregations.sql
│
├── outputs/
│   ├── predictions/
│   └── metrics/
│
├── dashboard/powerbi/image.png
│
├── main.py
├── requirements.txt
└── README.md
```

---

##  How to Run

```bash
# Install dependencies
pip install -r requirements.txt

# Run full pipeline
python main.py
```

---

##  Outputs

* Model predictions (ARIMA & LSTM)
* Forecast for next 12 months
* Model comparison metrics
* Power BI dashboard insights

---

##  Key Learnings

* Built complete **data science pipeline (SQL → ML → BI)**
* Compared **statistical vs deep learning models**
* Learned when simpler models outperform complex ones
* Designed **business-ready dashboards**
* Structured project like real-world production systems

---

##  Future Improvements

* Implement SARIMA for seasonality handling
* Add external features (holidays, promotions, events)
* Automate pipeline using workflow tools
* Deploy model as API (FastAPI / Flask)
* Integrate real-time dashboard updates

---

##  Conclusion

This project demonstrates a **production-style data science workflow**, combining:

* Data engineering
* Machine learning
* Business analytics

to deliver actionable insights for supply chain optimization.
