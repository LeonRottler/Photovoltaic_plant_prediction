# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 23:54:35 2023

@author: leonr
"""

import streamlit as st
import pandas as pd 
import pickle

try:
    data = pd.read_csv("C:/Users/leonr/Documents/Git/Photovoltaic_plant_prediction/Data/data.csv").set_index("MESS_DATUM")
    model = pickle.load(open("C:/Users/leonr/Documents/Git/Photovoltaic_plant_prediction/ML/xgb_model.pkl", "rb"))
except:
    print("Error while trying to read data or model!")

def prediciton(pred_df): 
    pred = model.predict(pred_df)
    return pred

st.header("Photovoltaic plan prediction")
st.caption("This system provides you with information about the estimated energy produced by the photovoltaic plan in the next days.")
st.caption("Because of problems with the API, it is currently not possible to perform automated prediction. Therefore you have to put in the values with the silder and start the prediction by clicking the button. Sorry for that :)")

    
RSK = st.slider("Tägliche Niederschlagshöhe [mm]:", 0.0, 40.0)
SDK = st.slider("Sonnenscheindauer pro Tag [H]:", 0.0, 20.0, 6.0)
SHK_TAG = st.slider("Schneehöhe pro Tag:", 0.0, 2.0, 0.0)
NM = st.slider("Tagesmittel des Bedeckungsgrades:", 0.0, 8.0, 5.6)
TMK = st.slider("Tagesmittel der Temperatur [°C]:", 0.0, 50.0, 12.5)
TXK = st.slider("Tagesmaximum der Temperatur in 2m Höhe [°C]:", 0.0, 50.0, 18.5)
TNK = st.slider("Tagesminimum der Temperatur in 2m Höhe [°C]:", 0.0, 50.0, 7.7)

if st.button("Execute prediction"):
    values = [[RSK, SDK, SHK_TAG, NM, TMK, TXK, TNK]]
    pred_df = pd.DataFrame([[RSK, SDK, SHK_TAG, NM, TMK, TXK, TNK]], 
                           columns = ["RSK", "SDK", "SHK_TAG", "NM", "TMK", "TXK", "TNK"])
    st.caption("The prediction for the data you provided:")
    st.caption("%1.1f" %prediciton(pred_df)[0] + " kWh")
