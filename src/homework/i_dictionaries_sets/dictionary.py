# showcases adding and removing from dictionaries

inventory_dictionary = {}

def add_inventory(widget_name, quantity, inventory_dictionary):
    if widget_name in inventory_dictionary:
        inventory_dictionary[widget_name] = inventory_dictionary[widget_name] + quantity
    else:
        inventory_dictionary[widget_name] = quantity

def remove_inventory_widget(widget_name, inventory_dictionary):
    if widget_name in inventory_dictionary:
        del inventory_dictionary[widget_name]
        return "Record Deleted"
    else:
        return "Item not Found"
    
def display_menu():
    print("inventory Menu:")
    print("1- Add or Update Item")
    print("2- Delete Item")
    print("3- Exit")

def run_menu():
    display_menu()
    option = str(input("Select an option: 1, 2, or 3: "))
    while (option != "1" and option != "2" and option != "3"):
        print(str(input("Invalid Option. Please Enter 1, 2, or 3: ")))
    handle_menu_option(option)

def handle_menu_option(option):
    if option == "1":
        option_1()
    if option == "2":
        option_2()
    if option == "3":
        option_3()

def option_1():
    num = int(input("How many widgets would you like to add or update?"))

    for i in range(num):
        widget_name = str(input("enter a key for your item: "))
        quantity = int(input("Enter a quantity for your item: "))
        add_inventory(widget_name, quantity, inventory_dictionary)
    print(inventory_dictionary)
    try_again_1()

def option_2():
    widget_name = str(input("Please enter the item you'd like to delete: "))
    result = remove_inventory_widget(widget_name, inventory_dictionary)
    print(result)
    print(inventory_dictionary)
    try_again_1()

def option_3():
    while True:
        exit = input("Are you sure you would like to exit? Type yes or no: ")
        if exit == "yes" or exit == "Yes":
            print("\nExiting now. Bye!")
            break
        elif exit == "no" or exit == "No":
            run_menu()
            break
        else:
            print("please Enter yes or no:")

def try_again_1():
     while True:
        x = str(input("Type menu to return to menu, or end to exit: "))
        if x == "menu" or x == "Menu":
            run_menu()
            break
        elif x == "end" or x == "End":
            option_3()
            break
        else:
            print("Please type menu to continue or end to exit: ")





