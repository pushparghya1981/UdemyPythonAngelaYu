from game_data import data
import random

# Generate a random account from the game data
account_a = {}
account_b = {}
win_count = 0
question_list = []


def generate_random_account():
    """generates a random number & creates account disctionary"""
    # 1st time, random generate between (0, 49)
    # If account_a = 49, then account_b = 0, else account_b = account_a + 1
    if len(question_list) == 0:
        account_a_index = random.randint(0, len(data) - 1)
        if account_a_index == 49:
            account_b_index = 0
        else:
            account_b_index = account_a_index + 1
        global account_a
        global account_b
        account_a = data[account_a_index]
        account_b = data[account_b_index]

        # 1st time, we append 2 questions in list
        question_list.append(account_a)
        question_list.append(account_b)
    # Rest iteration, we want the earlier acount_b question to be account_a
    elif len(question_list) >= 1:
        account_a = question_list[0]
        account_b = data[random.randint(0, len(data) - 1)]
        # if the random generated account is same as above, then we try once more
        if account_b == account_a:
            account_b = data[random.randint(0, len(data) - 1)]
        question_list.append(account_b)


def print_account_data(account):
    """It takes account dictionary & formats name, description, country, followers"""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"[Name :{account_name}] - [Description :{account_description}] - [Country :{account_country}]"


def check_answer(guess, account_a_follower, account_b_follower):
    """It takes guess, 2 account followers & returns True/False based on followers count"""
    if user_input == "a":
        if account_a_follower > account_b_follower:
            return True
        else:
            return False
    else:
        if account_b_follower > account_a_follower:
            return True
        else:
            return False


game_to_continue = True
while game_to_continue:
    generate_random_account()

    print(f"Compare A : {print_account_data(account_a)}")
    print(f"Compare B : {print_account_data(account_b)}")

    # Ask user for a guess
    user_input = input("Who has more followers? Type 'A' or 'B':")
    user_input = user_input.lower()
    is_guess_correct = check_answer(user_input, account_a["follower_count"], account_b["follower_count"])

    # if the guess is correct & keep on incrementing win count by 1
    if is_guess_correct:
        win_count = win_count + 1
        # to make account_b to account_a, we need to pop out 1st element in "question_list"
        question_list.pop(0)
        print(f"Congrats! Current score :[{win_count}]")
    # if the guess is not correct, then we quit the game by displaying the final win count
    else:
        print(f"Game over! Final score :[{win_count}]")
        game_to_continue = False
        question_list.clear()



