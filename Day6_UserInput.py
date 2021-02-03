# print("Hello "+input("What is your name?"))


# Exercise: output the size of user name provided

username_input = input("What is your name?")
username_length = len(username_input)
print("Length of your name:", username_length)

# Exercise to swap 2 variables values

num1_input = input("Enter number1: ")
num2_input = input("Enter number2: ")
temp = num2_input
num2_input = num1_input
num1_input = temp
print("Number1 :", num1_input)
print("Number2 :", num2_input)

# Exercise to generate band name based on user
print("Welcome to the band name generator")
user_city = input("Enter the city you grew up?\n")
user_pet = input("Enter your pet name?\n")
print("Suggested band name:", user_city+" "+user_pet)
