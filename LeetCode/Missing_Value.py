# arr = n - 1 el  (unique)  1 -> n

arr = [1, 2] # -> 3 is missing
arr = [1, 3] # -> 2 is missing

def missing_val(arr):
    length = len(arr)
    for i in range(1, length + 1):
        if i not in arr:
            return i

# Time complexity: O (n^2) 
# Space complexity: O (1) 

def missing_val(arr):
    arr_sum = sum(range(1 , len(arr) + 1))
    for i in arr:
        arr_sum -= i
    return arr_sum

# Time complexity: O(n)
# Space complexity: O(1)

