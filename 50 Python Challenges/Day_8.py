# Day 8 

## Odd and Even 

'''
Write a function called odd_even that has one parameter and takes a list of numbers as an argument. The function returns the difference between the largest even number in the list and the smallest odd number in the list. 
For example, if you pass [1,2,4,6] as an argument the function should return 6 - 1= 5.
'''

def odd_even(arr):
    odd_val = [el for el in arr if el % 2 != 0]
    even_val = [el for el in arr if el % 2 == 0]
    largest_even = max(even_val)
    smallest_odd = min(odd_val)
    print(f"{largest_even} - {smallest_odd} = {largest_even - smallest_odd}")

odd_even(arr = [1,2,4,6])