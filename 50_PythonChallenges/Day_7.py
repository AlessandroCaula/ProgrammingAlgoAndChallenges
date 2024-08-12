# Day 7

## A String Range

'''
Write a function called string_range that takes a single nnumber and returns a string of its range. The string characters should be separated by dots(.)
For example, if you pass 6 as an argument, your function should return '0.1.2.3.4.5'.
'''

def string_range(num):
    range_string = ''
    for i in range(num):
        range_string += str(i) + '.'
    return range_string[:-1]

print(string_range(6))