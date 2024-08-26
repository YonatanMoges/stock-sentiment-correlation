from textblob import TextBlob
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from gensim import corpora
from gensim.models import LdaModel


def headline_length(df, column_name='headline'):
    df['headline_length'] = df[column_name].apply(lambda text: len(text.split()))
    return df['headline_length'].describe().round(2)

def sentiment_analysis(df):
    df['sentiment'] = df['headline'].apply(lambda x: TextBlob(x).sentiment.polarity)
    return df['sentiment'].describe()
