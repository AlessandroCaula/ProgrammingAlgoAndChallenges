######################
# Challenge 02/07/2024
######################

# Normal Binary Search
def binary_search(arr, target):
    first_target_idx = -1; 
    first = 0
    last = len(arr) - 1
    while (first <= last):
        mid = (first + last) // 2
        if (target == arr[mid]):
            first_target_idx = mid
            break
        else:
            if (target < arr[mid]):
                last = mid - 1
            else:
                first = mid + 1
    return first_target_idx

arr = [1, 2, 3, 4, 5, 6, 7, 8]
target = 9

if (binary_search(arr, target) == -1):
    print("Element not found")
else:
    print("Element found at index: " + str(binary_search(arr, target)))

# Given a sorted array of integers and a target integer, find the first occurrence of the target and return its index.
# Return -1 if the target is not in the array.
# #Input:
# 
# arr = [1, 3, 3, 3, 3, 6, 10, 10, 10, 100]
# 
# target = 3
# 
# find_first_occurrence(arr,target) # Return 1
# 
# #Explanation: The first occurrence of 3 is at index 1.

# #Input:
# 
# arr = [2, 3, 5, 7, 11, 13, 17, 19]
# 
# target = 6
# find_first_occurrence(arr,target) # Return -1
# 
# #Explanation: 6 does not exist in the array.

def find_first_occurrence(arr, target):
    first = 0
    last = len(arr) - 1
    while (first <= last):
        mid = (first + last) // 2
        # If the target is equal to the current mid element.
        if (target == arr[mid]):
            # Check backword if it is the first occurrence in the array.
            while (mid != -1 and target == arr[mid]):
                mid -= 1
            return mid + 1
        else:
            if (target < arr[mid]):
                last = mid - 1
            else:
                first = mid + 1
    return -1

arr = [1, 3, 3, 3, 3, 6, 10, 10, 10, 100]
target = 3

if (find_first_occurrence(arr, target) == -1):
    print("Element not found")
else:
    print("Element found at index: " + str(find_first_occurrence(arr, target)))
