class Trader:
    def __init__(self, strategy_data):
        self.strategy_data = strategy_data

    def execute_trades(self):
        for index, row in self.strategy_data.iterrows():
            if row['Position'] == 1:
                print(f"BUY signal on {index}. Close price: {row['Close']}")
            elif row['Position'] == -1:
                print(f"SELL signal on {index}. Close price: {row['Close']}")
