logo = """
 _______               ___.                   _______  .__            __        
 \      \  __ __  _____\_ |__   ___________   \      \ |__| ____     |__|____   
 /   |   \|  |  \/     \| __ \_/ __ \_  __ \  /   |   \|  |/    \    |  \__  \  
/    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/ /    |    \  |   |  \   |  |/ __ \_
\____|__  /____/|__|_|  /___  /\___  >__|    \____|__  /__|___|  /\__|  (____  /
        \/            \/    \/     \/                \/        \/\______|    \/ 
"""

import random

#global variables
EASY_COUNT = 10
HARD_COUNT = 5

print(logo)

def num_checker(comp_num,guess_count):
    guess_num = 0 #local variable
    while guess_count!=0:
        print(f"You have {guess_count} attempts remaining to guess the number.\n")
        guess_num = int(input("Make a guess: "))
        if comp_num == guess_num:
            print(f"You Got It!!The answer is {comp_num} ")
            return
        elif comp_num > guess_num:
            print(f"Too Low.\nGuess Again.")
            guess_count-=1
        else:
            print(f"Too High.\nGuess Again.")
            guess_count-=1
    if comp_num != guess_num:
        print("You've run out of guesses. Refresh the page to run again.")
        return

def game():    
    print("Welcome to the Number Guessing game!!\n")
    print("I'm thinking of a number between 1 and 100.\n")
    # local variables
    rand_num = random.randint(1,100) 
    choice = input("Choose the Difficulty.Type 'easy' or 'hard' : ").lower()
    
    if choice == "easy":
        num_checker(rand_num,EASY_COUNT)
    elif choice == "hard":
        num_checker(rand_num,HARD_COUNT)

game()