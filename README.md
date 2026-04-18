# 📦 Supply Chain Demand Forecasting

## 📌 Project Overview

This project focuses on forecasting monthly sales in a retail supply chain using time series techniques. The goal is to predict future demand and compare traditional statistical models with deep learning approaches.

---

## 🎯 Objectives

* Perform data aggregation using SQL
* Build time series forecasting models
* Compare ARIMA and LSTM performance
* Evaluate models using RMSE and MAE
* Generate future sales forecasts

---

## 🛠️ Tech Stack

* Python (Pandas, NumPy)
* SQL (PostgreSQL)
* Statsmodels (ARIMA)
* TensorFlow / Keras (LSTM)
* Scikit-learn (RMSE, MAE)

---

## 📊 Data Pipeline

1. Raw sales data stored in database
2. SQL transformations performed:

   * Monthly sales aggregation
   * Running total
   * Moving average (3-month)
   * Growth percentage
3. Exported processed data as CSV
4. Used for model training

---

## 🤖 Models Implemented

### 1. ARIMA Model

* Order: (1,1,2)
* Used as baseline forecasting model
* Best performing model

### 2. LSTM Model

* Sequence length: 3
* Deep learning approach
* Used for comparison

---

## 📈 Model Evaluation

| Model | RMSE | MAE |
| ----- | ---- | --- |
| ARIMA | ~12M | ~9M |
| LSTM  | ~17M | -   |

👉 ARIMA performed better due to structured and limited dataset.

---

## 🔄 How to Run

```bash
pip install -r requirements.txt
python main.py
```

---

## 📂 Project Structure

```
supply_chain_forecasting/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── aggregated/
│
├── src/
│   ├── models/
│   │   ├── arima_model.py
│   │   ├── lstm_model.py
│   │   └── evaluate.py
│   │
│   ├── sql/
│   │   └── aggregations.sql
│
├── outputs/
│   ├── predictions/
│   └── metrics/
│
├── dashboard/
│
├── main.py
├── requirements.txt
└── README.md
```

---

## 📊 Outputs Generated

* Model predictions (ARIMA & LSTM)
* Forecast data for future months
* Model comparison (RMSE)

---

## 🚀 Key Learnings

* Time series forecasting using ARIMA and LSTM
* Model comparison and evaluation
* SQL-based feature engineering
* End-to-end ML pipeline development

---

## 🔮 Future Improvements

* Hyperparameter tuning (SARIMA)
* Add external features (holidays, promotions)
* Deploy model as API
* Build interactive dashboard (Power BI/Tableau)
