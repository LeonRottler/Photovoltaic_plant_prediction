# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 13:43:19 2023

@author: leonr
"""

import os 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv(os.path.dirname(os.getcwd()) + "\Data\data.csv").set_index("MESS_DATUM")
data_v2 = pd.read_csv(os.path.dirname(os.getcwd()) + "\Data\data_v2.csv").set_index("MESS_DATUM")
data_v3 = pd.read_csv(os.path.dirname(os.getcwd()) + "\Data\data_v3.csv").set_index("MESS_DATUM")


def plot_hist_all_attributes():
    data.hist()
    plt.savefig(os.path.dirname(os.getcwd()) + "\Data_Vis\plots\hist_all_attributes.svg")
    plt.show()
    

def plot_hist_attributes_V2():
    data_v2.hist()
    plt.savefig(os.path.dirname(os.getcwd()) + "\Data_Vis\plots\hist_attributes_V2.svg")
    plt.show()


def plot_correlation_matrix_v1():
    correlations = data.corr()
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    cax = ax.matshow(correlations, vmin = -1, vmax = 1)
    fig.colorbar(cax)
    ticks = np.arange(0, 17)
    ax.set_xticks(ticks)
    ax.set_yticks(ticks)
    ax.set_xticklabels(data.columns)
    ax.set_yticklabels(data.columns)
    plt.xticks(rotation = 90)
    plt.title("Correlation Matrix of the dataset")
    plt.savefig(os.path.dirname(os.getcwd()) + "\Data_Vis\plots\correlation_matrix.svg", bbox_inches='tight')
    plt.show()


def plot_correlation_matrix_v2():
    correlations_v2 = data_v2.corr()
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    cax = ax.matshow(correlations_v2, vmin = -1, vmax = 1)
    fig.colorbar(cax)
    ticks = np.arange(0, 8)
    ax.set_xticks(ticks)
    ax.set_yticks(ticks)
    ax.set_xticklabels(data_v2.columns)
    ax.set_yticklabels(data_v2.columns)
    plt.xticks(rotation = 90)
    plt.title("Correlation Matrix of the dataset V2")
    plt.savefig(os.path.dirname(os.getcwd()) + "\Data_Vis\plots\correlation_matrix_V2.svg", bbox_inches='tight')
    plt.show()
    
    
def plot_correlation_matrix_v3():
    correlations_v3 = data_v3.corr()
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    cax = ax.matshow(correlations_v3, vmin = -1, vmax = 1)
    fig.colorbar(cax)
    ticks = np.arange(0, 6)
    ax.set_xticks(ticks)
    ax.set_yticks(ticks)
    ax.set_xticklabels(data_v3.columns)
    ax.set_yticklabels(data_v3.columns)
    plt.xticks(rotation = 90)
    plt.title("Correlation Matrix of the dataset V3")
    #plt.savefig(os.path.dirname(os.getcwd()) + "\Data_Vis\plots\correlation_matrix.svg")
    plt.show()


def plot_scatter_matrix():
    pd.plotting.scatter_matrix(data)
    plt.show()


plot_hist_all_attributes()
plot_hist_attributes_V2()
plot_correlation_matrix_v1()
plot_correlation_matrix_v2()
plot_correlation_matrix_v3()
plot_scatter_matrix()