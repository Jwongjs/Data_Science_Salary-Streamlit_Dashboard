##TO-DO LIST
#Add graph of postgraduate CS students
#Add graph of data science specialist 
#justify why this dashboard/ data visualization is important based on the increasing number of data science based cs students

##STREAMLIT ELEMENTS
# x = st.text_input("How are you?")

# is_clicked = st.button("Click Me")

# if is_clicked:
#     st.write(f"You replied: {x}")

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
import streamlit as st
import pandas as pd
import lottie_animations as l
from streamlit_lottie import st_lottie
import plotly.express as px

df = pd.read_csv("processed_data.csv")

st.set_page_config(
    page_title = "Homepage",
    page_icon = "🏠",
    layout="wide"
)

st.title("💵 Data Science Salary Trends 💵")

#create columns for a side-by-side layout of the text and lottie animation
col1, col2 = st.columns([2,1])

#Display text in the first column
with col1:
    st.write("**Welcome to our interactive Data Science Salary Trends 2023 Dashboard!**")
    st.write("This dashboard is designed to provide a comprehensive analysis of salary trends in the data science industry.")
    st.write("By leveraging the dataset below, we are able to deliver valuable insights into how various factors impact salary distributions within the industry.")

#Display lottie animation in the second column
with col2:
    st_lottie(l.welcome_lottie, loop = True, width = 250, height = 180, key = None)
    
st.subheader("Dataset")
st.dataframe(df) #to display the interactive table
st.write(f"This dataset consist of {df.shape[0]} rows.")