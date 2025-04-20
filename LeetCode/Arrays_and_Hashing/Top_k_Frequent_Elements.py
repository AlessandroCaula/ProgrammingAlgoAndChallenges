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

def top_k_frequent_elements(nums: list[int], k: int) -> list[int]:
    nums_count = defaultdict(int)
    for num in nums:
        nums_count[num] += 1
    sorted_nums = sorted(nums_count.items(), key=lambda x:x[1], reverse=True)
    return [sorted_nums[i][0] for i in range(k)]

print(top_k_frequent_elements([1,2,2,3,3,3,3], 2))

##########################
# 
#### Min-Heap Solution
# 
# Min heap is a binary tree (usually implemented as an array) where:
# 
# 1. Heap Property: Every parent node is less than or equal to it's children. 
#   -> This ensures the smallest element is always at the root
# 2. Complete Binary Tree: All levels are filled from left to right, except possibly the last level
#        2
#       / \
#      3   4
#     / \  
#    5   6
# 
# Same Min Heap as Array: [2, 3, 4, 5, 6]
# 
import heapq
def top_k_frequent_elements1(nums: list[int], k:int) -> list[int]:
    count = {}
    for num in nums:
        count[num] = 1 + count.get(num, 0)

    heap = []
    for num in count.keys():
        heapq.heappush(heap, (count[num], num))
        if len(heap) > k:
            heapq.heappop(heap)

    res = []
    for i in range(k):
        res.append(heapq.heappop(heap)[1])
    
    return res

print(top_k_frequent_elements1([1,2,2,3,3,3,3], 2))

# Time complexity: O(n log k) -> Where n is the length of the array and k is the number of top frequent elements


##########################
# 
#### Bucket Sort
# 
def top_k_frequent_elements2(nums: list[int], k:int) -> list[int]:
    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for num in nums:
        count[num] = 1 + count.get(num, 0)

    for num, cnt in count.items():
        freq[cnt].append(num)

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for num in freq[i]:
            res.append(num)
            if len(res) == k:
                return res 

print(top_k_frequent_elements2([1,2,2,3,3,3,3], 2))

# Time complexity: O(n)