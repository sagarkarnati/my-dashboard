import streamlit as st
import tweepy
import config
import requests
import pandas as pd


def load_stocktwits_dashboard(cached_session):
    stocktwits_option = st.sidebar.selectbox("Which feature ?", ('trending', 'stock feed'), 0)
    if stocktwits_option == 'stock feed':
        symbol = st.sidebar.text_input("Symbol", value='AAPL', max_chars=5)
        r = cached_session.get(f"https://api.stocktwits.com/api/2/streams/symbol/{symbol}.json")
        data = r.json()
        for message in data['messages']:
            st.image(message['user']['avatar_url'])
            st.write(message['user']['username'])
            st.write(message['created_at'])
            st.write(message['body'])
            if '$' in message['body']:
                words = message['body'].split(' ')
                for word in words:
                    if word.startswith('$') and word[1:].isalpha():
                        symbol = word[1:]
                        st.write(symbol)
                        st.image(f"https://finviz.com/quote.ashx?t={symbol}")
    elif stocktwits_option == 'trending':
        data = cached_session.get(f"https://api.stocktwits.com/api/2/trending/symbols.json").json()
        dataframe = pd.json_normalize(data['symbols'])
        dataframe.sort_values(by='watchlist_count', ascending=False, inplace=True)
        st.dataframe(dataframe)
