# Day 40

## Pig Latin

'''
Write a function called translate that takes the following words and translates them into pig Latin.

a = 'i love python'

Here are the rules:
1. If a word starts with a vowel (a, e, i, o, u) add 'yay' at the end. For example 'eat' will become 'eatyay'.
2. If a word starts with anything other than a vowel, move the first letter to the end and add 'ay' to the end. For example 'day' will become 'ayday'

Your code should return:
iyay ovelay ythonpay
'''

def translate(string):
    pig_lating = ""
    string_split = string.split(' ')
    for word in string_split:
        if word[0].lower() in 'aeiou':
            word += "yay"
        else:
            word = word[1:] + word[0]
            word += 'ay'
        pig_lating += word + " "
    return pig_lating[:-1]

string = "i love python"
print(translate(string))