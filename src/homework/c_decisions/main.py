import decisions
#prompt user for information and use the input to get a faculty rating

option = int(input("Enter the numerical grade"))

total = int(input("Enter total possible grade"))
result=decisions.get_options_ratio(option, total)

print ("The Faculty Rating is " + decisions.get_faculty_rating(result))
