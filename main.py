import streamlit as st
from scrape import scrape_website
st.title("AI Based Web Scrapper")
url=st.text_input("Enter your website url: ")

if st.button("Scrape Site"):
    st.write("Scraping the website.")
    result = scrape_website(url)
    print(result)