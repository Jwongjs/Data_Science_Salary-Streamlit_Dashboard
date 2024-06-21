import streamlit as st
from streamlit_lottie import st_lottie
import json


#lottie is an animation or image that can be implemented inside streamlit web page
#Function for opening lottie file url imported from Lottiefiles
def load_lottiefile(filepath):
    with open(filepath) as f:
        return json.load(f)
    
welcome_lottie = load_lottiefile(r"lottie_animations\Welcome.json")
graduation_lottie = load_lottiefile(r"lottie_animations\Graduation.json")
professional_lottie = load_lottiefile(r"lottie_animations\Professional.json")