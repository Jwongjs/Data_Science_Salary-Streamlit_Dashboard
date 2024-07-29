import pandas as pd
import streamlit as st
from streamlit_lottie import st_lottie
import lottie_animations as l
import pickle
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("processed_data.csv")

st.set_page_config(
    page_title = "Salary Prediction",
    page_icon = "📈",
    layout="wide"
)

def page_intro_section():
    ##Page introduction section
    col1, col2 = st.columns([2,1])
    with col1:
        st.title("Data Science Salary Prediction")
        st.subheader("**In this section, we will attempt to predict the $alary of data professionals based on the selected features:**")
        col3, col4 = st.columns([1,1])
        with col3:
            st.write("""
                    - **Job Title:** Specific data science profession label
                    - **Country:** Location of the company 
                    - **Experience Level:** Employee level of work experience  
                    """)
        with col4:
            st.write("""
                    - **Employment Type:** Type of employment 
                    - **Company Size:** Size of companies
                    """)
    with col2:
        st_lottie(l.ai_lottie, loop = False, width = 300, height = 300, key = None)

def select_box_section():
    #Job Title and Country
    job_title = st.selectbox("Select Job Title:", df["job_title"].sort_values().unique())
    country = st.selectbox("Select Country:", df["country_name"].sort_values().unique())

    #Experience Level, Employment Type and Company Size
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        experience_level = st.selectbox("Select Experience Level:", df["experience_level"].unique())
    with col2:
        employment_type = st.selectbox("Select Employment Type:", df["employment_type"].unique())
    with col3:
        company_size = st.selectbox("Select Company Size:", df["company_size"].unique())
        
    with st.expander("Check short-form meaning"):
        col_a, col_b, col_c = st.columns([1, 1, 1])
        with col_a:
            st.write("#### Experience Level")
            st.write("- **EN**: Entry-Level")
            st.write("- **EX**: Executive-Level")
            st.write("- **MI**: Mid-Level")
            st.write("- **SE**: Senior-Level")
        with col_b:
            st.write("#### Employment Type")
            st.write("- **FT**: Full-Time")
            st.write("- **PT**: Part-Time")
            st.write("- **CT**: Contract")
            st.write("- **FL**: Freelance")
        with col_c:
            st.write("#### Company Size")
            st.write("- **L**: Large")
            st.write("- **M**: Medium")
            st.write("- **S**: Small")
        
    return job_title, country, experience_level, employment_type, company_size

def encode_process(job_title, country, experience_level, employment_type, company_size):
    feature_df = pd.DataFrame({"job_title": [job_title], "country_name": [country], "experience_level": [experience_level], "employment_type": [employment_type], "company_size": [company_size]})
    new_df = df.drop(columns = ['salary', 'salary_currency', 'salary_in_usd', 'work_year', 'company_location', 'salary_in_myr'], axis = 1)
    
    # Dictionary to store the encoders
    feature_encoders = {}   
    
    #Encode Features
    encoded_columns = ['job_title', 'country_name', 'experience_level', 'employment_type', 'company_size']
    for column in encoded_columns:
        le = LabelEncoder()
        new_df[column] = le.fit_transform(df[column])
        #Each LabelEncoder (le) object is stored in a dictionary with the column name as the key.
        feature_encoders[column] = le
    
    # Encode the feature_df using the same encoders
    for column in encoded_columns:
        feature_df[column] = feature_encoders[column].transform(feature_df[column])
        
    return feature_df
    
#Import regressor model 
model_file_path = "Salary Regressor Model/xgb_regressor.pkl"
with open(model_file_path, 'rb') as f:
    salary_regressor = pickle.load(f)

##Main
page_intro_section()

# radio button for selecting currency type
currency_type = st.radio(
"**Currency Selection**",
["***USD*** us", "***MYR*** 🇲🇾"],
captions = ["United States Dollar", "Malaysian Ringgit"],horizontal=True)

st.divider()

st.write("*Prediction is not 100% accurate. The accuracy is solely based on the values provided in dataset.")

job_title, country, experience_level, employment_type, company_size = select_box_section()

button_clicked = st.button("Predict")

if button_clicked:
    feature_df = encode_process(job_title, country, experience_level, employment_type, company_size) 
    
    salary_prediction = salary_regressor.predict(feature_df)

    st_lottie(l.money_lottie, loop=False, width=450, height=200, key=None)
    
    if currency_type == "***USD*** us":
        st.subheader(f"The predicted salary is: ${salary_prediction[0]:,.2f}")
    else:
        myr_salary = salary_prediction[0] * 4.70
        st.subheader(f"The predicted salary is: RM{myr_salary:,.2f}")
