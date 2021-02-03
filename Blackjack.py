import random
from replit import clear

list_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_cards():
    """ Returns a random card from a deck """
    return random.choice(list_cards)


def calculate_score(cards_list):
    """ Take a list of cards and return the score calculated from the cards """
    if sum(cards_list) == 21 and len(cards_list) == 2:
        return 0
    if 11 in cards_list and sum(cards_list) > 21:
        cards_list.remove(11)
        cards_list.append(1)
    return sum(cards_list)


def compare(user_result, computer_result):
    """ It compares User & Computer results and declare the winner"""
    if user_result == computer_result:
        return "DRAW"
    elif computer_result == 0:
        return "You lose, opponent has a BlackJack"
    elif user_result == 0:
        return "You won with a BlackJack"
    elif user_result > 21:
        return "You went over, You lose"
    elif computer_result > 21:
        return "Opponent went over, You Win"
    elif user_result > computer_result:
        return "You Win"
    else:
        return "You Lose"


def play_game():
    user_cards_list = []
    computer_cards_list = []
    is_game_over = False

    # Deal the user & computer 2 cards each using deal_cards()
    for i in range(2):
        user_cards_list.append(deal_cards())
        computer_cards_list.append(deal_cards())

    # keep on until the game is over
    while not is_game_over:
        # calculate user & computer score
        user_score = calculate_score(user_cards_list)
        computer_score = calculate_score(computer_cards_list)
        print(f"User Cards : {user_cards_list} and Total : {user_score}")
        print(f"Computer 1st Card : {computer_cards_list[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass:")
            if user_should_deal == "y":
                user_cards_list.append(deal_cards())
            else:
                is_game_over = True

        # Computer plays once the user has played
        while computer_score != 0 and computer_score < 17:
            computer_cards_list.append(deal_cards())
            computer_score = calculate_score(computer_cards_list)

    print(f"Your final hand {user_cards_list}, final score : {user_score}")
    print(f"Computer final hand {computer_cards_list}, final score : {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of BlackJack? Type 'y' or 'n' :") == "y":
    clear()
    play_game()


