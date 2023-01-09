# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 10:53:28 2023

@author: leonr
"""

import os 
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(os.path.dirname(os.getcwd()) + "\Data\data_v2.csv").set_index("MESS_DATUM")

def plot_temp():
    plt.plot(data["TMK"])
    plt.title("Average temperature per day")
    plt.xlabel("days")
    plt.ylabel("temp in °C")
    plt.grid(axis = "y", linestyle = '--')
    plt.savefig(os.path.dirname(os.getcwd()) + r"\Data_Vis\plots\temperature.svg", bbox_inches='tight')
    plt.show()
    
    
def plot_temp_sunshine_hours():
    fig = plt.figure()
    plt.plot(data["TMK"])
    plt.plot(data["SDK"])
    plt.title("Average temperature and sunshine hours per day")
    plt.xlabel("days")
    plt.ylabel("temp in °C / hours")
    plt.legend(["temperature", "sunshine hours"])
    plt.grid(axis = "y", linestyle = '--')
    plt.savefig(os.path.dirname(os.getcwd()) + r"\Data_Vis\plots\temp_sunshine_hours.svg", bbox_inches='tight')
    fig.show()
    

plot_temp()
plot_temp_sunshine_hours()