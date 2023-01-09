# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 00:15:07 2023

@author: leonr
"""

import os 
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(os.path.dirname(os.getcwd()) + "\Data\data.csv").set_index("MESS_DATUM")


def plot_kWh():
    plt.plot(data["kWh"])
    plt.title("kWh per day")
    plt.xlabel("days")
    plt.ylabel("kWh")
    plt.grid(axis = "y", linestyle = '--')
    plt.savefig(os.path.dirname(os.getcwd()) + "\Data_Vis\plots\kWh.svg", bbox_inches='tight')
    plt.show()
    
    
def plot_kWh_hist():
    plt.hist(data["kWh"])
    plt.title("Histogram kWh")
    plt.ylabel("kWh")
    plt.savefig(os.path.dirname(os.getcwd()) + "\Data_Vis\plots\kWh_hist.svg", bbox_inches='tight')
    plt.show()
    

def plot_sunshine_hours():
    plt.plot(data["SDK"])
    plt.title("Sunshine in hours per day")
    plt.xlabel("days")
    plt.ylabel("Sunshine per day [hours]")
    plt.grid(axis = "y", linestyle = '--')
    plt.show()
    

def plot_kWh_and_temp():
    fig1 = plt.figure()
    plt.plot(data.index, data["kWh"])
    plt.plot(data.index, data["TMK"])
    plt.title("kWh per day")
    plt.xlabel("days")
    plt.ylabel("kWh / in °C")
    plt.legend(["kWh", "temp"])
    plt.grid(axis = "y", linestyle = '--')
    plt.savefig(os.path.dirname(os.getcwd()) + "\Data_Vis\plots\kWh_temp.svg", bbox_inches='tight')
    fig1.show()
    

def plot_kWh_and_sunshine_hours():
    fig2 = plt.figure()
    plt.scatter(data.index, data["kWh"], s = data["SDK"]*2)
    plt.title("kWh per day (size depending on sunshine hours)")
    plt.xlabel("days")
    plt.ylabel("kWh")
    plt.grid(axis = "y", linestyle = '--')
    plt.savefig(os.path.dirname(os.getcwd()) + "\Data_Vis\plots\kWh_sunshine_houra.svg", bbox_inches='tight')
    fig2.show()
    

def plot_kWh_and_temp_sunshine_hours():
    fig3 = plt.figure()
    plt.plot(data["kWh"])
    plt.plot(data["TMK"])
    plt.plot(data["SDK"])
    plt.title("kWh / average temperature / sunshine hours per day")
    plt.xlabel("days")
    plt.ylabel("kWh / temp in °C / hours")
    plt.legend(["kWh", "temp", "sunshine hours"])
    plt.grid(axis = "y", linestyle = '--')
    plt.savefig(os.path.dirname(os.getcwd()) + "\Data_Vis\plots\kWh_temp_sunshine.svg", bbox_inches='tight')
    fig3.show()
    

#plot_kWh()
#plot_kWh_hist()
#plot_sunshine_hours()
plot_kWh_and_temp()
#plot_kWh_and_sunshine_hours()
plot_kWh_and_temp_sunshine_hours()