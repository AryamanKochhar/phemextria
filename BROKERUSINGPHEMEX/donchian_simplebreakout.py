import yfinance as yf
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import talib as ta
import xlrd 
#seaborn is just styling pattern ONE CAN CHECK FOR THE STYLING PATTERN
plt.style.use("dark_background")
#THE FORMAT for a date is YYYY/MM/DD
startdate='2013-01-20'
enddate='2024-06-27'
data=yf.download(tickers="PAGE.NS",interval="1d",start=startdate,end=enddate)
# #while using mathplot remember to first plot and then call the use function 
# #now coding a simple donchian breakout  stratergy
data['upper']=data['Close'].rolling(window=96).max().shift(1)
data['lower']=data['Close'].rolling(window=96).min().shift(1)
data['middle']=(data['upper']+data['lower'])/2
data['SMA200']=ta.SMA(data['Close'],timeperiod=200)

# data['signal_BASEDONDC&SMA_buy']=0
# data['signal_BASEDONDC&SMA_sell']=0
# make sure you check the precedence order and put () whereever necessary
data['signal_BASEDONDC&SMA_buy']=np.where((data['Close'] > data['upper']) & (data['Close']> data['SMA200']),1,0)
data['signal_BASEDONDC&SMA_sell']=np.where((data['Close'] < data['lower'])& (data['Close']<data['SMA200']),-1,0)
data['Final']=data['signal_BASEDONDC&SMA_sell']+data['signal_BASEDONDC&SMA_buy'] 
plt.figure(figsize=(12,8))
plt.plot(data['Close'], label='Close Price', color='blue')
plt.plot(data['upper'], label='Upper Band', color='red')
plt.plot(data['lower'], label='Lower Band', color='green')
plt.plot(data['middle'], label='Middle Band', color='orange')
plt.plot(data['SMA200'], label='simple moving average',color='yellow')
buy_signals=data[data['signal_BASEDONDC&SMA_buy']==1]
sell_signals=data[data['signal_BASEDONDC&SMA_sell']==-1]
plt.plot(buy_signals['Close'],'^',markersize=10,color='g',label='Buy signal')
plt.plot(sell_signals['Close'],'v',markersize=10,color='r',label='Sell signal')
plt.legend()
plt.title('MSFT Donchian Channel and SMA200')
# data.loc["2023":"2023-08"].plot(data['upper'],data['Close'],data['upper'],data['middle'],data['SMA200'],figsize=(12,8))
plt.show()
# weights=np.random.random(len(data))
# weights/=np.sum(weights)
# print(weights)
# print(data)
data.to_csv('signals.csv')
#fama french factors and calculatr rolling factor betas
from sklearn.cluster import KMeans

# data = data.drop('cluster', axis=1)

# def get_clusters(df):
#     df['cluster'] = KMeans(n_clusters=4,
#                            random_state=0,
#                            init=initial_centroids).fit(df).labels_
#     return df

# data = data.dropna().groupby('date', group_keys=False).apply(get_clusters)

# data
#using monte carlo
#selecting stocks from the internet
#optimizing  the stratergy
#TRAINING fama fremch
#