# Day 31

## Longest Word

'''
Write a function that has one parameter and takes a list of words as an argument. The function returns the longest word from the list. 
Name the function longest_word. The function should return the longest word and the number of letters in that word. 
For example, if you pass ['Java', 'JavaScript', 'Python'], your function should return  [10, JavaScript] as the longest word. 
'''

def longest_word(words):
    words_sorted = sorted(words, key= lambda x: len(x), reverse=True)
    return [len(words_sorted[0]), words_sorted[0]]

print(longest_word(['Java', 'JavaScript', 'Python']))