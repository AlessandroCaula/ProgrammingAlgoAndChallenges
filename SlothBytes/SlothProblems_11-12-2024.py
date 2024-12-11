################################################
### Is the Phone Number Formatted Correctly? ###
################################################

# Create a function that accepts a string and returns true if it's in the format of a proper phone number and false if it's not. Assume any number between 0-9 (n the appropriate spots) will produce a valid phone number. 
# 
# This is what a valid phone number looks like:
# 
# (123) 456-7890
# 
# Example:
# 
# isValidPhoneNumber("(123) 456-7890")
# output = True

# isValidPhoneNumber("1111)555 2345")
# output = False

# isValidPhoneNumber("098) 123 4567")
# output = False

def isValidPhoneNumber(number:str) -> bool:
    # Check first if the length is the correct one. 
    if len(number) != 14:
        return False
    # Since the template of a number is always the same I can simply loop all the positions and check if there is something not "allowed".
    for i, c in enumerate(number):
        if i == 0:
            if c != "(": return False
        elif i == 4:
            if c != ")": return False
        elif i == 5:
            if c != " ": return False
        elif i == 9:
            if c != "-": return False
        else:
            if not c.isnumeric():
                return False
    return True
    
    
    
print(isValidPhoneNumber("(123) 456-7890"))

print(isValidPhoneNumber("1111)555 2345"))

print(isValidPhoneNumber("098) 123 4567"))