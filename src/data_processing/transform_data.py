import pandas as pd
import os

def load_data():
    df = pd.read_csv("data/processed/cleaned_data.csv")
    return df


def transform_data(df):
    # Convert Date
    df['Date'] = pd.to_datetime(df['Date'])

    
    # Time-based Features
   
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    df['Day'] = df['Date'].dt.day
    df['WeekOfYear'] = df['Date'].dt.isocalendar().week.astype(int)

    # Weekend Feature
    df['IsWeekend'] = df['DayOfWeek'].apply(lambda x: 1 if x in [6, 7] else 0)

    return df


def save_data(df):
    os.makedirs("data/processed", exist_ok=True)
    df.to_csv("data/processed/featured_data.csv", index=False)


if __name__ == "__main__":
    df = load_data()
    df = transform_data(df)
    save_data(df)

    print("Feature Engineering Done ")