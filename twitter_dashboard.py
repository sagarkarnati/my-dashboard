import datetime

import streamlit as st
import tweepy

import config
import timeago

auth = tweepy.OAuthHandler(config.TWITTER_CONSUMER_KEY, config.TWITTER_CONSUMER_SECRET)
auth.set_access_token(config.TWITTER_ACCESS_TOKEN, config.TWITTER_ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

date = datetime.datetime.utcnow()
username = st.sidebar.selectbox("User", list(config.TWITTER_USERNAMES), 0)
user = api.get_user(screen_name=username)
tweets = api.user_timeline(screen_name=username, count=100, exclude_replies=True, trim_user=True,
                           tweet_mode="extended")

st.subheader(username)
for tweet in tweets:
    created_at = tweet.created_at.replace(tzinfo=datetime.timezone.utc)
    date = date.replace(tzinfo=datetime.timezone.utc)
    timeago_str = timeago.format(created_at, date, 'en_short')
    if '$' in tweet.full_text:
        with st.expander('[ ' + timeago_str + ' ] ' + tweet.full_text):
            words = tweet.full_text.split(' ')
            for word in words:
                if word.startswith('$') and word[1:].isalpha():
                    symbol = word[1:]
                    st.subheader(symbol)
                    st.image(f"https://finviz.com/chart.ashx?t={symbol}")
    elif 'What:' in tweet.full_text:
        st.write('[ ' + timeago_str + ' ] ')
        st.markdown(tweet.full_text.replace("\n", "<br /> "), unsafe_allow_html=True)
st.markdown("""---""")
