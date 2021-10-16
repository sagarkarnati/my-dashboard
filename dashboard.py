import os
import streamlit as st

root = os.path.join(os.path.dirname(__file__))
dashboards = {
    "Twitter": os.path.join(root, "twitter_dashboard.py"),
    "Stocktwits": os.path.join(root, "stocktwits_dashboard.py"),
    "Telegram": os.path.join(root, "telegram_dashboard.py")
}

choice = st.sidebar.selectbox("Which Dashboard?", list(dashboards.keys()), 2)

path = dashboards[choice]
with open(path, encoding="utf-8") as code:
    exec(code.read(), globals())