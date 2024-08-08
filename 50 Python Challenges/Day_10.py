# Day 10

## Hide my Password

'''
Write a function called hide_password that takes no parameters. The function takes an input( a password) from a user and returns a hidden password. 
For example, if the user enters 'hello' as a password the function should return '****' as a password and tell the user that the password is 4 characters long.
'''

def hide_password():
    pssw = input("Insert your password: ")
    print(f"Your password is: {''.join(['*' for el in pssw])} of length: {len(pssw)}")

hide_password()

## Extra Challenge
'''
Your new company has a list of figures saved in a list. The issue is that these numbers have no separator. 
The numbers are saved in the following format: 
[1000000, 2356989, 2354672, 9878098] 

You have been asked to write a code that will convert each of the numbers in the list into a string. Your code should then add a comma on each number as a thousand separator for readability. 
When you run your code on the above list, your output should be : 
['1,000,000', '2,356,989', '2,354,672', '9,878,098']

Write a function called convert_numbers that will take one argument, a list of numbers above.
'''

def convert_numbers(list_int):
    list_to_string = [str('{:,}'.format(val)) for val in list_int]
    return list_to_string

print(convert_numbers([1000000, 2356989, 2354672, 9878098]))