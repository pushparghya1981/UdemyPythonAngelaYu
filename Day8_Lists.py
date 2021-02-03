
# Lists

# Exercise 1:

import random

print("****** Who will pay the bill? ******")

persons = input("Give me everybody's name, separated by a comma & space.")
persons_split = persons.split(", ")
# print(f"Persons List :{persons_split}")
persons_split_size = len(persons_split)
# print(f"Persons Count :{persons_split_size}")
random_person = random.randint(0, (persons_split_size - 1))
print(f"Bill to be payed by:{persons_split[random_person]}")

# ************************************** #

# Nested List
fruits_list = ["apple", "banana", "orange"]
vegetables_list = ["potato", "onion", "ginger", "spinach"]
fruits_veggies_list = [fruits_list, vegetables_list]

print(fruits_veggies_list)
print(len(fruits_veggies_list))
print(fruits_veggies_list[0], fruits_veggies_list[1])

# ************************************** #

# Exercise 2:

print("****** Welcome to Treasure Map game ******")
row1_list = ["🎁", "🎁", "🎁"]
row2_list = ["🎁", "🎁", "🎁"]
row3_list = ["🎁", "🎁", "🎁"]
treasure_map = [row1_list, row2_list, row3_list]
print(f"{row1_list}\n{row2_list}\n{row3_list}")

# get the input from user
user_input = input("Where do you want to put your treasure? Provide row & column index: (Ex: 12)\n")
# get the row & column index
row = int(user_input[0])
column = int(user_input[1])
# Row & Column inputs are always (-1) given by user
real_row = row-1
real_column = column-1
# Now, mark the treasure position "💖"
treasure_map[real_row][real_column] = "💖"
print("Your treasure placed below:")
print(f"{row1_list}\n{row2_list}\n{row3_list}")

# ************************************** #

# Exercise 3: Rock, Paper, Scissors game

print("****** Welcome to Rock, Paper, Scissors game ******")

# user_choice_list = ["⛰", "📰", "✂"]
choice_list = ["Rock", "Paper", "Scissors"]
# Get User choice
user_choice = input("What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors.\n")
# Print the user's choice to console
user_choice = int(user_choice)

# Check for wrong choice
if not(user_choice == 0 or user_choice == 1 or user_choice == 2):
    print("Wrong choice!")
else:
    if user_choice == 0:
        user_choose = choice_list[0]
        print("You choose :⛰")
    elif user_choice == 1:
        user_choose = choice_list[1]
        print("You choose :📰")
    else:
        user_choose = choice_list[2]
        print("You choose :✂")

    # Computer will choose randomly everytime
    computer_random = random.randint(0, 2)
    computer_choose = choice_list[computer_random]

    # Print the computer's choice to console
    if computer_choose == "Rock":
        print("Computer choose :⛰")
    elif computer_choose == "Paper":
        print("Computer choose :📰")
    else:
        print("Computer choose :✂")

    # Ultimate decision
    if (user_choose == "Rock" and computer_choose == "Scissors") or (user_choose == "Scissors" and computer_choose == "Papers") or (user_choose == "Paper" and computer_choose == "Rock"):
        print("---- You win! ----")
    elif (computer_choose == "Rock" and user_choose == "Scissors") or (computer_choose == "Scissors" and user_choose == "Papers") or (computer_choose == "Paper" and user_choose == "Rock"):
        print(" ---- Computer win! ----")
    else:
        print("---- Draw ----")

# It generates any integer between 1 & 10 (inclusive of 1 & 10)
random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random()
print(random_float)

# Exercise : Heads & Tails

random_side = random.randint(0, 1)
if random_side == 1:
    print("Heads")
else:
    print("Tails")

# ************************************** #
