import pandas as pd

class Strategy:
    def __init__(self, data):
        self.data = data

    def moving_average_crossover(self):
        self.data['SMA_50'] = self.data['Close'].rolling(window=50).mean()
        self.data['SMA_200'] = self.data['Close'].rolling(window=200).mean()

        self.data['Signal'] = 0
        self.data['Signal'][self.data['SMA_50'] > self.data['SMA_200']] = 1
        self.data['Position'] = self.data['Signal'].diff()

        return self.data
