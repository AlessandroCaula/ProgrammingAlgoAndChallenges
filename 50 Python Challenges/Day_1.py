# Day 1

## Division and Square-root

'''
Write a function called **`divide_or_square`** that takes one argument (a number), and returns the square root of the number if it is divisible by 5, returns its remainder if it is not divisible by 5.   
For example, if you pass 10 as an argument, then your function should return 2.16 as the square root.
'''

from math import sqrt


def divide_or_square(num):
    if num % 5 == 0:
        print(f"The square root of {num} is : {sqrt(num):.2f}")
    else:
        remainder = num % 5
        print(f"The remainders is: {remainder}")

divide_or_square(6)