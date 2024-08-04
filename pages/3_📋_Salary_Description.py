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
    page_title = "Salary Description",
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
    if currency_type == "***USD*** us":
        # Display bar chart with USD salary
        top_15_high_sal = df.groupby(["job_title"])["salary_in_usd"].mean().sort_values(ascending=False).head(15)
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
        top_15_high_sal = df.groupby(["job_title"])["salary_in_myr"].mean().sort_values(ascending=False).head(15)
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
    if currency_type == "***USD*** us":
        top_15_high_sal = df.groupby(["job_title"])["salary_in_usd"].mean().sort_values(ascending=False).head(15)
    else:
        top_15_high_sal = df.groupby(["job_title"])["salary_in_myr"].mean().sort_values(ascending=False).head(15)

    job_market = df[df["job_title"].isin(top_15_high_sal.index)]
    #Can try sunburst chart
    fig = px.pie(job_market, 
                 values=job_market.job_title.value_counts().values, 
                 names=job_market.job_title.value_counts().index, 
                 height=600,
                 width=1200
                 )
    
    fig.update_traces(
        textfont=dict(
            family="Arial MT",  
            size=12,       
            color="white"   
        )
    )

    fig.update_layout(
        legend=dict(font=dict(family="Arial MT Extra Bold",size=15))
    )
    st.plotly_chart(fig)

# function for correlation of size & salary model
@st.cache_data
def display_correlation_size_salary(currency_type):
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
@st.cache_data()
def display_average_salary(currency_type):
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

def display_entry_level_job(currency_type):
    entry_lvl_jobs_df = df[df["experience_level"] == "EN"]
    if currency_type == "***USD*** us":
        # Calculate job title counts and average salary
        job_titles_df = entry_lvl_jobs_df.groupby("job_title").agg(count=("job_title", "count"), avg_salary=("salary_in_usd", "mean")).reset_index()
        salary_prefix = "$"
    else:
        job_titles_df = entry_lvl_jobs_df.groupby("job_title").agg(count=("job_title", "count"), avg_salary=("salary_in_myr", "mean")).reset_index()
        salary_prefix = "RM"

    # Create a new column with job title and average salary for display in the treemap
    job_titles_df["label"] = job_titles_df.apply(lambda x: f"{x['job_title']}<br>Avg Salary: {salary_prefix}{x['avg_salary']:,.0f}", axis=1)

    fig = px.treemap(job_titles_df, path=['label'], values='count')
    # Update the font size and text position
    fig.update_traces(
        textinfo='label+value', 
        textfont_size=16, 
        textposition='middle center',
        hovertemplate = '<b>%{label}</b><br>Count: %{value}<extra></extra>' #to supress default display of parent and id hover data
        )
    fig.update_layout(width=1250, height=700)
    st.plotly_chart(fig)
    
col1, col2 = st.columns([1,1])
#Display text in the first column
with col1:
    st.subheader("**Part 1: Descriptive Models page**")
    st.write("Here, our descriptive models will be displayed, that aim to provide insight on past patterns regarding salary trends in the data science industry, including:")
    st.markdown("* Highest Salary by Profession")
    st.markdown("* Job Market Saturation of Top 5-10 Highest Salary Professions")
    st.markdown("* Correlation between Company Size and Average Salary")
    st.markdown("* Average Salary by Experience Level and Employment Type")
    st.markdown("* Entry-Level Job Recommendations")

    # radio button for selecting currency type
    currency_type = st.radio(
    "**Currency Selection**",
    ["***USD*** us", "***MYR*** 🇲🇾"],
    captions = ["United States Dollar", "Malaysian Ringgit"],horizontal=True)

#Display lottie animation in the second column
with col2:
    st_lottie(l.descriptive_lottie, loop = True, width = 600, height = 350, key = None)

#tabs for different desc models 
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Highest Average Salary Profession", 
                                  "Job Market Saturation",
                                  "Company Size vs Average Salary",
                                  "Average Salary by Exp Level & Emp Type", 
                                  "Entry-Level Job Distribution"])

with tab1:
    st.markdown("#### 📈 *Highest Average Salary by Profession (Top 15)*")
    st.write("- Horizontal bar chart that shows the top 15 highest average annual salary of job professions")
    st.write("- Color intensity represents the salary amount, shade darkens as salary increases")
    st.divider()
    display_highest_salary_model(currency_type)
    st.write("As seen above in the bar chart, the Data Science Tech Lead position is clearly in the lead in terms of annual salary with \$375k, showing that a leadership position such as Data Science Tech Lead is a very well paying position, as also shown by the presence of other leadership or managerial positions such as Data Science Manager and Data Analytics Lead.")
    st.write("On the other hand, the overall range of top 15 highest average annual salary is from \$163k to \$375k, with most top jobs here falling within the \$175k-\$215k range, such as Data Infrastructure Lead at \$175k to Data Lead at \$213k.")

with tab2:
    st.markdown("#### 🗺️ *Job Market Saturation of Top 15 Highest Salary Professions*")
    st.write("- Pie chart showing the job market saturation of the top 15 professions with highest average salary")
    st.write("- Color coded based on profession")
    st.divider()
    display_job_market_saturation(currency_type)
    st.write("As the pie chart shows, out of the top 15 highest average salary jobs, the two positions with the biggest slice of the pie, or the most saturated within the market are Applied Scientist and Data Science Manager, covering 29% of all positions each.")
    st.write("Going off of the previous bar chart showing the average salaries of these two jobs, roughly 58% of the top job positions have an average annual salary of \$190k-\#191k.")

with tab3:
    st.markdown("#### 🏢 *Correlation between Company Size and Salary*")
    st.write("- Bar chart showing the correlation between company size, and average salary of the job positions")
    st.write("- S = Small, M = Medium, L = Large")
    st.divider()
    display_correlation_size_salary(currency_type)
    st.write("Here, the bar chart shows the average salaries of companies based on their size. The main correlation that can be interpreted from the results here is that, medium and large-sized companies seem to have higher average salaries overall, at \$192k and \$186k respectively, while smaller companies have lower annual incomes for their job positions at \$159k.")
    st.write("This does mean that job applicants may want to seek job positions within medium to large sized companies if they wish for higher salaries, on average.")

with tab4:
    st.markdown("#### 🧑 *Average Salary by Experience Level and Employment Type*")
    st.write("- Heatmap below shows the average salary based on the combined features of experience level and employment type")
    st.write("- The color intensity represents the salary amount")
    st.divider()
    
    col1, col2 = st.columns([1,1])
    with col1:
        display_average_salary(currency_type)
    
    with col2: 
        col_a, col_b = st.columns([1,1])

        with col_b:
            for i in range(5):
                st.markdown("<br>", unsafe_allow_html=True)  # Adds a blank line
            
            st.write("#### Experience Level")
            st.write("- **EN**: Entry-Level")
            st.write("- **EX**: Executive-Level")
            st.write("- **MI**: Mid-Level")
            st.write("- **SE**: Senior-Level")
            
            st.write("#### Employment Type")
            st.write("- **CT**: Contract")
            st.write("- **FL**: Freelance")
            st.write("- **FT**: Full-Time")
            st.write("- **PT**: Part-Time")
    
    st.write("The heatmap above shows the highest average salary at $416k for \"Executive-Level\" experience and \"Contract\" employment. This may suggest that \"Contract\" employment type is employed for certain projects and make more frequent top-level decisions with \"Executive-Level\" position.")
    st.write("On the other hand, the lowest average salary is at $100k for \"Entry-Level\" experience and \"Part-Time\" employment. This may suggest that \"Part-Time\" employment type is employed for less demanding and basic workloads in which they may also be supervised at the \"Entry-Level\" position.")
            
with tab5:
    st.markdown("#### 📚 *Entry-Level Job Distribution*")
    st.write("- Treemap below suggests the most sought-after entry-level jobs for aspiring postgraduates")
    st.write("- Including the count and average salary for each job title")
    st.divider()
    display_entry_level_job(currency_type)
    
    st.write("The treemap above shows that the most sought-after entry-level job is Data Engineer, with a count of 66 and an average salary of $91,527. This may suggest that Data Analyst is a popular entry-level job for aspiring postgraduates which may also allow for further career growth.")
    st.write("Even though Machine Learning Engineer has a higher average salary of $94,276, it has a lower count of 21. This may suggest that Machine Learning Engineer is a more specialized entry-level job that requires more experience and knowledge in the field.")
    