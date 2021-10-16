import streamlit as st
from st_aggrid import AgGrid
import pandas as pd
from datetime import timedelta
from requests_cache import CachedSession

cached_session = CachedSession(cache_name='http_cache', expire_after=timedelta(hours=1))

stocktwits_option = st.sidebar.selectbox("Which feature ?", ('Trending', 'Feed'), 0)
st.subheader(stocktwits_option)
if stocktwits_option == 'Feed':
    symbol = st.sidebar.text_input("Symbol", value='AAPL', max_chars=5)
    r = cached_session.get(f"https://api.stocktwits.com/api/2/streams/symbol/{symbol}.json")
    data = r.json()
    for message in data['messages']:
        st.write(message['user']['username'])
        st.write(message['created_at'])
        st.write(message['body'])
        if '$' in message['body']:
            words = message['body'].split(' ')
            for word in words:
                if word.startswith('$') and word[1:].isalpha():
                    symbol = word[1:]
                    st.write(symbol)
                    st.image(f"https://finviz.com/chart.ashx?t={symbol}")
        st.markdown("""---""")
elif stocktwits_option == 'Trending':
    data = cached_session.get(f"https://api.stocktwits.com/api/2/trending/symbols.json").json()
    dataframe = pd.json_normalize(data['symbols'])
    dataframe = dataframe[['symbol', 'title', 'watchlist_count']]
    dataframe.sort_values(by='watchlist_count', ascending=False, inplace=True)
    AgGrid(dataframe, fit_columns_on_grid_load=True, sortable=True, filter=True, resizable=False)
