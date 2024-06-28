import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import talib as ta

# List of tickers
tickers = ['AAPL'],# 'PAGEIND.NS', 'MRF.NS', 'NRBBEARING.NS', 'RATNAMANI.NS', 
#            'SUNDARMFIN.NS', 'SUPREMEIND.NS', 'THERMAX.NS', 
#            'TRITURBINE.NS', 'TTKPRESTIG.NS', 'ADVENZYMES.NS', 
#            'KKCL.NS'] 

# Date range
start_date = '2010-01-01'
end_date = '2024-01-01'

# Function to generate signals
def generate_signals(df):
    n = 20  # period for the Donchian Channel
    df['Upper'] = df['Close'].rolling(window=n).max()
    df['Lower'] = df['Close'].rolling(window=n).min()
    df['Middle'] = (df['Upper'] + df['Lower']) / 2
    df['RSI'] = ta.RSI(df['Close'], timeperiod=14)
    df['ADX'] = ta.ADX(df['High'], df['Low'], df['Close'], timeperiod=14)
    # df['Signal'] = np.where(
    #     (df['Close'] > df['Upper']) & (df['RSI'].between(30, 50)) & (df['ADX'] > 35), 
    #     1, 
    #     np.where(
    #         (df['Close'] < df['Lower']) & (df['RSI'].between(60, 80)) & (df['ADX'] > 35), 
    #         -1, 
    #         0
    #     )
    # )
    return df

# Download data and apply the strategy for each ticker
for ticker in tickers:
    df = yf.download(ticker, start=start_date, end=end_date)
    df = generate_signals(df)
    
    # Add a column for the ticker symbol
    df['Ticker'] = ticker
    
    # Export each ticker's DataFrame with signals to CSV
    df.to_csv(f'{ticker}_trading_signals.csv', index=False)

    # Plotting the results for each ticker
    plt.figure(figsize=(14, 7))
    plt.plot(df['Close'], label='Close Price', color='blue')
    plt.plot(df['Upper'], label='Upper Band', color='red')
    plt.plot(df['Lower'], label='Lower Band', color='green')
    plt.plot(df['Middle'], label='Middle Band', color='orange')
    
    # Plot buy and sell signals
    plt.plot(df[df['Signal'] == 1].index, df['Close'][df['Signal'] == 1], '^', markersize=10, color='g', label='Buy Signal')
    plt.plot(df[df['Signal'] == -1].index, df['Close'][df['Signal'] == -1], 'v', markersize=10, color='r', label='Sell Signal')
    
    plt.title(f'Complex Donchian Channel Trading Strategy for {ticker}')
    plt.legend(loc='best')
    plt.show()
