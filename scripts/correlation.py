import pandas as pd
from textblob import TextBlob

def filter_stock_data(stock_data, start_date):
    """
    Filter the stock data to match the date range of the news data.
    """
    return stock_data[stock_data['Date'] >= start_date]

def calculate_daily_return(stock_data):
    """
    Calculate daily stock returns as percentage change in closing prices.
    """
    stock_data['daily_return'] = stock_data['Close'].pct_change()
    return stock_data

def get_sentiment(headline):
    """
    Perform sentiment analysis on a single news headline.
    """
    analysis = TextBlob(headline)
    if analysis.sentiment.polarity > 0:
        return 1  # Positive
    elif analysis.sentiment.polarity == 0:
        return 0  # Neutral
    else:
        return -1  # Negative

def analyze_news_sentiment(news_data):
    """
    Apply sentiment analysis to all headlines in the news dataset.
    """
    news_data['sentiment'] = news_data['headline'].apply(get_sentiment)
    return news_data

def calculate_correlation(stock_data, news_data):
    """
    Calculate the correlation between daily stock returns and news sentiment.
    """
    # Group news data by date and calculate average sentiment per day
    daily_sentiment = news_data.groupby('date')['sentiment'].mean().reset_index()

    # Merge stock data with daily sentiment data
    merged_data = pd.merge(stock_data, daily_sentiment, how='inner', left_on='Date', right_on='date')

    # Calculate correlation
    correlation = merged_data['daily_return'].corr(merged_data['sentiment'])
    return correlation

