#Top highest average salary job- data professions (Job Title vs Salary)
#Job market saturation of top 5-10 professions with the highest salary *check if it is oversaturated (number of every top 5-10 job titles)
#The correlation of company size and the salary (Company Size vs Salary)
#Average salary by Experience Level and Employment Type (Salary vs Experience Level & Employment Type)
import streamlit as st
import pandas as pd
from streamlit_lottie import st_lottie 
import lottie_animations as l
import plotly_express as px

st.set_page_config(
    page_title = "Descriptive",
    page_icon = "📋",
    layout="wide"
)

# function for retrieving dataset
@st.cache_data
def fetch_data():
    df = pd.read_csv("processed_data.csv")
    return df
df = fetch_data()

# function for displaying highest salary model
@st.cache_data
def display_highest_salary_model(currency_type):
    st.markdown("#### 📈 *Highest Salary by Profession (Top 15)*")

    if currency_type == "***USD*** us":
        # Display bar chart with USD salary
        high_salary = df.groupby(["job_title"])["salary_in_usd"].max().head(15).sort_values(ascending=False)
        fig = px.bar(high_salary, color='salary_in_usd', y="salary_in_usd",
                labels={'job_title':'Profession', "salary_in_usd":"Highest Salary (USD)"}, color_continuous_scale="Mint", height=600,text="salary_in_usd")
    else:
        # Display bar chart with MYR salary
        high_salary = df.groupby(["job_title"])["salary_in_myr"].max().head(15).sort_values(ascending=False)
        fig = px.bar(high_salary, color='salary_in_myr', y="salary_in_myr",
                labels={'job_title':'Profession', "salary_in_myr":"Highest Salary (MYR)"}, color_continuous_scale="amp", height=600,text="salary_in_myr")
        
    st.plotly_chart(fig)

# function for job market saturation model
@st.cache_data
def display_job_market_saturation(currency_type):
    st.markdown("#### 🗺️ *Job Market Saturation of Top 15 Highest Salary Professions*")

    # I'm.. not sure how to make this scatter geo plot better atm, WIP
    if currency_type == "***USD*** us":
        top_15_jobs = df.groupby(["job_title"])["salary_in_usd"].max().sort_values(ascending=False).head(15)
        job_market = df[df["job_title"].isin(top_15_jobs.index)]
        fig = px.scatter_geo(job_market, locations="country_name",
                     size="salary_in_usd", locationmode="country names",
                     title="Job Market Saturation of Top 15 Highest Salary Professions", height=600,
                     hover_data = ["job_title","salary_in_usd"]
                     )
    else:
        top_15_jobs = df.groupby(["job_title"])["salary_in_myr"].max().sort_values(ascending=False).head(15)
        job_market = df[df["job_title"].isin(top_15_jobs.index)]
        fig = px.scatter_geo(job_market, locations="country_name",
                     size="salary_in_myr", locationmode="country names",
                     title="Job Market Saturation of Top 15 Highest Salary Professions", height=600,
                     hover_data = ["job_title","salary_in_myr"]
                     )
        
    # alternate scatter plot chart, this also sucks but I'm tired

    fig2 = px.scatter_matrix(job_market, dimensions=["job_title","country_name"], color="job_title", height=900)
    fig2.update_traces(diagonal_visible=False)

    # attempt at a bar chart
    fig3 = px.bar(job_market, x = "job_title", y="country_name", color="country_name", height=900)
    st.plotly_chart(fig)
    st.plotly_chart(fig2)
    st.plotly_chart(fig3)

# function for correlation of size & salary model
@st.cache_data
def display_correlation_size_salary(currency_type):
    st.markdown("#### 🏢 *Correlation between Company Size and Average Salary*")


# function for displaying average salary model
@st.cache_data
def display_average_salary(currency_type):
    st.markdown("#### 🧑 *Average Salary by Experience Level and Employment Type*")
    st.divider()

#create columns for a side-by-side layout of the text and lottie animation
col1, col2 = st.columns([1,1])

#Display text in the first column
with col1:
    st.subheader("**Part 1: Descriptive Models page**")
    st.write("Here, our descriptive models will be displayed, that aim to provide insight on past patterns regarding salary trends in the data science industry, including:")
    st.markdown("* Highest Salary by Profession")
    st.markdown("* Job Market Saturation of Top 5-10 Highest Salary Professions")
    st.markdown("* Correlation between Company Size and Average Salary")
    st.markdown("* Average Salary by Experience Level and Employment Type")

    # radio button for selecting currency type
    currency_type = st.radio(
    "Currency Selection",
    ["***USD*** us", "***MYR*** 🇲🇾"],
    captions = ["United States Dollar", "Malaysian Ringgit"],horizontal=True)

#Display lottie animation in the second column
with col2:
    st_lottie(l.descriptive_lottie, loop = True, width = 600, height = 350, key = None)

#tabs for different desc models 
tab1, tab2, tab3, tab4 = st.tabs(["Highest Salary Profession", 
                                  "Job Market Saturation",
                                  "Company Size vs Average Salary",
                                  "Average Salary"])

with tab1:
    display_highest_salary_model(currency_type)

with tab2:
    display_job_market_saturation(currency_type)

with tab3:
    display_correlation_size_salary(currency_type)

with tab4:
    display_average_salary(currency_type)
    
