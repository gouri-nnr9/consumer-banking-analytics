from sqlalchemy import create_engine
import pandas as pd
from pipeline.fetch_data import fetch_stock_data

DB_PATH = "data/banking.db"
engine = create_engine(f"sqlite:///{DB_PATH}")

def store_data():
    df = fetch_stock_data()
    df.to_sql("stock_prices", engine, if_exists="replace", index=False)
    print(f"✅ Stored {len(df)} rows to database")

def load_data():
    return pd.read_sql("SELECT * FROM stock_prices", engine)

if __name__ == "__main__":
    store_data()