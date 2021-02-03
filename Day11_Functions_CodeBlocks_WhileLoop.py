# Functions, Code blocks, While loop

# Imports
import math
import random
from replit import clear


# Function without any parameters
def my_function():
    print("Hello")
    print("Bye")


my_function()

# *********************

# while loop

is_found = False
num = 0
while is_found is False and num <= 5:
    print(num)
    num = num + 1

# ******************************************

"""
# Exercise: Hangman Game

print("****** Welcome to HANGMAN game ******")

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# randomly choose a word
words_list = ["sankha", "suparna", "momo", "biriyani", "aparna", "akshay", "madhuri"]

random_word_to_guess = random.choice(words_list)
# print(f"Random word :{random_word_to_guess}")

# declare a list with "_"
guess_list = []
for item1 in random_word_to_guess:
    guess_list.append("_")


# function to display
def word_guessed():
    word_to_guess = ""
    for item2 in guess_list:
        word_to_guess += item2
    print(f"Word guessed :{word_to_guess}")


wrong_guess_index = 0
guess_word = ""

# we will give 6 chances
while wrong_guess_index <= len(HANGMANPICS) - 1:
    # ask user to guess
    guess = input("Guess a letter :").lower()
    clear()

    # display the correct guess letter in the word to user
    for index in range(0, len(random_word_to_guess)):
        if guess == random_word_to_guess[index]:
            guess_list[index] = guess
    word_guessed()

    # display warning letters if guess is not correct
    if guess not in random_word_to_guess:
        print(f"You guessed - {guess}, that's not in the word. You lose a life!")
        print(HANGMANPICS[wrong_guess_index])

        if wrong_guess_index == 6:
            print(f"Game Over! You're hanged!!!, word to guess : {random_word_to_guess}")
        wrong_guess_index += 1
    # win message to user only when there is no "_" in "guess_list"
    else:
        if "_" not in guess_list:
            print("Game Over! You WON!")
            wrong_guess_index = 7

# **************************

"""

# function with parameters


def greet_by_name(name):
    print(f"Hello {name}")


greet_by_name("Sankha")


def greet_with(name, location):
    print(f"Hello {name}")
    print(f"Tell me something about {location}")


greet_with("Rumi", "Paikpara")

# Function with keyword argument


def greet_with(name, location):
    print(f"Hello {name}")
    print(f"Tell me something about {location}")


greet_with(location="Palpara", name="Sankha")

# ************* Exercise : Paint wall calculation ************* #

"""
wall_height = int(input("What's the height of the wall? :"))
wall_width = int(input("What's the width of the wall? :"))
cover = 5


def paint_calc(height, width, coverage):
    wall_area = height * width
    no_of_cans_needed = wall_area / coverage
    # no_of_cans_needed = round(no_of_cans_needed)
    no_of_cans_needed = math.ceil(no_of_cans_needed)
    print(f"You will need {no_of_cans_needed} cans of paint")


paint_calc(wall_height, wall_width, cover)

# ************* Exercise: Evaluate prime number ************* #

input_num = int(input(f"Input a number :\n"))

# a prime number is only divisible by 1 & by itself.


def prime_checker(number_to_check):
    # by default 1 & 2 is considered as prime number
    if number_to_check == 1 or number_to_check == 2:
        print("It's a prime number.")
    else:
        is_divisible = False
        for n in range(2, number_to_check):
            if number_to_check % n == 0:
                is_divisible = True
        if not is_divisible:
            print("It's a prime number.")
        else:
            print("It's not a prime number.")


prime_checker(input_num)

"""
# ************* Exercise: Encode & decode ************* #

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encode(plain_text, shift_amount):
    # we start with default list
    # loop through each letter & find it's index & then add the shift_amount to it's index
    encoded_text = ""
    for letter in plain_text:
        # if the text contains other than letters, we keep that intact
        if letter in alphabet:
            # we fetch the current position
            position = alphabet.index(letter)
            # if the current position + shift < 25, then we consider the default list
            new_position = position + shift_amount
            if new_position <= 25:
                encoded_text += alphabet[new_position]
            # if the current position + shift > 25, then we get deduct (new position - 26)
            elif new_position > 25:
                encoded_text += alphabet[new_position - len(alphabet)]
        else:
            encoded_text += letter
    print(f"The encoded text :{encoded_text}")


def decode(plain_text, shift_amount):
    # we start with reversed list
    # loop through each letter & find it's index & then add the shift_amount to it's index
    decoded_text = ""
    reversed_alphabet = list(reversed(alphabet))
    for letter in plain_text:
        # if the text contains other than letters, we keep that intact
        if letter in reversed_alphabet:
            position = reversed_alphabet.index(letter)
            new_position = position + shift_amount
            # if the current position + shift < 25, then we consider the default reversed list
            if new_position <= 25:
                decoded_text += reversed_alphabet[new_position]
            # if the current position + shift > 25, then we get deduct (new position - 26)
            elif new_position > 25:
                decoded_text += reversed_alphabet[new_position - len(alphabet)]
        else:
            decoded_text += letter
    print(f"The decoded text :{decoded_text}")


# check for correct action & display proper message
should_continue = True
while should_continue:
    action = input("What you want to do? encode or decode?\n").lower()
    if not (action == "decode" or action == "encode"):
        print("Wrong Action!")
        should_continue = False
    else:
        cipher_text = input(f"Enter the cipher text :\n")
        shift = int(input(f"Enter the shift :\n"))

        if action == "encode":
            encode(cipher_text, shift)
        elif action == "decode":
            decode(cipher_text, shift)

        yes_no = input("Do you want to continue? yes or no? :").lower()
        if yes_no == "no":
            should_continue = False
            print("Good-Bye!")

