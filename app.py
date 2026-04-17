import streamlit as st
import pandas as pd
import sqlite3

# 🔹 DB CONNECT
conn = sqlite3.connect("database.db", check_same_thread=False)

st.set_page_config(layout="wide")

st.title("🚀 SQL + BI Dashboard")

# =========================
# SIDEBAR
# =========================
page = st.sidebar.selectbox("📂 Navigation", [
    "🏠 Overview",
    "📊 SQL Analysis",
    "🔧 Data Management"
])

# =========================
# 🏠 OVERVIEW
# =========================
if page == "🏠 Overview":

    st.subheader("📊 Market Overview")

    col1, col2, col3 = st.columns(3)

    crypto = pd.read_sql("SELECT AVG(price) FROM crypto_prices", conn)
    oil = pd.read_sql("SELECT AVG(price_usd) FROM oil_prices", conn)
    stock = pd.read_sql("SELECT AVG(close) FROM stock_prices", conn)

    col1.metric("💰 Crypto Avg", round(crypto.iloc[0,0],2))
    col2.metric("🛢️ Oil Avg", round(oil.iloc[0,0],2))
    col3.metric("📈 Stock Avg", round(stock.iloc[0,0],2))

    st.markdown("---")

    df = pd.read_sql("""
        SELECT name, market_cap
        FROM cryptocurrencies
        ORDER BY market_cap DESC
        LIMIT 10
    """, conn)

    st.dataframe(df, use_container_width=True)

# =========================
# 📊 SQL ANALYSIS
# =========================
elif page == "📊 SQL Analysis":

    st.subheader("🧠 SQL Queries")

    query_option = st.selectbox("Choose Query", [
        "BTC vs Oil",
        "BTC vs Stock",
        "Full Market",
        "Oil Yearly",
        "Stock Monthly"
    ])

    if st.button("Run Query"):

        if query_option == "BTC vs Oil":
            query = """
            SELECT c.date, c.price, o.price_usd
            FROM crypto_prices c
            LEFT JOIN oil_prices o ON c.date=o.date
            WHERE c.coin_id='bitcoin'
            """

        elif query_option == "BTC vs Stock":
            query = """
            SELECT c.date, c.price, s.close
            FROM crypto_prices c
            LEFT JOIN stock_prices s ON c.date=s.date
            WHERE c.coin_id='bitcoin'
            """

        elif query_option == "Full Market":
            query = """
            SELECT c.date, c.price, o.price_usd, s.close
            FROM crypto_prices c
            LEFT JOIN oil_prices o ON c.date=o.date
            LEFT JOIN stock_prices s ON c.date=s.date
            WHERE c.coin_id='bitcoin'
            """

        elif query_option == "Oil Yearly":
            query = """
            SELECT strftime('%Y', date) as year,
                   AVG(price_usd) as avg_price
            FROM oil_prices
            GROUP BY year
            """

        elif query_option == "Stock Monthly":
            query = """
            SELECT ticker,
                   strftime('%Y-%m', date) as month,
                   AVG(close) as avg_close
            FROM stock_prices
            GROUP BY ticker, month
            """

        df = pd.read_sql(query, conn)

        if df.empty:
            st.warning("⚠️ No data found")
        else:
            st.success("✅ Query Executed")

            # 🔍 SEARCH
            search = st.text_input("🔍 Search")
            if search:
                df = df[df.astype(str).apply(lambda x: x.str.contains(search).any(), axis=1)]

            # 🔢 PAGINATION
            page_size = 10
            total_pages = (len(df) // page_size) + 1
            page_num = st.number_input("Page", 1, total_pages, 1)

            start = (page_num - 1) * page_size
            end = start + page_size

            st.dataframe(df.iloc[start:end], use_container_width=True)

            # 📄 EXPORT
            st.download_button("⬇ Download CSV", df.to_csv(index=False), "data.csv")

            # 📊 CHART FIX
            if "date" in df.columns:
                df["date"] = pd.to_datetime(df["date"])
                df = df.set_index("date")

                chart_df = df.select_dtypes(include=['float','int'])

                if not chart_df.empty:
                    st.line_chart(chart_df)

            elif "year" in df.columns:
                st.bar_chart(df.set_index("year"))

            elif "month" in df.columns:
                st.bar_chart(df.set_index("month"))

# =========================
# 🔧 DATA MANAGEMENT (CRUD)
# =========================
elif page == "🔧 Data Management":

    st.subheader("🔧 Manage Data")

    action = st.selectbox("Choose Action", [
        "View",
        "Insert",
        "Update",
        "Delete"
    ])

    # 🔹 VIEW
    if action == "View":

        table = st.selectbox("Select Table", [
            "cryptocurrencies",
            "crypto_prices",
            "oil_prices",
            "stock_prices"
        ])

        df = pd.read_sql(f"SELECT * FROM {table}", conn)

        # 🔍 SEARCH
        search = st.text_input("🔍 Search")
        if search:
            df = df[df.astype(str).apply(lambda x: x.str.contains(search).any(), axis=1)]

        # PAGINATION
        page_size = 10
        total_pages = (len(df) // page_size) + 1
        page_num = st.number_input("Page", 1, total_pages, 1)

        start = (page_num - 1) * page_size
        end = start + page_size

        st.dataframe(df.iloc[start:end], use_container_width=True)

        # EXPORT
        st.download_button("⬇ Download CSV", df.to_csv(index=False), "table.csv")

    # 🔹 INSERT
    elif action == "Insert":

        st.subheader("➕ Insert Crypto")

        coin = st.text_input("Coin ID")
        date = st.date_input("Date")
        price = st.number_input("Price")

        if st.button("Insert"):
            conn.execute(
                "INSERT INTO crypto_prices (coin_id, date, price) VALUES (?, ?, ?)",
                (coin, str(date), price)
            )
            conn.commit()
            st.success("Inserted Successfully")

    # 🔹 UPDATE
    elif action == "Update":

        st.subheader("✏️ Update")

        coin = st.text_input("Coin ID")
        date = st.date_input("Date")
        price = st.number_input("New Price")

        if st.button("Update"):
            conn.execute(
                "UPDATE crypto_prices SET price=? WHERE coin_id=? AND date=?",
                (price, coin, str(date))
            )
            conn.commit()
            st.success("Updated Successfully")

    # 🔹 DELETE
    elif action == "Delete":

        st.subheader("🗑️ Delete")

        coin = st.text_input("Coin ID")

        confirm = st.checkbox("Confirm Delete")

        if st.button("Delete"):
            if not confirm:
                st.warning("⚠️ Please confirm delete")
            else:
                conn.execute(
                    "DELETE FROM crypto_prices WHERE coin_id=?",
                    (coin,)
                )
                conn.commit()
                st.success("Deleted Successfully")