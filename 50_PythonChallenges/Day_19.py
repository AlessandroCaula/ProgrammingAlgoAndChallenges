# Day 19

## Words and Elements

'''
Write two functions. The first function is called count_words which takes a string of words and counts how many words are in the string.

The second function called count_elements takes a string of words and counts how many elements are in the string. Do not count the whitespaces. 
The first function will return the number of words in a string and the second one will return the number of elements (less whitespace). 
If you pass ‘I love learning’, the count_words function should return 3 words and count_elements should return 13 elements.
'''

def count_words(string):
    string_words = string.split(' ')
    return len(string_words)

def count_elements(string):
    element_count = len([el for el in string if el != " "])
    return element_count

string = "I love learning"
print(f"The number of words is {count_words(string)}. The number of elements {count_elements(string)}")