# strategy/sma_crossover.py
import pandas as pd

def generate_signals(df: pd.DataFrame, short_window=20, long_window=50) -> pd.DataFrame:
    df = df.copy()
    df['sma_short'] = df['price'].rolling(window=short_window).mean()
    df['sma_long'] = df['price'].rolling(window=long_window).mean()
    
    df['signal'] = 0
    df.loc[df['sma_short'] > df['sma_long'], 'signal'] = 1  # Buy
    df.loc[df['sma_short'] < df['sma_long'], 'signal'] = -1 # Sell
    df['signal'] = df['signal'].shift(1)  # Avoid lookahead bias
    
    return df
