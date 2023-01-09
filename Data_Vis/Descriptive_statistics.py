# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 11:24:20 2023

@author: leonr
"""

import os 
import pandas as pd

data = pd.read_csv(os.path.dirname(os.getcwd()) + "\Data\data.csv").set_index("MESS_DATUM")

print("First 10 rows of the data:")
print(data.head(10))

print("------------------------------------")
print("Dimension of the data:")
print(data.shape)

print("------------------------------------")
print("Description of the data:")
print(data.describe())

print("------------------------------------")
print("Description of the data:")
for col in data.columns:
    print(data[col].describe())
    print("----------")

print("------------------------------------")
print("Data types for each attribute:")
print(data.dtypes)

print("------------------------------------")
print("Data skew:")
print(data.skew())

data_v2 = pd.read_csv(os.path.dirname(os.getcwd()) + "\Data\data_v2.csv").set_index("MESS_DATUM")

print("First 10 rows of the data:")
print(data_v2.head(10))

print("------------------------------------")
print("Dimension of the data:")
print(data_v2.shape)

print("------------------------------------")
print("Description of the data:")
print(data_v2.describe())

print("------------------------------------")
print("Description of the data:")
for col in data_v2.columns:
    print(data_v2[col].describe())
    print("----------")

print("------------------------------------")
print("Data types for each attribute:")
print(data_v2.dtypes)

print("------------------------------------")
print("Data skew:")
print(data_v2.skew())