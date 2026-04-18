import pandas as pd
import os
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
import numpy as np


def load_data():
    df = pd.read_csv("data/aggregated/monthly_sales.csv")
    return df


def prepare_data(df):
    # Create date column
    df['ds'] = pd.to_datetime(
        df['year'].astype(str) + '-' + df['month'].astype(str) + '-01'
    )

    df = df.sort_values('ds')

    # Set index
    df.set_index('ds', inplace=True)

    # Fix frequency (important for time series)
    df.index = pd.DatetimeIndex(df.index).to_period('M').to_timestamp()

    ts = df['total_sales'].astype(float)

    return ts


def train_model(ts):
    train_size = int(len(ts) * 0.8)
    train, test = ts[:train_size], ts[train_size:]

    model = ARIMA(train, order=(1, 1, 2))
    model_fit = model.fit()

    predictions = model_fit.forecast(steps=len(test))

    rmse = np.sqrt(mean_squared_error(test, predictions))
    print("ARIMA RMSE:", rmse)

    # Save test vs predicted
    results_df = pd.DataFrame({
        "Date": test.index,
        "Actual": test.values,
        "Predicted": predictions.values
    })

    os.makedirs("outputs/predictions", exist_ok=True)
    results_df.to_csv("outputs/predictions/arima_test_vs_pred.csv", index=False)

    return model_fit, rmse


def forecast(model_fit, ts, steps=12):
    forecast_values = model_fit.forecast(steps=steps)

    # Create future dates
    last_date = ts.index[-1]
    future_dates = pd.date_range(start=last_date, periods=steps+1, freq='MS')[1:]

    forecast_df = pd.DataFrame({
        "Date": future_dates,
        "Forecast": forecast_values.values
    })

    return forecast_df


def save_output(forecast_df):
    os.makedirs("outputs/predictions", exist_ok=True)
    forecast_df.to_csv("outputs/predictions/arima_forecast.csv", index=False)


def save_metrics(rmse):
    os.makedirs("outputs/metrics", exist_ok=True)

    with open("outputs/metrics/arima_metrics.txt", "w") as f:
        f.write(f"RMSE: {rmse}")


#  IMPORTANT: Pipeline function
def run_arima_model():
    df = load_data()
    ts = prepare_data(df)

    model_fit, rmse = train_model(ts)

    forecast_df = forecast(model_fit, ts)

    save_output(forecast_df)
    save_metrics(rmse)

    return rmse


# Clean main execution
if __name__ == "__main__":
    rmse = run_arima_model()
    print(f"\nARIMA Model Completed | RMSE: {rmse}")