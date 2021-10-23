import os
import streamlit as st

DB_USER = os.getenv('DB_USER', default=st.secrets['DB_USER'])
DB_PWD = os.getenv('DB_PWD', default=st.secrets['DB_PWD'])
DB_HOST = os.getenv('DB_HOST', default=st.secrets['DB_HOST'])
DB_PORT = os.getenv('DB_PORT', default=st.secrets['DB_PORT'])
DB_DATABASE = os.getenv('DB_DATABASE', default=st.secrets['DB_DATABASE'])

TWITTER_CONSUMER_KEY = os.getenv('TWITTER_CONSUMER_KEY', default=st.secrets['TWITTER_CONSUMER_KEY'])
TWITTER_CONSUMER_SECRET = os.getenv('TWITTER_CONSUMER_SECRET', default=st.secrets['TWITTER_CONSUMER_SECRET'])
TWITTER_ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN', default=st.secrets['TWITTER_ACCESS_TOKEN'])
TWITTER_ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET', default=st.secrets['TWITTER_ACCESS_TOKEN_SECRET'])

TWITTER_USERNAMES = [
    'SRStockAlertBot',
    'traderstewie',
    'the_chart_life',
    'canuck2usa',
    'sunrisetrader',
    'tmltrader',
]
