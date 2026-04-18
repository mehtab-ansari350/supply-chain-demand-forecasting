import pandas as pd
import numpy as np
import os

from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense


def load_data():
    df = pd.read_csv("data/aggregated/monthly_sales.csv")
    return df


def prepare_data(df):
    df['ds'] = pd.to_datetime(
        df['year'].astype(str) + '-' + df['month'].astype(str) + '-01'
    )

    df = df.sort_values('ds')
    df.set_index('ds', inplace=True)

    ts = df['total_sales'].astype(float)

    return ts


def create_sequences(data, seq_length=3):
    X, y = [], []

    for i in range(len(data) - seq_length):
        X.append(data[i:i+seq_length])
        y.append(data[i+seq_length])

    return np.array(X), np.array(y)


def train_model(ts):
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(ts.values.reshape(-1, 1))

    # Train-test split
    train_size = int(len(scaled_data) * 0.8)
    train_data = scaled_data[:train_size]
    test_data = scaled_data[train_size:]

    seq_length = 3

    X_train, y_train = create_sequences(train_data, seq_length)
    X_test, y_test = create_sequences(test_data, seq_length)

    # Reshape for LSTM
    X_train = X_train.reshape((X_train.shape[0], X_train.shape[1], 1))
    X_test = X_test.reshape((X_test.shape[0], X_test.shape[1], 1))

    # Build model
    model = Sequential()
    model.add(LSTM(50, activation='relu', input_shape=(seq_length, 1)))
    model.add(Dense(1))

    model.compile(optimizer='adam', loss='mse')

    model.fit(X_train, y_train, epochs=50, verbose=0)

    # Predictions
    predictions = model.predict(X_test)

    # Inverse scaling
    predictions = scaler.inverse_transform(predictions)
    y_test_actual = scaler.inverse_transform(y_test.reshape(-1, 1))

    # RMSE
    rmse = np.sqrt(mean_squared_error(y_test_actual, predictions))
    print("LSTM RMSE:", rmse)

    # Save results
    results_df = pd.DataFrame({
        "Date": ts.index[-len(y_test_actual):],
        "Actual": y_test_actual.flatten(),
        "Predicted": predictions.flatten()
    })

    os.makedirs("outputs/predictions", exist_ok=True)
    results_df.to_csv("outputs/predictions/lstm_test_vs_pred.csv", index=False)

    return model, scaler, rmse


def forecast(model, scaler, ts, steps=12):
    data = ts.values.reshape(-1, 1)
    data_scaled = scaler.transform(data)

    seq_length = 3
    input_seq = data_scaled[-seq_length:]

    predictions = []

    for _ in range(steps):
        input_reshaped = input_seq.reshape((1, seq_length, 1))
        pred = model.predict(input_reshaped, verbose=0)

        predictions.append(pred[0][0])

        input_seq = np.append(input_seq[1:], pred, axis=0)

    predictions = scaler.inverse_transform(np.array(predictions).reshape(-1, 1))

    return predictions


def save_output(predictions, ts):
    os.makedirs("outputs/predictions", exist_ok=True)

    last_date = ts.index[-1]
    future_dates = pd.date_range(start=last_date, periods=13, freq='MS')[1:]

    forecast_df = pd.DataFrame({
        "Date": future_dates,
        "Forecast": predictions.flatten()
    })

    forecast_df.to_csv("outputs/predictions/lstm_forecast.csv", index=False)


def run_lstm_model():
    df = load_data()
    ts = prepare_data(df)

    model, scaler, rmse = train_model(ts)

    forecast_values = forecast(model, scaler, ts)

    save_output(forecast_values,ts)

    return rmse


if __name__ == "__main__":
    rmse = run_lstm_model()
    print(f"\nLSTM Model Completed | RMSE: {rmse}")