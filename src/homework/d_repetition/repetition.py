#for loop that gets factorial for a number parameter

def get_factorial(num):
    product = 1
    if num < 0:
        return "Invalid"
    else:
        for n in range(1,num+1):
            product *= n
        return product

#while loop that returns sum of all odd numbers up to num
def sum_odd_numbers(num):
    sum=0
    count=0
    while count< num:
        count += 1
        if count % 2 == 1:
            sum += count
    return sum
          
def display_menu():
    print("Homework 3 Menu")
    print("1-Factorial")
    print("2-Sum odd numbers")
    print("3-Exit")

def run_menu():
    display_menu()
    option = (input("Enter a menu option: 1, 2, or 3: "))
    run_menu_option(option)
def run_menu_option(option):
    if(option == '1'):
        option_1_selected()
    if (option =='2'):
        option_2_selected()
    if (option == '3'):
        option_3_selected()
def option_1_selected():
    num=0
    while num <1 or num > 10:
        while True:
            try:
                num = int(input("Enter number 1-10: "))
                break
            except ValueError:
                print("not a number, input number 1-10: ")
    factorial = get_factorial(num)
    print("The factorial of ", num, "is equal to: ", factorial)
    exit_menu()

def option_2_selected():
    num = 0
    while num < 1 or num > 100:
        while True:
            try:
                num = int(input("Enter a number 1-100: "))
                break
            except ValueError:
                print("Not a number, input a number 1-100: ")
    sum=sum_odd_numbers(num)
    print("The sum of odd numbers for", num, "is:", sum)
    exit_menu()
def option_3_selected():
    while True:
        exit= input ("Enter y if you want to exit, enter n if you want to continue: ")
        if exit == "y" or exit == "Y":
            print("Exiting program. Goodbye!")
            break
        elif exit == "n" or exit == "N":
            run_menu()
            break
        else:
            print("Enter y or n")

def exit_menu():
    while True:
        continued = input("Do you want to continue, y or n")
        if continued == "Y" or continued == "y":
            run_menu()
            break
        if continued == "N" or continued == "n":
            print("Exiting Program. Goodbye!")
            break
        else:
            print("Enter y or n")


    