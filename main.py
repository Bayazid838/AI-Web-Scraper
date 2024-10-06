import streamlit as st
from scrape import scrape_site

st.title("Bayazid's AI Web Scraper")
url = st.text_input("Enter a Website URL: ")

if st.button("Scrape Site"):
    st.write("Scraping the website...")
    result = scrape_site(url)
    print(result)