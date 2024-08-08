# Day 21

## List of Tuples

'''
Write a function called make_tuples that takes two lists, equal lists, and combines them into a list of tuples. 
For example if list a is [1,2,3,4] and list b is [5,6,7,8], your function should return [(1,5),(2,6),(3,7),(4,8)].
'''

def make_tuples(list_a, list_b):
    final_list_of_tuple = []
    for i in range(len(list_a)):
        tup = (list_a[i], list_b[i])
        final_list_of_tuple.append(tup)
    
    return final_list_of_tuple

print(make_tuples([1,2,3,4], [5,6,7,8]))