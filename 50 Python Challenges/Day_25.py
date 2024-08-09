# Day 25

## All the Same

'''
Create a function all_the_same that takes one argument, a string, a list, or a tuple and checks if all the elements are the same.
If the elements are the same, the function should return True. If not, it should return Fales. 
For example, ['Mary', 'Mary', Mary'] should return True.
'''

def all_the_same(collection):        
    return collection.count(collection[0]) == len(collection)


print(all_the_same(['mary', 'luca', 'mary', 'mary']))


## Other solutions

'''
We can use the in-built all() function. The all() function will return True if all the elements of iterable are true.
'''

def all_the_same1(collection):
    are_the_same = all(i == collection[0] for i in collection)
    return are_the_same

print(all_the_same1(['mary', 'luca', 'mary', 'mary']))


'''
We can also use the built-in enumerate() function. The enumerate function will return an item and its index. We can use to check if all the items in the string, tuple or listst are equal to the item sitting at index 0.
'''

def all_the_same2(collection):
    are_the_same = True
    for i, item in enumerate(collection):
        if collection[i] != collection[0]:
            are_the_same = False
    return are_the_same

print(all_the_same2(['mary', 'luca', 'mary', 'mary']))

