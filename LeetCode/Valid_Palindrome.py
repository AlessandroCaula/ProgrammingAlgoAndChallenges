# Valid Palindrome

# Given a string s, return true if it is a palindrome, otherwise return false.
# A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

# Example 1:

# Input: s = "Was it a car or a cat I saw?"
# Output: true

def isPalindrome(s: str) -> bool:
    alnum_s = ""
    for ch in s:
        if ch.isalnum():
            alnum_s += ch.lower()
    alnum_s_opposite = ""
    for ch in s[::-1]:
        if ch.isalnum():
            alnum_s_opposite += ch.lower()
    return alnum_s == alnum_s_opposite

print(isPalindrome("Was it a car or a cat I saw?"))

# Other solution

def isPalindrome1(s: str) -> bool:
    alnum_s = ""
    for ch in s:
        if ch.isalnum():
            alnum_s += ch.lower()
    return alnum_s == alnum_s[::-1]

print(isPalindrome1("Was it a car or a cat I saw?")) 