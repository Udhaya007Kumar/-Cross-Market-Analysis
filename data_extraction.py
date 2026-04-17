import requests
import pandas as pd
import yfinance as yf

# 🔹 Crypto list
def get_crypto_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {"vs_currency": "usd", "per_page": 10, "page": 1}
    data = requests.get(url, params=params).json()
    return pd.DataFrame(data)

# 🔹 Crypto history
#
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
    params = {"vs_currency": "usd", "days": 365}
    data = requests.get(url, params=params).json()

    prices = data["prices"]
    df = pd.DataFrame(prices, columns=["timestamp", "price"])
    df["date"] = pd.to_datetime(df["timestamp"], unit="ms")
    df["coin_id"] = coin_id

    return df[["coin_id", "date", "price"]]

def get_crypto_history(coin_id):
    import requests
    import pandas as pd
    import time

    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
    params = {"vs_currency": "usd", "days": 365}

    response = requests.get(url, params=params)

    # ❌ API failனா
    if response.status_code != 200:
        print(f"❌ API failed for {coin_id}")
        return pd.DataFrame()

    data = response.json()

    # ❌ prices இல்லனா
    if "prices" not in data:
        print(f"⚠️ No price data for {coin_id}")
        return pd.DataFrame()

    prices = data["prices"]

    df = pd.DataFrame(prices, columns=["timestamp", "price"])
    df["date"] = pd.to_datetime(df["timestamp"], unit="ms")
    df["coin_id"] = coin_id

    time.sleep(2)  # 🔥 important

    return df[["coin_id", "date", "price"]]
    

# 🔹 Stock data
def get_stock_data():
    tickers = ["^GSPC", "^IXIC", "^NSEI"]
    df = yf.download(tickers, start="2020-01-01", end="2025-01-01")
    return df