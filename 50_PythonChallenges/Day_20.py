# Day 20

## Capitalize First Letter


'''
Write a function called capitalize. This function takes a string as an argument and capitalizes the first letter of each word. 
For example, ‘i like learning’ becomes ‘I Like Learning’.
'''

def capitalize(string):
    string_lits = string.split(' ')
    capitalized_string = ""
    for i, word in enumerate(string_lits):
        capitalized_string += word.capitalize()
        if i != len(string_lits) - 1:
            capitalized_string += " "
    return capitalized_string

print(capitalize("i like learning"))