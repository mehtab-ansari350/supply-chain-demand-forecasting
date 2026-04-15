import pandas as pd
import os

def load_data():
    train = pd.read_csv("data/raw/train.csv", low_memory=False)
    store = pd.read_csv("data/raw/store.csv")

    df = train.merge(store, on="Store", how="left")
    return df


def clean_data(df):
    # Convert date to datetime
    df['Date'] = pd.to_datetime(df["Date"])

    # Remove closed stores
    df = df[df['Open'] == 1]

    # =========================
    # Handle Missing Values
    # =========================

    # Competition Distance → fill with median
    df['CompetitionDistance'] = df['CompetitionDistance'].fillna(df['CompetitionDistance'].median())

    # Competition Open Since → fill with 0
    df['CompetitionOpenSinceMonth'] = df['CompetitionOpenSinceMonth'].fillna(0)
    df['CompetitionOpenSinceYear'] = df['CompetitionOpenSinceYear'].fillna(0)

    # Promo2 related → fill with 0 or 'None'
    df['Promo2SinceWeek'] = df['Promo2SinceWeek'].fillna(0)
    df['Promo2SinceYear'] = df['Promo2SinceYear'].fillna(0)
    df['PromoInterval'] = df['PromoInterval'].fillna('None')

    return df


def save_data(df):
    os.makedirs("data/processed", exist_ok=True)
    df.to_csv("data/processed/cleaned_data.csv", index=False)


if __name__ == "__main__":
    df = load_data()
    df = clean_data(df)
    save_data(df)

    print("Cleaning Phase Done ")