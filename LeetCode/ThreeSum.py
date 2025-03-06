# Given an integer array nums, return all the triples [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# 
# Notice that the solution set must not contain duplicate triplets. 
# 
# Example 1:
# 
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 0 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
#
# The distinct triplets are [-1,0,1] and [-1,-1,2]
#
# Example2:
#
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.

# To solve this problem, we will sort the array first. This will help us avoid duplicates. It would also enable us to use the two pointer approach. Let's explain this in more detail. 
#
# The idea is to iterate the array and then find two other elements that sum up to -nums[i]. This would mean that nums[i] plus these two numbers would be 0. This will give us a valid triplet for the answer. 
# 
# We will use the 'twoSum function to find these two number we would only look for the numbers to the right of the nums[i] to avoid duplicates. Since the array is sorted, we can use two pointer to find the number efficiently. 
# 
# Sorting has a time complexity of O(n log n). Nested for loops have a time complexity of O(n^2). Since O(n^2) is bigger than O(n log n), overall time complexity is O(n^2).

def three_sum(nums: list):
    # Find two nums that sum to target starting at left
    def two_sum(nums, target, left):
        i, j = left, len(nums) - 1
        result = []
        while i < j:
            # Skip duplicates
            if nums[i] == nums[i-1] and i != left:
                i += 1
            # If sum is less than target
            elif nums[i] + nums[j] < target:
                # Increment left pointer to increase sum (array is sorted) 
                i += 1
            # If sum is more than target
            elif nums[i] + nums[j] > target:
                # Decrement right pointer to reduce sum (array is sorted)
                j -= 1
            # Otherwise, add to the result
            else:
                result.append((i, j))
                i += 1
                j -= 1
        return result

    answer = []
    # Sort nums 
    nums = sorted(nums)
    for i in range(len(nums)):
        # Skip duplicates
        if i > 0 and nums[i] == nums[i-1]:
            continue
        # Call twoSum with target as -nums[i]
        # Only look on the right side of i
        for j, k in two_sum(nums, -nums[i], i+1):
            answer.append((nums[i], nums[j], nums[k]))
    return answer

print(three_sum([-1,0,1,2,-1,-4]))