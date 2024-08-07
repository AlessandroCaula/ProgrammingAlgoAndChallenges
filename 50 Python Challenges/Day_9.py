# Day 9 

## Biggest Odd Number

'''
Create a function called biggest_odd that takes a string of numbers and returns the biggest odd number in the list. 
For example, if you pass '23569' as an argument, your function should return 9. Use list comprehension.
'''

def biggest_odd(number):
    max_odd = max([n for n in number if int(n) % 2 != 0])
    return max_odd

print(f"Maximum odd number {biggest_odd('23569')}")