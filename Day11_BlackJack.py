logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


import random

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """Calculate the score. Return 0 if Blackjack."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    while sum(cards) > 21 and 11 in cards:
        cards[cards.index(11)] = 1
    return sum(cards)

def compare(user_score, computer_score):
    if user_score > 21:
        return "You went over. You lose "
    if computer_score > 21:
        return "Computer went over. You win "
    if user_score == computer_score:
        return "It's a draw "
    if user_score == 0:
        return "Win with a Blackjack "
    if computer_score == 0:
        return "Lose, opponent has Blackjack "
    if user_score > computer_score:
        return "You win "
    else:
        return "You lose "

def blackjack():
    print(logo)
    choice1 = input("Welcome to Blackjack.\nDo you want to play? Type 'y' or 'n': ")
    if choice1 != 'y':
        return

    user_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]

    game_over = False

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            should_continue = input("Type 'y' to get another card, type 'n' to pass: ")
            if should_continue == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"\nYour final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

    again = input("Do you want to play again? Type 'y' or 'n': ")
    if again == 'y':
        print("\n" * 30)
        blackjack()

blackjack()