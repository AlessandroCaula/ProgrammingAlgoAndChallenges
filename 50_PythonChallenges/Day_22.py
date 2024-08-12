#Day 22

## Add Under_Score

'''
Create three functions. The first called add_hash takes a string and adds a hash # between the words. The second function called add_underscore removes the hash(#) and replaces it with an underscore ( _ ) 
The third function called remove_underscore, removes the underscore and replaces it with nothing. if you pass ‘Python’ as an argument for the three functions, and you call them at the same time like: 
print(remove_underscore(add_underscore(add_hash('Python')))) it should return ‘Python’. 
'''

def add_ash(string):
    string = string.replace(" ", "#")
    return string

def add_underscore(string):
    string = string.replace("#", "_")
    return string

def remove_underscore(string):
    string = string.replace("_", " ")
    return string

print(remove_underscore(add_underscore(add_ash("Ciao come va?"))))