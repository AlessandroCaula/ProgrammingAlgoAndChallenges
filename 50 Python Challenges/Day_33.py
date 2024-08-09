# Day 33

## List Intersection

'''
Write a function called inter_section that takes two lists and finds the intersection (the elements that are present in both lists). The function should return a tuple of intersections. 
Use list comprehension in your solution. Use the lists below. Your function should return (30, 65, 80). 
list1 = [20, 30, 60, 65, 75, 80, 85] 
list2  = [ 42, 30, 80, 65, 68, 88, 95]
'''

def inter_section(a, b):
    intersection_tuple = tuple(el for el in a if el in b)
    return intersection_tuple

print(inter_section([20, 30, 60, 65, 75, 80, 85], [42, 30, 80, 65, 68, 88, 95]))


## Exrta Challenge: Set or List

'''
You want to implement a code that will search for a number in a range. You have a decision to make as to whether to store the number in a set or a list. Your decision will be based on time. 
You have to pick a data type that executes faster. 

You have a range and you can either store it in a set or a list depending on which one executes faster when you are searching for a number in the range. See below: 
a = range(10000000) 
x = set(a) 
y = list(a) 
Let's say you are looking for a number 9999999 in the range above. Search for this number in the list and the set. Your challenge is to find which code executes faster. 
You will pick the one that executes quicker, lists, or sets. Run the two searches and time them.
'''

import time

def select_faster():
    a = range(10000000)
    list_a = list(a)
    set_a = set(a)
    num_to_search = 9999999
    # Check time execution of 9999999 in list.
    start_time_list = time.time()
    for el in list_a:
        if el == num_to_search:
            break
    list_search_time = time.time() - start_time_list
    # Check time execution of 9999999 in set.
    start_time_set = time.time()
    for el in set_a:
        if el == num_to_search:
            break
    set_search_time = time.time() - start_time_set

    print(f"List search: {list_search_time}")
    print(f"Set search: {set_search_time}")

select_faster()


import timeit

# Testing the speed of execution in a set
speed_test = '''
a = range(10000000) 
b = set(a) 
i = 9999999

for i in b :
    print('')
'''
print(timeit.timeit(stmt=speed_test, number=3))

# Testing the speed of execution in a set
speed_test = '''
a = range(10000000) 
b = list(a) 
i = 9999999

for i in b :
    print('')
'''
print(timeit.timeit(stmt=speed_test, number=3))