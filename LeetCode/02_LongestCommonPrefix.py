# Write a function to find the longest common prefix string amongst an array of strings.
# 
# If there is no common prefix, return an empty string "".
# 
#  
# 
# Example 1:
# 
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:
# 
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

def longestCommonPrefix(strs: list[str]) -> str:
    longest_pref = ""
    first_string = strs[0]
    for i in range(len(first_string)):
        for other_string in strs[1:]:
            if first_string[:i + 1] != other_string[:i + 1]:
                return longest_pref
        longest_pref = first_string[:i + 1]
    return longest_pref


print(longestCommonPrefix(strs = ["flower","flow","flight"]))
