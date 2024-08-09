# Day 34

## Guess a Number

'''
Write a function called guess_a_number. The function should ask a user to guess a randomly generated number. If the user guesses a higher number, the code should tell them that the guess is too high, 
if the user guesses low, the code should tell them that their guess is too low. The user should get a maximum of three guesses. When the user guesses right, the code should declare them a winner. 
After three wrong guesses, the code should declare them a loser.
'''

import random

def guess_a_number():
    random_generated_number = random.randint(0, 100)
    i = 0
    while i < 3:
        i += 1
        user_guess = int(input("Guess the number (0-100): "))
        if user_guess == random_generated_number:
            print("You won!")
            return
        if user_guess < random_generated_number:
            print(f"Your guess is too low! Try again, you still have {3 - (i)} guesses")
        elif user_guess > random_generated_number:
            print(f"Your guess is too high! Try again, you still have {3 - (i)} guesses")

    return (f"You lost. The number to guess was {random_generated_number}")

print(guess_a_number())