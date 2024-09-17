#! python


# Example function that takes two parameters and capitalizes the first letters in each
def format_name(f_name, l_name):
    
    # function can have multiple return statements...
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs..."
    
    # Capitalize the first letter of the params
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return f"{formated_f_name} {formated_l_name}"


print(format_name(input("What is your first name? "), input("What is your last name? ")))
