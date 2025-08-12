######################
## Valid Palindrome ##
######################

# Given a string s, return true if it is a palindrome, otherwise return false.
# 
# A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.
# 
# Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9)
# 
# Example 1:
# 
# Input: s = "Was it a car or a cat I saw?"
# Output: true

def valid_palindrome(s: str) -> bool:
    # Cleaning the text
    cleaned_s = ''.join(char for char in s if char.isalnum())
    cleaned_s = cleaned_s.lower()

    return cleaned_s == cleaned_s[::-1]

palindrome = "Was it a car or a cat I saw?"
print(valid_palindrome(palindrome))
palindrome = "tab a cat"
print(valid_palindrome(palindrome))