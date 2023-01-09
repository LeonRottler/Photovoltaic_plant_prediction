# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 11:49:11 2023

@author: leonr
"""

import os
import numpy as np
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error as MSE
from sklearn.metrics import mean_absolute_error as MAE


data = pd.read_csv(os.path.dirname(os.getcwd()) + "\Data\data_v2.csv").set_index("MESS_DATUM")

data.reset_index(drop = True, inplace = True)
X, y = data.drop(["kWh"], axis = "columns"), data["kWh"]

train_X, test_X, train_y, test_y = train_test_split(X, y, test_size = 0.2, random_state = 42)

model = LinearRegression()

model.fit(train_X, train_y)

pred = model.predict(test_X)

mae = MAE(test_y, pred)

print("MAE : % f" %(mae))

mse = MSE(test_y, pred)

print("MSE : % f" %(mse))

rmse = np.sqrt(MSE(test_y, pred))
print("RMSE : % f" %(rmse))

baseline = np.tile(data["kWh"].mean(), len(pred))

rmse = np.sqrt(MSE(test_y, baseline))
print("Baseline RMSE : % f" %(rmse))

pickle.dump(model, open(os.path.dirname(os.getcwd()) + "/ML/linear_reg_model.pkl", "wb"))


def plot_pred_y_test_chart():
    x = np.arange(0, len(pred))
    
    fig = plt.figure()
    plt.plot(x, pred)
    plt.plot(x, test_y, ls = "--")
    plt.title("Linear Regression model")
    plt.ylabel("kWh")
    plt.legend(["prediction", "real values"])
    plt.grid(axis = "y", linestyle = '--')
    #plt.savefig(os.path.dirname(os.getcwd()) + "\Data_Vis\plots\linear_regression.svg")
    fig.show()
    

plot_pred_y_test_chart()