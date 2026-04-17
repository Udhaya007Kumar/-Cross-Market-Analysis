import pandas as pd

def clean_crypto(df):
    return df[[
        "id", "symbol", "name",
        "current_price", "market_cap", "market_cap_rank"
    ]]

def clean_crypto_prices(df):
    df["date"] = pd.to_datetime(df["date"]).dt.date
    return df

def clean_oil(df):
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.rename(columns={
        "Date": "date",
        "Price": "price_usd"
    })
    return df

def clean_stock(df):
    df = df.stack(level=1).reset_index()
    df.columns = ["date", "ticker", "open", "high", "low", "close", "volume"]
    return df