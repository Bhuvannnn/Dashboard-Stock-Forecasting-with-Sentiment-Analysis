import pandas as pd
import numpy as np
import os
import yfinance as yf
import matplotlib.pyplot as plt
from scipy.stats import norm
from datetime import datetime, timedelta
import plotly as py
import plotly.io as pio
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

# Define the list of tickers
tickers = ['AAPL', 'AMZN', 'GOOG', 'MSFT', 'META', 'TSLA', 'Adanient.ns', 'NFLX', 'RELIANCE.NS', 'WIPRO.NS', 'TCS.NS', 'INFY.NS', 'NESTLEIND.NS', 'TATAMOTORS.NS', 'ZOMATO.NS']

# Set the default ticker
comp = 'AAPL'

today = datetime.today().strftime('%Y-%m-%d')
six_months_ago = (datetime.today() - timedelta(days=3000)).strftime('%Y-%m-%d')
# df_dict = {ticker: yf.download(ticker, start=six_months_ago, end=today) for ticker in tickers}
df_dict = {ticker: yf.download(ticker, start=six_months_ago, end=today).tz_localize('UTC').tz_convert('Asia/Kolkata') for ticker in tickers}

# Create the dropdown menu
dropdown = [{'label': ticker, 'method': 'update', 'args': [{'y': [df_dict[ticker]['High'], df_dict[ticker]['Close'], df_dict[ticker]['Low'], df_dict[ticker]['Open']]}, {'title': f'{ticker} Price With Year Selection'}]} for ticker in tickers]

# Create the figure
fig = go.Figure(data=[go.Scatter(x=df_dict[comp].index, y=df_dict[comp]['Close'])])
fig.update_layout(title=f'{comp} Price With Year Selection')

# Add the dropdown menu to the figure
fig.update_layout(
    updatemenus=[
        dict(
            buttons=dropdown,
            showactive=True,
            xanchor='left',
            yanchor='top',
            x=0,
            y=1
        )
    ]
)

# Add the subplots to the figure
fig.update_layout(
    xaxis=dict(rangeslider=dict(visible=False)),
    yaxis=dict(title='Price'),
    yaxis2=dict(title='Volume', overlaying='y', side='right')
)

fig.update_xaxes(rangeslider_visible=False, rangeselector=dict(
    buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(count=5, label="5y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)
fig.add_trace(go.Scatter(x=df_dict[comp].index, y=df_dict[comp]['High'], visible=True, name='High'))
fig.add_trace(go.Scatter(x=df_dict[comp].index, y=df_dict[comp]['Low'], visible=True, name='Low'))
fig.add_trace(go.Scatter(x=df_dict[comp].index, y=df_dict[comp]['Open'], visible=True, name='Open'))
fig.add_trace(go.Scatter(x=df_dict[comp].index, y=df_dict[comp]['Close'], visible=True, name='Close'))

fig.show()
fig.write_html('dropstock.html')