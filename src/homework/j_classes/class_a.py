#class creates a dice roller
import random

class Die:
    roll_value = "not rolled"

    def roll(self):
        result = random.randint(1,6)
        self.roll_value = result


    def get_rolled_value(self):
        return self.roll_value
        

def display_menu():
    print("Choose a Menu Option: ")
    print("1. Roll Die")
    print("2. Exit")

def run_menu(Die):
    display_menu()
    option = str(input("Select Option 1 or 2: "))
    while(option != "1" and option != "2"):
        print(str(input("invalid selection. Please type 1 or 2: ")))
    menu_option(option, Die)

def menu_option(option, Die):
    if option == "1":
        Die.roll()
        print("You rolled: {} ".format(Die.get_rolled_value()))
        try_again(Die)
    if option == "2":
        while True:
            exit = input("Are you sure you would like to exit? Type yes or no: ")
            if exit == "yes" or exit == "Yes":
                print("\nExiting now. Bye!")
                break
            elif exit == "no" or exit == "No":
                run_menu(Die)
            else:
                print("please Enter yes or no: ")

def try_again(Die):
    while True:
        x = input("would you like to continue?Type yes or no: ")
        if x.casefold() == "no":
            print("Exiting Now! Bye!")
            break
        elif x.casefold() == "yes":
            run_menu(Die)
            break




       
        



        


              