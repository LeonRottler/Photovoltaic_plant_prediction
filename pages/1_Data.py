# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 14:26:09 2023

@author: leonr
"""

import streamlit as st
import pandas as pd 

data = pd.read_csv("C:/Users/leonr/Documents/Git/Photovoltaic_plant_prediction/Data/data.csv").set_index("MESS_DATUM")

st.header("Overview of the kWh output per day in the last year")

st.line_chart(data["kWh"])