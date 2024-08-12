# Day 2

## Strings to Integers

'''
Write a function called convert_add that takes a list of strings as an argument and convers it to integers and sums the list.
For example ['1', '3', '5'] should be converted to [1, 3, 5] and summed to 9.
'''

def convert_add(arr):
    final_sum = 0
    for val in arr:
        if val.isdigit():
            final_sum += int(val)
    return final_sum

arr = ['1', '3', '5']
print(f"Final sum: {convert_add(arr)}") 