# Day 11

## Are They Equal?

'''
Write a function called equal_strings. The function takes two strings as arguments and compares them. 
If the strings are equal (if they have the same characters and have equal length), it should return True, if they are not, it should return False. 
For example, ‘love’ and ‘evol’ should return True.
'''

def equal_strings(a, b):
    are_equal = False
    set_a = {el for el in a}
    set_b = {el for el in b}
    if len(a) == len(b) and set_a == set_b:
        are_equal = True
    return are_equal


print(equal_strings('love', 'evol'))