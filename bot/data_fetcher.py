import requests
import pandas as pd
from config.config import API_KEY, BASE_URL

class DataFetcher:
    def __init__(self, symbol):
        self.symbol = symbol

    def fetch_data(self):
        url = f"{BASE_URL}function=TIME_SERIES_INTRADAY&symbol={self.symbol}&interval=5min&apikey={API_KEY}&outputsize=full"
        response = requests.get(url)
        data = response.json()

        time_series = data.get("Time Series (5min)", {})
        df = pd.DataFrame.from_dict(time_series, orient='index', dtype='float')
        df = df.rename(columns={
            "1. open": "Open",
            "2. high": "High",
            "3. low": "Low",
            "4. close": "Close",
            "5. volume": "Volume"
        })

        df.index = pd.to_datetime(df.index)
        df = df.sort_index()
        return df
