"""Car price predictor Streamlit App"""
import streamlit as st
import numpy as np
from streamlit_option_menu import option_menu
from calculator import render_calculator_page

#### Homepage setup ####

def render_homepage():
    """ Rendering the homepage components"""
    st.title("This is the homepage!")

# Create a sidebar to navigate between the pages
st.sidebar.title("Navigation")
sidebar_pages = ["Home", "About"]
current_page = option_menu(
    menu_title=None,
    options=["Home", "Calculator"],
    default_index=0,
    orientation="horizontal",
    icons = ["house", "calculator-fill"],
)

# Render the appropriate page based on the user's selection
if current_page == "Home":
    # Render the home page
    render_homepage()
elif current_page == "Calculator":
    # Render the about page
    render_calculator_page()
else:
    # Render the default page
    render_homepage()
