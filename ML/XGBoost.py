# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 23:54:35 2023

@author: leonr
"""

import os
import numpy as np
import pandas as pd
import xgboost as xgb
import pickle
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error as MSE
from sklearn.metrics import mean_absolute_error as MAE


data = pd.read_csv(os.path.dirname(os.getcwd()) + "\Data\data_v2.csv").set_index("MESS_DATUM")

data.reset_index(drop = True, inplace = True)
X, y = data.drop(["kWh"], axis = "columns"), data["kWh"]

train_X, test_X, train_y, test_y = train_test_split(X, y, test_size = 0.2, random_state = 42)

#model = xgb.XGBRegressor(seed = 42)
model = xgb.XGBRegressor(n_estimators = 70, colsample_bytree = 0.9, eta = 0.1, 
                         subsample = 0.45, seed = 42)

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

pickle.dump(model, open(os.path.dirname(os.getcwd()) + "/ML/xgb_model.pkl", "wb"))


def plot_pred_y_test_chart():
    x = np.arange(0, len(pred))
    
    fig = plt.figure()
    plt.plot(x, pred)
    plt.plot(x, test_y, ls = "--")
    plt.title("XGBoost Regressor")
    plt.ylabel("kWh")
    plt.legend(["prediction", "real values"])
    plt.grid(axis = "y", linestyle = '--')
    #plt.savefig(os.path.dirname(os.getcwd()) + "/Data_Vis/plots/xgboost_regressor_with_hyp.svg")
    fig.show()


def plot_feature_importance():
    f_importance = model.get_booster().get_score(importance_type='gain')
    
    print(f_importance)
    
    importance_df = pd.DataFrame.from_dict(data=f_importance, orient='index')
    
    importance_df.plot.bar()
    

#plot_pred_y_test_chart()
#plot_feature_importance()