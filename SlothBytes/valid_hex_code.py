####################
## Valid Hex Code ##
####################
# 27-08-2025

# Create a function that determines whether a string is a valid hex code.
# 
# A hex code must begin with a pound key # and is exactly 6 characters in length. 
#
# Each character must be a digit from 0 - 9 or an alphabetic character from A - F. 
# All alphabetic characters may be uppercase or lowercase. 
#
# Examples
# 
# is_valid_hex_code("#CD5C5C")
# output = True

# is_valid_hex_code("#EAECEE")
# output = True

# is_valid_hex_code("#eaecee")
# output = True

# is_valid_hex_code("#CD5C58C")
# output = False
# # Length exceeds 6

# is_valid_hex_code("#CD5C5Z")
# output = False
# # Not all alphabetic characters in A-F

# is_valid_hex_code("#CD5C&C")
# output = False
# # Contains unacceptable character

# is_valid_hex_code("CD5C5C")
# output = False
# # Missing #

def is_valid_hex_code(code: str) -> bool:
    valid_char = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'A', 'B', 'C', 'D', 'E', 'F']

    if code[0] != "#":
        return False
    if len(code[1:]) != 6:
        return False
    for c in code[1:]:
        if c.upper() not in valid_char:
            return False

    return True


print(is_valid_hex_code("#CD5C5C"))
print(is_valid_hex_code("#EAECEE"))
print(is_valid_hex_code("#eaecee"))
print(is_valid_hex_code("#CD5C58C"))
print(is_valid_hex_code("#CD5C5Z"))
print(is_valid_hex_code("CD5C5C"))
print(is_valid_hex_code("#CD5C&C"))