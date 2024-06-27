#Top highest average salary job- data professions (Job Title vs Salary)
#Job market saturation of top 5-10 professions with the highest salary *check if it is oversaturated (number of every top 5-10 job titles)
#The correlation of company size and the salary (Company Size vs Salary)
#Average salary by Experience Level and Employment Type (Salary vs Experience Level & Employment Type)
import streamlit as st
import pandas as pd
from streamlit_lottie import st_lottie 
import lottie_animations as l

st.set_page_config(
    page_title = "Descriptive",
    page_icon = "📋",
    layout="wide"
)

# function for retrieving dataset
@st.cache_data
def fetch_data():
    df = pd.read_csv("processed_data.csv")
    st.dataframe(df)

    return df

#create columns for a side-by-side layout of the text and lottie animation
col1, col2 = st.columns([1,1])

#Display text in the first column
with col1:
    st.subheader("**Part 1: Descriptive Models page**")
    st.write("Here, our descriptive models will be displayed, that aim to provide insight on past patterns regarding salary trends in the data science industry, including:")
    st.markdown("* Average Salary by Experience Level and Employment Type")
    st.markdown("* Highest Salary by Profession")
    st.markdown("* Job Market Saturation of Top 5-10 Highest Salary Professions")
    st.markdown("* Correlation between Company Size and Salary")
#Display lottie animation in the second column
with col2:
    st_lottie(l.descriptive_lottie, loop = True, width = 600, height = 350, key = None)
#tabs for different desc models 
tab1, tab2, tab3, tab4 = st.tabs(["Highest Salary Profession", 
                                  "Job Market Saturation",
                                  "Company Size vs Salary",
                                  "Average Salary"])

with tab1:
    st.markdown("#### 📈 *Highest Salary by Profession*")
    st.divider()

with tab2:
    st.markdown("#### 🗺️ *Job Market Saturation of Top 5-10 Highest Salary Professions*")
    st.divider()

with tab3:
    st.markdown("#### 🏢 *Correlation between Company Size and Salary*")
    st.divider()

with tab4:
    st.markdown("#### 🧑 *Average Salary by Experience Level and Employment Type*")
    st.divider()