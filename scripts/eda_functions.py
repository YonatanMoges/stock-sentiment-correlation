from textblob import TextBlob

# scripts/descriptive_stats.py

""" def headline_length(df):
    df['headline_length'] = df['headline'].apply(len)
    return df['headline_length'].describe()
 """
def count_words(column):
    return len(column.split())

# scripts/descriptive_stats.py

def headline_length(df, column_name='headline'):
    df['headline_length'] = df[column_name].apply(lambda text: len(text.split()))
    return df['headline_length'].describe().round(2)


def sentiment_analysis(df):
    df['sentiment'] = df['headline'].apply(lambda x: TextBlob(x).sentiment.polarity)
    return df['sentiment'].describe()
