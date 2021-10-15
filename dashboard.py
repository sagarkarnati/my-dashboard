from datetime import timedelta

import streamlit as st
from requests_cache import CachedSession

from stocktwits_dashboard import load_stocktwits_dashboard
from twitter_dashboard import load_twitter_dashboard

cached_session = CachedSession(expire_after=timedelta(days=1))

option = st.sidebar.selectbox("Which Dashboard?", ('twitter', 'stocktwits'), 1)
st.header(option)

if option == 'twitter':
    load_twitter_dashboard()
elif option == 'stocktwits':
    load_stocktwits_dashboard(cached_session)
