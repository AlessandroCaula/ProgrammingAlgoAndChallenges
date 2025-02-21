#############################
## Phone Number Formatting ##
#############################

# Create a function that takes a list of 10 numbers (between 0 and 9) and returns a string of those numbers formatted as a phone number (e.g. (555) 555-5555 ).
# 
# Examples
# 
# format_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
# output = "(123) 456-7890"
# 
# format_phone_number([5, 1, 9, 5, 5, 5, 4, 4, 6, 8])
# output = "(519) 555-4468"
# 
# format_phone_number([3, 4, 5, 5, 0, 1, 2, 5, 2, 7])
# output = "(345) 501-2527"

def format_phone_number(numbers: list):
    string_phone_number = '('

    for i, number in enumerate(numbers):
        if i == 3:
            string_phone_number += ') '
        if i == 6:
            string_phone_number += "-"
        string_phone_number += str(number)

    return string_phone_number

print(format_phone_number([5, 1, 9, 5, 5, 5, 4, 4, 6, 8]))
print(format_phone_number([3, 4, 5, 5, 0, 1, 2, 5, 2, 7]))
print(format_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))