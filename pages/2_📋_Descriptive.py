#Top highest average salary job- data professions (Job Title vs Salary)
#Job market saturation of top 5-10 professions with the highest salary *check if it is oversaturated (number of every top 5-10 job titles)
#The correlation of company size and the salary (Company Size vs Salary)
#Average salary by Experience Level and Employment Type (Salary vs Experience Level & Employment Type)
import streamlit as st
import pandas as pd
st.set_page_config(
    page_title = "Descriptive",
    page_icon = "📋",
    layout="wide"
)

@st.cache_data
def fetch_data():
    df = pd.read_csv("processed_data.csv")
    st.dataframe(df)

    return df

tab1, tab2, tab3, tab4 = st.tabs(["Average Salary by Exp. Level/Emp. Type", 
                                  "Highest Salary Profession", 
                                  "Job Market Saturation",
                                  "Correlation between Company Size and Salary"])

with tab1:
    st.markdown("#### 🧑 *Average Salary by Experience Level and Employment Type*")
    st.divider()

with tab2:
    st.markdown("#### 📈 *Highest Salary by Profession*")
    st.divider()

with tab3:
    st.markdown("#### 🗺️ *Job Market Saturation of Top 5-10 Highest Salary Professions*")
    st.divider()

with tab4:
    st.markdown("#### 🏢 *Correlation between Company Size and Salary*")
    st.divider()
