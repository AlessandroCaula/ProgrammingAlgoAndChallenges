######################
## Next in alphabet ##
######################

# Create a function which returns the next letters alphabetically in a given string. If the last letter is a "Z", change the rest of the letters accordingly.
# 
# Examples:
# 
# next_letters("A")
# output = "B"
# "A" becomes "B" - simple increment.
# 
# next_letters("ABC")
# output = "ABD"
# "C" becomes "D" - last character changes without carry.
# 
# next_letters("Z")
# output = "AA"
# "Z" rolls over to "A", and since there's no previous letter, we add a new "A"
# Think of it like 9 + 1 = 10, here Z + 1 = AA
# 
# next_letters("CAZ")
# output = "CBA"
# "Z" -> "A" (carry), "A" -> "B" (no carry). So "CAZ" becomes "CBA"
# Like incrementing 129 -> 130 but in letters
# 
# next_letters("")
# output = "A"
# Empty input is treated as 0 -> return "A"
# 
# 
# NOTES
# - Tests will all be in CAPITALS
# - Think about the letter "Z" like the number 9 and how it carries over to increment the next letter/digit over

import string 

def next_letters(letters):
    alphabet = list(string.ascii_uppercase)
    letters = letters.upper()
    letters_list = [let for let in letters]

    carry = False
    for i, let in enumerate(letters_list[::-1]):
        # Invert the index i
        idx = len(letters_list) - 1 - i
        if let == "Z":
            letters_list[idx] = "A"
            carry = True
        else:
            if carry == True:
                letters_list[idx] = alphabet[alphabet.index(let) + 1]
                carry = False
            else:
                if idx == len(letters_list) - 1:
                    letters_list[idx] = alphabet[alphabet.index(let) + 1]
    
    # Add an A at the beginning of the string if there is still a carry value to deal with 
    if carry == True or len(letters_list) == 0:
        letters_list.insert(0, "A")

    return "".join(letters_list)

print(next_letters("ABC"))
print(next_letters("CAZ"))
print(next_letters("Z"))
print(next_letters("A"))
print(next_letters(""))
