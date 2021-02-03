# Functions with Outputs

# Exercise : title case words

# title() always Capitalize the 1st character of the word

"""
def format_name(f_name, l_name):
    formatted_fname = f_name.title()
    formatted_lname = l_name.title()
    return f"{formatted_fname} {formatted_lname}"


formatted_string = format_name("SANKHA", "PusHPARghya")
print(formatted_string)

# exercise : multiple 'return' in a function


def format_name(f_name, l_name):
    if f_name == "" and l_name == "":
        return "You didn't provide valid inputs!"
    formatted_fname = f_name.title()
    formatted_lname = l_name.title()
    return f"{formatted_fname} {formatted_lname}"


formatted_string = format_name("", "")
print(formatted_string)

# Exercise: Return month days according to Leap year or not

user_year = int(input("Enter year :"))
user_month = int(input("Enter month :"))

month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap_year(year):
    # This method checks a year as a Leap or not.
    # Returns "True" if it's a Leap year.
    # Returns "false" if it's not a Leap year
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def get_days_in_month():
    # Returns the days of a month based on the Leap year or not.
    # Also throws "Error message" if user inputs month less than 1 or greater than 12
    if user_month < 1 or user_month > 12:
        return "Invalid input!"
    else:
        if is_leap_year(user_year) and user_month == 2:
            return 29
        else:
            return month_days[user_month - 1]


days = get_days_in_month()
print(days)

# Exercise: Calculator

# Add
def add(n1, n2):
    return n1 + n2

# Substract
def substract(n1, n2):
    return n1 - n2

# Multiple
def multiple(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

# Dictionary for operators
operations = {
    "+": add,
    "-": substract,
    "*": multiple,
    "/": divide
}

num1 = int(input("Input 1st number :"))

should_continue = True
while should_continue:
    # Display the operators
    for operator in operations:
        print(operator)
    operation = input("Choose operation from above :")
    num2 = int(input("Input 2nd number :"))

    # get the function based on operator
    operation_function = operations[operation]
    output = operation_function(num1, num2)
    print(f"{num1} {operation} {num2} = {output}")

    # ask the user for further continue
    choose = input(f"Type 'y' to continue with calculation with {output}, or type 'n' to exit. :")
    if choose == "y":
        num1 = output
    else:
        should_continue = False
"""

# Exercise: Calculator - v2 - Recursive

# Add
def add(n1, n2):
    return n1 + n2

# Substract
def substract(n1, n2):
    return n1 - n2

# Multiple
def multiple(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

# Dictionary for operators
operations = {
    "+": add,
    "-": substract,
    "*": multiple,
    "/": divide
}

def calculator():
    # ask for 1st number
    num1 = float(input("Input 1st number :"))

    should_continue = True
    while should_continue:
        # Display the operators
        for operator in operations:
            print(operator)
        # ask for operator
        operation = input("Choose operation from above :")
        # ask for 2nd number
        num2 = float(input("Input 2nd number :"))

        # get the function based on operator
        operation_function = operations[operation]
        output = operation_function(num1, num2)
        print(f"{num1} {operation} {num2} = {output}")

        # ask the user for further continue
        choose = input(f"Type 'y' to continue with calculation with {output}, or type 'n' to start a new calculation or type 'e' to exit. :")
        if choose == "y":
            num1 = output
        elif choose == "n":
            calculator() # here is the recursive call
        else:
            exit()

calculator()
