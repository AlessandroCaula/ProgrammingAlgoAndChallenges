# Day 45

## Words and Special Characters

'''
Write a function called analyse_string that returns the number of special characters (#$%&'()*+,-./:;<=>?@[\]^_`{|}~), words, and total characters (all letters and special characters minus whitespaces) in a string.
Return everything in a dictionary format:
{“special character”: “number”, “words”: “number”, “total characters”: “number”} 

Use the string below as an argument: 

“Python has a string format operator %. This functions analogously to  
printf format strings in C, e.g. "spam=%s eggs=%d" % ("blah", 2) 
evaluates to "spam=blah eggs=2"
Source Wikipedia
'''

import string 

def analyse_string(text):
    dict_count = {"special character": 0, "words": 0, "total character": 0}
    for word in text.split(" "):
        # Increase word count.
        dict_count["words"] += 1   
        for ch in word:    
            if ch in string.punctuation:
                dict_count["special character"] += 1
            dict_count["total character"] += 1
    return dict_count

text = 'Python has a string format operator %. This functions analogously to printf format strings in C, e.g. "spam=%s eggs=%d" % ("blah", 2) evaluates to "spam=blah eggs=2'

print(analyse_string(text))