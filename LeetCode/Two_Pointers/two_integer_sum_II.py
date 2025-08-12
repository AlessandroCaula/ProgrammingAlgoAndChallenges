########################
## Two Integer Sum II ##
########################

# Given an array of integers numbers that is sorted in non-decreasing order.
# 
# Return the indices (1-indexes) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2.
# Note that index1 and index2 cannot be equal, therefore you may not use the same element twice. 
# 
# There will always be exactly on valid solution.
# 
# Your solution must use O(1) additional space
# 
# Example:
# 
# Input: numbers = [1,2,3,4], target = 3
# Output: [1,2]
# 
# Explanation:
# The sum of 1 and 2 is 3. Since we are assuming a 1-indexed array, index1 = 1, index2 = 2. We return [1,2]

def two_integer_sum(numbers: list[int], target: int) -> list[int]:
    i = 0
    j = 1
    
    while i < len(numbers):
        if j == len(numbers):
            i += 1
            j = i + 1
        else:
            # check if the two number sums to the target
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
            else:
                j += 1    
    return []

numbers = [1,2,3,4]
target = 7
print(two_integer_sum(numbers, target))

# Time complexity: O(n^2)
# Space complexity: O(1)


###################
## Binary Search

def two_integer_sum1(numbers: list[int], target: int) -> list[int]:
    
    for i in range(len(numbers)):
        l, r = i + 1, len(numbers) - 1
        tmp = target - numbers[i]

        while l <= r:
            mid = l + (r - l) // 2
            if numbers[mid] == tmp:
                return [i + 1, mid + 1]
            elif numbers[mid] < tmp:
                l = mid + 1
            else:
                r = mid - 1
    return []

numbers = [1,2,3,4]
target = 7
print(two_integer_sum1(numbers, target))

# Time complexity: O(n log n)
# Space complexity: O(1)


###################
## Hash Map

def two_integer_sum2(numbers: list[int], target: int) -> list[int]:
    mp = defaultdict(int)
    for i in range(len(numbers)):
        tmp = target - numbers[i]
        if mp[tmp]:
            return [mp[tmp], i + 1]
        mp[numbers[i]] = i + 1

    return []

# Time complexity: O(n)
# Space complexity: O(n)


###################
## Two pointers

def two_integer_sum3(numbers: list[int], target: int) -> list[int]:
    l, r = 0, len(numbers) - 1

    while l < r:
        curSum = numbers[l] + numbers[r]

        if curSum > target:
            r -= 1
        elif curSum < target:
            l += 1
        else:
            return [l + 1, r + 1]

    return []

# Time complexity: O(n)
# Space complexity: O(1)