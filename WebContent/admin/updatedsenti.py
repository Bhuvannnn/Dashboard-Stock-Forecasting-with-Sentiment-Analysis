from textblob import TextBlob
import sys
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

#from wordcloud import WordCloud, STOPWORDS
from PIL import Image
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from langdetect import detect
from nltk.stem import SnowballStemmer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import CountVectorizer

new_words = {
    'bullish'  : 2.5,	  
'bearish'  : -2.5,  
'rally' : 2.4,  
'slump':  -2.3,  
'volatility' : -1.5,  
'optimism':  2.7,  
'pessimism':  -2.5,
'correction':  -1.7,  
'growth':  2.5,  
'decline':  -2.3,  
'recession':  -2.7, 
'recovery':  2.4,  
'uncertainty':  -1.9,  
'stability':  1.4,  
'momentum':  1.6,  
'resistance':  -1.2, 
'support':  1.2,  
'sell-off':   2.1 
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

#Sentiment Analysis
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

def percentage(part,whole):
    return 100 * float(part)/float(whole) 

# handles = ["business", "cnnbrk", "CNN", "BBC Breaking News", "TheEconomist", "washingtonpost", "ABC"]

keyword = input("Please enter keyword or hashtag to search: ")
noOfTweet = int(input ("Please enter how many tweets to analyze: "))

# for handle in handles:
#     tweets = tweepy.Cursor(api.search_tweets, q=f"from:{handle} {keyword}").items(noOfTweet)

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
    cleaned_tweet = clean_tweet(tweet.text)
    tweet_list.append(cleaned_tweet)
    analysis = TextBlob(cleaned_tweet)
    score = Analyzer.polarity_scores(cleaned_tweet)
    neg = score['neg']
    neu = score['neu']
    pos = score['pos']
    comp = score['compound']
    polarity += analysis.sentiment.polarity
    
    if neg > pos:
        negative_list.append(cleaned_tweet)
        negative += 1

    elif pos > neg:
        positive_list.append(cleaned_tweet)
        positive += 1
    
    elif pos == neg:
        neutral_list.append(cleaned_tweet)
        neutral += 1

positive = percentage(positive, len(tweet_list))
negative = percentage(negative, len(tweet_list))
neutral = percentage(neutral, len(tweet_list))
polarity = percentage(polarity, len(tweet_list))
positive = format(positive, '.1f')
negative = format(negative, '.1f')
neutral = format(neutral, '.1f')

#Number of Tweets (Total, Positive, Negative, Neutral)
tweet_list = pd.DataFrame(tweet_list)
neutral_list = pd.DataFrame(neutral_list)
negative_list = pd.DataFrame(negative_list)
positive_list = pd.DataFrame(positive_list)

print("total number: ",len(tweet_list))
print("positive number: ",len(positive_list))
print("negative number: ", len(negative_list))
print("neutral number: ",len(neutral_list))

print(tweet_list)

labels = ['Positive ['+str(positive)+'%]' , 'Neutral ['+str(neutral)+'%]','Negative ['+str(negative)+'%]']
values = [positive, neutral, negative]
colors = ['yellowgreen', 'blue','red']

fig = go.Figure(data=[go.Pie(labels=labels, values=values)])

fig.update_traces(marker=dict(colors=colors), hole=.5)

fig.update_layout(
    title="Sentiment Analysis Result for keyword =  "+keyword+"",
    legend=dict(
        title=None,
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    )
)

fig.show()
fig.write_html('D:/Intern/updated_dashboard/stockprediction/WebContent/admin/Sentiment Analysis of {} .html'.format(keyword))
# create CSV files for tweet lists
tweet_list.to_html("D:/Intern/updated_dashboard/stockprediction/WebContent/admin/tweet.html", index=False)
tweet_list.to_csv("tweets.csv", index=False)
tweet_df = pd.read_csv('tweets.csv')
# tweet_html = tweet_df.to_html('tweet.html')