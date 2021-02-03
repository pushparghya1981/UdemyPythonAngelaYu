# Data Types - String, Integer, Float, Boolean

# Exercise - User inputs 2 digit number. From that number, we return sum of 2 digits

two_digit_number = input("Enter a 2 digit number:")
first_digit_num = int(two_digit_number[0])
second_digit_num = int(two_digit_number[1])
sum_digits = first_digit_num+second_digit_num
print("Sum of digits is:", sum_digits)

# ************************************* #

# Exercise to calculate BMI

print("****** Welcome to BMI Calculator *******")

user_height = input("Enter your height in meters:")
user_height = float(user_height)

user_weight = input("Enter your weight in Kgs:")
user_weight = float(user_weight)

user_bmi = user_weight/(user_height ** 2)
user_bmi_integer = round(user_bmi, 2)

print("Your BMI :", user_bmi_integer)

# ************************************* #

# Exercise to calculate remaining days, weeks & months left

current_age = input("What's your current age? ")
expected_years_to_live = input("What's your expected years to live? ")

# convert user input to int
current_age_int = int(current_age)
expected_years_to_live_int = int(expected_years_to_live)
years_remaining = expected_years_to_live_int - current_age_int

months_remaining = years_remaining * 12
weeks_remaining = years_remaining * 52
days_remaining = years_remaining * 365

message = f"you have {days_remaining} days, {weeks_remaining} weeks and {months_remaining} months left"
print(message)

# ************************************* #

# Exercise : Tip Calculator
print("******* Welcome to Tip Calculator *******")

total_bill = float(input("What was the total bill?"))
tip_percentage = int(input("What percentage tip would you like to give ? 10, 12 or 15?"))
people_to_split = int(input("How many people to split the bill?"))

each_person_pay = (((total_bill*tip_percentage)/100)+total_bill)/people_to_split
each_person_pay = round(each_person_pay, 2)
# This will always show 2 decimal places
each_person_pay = "{:.2f}".format(each_person_pay)

print(f"Each person should pay: {each_person_pay}")

# ************************************* #

