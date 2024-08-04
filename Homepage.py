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
from streamlit_lottie import st_lottie
import plotly.express as px
import lottie_animations as l

df = pd.read_csv("processed_data.csv")

st.set_page_config(
    page_title = "Homepage",
    page_icon = "🏠",
    layout="wide"
)

def workYearDistribution_pie_chart():
    work_year_df = df["work_year"].value_counts().reset_index()
    work_year_df.columns = ['work_year', 'count']
    return px.pie(work_year_df, values = 'count', names = 'work_year', title = "Pie Chart")    

#Homepage Opening
st.title("💵 Data Science Salary Trends 💵")
st.write("In recent years, there has been a significant surge in interest in data science as a profession. This trend is mainly driven by the increasing reliance on data-driven decision-making across industries.")

st.subheader("Data Science Platform Market Size to Reach USD 501.03 Bn by 2032")
st.image("Data-Science-Platform-Market-Size.jpg", caption= "Bar Graph")
st.write("Based on **Precedence Research**, The global data science platforms market was valued at USD 112.12 billion in 2022. Thus, it is expected to grow significantly, reaching about USD 501.03 billion by 2032. This means it will grow at an average annual rate of 16.2% from 2023 to 2032.") 

#Data science salary trends over time 
salary_trend = df.groupby('work_year')['salary_in_usd'].mean().reset_index()
fig = px.line(salary_trend, x='work_year', y='salary_in_usd', title='Data Science Salary Trends Over Time')
fig.update_traces(line=dict(dash='dash'))  # Show legend with title, add line markers, and set dash linestyle
fig.update_layout(
    showlegend=True,
    legend_title="Salary Trends",
    xaxis_title="Work Year",
    yaxis_title="Salary in USD",
    yaxis=dict(range=[0, 200000])  # Set the range for the y-axis
)
st.plotly_chart(fig)
st.write("Within the dataset, at first it shows that there is an stagnant trend since 2020. Subsequently, there are continual positive changes in salary from 2021 to 2022. Ultimately, the steep uphill of trend in salary surge at an all-time high towards the end of the year 2023.")

st.write("***As the demand for skilled data scientists continues to grow, it is important to understand salary trends in this field for:***")
#1st point for salary trend importance

col3, col4 = st.columns([1,1])

with col3:
    st.subheader("*Guidance for Graduates and Job Seekers*")
    st.write("With an increasing number of **computer science postgraduates** aspiring to specialize in data science, this dashboard provides critical insights into salary expectations. Graduates can make informed decisions about their career paths based on up-to-date salary data.")
    st.write("**Market Competitiveness:** Job seekers can use this information to negotiate better salaries and benefits, ensuring they receive compensation that reflects their skills and the current market demand.")

with col4:
    st_lottie(l.graduation_lottie, loop = True, width = 600, height = 250, key = None)

#2nd point for salary trend importance
col5, col6  = st.columns([1,1])

with col5:
    st_lottie(l.professional_lottie, loop = True, width = 600, height = 250, key = None)

with col6:
    st.subheader("*Industry Professionals*")
    st.write("For those already in the field, understanding salary trends can highlight opportunities for career advancement and identify areas where additional skills or certifications may lead to higher earnings.")
    st.write("**Benchmarking:** Professionals can benchmark their current salary against industry standards based on our informative dashboard, thus helping them to assess whether their current role is meeting their financial goals.")
 
#Pie Chart for Work Year Distribution
st.subheader("Work Year Distribution")   
fig = workYearDistribution_pie_chart()
st.plotly_chart(fig)

st.write("The timeframe for the descriptive and predictive analytics in our dashboard spans the work years from 2020 to 2023.")