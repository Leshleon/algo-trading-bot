# data/fetch.py
import yfinance as yf
import pandas as pd

def get_price_data(ticker: str, start: str, end: str) -> pd.DataFrame:
    df = yf.download(ticker, start=start, end=end)
    df = df[['Close']].copy()
    df.columns = ['price']
    df.dropna(inplace=True)
    return df
