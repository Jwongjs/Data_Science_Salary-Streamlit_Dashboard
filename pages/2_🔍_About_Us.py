import pandas as pd
import streamlit as st
from streamlit_lottie import st_lottie 
import lottie_animations as l

df = pd.read_csv("processed_data.csv")

st.set_page_config(
    page_title = "About Us",
    page_icon = "🔍",
    layout="wide"
)

#create columns for a side-by-side layout of the text and lottie animation
col1, col2 = st.columns([1,1])

#Display text in the first column
with col1:
    st.subheader("**Welcome to our interactive Data Science Salary Trends 2023 Dashboard!**")
    st.write("This dashboard is designed to provide a comprehensive analysis of salary trends in the data science industry.")
    st.write("By leveraging the dataset below, we are able to deliver valuable insights into how various factors such as work experience, job titles and company locations impact salary distributions within the industry.")

#Display lottie animation in the second column
with col2:
    st_lottie(l.welcome_lottie, loop = True, width = 600, height = 350, key = None)
    
st.subheader("Preprocessed Data Science Salary Trends Dataset")
st.dataframe(df) #to display the interactive table
st.write(f"This dataset consist of <span style='color: green;'>{df.shape[0]}</span> rows.", unsafe_allow_html=True)