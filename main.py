import streamlit as st
from views.ai_web_scraper import show as show_ai_web_scraper

st.set_page_config(page_title="Shariq Nauman's Portfolio", page_icon="🚀", layout="wide")

# Define pages
about_me_page = st.Page(page="views/about_me.py", title="About Me", icon="👤", default=True)
ai_web_scraper_page = st.Page(page=show_ai_web_scraper, title="AI Web Scraper", icon="🕷️")
google_playstore_eda = st.Page(page="views/google_playstore_eda.py", title="Google Playstore EDA", icon="📊")

# Set up navigation
pg = st.navigation({
    "Info": [about_me_page],
    "Projects": [ai_web_scraper_page, google_playstore_eda]
})

st.sidebar.text("Made with 💗 by Shariq Nauman")

pg.run()