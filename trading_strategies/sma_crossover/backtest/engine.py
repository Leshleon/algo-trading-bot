# backtest/engine.py
import pandas as pd

def backtest(df: pd.DataFrame, initial_cash: float = 100000) -> pd.DataFrame:
    cash = initial_cash
    position = 0
    equity_curve = []

    for i, row in df.iterrows():
        price = row['price']
        signal = row['signal']

        # Execute trade
        if signal == 1 and cash > 0:
            position = cash / price
            cash = 0
        elif signal == -1 and position > 0:
            cash = position * price
            position = 0

        total_value = cash + position * price
        equity_curve.append(total_value)

    df['equity'] = equity_curve
    return df
