######################
## Majority Element ##
######################

# Given an array nums of size n, return the majority element. 
# 
# The majority element is the element that appears more than [n / 2] times. You may assume that the majority element always exists in the array. 

# Example 1:
# input: nums = [3, 2, 3]
# output: 3

# Example 2:
# input: nums = [2, 2, 1, 1, 1, 2, 2]
# output: 2

def majority_element(nums: list) -> int:
    # Compute first the half length of the array.
    half_length = len(nums) / 2
    # Create a set collection that will store a unique element avoiding repetitions. 
    unique_nums = set(nums)
    # Loop through all the unique_nums and count their occurrences in the original nums collection. 
    for el in unique_nums:
        el_count = nums.count(el)
        # If the count of the current element is higher than [n / 2] we can return it. 
        if el_count > half_length:
            return el        
    return -1


nums = [2, 2, 1, 1, 1, 2, 2]
print(majority_element(nums))


###### Other possible solution
# 
# This one assuming that there are always only 2 different elements (numbers) in the list.

def majorityELement(nums):
    # Initialize count and candidate
    count = 0
    candidate = None
    
    # Boyer-Moore Voting Algorithm
    for num in nums:
        # If count is 0, pick new candidate
        if count == 0:
            candidate = num
        
        # Update count based on whether we see candidate or different number
        count += 1 if num == candidate else -1
    
    # Return the majority element
    return candidate

nums = [2, 2, 1, 1, 1, 2, 2]
print(majorityELement(nums))