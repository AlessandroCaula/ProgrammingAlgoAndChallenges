###################################
## Sherlock and the Valid String ##
###################################

## 15 July 2025 ##

# Sherlock considers a string to be valid if all characters of the string appear the same number of times. 
# It is also valid if he can remove just one character at one index in the string s, and the remaining characters will occur the same number of times. 

# Given a string, determine if it is valid. If so, return "YES", otherwise return "NO".

## EXAMPLE
#
# isValid("abc")
# output = "YES"
# This is a valid string because frequencies are { a: 1, b: 1, c: 1 }
# 
# isValid("abcc")
# output = "YES"
# This is a valid string because we can remove one c and have one of each character in the remaining string. 
# 
# isValid("abccc")
# output = "NO"
# This string is not valid as even if we remove once c. 
# It still leaves character frequencies of: { a: 1, b: 1, c: 2 }
# 
# isValid("aabbcd")
# output = "NO"

# isValid("aabbccddeefghi")
# output = "NO"

# isValid("abcdefghhgfedecba")
# output = "YES"

from collections import defaultdict

def is_valid(valid_string: str) -> bool:
    # compute the count for each of the letters
    let_counts = defaultdict(int)
    for l in valid_string:
        let_counts[l] += 1

    let_counts_list = list(let_counts.values())
    let_counts_set = set(let_counts_list)

    if len(let_counts_set) == 1:
        return True
    
    # Find the max and min values
    max_val = max(let_counts_set)
    min_val = min(let_counts_set)
    # Check if the max value occurs just once and if that by subtracting 1 to it it is equal to the min value
    if let_counts_list.count(max_val) == 1 and max_val - 1 == min_val:
        return True

    return False

sherlock_string = "abccc"
print(is_valid(sherlock_string))
sherlock_string = "abcc"
print(is_valid(sherlock_string))
sherlock_string = "aabbcd"
print(is_valid(sherlock_string))
sherlock_string = "abcdefghhgfedecba"
print(is_valid(sherlock_string))
sherlock_string = "aabbccddeefghi"
print(is_valid(sherlock_string))