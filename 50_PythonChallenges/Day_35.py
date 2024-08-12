# Day 35

## Pangram

'''
Write a function called check_pangram that takes a string and checks ifi it is a pangram. A pangram is a sentece that contains all the letters of the alphabet. 
If it is a pangram, the function should return True, otherwise, return False. 
The following sentence is a pangram so it should return True:
'the quick brown fox jumps over a lazy dog'
'''

def check_pangram(string):
    set_pangram = {let.lower() for let in string if let.isalpha and let != " "}
    #If there are all the letters of the alphabet, the length of the set should be 26.
    return len(set_pangram) == 26

string = 'the quick brown fox jumps over a lazy dog'
print(check_pangram(string))