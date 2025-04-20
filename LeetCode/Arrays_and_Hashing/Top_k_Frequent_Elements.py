#############################
## Top K Frequent Elements ##
#############################

# Given an integer array nums and an integer k, return the k most frequent elements within the array. 

# You may return the output in any order.

# Example 1:
# 
# Input: nums = [1,2,2,3,3,3], k = 2
# Output: [2,3]
#
#
# Example 2:
# Input: nums = [7,7], k = 1
# Output: [7]

from collections import defaultdict

# Solution with time complexity O(n log n)

def top_k_frequent_elements(nums: list, k: int) -> list:
    nums_count = defaultdict(int)
    for num in nums:
        nums_count[num] += 1
    sorted_nums = sorted(nums_count.items(), key=lambda x:x[1], reverse=True)
    return [sorted_nums[i][0] for i in range(k)]

print(top_k_frequent_elements([1,2,2,3,3,3,3], 2))
