###################
## Valid Anagram ##
###################

# Given two strings s and t, return true if t is an anagram of s, and false.
#
# Example 1
# Input: s = "anagram", t ="nagaram"
# Output: true
# 
# Example 2
# Input s = "rat", t = "car"
# Output: false

def valid_anagram(s: str, t: str) -> bool:
    char_dict = {}
    for letter in s:
        if letter in char_dict:
            char_dict[letter] += 1
        else:
            char_dict[letter] = 1
    for letter in t:
        if letter not in char_dict:
            return False
        if letter in char_dict:
            char_dict[letter] -= 1
            if char_dict[letter] < 0:
                return False
    return True

print(valid_anagram("anagram", "nagaram"))

print(valid_anagram("bbcc", "ccbc"))

print(valid_anagram("anagra", "nagaraa"))


#####################################
# Other solution

def is_anagram(s:str, t:str) -> bool:
    # If lengths are different, strings can't be anagrams
    if len(s) != len(t):
        return False
    
    # Dictionary to store character frequencies 
    char_count = {}

    # Count frequencies of characters in both strings
    for i in range(len(s)):
        char_count[s[i]] = char_count.get(s[i], 0) + 1
        char_count[s[i]] = char_count.get(t[i], 0) - 1
    
    # Check if all frequencies are zeros
    return all(count == 0 for count in char_count.values())


# print(is_anagram("anagram", "nagaram"))

# print(is_anagram("cat", "car"))

# print(is_anagram("anagra", "nagaraa"))

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    letter_count_dict = {}
    for letter in s:
        if letter in letter_count_dict.keys():
            letter_count_dict[letter] += 1
        else:
            letter_count_dict[letter] = 1
    for letter in t:
        if letter in letter_count_dict.keys():
            letter_count_dict[letter] -= 1
            if letter_count_dict[letter] < 0:
                return False
        else: 
            return False
    return sum(letter_count_dict.values()) == 0

print(isAnagram("bbcc", "ccbc"))