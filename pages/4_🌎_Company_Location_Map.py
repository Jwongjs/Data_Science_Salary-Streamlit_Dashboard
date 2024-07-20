from matplotlib import container
import streamlit as st
import pandas as pd
from streamlit_lottie import st_lottie 
import lottie_animations as l
import plotly_express as px
import matplotlib.pyplot as plt
from streamlit_plotly_events import plotly_events


map_scope = {"NA":"north america","SA":"south america","AS":"asia","AF":"africa","EU":"europe"}
map_scope_title = {"NA":"North America","SA":"South America","AS":"Asia","AF":"Africa","EU":"Europe"}
st.set_page_config(
    page_title = "Company Location Map",
    page_icon = "🌎",
    layout="wide"
)

st.markdown("""<style>
             * {
                ::before, ::after {
                box-sizing: inherit;
                }
            </style>""", unsafe_allow_html=True)

@st.cache_data
def fetch_data():
    df = pd.read_csv("processed_data.csv")
    return df
df = fetch_data()

def display_map(map_scope_rb, currency_type):
    st.subheader(f"Map of Company Locations: {map_scope_title[map_scope_rb]}")
    if currency_type == "***USD*** us":
        grouped_df = df.groupby('country_name', as_index=False).agg({'salary_in_usd': 'mean'})
        currency_type = "salary_in_usd"
        legend_title = "Average Salary in USD"
    else:
        grouped_df = df.groupby('country_name', as_index=False).agg({'salary_in_myr': 'mean'})
        currency_type = "salary_in_myr"
        legend_title = "Average Salary in MYR"
    
    fig = px.choropleth(grouped_df, locations="country_name",
                         scope=map_scope[map_scope_rb],
                         locationmode="country names",
                         color=currency_type,
                         width=1300,
                         height=800,
                         color_continuous_scale="bupu",
                         fitbounds="locations"
                        )
    fig.update_traces(marker_line_width=0.5)
    fig.update_layout(
        coloraxis_colorbar=dict(
            title=dict(
                text=legend_title,
                font=dict(size=20)  # Adjust the font size as needed
            ),
        tickfont=dict(
            size=18
        ),
    ))

    st.plotly_chart(fig)

def display_info(map_scope_rb, currency_type):
    country = st.selectbox("Country Selection:",
                        df[df.continent_name == map_scope_title[map_scope_rb]]["country_name"].sort_values(ascending=True).unique())
    
    country_df = df[df.country_name == country]
    if currency_type == "***USD*** us":
        currency_type = "salary_in_usd"
        prefix = "$"
    else:
        currency_type = "salary_in_myr"
        prefix = "RM"

    exp_level_dict = {"EN":"entry level (EN)","EX":"experienced level (EX)","MI":"mid level (MI)","SE":"senior level (SE)"}
    
    count_jobs = country_df.shape[0]
    average_sal = "{:.2f}".format(country_df[currency_type].mean())
    count_exp = exp_level_dict[country_df.experience_level.mode().iloc[0]]

    highest_paying_job = country_df[country_df[currency_type] == country_df[currency_type].max()]["job_title"].mode().iloc[0]
    count_highest_paying = country_df[country_df.job_title == highest_paying_job].shape[0]
    highest_avrg_sal = "{:.2f}".format(country_df[country_df.job_title == highest_paying_job][currency_type].mean())

    most_common_job = country_df["job_title"].mode().iloc[0]
    count_most_common = country_df[country_df.job_title == most_common_job].shape[0]
    most_common_avrg_sal = "{:.2f}".format(country_df[country_df.job_title == most_common_job][currency_type].mean())
    st.subheader("**Within the dataset:**")
    col1, col2, col3 = st.columns(3)
    with col1:
        if count_jobs == 1:
            st.markdown(f"There is only ***{count_jobs}*** data science position recorded in ***{country}***.")
        else:
            st.markdown(f"There are ***{count_jobs}*** data science positions recorded in ***{country}***.")
        st.markdown(f"The average salary of all jobs within ***{country}*** is ***{prefix + average_sal}***.")
        st.markdown(f"The most common experience level for data science positions within ***{country}*** are ***{count_exp}*** positions.")
    with col2:
        st.markdown(f"The highest paying data science position in ***{country}*** is ***{highest_paying_job}***.")
        if count_highest_paying == 1:
            st.markdown(f"There is only ***{count_highest_paying}*** recorded instance of ***{highest_paying_job}*** postions in ***{country}***.")
        else:
            st.markdown(f"There are ***{count_highest_paying}*** recorded instances of ***{highest_paying_job}*** positions in ***{country}***.")
        st.markdown(f"The average salary of ***{highest_paying_job}*** is ***{prefix + highest_avrg_sal}***.")
    with col3:
        st.markdown(f"The most common data science position in ***{country}*** is ***{most_common_job}***.")
        if count_most_common == 1:
            st.markdown(f"There is only ***{count_most_common}*** recorded instance of ***{most_common_job}*** postions in ***{country}***.")
        else:
            st.markdown(f"There are ***{count_most_common}*** recorded instances of ***{most_common_job}*** positions in ***{country}***.")
        st.markdown(f"The average salary of ***{most_common_job}*** is ***{prefix + most_common_avrg_sal}***.")





col1, col2 = st.columns([2,1])
with col1:
    st.subheader("**Company Location Map**")
    st.write("This section will contain our interactive map to view data science salary job data by country.")
    st.write("Below, you can choose which country to display data of, the scope of the map to display based on continent, the currency type to display salary amounts with.")
    st.write("Upon selecting a country, data about the data science positions within that country will be displayed.")
    st.write("Note: The dataset used for this project does not have data for every country in the world, and some countries have low recorded instances, which may not reflect the true state of the data science industry in said countries.")
with col2:
    st_lottie(l.map_lottie, loop = False, width = 300, height = 300, key = None)

container = st.container(border=False)

col3, col4 = st.columns([2,1])

with col3:
    map_scope_rb = st.radio(
        "**Map Scope Selection**",
        ["NA", "EU", "SA", "AF","AS"],
        captions = ["North America", "Europe", "South America","Africa", "Asia"],horizontal=True)
with col4:
    currency_type = st.radio(
        "**Currency Selection**",
        ["***USD*** us", "***MYR*** 🇲🇾"],
        captions = ["United States Dollar", "Malaysian Ringgit"],horizontal=True)
    
with container:
    display_map(map_scope_rb, currency_type)

display_info(map_scope_rb, currency_type)