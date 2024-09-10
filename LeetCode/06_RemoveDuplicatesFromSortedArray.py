# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. 
# Then return the number of unique elements in nums.
# 
# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
# 
# - Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# - Return k.
# 
# Example 1:
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# 
# Example 2:
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Solution in-place
def removeDuplicates(nums):
    unique_idx = 0
    unique_el_count = 0
    for i, el in enumerate(nums):
        if (i == 0):
            curr_el = el
            unique_idx += 1
            unique_el_count += 1
            continue
        if el == curr_el:
            nums[i] = "_"
        else:
            nums[unique_idx] = nums[i]
            curr_el = nums[i]                
            if i != unique_idx:       
                nums[i] = "_"  
            unique_idx += 1        
            unique_el_count += 1    
    return (nums, unique_el_count, nums[:unique_el_count])


nums = [1, 1, 2]
nums = [0,0,1,1,1,2,2,3,3,4]
#nums = [1, 2]
print(removeDuplicates(nums))


# Solution not in-place. Just by using a set.
def removeDuplicates1(nums):
    unique = set()
    for el in nums:
        unique.add(el)
    return unique

nums = [1, 1, 2]
nums = [0,0,1,1,1,2,2,3,3,4]
#nums = [1, 2]
print(removeDuplicates1(nums))


# Another in-place solution. 
def removeDuplicates2(nums):
    idx = 0
    for i in range(1, len(nums)):
        if nums[idx] == nums[i]:
            continue
        idx += 1
        nums[idx] = nums[i]  
    # if needed fill all the remaining places with "_"
    for i in range(idx + 1, len(nums)): nums[i] = "_"

    return (nums, idx + 1)

nums = [1, 1, 2]
nums = [0,0,1,1,1,2,2,3,3,4]
#nums = [1, 2]
print(removeDuplicates2(nums))