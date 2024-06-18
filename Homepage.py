#Introduction to data science salary related stuff
#   This sets the context and shows historical trends in data science salaries.
#Work year distribution in this dataset (every work year) 
#   Histogram
#   This helps understand the experience level of professionals in the dataset.
import streamlit as st
from streamlit_lottie import st_lottie
import pandas as pd

st.set_page_config(
    page_title = "Homepage",
    page_icon = "🏠",
)

st.title("Data Science Salary Trends")
st.write("**Welcome to our interactive Data Science Salary Trends 2023 Dashboard!**")
st.write("This dashboard is designed to provide a comprehensive analysis of salary trends in the data science industry from 2021 to 2023. By leveraging this dataset, we aim to deliver valuable insights into how various factors such as work experience, job titles, and company locations impact salary distributions within the industry.")

#Add graph of postgraduate CS students
#Add graph of data science specialist 
#justify why this dashboard/ data visualization is important based on the increasing number of data science based cs students

x = st.text_input("How are you?")

is_clicked = st.button("Click Me")

if is_clicked:
    st.write(f"You replied: {x}")

# st.title("Streamlit Example")


# # something = title 
# st.write("""
# # Explore different classifier 
# Which one is the best?         
# """)

# #st.selectbox() is within the page; st.sidebar.selectbox() is on the sidebar
# dataset_choice = st.sidebar.selectbox("Select Dataset", ("Iris", "Breast Cancer", "Wine"))
# st.write(f"You have chosen {dataset_choice} as the dataset.")

# classifier_name = st.sidebar.selectbox("Select Classifier", ("KNN", "SVM", "Random Forest"))

# #slider (can choose whether on side bar or not)
# max_depth = st.sidebar.slider("max_depth", 2, 15)