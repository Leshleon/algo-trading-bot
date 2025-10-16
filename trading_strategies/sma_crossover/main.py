# main.py
from data.fetch import get_price_data
from strategy.sma_crossover import generate_signals
from backtest.engine import backtest
from utils.metrics import calculate_returns
import matplotlib.pyplot as plt

if __name__ == "__main__":
    df = get_price_data("AAPL", "2023-01-01", "2024-01-01")
    df = generate_signals(df)
    df = backtest(df)
    
    # Plotting
    df['equity'].plot(title="Equity Curve")
    plt.xlabel("Date")
    plt.ylabel("Portfolio Value")
    plt.grid()
    plt.show()

    # Metrics
    print(f"Total Return: {calculate_returns(df)}%")
