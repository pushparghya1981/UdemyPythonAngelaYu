import random

"""
print("Welcome to Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

# create a list that will have numbers from 1 to 100
number_list = []
for n in range (1, 101):
    number_list.append(n)
# print(f"Number List :{number_list}")

# define game level attempts: easy = 10 & hard = 5
level_attempts = 0
user_choose_level = input("Choose a difficulty: Type 'easy' or 'hard' :")
if user_choose_level.lower() == "easy":
    level_attempts = 10
elif user_choose_level.lower() == "hard":
    level_attempts = 5
else:
    print("Wrong level!")

random_choosen = random.choice(number_list)

is_guessed = False
is_game_over = False
while not (is_guessed or is_game_over):
    for n in range (1, (level_attempts + 2)):
        if n <= level_attempts and is_guessed == False and is_game_over == False:
            print(f"You have {level_attempts - (n - 1)} attempts left to guess the number")
            user_guessed = int(input("Make a guess :"))

            if user_guessed == random_choosen:
                # Game over, correct guess
                print("Correct guess!! You win")
                is_guessed = True
                is_game_over = True
                # exit()
            elif user_guessed < random_choosen:
                # Game continue
                print("Too low")
            elif user_guessed > random_choosen:
                # Game continue
                print("Too high")
            if n < level_attempts and is_guessed == False and is_game_over == False:
                print("Guess again...")
        elif is_guessed == False and is_game_over == False:
            # Game over, no attempts left
            print(f"Attempts over!! You lose. Number was : {random_choosen}")
            is_game_over = True
            # exit()
"""

# Version 2:

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

# returns the game level
def get_game_level():
    game_level = input("Choose a difficulty: Type 'easy' or 'hard' :")
    if game_level.lower() == "easy":
        return EASY_LEVEL_ATTEMPTS
    elif game_level.lower() == "hard":
        return HARD_LEVEL_ATTEMPTS
    else:
        print("Wrong level!")
        return -1


# checks game level
def check_guess(num_guess, num_answer):
    if num_guess > num_answer:
        print("Too high")
    elif num_guess < num_answer:
        print("Too low")
    else:
        print(f"Correct guess : {num_guess}. You win")


print("Welcome to Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

answer = random.randint(1, 100)
attempts = get_game_level()
guess = 0
is_game_over = False

while guess != answer and is_game_over == False:
    if attempts == 0:
        is_game_over = True
        print(f"Attempts over!! You lose. Number was : {answer}")
    else:
        if attempts == -1:
            print("Game Over!")
            is_game_over = True
        else:
            print(f"You have {attempts} attempts left to guess the number")
            guess = int(input("Make a guess :"))
            check_guess(guess, answer)
            attempts = attempts - 1











