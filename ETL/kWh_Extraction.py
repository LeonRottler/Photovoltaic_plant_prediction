# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 23:54:35 2023

@author: leonr
"""

import re
import pandas as pd
from datetime import *


def get_date_of_txt_file(path:str):
    file_input = open(path, "r")

    regex_date_of_textfile = "P.97"

    for line in file_input:
        regexObj = re.search(regex_date_of_textfile, line)
        if regexObj is not None:
            return regexObj.string.split("=")[1]


def get_kWh_df(path:str):

    date_txt_file = get_date_of_txt_file(path)
    date_txt_file = date(int(date_txt_file.split(".")[2]), int(date_txt_file.split(".")[1]),
                         int(date_txt_file.split(".")[0]))

    file_input = open(path, "r")

    regex_dates = "\A[0-9][0-9].[0-9]"

    index_list = []
    values = []

    for line in file_input:
        regexObj = re.search(regex_dates, line)
        if regexObj is not None:
            try: #necessary because 29.02 is always in the text file
                line_date = regexObj.string.split()[0]
                line_date = date(date.today().year, int(line_date.split(".")[1]), int(line_date.split(".")[0]))
                if date_txt_file > line_date:
                    index_list.append(line_date)
                else:
                    line_date = regexObj.string.split()[0]
                    line_date = date(date.today().year - 1, int(line_date.split(".")[1]), int(line_date.split(".")[0]))
                    index_list.append(line_date)
                values.append(regexObj.string.split()[1].replace(",", "."))
            except ValueError:
                print("Exception: No leap year -- " + str(line_date))


    df = pd.DataFrame(values, index = index_list, columns = ["kWh"])
    df.index.name = "MESS_DATUM"
    df["kWh"] = df["kWh"].apply(pd.to_numeric)
    return df

#print(get_kWh_df("C:/Users/leonr/Desktop/EJ-Logger.txt"))