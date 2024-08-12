# Day 28

## Return Indexes

'''
Write a function called index_position. This function takes a string as a parameter and returns the positions or indexes of all lower letters in the string. 
For example 'LovE' should return [1, 2]
'''

def index_position(string):
    indexes = []
    for i, let in enumerate(string):
        if let != let.upper() or let.islower():
            indexes.append(i)
    return indexes

print(index_position('LovE'))
