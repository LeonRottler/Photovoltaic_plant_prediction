# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 23:54:35 2023

@author: leonr
"""

import pandas as pd
import os

import ETL.Weather_Data_Extraction as weather
import ETL.kWh_Extraction as kWh


def update_data():
    
    print(os.path.dirname(os.getcwd()) + "\Data\kWh_data.txt")
    
    kWh_df = kWh.get_kWh_df((os.path.dirname(os.getcwd()) + "\Data\kWh_data.txt"))

    # historical weather data from https://www.dwd.de/DE/leistungen/klimadatendeutschland/klarchivtagmonat.html for station
    # Lahr/Schwarzwald
    weather_df = weather.get_weather_data(os.path.dirname(os.getcwd()) + "\Data\Weather_data.csv")

    data = pd.merge(kWh_df, weather_df, on = "MESS_DATUM", how = "inner")
    
    
    data.to_csv(os.path.dirname(os.getcwd()) + "\Data\data.csv")
    
    data_v2 = data
    
    # remove unimportant features
    data_v2.drop(["QN_3", "QN_4", "FX", "FM", "RSKF", "VPM", "PM", "UPM", "TGK"], axis = 1, inplace = True)
    
    data_v2.to_csv(os.path.dirname(os.getcwd()) + "\Data\data_v2.csv")


print(update_data())