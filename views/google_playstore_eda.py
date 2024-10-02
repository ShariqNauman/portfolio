import streamlit as st

# Read the HTML file
with open("04_googleplaystore_eda.html", "r") as f:
    html_content = f.read()

# Embed the HTML content
st.components.v1.html(html_content, height=38000)