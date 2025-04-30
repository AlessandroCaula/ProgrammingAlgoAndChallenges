########################
## Shuffled Properly? ##
########################

# Given an array of 10 numbers, return whether or not the array is shuffled enough. 
# 
# In this case, if 3 or more numbers appear consecutively (ascending or descending), return false.
# 
# 
# Examples
# 
# isShuffledWell([1, 2, 3, 5, 8, 6, 9, 10, 7, 4])
# output = false
# # 1, 2, 3 appear consecutively
# 
# isShuffledWell([3, 5, 1, 9, 8, 7, 6, 4, 2, 10])
# output = false
# # 9, 8, 7, 6 appear consecutively
# 
# isShuffledWell([1, 5, 3, 8, 10, 2, 7, 6, 4, 9])
# output = true
# # No consecutive numbers appear

# isShuffledWell([1, 3, 5, 7, 9, 2, 4, 6, 8, 10])
# output = true
# # No consecutive numbers appear

def isShuffledWell(nums: list[int]) -> bool:
    for i in range(2, len(nums)):
        if nums[i - 1] == nums[i] - 1:
            if nums[i - 2] == nums[i - 1] - 1:
                return False
        if nums[i - 1] == nums[i] + 1:
            if nums[i - 2] == nums[i - 1] + 1:
                return False
    return True

print(isShuffledWell([1, 2, 3, 5, 8, 6, 9, 10, 7, 4]))
print(isShuffledWell([3, 5, 1, 9, 8, 7, 6, 4, 2, 10]))
print(isShuffledWell([1, 5, 3, 8, 10, 2, 7, 6, 4, 9]))
print(isShuffledWell([1, 3, 5, 7, 9, 2, 4, 6, 8, 10]))