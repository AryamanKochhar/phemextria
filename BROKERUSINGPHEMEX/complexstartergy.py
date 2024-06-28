import talib
import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Function to fetch data
def fetch_data(stock_symbol):
    data = yf.download(stock_symbol)
    data = data.drop(labels='Adj Close', axis=1)
    return data

# Function to calculate Donchian Channel
def donchian_indicator(data, n=96):
    hi = data['High']
    lo = data['Low']
    uc = hi.rolling(window=n).max()
    lc = lo.rolling(window=n).min()
    mc = (uc + lc) / 2
    data['donchian_upper'] = uc
    data['donchian_lower'] = lc
    data['donchian_middle'] = mc
    return data


# Function to calculate SMA 200
def sma200(data):
    data['sma200'] = talib.SMA(data['Close'], timeperiod=200)
    return data
# Function to generate trading signal
def generate_signal(data):
    data['signal'] = np.where(
        (data['Close'] > data['sma200'])&(data['Close']>data['donchian_upper']),1,
        np.where((data['Close']<data['sma200'])&(data['Close']<data['donchian_lower']),-1)
        ,0
        )
    for i in range(len(data)):
        if(data.loc[i,'Close']>data.loc[i,'sma200'] and data.loc[i,'Close']<data.loc[i,'donchian_upper'] and data.loc[i]
        return data

# Main function to execute all steps for a list of stock symbols
def process_stocks(stock_symbols):
    for symbol in stock_symbols:
        data = fetch_data(symbol)
        data = donchian_indicator(data)
        data = sma200(data)
        data, signal = generate_signal(data)

        # Save to CSV
        csv_file_path = f'{symbol}_data.csv'
        data.to_csv(csv_file_path)

        # Plotting
        plt.figure(figsize=(14, 7))
        plt.plot(data.index, data['Close'], label='Close Price')
        plt.plot(data.index, data['donchian_upper'], label='Donchian Upper')
        plt.plot(data.index, data['donchian_lower'], label='Donchian Lower')
        plt.plot(data.index[data['signal'] == 1], data['Close'][data['signal'] == 1], '^', markersize=8, color='g', lw=0, label='Buy Signal')
        plt.title(f'Donchian Channels and Buy Signals for {symbol}')
        plt.legend()
        plt.grid(True)
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.show()

        print(f'Processed and saved data for {symbol}')

# List of stock symbols to process
stock_symbols = ['PAGEIND.NS']

# Process the stocks
process_stocks(stock_symbols)
