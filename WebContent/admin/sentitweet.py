import streamlit as st
from textblob import TextBlob
import tweepy
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import nltk
import pycountry
import re
import string
import plotly.graph_objects as go
import nltk
# nltk.download('vader_lexicon')

from PIL import Image
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from langdetect import detect
from nltk.stem import SnowballStemmer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import CountVectorizer


new_words = {
    'bullish': 2.5,
    'bearish': -2.5,
    'rally': 2.4,
    'slump': -2.3,
    'volatility': -1.5,
    'optimism': 2.7,
    'pessimism': -2.5,
    'correction': -1.7,
    'growth': 2.5,
    'decline': -2.3,
    'recession': -2.7,
    'recovery': 2.4,
    'uncertainty': -1.9,
    'stability': 1.4,
    'momentum': 1.6,
    'resistance': -1.2,
    'support': 1.2,
    'sell-off': 2.1
}

Analyzer = SentimentIntensityAnalyzer()
Analyzer.lexicon.update(new_words)

# Authentication for live twitter data
consumerKey = "6nb67J33fyqm7G59L6nkN2CYw"
consumerSecret = "hK0mjjRWjWhKdPyDQgtdw4khCtPcpQd3usEEGIMykEJyIf5nj8"
accessToken = "851076892551774209-IwbaI4Hm1bqy6UeMX2RJ09Bbh4ZxPBh"
accessTokenSecret = "8PGEoWxtCNvBoyRYgaGSQFLCaij8qofeM69yePBOl6Erz"

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

# Sentiment Analysis
def clean_tweet(tweet):
    """
    Utility function to clean tweet text by removing links, special characters
    using simple regex statements.
    """
    # remove URLs
    tweet = re.sub(r"http\S+", "", tweet)

    # remove mentions
    tweet = re.sub(r"@\w+", "", tweet)

    # remove hashtags
    tweet = re.sub(r"#\w+", "", tweet)

    tweet = re.sub(r"RT ", "", tweet)

    # # remove punctuation
    # tweet = re.sub(r"[^\w\s]", "", tweet)

    return tweet

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """

st.markdown(hide_streamlit_style, unsafe_allow_html=True)
def percentage(part, whole):
    return 100 * float(part) / float(whole)

def main():
    st.title("Twitter Sentiment Analysis")

    keyword = st.text_input("Please enter keyword or hashtag to search")
    noOfTweet = st.number_input("Please enter how many tweets to analyze", step=1)

    if st.button("Analyze"):
        tweets = tweepy.Cursor(api.search_tweets, q=keyword).items(noOfTweet)
        positive = 0
        negative = 0
        neutral = 0
        polarity = 0
        tweet_list = []
        neutral_list = []
        negative_list = []
        positive_list = []

        for tweet in tweets:
            tweet_clean = clean_tweet(tweet.text)
            tweet_list.append(tweet_clean)
            analysis = TextBlob(tweet_clean)
            score = SentimentIntensityAnalyzer().polarity_scores(tweet_clean)
            neg = score["neg"]
            neu = score["neu"]
            pos = score["pos"]
            comp = score["compound"]
            polarity += analysis.sentiment.polarity
            
            if neg > pos:
                negative_list.append(tweet_clean)
                negative += 1

            elif pos > neg :
                positive_list.append(tweet_clean)
                positive += 1

            else:
                neutral_list.append(tweet_clean)
                neutral += 1

        positive = percentage(positive, len(tweet_list))
        neutral = percentage(neutral, len(tweet_list))
        negative = percentage(negative, len(tweet_list))
        polarity = percentage(polarity, len(tweet_list))

        st.write("Analysis Results:")
        st.write("Total Tweets:", len(tweet_list))
        st.write("Positive Tweets:", positive, "({}%)".format(positive))
        st.write("Neutral Tweets:", neutral, "({}%)".format(neutral))
        st.write("Negative Tweets:", negative, "({}%)".format(negative))
        st.write("Overall Polarity Score:", polarity)

        # Plotting the sentiment analysis results
        sentiment_labels = ['Positive', 'Neutral', 'Negative']
        sentiment_values = [positive, neutral, negative]

        fig = go.Figure([go.Bar(x=sentiment_labels, y=sentiment_values)])
        fig.update_layout(title_text='Sentiment Analysis of Tweets',
                          xaxis_title='Sentiment',
                          yaxis_title='Percentage')
        
        st.plotly_chart(fig)

        st.write("Positive Tweets:")
        for tweet in positive_list:
            st.text("- " + tweet)

        st.write("Neutral Tweets:")
        for tweet in neutral_list:
            st.text("- " + tweet)

        st.write("Negative Tweets:")
        for tweet in negative_list:
            st.text("- " + tweet)

        
if __name__ == '__main__':
    main()