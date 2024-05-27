import streamlit as st
import pandas as pd

st.title("Dashboard")
st.write("This is a simple Streamlit app.")

x = st.text_input("How are you?")

st.write(f"You replied: {x}.")

is_clicked = st.button("Click Me")

st.write("")
