# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# 
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# 
# You can return the answer in any order.
# 
#  
# 
# Example 1:
# 
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
# 
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:
# 
# Input: nums = [3,3], target = 6
# Output: [0,1]


### Not Optimezed Solution 

def twoSum(nums: list[int], target: int) -> list[int]:
    for i, el in enumerate(nums):
        el_to_find = target - el
        for j, el1 in enumerate(nums[i + 1:]):
            if el1 == el_to_find:
                return [i, j + i + 1]
            
print(twoSum(nums = [3, 2, 4], target = 6))


### Optimized Solution

def twoSum(nums: list[int], target: int) -> list[int]:
    numToIndex = {}
    for i, el in enumerate(nums):
        # if the result of the subtraction target - el have already been seen in the array, it is stored in the hash table
        if target - el in numToIndex:
            return [numToIndex[target - el], i]
        numToIndex[el] = i
            
print(twoSum(nums = [3, 2, 4], target = 6))