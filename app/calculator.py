"""Car price predictor Streamlit App"""
import streamlit as st
import xgboost as xgb
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error

df = pd.read_csv("cleaned_df.csv", delimiter=",")

bst = xgb.Booster()
bst.load_model('xgboost_best_regressor.json')

def predict_car_price(input_data):
    bst.predict()
    return None

### Form options ###
marken = df.make.unique()
models = df.model.unique()
fuel_types = df.fuel.unique()
offer_types = df.offerType.unique()
gear_types = df.gear.unique()

### Page rendering ###

def render_calculator_page():
    """ Func for rendering the calcualtor page"""
    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.title(":car: :money_mouth_face: Gebrauchtwagenpreisrechner")
    
    with col2: 
        st.image('kaefer.jpg')
    
    st.divider()
    st.subheader("Gib uns nähere Infos zum Fahrzeug")
    col1, col2, col3 = st.columns(3, gap="large")
    with col1:
        marke = st.selectbox(label="Marke des Fahrzeugs", options=marken)
        model = st.selectbox(label="Model", options=models)

    with col2:
        mileage = st.number_input("KM Laufleistung:", min_value=0)
        hp = st.slider(label="PS", min_value=1, max_value=1000, step=1)
        
    with col3:
        year = st.number_input(label="Jahr")
        fuel_type = st.selectbox(label="Antrieb", options=fuel_types)
        gear_type = st.selectbox(label="Schaltung", options=gear_types)
        offer_type = st.selectbox(label="Angebot", options=offer_types)
        
    car_predict = {"mileage":mileage, "marke":marke, "model":model, "hp":hp, "year":year, "fuel_type":fuel_type, "gear_type":gear_type, "offer_type":offer_type}
    st.text(f"{car_predict}")
    st.button("Preis berechnen")