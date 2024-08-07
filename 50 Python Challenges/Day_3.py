# Day 3

## Register Check

'''
Write a function called register_check that checks how many students are in school. The function takes a dictionary as a parameter. If the student is in school, the dictionary as a parameter. 
If the student is in school, the dictionary says 'yes'. If the student is not in school, the ditionary says 'no'. Your function should return the number of students in school. 
'''

def register_check(register):
    count = 0
    for present in register.values():
        if present == 'yes':
            count += 1
    return count


register = {'Michael': 'yes', 'John': 'no', 'Peter': 'yes', 'Mary': 'yes'} 
print(f"Number of students in school: {register_check(register)}")