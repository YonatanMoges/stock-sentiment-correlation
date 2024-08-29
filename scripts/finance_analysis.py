import pandas as pd
import talib as ta
import pynance as pn
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

def load_data(file_path):
    df = pd.read_csv(file_path, parse_dates=['date'])
    df.sort_values('date', inplace=True)
    return df

def ta_indicators(df):
    df['SMA_20'] = ta.SMA(df['Close'], timeperiod=20)
    df['SMA_50'] = ta.SMA(df['Close'], timeperiod=50)
    df['RSI'] = ta.RSI(df['Close'], timeperiod=14)
    df['MACD'], df['MACD_signal'], df['MACD_hist'] = ta.MACD(df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
    return df

def financial_metrics(df):
    df = df.rename(columns={'adjclose': 'Close'})
    
    # Calculate returns
    df['returns'] = df['Close'].pct_change()

    # Annualized Return
    cumulative_return = df['Close'].iloc[-1] / df['Close'].iloc[0] - 1
    num_years = len(df) / 252  # Assuming 252 trading days in a year
    annualized_return = (1 + cumulative_return)**(1/num_years) - 1

    # Volatility
    daily_volatility = df['returns'].std()
    annualized_volatility = daily_volatility * np.sqrt(252)
    metrics = {
        'Annualized Return': annualized_return,
        'Volatility': annualized_volatility
    }
    return metrics

def plot_data(df):
    plt.figure(figsize=(14, 7))
    
    # Plot Close price and SMA
    plt.plot(df['Date'], df['Close'], label='Close Price', color='black')
    plt.plot(df['Date'], df['SMA_20'], label='SMA 20', color='blue')
    plt.plot(df['Date'], df['SMA_50'], label='SMA 50', color='red')
    
    plt.title('AAPL Close Price with SMA')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()
    
    # Plot RSI
    plt.figure(figsize=(14, 7))
    plt.plot(df['Date'], df['RSI'], label='RSI', color='purple')
    plt.title('AAPL RSI')
    plt.xlabel('Date')
    plt.ylabel('RSI')
    plt.legend()
    plt.show()
    
    # Plot MACD
    plt.figure(figsize=(14, 7))
    plt.plot(df['Date'], df['MACD'], label='MACD', color='green')
    plt.plot(df['Date'], df['MACD_signal'], label='MACD Signal', color='orange')
    plt.title('AAPL MACD')
    plt.xlabel('Date')
    plt.ylabel('MACD')
    plt.legend()
    plt.show()


