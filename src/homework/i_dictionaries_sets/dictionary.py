#This code will return the p-distance between two strings
def get_p_distance(list1, list2):
    p_distance = 0
    if len(list1) != len(list2):
        return "Invalid input. lists must be of equal length"
    else:
        for position in range(len(list1)):
            if list1[position] != list2[position]: 
                p_distance += 1
    return p_distance

def get_p_distance_matrix(list1):
    matrix = []
    i = 0
    j = 0
    for i in range (0, (len(list1))):
        l1 = []
        for j in range (0, (len(list1))):
            distance = get_p_distance(list1[i], list1[j])
            fas = distance/10
            l1.append(fas)
        i += 1
        matrix.append(l1)
    return matrix

def display_menu():
    print("1-Get p distance matrix")
    print("2-Exit")

def run_menu():
    display_menu()
    option = str(input("Select option: 1 or 2 "))
    while (option != "1" and option != "2"):
        print(str(input("Invalid Option. Please Enter 1 or 2: ")))
    handle_menu_option(option)

def handle_menu_option(option):
    if option == "1":
        option_1()
    if option == "2":
        option_2()

def option_1():
    dna_list = []
    n = int(input("How many DNA strings: "))
    for i in range(n):
        string = input(f"DNA String {i + 1}: ")
        total_strings = (list(string))
        dna_list.append(total_strings)

    matrix = get_p_distance_matrix(dna_list)
    print(matrix)
    try_again_1()

def option_2():
    while True:
        exit = input("Are you sure you would like to exit? Type yes or no: ")
        if exit == "yes" or exit == "Yes":
            print("\nExiting now. Bye!")
            break
        elif exit == "no" or exit == "No":
            run_menu()
        else:
            print("please Enter yes or no:")


def try_again_1():
    while True:
        x = str(input("Type yes to try again, or no to exit: "))
        if x == "yes" or x == "Yes":
            option_1()
            break
        elif x == "no" or x == "No":
            option_2()
            break
        else:
            print("Please enter yes or no: ")
