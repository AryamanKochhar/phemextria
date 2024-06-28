import talib
import numpy as np
import pandas as pd
import yfinance as yf
from scipy.signal import argrelextrema

# Function to fetch data
def fetch_data(stock_symbol):
    data = yf.download(stock_symbol)
    data = data.drop(labels='Adj Close', axis=1)
    return data

# Function to calculate Donchian Channel
def donchian_indicator(data, n=20):
    hi = data['High']
    lo = data['Low']
    uc = hi.rolling(window=n).max()
    lc = lo.rolling(window=n).min()
    data['donchian_upper'] = uc
    data['donchian_lower'] = lc
    return data

# Function to calculate SMA 200
def sma200(data):
    data['sma200'] = talib.SMA(data['Close'], timeperiod=200)
    return data

# Function to find local maxima and minima
def find_local_extrema(data):
    data['local_max'] = np.nan
    data['local_min'] = np.nan
    
    local_max_indices = argrelextrema(data['donchian_upper'].values, np.greater, order=1)[0]
    local_min_indices = argrelextrema(data['donchian_lower'].values, np.less, order=1)[0]
    
    data.loc[data.index[local_max_indices], 'local_max'] = data['donchian_upper'].iloc[local_max_indices]
    data.loc[data.index[local_min_indices], 'local_min'] = data['donchian_lower'].iloc[local_min_indices]
    
    return data

# Function to generate trading signals
def generate_signal(data):
    data['signal'] = 0

    for i in range(200, len(data) - 1):  # Ensure i+1 is within bounds
        if data['Close'].iloc[i] > data['sma200'].iloc[i]:
            if(data['local_min'].iloc[i]):
                # Look for previous local max
                for j in range(i-1, -1, -1):
                    if not np.isnan(data['local_max'].iloc[j]):
                        if data['donchian_upper'].iloc[i] > data['local_max'].iloc[j]:
                            if i + 1 < len(data):
                                data.loc[data.index[i+1], 'signal'] = 1  # Buy signal on the next candle
                            break
        elif data['Close'].iloc[i] < data['sma200'].iloc[i]:
            if (data['local_max'].iloc[i]):
                # Look for previous local min
                for j in range(i-1, -1, -1):
                    if not np.isnan(data['local_min'].iloc[j]):
                        if data['donchian_lower'].iloc[i] < data['local_min'].iloc[j]:
                            if i + 1 < len(data):
                                data.loc[data.index[i+1], 'signal'] = -1  # Sell signal on the next candle
                            break

    return data

# Main function to execute all steps for a list of stock symbols
def process_stocks(stock_symbols):
    for symbol in stock_symbols:
        data = fetch_data(symbol)
        data = donchian_indicator(data)
        data = sma200(data)
        data = find_local_extrema(data)
        data = generate_signal(data)

        # Save to CSV
        csv_file_path = f'{symbol}_data.csv'
        data.to_csv(csv_file_path)

        # Save to Excel
        excel_file_path = f'{symbol}_data.xlsx'
        data.to_excel(excel_file_path)

        print(f'Processed and saved data for {symbol}')

# List of stock symbols to process
stock_symbols = [
    'MRF.NS'
]

# Process the stocks
process_stocks(stock_symbols)
