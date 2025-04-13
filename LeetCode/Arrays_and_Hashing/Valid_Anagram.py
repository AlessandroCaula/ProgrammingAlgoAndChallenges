# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1
# 
# Input: s = "racecar", t = "carrace"

# Output: true

# Example 2
# 
# Input: s = "jar", t = "jam"

# Output: false

def isAnagram(s: str, t: str) -> bool:
    s_dict = {}
    t_dict = {}
    for let in s: 
        if let in s_dict.keys():
            s_dict[let] += 1
        else:
            s_dict[let] = 1
    for let in t:
        if let in t_dict.keys():
            t_dict[let] += 1
        else:
            t_dict[let] = 1
    
    return s_dict == t_dict

print(isAnagram(s = "racecar", t = "carrace"))
print(isAnagram(s = "jar", t = "jam"))

def isAnagram1(s: str, t: str) -> bool:
    s_dict = {}
    t_dict = {}
    for let in s: 
        s_dict[let] = s_dict.get(let, 0) + 1
    for let in t:
        t_dict[let] = t_dict.get(let, 0) + 1
    
    return s_dict == t_dict

print(isAnagram1(s = "racecar", t = "carrace"))
print(isAnagram1(s = "jar", t = "jam"))