import matplotlib.pyplot as plt

def plot_data(df, symbol):
    plt.figure(figsize=(14, 7))
    plt.plot(df['Close'], label='Close Price', alpha=0.5)
    plt.plot(df['SMA_50'], label='50-SMA', alpha=0.9)
    plt.plot(df['SMA_200'], label='200-SMA', alpha=0.9)
    plt.title(f"{symbol} Stock Price and Moving Averages")
    plt.xlabel('Date')
    plt.ylabel('Price ($)')
    plt.legend()
    plt.grid(True)
    plt.show()
