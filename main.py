import pandas as pd
import os

from src.models.arima_model import run_arima_model
from src.models.lstm_model import run_lstm_model


def compare_models():
    print("\nRunning ARIMA model...")
    arima_rmse = run_arima_model()

    print("\nRunning LSTM model...")
    lstm_rmse = run_lstm_model()

    # Create comparison table
    comparison_df = pd.DataFrame({
        "Model": ["ARIMA", "LSTM"],
        "RMSE": [arima_rmse, lstm_rmse]
    })

    print("\nModel Comparison:\n")
    print(comparison_df)

    # Save comparison
    os.makedirs("outputs/metrics", exist_ok=True)
    comparison_df.to_csv("outputs/metrics/model_comparison.csv", index=False)

    return comparison_df


if __name__ == "__main__":
    compare_models()