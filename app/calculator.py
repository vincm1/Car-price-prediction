"""Car price predictor Streamlit App"""
import pickle
import streamlit as st
import xgboost as xgb

xgb_model = pickle.load(open('xgboost_regressor.pkl','rb'))

def render_calculator_page():
    """ Func for rendering the calcualtor page"""
    st.title("Preisrechner")
