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
        top_15_high_sal = df.groupby(["job_title"])["salary_in_usd"].max().sort_values(ascending=False).head(15)
        fig = px.bar(top_15_high_sal, 
                     color='salary_in_usd', 
                     x="salary_in_usd",
                     labels={'job_title':'Profession', "salary_in_usd":"Highest Salary (USD)"}, 
                     color_continuous_scale="Mint", 
                     height=700,
                     width=1200,
                     text="salary_in_usd",
                     orientation="h")
        fig.update_traces(texttemplate='$%{text:.3s}')
    else:
        # Display bar chart with MYR salary
        top_15_high_sal = df.groupby(["job_title"])["salary_in_myr"].max().sort_values(ascending=False).head(15)
        fig = px.bar(top_15_high_sal, 
                     color='salary_in_myr', 
                     x="salary_in_myr",
                     labels={'job_title':'Profession', "salary_in_myr":"Highest Salary (MYR)"}, 
                     color_continuous_scale="amp", 
                     height=700,
                     width=1200,
                     text="salary_in_myr",
                     orientation="h")
        fig.update_traces(texttemplate='RM%{text:.3s}')
    
    fig.update_traces(
        textfont = dict(
            family = "Arial MT Extra Bold",   
            size=20,
            color = "black"   
        ),
        width = 0.6,
        textangle = 0
    )

    fig.update_layout(
        bargap=0.2,
        legend = dict(font=dict(size=15)),
        xaxis = dict(tickfont=dict(size=15)),
        yaxis = dict(tickfont=dict(size=15))
    )
    st.plotly_chart(fig)

# function for job market saturation model
@st.cache_data
def display_job_market_saturation(currency_type):
    st.markdown("#### 🗺️ *Job Market Saturation of Top 15 Highest Salary Professions*")

    if currency_type == "***USD*** us":
        top_15_high_sal = df.groupby(["job_title"])["salary_in_usd"].max().sort_values(ascending=False).head(15)
    else:
        top_15_high_sal = df.groupby(["job_title"])["salary_in_myr"].max().sort_values(ascending=False).head(15)

    job_market = df[df["job_title"].isin(top_15_high_sal.index)]
    fig = px.pie(job_market, 
                 values=job_market.job_title.value_counts().values, 
                 names=job_market.job_title.value_counts().index, 
                 height=800,
                 width=1200
                 )
    
    fig.update_traces(
        textfont=dict(
            family="Arial MT",  
            size=22,       
            color="white"   
        )
    )

    fig.update_layout(
        legend=dict(font=dict(family="Arial MT Extra Bold",size=20))
    )
    st.plotly_chart(fig)

# function for correlation of size & salary model
@st.cache_data
def display_correlation_size_salary(currency_type):
    st.markdown("#### 🏢 *Correlation between Company Size and Salary*")

    if currency_type == "***USD*** us":
        top_15_avrg_sal = df.groupby(["job_title"])["salary_in_usd"].mean().sort_values(ascending=False).head(15)

        job_market = df[df["job_title"].isin(top_15_avrg_sal.index)]
        job_market.loc[:,"company_size"] = job_market.company_size.replace({"S":"Small","M":"Medium","L":"Large"})

        avrg_sal_by_comp_size = job_market.groupby(["company_size"])["salary_in_usd"].mean()

        fig = px.bar(avrg_sal_by_comp_size, color=avrg_sal_by_comp_size.index, y="salary_in_usd",
                labels={'company_size':'Company Size', "salary_in_usd":"Average Salary (USD)"}, 
                color_discrete_map={"S":"#74FF00", "M":"#28BBFF", "L":"#FA3819"}, 
                height=600,
                width=900,
                text="salary_in_usd",
                category_orders={"company_size": ["Small", "Medium", "Large"]})
        fig.update_traces(texttemplate='$%{text:.3s}')
    else:
        top_15_avrg_sal = df.groupby(["job_title"])["salary_in_myr"].mean().sort_values(ascending=False).head(15)

        job_market = df[df["job_title"].isin(top_15_avrg_sal.index)]
        job_market.loc[:,"company_size"] = job_market.company_size.replace({"S":"Small","M":"Medium","L":"Large"})

        avrg_sal_by_comp_size = job_market.groupby(["company_size"])["salary_in_myr"].mean()

        fig = px.bar(avrg_sal_by_comp_size, color=avrg_sal_by_comp_size.index, y="salary_in_myr",
                labels={'company_size':'Company Size', "salary_in_myr":"Average Salary (MYR)"}, 
                color_discrete_map={"S":"#74FF00", "M":"#28BBFF", "L":"#FA3819"}, 
                height=600,
                width=900,
                text="salary_in_myr",
                category_orders={"company_size": ["Small", "Medium", "Large"]})

        fig.update_traces(texttemplate='RM%{text:.3s}')

    fig.update_traces(
        textfont = dict(
            family="Arial MT Extra Bold",  
            size=20,       
            color="black"   
        ),
        width = 0.4
    )

    fig.update_layout(
        bargap = 0.01,
        legend = dict(font=dict(size=15)),
        xaxis = dict(tickfont=dict(size=15)),
        yaxis = dict(tickfont=dict(size=15))
    )
    st.plotly_chart(fig)
    
# function for displaying average salary model
@st.cache_data(experimental_allow_widgets= True)
def display_average_salary(currency_type):
    st.markdown("#### 🧑 *Average Salary by Experience Level and Employment Type*")
    st.divider()
    
    col_a, col_b = st.columns([1,1])
    with col_a:
        st.write("#### Experience Level")
        st.write("- **EN**: Entry-Level")
        st.write("- **EX**: Executive-Level")
        st.write("- **MI**: Mid-Level")
        st.write("- **SE**: Senior-Level")
    with col_b:
        st.write("#### Employment Type")
        st.write("- **CT**: Contract")
        st.write("- **FL**: Freelance")
        st.write("- **FT**: Full-Time")
        st.write("- **PT**: Part-Time")
    
    ## OPTIONAL CHECKBOXES
    # col_c, col_d = st.columns([7,3])
    # with col_d:
    #     # Selection for experience levels
    #     exp_levels = ["EN", "EX", "MI", "SE"]
    #     selected_levels = []
        
    #     for level in exp_levels:
    #         if st.checkbox(f"Show {level}", value = True):
    #             selected_levels.append(level)
        
    # with col_c:
    if currency_type == "***USD*** us":
        #Restructuring the dataframe 
        new_df = df.groupby(["experience_level", "employment_type"])["salary_in_usd"].mean().round(2).reset_index()
        #new_df = new_df[new_df["experience_level"].isin(selected_levels)]  # Filter based on selected levels
        new_df = new_df.pivot(index = "experience_level", columns = "employment_type")["salary_in_usd"].fillna(0)
        
        #Creating heatmap
        fig = px.imshow(new_df, x = new_df.columns, y = new_df.index, text_auto = True, 
                    color_continuous_scale= "Viridis", width = 750, height = 750) 
        fig.update_layout(xaxis_title="<b>Employment Type</b>", yaxis_title="<b>Experience Level</b>"
                        ,coloraxis_colorbar=dict(title="Average Salary (USD)"))       
    else:
        #Restructuring the dataframe 
        new_df = df.groupby(["experience_level", "employment_type"])["salary_in_myr"].mean().round(2).reset_index()
        #new_df = new_df[new_df["experience_level"].isin(selected_levels)]  # Filter based on selected levels
        new_df = new_df.pivot(index = "experience_level", columns = "employment_type")["salary_in_myr"].fillna(0)
        
        #Creating heatmap
        fig = px.imshow(new_df, x = new_df.columns, y = new_df.index, text_auto = True, 
                    color_continuous_scale= "Viridis", width = 750, height = 750) 
        fig.update_layout(xaxis_title="<b>Employment Type</b>", yaxis_title="<b>Experience Level</b>"
                        ,coloraxis_colorbar=dict(title="Average Salary (MYR)"))       

    st.plotly_chart(fig)

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
    "**Currency Selection**",
    ["***USD*** us", "***MYR*** 🇲🇾"],
    captions = ["United States Dollar", "Malaysian Ringgit"],horizontal=True)

#Display lottie animation in the second column
with col2:
    st_lottie(l.descriptive_lottie, loop = True, width = 600, height = 350, key = None)

#tabs for different desc models 
tab1, tab2, tab3, tab4 = st.tabs(["Highest Salary Profession", 
                                  "Job Market Saturation",
                                  "Company Size vs Average Salary",
                                  "Average Salary by Exp Level & Emp Type"])

with tab1:
    display_highest_salary_model(currency_type)

with tab2:
    display_job_market_saturation(currency_type)

with tab3:
    display_correlation_size_salary(currency_type)

with tab4:
    display_average_salary(currency_type)
    