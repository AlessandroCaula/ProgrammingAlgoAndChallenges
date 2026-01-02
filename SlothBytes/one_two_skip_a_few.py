############################
### One, Two, Skip a Few ###
############################

"""
Create a function which calculates how many numbers are missing from
an ordered number line.

This number line starts at the first value of the array, and increases by 1 to the end of the number line, ending at the last value of the array. 

Examples

howManyMissing([1, 2, 3, 8, 9])
output = 4
# The numbers missing from this line are 4, 5, 6, and 7.
# 4 numbers are missing.
howManyMissing([1, 3])
output = 1

howManyMissing([7, 10, 11, 12])
output = 2

howManyMissing([1, 3, 5, 7, 9, 11])
output = 5

howManyMissing([5, 6, 7, 8])
output = 0
"""


def how_many_missing(nums: [int]):
    all_nums = nums[len(nums) - 1] - nums[0]
    act_nums = len(nums) - 1
    return all_nums - act_nums


print(how_many_missing([2, 3, 8, 9]))
print(how_many_missing([7, 10, 11, 12]))
print(how_many_missing([1, 3, 5, 7, 9, 11]))
print(how_many_missing([5, 6, 7, 8]))
