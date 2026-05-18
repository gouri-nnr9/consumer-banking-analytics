import pandas as pd
from sqlalchemy import create_engine

DB_PATH = "data/banking.db"
engine = create_engine(f"sqlite:///{DB_PATH}")

def get_latest_prices():
    query = """
        SELECT ticker, date, close, volume
        FROM stock_prices
        WHERE date = (SELECT MAX(date) FROM stock_prices)
        ORDER BY close DESC
    """
    return pd.read_sql(query, engine)

def get_price_trends(ticker):
    query = f"""
        SELECT date, close, volume
        FROM stock_prices
        WHERE ticker = '{ticker}'
        ORDER BY date ASC
    """
    return pd.read_sql(query, engine)

def get_top_gainers():
    query = """
        SELECT ticker,
               MIN(close) as start_price,
               MAX(close) as peak_price,
               ROUND(((MAX(close) - MIN(close)) / MIN(close)) * 100, 2) as pct_gain
        FROM stock_prices
        GROUP BY ticker
        ORDER BY pct_gain DESC
        LIMIT 5
    """
    return pd.read_sql(query, engine)

def get_volatility():
    query = """
        SELECT ticker,
               ROUND(AVG(high - low), 2) as avg_daily_range,
               ROUND(AVG(volume), 0) as avg_volume
        FROM stock_prices
        GROUP BY ticker
        ORDER BY avg_daily_range DESC
    """
    return pd.read_sql(query, engine)

def get_moving_average(ticker):
    df = get_price_trends(ticker)
    df["MA_7"] = df["close"].rolling(7).mean()
    df["MA_21"] = df["close"].rolling(21).mean()
    return df