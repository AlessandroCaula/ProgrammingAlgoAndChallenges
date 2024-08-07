# Day 4

## Only Floats

'''
Write a function called only_floats, which takes two parameters a and b, and returns 2 if both arguments are floats, returns 1 if only one argument is a float, and returns 0 if neither argument is a float. 
If you pass (12.1, 23) as an argument, you function should return a 1.
'''

def only_floats(a, b):
    count_float = 0
    if a % 1 != 0:
        count_float += 1
    if b % 1 != 0:
        count_float += 1
    return count_float

a = 12.1
b = 23
print(only_floats(a, b))