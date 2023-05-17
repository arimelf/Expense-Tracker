from utils import *

if __name__ == "__main__":
    print("Welcome to the expense tracker:\nPlease choose one of the following options")
    option = input("1. View expenses data \n2. Add an expense\n 3. Delete one of the expense data\n4.Exit")
    if option == "1":
        option_2 = input("Please choose on of the following:\n1.View expenses data for the month\n2.View expenses data for the year\n3.Exit")
        if option_2 == "1":
            view_data_month()
        elif option_2 == "2":
            view_data_year()
        elif option_2 == "3":
            exit
    