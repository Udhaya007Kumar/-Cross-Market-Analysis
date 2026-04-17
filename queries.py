    queries = {

    # =========================
    # 🟢 BASIC SELECT (DQL)
    # =========================
    "All Cryptos": "SELECT * FROM cryptocurrencies LIMIT 50;",
    "All Crypto Prices": "SELECT * FROM crypto_prices LIMIT 100;",
    "All Oil": "SELECT * FROM oil_prices LIMIT 100;",
    "All Stocks": "SELECT * FROM stock_prices LIMIT 100;",

    # =========================
    # 🟢 AGGREGATION
    # =========================
    "Avg Crypto Price": "SELECT AVG(price) FROM crypto_prices;",
    "Max BTC Price": "SELECT MAX(price) FROM crypto_prices WHERE coin_id='bitcoin';",
    "Min Oil Price": "SELECT MIN(price_usd) FROM oil_prices;",
    "Stock Avg by Ticker": "SELECT ticker, AVG(close) FROM stock_prices GROUP BY ticker;",

    # =========================
    # 🟢 GROUP BY
    # =========================
    "Oil Yearly": """
    SELECT strftime('%Y', date) AS year,
    AVG(price_usd) FROM oil_prices GROUP BY year;
    """,

    "Stock Monthly": """
    SELECT ticker,
    strftime('%Y-%m', date) AS month,
    AVG(close)
    FROM stock_prices
    GROUP BY ticker, month;
    """,

    # =========================
    # 🔥 JOIN QUERIES
    # =========================
    "BTC vs Oil": """
    SELECT c.date, c.price, o.price_usd
    FROM crypto_prices c
    LEFT JOIN oil_prices o ON c.date=o.date
    WHERE c.coin_id='bitcoin';
    """,

    "BTC vs Stock": """
    SELECT c.date, c.price, s.close
    FROM crypto_prices c
    LEFT JOIN stock_prices s ON c.date=s.date
    WHERE c.coin_id='bitcoin';
    """,

    "Full Market": """
    SELECT c.date, c.price, o.price_usd, s.close
    FROM crypto_prices c
    LEFT JOIN oil_prices o ON c.date=o.date
    LEFT JOIN stock_prices s ON c.date=s.date
    WHERE c.coin_id='bitcoin';
    """,

    # =========================
    # 🟡 INSERT (DML)
    # =========================
    "Insert Sample Crypto": """
    INSERT INTO cryptocurrencies (id,name) VALUES ('test','TestCoin');
    """,

    # =========================
    # 🟡 UPDATE
    # =========================
    "Update Crypto Name": """
    UPDATE cryptocurrencies SET name='UpdatedCoin' WHERE id='test';
    """,

    # =========================
    # 🔴 DELETE
    # =========================
    "Delete Crypto": """
    DELETE FROM cryptocurrencies WHERE id='test';
    """,

    # =========================
    # 🧠 ADVANCED
    # =========================
    "BTC Moving Avg": """
    SELECT date,
    price,
    AVG(price) OVER (ORDER BY date ROWS 5 PRECEDING)
    FROM crypto_prices
    WHERE coin_id='bitcoin';
    """,

    }
