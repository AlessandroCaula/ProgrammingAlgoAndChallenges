# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

# Example 1:
# 
# Input: nums = [1, 2, 3, 3]

# Output: true


# Example 2:
# 
# Input: nums = [1, 2, 3, 4]

# Output: false


def hasDuplicate(nums: list[int]) -> bool:
    set_nums = set(nums)
    if len(set_nums) == len(nums):
        return False
    else:
        return True

print(hasDuplicate([1, 2, 3, 3]))
print(hasDuplicate([1, 2, 3, 4]))