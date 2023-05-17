from exception import CustomException
import os
import sys
import dill
import pandas as pd
from logger import logging
import matplotlib.pyplot as plt
import numpy as np

def save_object(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok = True)

        logging.info("Saving object")

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e,sys)

def add_expense(df, expense_info):
    df.loc[len(df)] = expense_info


    

def view_data_month(df):
    #print("Total expenses for the month is :")
    sum_gro = 0; sum_dp = 0; sum_to = 0; sum_oth = 0
    for i in range(len(df.index)):
        if df.iat[i,2] == "Groceries":
            sum_gro += df.iat[i,1]
        elif df.iat[i,2] == "Delivery/Pick-Up":
            sum_dp += df.iat[i,1]
        elif df.iat[i,2] == "Eat-Out":
            sum_to += df.iat[i,1]
        elif df.iat[i,2] == "Other Purchases":
            sum_oth += df.iat[i,1]
    arr = np.array([sum_gro,sum_dp,sum_to,sum_oth])
    mylabels = ["Groceries", "Delivery/Take-Out", "Eat-Out", "Other Purchases"]
    plt.pie(arr, labels = mylabels)
    plt.show()