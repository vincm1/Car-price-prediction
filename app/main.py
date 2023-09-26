"""Car price predictor Streamlit App"""
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from calculator import render_calculator_page

#### Dataset ####

df = pd.read_csv("cleaned_df.csv", delimiter=",")

#### Page setup ####

st.set_page_config(
    page_title="Dein Gebrauchtwagenrechner",
    page_icon=":car:",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
    #     'Get Help': 'Test',
    #     'Report a bug': "Test",
        'About': "Das ist eine Portfolio App"
    }
)

#### Homepage setup ####

def render_homepage():
    """ Rendering the homepage components"""
    col1, col2 = st.columns([1,1], gap="large")
    with col1:
        st.title(":oncoming_automobile: Dein unabhängiger Gebrauchtwagenpreisrechner!", )
        st.subheader("Lass dir den Preis deines Gebrauchtwagen berechnen.")
        st.text(f"Anhand von {len(df)} Fahrzeugen den besten Preis für deinen Gebrauchten finden.")
    
    with col2: 
        st.image('cars.jpg')
    
    st.divider()
    
    container = st.container()
    container.write("This is inside the container")
    st.write("This is outside the container")

    # Now insert some more in the container
    container.write("This is inside too")

    # Showcasing dataset #

#### NAVIGATION ####
# Create a sidebar to navigate between the pages
#st.sidebar.title("Navigation")
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
