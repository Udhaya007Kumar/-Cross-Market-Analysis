import streamlit as st
import pandas as pd
import sqlite3
from queries import queries

# 🔹 DB connect
conn = sqlite3.connect("database.db")

st.set_page_config(layout="wide")

st.title("📊 Cross Market Analysis Dashboard")

# 🔹 Sidebar Navigation
page = st.sidebar.radio("Navigation", [
    "Overview",
    "Market Comparison",
    "SQL Analysis"
])

# =========================
# 📊 OVERVIEW
# =========================
if page == "Overview":
    st.subheader("📊 Market Overview")

    col1, col2, col3 = st.columns(3)

    crypto = pd.read_sql("SELECT AVG(price) as avg FROM crypto_prices", conn)
    oil = pd.read_sql("SELECT AVG(price_usd) as avg FROM oil_prices", conn)
    stock = pd.read_sql("SELECT AVG(close) as avg FROM stock_prices", conn)

    col1.metric("💰 Crypto Avg", round(crypto["avg"][0], 2))
    col2.metric("🛢️ Oil Avg", round(oil["avg"][0], 2))
    col3.metric("📈 Stock Avg", round(stock["avg"][0], 2))

    st.markdown("---")

    st.subheader("Top Cryptos")
    df = pd.read_sql(queries["Top Cryptos"], conn)
    st.dataframe(df)

# =========================
# 📈 MARKET COMPARISON
# =========================
elif page == "Market Comparison":
    st.subheader("📈 BTC vs Oil vs S&P500")

    df = pd.read_sql(queries["Full Market Comparison"], conn)

    df["date"] = pd.to_datetime(df["date"])
    df = df.set_index("date")

    st.line_chart(df)

    st.dataframe(df.tail(50))

# =========================
# 🔎 SQL ANALYSIS
# =========================
elif page == "SQL Analysis":
    st.subheader("🔎 Run SQL Queries")

    selected = st.selectbox("Choose Query", list(queries.keys()))

    if st.button("Run Query"):
        df = pd.read_sql(queries[selected], conn)
        st.dataframe(df)

        # 📊 Chart auto
        if "date" in df.columns:
            df["date"] = pd.to_datetime(df["date"])
            df = df.set_index("date")
            st.line_chart(df.select_dtypes(include=['float', 'int']))