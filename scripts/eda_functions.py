from textblob import TextBlob
import nltk
from nltk.corpus import stopwords
from collections import Counter

nltk.download('punkt')
nltk.download('stopwords')


def headline_length(df, column_name='headline'):
    df['headline_length'] = df[column_name].apply(lambda text: len(text.split()))
    return df['headline_length'].describe().round(2)

def sentiment_analysis(df):
    df['sentiment'] = df['headline'].apply(lambda x: TextBlob(x).sentiment.polarity)
    return df['sentiment'].describe()

def common_keywords(df, num_common):
    # Initialize the stop words
    stop_words = set(stopwords.words('english'))
    
    # Initialize an empty list to hold all keywords
    keywords = []
    
    # Tokenize, clean, and collect keywords from each headline
    for headline in df['headline']:
        from nltk.tokenize import RegexpTokenizer
        tokenizer = RegexpTokenizer(r'\w+')
        words = tokenizer.tokenize(headline.lower())
        words = [word for word in words if word.isalnum() and word not in stop_words]  # Remove stopwords and non-alphanumeric characters
        keywords.extend(words)
    
    # Frequency analysis to identify common keywords
    keyword_freq = Counter(keywords)
    common_keywords = keyword_freq.most_common(num_common)  # Get the top `num_common` most common keywords
    
    return common_keywords

def classify_sentiment(headline):
    analysis = TextBlob(headline)
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity < 0:
        return 'negative'
    else:
        return 'neutral'

