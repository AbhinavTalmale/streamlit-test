import streamlit as st
import pandas as pd
import yfinance as yf
st.markdown("<h1 style='text-align: center;'>Stock Price Analyzer</h1>", unsafe_allow_html=True)

st.sidebar.title("Stock Price Analyzer")

ticker_data = yf.Ticker(st.sidebar.text_input("Enter Stock Ticker (e.g., AAPL, MSFT):", "NVDA"))

ticker_df = ticker_data.history(start = st.sidebar.date_input('Enter the Start Date:'),end = st.sidebar.date_input('Enter the End Date:'))

on = st.sidebar.toggle("Press for More Information")

if on:

    st.header(f"Stock Price Data for {ticker_data.ticker}")

    st.dataframe(ticker_df)

    st.subheader('Price movement over time')

    st.line_chart(ticker_df['Close'])

    st.subheader('Volume traded over time') 

    st.bar_chart(ticker_df['Volume'])
    
else:
    st.sidebar.write("Feature deactivated! Please press to view stock data.")

