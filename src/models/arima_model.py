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

    # Fix frequency warning (important)
    df.index = pd.DatetimeIndex(df.index).to_period('M').to_timestamp()

    # Target variable
    ts = df['total_sales'].astype(float)

    return ts


def train_model(ts):
    # Split data (train/test)
    train_size = int(len(ts) * 0.8)
    train, test = ts[:train_size], ts[train_size:]

    # Improved ARIMA order
    model = ARIMA(train, order=(1, 1, 2))
    model_fit = model.fit()

    # Forecast on test set
    predictions = model_fit.forecast(steps=len(test))

    # RMSE
    rmse = np.sqrt(mean_squared_error(test, predictions))
    print("RMSE:", rmse)

    results_df = pd.DataFrame({
        "Date": test.index,
        "Actual": test.values,
        "Predicted": predictions.values
    })

    os.makedirs("outputs/predictions", exist_ok=True)
    results_df.to_csv("outputs/predictions/arima_test_vs_pred.csv", index=False)
    return model_fit, rmse


def forecast(model_fit):
    forecast = model_fit.forecast(steps=12)
    return forecast


def save_output(forecast):
    os.makedirs("outputs/predictions", exist_ok=True)

    forecast_df = forecast.reset_index()
    forecast_df.columns = ['Date', 'Forecast']

    forecast_df.to_csv("outputs/predictions/arima_forecast.csv", index=False)


def save_metrics(rmse):
    os.makedirs("outputs/metrics", exist_ok=True)

    with open("outputs/metrics/arima_metrics.txt", "w") as f:
        f.write(f"RMSE: {rmse}")


if __name__ == "__main__":
    df = load_data()
    ts = prepare_data(df)

    model_fit, rmse = train_model(ts)

    forecast_values = forecast(model_fit)

    print("\nForecast:\n", forecast_values)

    save_output(forecast_values)
    save_metrics(rmse)

    print("\nARIMA Model Completed ")