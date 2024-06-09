#Introduction to data science salary related stuff
#   This sets the context and shows historical trends in data science salaries.
#Work year distribution in this dataset (every work year) 
#   Histogram
#   This helps understand the experience level of professionals in the dataset.


import streamlit as st
import pandas as pd

st.set_page_config(
    page_title = "Homepage",
    page_icon = "🏠",
)

st.title("Dashboard")
st.write("This is a simple Streamlit app.")

x = st.text_input("How are you?")

st.write(f"You replied: {x}.")

is_clicked = st.button("Click Me")

st.write("")
