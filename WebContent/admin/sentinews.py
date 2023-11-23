import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from GoogleNews import GoogleNews
from newspaper import Article
from newspaper import Config
import plotly.graph_objs as go
import streamlit as st

nltk.download('vader_lexicon')
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """

st.markdown(hide_streamlit_style, unsafe_allow_html=True)
def main():
    st.title("Google News Sentiment Analysis")
    now = dt.date.today()
    now = now.strftime('%m-%d-%Y')
    yesterday = dt.date.today() - dt.timedelta(days = 1)
    yesterday = yesterday.strftime('%m-%d-%Y')
    nltk.download('punkt')
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0'
    config = Config()
    config.browser_user_agent = user_agent
    config.request_timeout = 10
    company_name = st.text_input("Please provide the name of the Company or a Ticker: ")
    news_df = pd.DataFrame()  # define news_df outside the if statement
    if company_name != '':
        print(f'Searching for and analyzing {company_name}, Please be patient, it might take a while...')

        #Extract News with Google News
        googlenews = GoogleNews(start=yesterday,end=now)
        googlenews.search(company_name)
        result = googlenews.result()
        #store the results
        df = pd.DataFrame(result)
        st.write(df)

        list =[] #creating an empty list 
        for i in df.index:
            dict = {} #creating an empty dictionary to append an article in every single iteration
            article = Article(df['link'][i],config=config) #providing the link
            article.download() #downloading the article 
            article.parse() #parsing the article
            article.nlp() #performing nlp

            #storing results in our empty dictionary
            dict['Date']=df['date'][i] 
            dict['Media']=df['media'][i]
            dict['Title']=article.title
            dict['Article']=article.text
            dict['Summary']=article.summary
            dict['Key_words']=article.keywords
            list.append(dict)

        if not list:
            st.write('Looks like, there is some error in retrieving the data, Please try again or try with a different ticker.')
        else:
            news_df=pd.DataFrame(list) #creating dataframe
            st.write(news_df)
    #Sentiment Analysis
    def percentage(part,whole):
        return 100 * float(part)/float(whole)
    #Assigning Initial Values
    positive = 0
    negative = 0
    neutral = 0
    #Creating empty lists
    news_list = []
    neutral_list = []
    negative_list = []
    positive_list = []

    #Iterating over the tweets in the dataframe
    for news in news_df['Summary']:
        news_list.append(news)
        analyzer = SentimentIntensityAnalyzer().polarity_scores(news)
        neg = analyzer['neg']
        neu = analyzer['neu']
        pos = analyzer['pos']
        comp = analyzer['compound']

        if neg > pos:
            negative_list.append(news) #appending the news that satisfies this condition
            negative += 1 #increasing the count by 1
        elif pos > neg:
            positive_list.append(news) #appending the news that satisfies this condition
            positive += 1 #increasing the count by 1
        elif pos == neg:
            neutral_list.append(news) #appending the news that satisfies this condition
            neutral += 1 #increasing the count by 1 

    positive = percentage(positive, len(news_df)) #percentage is the function defined above
    negative = percentage(negative, len(news_df))
    neutral = percentage(neutral, len(news_df))

    #Converting lists to pandas dataframe
    news_list = pd.DataFrame(news_list)
    neutral_list = pd.DataFrame(neutral_list)
    negative_list = pd.DataFrame(negative_list)
    positive_list = pd.DataFrame(positive_list)
    #using len(length) function for counting
    st.write("Positive Sentiment:", '%.2f' % len(positive_list), end='\n')
    st.write("Neutral Sentiment:", '%.2f' % len(neutral_list), end='\n')
    st.write("Negative Sentiment:", '%.2f' % len(negative_list), end='\n')

        #Creating Piechart
    labels = ['Positive ['+str(round(positive))+'%]' , 'Neutral ['+str(round(neutral))+'%]','Negative ['+str(round(negative))+'%]']
    sizes = [positive, neutral, negative]
    colors = ['yellowgreen', 'blue','red']

    fig = go.Figure(data=[go.Pie(
            labels=labels, 
            values=sizes, 
            hole=0.3,
            sort=False
            )])
    fig.update_layout(
            title="Sentiment Analysis Result for stock= "+company_name,
            height=700,
            width=1000
            )
    st.plotly_chart(fig)


if __name__ == '__main__':
    main()


