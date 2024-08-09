# Day 32

## Password Validator

'''
Write a function called password_validator. The function asks the user to enter a password. A valid password should have at least one upper letter, one lower letter, and one number. 
It should not be less than 8 characters long. When the user enters a password, the function should check if the password is valid. If the password is valid, the function should return the valid password. 
If the password is not valid, the function should tell the users the errors in the password and prompt the user to enter another password. The code should only stop once the user enters a valid password.
'''

def password_validator():
    is_valid = False
    while not is_valid:
        password = input("Password: ")
        is_valid = True
        # Validate the password
        # Check length
        if len(password) < 8:
            print("Password should have at least 8 characters.")
            is_valid = False
        # Check upper letter.
        has_upper = not all(letter.islower() for letter in [letters for letters in password if not letters.isdigit()])
        if not has_upper:
            print("Password should contains at least one upper letter")
            is_valid = False
        # Check lower letter.
        has_lower = not all(letter.isupper() for letter in [letters for letters in password if not letters.isdigit()])
        if not has_lower:
            print("Password should contains at least one lower letter")
            is_valid = False
        has_digit = not all(letter.isalpha() for letter in password)
        if not has_digit:
            print("Password should contains at least one digit")
            is_valid = False
    print("Valid password")

password_validator()