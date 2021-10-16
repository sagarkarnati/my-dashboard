import datetime
import streamlit as st
import timeago

from repository.telegram_data_repository import TelegramDataRepository

date = datetime.datetime.utcnow()
telegram_data_repo = TelegramDataRepository()

st.subheader('Feed')
channel_name = st.sidebar.selectbox("Channel", list(telegram_data_repo.get_all_channels()), 0)
st.subheader(channel_name)
telegram_data_list = telegram_data_repo.get_telegram_data(channel_name=channel_name, start_date=None)
for telegram_data in telegram_data_list:
    with st.expander('[ '+timeago.format(telegram_data['MESSAGE_TIME'], date, 'en_short')+' ] '+telegram_data['MESSAGE']):
        if '$' in telegram_data['MESSAGE']:
            words = telegram_data['MESSAGE'].split(' ')
            for word in words:
                if (word.startswith('$') or word.startswith('#')) and word[1:].isalpha():
                    symbol = word[1:]
                    st.subheader(symbol)
                    st.image(f"https://finviz.com/chart.ashx?t={symbol}")
