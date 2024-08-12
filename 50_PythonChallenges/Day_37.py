# Day 37

## Count the Vowels

'''
Create a function called count_the_vowels. The function takes one argument, a string, and returns the number of vowels (vocali) in the string. 
For example 'hello' should return 2 vowels. If a vowel appears in a string more than once it should be counted as one. 
For example, 'saas' should return 1 vowel. Your code should count lowercase and uppercase vowels.
'''

def count_the_vowels(string):
    dict_vowel_count = {}
    for let in string:
        if let.lower() in 'aeiou':
            if let.lower() not in dict_vowel_count.keys():
                dict_vowel_count[let.lower()] = 1
            else:
                dict_vowel_count[let.lower()] += 1
    return len(dict_vowel_count)

string = 'helloO'
print(count_the_vowels(string))
