import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error


def evaluate_model(path):
    df = pd.read_csv(path)

    print("Columns in file:", df.columns)  

    y_true = df['Actual']
    y_pred = df['Predicted']

    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    mae = mean_absolute_error(y_true, y_pred)

    print(f"RMSE: {rmse}")
    print(f"MAE: {mae}")

    return rmse, mae


if __name__ == "__main__":
    evaluate_model("outputs/predictions/arima_test_vs_pred.csv")