import sqlite3

def create_connection():
    conn = sqlite3.connect("database.db")
    print("✅ DB Connected")
    return conn

def create_tables(conn):
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cryptocurrencies(
        id TEXT PRIMARY KEY,
        symbol TEXT,
        name TEXT,
        current_price REAL,
        market_cap REAL,
        market_cap_rank INTEGER
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS crypto_prices(
        coin_id TEXT,
        date DATE,
        price REAL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS oil_prices(
        date DATE,
        price_usd REAL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS stock_prices(
        date DATE,
        ticker TEXT,
        open REAL,
        high REAL,
        low REAL,
        close REAL,
        volume INTEGER
    )
    """)

    conn.commit()