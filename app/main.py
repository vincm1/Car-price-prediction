"""Car price predictor Streamlit App"""
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from calculator import render_calculator_page
import matplotlib.pyplot as plt

#### Dataset ####

df = pd.read_csv("cleaned_df.csv", delimiter=",")
df = df[["mileage","make", "model","fuel","gear","offerType","price","hp", "year"]].copy()

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
        st.text("Datenquelle: https://www.kaggle.com/datasets/ander289386/cars-germany")
    with col2: 
        st.image('cars.jpg')
    st.divider()
    #compute top analytics
    mean_price = float(df.price.mean())
    mean_mileage = float(df.mileage.mean())
    marke = tuple(pd.Series(df.make.value_counts().head(1)))
    model = tuple(pd.Series(df.model.value_counts().head(1)))
    total1,total2,total3,total4=st.columns(4,gap='large')
    with total1:
        st.info('Ø Preis EUR',icon="📌")
        st.metric(label="Preis", label_visibility="hidden", value=f"{mean_price:,.0f}".replace(',', '.'))

    with total2:
        st.info('Ø KM-Laufleistung',icon="📌")
        st.metric(label="Laufleistung", label_visibility="hidden", value=f"{mean_mileage:,.0f}".replace(',', '.'))

    with total3:
        st.info('Beliebteste Marke',icon="📌")
        st.metric(label="# Stück in DS",value=f"VW ({marke[0]})")

    with total4:
        st.info('Beliebtestes model',icon="📌")
        st.metric(label="# Stück in DS",value=f"Golf ({model[0]})")
    
    st.divider()
        
    st.subheader(f"Wie sieht Gebrauchtwagenmarkt aus zwischen {df.year.min()} und {df.year.max()} ?")
    
    chart1, chart2, chart3 = st.columns(3, gap="large")

    with chart1:
        st.subheader("Verteilung der Marke:")
        marke_counts = df.make.value_counts()
        st.bar_chart(data=marke_counts)
        
    with chart2:
        st.subheader("Verteilung der PS:")
        # Create a new figure
        fig, ax = plt.subplots()
        # Plot the histogram on the figure's axis
        df.hp.hist(bins=20, ax=ax)
        # Display the figure in Streamlit
        st.pyplot(fig)
        
    with chart3:
        st.subheader("Verteilung der PS:")
        # Create a new figure
        # Create a new figure and axis
        fig, ax = plt.subplots()

        # Plot the scatter plot on the figure's axis
        ax.scatter(df['mileage'], df['price'], alpha=0.5)

        # Customize the plot
        ax.set_title("Scatter plot between mileage and price")
        ax.set_xlabel("Mileage")
        ax.set_ylabel("Price")

        # Display the figure in Streamlit
        st.pyplot(fig)
        
        
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
