import yfinance as yf
import pandas as pd

# Banking & financial sector tickers
TICKERS = [
    "JPM", "BAC", "WFC", "C", "GS",   # US Banks
    "HDFCBANK.NS", "ICICIBANK.NS",      # Indian Banks
    "V", "MA", "PYPL"                   # Payments
]

def fetch_stock_data():
    all_data = []
    for ticker in TICKERS:
        try:
            stock = yf.Ticker(ticker)
            hist = stock.history(period="3mo")
            hist["ticker"] = ticker
            hist.reset_index(inplace=True)
            all_data.append(hist)
            print(f"✅ Fetched {ticker}")
        except Exception as e:
            print(f"❌ Failed {ticker}: {e}")
    
    df = pd.concat(all_data, ignore_index=True)
    df.columns = [c.lower().replace(" ", "_") for c in df.columns]
    return df

if __name__ == "__main__":
    df = fetch_stock_data()
    print(df.head())