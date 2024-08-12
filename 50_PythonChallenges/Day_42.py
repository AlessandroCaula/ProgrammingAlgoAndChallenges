# Day 42

## Spelling Checker

'''
Write a function called spelling_checker. This code asks the user to input a word and if a user inputs a wrong spelling it should suggeste the correct spelling by asking the user if they meant to type that word.
If the user says no, it should ask the user to enter the word again. If the user says yes, it should return the correct word.
If the word entered by the user is correctly spelled the function should return the correct word. USe the module texblob.
'''

from textblob import TextBlob 

def spelling_checker():
    while True:
        input_word = input("Enter a word: ")
        # Check if the input word is correct
        if input_word != TextBlob(input_word).correct():
            # Suggesting the correct word to the user
            is_suggestion_correct = input(f"Do you ment {TextBlob(input_word).correct()}? yes/no - ")
            if (is_suggestion_correct == "yes"):
                break
            else:
                print("Try again...")
        elif input_word == TextBlob(input_word).correct():
            break
    return f"Your word is: {TextBlob(input_word).correct()}"

print(spelling_checker())