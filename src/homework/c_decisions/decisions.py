def get_options_ratio (option, total):
    options_ratio = option /total
    return options_ratio
    
def get_faculty_rating(options_ratio):
    faculty_rating =  ""
    if (options_ratio >= 0.9 and options_ratio <1.0):
        faculty_rating= "Excellent"
    elif (options_ratio >= 0.8 and options_ratio <0.9):
        faculty_rating = "Very Good"
    elif (options_ratio >= 0.7 and options_ratio <0.8):
        faculty_rating = "Good"
    elif (options_ratio >= 0.6 and options_ratio <0.7):
        faculty_rating = "Needs Improvement"
    elif (options_ratio >= 0.0 and options_ratio <0.6):
        faculty_rating = "Unacceptable"
    return faculty_rating
       