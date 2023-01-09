# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 23:54:35 2023

@author: leonr
"""

import pandas as pd
from datetime import *


def remove_whitespaces(string:str):
    return string.replace(" ", "")


def convert_date(str_date:str):
    cus_lens = [4, 2, 2]
    stritr = iter(str_date)
    res = ["".join(next(stritr) for idx in range(size)) for size in cus_lens]
    date_Obj = date(int(res[0]), int(res[1]), int(res[2]))
    return date_Obj


def get_weather_data(path:str):
    weather_data = pd.read_csv(path, sep = ";")

    keys = []

    for key in weather_data.keys():
        keys.append(remove_whitespaces(key))

    weather_data.columns = keys
    weather_data.drop(["STATIONS_ID", "eor"], axis = "columns", inplace = True)

    for key, value in weather_data["MESS_DATUM"].items():
        weather_data["MESS_DATUM"] = weather_data["MESS_DATUM"].replace({value: convert_date(str(value))})

    return weather_data.set_index("MESS_DATUM")

#print(get_weather_data("C:/Users/leonr/Desktop/produkt_klima_tag_20210628_20221229_02812.csv"))