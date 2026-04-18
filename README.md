# -Cross-Market-Analysis# 🚀 Cross Market Analysis Dashboard

An end-to-end **Data Analytics & Business Intelligence project** that integrates **Cryptocurrency, Oil, and Stock Market data** into a unified dashboard using **Python, SQL, and Streamlit**.

---

## 📊 Project Overview

This project demonstrates how to:

* Collect financial data from multiple sources
* Store and manage data using SQL (SQLite)
* Perform advanced SQL analytics (JOIN, GROUP BY, Aggregations)
* Build an interactive dashboard using Streamlit

The dashboard provides insights across different markets in a **single platform**.

---

## ⚙️ Tech Stack

* **Python**
* **SQLite (SQL)**
* **Streamlit (Dashboard UI)**
* **Pandas (Data Processing)**
* **APIs**

  * CoinGecko (Crypto data)
  * Yahoo Finance (Stock data)

---

## 🧠 Key Features

### 📊 Interactive Dashboard

* KPI Metrics (Crypto, Oil, Stock averages)
* Sidebar navigation
* Clean and responsive UI

### 🧠 SQL Analytics

* SELECT queries
* JOIN operations (multi-table)
* GROUP BY analysis
* Aggregations (AVG, MAX, MIN)

### 🔧 Data Management (CRUD)

* Insert new records
* Update existing data
* Delete records with confirmation
* View and manage all tables

### 🔍 Advanced Functionalities

* Search/filter data
* Pagination (10 rows per page)
* CSV export functionality
* Automatic chart generation

---

## 🗄️ Database Schema

### Tables Used:

* `cryptocurrencies` → coin details
* `crypto_prices` → historical crypto prices
* `oil_prices` → oil price data
* `stock_prices` → stock market data

---

## 🔥 Sample SQL Queries

### 🔹 BTC vs Oil (JOIN)

```sql
SELECT c.date, c.price, o.price_usd
FROM crypto_prices c
LEFT JOIN oil_prices o ON c.date = o.date
WHERE c.coin_id = 'bitcoin';
```

### 🔹 Oil Yearly Trend (GROUP BY)

```sql
SELECT strftime('%Y', date) AS year,
       AVG(price_usd) AS avg_price
FROM oil_prices
GROUP BY year;
```

### 🔹 Stock Monthly Average

```sql
SELECT ticker,
       strftime('%Y-%m', date) AS month,
       AVG(close) AS avg_close
FROM stock_prices
GROUP BY ticker, month;
```

---


```

### 4️⃣ Run Dashboard

```bash
streamlit run app.py
```

---

## 📸 Screenshots

*Add screenshots of your dashboard here (Overview, SQL Analysis, CRUD)*

---

## 💼 Resume Highlight

> Built an end-to-end financial analytics dashboard integrating crypto, oil, and stock data using SQL joins, aggregation, and Streamlit visualization with CRUD operations.

---

## 🎯 Future Improvements

* 📊 Interactive charts using Plotly
* 📉 Correlation analysis
* 📅 Date-based filtering
* ☁️ Deployment (Streamlit Cloud / AWS)

---

## 👨‍💻 Author

**Udhayakumar**

---
