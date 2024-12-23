# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

def lengthOfLongestSubstring(s: str):
    longest_substring = ""
    local_substring = ""
    for i in range(len(s)):
        if len(local_substring) > len(longest_substring):
            longest_substring = local_substring
        local_substring = s[i]
        for el in s[i + 1:]:
            b = len(s) - 1
            if el in local_substring:
                if len(local_substring) > len(longest_substring):
                    longest_substring = local_substring
                break
            else:
                local_substring += el
    if longest_substring == "":
        longest_substring = s
    return (longest_substring, len(longest_substring))
        
# print(lengthOfLongestSubstring("abcabcbb"))
# print(lengthOfLongestSubstring("pwwkew"))
# print(lengthOfLongestSubstring("c"))
# print(lengthOfLongestSubstring("au"))
print(lengthOfLongestSubstring("aab"))