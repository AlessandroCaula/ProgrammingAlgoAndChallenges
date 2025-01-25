# TWO SUM

# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
# Return the answer with the smaller index first.

# Example 1
# Input: nums = [3,4,5,6], target = 7
# Output: [0,1]
# Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

def twoSum(nums: list[int], target: int) -> list[int]:
    for i, el in enumerate(nums):
        # Compute the difference between the current number at the ith position and the target.
        difference = target - el
        # Check if the difference number is present in the other element of the list. 
        for j in range(len(nums[i+1:])):
            pp = nums[i+j+1]
            if nums[i+j+1] == difference:
                return [i, i+j+1]
    return False

# print(twoSum([3,4,5,6], 7))
print(twoSum([4,5,6], 10))

# Other Solution

def twoSum1(nums: list[int], target: int) -> list[int]:
    difference_list = {} # val -> index
    for i, el in enumerate(nums):
        difference_list[target - el] = i 
    for j, diff in enumerate(difference_list):
        if diff in nums:
            return ([i, j] if i < j else [j, i])
    return False
# ß
# print(twoSum1([3,4,5,6], 7))
print(twoSum1([4,5,6], 10))

# Other Solution -- Best one

def twoSum2(nums: list[int], target: int) -> list[int]:
    prevMap = {} # val -> index

    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i

# print(twoSum2([3,4,5,6], 7))
print(twoSum2([4,5,6], 10))