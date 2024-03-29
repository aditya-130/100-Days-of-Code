import random
import os
clear = lambda: os.system("cls")

def play_game(difficulty):
    attempts = 0
    if difficulty == 'easy':
        attempts = 10
    elif difficulty == 'hard':
        attempts = 5
    else:
        print('Wrong difficulty input')
        return
    number_to_guess = random.randint(1, 101)
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number\n")
        user_guess = int(input("Make a guess: "))
        if user_guess > number_to_guess:
            clear()
            print("\nToo high\nGuess again\n")
            attempts -= 1
        elif user_guess < number_to_guess:
            clear()
            print("\nToo low\nGuess again\n")
            attempts -= 1
        else:
            clear()
            print(f"\nYou got it! The answer was {number_to_guess}")
            return
    clear()
    print(f"\nYou've run out of guesses. The number was {number_to_guess}. you lose")

clear()
print("Welcome to the Number Guessing Game\nI'm thinking of a number between 1 and 100\n")
difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
play_game(difficulty = difficulty_level)
