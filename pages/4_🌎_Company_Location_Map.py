import streamlit as st
import pandas as pd
from streamlit_lottie import st_lottie 
import lottie_animations as l
import plotly_express as px
import matplotlib.pyplot as plt

map_scope = {"NA":"north america","SA":"south america","AS":"asia","AF":"africa","EU":"europe"}
map_scope_title = {"NA":"North America","SA":"South America","AS":"Asia","AF":"Africa","EU":"Europe"}
st.set_page_config(
    page_title = "Company Location Map",
    page_icon = "🌎",
    layout="wide"
)

@st.cache_data
def fetch_data():
    df = pd.read_csv("processed_data.csv")
    return df
df = fetch_data()

def handle_click(trace, points, state):
    if points.point_inds:
        selected_country = grouped_df.iloc[points.point_inds[0]]['country_name']
        st.write(f"You clicked on {selected_country}")

def display_map(map_scope_rb):
    st.subheader(f"Map of Company Locations: {map_scope_title[map_scope_rb]}")
    grouped_df = df.groupby('country_name', as_index=False).agg({'salary_in_usd': 'mean'})

    fig = px.choropleth(grouped_df, locations="country_name",
                         scope=map_scope[map_scope_rb],
                         locationmode="country names",
                         color="salary_in_usd",
                         width=1300,
                         height=800,
                        )
    fig.update_traces(marker_line_width=0.5)
    fig.update_layout(clickmode='event+select')
    st.plotly_chart(fig, use_container_width=True)

col1, col2 = st.columns([2,1])
with col1:
       st.subheader("**Company Location Map**")
       st.write("This section will contain our interactive map to view data science salary job data by country.")
       map_scope_rb = st.radio(
             "**Map Scope Selection**",
             ["NA", "EU", "SA", "AF","AS"],
             captions = ["North America", "Europe", "South America","Africa", "Asia"],horizontal=True)
       with col2:
           st_lottie(l.ai_lottie, loop = False, width = 300, height = 300, key = None)

display_map(map_scope_rb)