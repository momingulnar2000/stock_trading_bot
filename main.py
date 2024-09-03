from bot.data_fetcher import DataFetcher
from bot.strategy import Strategy
from bot.trader import Trader
from bot.utils import plot_data

def main():
    symbol = "MSFT"  

    # Fetch data
    data_fetcher = DataFetcher(symbol)
    data = data_fetcher.fetch_data()

    # Apply strategy
    strategy = Strategy(data)
    strategy_data = strategy.moving_average_crossover()

    # Execute trades
    trader = Trader(strategy_data)
    trader.execute_trades()

    # Plot results
    plot_data(strategy_data, symbol)

if __name__ == "__main__":
    main()
