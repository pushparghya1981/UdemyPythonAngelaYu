
# loop

# Imports
import random

fruits_list = ["apple", "peach", "orange"]
for item in fruits_list:
    print(f"Fruit item :{item}")

for n in range(0, len(fruits_list)):
    print(f"Fruit at [{n}]:{fruits_list[n]}")

# ****************************************************

# Exercise : Get average height of students
# input from user (separated by space)

print("****** Get Average height of students from a list ******")
heights_str = input("Input a list of students heights (separated by space). Ex:123 134\n")

# get the height in a list by split
height_list = heights_str.split(" ")
# get the height list size
height_list_size = len(height_list)

# get the total height of students from the list
total_height = 0.00
for height in height_list:
    total_height = total_height + float(height)

# Get average
average_height = total_height / height_list_size
average_height = "{:.2f}".format(average_height)

print(f"Total Height :{total_height}")
print(f"Students :{height_list_size}")
print(f"Average :{average_height}")

# ****************************************************

# Exercise : Get average height of students (V2)
# input from user (separated by space)

print("****** Get Average height of students from a list(V2) ******")
heights_str = input("Input a list of students heights (separated by space). Ex:123 134\n")

# get the height in a list by split
height_list = heights_str.split(" ")
# get the height list size
height_list_size = len(height_list)

# create a list of heights in floats
height_list_float = []
for n in range(0, height_list_size - 1):
    height_list_float.insert(n, float(height_list[n]))
print(f"Height List :{height_list_float}")

# get the total height of students from the list
total_height = sum(height_list_float)

# Get average
average_height = total_height / height_list_size
average_height = "{:.2f}".format(average_height)

print(f"Total Height :{total_height}")
print(f"Students :{height_list_size}")
print(f"Average :{average_height}")

# ****************************************************

# Exercise : To get min, max value within a list
# input from user (separated by space)

print("****** Get min, max value within a list ******")
scores_str = input("Input a list of students scores (separated by space). Ex:123 134\n")
# split the user input by 'comma'
scores_list = (scores_str.split(" "))
# create a list of integers from above list
scores_list_int = []
for n in range(0, len(scores_list)):
    scores_list_int.insert(n, int(scores_list[n]))
print(f"Score List :{scores_list_int}")

# derive the max value in the list
max_num = 0
for n in range(0, len(scores_list_int)):
    current_num = scores_list_int[n]
    if current_num > max_num:
        max_num = current_num
print(f"Max number :{max_num}")

# derive the min value in the list
min_num = scores_list_int[0]
for n in range(1, len(scores_list_int)):
    current_num = scores_list_int[n]
    if current_num < min_num:
        min_num = current_num
print(f"Min number :{min_num}")

# ****************************************************

# Exercise : FizzBuzz
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(f"{number}")

# ****************************************************

# Exercise : Random password generator(V1)

print("*** Welcome to Random Password generator(V1) ***")
letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols_list = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# ask user inputs
how_many_letters = input(f"How many letters do you like in your password?\n")
how_many_numbers = input(f"How many numbers do you like in your password?\n")
how_many_symbols = input(f"How many symbols do you like in your password?\n")

# We create password - with letters, symbols, numbers (sequence)
password = ""

# getting random letters from the list
for letter in range(1, int(how_many_letters)+1):
    password += random.choice(letters_list)

# getting random symbols from the list
for symbol in range(1, int(how_many_symbols)+1):
    password += random.choice(symbols_list)

# getting random numbers from the list
for number in range(1, int(how_many_numbers)+1):
    password += random.choice(numbers_list)

print(f"Your password :{password}")

# ****************************************************

# Exercise : Random password generator(V2)

print("*** Welcome to Random Password generator(V2) ***")
letters_list2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers_list2 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols_list2 = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# ask user inputs
how_many_letters2 = input(f"How many letters do you like in your password?\n")
how_many_numbers2 = input(f"How many numbers do you like in your password?\n")
how_many_symbols2 = input(f"How many symbols do you like in your password?\n")

# We create password - with letters, symbols, numbers (in random sequence)
final_password = ""
temp_password_list = []

# getting random letters from the list
for letter2 in range(1, int(how_many_letters2) + 1):
    temp_password_list.append(random.choice(letters_list2))

# getting random symbols from the list
for symbol2 in range(1, int(how_many_symbols2) + 1):
    temp_password_list.append(random.choice(symbols_list2))

# getting random numbers from the list
for number2 in range(1, int(how_many_numbers2) + 1):
    temp_password_list.append(random.choice(numbers_list2))

# print(temp_password_list)

# shuffle the password list of items
random.shuffle(temp_password_list)

# generate the final password
for item in temp_password_list:
    final_password += item

print(f"Your password :{final_password}")

# ****************************************************
