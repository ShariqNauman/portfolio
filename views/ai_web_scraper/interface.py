import streamlit as st
from .scrape import scrape_website, extract_body_content, clean_body_content, split_dom_content
from .parse import parse_with_ollama
import logging


def show():
    # Set up logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Custom CSS for dark mode
    st.markdown("""
    <style>
        .main {
            background-color: #1E1E1E;
            color: #E0E0E0;
        }
        .stButton>button {
            width: 100%;
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
        }
        .stTextInput>div>div>input {
            background-color: #2D2D2D;
            color: #E0E0E0;
        }
        .stTextArea>div>div>textarea {
            background-color: #2D2D2D;
            color: #E0E0E0;
        }
        .css-1siy2j7 {
            background-color: #2D2D2D;
            color: #E0E0E0;
            border-radius: 5px;
            padding: 1rem;
            margin-top: 1rem;
        }
        h1, h2, h3 {
            color: #4CAF50;
        }
        .stExpander {
            background-color: #2D2D2D;
            border-radius: 5px;
        }
        .streamlit-expanderHeader {
            color: #E0E0E0;
        }
        .stAlert {
            background-color: #2D2D2D;
            color: #E0E0E0;
        }
        .stCodeBlock {
            background-color: #333333;
        }
        .sidebar .sidebar-content {
            background-color: #1E1E1E;
        }
    </style>
    """, unsafe_allow_html=True)

    # Main content
    st.title("🕷️ AI Web Scraper")

    # URL input
    url = st.text_input("Enter a Website URL", placeholder="https://example.com")

    # Scrape button
    if st.button("Scrape Website"):
        if url:
            with st.spinner("🔍 Scraping Website..."):
                result = scrape_website(url)
                
                if result:
                    body_content = extract_body_content(result)
                    cleaned_content = clean_body_content(body_content)

                    st.session_state.dom_content = cleaned_content

                    st.success("✅ Website scraped successfully!")
                    with st.expander("View Raw Content"):
                        st.text_area("DOM Content", cleaned_content, height=200)
                else:
                    st.error("❌ Failed to scrape the website. Please try again.")
        else:
            st.warning("⚠️ Please enter a valid URL.")

    # Parse content if DOM content is available
    if "dom_content" in st.session_state:
        st.markdown("### Extract Information")
        parse_description = st.text_area("Describe what you want to extract from the website", 
                                        placeholder="E.g., 'Extract all product names and their prices'")

        if st.button("Extract Information"):
            if parse_description:
                with st.spinner("🧠 Analyzing content..."):
                    dom_chunks = split_dom_content(st.session_state.dom_content)
                    result = parse_with_ollama(dom_chunks, parse_description)
                    
                    if result.strip():
                        st.success("✅ Information extracted successfully!")
                        st.markdown("### Extracted Information")
                        st.write(result)

                    else:
                        st.info("ℹ️ No relevant information found based on your description.")
            else:
                st.warning("⚠️ Please provide a description of what to extract.")


        
if __name__ == "__main__":
    show()