from utils import *
import pandas as pd

df = pd.DataFrame(
   {
      "Date": [],
      "Amount": [],
      "Category": []
   }
)

save_object("Expense-Tracker/data/expenses",df)

