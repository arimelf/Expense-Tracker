from exception import CustomException
import os
import sys
import dill
import pandas as pd
from logger import logging

def save_object(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok = True)

        logging.info("Saving object")

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e,sys)

def add_expense(expense_info):
    current_expense = pd.read_pickle("data/expenses")
    

def view_data_month():
    print("Displaying expenses for the month:")
    # object = pd.read_pickle()
    