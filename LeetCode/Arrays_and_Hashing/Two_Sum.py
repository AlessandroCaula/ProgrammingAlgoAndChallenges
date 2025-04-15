# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

# Return the answer with the smaller index first.

# Example 1:
# 
# Input: 
# nums = [3,4,5,6], target = 7
# 
# Output: [0,1]

# Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

def twoSum(nums: list[int], target: int) -> list[int]:
    hash_map = {}
    for i, el in enumerate(nums):
        diff = target - el
        # Check if the diff is in the dictionary 
        if hash_map.get(diff) is not None and hash_map[diff] != i:
            return [hash_map[diff], i]
        hash_map[el] = i

print(twoSum([3,4,5,6], 7))


def twoSum1(nums: list[int], target:int) -> list[int]:
    h = {}
    for i, num in enumerate(nums):
        h[nums] = i
    
    for i, num in enumerate(nums):
        desired = target - num
        if desired in h and h[desired] != i:
            return [i, h[desired]]