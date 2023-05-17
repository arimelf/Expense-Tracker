import sys
sys.path.append("/Users/curtiswu/Documents/GitHub/Expense-Tracker")
from utils import *
from datetime import date

if __name__ == "__main__":

    print("Welcome to the expense tracker\n")

    df = pd.read_pickle("Expense-Tracker/data/expenses")
    my_dict = {"1":"Groceries","2":"Delivery/Pick-Up","3":"Eat-Out","4":"Other Purchases"}

    while(True):
        print("Please choose one of the following options:\n")
        option = input("1. View expenses data \n2. Add an expense\n3. Delete one of the expense data\n4. Exit\n")
        if option == "1":
            option_1_2 = input("Please choose on of the following:\n1. View expenses data for the month\n2. View expenses data for the year\n3. Exit\n")
            if option_1_2 == "1":
                view_data_month(df)
            elif option_1_2 == "2":
                view_data_year(df)
            elif option_1_2 == "3":
                break

        elif option == "2":
            option_2_1 = input("Please enter the date:\n1. Today\n2. Enter a date\n")
            if option_2_1 == "1":
                print(f"You have entered the date: {date.today()}")
                my_date = date.today()
            else:
                my_date = input("Please enter the date: ")

            my_amount = float(input("Please enter the amount: "))

            option_2_3 = input("Please Choose one of the following categories the amount:\n1. Groceries\n2. Delivery/Pick-Up\n3. Eat-Out\n4. Other Purchases\n")
            my_cat = my_dict[option_2_3]
            add_expense(df,[my_date,my_amount,my_cat])
            print(f"Expense successfully added: {my_date}, {my_amount}, {my_cat}")

            save_object("Expense-Tracker/data/expenses",df)

        elif option == "3":
            my_del = input(f"Please enter the index of the expense that you want to delete:\n{df}\n")
            delete_row(df,int(my_del))
            print(f"Deletion successful, now the expense is \n{df}")
            
            save_object("Expense-Tracker/data/expenses",df)

        elif option == "4":
            break
    
    

        
    