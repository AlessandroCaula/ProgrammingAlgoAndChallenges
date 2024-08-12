# Day 16

## Sum the List

'''
Write a function called sum_list with one parameter that takes a nested list of integers as an argument and returns the sum of the integers. F
or example, if you pass [[2, 4, 5, 6], [2, 3, 5, 6]] as an argument your function should return a sum of 33. 
'''

def sum_list(nested_list):
    final_sum = 0
    for list in nested_list:
        for el in list:
            final_sum += el
    return final_sum

nested_list = [[2, 4, 5, 6], [2, 3, 5, 6]]
print(sum_list(nested_list))