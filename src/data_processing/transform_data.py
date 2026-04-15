import pandas as pd
import os

def load_data():
    df = pd.read_csv("data/processed/cleaned_data.csv")
    return df


def transform_data(df):
    # Convert Date
    df['Date'] = pd.to_datetime(df['Date'])

    # =========================
    # Time-based Features
    # =========================
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    df['Day'] = df['Date'].dt.day
    df['WeekOfYear'] = df['Date'].dt.isocalendar().week.astype(int)

    # Weekend Feature
    df['IsWeekend'] = df['DayOfWeek'].apply(lambda x: 1 if x in [6, 7] else 0)

    # =========================
    # SQL-READY DATA
    # =========================
    df_sql = df[[
        'Store',
        'Date',
        'Sales',
        'Customers',
        'Promo',
        'StateHoliday',
        'SchoolHoliday',
        'StoreType',
        'Assortment',
        'CompetitionDistance',
        'Promo2',
        'Year',
        'Month',
        'WeekOfYear',
        'IsWeekend'
    ]].copy()

    # =========================
    #  CRITICAL FIXES FOR POSTGRES
    # =========================

    # 1. Convert Date to string (safe import)
    df_sql['Date'] = df_sql['Date'].astype(str)

    # 2. Ensure numeric columns are valid
    numeric_cols = [
        'Store', 'Sales', 'Customers', 'Promo',
        'CompetitionDistance', 'Promo2',
        'Year', 'Month', 'WeekOfYear', 'IsWeekend'
    ]

    for col in numeric_cols:
        df_sql[col] = pd.to_numeric(df_sql[col], errors='coerce')

    # 3. Fill NULL values
    df_sql = df_sql.fillna(0)

    # 4. Convert categorical safely to string
    df_sql['StateHoliday'] = df_sql['StateHoliday'].astype(str)
    df_sql['StoreType'] = df_sql['StoreType'].astype(str)
    df_sql['Assortment'] = df_sql['Assortment'].astype(str)

    return df, df_sql


def save_data(df, df_sql):
    os.makedirs("data/processed", exist_ok=True)

    # Full dataset (for ML)
    df.to_csv("data/processed/featured_data.csv", index=False)

    # SQL-ready dataset
    df_sql.to_csv("data/processed/sql_ready_data.csv", index=False)


if __name__ == "__main__":
    df = load_data()
    df, df_sql = transform_data(df)
    save_data(df, df_sql)

    print("Feature Engineering + SQL Data Ready Done ")