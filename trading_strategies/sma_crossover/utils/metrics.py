# utils/metrics.py
import pandas as pd

def calculate_returns(df: pd.DataFrame) -> float:
    return_pct = (df['equity'].iloc[-1] / df['equity'].iloc[0]) - 1
    return round(return_pct * 100, 2)
