# Day 6

## User Name Generator

'''
Write a function called user_name that generates a username from the user's email. The code should ask the user to input an email and the code should return everything before the @ sign as their user name. 
For example, if someone enters ben@gmail.com, the code should return ben as their user name. 
'''

def user_name(user_email):
    splitted_email = user_email.split('@')
    user_name = splitted_email[0]
    return user_name


user_email = input("What's your e-mail? ")
print(f"Your User Name is: {user_name(user_email)}")