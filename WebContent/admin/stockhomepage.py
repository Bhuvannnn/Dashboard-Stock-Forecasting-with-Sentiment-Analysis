import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import time
from datetime import datetime

def plot_stock_price(stock_ticker, fig):
    df = yf.Ticker(stock_ticker)
    df = df.history(start=datetime.now().strftime('%Y-%m-%d'), interval='1m', actions=False)

    fig.update_traces(selector=dict(name='Price'), x=df.index, open=df['Open'], high=df['High'], low=df['Low'], close=df['Close'])
    fig.update_traces(selector=dict(name='Volume'), x=df.index, y=df['Volume'])

    fig.update_layout(title=stock_ticker.upper() + ' Stock Price', xaxis_title='Date', yaxis_title='Price/Volume')

    return fig

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """

st.markdown(hide_streamlit_style, unsafe_allow_html=True)
def main():
    st.title("Real-time Stock Price Visualization")
    stock_ticker = st.text_input("Enter the Stock Ticker Symbol (e.g. AAPL)")

    if stock_ticker:
        fig = make_subplots(rows=2, cols=1)
        trace1 = go.Candlestick(name='Price')
        trace2 = go.Bar(name='Volume')
        fig.add_trace(trace1, row=1, col=1)
        fig.add_trace(trace2, row=2, col=1)

        chart = st.plotly_chart(fig, use_container_width=True, key='chart')

        # Refresh the graph every 1 or 2 minutes
        refresh_time = st.selectbox("Refresh Time", options=[0.1, 1, 2, 5])
        while True:
            time.sleep(refresh_time * 60)
            fig = plot_stock_price(stock_ticker, fig)
            chart.plotly_chart(fig, use_container_width=True, key='chart')

if __name__ == "__main__":
    main()
