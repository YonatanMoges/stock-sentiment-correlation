import pandas as pd
import talib as ta

import matplotlib.pyplot as plt

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
