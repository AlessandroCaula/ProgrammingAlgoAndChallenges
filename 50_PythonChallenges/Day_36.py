# Day 36

## Count String

'''
Write a function called count that takes one argument a string, and returns a dictionary of how many times each element appears in the string. 
For example 'hello' should return:
{'h':1,'e': 1,'l':2, 'o':1}
'''

def count(string):
    dict_count = {}
    for let in string:
        if let not in dict_count.keys():
            dict_count[let] = 1
        else:
            dict_count[let] += 1
    return dict_count

string = 'hello'
print(count(string))