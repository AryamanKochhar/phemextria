import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

# Fetch historical data for a specific stock
ticker = 'AAPL'  # Example ticker
start_date = '2020-01-01'
end_date = '2023-01-01'

df = yf.download(ticker, start=start_date, end=end_date)

# Calculate the Donchian Channel
n = 20  # period for the Donchian Channel
df['Upper'] = df['Close'].rolling(window=n).max()
df['Lower'] = df['Close'].rolling(window=n).min()
df['Middle'] = (df['Upper'] + df['Lower']) / 2

# Generate signals
df['Buy_Signal'] = np.where(df['Close'] > df['Upper'].shift(1), 1, 0)
df['Sell_Signal'] = np.where(df['Close'] < df['Lower'].shift(1), -1, 0)
df['Position'] = df['Buy_Signal'] + df['Sell_Signal']

# Plotting the results
plt.figure(figsize=(14, 7))
plt.plot(df['Close'], label='Close Price', color='blue')
plt.plot(df['Upper'], label='Upper Band', color='red')
plt.plot(df['Lower'], label='Lower Band', color='green')
plt.plot(df['Middle'], label='Middle Band', color='orange')

# Plot buy and sell signals
plt.plot(df[df['Buy_Signal'] == 1].index, df['Close'][df['Buy_Signal'] == 1], '^', markersize=10, color='g', label='Buy Signal')
plt.plot(df[df['Sell_Signal'] == -1].index, df['Close'][df['Sell_Signal'] == -1], 'v', markersize=10, color='r', label='Sell Signal')

plt.title(f'Donchian Channel Trading Strategy for {ticker}')
plt.legend(loc='best')
plt.show()
