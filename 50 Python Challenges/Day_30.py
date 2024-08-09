# Day 30

## Most Repeated Name

'''
Write a function called repeated_name that finds the most repeated name in the following list. 
name = ["John", "Peter", "John", "Peter", "Jones", "Peter"]
'''

def repeated_name(name_collection):
    repetition = {}
    for name in name_collection:
        if name not in repetition.keys():
            repetition[name] = 1
        else:
            repetition[name] += 1
    return f"The most repeated name is: {sorted(repetition, key= lambda x: x[1])[0]}"

print(repeated_name(["John", "Peter", "John", "Peter", "Jones", "Peter"]))


## Other solution
'''
The collection module has a counter() class that we can use to find the most common element of a list. The function most_common() returns a list of the n most common elements and their counts from a collection sorted by frequency.
'''
from collections import Counter

def repeated_name1(name_collection):
    return max(Counter(name_collection).most_common())

print(repeated_name1(["John", "Peter", "John", "Peter", "Jones", "Peter"]))


## Extra Challenge: Sort by Last Name

'''
You work for a local school in your area. The school has a list of names of students saved in a list. The school has asked you to write a program that takes a list of names and sorts them alphabetically. 
The names should be sorted by last names. Here is a list of names: 

['Beyonce Knowles', 'Alicia Keys', 'Katie Perry', 'Chris Brown','Tom Cruise']

Your code should not just sort them alphabetically, but it should also switch the names (the last name must be the first). Here is how your code output should look: 

['Brown Chris', 'Cruise Tom', 'Keys Alicia', 'Perry Katie', 'Knowles Beyonce'] 

Write a function called sorted_names.
'''

def sorted_names(names):
    # list comprehension for changing the surname with the name of the names sorted by surname. 
    names_sort = [name.split()[1] + " " + name.split()[0] for name in sorted(names, key = lambda x : x.split()[1])]
    return names_sort
    
print(sorted_names(['Beyonce Knowles', 'Alicia Keys', 'Katie Perry', 'Chris Brown','Tom Cruise']))